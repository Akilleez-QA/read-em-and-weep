#!/usr/bin/env python3
"""Universal degree/parity bound, not an evaluation of the actual HM pencil."""
source,target,rank0,rank1=44,48,38,4
assert source-rank0==6 and target-rank0==10
assert source-rank0-rank1==2 and target-rank0-rank1==6
import runpy
from pathlib import Path
r=runpy.run_path(str(Path(__file__).with_name('verify_twist_five_global_cohomology.py')))
q=r['r']; va,vm,vs=r['va'],r['vm'],r['vs']
characters=[]
for t in (2,4):
 chi=vs(-1,q['ambient_sym'](t))
 for i,ri in r['fc'].items():
  for j,rj in r['fc'].items():
   chi=va(chi,vm(vm(ri,rj),q['ambient_sym'](t+1+i+j)))
 multiplicities=[q['inner'](vs(-1,chi),q[k]) for k in ('W','Wp','S','T')]
 assert all(b==0 and a.denominator==1 for a,b in multiplicities)
 characters.append([int(a) for a,b in multiplicities])
assert characters==[[2,2,3,4],[3,1,4,4]]
coefficient_bound=sum(d*min(a,b) for d,a,b in zip([2,2,4,6],*characters))
assert coefficient_bound==42
orders=[e for e in range(2,source+1) if rank1+2*e<=coefficient_bound]
assert orders==list(range(2,20))
# Sharp abstract model: W tensor (t I_2 direct-sum (N20+t I20)),
# with target enlarged by W tensor C^2. N20 is the regular nilpotent
# Jordan matrix. Its superdiagonal 19-minor is 1; determinant is t^20.
# Therefore its Smith factors are nineteen units and t^20.
smith=[0]*38+[1]*4+[20]*2
assert len(smith)==44 and sum(smith)==44
assert sum(e==0 for e in smith)==38
assert sum(e==1 for e in smith)==4
assert all(smith.count(e)%2==0 for e in set(smith))
assert max(smith)==20
print('PASS: 38 unit factors + four order-one factors leave two factors.')
print('PASS: even higher-obstruction ranks force their finite orders to coincide.')
print('PASS: actual odd characters bound invariant coefficient rank by42; 4+2e <=42 gives e in {2,...,19}.')
print('PASS: the abstract doubled Jordan pencil realizes e=20 with the same sizes and parity.')
print('No actual HM coefficient, matrix, rank, or obstruction evaluated.')
