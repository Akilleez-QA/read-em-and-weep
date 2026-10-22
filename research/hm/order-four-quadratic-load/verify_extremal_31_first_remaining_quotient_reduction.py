#!/usr/bin/env python3
"""Exact abstract characters and splitting tails, not actual-instance experiments."""
from pathlib import Path
from itertools import product
import contextlib, io, runpy
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
    b=runpy.run_path(str(ROOT/'verify_extremal_31_five_quotient_section_envelopes.py'))
for k in ('va','vs','vm','sym','reps','effective','euler','sections','vec','mu','profiles'):
    globals()[k]=b[k]
zero=vs(0,reps['one'])
sub=lambda x,y:va(x,vs(-1,y))
one,W,Wp,A,V,P,D,S4,T=[reps[n] for n in ('one','W','Wp','A','V','P','D','S','T')]
def hom(C,j,B,t):return mu(vm(C,vm(B,sections(j-t))),one)
chi3=zero;chi4=va(vs(2,V),vs(2,P));odd={'W','Wp','S','T'}; allowed=[]
for j in range(5,31):
 for name,C in reps.items():
  if (j%2==1)!=(name in odd):continue
  h=vm(C,sym(j-5))
  if effective(sub(va(Wp,T,S4),h)):allowed.append((j,name,h))
def tails(rem,start=0,blocks=()):
 if rem==zero:yield blocks;return
 for i in range(start,len(allowed)):
  j,name,h=allowed[i]
  if effective(sub(rem,h)):yield from tails(sub(rem,h),i,blocks+((j,name),))
def fmt(C):return '+'.join(f'{mu(C,R)}{n}' for n,R in reps.items() if mu(C,R)) or '0'
rows=[]
for a,s,t,d in product(range(2),repeat=4):
 X=va(vs(a,Wp),vs(s,S4),vs(t,T)); R2=vs(d,D); R3=sub(X,vm(R2,W))
 if not effective(R3):continue
 for tail in tails(X):
  R4=va(chi4,vs(-1,vm(R2,A)),vs(-1,vm(R3,W)),*[vs(-1,vm(reps[n],euler(4-j))) for j,n in tail])
  if not effective(R4):continue
  blocks=[(2,R2),(3,R3),(4,R4)]+[(j,reps[n]) for j,n in tail]
  dim=b['prior']['dimension']; assert sum(dim(C) for j,C in blocks)==14;assert sum(j*dim(C) for j,C in blocks)==56
  rows.append((a,s,t,d,tail,R4))
  print(len(rows), 'X',fmt(X),'d',d,'R3',fmt(R3),'R4',fmt(R4),'tail',tail,'low',[(j,fmt(C),hom(C,j,Wp,3)) for j,C in blocks if hom(C,j,Wp,3)])
print('count',len(rows))
expected=[(0,0,0,0,()),(0,0,1,0,((10,'one'),)),(0,1,1,1,((8,'one'),(10,'one'))),(0,1,1,1,((9,'W'),)),(1,0,0,0,((5,'Wp'),)),(1,0,1,0,((5,'Wp'),(10,'one'))),(1,1,1,1,((5,'Wp'),(8,'one'),(10,'one'))),(1,1,1,1,((5,'Wp'),(9,'W')))]
assert [(a,s,t,d,tail) for a,s,t,d,tail,R4 in rows]==expected
for _,_,blocks in profiles:
 assert sub(va(*[vm(C,euler(3-j)) for j,C in blocks]),va(sym(7),vm(Wp,A)))==zero
 assert sub(va(*[vm(C,euler(4-j)) for j,C in blocks]),va(sym(8),vm(Wp,S4)))==chi4
assert hom(T,3,Wp,3)==0 and hom(Wp,3,one,-2)==0
assert hom(D,2,Wp,3)==0
assert hom(V,4,Wp,3)==0 and hom(P,4,Wp,3)==1
assert vm(Wp,W)==P
assert hom(Wp,5,one,-2)==1
assert hom(V,4,one,-2)==1 and hom(P,4,one,-2)==1
# Tensor Euler low kernel; complete quintic/quartic high kernels.
assert sub(vm(P,W),vm(Wp,A))==Wp
assert sub(vm(T,W),sym(6))==D
assert sub(vm(D,W),sym(5))==S4
# All triangular high/low lifts used in the proof have H1 degree >= -1.
for kernel_j,source_js in [(4,(4,5,10)),(3,(3,4,5,8,9,10)),(5,(8,9,10))]:
 assert all(j-kernel_j>=-1 for j in source_js)
# Exceptional P-low-zero case: next quotient has W(-11), inaccessible.
assert all(hom(C,j,W,11)==0 for j,C in [(3,S4),(4,V),(4,P)])
# If residual high f uses only Wp(-5), kernel has a single low-map line.
assert all(hom(C,4,Wp,5)==0 for C in (V,P))
assert hom(one,12,Wp,5)==1
print('PASS: exactly eight positive K splittings; actual-kernel reduction checks passed.')
print('No full exclusion is asserted; SF >= 3 and square rank >= 27 unchanged.')
