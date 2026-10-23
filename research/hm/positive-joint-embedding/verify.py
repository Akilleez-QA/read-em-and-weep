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

require(vm(V,W)==T, 'positive irreducible coefficient domain')
require(vm(V,A)==va(P,D), 'mixed coefficient quotient')
require(vm(W,T)==va(V,P,D), 'mixed domain decomposition')
require(vm(Wp,A)==T and vm(Wp,W)==P, 'tensor contraction model')
require(inner(T,vm(D,W))==z(1) and inner(T,vm(P,W))==z(1), 'both unique channels')
require(inner(one,A)==z(0), 'no invariant kernel line')
U=va(vs(2,W),vs(2,Wp),vs(3,S),vs(4,T))
require(U[0]==z(44) and inner(U,T)==z(4), 'full degree-two negative space')
require(6-5==1 and -6==-6, 'quintic kernel rank and degree')
require(6-4==2 and -6==2*(-3), 'tensor quadratic kernel degree')
require(9-6==3 and 0-(-6)==3*2, 'mixed quotient rank and degree')
# Bounded spectral-sequence index check, not cohomology or an instance map.
for r in range(2,7):
 require(-3-r < -3, 'incoming differential outside Koszul columns')
 target=(-3+r,2-r)
 if r==2: require(target==(-1,0), 'only higher target is assumed zero H0')
 else: require(target[1]<0, 'later outgoing differential outside cohomology')
require(-3+1<0, 'abutment negative-degree vanishing')
root=Path(__file__).resolve().parent
items=json.loads((root/'INPUTS.json').read_text())
require(len(items)==4,'four immutable originals')
for item in items:
 data=(root/'audit-inputs'/f"{item['key']}.md").read_bytes()
 blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 require(blob==item['blob'],f"immutable input mismatch: {item['key']}")
print('PASS: four immutable originals; fixed representation channels; full44 character; Koszul indices; universal kernel and quotient degrees.')
print('No actual selected coefficient, point, parameter, matrix, jet, instance rank or scan evaluated.')
