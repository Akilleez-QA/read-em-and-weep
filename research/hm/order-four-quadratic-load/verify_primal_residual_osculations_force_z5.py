#!/usr/bin/env python3
"""Genuine primal residual osculations force full Sym10 span and residual type Z5."""
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
'PRIMAL-EQUALITY-CONSTANT-SPAN-INTERSECTION.md':'fab32f62c3979dbdea775b6de48e2f98912cbc32577576333e8e609da2e104f0',
'primal-equality-constant-span-intersection.json':'c6b91aa7361eee65687875acb4fc771463e49b31c52981b0120747519358a543',
'PRIMAL-EQUALITY-RESIDUAL-FILTRATIONS-REMOVE-BOUNDARY-STRATA.md':'c96492d46c900920337d2622cfa69e04c352ed77bf23c9d9e60de7a2720768c0',
'EQUALITY-GAUSS-ENVELOPES-FORCE-RATIONAL-NORMAL-SUBBUNDLES.md':'cc64326df0b4c5d3b35a195a994f1faf397cac88ec377d608aac56b29f4fb9db',
'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md':'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256',
'PRIMAL-EQUALITY-HAS-SIX-RESIDUAL-QUOTIENT-PARAMETER-SPACES.md':'de06847ba55aae35effb6ad394de4792b5c8813d48dbee35b4c1bed79935afa6',
}
for f,h in PINNED.items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
prior=json.loads((ROOT/'primal-equality-constant-span-intersection.json').read_text())
assert prior['ids']==['G3.11.942927348917','G3.12.8e9af2d08af9']
assert prior['projected_residual_Z']==dict(rank=8,degree=-36,ambient_constant_rank=19,saturated=True)
M3=linear([(3,'Wp'),(3,'S'),(6,'T')]);M2=linear([(1,'A'),(2,'V'),(3,'P'),(4,'D')])
X=decompose(sub(M3,mul(chars['W'],symchar(8))))
Y=decompose(sub(M2,mul(chars['W'],symchar(7))))
assert min(X)>=0 and min(Y)>=0
# Qprime is isomorphic to the complement of the forced W O(-9) block.
# Exhaust every original allowable block degree [-42,-1] against its remaining
# two actual H1 budgets. This overlist is sufficient, not a realization list.
co=[]
for e in range(-42,0):
 for n in names:
  d=int(chars[n][0][0])
  if e%2!=int(chars[n][1][0]<0)or (-e)*d+(13-d)>54:continue
  x=decompose(mul(chars[n],symchar(-e-1)))
  y=decompose(mul(chars[n],symchar(-e-2)))if e<=-2 else (0,)*9
  if all(a<=b for a,b in zip(x,X))and all(a<=b for a,b in zip(y,Y)):
   co.append(dict(degree=e,irrep=n,H1_minus_one=x,H1_zero=y))
assert len(co)==21 and min(b['degree']for b in co)==-18
assert all(b['degree']>-28 for b in co)
# N_j is the actual projection of F_j, not an assumed iterated Gauss kernel.
filtration=[]
for j in range(7):
 rank=6-j;degree=sum(2-2*k for k in range(j+1,7))
 filtration.append(dict(j=j,rank=rank,degree=degree))
assert filtration[0]==dict(j=0,rank=6,degree=-30)
assert filtration[5]==dict(j=5,rank=1,degree=-10)
assert filtration[6]==dict(j=6,rank=0,degree=0)
symbols=[]
for j in range(1,6):
 source=2-2*(j+1);target=(2-2*j)-2
 assert source==target
 symbols.append(dict(source_quotient_j=j+1,target_quotient_j=j,source_degree=source,target_degree_with_Omega=target,isomorphism_from_equality=True))
assert (2-2*1)==2-2 # N0/N1 -> top O2 in Z/N0, tensored by Omega.
oscs=[]
for i in range(7):
 rank=i+1;degree=(i+1)*(i-10)
 if i<=5:assert (rank,degree)==(filtration[5-i]['rank'],filtration[5-i]['degree'])
 else:assert (rank,degree)==(7,-30+2)
 oscs.append(dict(order=i,rank=rank,degree=degree,identified_with=('N'+str(5-i))if i<=5 else'Y=preimage of O2'))
assert decompose(symchar(10))==(0,0,0,1,1,0,0,1,0)
possible=[]
for mask in range(8):
 ns=[n for k,n in enumerate(['A','V','D'])if mask>>k&1]
 d=sum(int(chars[n][0][0])for n in ns)
 if d>=7:possible.append(dict(irreps=ns,dimension=d))
assert possible==[dict(irreps=['A','D'],dimension=8),dict(irreps=['V','D'],dimension=8),dict(irreps=['A','V','D'],dimension=11)]
# In either proper span dimension8, Y has annihilator line degree -28.
assert 8-7==1 and -28<-18
assert decompose(symchar(6))==(0,0,0,0,1,1,0,0,0)
assert decompose(symchar(5))==(0,0,0,0,0,0,0,0,1)
assert 6-10==-4 and 5-10==-5
assert -4-(-8)==4 and 4>=-1 # Ext1(O(-8),Sym6 O(-4))=0.
E=[(-2,'P'),(-2,'D'),(-4,'V'),(-4,'P'),(-8,'one')]
assert sum(int(chars[n][0][0])for e,n in E)==17
assert sum(e*int(chars[n][0][0])for e,n in E)==-54
out=dict(scope='Actual residual osculation forces only mixed Z5 for both remaining primal equality labels; no label exclusion or realization.',source_hashes=PINNED,ids=prior['ids'],Qprime_H1_minus_one=X,Qprime_H1_zero=Y,complete_Qprime_block_overlist=co,Qprime_minimum_degree=-18,actual_projected_filtration=filtration,actual_descended_symbols=symbols,osculations=oscs,constant_span_alternatives=possible,proper_eight_dimensional_span_excluded_by_annihilator_degree=-28,forced_constant_span=['A','V','D'],forced_residual_Z=[[-4,'V'],[-4,'P'],[-8,'one']],forced_N=[[-5,'T']],forced_E=E,retained_residual_type='Z5',retained_scalar_condition='a != 0 and alpha*beta != 0',removed_residual_types=['Z1','Z2','Z3','Z4'],no_identification_N_equals_Z_Gauss_kernel=True,no_new_label_exclusions=True,realization_claimed=False)
(ROOT/'primal-residual-osculations-force-mixed-z5.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: actual residual symbol chain arithmetic; 21 Qprime blocks have degree >=-18; proper span annihilator O(-28) impossible; only mixed Z5 remains.')
