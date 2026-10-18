"""Disposable local-copy controls, no external writes or production imports."""
from pathlib import Path
import tempfile,shutil,subprocess,sys,json
ROOT=Path(__file__).resolve().parents[1]
mutations=[
 ('proof pin','PROOF.md',None,'\nmodified\n','check_binding.py'),
 ('branch pin','branches.json',None,'\n','check_binding.py'),
 ('dependency pin','dependencies/source-adjoint.md',None,'\n','check_binding.py'),
 ('prism sign','check.py','coefficient=(-1)**k*','coefficient=1*','check.py'),
 ('omit source defect','independent/check_exterior.py','qd=boundary(prism(tags,vec))','qd={}','independent/check_exterior.py'),
]
results=[]
for opt in [False,True]:
 for label,file,old,new,checker in mutations:
  with tempfile.TemporaryDirectory() as td:
   dst=Path(td)/'packet'; shutil.copytree(ROOT,dst)
   p=dst/file; text=p.read_text()
   if old is None: text+=new
   else:
    if old not in text: raise RuntimeError('mutation anchor missing')
    text=text.replace(old,new,1)
   p.write_text(text)
   cmd=[sys.executable,'-BO' if opt else '-B',str(dst/checker)]
   r=subprocess.run(cmd,capture_output=True,text=True)
   if r.returncode==0: raise RuntimeError('accepted mutation: '+label)
   results.append({'mutation':label,'optimized':opt,'rejected':True})
print(json.dumps(results,indent=2))
