#!/usr/bin/env python3
"""One quotient exclusion from an impossible H1 surjection; abstract characters only."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import hashlib, json
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
PINNED={'rank-three-quotient-frontier-144.json': 'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad', 'two-one-rank-eleven-endpoint-splittings.json': '4704e794183cb1a2b0bf5069e3baedafeedc9ae186c40dea2917766100d23a16'}

assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
data={f:json.loads((ROOT/f).read_text())for f in PINNED}
front=data['rank-three-quotient-frontier-144.json']
ID='G3.21.bf8462f3a0d7'
f=next(c for c in front['cases']if c['id']==ID)
assert f['status']=='not_excluded' and f['profile']=='21' and f['source_index']==11
A=((-5,'Wp'),(16,'one'));B=((-18,'one'),(3,'Wp'));J=((-7,'Wp'),(14,'one'))
assert f['A']==[list(x)for x in A] and f['B']==[list(x)for x in B]
p=data['two-one-rank-eleven-endpoint-splittings.json']['pairs'][11]
assert p['source_pair_index']==11 and p['A']==f['A'] and p['B']==f['B']
assert p['retained_second_defects']==[0]
# E embeds in M3 O(-1), and K embeds in E: H0(K(-2))=0.
# Thus H1(K(-2))=-chi(K(-2))=chi(A(-2))-chi(E(-2)).
# Euler formula: chi(O(d))=Sym^d W for d>=0, -Sym^(-d-2) W for d<=-2.
e=decompose(sub(M4,mul(M3,W)))
a=decompose(sub(symchar(14),mul(chars['Wp'],symchar(5))))
k=tuple(x-y for x,y in zip(a,e))
j=decompose(mul(chars['Wp'],symchar(7)))
assert a==(0,0,0,0,1,0,0,0,0)
assert e==(0,0,0,-3,-4,-5,0,-6,0)
assert k==(0,0,0,3,5,5,0,6,0)
assert j==(1,0,0,1,1,1,0,1,0)
assert k[0]==0 and j[0]==1
# H1(K(-2)) -> H1(J(-2)) must be onto since H2(M(-2))=0.
assert any(x<y for x,y in zip(k,j))
assert front['not_excluded']==144 and front['remaining_by_profile']=={'11':122,'12':10,'21':12}
certificate=dict(scope='One necessary quotient pair excluded, no actual map evaluation or realization claim.',source_hashes=PINNED,id=ID,profile='21',A=A,B=B,s=0,J=J,twist=-2,character_order=names,chi_E=e,chi_A=a,H1_K=k,H1_J=j,obstruction='An equivariant surjection cannot map zero trivial multiplicity onto one trivial multiplicity.',previous_frontier=144,new_frontier=143,remaining_by_profile={'11':122,'12':10,'21':11})
(ROOT/'two-one-wprime-sixteen-quotient-exclusion.json').write_text(json.dumps(certificate,indent=2)+'\n')
print('PASS:',ID,'excluded; trivial multiplicity 0 cannot surject onto 1 at twist -2.')
print('Frontier 144 -> 143; profile counts 122, 10, 11. No actual realization claimed.')
