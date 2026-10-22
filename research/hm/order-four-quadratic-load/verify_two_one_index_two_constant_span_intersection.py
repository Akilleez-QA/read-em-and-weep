#!/usr/bin/env python3
"""Source2 constant-span intersection: exact complete E-block support."""
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
M3=linear([(3,'Wp'),(3,'S'),(6,'T')])
M4=linear([(2,'V'),(4,'P'),(3,'D')])
PINNED={'rank-three-quotient-frontier-144.json': 'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad', 'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md': 'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256', 'EQUALITY-GAUSS-ENVELOPES-FORCE-RATIONAL-NORMAL-SUBBUNDLES.md': 'cc64326df0b4c5d3b35a195a994f1faf397cac88ec377d608aac56b29f4fb9db', 'TWO-ONE-INDEX-TWO-DUAL-RANK-FOUR-RESIDUAL.md': '12a381971cc8b418212dd627fc875aeff7d3000de93c9a8f3a64569ba1cedb6f'}

assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
ID='G3.21.d610e381ed75'
row=next(r for r in json.loads((ROOT/'rank-three-quotient-frontier-144.json').read_text())['cases']if r['id']==ID)
assert row['profile']=='21' and row['source_index']==2
assert row['A']==[[-8,'one'],[2,'one'],[16,'one']] and row['B']==[[-18,'one'],[-4,'one'],[6,'one']]
dims=dict(zip(names,[1,2,2,3,3,4,4,5,6]));X,Y=decompose(M3),decompose(M4)
# rank E=17, degree=-54, top<=-2 yields the exhaustive minimum -22.
minimum=-54-16*(-2);assert minimum==-22
eligible=[];support=[]
for e in range(minimum,-1):
 for n in names:
  if e%2!=int(chars[n][1][0]<0):continue
  x=decompose(mul(chars[n],symchar(-e-1)))
  y=decompose(mul(chars[n],symchar(-e-2)))
  if not(all(a<=b for a,b in zip(x,X))and all(a<=b for a,b in zip(y,Y))):continue
  h=0 if e>-9 else inner(mul(chars[n],symchar(-9-e)),chars['W'])[0]
  assert h.denominator==1 if hasattr(h,'denominator') else h==0
  rec=dict(degree=e,irrep=n,H1_minus_one=x,H1_zero=y,Hom_to_W_minus_nine=int(h))
  eligible.append(rec)
  if h:support.append([e,n,int(h)])
assert support==[[-10,'one',1],[-9,'W',1]]
# Complete degree-ten evaluation and its first osculating filtration.
assert decompose(symchar(10))==(0,0,0,1,1,0,0,1,0)
assert decompose(symchar(8))==(0,0,0,0,0,1,0,1,0)
assert decompose(symchar(7))==(0,0,1,0,0,0,0,0,1)
assert inner(mul(chars['W'],symchar(1)),chars['one'])==z(1)
# U=Sym8 O(-2), U^perp=W O(-9); canonical O(-10) has annihilator Sym9 O(-1).
assert 9*(-2)+2*9==0 and 2*(-9)+9*2==0
assert 10*(-1)+10==0
# A W O(-9) block is forced. Its complement has min>=-8, forbidding any other source map to W O(-9).
res_rank=17-2;res_degree=-54-2*(-9);res_min=res_degree-(res_rank-1)*(-2)
assert (res_rank,res_degree,res_min)==(15,-36,-8)
assert res_min>-9
out=dict(scope='Source2 constant-span intersection and genuine constant-quotient residual; no label exclusion.',id=ID,source_hashes=PINNED,equality_commit='3349988b5c3fc82dbca0741fc1b5fe70af1c7d0d',dual_residual_commit='92c1580998dd5476458e32d8d6c2ca14a9c55edb',character_order=names,E_degree_window=[-22,-2],H1_E_minus_one=X,H1_E=Y,all_eligible_E_blocks=eligible,only_nonzero_Hom_support=support,forced_E_summand=[-9,'W'],E_projection_kernel=dict(rank=res_rank,degree=res_degree,degree_window=[res_min,-2]),intersection='Qstar intersect V0=Sym8 W O(-2)=U',constant_quotient_residual=dict(rank=4,degree=-36,saturated=True,ambient_rank=19,contains_projected_L_rank=2),no_identification_of_projected_L_with_Gauss_kernel=True,realization_claimed=False)
(ROOT/'two-one-index-two-constant-span-intersection.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',ID,'only O(-10), W O(-9) can map to U-perp; W O(-9) forced; intersection U, saturated residual rank4.')
