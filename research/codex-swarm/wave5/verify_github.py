"""Read back published wave bytes; no mathematical or physical execution."""
import argparse,base64,concurrent.futures,hashlib,json,pathlib,subprocess
HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parents[2]
BASE='7d73d540981a3a152d807c39844ec63bc9913b89'
API='repos/Akilleez-QA/read-em-and-weep/'
def run(*args):return subprocess.check_output(args,cwd=ROOT)
def api(path):return json.loads(run('gh','api',API+path))
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--commit',required=True);args=parser.parse_args();commit=args.commit
 head=api('pulls/87')['head']['sha']
 if head!=commit and api('compare/'+commit+'...'+head)['status']!='ahead':raise ValueError('snapshot is not on published PR87 ancestry')
 paths=run('git','diff','--name-only',BASE,commit,'--','research/codex-swarm').decode().splitlines()
 def check(path):
  blob=run('git','rev-parse',commit+':'+path).decode().strip();data=base64.b64decode(api('git/blobs/'+blob)['content']);local=run('git','show',commit+':'+path)
  if data!=local:raise ValueError('GitHub bytes differ: '+path)
  return{'path':path,'git_blob':blob,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'github_bytes_match':True}
 with concurrent.futures.ThreadPoolExecutor(max_workers=4)as pool:files=list(pool.map(check,paths))
 out={'schema':'github-wave5-exact-readback-v1','pull_request':87,'remote_head_at_readback':head,'source_snapshot':commit,'source_base':BASE,'files':files,'file_count':len(files),'total_bytes':sum(x['bytes']for x in files),'physical_source_evaluated':False,'execution_release':False}
 (HERE/'github-readback.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print('GitHub exact read-back:',len(files),'files,',out['total_bytes'],'bytes match')
if __name__=='__main__':main()
