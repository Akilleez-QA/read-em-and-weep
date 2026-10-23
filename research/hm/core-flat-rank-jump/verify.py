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
# Bounded fixed characters and universal quotient identities only.
def sy(n):return [sym(n,x) for x in W]
for n in range(6):require(inner(Wp,sy(n))==z(0),'v rank-one factor excluded')
require(inner(Wp,vm(A,T))==z(1) and inner(S,sy(9))==z(1),'v and c channels exist uniquely')
require(inner(S,W)==z(0) and inner(S,Wp)==z(0),'low-degree c quotient exclusions')
require(vm(Wp,A)==T and inner(S,T)==z(0),'no Wprime degree3 quotient')
require(inner(S,vm(W,A))==z(1) and inner(W,sy(7))==z(0),'unique contraction does not kill c')
require(sy(10)==va(A,V,D) and vm(S,W)==va(A,D),'c quotient multiplicity V')
require(inner(V,vm(A,A))==z(0),'extension connecting map injective')
require(sy(6)==va(V,P) and inner(V,sy(6))==z(1),'extension space is a line')
H=va(one,vs(3,A),V,vs(2,P),vs(2,D));E=va(vs(2,W),Wp,vs(2,S),vs(2,T))
require(va(A,vm(P,sy(6)))==H,'generic H31 character')
require(va(W,vm(P,sy(5)))==E,'generic E26 character')
require(va(A,sy(12),vm(V,D))==H,'special H31 character')
require(va(W,sy(11),vm(V,S))==E,'special E26 character')
require(2+24==26 and 7-3==4 and 10-(-14)==24,'core and C ranks/degrees')
require(3*4+12==4*6==24,'extension middle degrees')
root=Path(__file__).resolve().parent
items=json.loads((root/'INPUTS.json').read_text())
require(len(items)==3,'three immutable inputs')
for item in items:
 data=(root/'audit-inputs'/f"{item['key']}.md").read_bytes()
 blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 require(blob==item['blob'],f"immutable input mismatch: {item['key']}")
print('PASS: three immutable inputs; saturated-channel character exclusions; nonzero extension test; both complete evaluation characters; degree identities.')
print('No actual HM/source coefficient, point, parameter, jet, derivative, matrix, or instance rank evaluated. No auxiliary parameter scan performed.')
