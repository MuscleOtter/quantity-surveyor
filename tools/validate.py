#!/usr/bin/env python3
"""Validate public structure, immutable evidence and distribution equivalence."""
import sys
sys.dont_write_bytecode = True
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import tempfile
import zipfile

ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'skills/quantity-surveyor'
EVAL=ROOT/'evaluation'


def require(value,message):
    if not value:
        raise ValueError(message)


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def verify_manifest(base,manifest):
    for name,record in json.loads(manifest.read_text()).items():
        expected=record['sha256'] if isinstance(record,dict) else record
        require(digest(base/name)==expected,'Hash mismatch: '+name)


def main():
    s=(SKILL/'SKILL.md').read_text()
    require(s.startswith('---\n'),'Missing frontmatter')
    head,body=s[4:].split('\n---\n',1)
    require(re.search(r'^name: quantity-surveyor$',head,re.M),'Name mismatch')
    require(re.search(r'^description: .+',head,re.M),'Missing description')
    manifest=json.loads((SKILL/'version.json').read_text())
    require(re.fullmatch(r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)',manifest['version']),'Expected stable major.minor.patch version')
    require('version: "'+manifest['version']+'"' in head,'Version mismatch')
    for name,record in json.loads((EVAL/'frozen.json').read_text())['files'].items():
        require(digest(EVAL/name)==record['sha256'],'Frozen suite mismatch: '+name)
    verify_manifest(EVAL/'candidate-round2',EVAL/'candidate-round2-hashes.json')
    for round_name in ['round1','round2']:
        verify_manifest(EVAL/round_name/'responses',EVAL/round_name/'response-hashes.json')
    old=(EVAL/'candidate-round2/SKILL.md').read_text().split('\n---\n',1)[1]
    qs_body=body.split('\n## Optional release updates\n',1)[0]
    # v2 adds explicit routing and a drawing-set gate; preserve the historical
    # base without claiming its old behavioral score applies to the additions.
    qs_body=qs_body.replace('- Multi-sheet drawing review, large sets, revision comparison or drawing-based take-off: [large-drawing-sets.md](references/large-drawing-sets.md).\n','')
    qs_body=qs_body.replace('For drawing sets, inventory and select the applicable issue before measuring. Track reviewed sheets/views, unresolved references and quantity evidence across batches. Text extraction alone is not visual inspection; unread scope is not zero. Apply the large-set reference proportionately, without imposing a full register on a simple dimension calculation.\n\n','')
    require(qs_body==old,'Historical QS base changed; update evidence deliberately')
    def v2_source(name):
        archived=EVAL/'v2-drawing-workflow/released-candidate'/name.removeprefix('skills/quantity-surveyor/')
        return archived if archived.is_file() else ROOT/name
    initial=json.loads((EVAL/'v2-drawing-workflow/frozen-initial.json').read_text())
    for name,expected in initial.items():
        archived=EVAL/'v2-drawing-workflow/initial-candidate'/name.removeprefix('skills/quantity-surveyor/')
        source=archived if archived.is_file() else v2_source(name)
        require(digest(source)==expected,'Initial v2 review source changed: '+name)
    for name,expected in json.loads((EVAL/'v2-drawing-workflow/frozen.json').read_text()).items():
        source=v2_source(name)
        require(digest(source)==expected,'Frozen v2 source changed: '+name)
        if source != ROOT/name:
            renamed=source.read_text().replace('universal-quantity-surveyor','quantity-surveyor').replace('"2.0.0"','"2.0.1"')
            require((ROOT/name).read_text()==renamed,'Unexpected repository-rename delta: '+name)
    verify_manifest(EVAL/'v2-drawing-workflow',EVAL/'v2-drawing-workflow/response-hashes.json')
    for name in json.loads((EVAL/'candidate-round2-hashes.json').read_text()):
        if name not in ('SKILL.md','README.md'):
            require(digest(SKILL/name)==digest(EVAL/'candidate-round2'/name),'Scored reference/helper changed: '+name)
    allowed=set(json.loads((EVAL/'candidate-round2-hashes.json').read_text()))-{'README.md'}
    allowed |= {'references/updates.md','scripts/check_updates.py','version.json','references/large-drawing-sets.md','templates/drawing-register.csv','templates/quantity-evidence.csv'}
    actual={p.relative_to(SKILL).as_posix() for p in SKILL.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
    require(actual==allowed,'Unexpected or missing distributable files: '+str(actual^allowed))
    documents=list((ROOT/'docs').glob('*.md'))+[ROOT/'README.md',ROOT/'quantity-surveyor-review.md',ROOT/'CONTRIBUTING.md']+list(SKILL.rglob('*.md'))
    for p in documents:
        for label,url in re.findall(r'\[([^\]]+)\]\(([^)]+)\)',p.read_text()):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',url) or url.startswith('#'):continue
            local=url.split('#',1)[0]
            require((p.parent/local).exists(),'Broken local link in '+p.relative_to(ROOT).as_posix()+': '+url)
    for p in ROOT.rglob('*'):
        if not p.is_file() or any(part in ('.git','__pycache__','work','dist') for part in p.relative_to(ROOT).parts):continue
        if p.suffix in ('.md','.json','.py','.csv','.yml','.txt'):
            require(not re.search(r'/U[s]ers/[A-Za-z0-9]', p.read_text()),'Private absolute host path in '+p.relative_to(ROOT).as_posix())
    spec=importlib.util.spec_from_file_location('builder',ROOT/'tools/build_release.py')
    builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)
    require((ROOT/'llms-full.txt').read_text()==builder.combined_markdown(),'Generated llms-full.txt is stale; rebuild with --sync-discovery')
    require(manifest['name']=='quantity-surveyor','Manifest name mismatch')
    require('Current release: '+manifest['version'] in (ROOT/'llms.txt').read_text(),'Discovery version mismatch')
    with tempfile.TemporaryDirectory(prefix='qs-package-') as temporary:
        out=Path(temporary);builder.build(out)
        with zipfile.ZipFile(out/'quantity-surveyor.zip') as z:
            names=z.namelist()
            require(all(name.startswith('quantity-surveyor/') for name in names),'ZIP enclosing folder mismatch')
            require(set(n.split('/',1)[1] for n in names)==allowed,'ZIP contents mismatch')
            require(z.testzip() is None,'Invalid ZIP')
            for p in builder.source_files():
                require(z.read('quantity-surveyor/'+p.relative_to(SKILL).as_posix())==p.read_bytes(),'ZIP bytes differ')
        for suffix in ('.zip','.md'):
            require((out/('universal-quantity-surveyor'+suffix)).read_bytes()==(out/('quantity-surveyor'+suffix)).read_bytes(),'Legacy alias differs')
        doc=(out/'quantity-surveyor.md').read_text()
        require(len(re.findall(r'<a id="',doc))==1+len(list((SKILL/'references').glob('*.md')))+len(list((SKILL/'templates').glob('*'))),'Missing combined section')
        require(not re.search(r'\]\((?:\.\.?/)?(?:references|templates)/',doc),'Unresolved combined reference')
    print('PASS: standard folder, versions, frozen suite, sealed answers, historical base preservation, frozen v2 sources, local links, discovery and complete distributions.')


if __name__=='__main__':
    main()
