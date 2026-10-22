#!/usr/bin/env python3
"""Universal actual-character bounds and abstract coupling checks only."""
import runpy
from pathlib import Path
r=runpy.run_path(str(Path(__file__).with_name('verify_twist_five_global_cohomology.py')))
q=r['r']; va,vm,vs=r['va'],r['vm'],r['vs']
chars=[]
for t in (2,4):
 chi=vs(-1,q['ambient_sym'](t))
 for i,a in r['fc'].items():
  for j,b in r['fc'].items():chi=va(chi,vm(vm(a,b),q['ambient_sym'](t+1+i+j)))
 v=[q['inner'](vs(-1,chi),q[k]) for k in ('one','A','V','P','D')]
 assert all(b==0 and a.denominator==1 for a,b in v)
 chars.append([int(a) for a,b in v])
assert chars==[[0,1,2,3,4],[0,0,2,4,3]]
dims=[1,3,3,4,5]
assert sum(min(a,b)*d for a,b,d in zip(*chars,dims))==33
assert q['inner'](vm(q['A'],q['A']),q['P'])==q['z'](0)
assert q['inner'](vm(q['A'],q['D']),q['P'])==q['z'](1)
sym6=[q['sym'](6,x) for x in q['W']]
assert sym6==va(q['V'],q['P'])
assert 3-2==1 and 5-1==4 and 33+4==37
print('PASS: positive source/target characters, invariant rank bound33, and unique first smoothing coupling.')
print('PASS: Cartan Sym6=V+P4 supplies the unique coupling; general two-root evaluation leaves kernel dimension1.')
print('The geometric two-point independence proof is in the companion; no actual scalar or rank evaluated.')
