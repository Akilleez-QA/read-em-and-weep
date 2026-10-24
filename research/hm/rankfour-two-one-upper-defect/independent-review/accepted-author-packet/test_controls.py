#!/usr/bin/env python3
"""Genuine subprocess mutations of universal data and equations, not actual instances."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import tempfile,subprocess,sys,json,shutil
ROOT=Path(__file__).resolve().parent
source=(ROOT/'verify.py').read_text()
mutations=[
 ('wrong_actual_M2','M2=vec(A=1,V=2,P=3,D=4)','M2=vec(A=2,V=2,P=3,D=4)'),
 ('wrong_actual_M4','M4=vec(V=2,P=4,D=3)','M4=vec(V=3,P=4,D=3)'),
 ('wrong_actual_H','H=vec(A=2,V=2,P=2,D=2)','H=vec(A=1,V=2,P=2,D=2)'),
 ('physical_Wprime_swap','(6,7),(5,8)','(6,8),(5,7)'),
 ('wrong_center_parity','PARITY=(0,1,0,1,0,1,0,1,0)','PARITY=(0,1,0,1,0,1,1,0,0)'),
 ('reverse_determinant_parity','if c1%2:continue','if not c1%2:continue'),
 ('wrong_degree_slack','2*u+4*v+d1+2*d2!=54','2*u+4*v+d1+2*d2!=52'),
 ('wrong_torsion_length','r+t-n))','r+t-n+2))'),
 ('omit_length20_character','20:[((20,r),)for r in range(0,6,2)]','20:[((20,r),)for r in range(0,4,2)]'),
 ('omit_repeated_length24_layers','for s in range(r,10,2)','for s in range(r+2,10,2)'),
 ('wrong_upper_elimination_shift','e-4:c for e,c in upper_B.items()','e-6:c for e,c in upper_B.items()'),
 ('wrong_dual_Euler_argument','chi(B,-t),torsion(T2,-t)','chi(B,-t-4),torsion(T2,-t)'),
 ('reverse_upper_torsion_sign','chi(B,-t),torsion(T2,-t)','chi(B,-t),mul(torsion(T2,-t),-1)'),
 ('wrong_primal_derivative_twist','horizontal_witnesses(F0,twist(B,-4))','horizontal_witnesses(F0,twist(B,-6))'),
 ('wrong_dual_derivative_twist','horizontal_witnesses(D0,twist(dual(B),-4))','horizontal_witnesses(D0,twist(dual(B),-6))'),
 ('wrong_internal_cotangent_twist','internal=twist(endpoint[:j]+endpoint[j+1:],-2)','internal=twist(endpoint[:j]+endpoint[j+1:],0)'),
 ('wrong_endpoint_degree_cap','xs=bounded_splits(9,dg,lo,-3)','xs=bounded_splits(9,dg,lo,-2)'),
 ('wrong_B_domain_floor','xs=bounded_splits(4,d,-10,d+30)','xs=bounded_splits(4,d,-8,d+30)'),
 ('wrong_source_cubic_degree','((-2,4),(-3,7),(-3,5),(-4,8),(-8,0))','((-2,4),(-3,7),(-3,5),(-4,8),(-6,0))'),
 ('wrong_rankone_persistence','for n in range(12,31)if 9*(n-9)<=30','for n in range(11,31)if 9*(n-9)<=30'),
 ('wrong_rankone_weight','weight=n*(30-r*ss)','weight=n*(31-r*ss)'),
 ('wrong_rankone_step','lines.append(lines[-1]+2+dd)','lines.append(lines[-1]+4+dd)'),
 ('wrong_actual_E_degree_cap','require(-12>-2*11','require(-12>-1*11'),
 ('wrong_pinned_four_source_hash','d5feb4b4478b5ec8178a049124179d25473b2e2526b20823a40f6dc60095e28e','05feb4b4478b5ec8178a049124179d25473b2e2526b20823a40f6dc60095e28e'),
]
for name,old,new in mutations:
 if old not in source:raise RuntimeError('missing mutation target '+name)
def run(task):
 name,old,new,opt=task
 with tempfile.TemporaryDirectory(prefix='rankfour21-control-')as td:
  p=Path(td);shutil.copytree(ROOT/'inputs',p/'inputs');shutil.copy(ROOT/'INPUTS.json',p/'INPUTS.json')
  (p/'verify.py').write_text(source.replace(old,new,1))
  proc=subprocess.run([sys.executable]+(['-O']if opt else[])+[str(p/'verify.py')],cwd='/',text=True,capture_output=True)
  if proc.returncode==0:raise RuntimeError('mutation was not rejected: '+name+(' optimized'if opt else''))
  last=proc.stderr.strip().splitlines()[-1]if proc.stderr.strip()else''
  if 'ValueError:'not in last:raise RuntimeError('mutation failed unexpectedly: '+name+' '+last)
  return {'mutation':name,'optimized':opt,'rejected':True,'reason':last}
tasks=[(name,old,new,opt)for name,old,new in mutations for opt in(False,True)]
with ThreadPoolExecutor(max_workers=4)as pool:results=list(pool.map(run,tasks))
print(json.dumps({'status':'PASS','subprocess_mutations_rejected':len(results),'results':results},indent=2,sort_keys=True))
