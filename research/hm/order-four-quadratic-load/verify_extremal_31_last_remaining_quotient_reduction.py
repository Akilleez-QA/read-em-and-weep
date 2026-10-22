#!/usr/bin/env python3
"""Exact abstract positive-tail exhaustion; no actual-instance computations."""
from pathlib import Path
from itertools import product
import contextlib,io,runpy
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
 b=runpy.run_path(str(ROOT/'verify_extremal_31_five_quotient_section_envelopes.py'))
for k in ('va','vs','vm','sym','reps','effective','euler','sections','vec','mu','profiles'):globals()[k]=b[k]
zero=vs(0,reps['one']);sub=lambda x,y:va(x,vs(-1,y))
one,W,Wp,A,V,P,D,S4,T=[reps[n] for n in ('one','W','Wp','A','V','P','D','S','T')]
def hom(C,j,B,t):return mu(vm(C,vm(B,sections(j-t))),one)
def fmt(C):return '+'.join(f'{mu(C,R)}{n}' for n,R in reps.items() if mu(C,R)) or '0'
chi3=sub(Wp,S4);chi4=va(vs(-1,A),V,vs(3,P))
for _,_,blocks in profiles:
 assert sub(va(*[vm(C,euler(3-j)) for j,C in blocks]),va(sym(9),vm(Wp,A)))==chi3
 assert sub(va(*[vm(C,euler(4-j)) for j,C in blocks]),va(sym(10),vm(Wp,S4)))==chi4
odd={'W','Wp','S','T'};allowed=[]
for j in range(5,33):
 for name,C in reps.items():
  if (j%2==1)!=(name in odd):continue
  h=vm(C,sym(j-5))
  if effective(sub(va(Wp,vs(2,T),S4),h)):allowed.append((j,name,h))
def tails(rem,start=0,blocks=()):
 if rem==zero:yield blocks;return
 for i in range(start,len(allowed)):
  j,name,h=allowed[i]
  if effective(sub(rem,h)):yield from tails(sub(rem,h),i,blocks+((j,name),))
rows=[]
for a,t,v,s in product(range(1,3),range(3),range(2),range(2)):
 X=va(vs(a,Wp),vs(t,T));R2=va(vs(v,V),vs(s,P));R3=sub(X,vm(R2,W))
 if not effective(R3):continue
 for tail in tails(sub(X,chi3)):
  R4=va(chi4,vs(-1,vm(R2,A)),vs(-1,vm(R3,W)),*[vs(-1,vm(reps[n],euler(4-j))) for j,n in tail])
  if not effective(R4):continue
  blocks=[(2,R2),(3,R3),(4,R4)]+[(j,reps[n]) for j,n in tail]
  dim=b['prior']['dimension'];assert sum(dim(C) for j,C in blocks)==14;assert sum(j*dim(C) for j,C in blocks)==58
  rows.append((a,t,v,s,tail,R4,blocks))
  print(len(rows),'X',fmt(X),'R2',fmt(R2),'R3',fmt(R3),'R4',fmt(R4),'tail',tail,'low',[(j,fmt(C),hom(C,j,Wp,3)) for j,C in blocks if hom(C,j,Wp,3)])
print('ALLOWED',[(j,n,fmt(h)) for j,n,h in allowed]);print('COUNT',len(rows))
# Exact frozen expected twenty rows, grouped by a,t,v,s and the tail choice.
L=[((8,'one'),(10,'one')),((9,'W'),)]
expected=[(1,0,0,0,((8,'one'),))]
expected += [(1,1,v,s,l) for v,s in ((0,0),(0,1),(1,0)) for l in L]
expected += [(1,2,1,s,l+((10,'one'),)) for s in (0,1) for l in L]
expected += [(2,0,0,0,((5,'Wp'),(8,'one')))]
expected += [(2,1,v,s,((5,'Wp'),)+l) for v,s in ((0,0),(0,1),(1,0)) for l in L]
expected += [(2,2,1,1,((5,'Wp'),)+l+((10,'one'),)) for l in L]
assert sorted((a,t,v,s,tail) for a,t,v,s,tail,_,_ in rows)==sorted(expected)
assert len(allowed)==21
# a=2 actual-map reduction: two Wp sections must be killed in twist three.
assert hom(Wp,3,one,-4)==1 and hom(Wp,3,Wp,3)==1
assert hom(Wp,5,one,-4)==0
assert hom(V,4,one,-4)==0
# The octic P high map lifts through the septic Wp evaluation.
assert mu(vm(P,sym(4)),one)==0 # Ext(P(-4),O(-10))=P Sym4 W.
assert hom(P,4,Wp,3)==1 and hom(P,4,one,-4)==1
# V sextic plus Wp septic has the unique nonsplit tensor Euler extension.
assert hom(Wp,3,V,2)==0
assert mu(vm(Wp,Wp),one)==1 and vm(Wp,W)==P
# Kernel characters for complete septic, sextic, and P sextic evaluations.
assert sub(vm(va(Wp,T),W),sym(8))==va(V,P)
assert list(sym(6))==va(V,P) and list(sym(5))==T
assert sub(vm(P,A),sym(8))==V
# All easy lifts invoked for the a=2 subcases.
for kernel_j,source_js in [(4,(4,5,8,9,10)),(4,(3,4,5,8,9,10)),(3,(5,8,9,10))]:
 assert all(j-kernel_j>=-1 for j in source_js)
# Sole possibly nonsplit scalar extension has H1(O(-2))=one.
assert euler(-2)==vs(-1,one)
# The four reduced Q shapes, all of rank 11 and degree -56.
Qs=[]
for l in L:
 Qs.append([(4,va(V,P)),(5,Wp)]+[(j,reps[n]) for j,n in l])
 Qs.append([(3,T),(5,Wp)]+[(j,reps[n]) for j,n in l]+[(10,one)])
for blocks in Qs:
 assert sum(dim(C) for j,C in blocks)==11
 assert sum(j*dim(C) for j,C in blocks)==56
 assert [(j,fmt(C)) for j,C in blocks if hom(C,j,Wp,5)]==[(5,'1Wp')]
print('PASS: exactly twenty positive splittings; a=2 actual kernels reduce to four Q shapes.')
print('No full exclusion; rank-one branch and SF>=3 / square-rank>=27 unchanged.')
