#!/usr/bin/env python3
"""Genuine subprocess mutation controls for the independent bounded review."""
from pathlib import Path
import json,shutil,subprocess,sys,tempfile,hashlib
ROOT=Path(__file__).resolve().parent
MUTATIONS=[
 ('class trace','independent.py','TR=(q(2),q(-2)','TR=(q(3),q(-2)'),
 ('class weight','independent.py','WEIGHTS=(1,1,12','WEIGHTS=(2,1,12'),
 ('representation dimension','independent.py','DIMS=(1,2,3,4,5,6,4,2,3)','DIMS=(1,2,3,4,5,6,4,2,4)'),
 ('central parity','independent.py','PAR=(0,1,0,1,0,1,0,1,0)','PAR=(0,1,0,1,0,1,0,0,0)'),
 ('torsion sign','independent.py','sub(linechi(0,r+t),linechi(0,r+t-n))','add(linechi(0,r+t),linechi(0,r+t-n))'),
 ('torsion length','independent.py','linechi(0,r+t-n))','linechi(0,r+t-n+2))'),
 ('omit stabilizer characters','independent.py','combinations_with_replacement(range(0,10,2),p)','combinations_with_replacement(range(0,4,2),p)'),
 ('omit length24 layers','independent.py','for p,q,r in product(range(5),range(3),range(2)):', 'for p,q,r in product(range(2),range(3),range(2)):'),
 ('degree identity','independent.py','numerator=-138+d1+2*d2-a','numerator=-136+d1+2*d2-a'),
 ('upper defect weight','independent.py','if d1+2*d2>54:continue','if d1+3*d2>54:continue'),
 ('primal quotient twist','independent.py','h1(B,-1)))and','h1(B,-3)))and'),
 ('internal cotangent twist','independent.py','y[0]-2,y[1]','y[0],y[1]'),
 ('endpoint cutoff','verify_bounded.py','c.splitting(9,degree,-3)','c.splitting(9,degree,-4)'),
 ('dual Euler torsion sign','verify_bounded.py','c.add(c.Qs(t),c.chi(B,-t),c.torsion(T2,-t))','c.sub(c.add(c.Qs(t),c.chi(B,-t)),c.torsion(T2,-t))'),
 ('primal outer target','verify_bounded.py','c.horizontal_witness(F,c.shift(B,-4))','c.horizontal_witness(F,c.shift(B,-2))'),
 ('dual outer target','verify_bounded.py','c.shift(c.dual(B),-4)','c.shift(c.dual(B),-6)'),
 ('require both horizontal obstructions','verify_bounded.py','if wf or wd:horizontal.append','if wf and wd:horizontal.append'),
 ('source cubic budget','verify_bounded.py','sourceh1=[c.h1(E,3)for E in sources]','sourceh1=[c.h1(E,2)for E in sources]'),
 ('source existential condition','verify_bounded.py','if any(c.pos(c.sub(v,h1))for v in sourceh1)','if all(c.pos(c.sub(v,h1))for v in sourceh1)'),
 ('persistence lower bound','verify_bounded.py','range(12,31)','range(11,31)'),
 ('rankone degree bound','verify_bounded.py','30>=9*(n-9)','36>=9*(n-9)'),
 ('weighted defect sign','verify_bounded.py','target=n*(30-r*(n-r))','target=n*(30+r*(n-r))'),
 ('left flag weights','verify_bounded.py','(n-r)*j if j<r','(n-r)*(j+1) if j<r'),
 ('right flag weights','verify_bounded.py','else r*(n-j)','else r*(n-j-1)'),
 ('line recurrence','verify_bounded.py','lines[-1]+2+dd','lines[-1]+2-dd'),
 ('line initial degree','verify_bounded.py','(-(n-1)*n-sum','(-(n-1)*n+sum'),
 ('flag divisor orbit floor','verify_bounded.py','deltas=[12]+[0]*10','deltas=[20]+[0]*10'),
 ('second transform degree','verify_bounded.py','sum(lines[:11])==-12','sum(lines[:11])==-22'),
 ('source pin','accepted-author-packet/inputs/four-sources.md','', 'CORRUPTED\n'),
]
def main():
 out=[]
 for name,filename,old,new in MUTATIONS:
  with tempfile.TemporaryDirectory(prefix='rankfour21-independent-')as td:
   td=Path(td)
   for file in('independent.py','verify_bounded.py'):shutil.copy2(ROOT/file,td/file)
   shutil.copytree(ROOT/'accepted-author-packet',td/'accepted-author-packet')
   shutil.copytree(ROOT/'remote-inputs',td/'remote-inputs')
   p=td/filename;s=p.read_text()
   if old:
    if old not in s:raise ValueError('mutation anchor missing: '+name)
    changed=s.replace(old,new)
   else:changed=new+s
   if changed==s:raise ValueError('non-mutating control: '+name)
   p.write_text(changed)
   cp=subprocess.run([sys.executable]+(['-O']if sys.flags.optimize else[])+[str(td/'verify_bounded.py')],cwd='/',capture_output=True,text=True)
   if cp.returncode==0:raise ValueError('mutation survived: '+name)
   if not cp.stderr.strip().splitlines()[-1].startswith('ValueError:'):raise ValueError('not a semantic rejection: '+name+' '+cp.stderr)
   out.append({'mutation':name,'target':filename,'rejected':True,'returncode':cp.returncode,'last_error_line':cp.stderr.strip().splitlines()[-1]})
 result={'status':'PASS','genuine_subprocess_mutations':len(out),'all_rejected':True,'mutations':out}
 print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
