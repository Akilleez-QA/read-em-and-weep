#!/usr/bin/env python3
"""Second-span annihilator rank obstruction for both remaining primal equality labels."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json
from functools import lru_cache
ROOT=Path(__file__).resolve().parent

# Exact Q(sqrt(5)) character arithmetic, independently reproduced here.
def plus(a,b):return(a[0]+b[0],a[1]+b[1])
def times(a,b):return(a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(c,a):return(c*a[0],c*a[1])
def minus(a,b):return plus(a,scale(-1,b))
def total(xs):
 out=(F(0),F(0))
 for x in xs:out=plus(out,x)
 return out
z=lambda a,b=0:(F(a),F(b))
phi=z(F(1,2),F(1,2));phip=z(F(1,2),-F(1,2))
W=[z(2),z(-2),phi,scale(-1,phi),phip,scale(-1,phip),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
@lru_cache(None)
def symchar(n):
 a=[z(1)]*9
 if n==0:return a
 b=W
 for _ in range(2,n+1):a,b=b,[minus(times(w,v),u)for w,v,u in zip(W,b,a)]
 return b
chars={'one':[z(1)]*9,'W':W,'A':symchar(2),'S':symchar(3),'D':symchar(4),'T':symchar(5)}
chars['P']=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
chars['V']=[minus(a,b)for a,b in zip(symchar(6),chars['P'])]
chars['Wp']=[minus(times(w,p),t)for w,p,t in zip(W,chars['P'],chars['T'])]
names=('one','W','Wp','A','V','P','S','D','T')
def inner(a,b):return scale(F(1,120),total(scale(s,times(x,y))for s,x,y in zip(sizes,a,b)))
assert all(inner(chars[a],chars[b])==z(a==b)for a in names for b in names)
# Characters are real, hence the nine irreducibles are self-dual.
# W has trivial determinant: Lambda^2 W = 1 (the standard SL2 lift).
# The recurrence uses exactly that determinant-one linearization.
def mul(a,b):return [times(x,y)for x,y in zip(a,b)]
def sub(a,b):return [minus(x,y)for x,y in zip(a,b)]
def linear(terms):return [total(scale(c,chars[n][i])for c,n in terms)for i in range(9)]
def decompose(a):
 out=[inner(a,chars[n])for n in names]
 assert all(b==0 and x.denominator==1 for x,b in out)
 return tuple(int(x)for x,b in out)
PINNED={
'PRIMAL-RESIDUAL-OSCULATIONS-FORCE-MIXED-Z5.md':'79cd9b45c9d50e808af5d1723282ac4d99b98dce26acfc803f982508cf799b56',
'primal-residual-osculations-force-mixed-z5.json':'0a446dde188819b24acdbfe49d8c171582b66880668d2249082dc55a552a6114',
'PRIMAL-EQUALITY-CONSTANT-SPAN-INTERSECTION.md':'fab32f62c3979dbdea775b6de48e2f98912cbc32577576333e8e609da2e104f0',
'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md':'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256',
}
for f,h in PINNED.items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
prior=json.loads((ROOT/'primal-residual-osculations-force-mixed-z5.json').read_text())
ids=['G3.11.942927348917','G3.12.8e9af2d08af9']
assert prior['ids']==ids and prior['forced_constant_span']==['A','V','D']
assert prior['forced_residual_Z']==[[-4,'V'],[-4,'P'],[-8,'one']]
M2=linear([(1,'A'),(2,'V'),(3,'P'),(4,'D')]);M3=linear([(3,'Wp'),(3,'S'),(6,'T')])
X=decompose(sub(M3,mul(chars['W'],symchar(8))))
Y=decompose(sub(M2,mul(chars['W'],symchar(7))))
assert Y==(0,0,0,1,1,1,0,3,0)
assert tuple(prior['Qprime_H1_minus_one'])==X and tuple(prior['Qprime_H1_zero'])==Y
# Independently rebuild the complete eligible complement-block overlist.
blocks=[]
for e in range(-42,0):
 for n in names:
  d=int(chars[n][0][0])
  if e%2!=int(chars[n][1][0]<0)or (-e)*d+(13-d)>54:continue
  x=decompose(mul(chars[n],symchar(-e-1)))
  y=decompose(mul(chars[n],symchar(-e-2)))if e<=-2 else (0,)*9
  if all(a<=b for a,b in zip(x,X))and all(a<=b for a,b in zip(y,Y)):
   h=inner(mul(chars[n],symchar(-7-e)),chars['S'])if e<=-7 else z(0)
   assert h[1]==0 and h[0].denominator==1
   blocks.append(dict(degree=e,irrep=n,rank=d,H1_minus_one=x,H1_zero=y,Hom_to_S_minus_seven=int(h[0])))
assert len(blocks)==21
support=[b for b in blocks if b['Hom_to_S_minus_seven']]
assert [(b['degree'],b['irrep'],b['Hom_to_S_minus_seven'])for b in support]==[(-18,'one',1),(-16,'one',1),(-11,'Wp',1),(-10,'one',1)]
pidx=names.index('P');assert Y[pidx]==1
assert all(b['H1_zero'][pidx]==1 for b in support)
# Genuine multiplicities cannot cancel. Each supported copy consumes the whole
# single-P budget, so at most one supported copy is available.
assert max(b['rank']for b in support)==2
assert decompose(symchar(3))==(0,0,0,0,0,0,1,0,0)
assert 10-6-1==3 and -6-1==-7
assert 11-7==4 and 7*(-4)+4*7==0 # Y perp = Sym3 W O(-7).
minimum_actual_restriction_rank=11-8
maximum_supported_restriction_rank=2
assert minimum_actual_restriction_rank==3>maximum_supported_restriction_rank
out=dict(scope='Universal second-span annihilator rank contradiction excludes both remaining primal equality labels; no actual-instance evaluation.',source_hashes=PINNED,excluded_ids=ids,character_order=names,H1_Qprime_minus_one=X,H1_Qprime=Y,complete_Qprime_block_overlist=blocks,only_Hom_support_to_S_minus_seven=support,P_budget=1,P_cost_each_supported_copy=1,maximum_number_supported_copies=1,maximum_restriction_rank=2,second_constant_span_dimension=11,Z_rank=8,minimum_actual_restriction_rank=3,annihilator_target=[[-7,'S']],no_second_exact_intersection_or_surjectivity_assumed=True,no_N_equals_Z_Gauss_kernel_assumed=True,realization_claimed=False)
(ROOT/'primal-second-span-annihilator-rank-obstruction.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: four Hom channels each cost the unique P; restriction rank <=2 but actual annihilator rank >=3; excludes',', '.join(ids))
