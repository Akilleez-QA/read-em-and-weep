#!/usr/bin/env python3
"""Adversarial controls for the independent universal checker."""
from pathlib import Path
import tempfile,subprocess,shutil,json,sys
from concurrent.futures import ThreadPoolExecutor
ROOT=Path(__file__).resolve().parent
source=(ROOT/'independent.py').read_text()
mutations=[
 ('incorrect_defect_budget','2*(u+v)+total!=20','2*(u+v)+total!=18'),
 ('omit_length12_defects','product((0,12,20),repeat=3)','product((0,20),repeat=3)'),
 ('drop_determinant_parity','if c1%2:rejected.append','if False:rejected.append'),
 ('wrong_torsion_length','r+t-12','r+t-10'),
 ('reverse_torsion_sign','x-y-z for x,y,z in zip(sig(ff),base,tor)','x-y+z for x,y,z in zip(sig(ff),base,tor)'),
 ('wrong_dual_positive_twist','neg(chi(bb,-2)),Qs(2)','neg(chi(bb,-3)),Qs(2)'),
 ('wrong_lower_target_twist','horizontal_witness(ff,shift(bb,-4))','horizontal_witness(ff,shift(bb,-6))'),
 ('wrong_upper_target_twist','horizontal_witness(dd,shift(dual(bb),-6))','horizontal_witness(dd,shift(dual(bb),-4))'),
 ('wrong_internal_derivative_twist','y[0]-2,y[1]','y[0],y[1]'),
 ('wrong_rankone_degree_bound','22>=5*(n-5)','25>=5*(n-5)'),
 ('wrong_final_required_weight','gap=n*(22-r*(n-r))','gap=n*(24-r*(n-r))'),
]
def run(task):
 name,old,new,opt=task
 if old not in source:raise ValueError('missing source mutation '+name)
 with tempfile.TemporaryDirectory(prefix='independent-rankfour22-')as td:
  p=Path(td);shutil.copytree(ROOT/'remote-inputs',p/'remote-inputs');shutil.copytree(ROOT/'accepted-author-packet',p/'accepted-author-packet')
  (p/'independent.py').write_text(source.replace(old,new,1))
  result=subprocess.run([sys.executable]+(['-O']if opt else[])+[str(p/'independent.py')],capture_output=True,text=True)
  if result.returncode==0:raise ValueError('mutation unexpectedly accepted '+name)
  reason=result.stderr.strip().splitlines()[-1]
  if 'ValueError:'not in reason:raise ValueError('unexpected mutation failure '+reason)
  return {'name':name,'optimized':opt,'reason':reason,'rejected':True}
with ThreadPoolExecutor(max_workers=4)as pool:
 results=list(pool.map(run,[(n,a,b,opt)for n,a,b in mutations for opt in(False,True)]))
print(json.dumps({'status':'PASS','rejections':len(results),'controls':results},indent=2,sort_keys=True))
