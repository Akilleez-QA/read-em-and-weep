"""Mutate disposable copies; never import or execute any frozen source input."""
from pathlib import Path
import tempfile,shutil,subprocess,sys,json
root=Path(__file__).resolve().parents[1]
results=[]
for mode in ([],['-O']):
    for target in ['inputs/compiler.py.txt','source-contracts.json','branches.json']:
        with tempfile.TemporaryDirectory() as tmp:
            dst=Path(tmp)/'packet';shutil.copytree(root,dst)
            p=dst/target;p.write_bytes(p.read_bytes()+b'\n ')
            run=subprocess.run([sys.executable,'-B',*mode,str(dst/'check.py')],capture_output=True,text=True)
            if run.returncode==0 or 'independent packet pin' not in run.stderr or 'PASS' in run.stdout:
                raise ValueError('tamper accepted: '+target)
            results.append({'optimized':bool(mode),'target':target,'rejected':True})
print(json.dumps({'status':'PASS','tamper_controls':results},sort_keys=True))
