#!/usr/bin/env python3
"""Executable negative controls against this reviewer's independent checker."""
from pathlib import Path
import json, subprocess, sys
root=Path(__file__).resolve().parent
original=(root/'independent.py').read_text()
mutations=[
 ('truncate_degree_ledger','range(-60,-39,2)','range(-58,-39,2)'),
 ('delete_positive_defects','sem={12*x+20*y+30*z','sem={0*12*x+0*20*y+0*30*z'),
 ('lose_upper_two_twist','target=dual(B,-6)','target=dual(B,-4)'),
 ('wrong_torsion_length','((r+t-12,0),)','((r+t-10,0),)'),
 ('omit_kernel_cubic_alternative','for top in (ZERO,unit(3)):','for top in (ZERO,):'),
 ('truncate_kernel_tail_domain','range(5,bound+1)','range(5,8)'),
 ('wrong_capacity_differential','-2*j*q','-j*q'),
 ('omit_length12_character','RESIDUES=tuple(range(0,10,2))','RESIDUES=tuple(range(0,8,2))'),
]
out=[]
for name,old,new in mutations:
 if original.count(old)!=1:raise RuntimeError('Mutation target not unique: '+name)
 path=root/('_mutation_'+name+'.py')
 path.write_text(original.replace(old,new))
 try:
  r=subprocess.run([sys.executable,'-O',str(path)],capture_output=True,text=True,cwd='/tmp')
  if r.returncode==0:raise RuntimeError('Mutation escaped: '+name)
  out.append({'mutation':name,'rejected':True,'reason':r.stderr.strip().splitlines()[-1]})
 finally:path.unlink()
print(json.dumps(out,indent=2,sort_keys=True))
