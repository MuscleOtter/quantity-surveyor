"""Regression for a missing primary with a surviving scoped backup; synthetic data only."""
from pathlib import Path
import argparse, hashlib, json, subprocess, sys, tempfile


def main():
 p=argparse.ArgumentParser();p.add_argument('--package',required=True);p.add_argument('--work',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 work=Path(a.work).resolve();work.mkdir(parents=True,exist_ok=True)
 root=Path(tempfile.mkdtemp(prefix='missing-primary-',dir=work));store=root/'store'
 script=Path(a.package).resolve()/'scripts/memory.py'
 record=root/'record.json'
 record.write_text(json.dumps({'summary':'synthetic verified recovery lesson','kind':'lesson','status':'verified','evidence':[{'source':'synthetic fixture','locator':'R1','verification':'controlled test input'}]}))
 args=[sys.executable,'-I','-S',str(script),'--root',str(store),'--user','SYN-U','--project','SYN-P']
 events=[];checks=[]
 def run(tail,expected):
  result=subprocess.run(args+tail,capture_output=True,text=True,cwd=root)
  events.append({'arguments':tail,'exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr})
  assert result.returncode==expected,(tail,result.stderr)
  return json.loads(result.stdout) if result.stdout else None
 first=run(['add','--file',str(record)],0)
 run(['add','--file',str(record)],0)
 backup=next(store.glob('*.previous.json'))
 primary=backup.with_name(backup.name.replace('.previous.json','.json'))
 before=backup.read_bytes();before_sha=hashlib.sha256(before).hexdigest()
 assert len(json.loads(before)['records'])==1
 lost_latest=primary.read_bytes();primary.unlink()  # Controlled fixture fault, never a live store.
 for operation in [['list'],['check'],['add','--file',str(record)],['correct',first['id'],'--file',str(record)],['recover']]:
  run(operation,2)
  assert not primary.exists()
  assert backup.read_bytes()==before
  checks.append({'operation':operation[0],'refused':True,'backup_unchanged':True,'primary_not_recreated':True})
 recovered=run(['recover','--confirm'],0)
 assert primary.exists() and primary.read_bytes()==before
 assert backup.read_bytes()==before and recovered['preserved_current'] is None
 assert [r['id'] for r in run(['list'],0)]==[first['id']]
 checks.append({'operation':'confirmed recovery','restored_previous_exactly':True,'no_false_archive_claim':True,'lost_latest_records':len(json.loads(lost_latest)['records'])-1})
 run(['add','--file',str(record)],0)
 assert len(run(['list'],0))==2 and len(json.loads(backup.read_bytes())['records'])==1
 checks.append({'operation':'post-recovery add','history_preserved':True})
 args[-1]='SYN-FRESH'
 assert run(['list'],0)==[]
 run(['add','--file',str(record)],0)
 assert len(run(['list'],0))==1
 checks.append({'operation':'genuinely new scope','fresh_initialisation_allowed':True})
 result={'passed':True,'checks':checks,'backup_sha_before_fault':before_sha,'script_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),'events':events,'limits':'Synthetic fault injection; no live data or power-loss durability test. Recovery deliberately rolls back the unavailable latest state.'}
 output=Path(a.output);output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'passed':True,'check_groups':len(checks),'subprocess_calls':len(events)}))

if __name__=='__main__':main()
