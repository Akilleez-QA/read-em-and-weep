"""Consume null's exact public artificial edge regression, never physical sources."""
import hashlib,json,os,pathlib,subprocess,sys,tempfile
HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parents[2]
COMMIT='93120cfab74e448e7df07268abe6c54031d630db'
BASE='research/hm/null-source-integration/ins-edge-order-regression/'
def main():
 blobs={}
 for name in('README.md','test_edge_order.py'):
  data=subprocess.check_output(['git','show',COMMIT+':'+BASE+name],cwd=ROOT)
  blobs[name]={'sha256':hashlib.sha256(data).hexdigest(),'git_blob':subprocess.check_output(['git','rev-parse',COMMIT+':'+BASE+name],cwd=ROOT,text=True).strip()}
 test=subprocess.check_output(['git','show',COMMIT+':'+BASE+'test_edge_order.py'],cwd=ROOT)
 rows=[]
 with tempfile.TemporaryDirectory(prefix='ins-edge-regression-')as tmp:
  path=pathlib.Path(tmp)/'test_edge_order.py';path.write_bytes(test)
  for optimized in(False,True):
   cmd=[sys.executable,'-B']+(['-O']if optimized else[])+[str(path),'-v']
   r=subprocess.run(cmd,cwd=ROOT,env={**os.environ,'PYTHONPATH':str(HERE.parent/'inserted-coefficients'),'PYTHONDONTWRITEBYTECODE':'1'},capture_output=True,text=True,timeout=20)
   if r.returncode:raise RuntimeError(r.stderr)
   rows.append({'optimized':optimized,'tests':1,'returncode':r.returncode,'result':'PASS; increasing-edge call=-1, reversed edge explicitly rejected'})
 out={'schema':'null-exact-edge-regression-replay-v1','source_commit':COMMIT,'source_directory':BASE,'source_files':blobs,'implementation_sha256':hashlib.sha256((HERE.parent/'inserted-coefficients/inserted_program.py').read_bytes()).hexdigest(),'controls':rows,'physical_source_evaluated':False,'execution_release':False}
 (HERE/'edge-regression-replay.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print('null exact artificial edge regression: PASS normal and -O')
if __name__=='__main__':main()
