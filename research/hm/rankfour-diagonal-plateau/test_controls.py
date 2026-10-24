#!/usr/bin/env python3
"""Subprocess mutation controls on the frozen universal checker, never HM instances."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import tempfile,subprocess,sys,json,shutil
ROOT=Path(__file__).resolve().parent
source=(ROOT/'verify.py').read_text()
mutations=[
 ('wrong_actual_M4','M4=vec(V=2,P=4,D=3)','M4=vec(V=3,P=4,D=3)'),
 ('wrong_actual_H','H=vec(A=2,V=2,P=2,D=2)','H=vec(A=1,V=2,P=2,D=2)'),
 ('physical_Wprime_swap',"(6,7),(5,8)","(6,8),(5,7)"),
 ('permit_length_ten','defects=[0,12,20]','defects=[0,10,20]'),
 ('drop_determinant_parity','if c1%2:','if False:'),
 ('wrong_torsion_length','r+t-12','r+t-10'),
 ('reverse_torsion_sign','sig[i]-base[i]-tv[i]','sig[i]-base[i]+tv[i]'),
 ('wrong_endpoint_shift','Q(t-4))[i]','Q(t-6))[i]'),
 ('omit_fourth_positive_test','for v in positive_tests(B))','for v in positive_tests(B)[:3])'),
 ('wrong_primal_derivative_twist',"('primal',ff,twist(B,-4))","('primal',ff,twist(B,-6))"),
 ('wrong_dual_derivative_twist',"('dual',dd,twist(dual(B),-6))","('dual',dd,twist(dual(B),-4))"),
 ('wrong_internal_cotangent_twist','inside=twist(endpoint[:j]+endpoint[j+1:],-2)','inside=twist(endpoint[:j]+endpoint[j+1:],0)'),
 ('wrong_rankone_degree_bound','if 5*(n-5)<=22','if 5*(n-5)<=25'),
 ('wrong_rankone_required_weight','weight=9*(22-5*4)','weight=8*(22-5*4)'),
]
for name,old,new in mutations:
 if old not in source:raise RuntimeError('missing mutation target '+name)
def run(task):
 name,old,new,opt=task
 with tempfile.TemporaryDirectory(prefix='rankfour22-control-')as td:
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
