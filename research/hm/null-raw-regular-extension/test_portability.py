"""Relocated subprocess replay and corruption controls. Never executes production inputs."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parent

def need(ok,msg):
 if not ok:raise ValueError(msg)

def run(root,optimized):
 return subprocess.run([sys.executable,*(['-O'] if optimized else []),str(root/'check.py')],cwd=root.parent,text=True,capture_output=True)

reports=[]
with tempfile.TemporaryDirectory(prefix='raw-domain-review-') as tmp:
 base=Path(tmp)/'relocated'
 shutil.copytree(ROOT,base)
 for optimized in (False,True):
  good=run(base,optimized);need(good.returncode==0,'relocated positive replay: '+good.stderr)
  original=(base/'inputs/raw_engine.py.txt').read_bytes()
  original_manifest=(base/'pins.json').read_bytes()
  (base/'inputs/raw_engine.py.txt').write_bytes(original+b'\n# inert corruption\n')
  bad=run(base,optimized)
  need(bad.returncode!=0 and 'input pin raw_engine.py.txt' in bad.stderr,'source corruption rejection')
  altered=json.loads(original_manifest)
  altered['raw_engine.py.txt']=hashlib.sha256((base/'inputs/raw_engine.py.txt').read_bytes()).hexdigest()
  (base/'pins.json').write_text(json.dumps(altered,indent=2)+'\n')
  joint=run(base,optimized)
  need(joint.returncode!=0 and 'immutable manifest pin' in joint.stderr,'joint source-manifest rejection')
  (base/'pins.json').write_bytes(original_manifest)
  (base/'inputs/raw_engine.py.txt').write_bytes(original)
  restored=run(base,optimized);need(restored.returncode==0,'restored replay')
  reports.append({'optimized':optimized,'relocated_pass':True,'source_corruption_rejected':True,'joint_source_manifest_rejected':True,'restored_pass':True})
print(json.dumps({'status':'PASS','modes':reports,'production_imports':False},indent=2))
