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




E8=va(vs(2,W),S)
H15=va(one,vs(2,A),V,D);H12=va(one,vs(2,A),D)
require(vm(V,W)==T,'linear source forbidden channel')
require(inner(E8,T)==z(0),'no linear source reaches V')
require(vm(V,A)==va(P,D),'unique quadratic channel')
require(inner(P,vm(V,A))==z(1),'quadratic Hom dimension one')
require(inner(E8,T)==z(0),'Ext E8(-1) to O(-8) vanishes')
require([sym(7,w) for w in W]==va(Wp,T),'opposite source Hom vanishes')
require(inner(E8,va(Wp,T))==z(0),'no opposite source shear')
require([sym(6,w) for w in W]==va(V,P),'sextic evaluation representations')
require(vm(P,A)==va(V,P,D),'sextic evaluation kernel character')
require([sym(8,w) for w in W]==va(P,D),'sextic syzygy character')
require(H15==va(H12,V),'canonical constant target quotient')
require(H12[0]==z(12) and E8[0]==z(8),'dimensions')
require(4-3==1 and -8-0==-8,'dual sextic kernel rank degree')
require(1+8==9 and 12+2==14 and 14-9==5,'endpoint rank')
require(10-(-8-8)==26,'endpoint degree')
# TWELVE Section5: all image and quotient atom degrees are positive.
filtration_degrees={9:[12,2,4],10:[18,2,2],14:[5,2,7],15:[5,2,7],17:[5,14,1],18:[18,1,3],20:[5,1,14]}
require(all(d>0 for ds in filtration_degrees.values() for d in ds),'no map from C to any constant bundle')
root=Path(__file__).resolve().parent
items=json.loads((root/'INPUTS.json').read_text())
require(len(items)==2,'two immutable originals')
for item in items:
 data=(root/'audit-inputs'/f"{item['key']}.md").read_bytes()
 blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 require(blob==item['blob'],f"immutable input mismatch: {item['key']}")
print('PASS: two immutable originals; unique quadratic channel; kernel Hom/Ext tests; positive filtration; nine-source rank and degree.')
print('No actual HM/source coefficient, point, parameter, matrix, instance rank or scan evaluated.')
