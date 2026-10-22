#!/usr/bin/env python3
"""Primal equality forces a dual degree-one section; exact complete block check."""
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
M2=linear([(1,'A'),(2,'V'),(3,'P'),(4,'D')])
PINNED={
'rank-three-quotient-frontier-144.json':'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad',
'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md':'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256',
'EQUALITY-GAUSS-ENVELOPES-FORCE-RATIONAL-NORMAL-SUBBUNDLES.md':'cc64326df0b4c5d3b35a195a994f1faf397cac88ec377d608aac56b29f4fb9db',
'equality-gauss-rational-normal-subbundles.json':'c1930c3f8977515f75fc9359866dd9a143e2101322a3fd80a352a8357d15377f',
}
for f,h in PINNED.items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
ids=['G3.11.942927348917','G3.12.8e9af2d08af9','G3.21.45ca6278cbfc']
rows=[next(r for r in json.loads((ROOT/'rank-three-quotient-frontier-144.json').read_text())['cases']if r['id']==i)for i in ids]
assert [r['profile']for r in rows]==['11','12','21']
assert [r['source_index']for r in rows]==[70,8,1]
for r in rows:
 assert r['A']==[[-8,'one'],[2,'one'],[6,'one']]
 assert r['B']==[[-8,'one'],[-4,'one'],[6,'one']]
X,Y=decompose(M3),decompose(M2)
# Actual Q* is negative, rank13, degree-54. Every line degree is at least
# -54 - 12*(-1)=-42. Repeated irreducible blocks obey the sharper rank bound.
minimum=-54-12*(-1);assert minimum==-42
eligible=[];support=[]
for e in range(minimum,0):
 for n in names:
  d=int(chars[n][0][0])
  if e%2!=int(chars[n][1][0]<0):continue
  if (-e)*d+(13-d)>54:continue
  x=decompose(mul(chars[n],symchar(-e-1)))
  y=decompose(mul(chars[n],symchar(-e-2)))if e<=-2 else (0,)*9
  if not(all(a<=b for a,b in zip(x,X))and all(a<=b for a,b in zip(y,Y))):continue
  h=inner(mul(chars[n],symchar(-9-e)),chars['W'])if e<=-9 else z(0)
  assert h[1]==0 and h[0].denominator==1
  twist1=decompose(mul(chars[n],symchar(-e-3)))if e<=-3 else (0,)*9
  rec=dict(degree=e,irrep=n,H1_minus_one=x,H1_zero=y,H1_plus_one=twist1,Hom_to_W_minus_nine=int(h[0]))
  eligible.append(rec)
  if h[0]:support.append(rec)
expected=[(1,'Wp'),(1,'S'),(1,'T'),(2,'V'),(2,'P'),(2,'D'),(3,'Wp'),(3,'T'),(4,'one'),(4,'V'),(4,'P'),(5,'W'),(5,'Wp'),(6,'one'),(6,'A'),(7,'W'),(7,'S'),(8,'one'),(8,'A'),(9,'W'),(10,'one'),(11,'Wp'),(16,'one'),(17,'W'),(18,'one'),(28,'one')]
assert len(eligible)==26 and {(-r['degree'],r['irrep'])for r in eligible}==set(expected)
assert [(r['degree'],r['irrep'],r['Hom_to_W_minus_nine'])for r in support]==[(-28,'one',1),(-10,'one',1),(-9,'W',1)]
chi=decompose(sub(M3,mul(M2,chars['W'])))
assert chi==(-0,-1,0,0,0,0,-2,0,-3)
wp=names.index('Wp')
assert all(r['H1_plus_one'][wp]==1 for r in support)
assert decompose(symchar(10))==(0,0,0,1,1,0,0,1,0)
assert decompose(symchar(8))==(0,0,0,0,0,1,0,1,0)
assert sum(int(chars[n][0][0])*m for n,m in zip(names,decompose(symchar(10))))==11
assert 9*(-2)+2*9==0 # C8 and the dual of its annihilator have opposite degrees.
# If H0(Q*(1)) has no Wp, chi_Wp=0 forces H1_Wp=0. This removes every
# supported block, hence the whole equivariant Hom into W O(-9) vanishes.
no_wp=[r for r in eligible if r['H1_plus_one'][wp]==0]
assert all(r['Hom_to_W_minus_nine']==0 for r in no_wp)
out=dict(scope='Universal annihilator obstruction; excludes one primal equality label, no instance evaluation.',source_hashes=PINNED,equality_commit='3349988b5c3fc82dbca0741fc1b5fe70af1c7d0d',character_order=names,dual_degree_window=[-42,-1],H1_Qstar_minus_one=X,H1_Qstar=Y,chi_Qstar_plus_one=chi,all_eligible_dual_blocks=eligible,only_Hom_support=support,necessary_for_all_three_primal_equalities='Wp occurs in H0(Qstar(1))',profile_consequences=[dict(id=r['id'],profile=r['profile'],source_index=r['source_index'],k=int(r['profile'][0]),excluded=r['profile']=='21')for r in rows],excluded_ids=[ids[2]],no_automatic_exact_intersection_or_quotient_connection=True,realization_claimed=False)
(ROOT/'primal-equality-annihilator-forces-dual-degree-one-sections.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: 26 exhaustive Q* blocks; all three Hom channels force Wp in H0(Q*(1)); excludes',ids[2])
