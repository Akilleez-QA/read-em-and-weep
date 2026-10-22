#!/usr/bin/env python3
"""Universal representation/degree checks, with no actual-instance data."""
from pathlib import Path
from itertools import combinations_with_replacement
import contextlib,io,runpy
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
 r=runpy.run_path(str(ROOT/'verify_extremal_31_cubic_image_rank.py'))
 q=runpy.run_path(str(ROOT/'verify_exceptional_cubic_gauss_corner.py'))
for key in ('va','vs','vm','sym','reps','zero','U','effective','dimension','hom','T'):
 globals()[key]=r[key]
def euler(d):
 return sym(d) if d>=0 else zero if d==-1 else vs(-1,sym(-d-2))
def sections(d):return sym(d) if d>=0 else zero
images=[]
for count in (1,2):
 for J in combinations_with_replacement(r['eligible'],count):
  if sum(dimension(reps[name]) for e,name in J)==2: images.append(J)
assert images==[((2,'Wp'),),((4,'Wp'),),((6,'Wp'),),((8,'W'),),((10,'W'),),
               ((9,'one'),(9,'one')),((9,'one'),(11,'one')),((11,'one'),(11,'one'))]
top_sums=[sum(sorted([j+1 for j,R in bs for _ in range(dimension(R))],reverse=True)[:2])
          for bs in r['profiles']]
assert len(top_sums)==28 and max(top_sums)==20
assert max(j for profile in q['profiles'] for j,name,c in profile)==8
assert hom(T,sym(9))==1
images=[J for J in images if J not in (((9,'one'),(9,'one')),((11,'one'),(11,'one')))]
survivors=[]
for J in images:
 m=sum(e*dimension(reps[name]) for e,name in J)
 assert 4<=m<=20 and all(e>=2 for e,name in J)
 assert sum(dimension(reps[name])*max(3-e,0) for e,name in J)<=2
 for n in (2,4,6,8):
  chi=va(U,vs(-1,sym(n+1)),*[vs(-1,vm(reps[name],euler(4-e))) for e,name in J])
  bound=va(sym(n-1),sections(n-3),*[vm(reps[name],sections(2-e)) for e,name in J])
  assert dimension(chi)==2-n+m
  if effective(va(bound,vs(-1,chi))):survivors.append((J,n))
assert survivors==[
 (((2,'Wp'),),4),(((2,'Wp'),),6),(((2,'Wp'),),8),
 (((4,'Wp'),),6),(((4,'Wp'),),8),
 (((10,'W'),),8),(((9,'one'),(11,'one')),8)]
assert vm(reps['W'],sym(4))==va(reps['S'],T)==list(sym(9))
assert va(sym(3),sym(5))==list(sym(9))
assert va(sym(7),sym(5))==U
for J,n in survivors[-2:]:
 chi=va(U,vs(-1,sym(n+1)),*[vs(-1,vm(reps[name],euler(4-e))) for e,name in J])
 bound=va(sym(n-1),sections(n-3),*[vm(reps[name],sections(2-e)) for e,name in J])
 assert chi==bound==U
 assert all(1-e-2 < -4 for e,name in J)
# H1(K(3))=0 forces min degree K>=-4, hence no low-target component.
final=survivors[:-2]
semigroup={12*a+20*b+30*c for a in range(2) for b in range(2) for c in range(2)}
for J,n in final:
 m=sum(e*dimension(reps[name]) for e,name in J)
 assert [d for d in semigroup if 0<=d<=m-4]==[0]
assert len(final)==5
print('PASS: rank-two dual cubic image leaves exactly five necessary first-quotient shapes.')
print('The actual rank-two image is saturated; both degree-twenty cases are excluded.')
print('No exclusion of the rank-one branch or entire (3,1) profile is asserted.')
