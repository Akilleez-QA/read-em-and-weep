"""Relocated standalone checker and real pin negatives, never production code."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parent
def need(ok,msg):
    if not ok:raise ValueError(msg)
results=[]
for optimized in (False,True):
    with tempfile.TemporaryDirectory(prefix='outer-formal-') as tmp:
        dst=Path(tmp)/'packet';shutil.copytree(ROOT,dst)
        command=[sys.executable,'-BO' if optimized else '-B',str(dst/'check.py')]
        def run():return subprocess.run(command,cwd=tmp,text=True,capture_output=True,timeout=60)
        result=run();need(result.returncode==0,'relocated clean control')
        source=dst/'sources/program.py.txt';source.write_bytes(source.read_bytes()+b'\n')
        result=run();need(result.returncode!=0 and 'pin program.py' in result.stderr,'corrupt source rejection')
        manifest=dst/'pins.json';pins=json.loads(manifest.read_text());raw=source.read_bytes()
        pins['program.py']['sha256']=hashlib.sha256(raw).hexdigest();pins['program.py']['bytes']=len(raw)
        pins['program.py']['git_blob']=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        manifest.write_text(json.dumps(pins,indent=2,sort_keys=True)+'\n')
        result=run();need(result.returncode!=0 and 'immutable manifest pin' in result.stderr,'joint pin rewrite rejection')
        results.append({'optimized':optimized,'relocated_clean':'PASS','source_corruption':'REJECTED','joint_manifest_corruption':'REJECTED'})
print(json.dumps({'status':'PASS','controls':results,'production_execution':False},indent=2))
