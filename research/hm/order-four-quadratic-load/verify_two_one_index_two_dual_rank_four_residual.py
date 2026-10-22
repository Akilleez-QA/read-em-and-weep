#!/usr/bin/env python3
"""Bounded dual rank-four residual classification and actual quotient consequences."""
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
PINNED={'rank-three-quotient-frontier-144.json': 'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad', 'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md': 'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256', 'EQUALITY-GAUSS-ENVELOPES-FORCE-RATIONAL-NORMAL-SUBBUNDLES.md': 'cc64326df0b4c5d3b35a195a994f1faf397cac88ec377d608aac56b29f4fb9db'}

assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
rows=json.loads((ROOT/'rank-three-quotient-frontier-144.json').read_text())['cases']
ID='G3.21.d610e381ed75';row=next(r for r in rows if r['id']==ID)
assert row['profile']=='21' and row['source_index']==2
assert row['A']==[[-8,'one'],[2,'one'],[16,'one']] and row['B']==[[-18,'one'],[-4,'one'],[6,'one']]
dims=dict(zip(names,[1,2,2,3,3,4,4,5,6]));parity={n:int(chars[n][1][0]<0)for n in names}
zero=(0,)*9
vadd=lambda *xs:tuple(map(sum,zip(*xs)))if xs else zero
vsub=lambda a,b:tuple(x-y for x,y in zip(a,b))
@lru_cache(None)
def prod(n,k):return decompose(mul(chars[n],symchar(k)))
M3v=decompose(M3);M2v=(0,0,0,1,2,3,0,4,0)
U=[(-2,'P'),(-2,'D')]
X=vsub(M3v,vadd(prod('P',1),prod('D',1)))
Y=vsub(M2v,vadd(prod('P',0),prod('D',0)))
assert X==(0,0,2,0,0,0,2,0,4) and Y==(0,0,0,1,2,2,0,3,0)
assert -54-(-18)==-36 and 13-9==4
# The residual top<=-2, so its minimum ordinary degree is -36-3*(-2)=-30.
assert -36-3*(-2)==-30
blocks=[]
for e in range(-30,-1):
 for n in names:
  if dims[n]>4 or e%2!=parity[n]:continue
  x,y=prod(n,-e-1),prod(n,-e-2)
  if all(a<=b for a,b in zip(x,X))and all(a<=b for a,b in zip(y,Y)):blocks.append((e,n,x,y))
solutions=[]
def search(start,rank,degree,x,y,bundle):
 if rank==4:
  if degree==-36 and x==X and y==Y:solutions.append(bundle)
  return
 for i in range(start,len(blocks)):
  e,n,u,v=blocks[i]
  if rank+dims[n]>4:continue
  xx,yy=vadd(x,u),vadd(y,v)
  if all(a<=b for a,b in zip(xx,X))and all(a<=b for a,b in zip(yy,Y)):search(i,rank+dims[n],degree+e*dims[n],xx,yy,bundle+[(e,n)])
search(0,0,0,zero,zero,[])
expected=[ [(-18,'one'),(-8,'one'),(-6,'one'),(-4,'one')], [(-18,'one'),(-8,'one'),(-5,'W')], [(-18,'one'),(-7,'W'),(-4,'one')], [(-18,'one'),(-6,'A')], [(-11,'Wp'),(-8,'one'),(-6,'one')], [(-11,'Wp'),(-7,'W')] ]
assert solutions==expected and len(blocks)==21
# A quotient onto B's O(-18) requires a source summand of degree<=-18.
survive=[R for R in solutions if min(e for e,n in U+R)<=-18];assert survive==expected[:4]
# U=Sym8 O(-2); its actual derivative kernel is Sym7 O(-3).
assert decompose(symchar(8))==(0,0,0,0,0,1,0,1,0)
assert decompose(symchar(7))==(0,0,1,0,0,0,0,0,1)
assert 9*(-2)==-18 and 10*(-1)==-10 and -10-(-18)-2==6
# Hom(R,O6) lifts through U: H1(Sym7 O(-3-e))=0 for every residual block.
assert all(-3-e>=1 for R in survive for e,n in R)
assert inner(symchar(14),chars['one'])==z(0) # O(-18)->O(-4) is zero.
def hom(n,e,target):return 0 if target<e else prod(n,target-e)[0]
assert [hom(n,e,-4)for e,n in survive[0][1:]]==[0,0,1]
assert [hom(n,e,-4)for e,n in survive[1][1:]]==[0,1]
assert [hom(n,e,-4)for e,n in survive[2][1:]]==[0,1]
assert [hom(n,e,-4)for e,n in survive[3][1:]]==[1]
# Evaluation kernels: W O(-5)->O(-4) has O(-6), A O(-6)->O(-4) has W O(-7).
residual_kernels=[[(-8,'one'),(-6,'one')],[(-8,'one'),(-6,'one')],[(-7,'W')],[(-7,'W')]]
forced_L=[ [(-3,'Wp'),(-3,'T')]+S for S in residual_kernels ]
assert all(sum(dims[n]for e,n in L)==10 and sum(e*dims[n]for e,n in L)==-38 for L in forced_L)
out=dict(scope='Source2 dual residual list6->4 and actual L restricted to2 types; no quotient-label exclusion or realization.',source_hashes=PINNED,equality_commit='3349988b5c3fc82dbca0741fc1b5fe70af1c7d0d',id=ID,source_pair_index=2,character_order=names,forced_top_U=U,residual_rank=4,residual_degree=-36,residual_degree_window=[-30,-2],H1_R_minus_one=X,H1_R=Y,eligible_blocks=[[e,n]for e,n,x,y in blocks],six_residual_types=solutions,excluded_by_O_minus_eighteen_quotient=solutions[4:],four_necessary_sources=[dict(R=R,Qstar=U+R,forced_L=L)for R,L in zip(survive,forced_L)],distinct_L_types=[forced_L[0],forced_L[2]],realization_claimed=False)
(ROOT/'two-one-index-two-dual-rank-four-residual.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',ID,'dual residual6->4 by actual quotient; L has2 necessary types, no label exclusion.')
