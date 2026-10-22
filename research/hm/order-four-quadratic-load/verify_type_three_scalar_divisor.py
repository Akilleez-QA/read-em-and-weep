#!/usr/bin/env python3
"""Universal type III extension and defining-biform existence. No actual coefficients."""
import runpy,json
from pathlib import Path
r=runpy.run_path(str(Path(__file__).with_name('verify_pure_cross_block_couplings.py')))
inner,sy,vm=r['inner'],r['sy'],r['vm']
row=r['rows'][2]
assert [(r['couplings']([v],2),r['diagonal']([v],6)) for v in row]==[(2,1),(1,0)]
cs=[]
for idx,row in enumerate(r['rows'],1):
 for p in range(max(d for R,d in row)+1):
  for q in range(7):
   if p+q not in (12,20,24):continue
   rem=sum(inner(sy(6-q),vm(R,sy(d-p))) for R,d in row if d>=p)
   if not rem:continue
   defining=inner(sy(p),sy(q))
   diag=inner(r['one'],sy(p+q))
   assert defining>=diag==1
   cs.append(dict(type=idx,p=p,q=q,residual=rem,defining=defining,diagonal_image=diag))
assert [(c['p'],c['q']) for c in cs if c['type']==3]==[(9,3)]
print('PASS: type III low/high (coupling, diagonal) multiplicities are (2,1), (1,0).')
print('PASS: every surviving residual candidate admits an invariant defining biform not divisible by the diagonal.')
print(json.dumps(cs,indent=2))
