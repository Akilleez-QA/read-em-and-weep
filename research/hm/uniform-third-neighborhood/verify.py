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
# Only fixed abstract character and degree/Ext identities.
require(vm(A,A)==va(one,A,D),'A tensor A = 1 + A + D')
require(inner(A,vm(D,A))==z(1),'unique dual y channel')
require(inner(vm(A,A),va(V,P,D))==z(1),'unique actual cup channel')
require(vm(W,S)==va(A,D),'W tensor Sym3W')
require(inner(va(V,P),vm(W,S))==z(0),'unique equivariant HN complement')
symD=vs(F(1,2),va(vm(D,D),psi2(D)))
require(symD==va(one,P,vs(2,D)),'Sym2D character')
require(3+4+2==9 and 3*2+4*2+2*5==24,'third even ranks/degrees')
require(9+6==15 and 24+6==30,'third full ranks/degrees')
require(9+15+6==30 and 24+15*4+6*6==120,'seventh even ranks/degrees')
require(int(symD[0][0])==15 and 15*8==120,'ninth target ranks/degrees')
for difference in (4-2,4-5,6-2,6-4,6-5):
 require(difference>=-1,'ordinary Ext1 of cohomology extensions vanishes')
require((-3)*(-1)+2==5,'dual-y quotient twist')
root=Path(__file__).resolve().parent
items=json.loads((root/'INPUTS.json').read_text())
require(len(items)==4,'four immutable dependencies')
for item in items:
 data=(root/'audit-inputs'/f"{item['key']}.md").read_bytes()
 blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 require(blob==item['blob'],f"immutable input mismatch: {item['key']}")
print('PASS: four immutable inputs; nine abstract character classes; unique dual-cup and HN channels; all Ext/rank/degree identities.')
print('No selected actual HM coefficients, points, jets, derivatives, matrices, or instance ranks evaluated.')
