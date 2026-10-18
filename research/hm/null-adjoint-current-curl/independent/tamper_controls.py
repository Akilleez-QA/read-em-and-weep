"""Reject deliberate changes in disposable copies under normal and optimized Python."""
from pathlib import Path
import tempfile,shutil,subprocess,sys,json
root=Path(__file__).resolve().parents[1]
mutations=[
 ('branches.json','"axis": 0','"axis": 1'),
 ('inputs/compiler.py.txt','Q(-1,4)','Q(1,4)'),
 ('inputs/raw_engine.py.txt','class RawSource','class WrongSource'),
 ('dependencies/source-adjoint-proof.md','seven','six'),
 ('check.py','Q(1,4));kik','Q(-1,4));kik'),
 ('check.py','newjk=add(scale(KderL,Q(-1,2))','newjk=add(scale(KderL,0)'),
 ('check.py','newij=add(scale(KderU,Q(1,2))','newij=add(scale(KderU,0)'),
 ('check.py','cU,scale(add(BU,M),-1)','cU,scale(BU,-1)'),
]
results=[]
for name,old,new in mutations:
    for optimized in [False,True]:
        with tempfile.TemporaryDirectory() as d:
            work=Path(d)/'packet';shutil.copytree(root,work)
            p=work/name;s=p.read_text()
            if old not in s:raise RuntimeError('missing mutation target '+name+' '+old)
            p.write_text(s.replace(old,new,1))
            command=[sys.executable,'-BO' if optimized else '-B',str(work/'check.py')]
            proc=subprocess.run(command,capture_output=True,text=True)
            if proc.returncode==0:raise RuntimeError('mutation survived '+name)
            if 'SyntaxError' in proc.stderr:raise RuntimeError('invalid mutation '+name)
            results.append({'target':name,'mutation':old,'optimized':optimized,'rejected':True})
print(json.dumps({'status':'PASS','rejections':len(results),'controls':results},indent=2))
