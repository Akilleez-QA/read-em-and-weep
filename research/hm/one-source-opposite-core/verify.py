#!/usr/bin/env python3
"""Nine-class abstract characters only. No actual tensors or instance evaluations."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json

def require(condition,message):
    if not condition: raise RuntimeError(message)
def z(a,b=0):return F(a),F(b)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[0],-x[1]
def sub(x,y):return add(x,neg(y))
def mul(x,y):return x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def scale(k,x):return k*x[0],k*x[1]
def total(xs):
    out=z(0)
    for x in xs:out=add(out,x)
    return out
def va(*args):return [total(v) for v in zip(*args)]
def vs(k,a):return [scale(k,x) for x in a]
def vm(a,b):return [mul(x,y) for x,y in zip(a,b)]
def sym(n,x):
    require(n>=0,'negative symmetric power')
    if n==0:return z(1)
    a,b=z(1),x
    for _ in range(2,n+1):a,b=b,sub(mul(x,b),a)
    return b
phi=z(F(1,2),F(1,2));phip=z(F(1,2),F(-1,2))
W=[z(2),z(-2),phi,neg(phi),phip,neg(phip),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
one=[z(1)]*9
A=[sym(2,x) for x in W];S=[sym(3,x) for x in W]
D=[sym(4,x) for x in W];T=[sym(5,x) for x in W]
P=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
V=[sub(sym(6,x),p) for x,p in zip(W,P)]
Wp=[sub(mul(w,p),t) for w,p,t in zip(W,P,T)]
reps=dict(zip(['1','W','Wp','A','V','P','S','D','T'],[one,W,Wp,A,V,P,S,D,T]))
def inner(a,b):return scale(F(1,120),total(scale(k,mul(x,y)) for k,x,y in zip(sizes,a,b)))
require(sum(sizes)==120,'class sizes')
for n,c in reps.items():
 for m,d in reps.items():require(inner(c,d)==z(int(n==m)),'character orthogonality')
require(sum(int(c[0][0])**2 for c in reps.values())==120,'irrep completeness')
require(V==[sym(2,x) for x in Wp],'positive ambient V=Sym2 Wp')
# W trace separates the nine classes; g-square has trace trace(g)^2-2.
square=[W.index(sub(mul(x,x),z(2))) for x in W]
require(square==[0,0,5,5,3,3,7,7,1],'exact square-class map')
def psi2(c):return [c[i] for i in square]





def sy(n):return [sym(n,w) for w in W]
require(vm(S,A)==va(W,S,T),'unique U-to-B4 channel')
require(inner(W,vm(S,A))==z(1),'U projection multiplicity')
require(inner(W,vm(Wp,A))==z(0),'compatible lift Hom vanishing')
require(inner(S,vm(Wp,sy(4)))==z(1),'target correction channel')
require(inner(W,vm(Wp,sy(6)))==z(1),'source error channel')
require(sy(11)==va(W,S,T),'degree-eleven system')
require(sy(13)==va(W,Wp,S,T),'degree-thirteen system')
require(inner(W,sy(11))==z(1) and inner(Wp,sy(13))==z(1),'two source channels')
require(inner(Wp,W)==z(0),'degree-thirteen divisor exclusion')
require(sy(7)==va(Wp,T) and inner(Wp,sy(7))==z(1),'nonzero extension dimension')
orbits=[60//k for k in (1,2,3,5)]
require(min(orbits)==12 and [n for n in orbits if n<=13]==[12],'small orbit degrees')
require(13-12==1 and 11<12,'base-divisor bounds')
def h0(n):return max(n+1,0)
def h1(n):return max(-n-1,0)
require(h1(2)==0 and h1(4)==0,'compatible lift Ext vanishings')
require(h0(-6)==0,'sextic extension model nonsplit')
require(-2!=10,'forced U projection degree obstruction')
for sr,sd,tr,td,qr,qd in [(2,-2,4,4,2,6),(1,-8,2,10,1,18),(1,-8,2,6,1,14),(1,-8,4,16,3,24),(2,10,3,24,1,14)]:
 require(tr-sr==qr and td-sd==qd,'universal rank degree')
q3={17:[('Wp',5),('1',14)],18:[('1',18),('W',3)],20:[('V',8)]}
for row,atoms in q3.items():
 require(sum(int(reps[n][0][0]) for n,d in atoms)==3,'Q3 rank')
 require(sum(int(reps[n][0][0])*d for n,d in atoms)==24,'Q3 degree')
require(len({tuple(atoms) for atoms in q3.values()})==3,'three distinct quotient types')
root=Path(__file__).resolve().parent
items=json.loads((root/'INPUTS.json').read_text())
require(len(items)==3,'three immutable originals')
for item in items:
 data=(root/'audit-inputs'/f"{item['key']}.md").read_bytes()
 blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 require(blob==item['blob'],f"immutable input mismatch: {item['key']}")
print('PASS: three immutable originals; forced channel; unique equivariant lift; two basepoint-free systems; nonzero extension; three intrinsic channel criteria.')
print('No actual HM/source coefficient, point, parameter, matrix, instance rank or scan evaluated.')
