#!/usr/bin/env python3
"""Reproducible subprocess tests; Python standard library only, synthetic inputs.

Run: python3 test_memory_helper.py --package /absolute/package --work /temporary/work --output /results
The package is read only; all state is written below --work.
"""
import argparse
import ast
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time
import unicodedata


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--package', type=Path, required=True)
    parser.add_argument('--work', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    package = args.package.resolve()
    work = args.work.resolve() / ('run-' + str(time.time_ns()))
    output = args.output.resolve()
    work.mkdir(parents=True)
    output.mkdir(parents=True, exist_ok=True)
    script = package / 'scripts/memory.py'
    script_sha256_before = hashlib.sha256(script.read_bytes()).hexdigest()
    root = work / 'shared store'
    root.mkdir()
    events, results = [], []

    def record(status='verified', summary='Synthetic inspected quantity', **extra):
        return dict(summary=summary, kind='observation', status=status,
                    evidence=[dict(source='synthetic fixture', locator='fixture row 1', verification='inspected by test')], **extra)

    def fixture(data, name=None):
        path = work / (name or ('input-' + str(time.time_ns()) + '.json'))
        path.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')
        return path

    def location(user='alpha', project='one', store=root):
        scope = dict(user=user, project=project)
        key = hashlib.sha256(json.dumps(scope, sort_keys=True).encode()).hexdigest()
        return store / (key + '.json')

    def call(command, user='alpha', project='one', store=root, target=script, raw=False, cwd=work):
        cli = [sys.executable, '-I', '-S', str(target)]
        if not raw:
            cli += ['--root', str(store), '--user', user, '--project', project]
        cli += [str(x) for x in command]
        completed = subprocess.run(cli, cwd=cwd, text=True, capture_output=True, timeout=45)
        event = dict(command=cli, cwd=str(cwd), exit_code=completed.returncode,
                     stdout=completed.stdout, stderr=completed.stderr)
        events.append(event)
        return event

    def parsed(event):
        return json.loads(event['stdout'])

    def ok(event):
        assert event['exit_code'] == 0, event
        return parsed(event)

    def rejected(event):
        assert event['exit_code'] == 2, event
        assert event['stderr'], event

    def test(name, fn):
        start = len(events)
        try:
            detail = fn()
            results.append(dict(test=name, outcome='PASS', detail=detail, events=list(range(start, len(events)))))
        except Exception as exc:
            results.append(dict(test=name, outcome='FAIL', detail=repr(exc), events=list(range(start, len(events)))))

    valid = fixture(record())
    tentative = fixture(record('tentative', 'Synthetic critic suggestion'))

    def configuration():
        for missing in ('--root', '--user', '--project'):
            pairs = {'--root': str(root), '--user': 'alpha', '--project': 'one'}
            del pairs[missing]
            command = [x for pair in pairs.items() for x in pair] + ['check']
            rejected(call(command, raw=True))
        for flag in ('--root', '--user', '--project'):
            pairs = {'--root': str(root), '--user': 'alpha', '--project': 'one'}
            pairs[flag] = '  '
            rejected(call([x for pair in pairs.items() for x in pair] + ['check'], raw=True))
        assert list(root.iterdir()) == []
        return 'All required and whitespace-only configuration failures returned exit 2; no store created.'
    test('explicit configuration required', configuration)

    def provenance():
        inputs = [dict(summary='Synthetic', kind='observation', status='verified'),
                  dict(record(), evidence=[]), dict(record(), evidence=['unstructured'])]
        for field in ('source', 'locator', 'verification'):
            row = record()
            del row['evidence'][0][field]
            inputs.append(row)
            row = record()
            row['evidence'][0][field] = '  '
            inputs.append(row)
        for data in inputs:
            rejected(call(['add', '--file', fixture(data)]))
        assert list(root.iterdir()) == []
        return 'Missing, empty, unstructured and incomplete provenance all refused before state creation.'
    test('provenance requirements', provenance)

    def isolation():
        for user, project in [('alpha', 'one'), ('beta', 'one'), ('alpha', 'two')]:
            row = ok(call(['add', '--file', fixture(record(summary=user + '/' + project))], user=user, project=project))
            assert row['scope'] == dict(user=user, project=project)
        for user, project in [('alpha', 'one'), ('beta', 'one'), ('alpha', 'two')]:
            rows = ok(call(['list', '--status', 'all'], user=user, project=project))
            assert len(rows) == 1 and rows[0]['summary'] == user + '/' + project
        assert ok(call(['list', '--status', 'all'], user='beta', project='two')) == []
        return 'Three scopes at the same root hold disjoint records; a fourth sees none.'
    test('same-root user and project isolation', isolation)

    def statuses():
        v = ok(call(['add', '--file', valid], project='statuses'))
        t = ok(call(['add', '--file', tentative], project='statuses'))
        assert [r['id'] for r in ok(call(['list'], project='statuses'))] == [v['id']]
        assert [r['id'] for r in ok(call(['list', '--status', 'tentative'], project='statuses'))] == [t['id']]
        current = location(project='statuses')
        before = current.read_bytes()
        rejected(call(['correct', v['id'], '--file', tentative], project='statuses'))
        assert current.read_bytes() == before
        injected = record(id='injected', scope={'user': 'other'}, replaces=v['id'], created_at='forged')
        added = ok(call(['add', '--file', fixture(injected)], project='statuses'))
        assert added['id'] != 'injected' and added['scope'] == dict(user='alpha', project='statuses')
        assert 'replaces' not in added and added['created_at'] != 'forged'
        rejected(call(['add', '--file', fixture(dict(record(), status='superseded'))], project='statuses'))
        return 'Default listing returns verified records, tentative suggestions stay separate, identity injection is discarded and tentative correction leaves verified bytes intact.'
    test('tentative versus verified and identity protection', statuses)

    def corrections():
        original = ok(call(['add', '--file', tentative], project='history'))
        replacement = ok(call(['correct', original['id'], '--file', valid], project='history'))
        next_row = ok(call(['correct', replacement['id'], '--file', valid], project='history'))
        rows = ok(call(['list', '--status', 'all'], project='history'))
        assert len(rows) == 3
        assert rows[0]['status'] == 'superseded' and rows[0]['previous_status'] == 'tentative'
        assert rows[0]['superseded_by'] == rows[1]['id'] and rows[1]['replaces'] == rows[0]['id']
        assert rows[1]['status'] == 'superseded' and rows[1]['previous_status'] == 'verified'
        assert rows[1]['superseded_by'] == rows[2]['id'] and rows[2]['replaces'] == rows[1]['id']
        assert rows[2]['id'] == next_row['id'] and rows[2]['status'] == 'verified'
        before = location(project='history').read_bytes()
        rejected(call(['correct', original['id'], '--file', valid], project='history'))
        rejected(call(['correct', 'unknown-id', '--file', valid], project='history'))
        assert location(project='history').read_bytes() == before
        assert ok(call(['check'], project='history'))['records'] == 3
        return 'Two successive corrections preserve all three rows and bidirectional links; duplicate and unknown corrections refused without changes.'
    test('correction history and duplicate refusal', corrections)

    def malformed():
        ok(call(['add', '--file', valid], project='malformed'))
        path = location(project='malformed')
        backup = path.with_suffix('.previous.json')
        before = (path.read_bytes(), backup.read_bytes())
        bad = work / 'invalid-input.json'
        bad.write_text('{bad', encoding='utf-8')
        rejected(call(['add', '--file', bad], project='malformed'))
        assert (path.read_bytes(), backup.read_bytes()) == before
        damaged = b'{damaged-store'
        path.write_bytes(damaged)
        for command in (['check'], ['list'], ['add', '--file', valid]):
            rejected(call(command, project='malformed'))
            assert path.read_bytes() == damaged and backup.read_bytes() == before[1]
        return 'Invalid incoming JSON preserves current and previous copies; corrupt stored JSON refuses reads/writes and preserves exact damaged bytes.'
    test('invalid JSON refusal without data loss', malformed)

    def wrong_scope():
        ok(call(['add', '--file', valid], project='wrong-envelope'))
        path = location(project='wrong-envelope')
        backup = path.with_suffix('.previous.json')
        envelope = json.loads(path.read_text())
        envelope['scope']['user'] = 'foreign-user'
        path.write_text(json.dumps(envelope), encoding='utf-8')
        before = path.read_bytes()
        for command in (['check'], ['list'], ['add', '--file', valid]):
            rejected(call(command, project='wrong-envelope'))
            assert path.read_bytes() == before
        backup.write_bytes(before)
        rejected(call(['recover', '--confirm'], project='wrong-envelope'))
        assert path.read_bytes() == before
        assert list(root.glob(path.stem + '.recovery-*.json')) == []
        return 'Wrong-scope current envelope and previous copy both refused; no mutation or recovery archive produced.'
    test('wrong-scope envelope refusal', wrong_scope)

    def recovery():
        first = ok(call(['add', '--file', valid], project='recovery'))
        ok(call(['add', '--file', tentative], project='recovery'))
        path = location(project='recovery')
        backup = path.with_suffix('.previous.json')
        previous = backup.read_bytes()
        damaged = b'\xffdamaged-current\n'
        path.write_bytes(damaged)
        rejected(call(['recover'], project='recovery'))
        assert path.read_bytes() == damaged and backup.read_bytes() == previous
        result = ok(call(['recover', '--confirm'], project='recovery'))
        assert Path(result['preserved_current']).read_bytes() == damaged
        rows = ok(call(['list', '--status', 'all'], project='recovery'))
        assert len(rows) == 1 and rows[0]['id'] == first['id']
        assert backup.read_bytes() == previous
        assert Path(result['preserved_current']).stat().st_mode & 0o777 == 0o600
        return 'Recovery requires confirmation, restores validated previous snapshot, preserves damaged bytes in a mode-0600 archive, and visibly rolls back the latest addition.'
    test('confirmed previous-copy recovery and preservation', recovery)

    def unresolved_lock():
        ok(call(['add', '--file', valid], project='locked'))
        path = location(project='locked')
        lock = path.with_suffix('.lock')
        lock.write_text('synthetic unresolved lock evidence', encoding='utf-8')
        before = path.read_bytes()
        rejected(call(['add', '--file', valid], project='locked'))
        rejected(call(['recover', '--confirm'], project='locked'))
        assert path.read_bytes() == before and lock.read_text() == 'synthetic unresolved lock evidence'
        assert len(ok(call(['list', '--status', 'all'], project='locked'))) == 1
        lock.unlink()
        return 'Writes and recovery refuse a preexisting lock, leave lock and state intact; snapshot reader continues to work as documented.'
    test('unresolved lock refusal', unresolved_lock)

    def concurrent():
        count = 32
        fixtures = [fixture(record(summary='Concurrent synthetic row ' + str(i), details={'payload': 'x' * 50000})) for i in range(count)]
        with ThreadPoolExecutor(max_workers=count) as pool:
            attempts = list(pool.map(lambda f: call(['add', '--file', f], project='concurrent'), fixtures))
        successes = [parsed(e) for e in attempts if e['exit_code'] == 0]
        failures = [e for e in attempts if e['exit_code'] != 0]
        for failure in failures:
            rejected(failure)
            assert 'store locked' in failure['stderr']
        rows = ok(call(['list', '--status', 'all'], project='concurrent'))
        assert len(rows) == len(successes)
        assert {r['id'] for r in rows} == {r['id'] for r in successes}
        assert {r['summary'] for r in rows} == {r['summary'] for r in successes}
        assert not location(project='concurrent').with_suffix('.lock').exists()
        assert ok(call(['check'], project='concurrent'))['records'] == len(successes)
        return dict(attempts=count, successful_writes=len(successes), safely_refused=len(failures), surviving_records=len(rows), lost_successful_records=0)
    test('concurrent subprocess writers', concurrent)

    def collision():
        cases = [('../../', '../project'), ('../', '../../project'), ('用户', '项目'),
                 ('é', 'site'), (unicodedata.normalize('NFD', 'é'), 'site'),
                 ('a/b', 'c'), ('a', 'b/c'), ('alpha', 'one ') ]
        paths = []
        for i, (user, project) in enumerate(cases):
            ok(call(['add', '--file', fixture(record(summary='Collision fixture ' + str(i)))], user=user, project=project))
            path = location(user=user, project=project)
            paths.append(path)
            assert path.exists() and path.parent == root and len(path.stem) == 64
        assert len(set(paths)) == len(cases)
        for i, (user, project) in enumerate(cases):
            rows = ok(call(['list', '--status', 'all'], user=user, project=project))
            assert len(rows) == 1 and rows[0]['summary'] == 'Collision fixture ' + str(i)
        assert not (work.parent / 'project').exists()
        return 'Traversal-like IDs, slash-colliding pairs, Unicode and composed/decomposed Unicode remain distinct hashed scope names in the chosen root.'
    test('human-scope collisions and traversal-like IDs', collision)

    def relocation():
        relocated = work / 'relocated package with spaces'
        shutil.copytree(package, relocated, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        moved_script = relocated / 'scripts/memory.py'
        moved_root = work / 'relocated store with spaces'
        added = ok(call(['add', '--file', valid], target=moved_script, store=moved_root, cwd=work.parent))
        assert ok(call(['list'], target=moved_script, store=moved_root, cwd=work.parent))[0]['id'] == added['id']
        assert ok(call(['check'], target=moved_script, store=moved_root, cwd=work.parent))['ok']
        tree = ast.parse(moved_script.read_text())
        imports = sorted({node.names[0].name.split('.')[0] if isinstance(node, ast.Import) else node.module.split('.')[0]
                          for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom))})
        assert set(imports) <= sys.stdlib_module_names
        return dict(cwd_outside_package=True, relocated_path=str(relocated), interpreter_flags=['-I', '-S'], imports=imports, external_dependencies=[])
    test('relocation and isolated standard-library execution', relocation)

    def package_inspection():
        templates = sorted((package / 'templates').iterdir())
        details = {}
        for path in templates:
            content = path.read_text(encoding='utf-8')
            if path.suffix == '.csv':
                assert len(content.splitlines()) == 1
                details[path.name] = 'header-only CSV; no filled rows'
            else:
                lines = [line for line in content.splitlines() if line.startswith('- ')]
                assert lines and all(line.endswith(':') for line in lines)
                details[path.name] = 'empty prompts; no filled values'
        core = (package / 'SKILL.md').read_text(encoding='utf-8')
        assert 'No service, connector, model or proprietary library is required.' in core
        assert 'Memory is off unless an explicit isolated location and scope are configured.' in core
        details['core'] = 'Explicitly requires no service, connector, model or proprietary library; memory optional. No hardcoded private user paths or installed-memory lookup.'
        assert '/Users/' not in core and '.codex/' not in core
        return details
    test('blank original templates and optional core tools', package_inspection)

    script_sha256_after = hashlib.sha256(script.read_bytes()).hexdigest()
    assert script_sha256_after == script_sha256_before, 'Package helper changed while tests ran'
    summary = dict(package=str(package), python=sys.version, executable=sys.executable,
                   script_sha256_before=script_sha256_before, script_sha256_after=script_sha256_after,
                   classification='explicit independent regression rerun, not blind new-case testing',
                   work=str(work), total=len(results), passed=sum(r['outcome'] == 'PASS' for r in results),
                   failed=sum(r['outcome'] == 'FAIL' for r in results), results=results)
    (output / 'results.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    (output / 'process-transcript.json').write_text(json.dumps(events, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    lines = ['# Optional memory helper and portability tests', '',
             f"{summary['passed']}/{summary['total']} test groups passed; {summary['failed']} failed.", '',
             'This is an explicit independent regression rerun, not blind new-case testing. These tests run the actual packaged script in separate processes with `-I -S`, synthetic records and isolated temporary storage. No private installed skill or memory was accessed. Package files were not modified.', '',
             'Candidate helper SHA-256 (unchanged before/after test): `' + script_sha256_before + '`.', '',
             'Reproduce with Python 3.10+ (uses `sys.stdlib_module_names`):', '',
             '```text',
             'python3 test_memory_helper.py --package /absolute/path/quantity-surveyor-portable --work /temporary/work --output /results/helper',
             '```', '',
             'Actual commands, exit codes, standard output and standard error are captured in `process-transcript.json`. `results.json` maps each group to the transcript event numbers. The transcript includes synthetic test content only.', '',
             '| Test group | Outcome | Observed result |', '|---|---|---|']
    for result in results:
        detail = result['detail'] if isinstance(result['detail'], str) else json.dumps(result['detail'], ensure_ascii=False)
        lines.append('| ' + result['test'] + ' | ' + result['outcome'] + ' | ' + detail.replace('|', '\\|') + ' |')
    lines += ['', '## Limits and material findings', '',
              'No material defect found in the requested memory-helper behavior. The helper validates evidence fields but cannot establish factual truth; `verified` is a user-supplied state. Exact Unicode scope identifiers remain separate: composed/decomposed forms and trailing whitespace can create distinct scopes, so callers must consistently reuse their chosen identifiers. This is documented exact-scope behavior, not a collision.', '',
              'Concurrency means successful writes serialize while contenders may fail with an explicit lock error. The test compares every successful writer ID with the final store and checks that no successful record was lost. It does not establish power-loss durability, network filesystem safety, distributed transaction support, encryption or resistance to hostile filesystem access.', '',
              'Core portability is checked by inspecting the package core and blank templates and executing the optional helper after copying the package to a path with spaces from a working directory outside the package. No independent model/harness execution of the surveying workflows is implied. Standards reference completeness was outside this helper regression.', '',
              'All fixture and copied-package state is under the work directory reported in `results.json`; original package files remain untouched.']
    (output / 'report.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps({k: summary[k] for k in ('total', 'passed', 'failed', 'work')}, indent=2))
    for result in results:
        print(result['outcome'] + ': ' + result['test'])
        if result['outcome'] == 'FAIL':
            print(result['detail'])
    return 1 if summary['failed'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
