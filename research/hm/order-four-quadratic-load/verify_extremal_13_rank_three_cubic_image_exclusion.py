#!/usr/bin/env python3
"""Universal character/tail check. No actual-instance coefficients or ranks."""
from pathlib import Path
import contextlib,io,runpy
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
 b=runpy.run_path(str(ROOT/'verify_extremal_31_last_remaining_quotient_reduction.py'))
 runpy.run_path(str(ROOT/'verify_extremal_13_cubic_image_reduction.py'))
for k in ('va','vs','vm','sym','reps','effective','euler','sections','zero','mu','fmt','hom'):
 globals()[k]=b[k]
dim=b['dim']; sub=lambda x,y:va(x,vs(-1,y))
one,W,Wp,V,P,D,T=[reps[n] for n in ('one','W','Wp','V','P','D','T')]
odd={'W','Wp','S','T'}
def tail_splittings(c3,c4):
 # H0(K(3))=0; all summands have degree at most -4.
 # Each negative tail contributes dim(R)*(j-4) to H1(K(3)).
 budget=vs(-1,c3); assert effective(budget)
 allowed=[]
 for j in range(5,dim(budget)+5):
  for n,C in reps.items():
   if (j%2==1)!=(n in odd):continue
   cost=vm(C,sym(j-5))
   if effective(sub(budget,cost)):allowed.append((j,n,cost))
 def tails(rem,start=0,tail=()):
  if rem==zero:
   yield tail # Includes the empty tail when the budget is zero.
   return
  for i in range(start,len(allowed)):
   j,n,cost=allowed[i]
   if effective(sub(rem,cost)):
    yield from tails(sub(rem,cost),i,tail+((j,n),))
 out=[]
 for tail in tails(budget):
  r4=sub(c4,va(zero,*[vm(reps[n],euler(4-j)) for j,n in tail]))
  if effective(r4):out.append((r4,tail))
 return out
expected={14:[(va(vs(2,V),D),((5,'Wp'),(8,'one')))],
 16:[(va(vs(2,V),P),((5,'Wp'),(6,'one'),(8,'one'))),
     (va(vs(2,V),P),((5,'Wp'),(7,'W')))]}
for d in (14,16):
 c3=sub(vs(2,T),sym(d+3))
 c4=sub(va(vm(vs(2,T),W),V),sym(d+4))
 rows=tail_splittings(c3,c4)
 assert rows==expected[d],[(fmt(c),t) for c,t in rows]
 for c,tail in rows:
  assert dim(c)+sum(dim(reps[n]) for j,n in tail)==14
  assert 4*dim(c)+sum(j*dim(reps[n]) for j,n in tail)==48+d
  assert mu(c,V)==2
  print('A0=Wp(-3)+O(%d): K='%d,fmt(c)+'(-4)',tail)
 # Endpoint target A0(-2)=Wp(-5)+O(d-2).
 assert hom(V,4,Wp,5)==0
 assert hom(V,4,one,2-d)==1
# Third image: A0=Wp(-1)+O(4), K pure of degree -56.
U=va(Wp,vs(2,T))
c3=sub(U,va(vm(Wp,sym(2)),sym(7)))
c4=sub(va(vm(U,W),V),va(vm(Wp,sym(3)),sym(8)))
assert c3==zero and c4==va(vs(2,V),vs(2,P))
assert tail_splittings(c3,c4)==[(c4,())]
assert hom(V,4,Wp,3)==0 and hom(V,4,one,-2)==1
# Internal derivative target has all degrees <=-6: no ordinary maps
# O(-4)->O(-j-2) for j>=4. Bound is symbolic, not instance testing.
assert sections(-2)==zero
print('PASS: every exact cubic-rank-three image forces a horizontal V(-4).')
print('Thus cubic-image rank is at most two in (1,3); no global SF bound changed.')
