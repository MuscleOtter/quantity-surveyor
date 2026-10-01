#!/usr/bin/env python3
"""Build reproducible install ZIP, complete Markdown edition and checksums."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/quantity-surveyor'
NAME = SKILL.name


def source_files():
    return [p for p in sorted(SKILL.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.suffix not in ('.pyc','.pyo')]


def combined_markdown():
    manifest=json.loads((SKILL/'version.json').read_text())
    version=manifest['version']
    paths=[SKILL/'SKILL.md']+sorted((SKILL/'references').glob('*.md'))+sorted((SKILL/'templates').glob('*'))
    anchors={p.resolve():'part-'+p.relative_to(SKILL).as_posix().replace('/','-').replace('.','-') for p in paths}
    def render(p):
        text=p.read_text(encoding='utf-8')
        if p.name=='SKILL.md':
            text=re.sub(r'^---\n.*?\n---\n','',text,count=1,flags=re.S)
        def target(match):
            label,url=match.groups()
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',url) or url.startswith('#'):
                return match.group(0)
            linked=(p.parent/url).resolve()
            if linked in anchors:
                return '['+label+'](#'+anchors[linked]+')'
            try:
                relative=linked.relative_to(SKILL).as_posix()
            except ValueError:
                return match.group(0)
            return '['+label+'](https://github.com/MuscleOtter/universal-quantity-surveyor/blob/v'+version+'/skills/'+NAME+'/'+relative+')'
        text=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',target,text)
        if p.suffix=='.csv':
            text='## '+p.name+'\n\n```csv\n'+text+'```\n'
        return '<a id="'+anchors[p.resolve()]+'"></a>\n\n'+text.strip()+'\n'
    header='# Quantity Surveyor — complete chat edition\n\nVersion '+version+'. Original instructions under MIT. Attach this file and ask the model to apply it to your task. It contains the core instructions, all references and original templates. Tools, optional helpers and persistent state depend on your chosen app; they are not enabled by this attachment.\n\n'
    return header+'\n\n---\n\n'.join(render(p) for p in paths)+'\n\n## Original content license\n\n'+(SKILL/'LICENSE').read_text()


def build(out):
    out.mkdir(parents=True,exist_ok=True)
    archive=out/(NAME+'.zip')
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in source_files():
            entry=zipfile.ZipInfo(NAME+'/'+p.relative_to(SKILL).as_posix(),date_time=(1980,1,1,0,0,0))
            entry.compress_type=zipfile.ZIP_DEFLATED
            entry.external_attr=0o100644 << 16
            z.writestr(entry,p.read_bytes())
    doc=out/(NAME+'.md')
    doc.write_text(combined_markdown(),encoding='utf-8')
    # Keep v1 README/latest-download URLs working after the skill identity change.
    legacy=[]
    for item in (archive,doc):
        alias=out/('universal-quantity-surveyor'+item.suffix)
        alias.write_bytes(item.read_bytes())
        legacy.append(alias)
    checksums=''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in [archive,doc,*legacy])
    (out/'SHA256SUMS.txt').write_text(checksums,encoding='utf-8')
    print('Built install ZIP, complete Markdown edition and SHA256SUMS.txt.')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,default=ROOT/'dist')
    parser.add_argument('--sync-discovery',action='store_true',help='Regenerate the checked-in llms-full.txt from canonical instructions.')
    args=parser.parse_args()
    if args.sync_discovery:
        (ROOT/'llms-full.txt').write_text(combined_markdown(),encoding='utf-8')
    build(args.out.resolve())
