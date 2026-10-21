#!/usr/bin/env python3
"""Universal type VI two-scalar gate; no actual coefficient evaluation."""
import runpy
from pathlib import Path
r=runpy.run_path(str(Path(__file__).with_name('verify_pure_cross_block_couplings.py')))
row=r['rows'][5]
assert [(r['couplings']([v],2),r['diagonal']([v],6)) for v in row]==[(0,0),(1,0),(2,1)]
candidates=[]
for p in range(15):
 for q in range(7):
  if p+q not in (12,20,24):continue
  dim=sum(r['inner'](r['sy'](6-q),r['vm'](R,r['sy'](d-p))) for R,d in row if d>=p)
  if dim:candidates.append((p,q))
assert candidates==[(10,2),(14,6)]
assert all(p>5 for p,q in candidates)
print('PASS: type VI components have (coupling,diagonal) dimensions (0,0),(1,0),(2,1).')
print('PASS: necessary common-divisor bidegrees are (10,2),(14,6), both killing the low W-prime component.')
print('No actual lambda or mu evaluated.')
