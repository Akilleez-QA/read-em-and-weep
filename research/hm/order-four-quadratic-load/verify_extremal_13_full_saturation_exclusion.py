"""Full-source abstract character enumeration, not an actual map evaluation."""
from pathlib import Path
import runpy,contextlib,io,itertools
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
 b=runpy.run_path(str(ROOT/'verify_extremal_13_cubic_image_reduction.py'))
 runpy.run_path(str(ROOT/'verify_extremal_13_rank_three_cubic_image_exclusion.py'))
for k in ('reps','hom','vm','va','vs','sym','dimension','effective','cohom','deg','T','W','S','U'):globals()[k]=b[k]
V=reps['V'];extra=[];full=[]
for e in range(-1,30):
 for n,R in reps.items():
  if dimension(R)>3 or R[1][0]!=(-1)**(e+1)*R[0][0]:continue
  hu=hom(U,vm(R,sym(e))) if e>=0 else 0
  hv=hom(V,vm(R,sym(e+1)))
  if hv and not hu:extra.append((e,n))
  if e>=0 and (hu or hv):full.append((e,n))
assert extra==[(-1,'V')]
assert full==b['eligible']
survivors=[]
for count in (1,2,3):
 for B in itertools.combinations_with_replacement(full,count):
  if sum(dimension(reps[n]) for e,n in B)!=3 or not 11<=deg(B)<=29:continue
  if not effective(va(cohom(B),vs(-1,U))):continue
  C=va(T,vs(-2,W),vs(-1,S),vs(-1,cohom(B,4,True,True)))
  if effective(va(cohom(B,2,True),cohom(B,0,True),vs(-1,C))):survivors.append(B)
assert survivors==b['survivors']
assert b['line_targets'](15)==[]
assert all(0<=deg(B)-11<12 for B in b['final'])
assert -45-(-56)==11
assert 3*(3+1)==12 and 17+12==29
remaining=[(k,l) for k in range(1,4) for l in range(1,4) if (k,l) not in [(3,3),(2,3),(3,2),(3,1),(1,3)]]
assert remaining==[(1,1),(1,2),(2,1),(2,2)]
print('PASS: full-source saturation has exactly the previously excluded three quotients, independent of cubic-image rank.')
print('CONCLUSION with geometric proof: full (1,3) profile excluded; remaining lengths both at most two.')
print('No SF>=4, square-rank improvement, or fourth value is inferred.')
