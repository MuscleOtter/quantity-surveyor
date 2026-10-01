#!/usr/bin/env python3
"""Explicit independent regression verification; synthetic state, subprocess CLI."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--package', type=Path, required=True)
    parser.add_argument('--work', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    package = args.package.resolve()
    script = package / 'scripts/memory.py'
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    work = args.work.resolve() / ('missing-primary-' + str(time.time_ns()))
    work.mkdir(parents=True)
    root = work / 'synthetic scoped memory'
    events, snapshots = [], []
    before_hash = hashlib.sha256(script.read_bytes()).hexdigest()

    def call(*command, project='synthetic-site'):
        cli = [sys.executable, '-I', '-S', str(script), '--root', str(root),
               '--user', 'regression-user', '--project', project] + list(command)
        result = subprocess.run(cli, cwd=work, text=True, capture_output=True, timeout=30)
        item = dict(command=cli, cwd=str(work), exit_code=result.returncode,
                    stdout=result.stdout, stderr=result.stderr)
        events.append(item)
        return item

    def ok(item):
        assert item['exit_code'] == 0, item
        return json.loads(item['stdout'])

    def fail(item, message):
        assert item['exit_code'] == 2, item
        assert message in item['stderr'], item

    def fixture(name, text):
        path = work / name
        data = dict(summary=text, kind='observation', status='verified',
                    evidence=[dict(source='synthetic independent fixture', locator=name,
                                   verification='observed test input')])
        path.write_text(json.dumps(data), encoding='utf-8')
        return str(path)

    first_input = fixture('first.json', 'Previous snapshot quantity observation')
    latest_input = fixture('latest.json', 'Latest current-only quantity observation')
    future_input = fixture('future.json', 'Safely added after recovery')
    correction_input = fixture('correction.json', 'Verified corrected previous observation')
    first = ok(call('add', '--file', first_input))
    latest = ok(call('add', '--file', latest_input))
    mains = [p for p in root.glob('*.json') if not p.name.endswith('.previous.json')]
    assert len(mains) == 1
    primary = mains[0]
    previous = primary.with_suffix('.previous.json')
    available_bytes = previous.read_bytes()
    available_hash = hashlib.sha256(available_bytes).hexdigest()
    available = json.loads(available_bytes)
    assert [r['id'] for r in available['records']] == [first['id']]
    saved_current = work / 'removed-primary-preserved-for-test.json'
    saved_current.write_bytes(primary.read_bytes())
    primary.unlink()

    def unchanged(label):
        item = dict(stage=label, primary_exists=primary.exists(),
                    previous_sha256=hashlib.sha256(previous.read_bytes()).hexdigest(),
                    previous_size=len(previous.read_bytes()),
                    lock_exists=primary.with_suffix('.lock').exists())
        snapshots.append(item)
        assert not item['primary_exists'] and item['previous_sha256'] == available_hash
        assert previous.read_bytes() == available_bytes and not item['lock_exists']

    outcome, detail = 'PASS', None
    try:
        unchanged('after deleting primary')
        for command in [('list', '--status', 'all'), ('check',),
                        ('add', '--file', future_input),
                        ('correct', first['id'], '--file', correction_input)]:
            fail(call(*command), 'primary store missing but previous copy exists')
            unchanged('refused ' + command[0])
        fail(call('recover'), 'recovery requires --confirm')
        unchanged('refused unconfirmed recovery')
        restored = ok(call('recover', '--confirm'))
        assert restored['preserved_current'] is None
        assert primary.read_bytes() == available_bytes and previous.read_bytes() == available_bytes
        assert list(root.glob(primary.stem + '.recovery-*.json')) == []
        restored_rows = ok(call('list', '--status', 'all'))
        assert [r['id'] for r in restored_rows] == [first['id']]
        assert latest['id'] not in {r['id'] for r in restored_rows}
        assert ok(call('check'))['records'] == 1
        snapshots.append(dict(stage='confirmed recovery', primary_sha256=hashlib.sha256(primary.read_bytes()).hexdigest(),
                              previous_sha256=hashlib.sha256(previous.read_bytes()).hexdigest(), records=1))
        future = ok(call('add', '--file', future_input))
        assert previous.read_bytes() == available_bytes
        rows = ok(call('list', '--status', 'all'))
        assert {r['id'] for r in rows} == {first['id'], future['id']}
        corrected = ok(call('correct', first['id'], '--file', correction_input))
        rows = ok(call('list', '--status', 'all'))
        assert len(rows) == 3
        old = next(r for r in rows if r['id'] == first['id'])
        assert old['status'] == 'superseded' and old['superseded_by'] == corrected['id']
        assert corrected['replaces'] == first['id']
        assert ok(call('check'))['records'] == 3
        current_after_recovery = primary.read_bytes()
        previous_after_recovery = previous.read_bytes()
        assert ok(call('list', project='genuinely-new-site')) == []
        new_check = ok(call('check', project='genuinely-new-site'))
        assert new_check['exists'] is False and new_check['records'] == 0
        fresh = ok(call('add', '--file', future_input, project='genuinely-new-site'))
        assert ok(call('list', project='genuinely-new-site'))[0]['id'] == fresh['id']
        assert ok(call('check', project='genuinely-new-site'))['records'] == 1
        assert primary.read_bytes() == current_after_recovery and previous.read_bytes() == previous_after_recovery
        detail = dict(refused_commands=['list', 'check', 'add', 'correct', 'recover without --confirm'],
                      backup_byte_preservation=True, restored_previous_records=1,
                      unavailable_latest_record_restored=False, recovered_scope_after_add_and_correct_records=3,
                      genuinely_new_scope_records=1, new_scope_did_not_change_recovered_scope=True)
    except Exception as exc:
        outcome, detail = 'FAIL', repr(exc)
    after_hash = hashlib.sha256(script.read_bytes()).hexdigest()
    if after_hash != before_hash:
        outcome, detail = 'FAIL', 'Package script changed during testing'
    result = dict(outcome=outcome, detail=detail, script_sha256_before=before_hash,
                  script_sha256_after=after_hash, package=str(package), python=sys.version,
                  work=str(work), process_count=len(events), snapshots=snapshots,
                  classification='explicit regression verification, not blind new-case testing')
    (output / 'missing-primary-results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    (output / 'missing-primary-transcript.json').write_text(json.dumps(events, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
    return 0 if outcome == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
