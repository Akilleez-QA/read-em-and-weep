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


sw=lambda n:[sym(n,x) for x in W]
require(inner(P,D)==z(0),'no discarded P-only quotient channel')
require(inner(P,sw(6))==z(1),'unique residual m channel')
require(vm(A,Wp)==T,'unique nonsplit P-kernel Ext')
require(vm(V,W)==T,'tensor Euler model')
require(vm(Wp,S)==va(V,D),'forced V sections of E(2)')
require(vm(A,A)==va(one,A,D),'target H1 has no V')
require(inner(V,vm(T,W))==z(1),'unique V Euler injection')
require(inner(Wp,T)==z(0),'no invariant E(4) section')
require(inner(W,vm(V,S))==z(0),'unique equivariant E splitting')
require(vm(A,W)==va(W,S),'quadratic evaluation channels')
require(inner(T,W)==z(0),'qW kills T summand')
for n in range(4):require(inner(V,sw(n))==z(0),'no rank-one V factor')
require(3*(-6)+2==3*(-2)+2*(-5)==-16,'E ranks and degrees')
require(6*(-1)-4==-10,'zero-P rank2 kernel degree')
require(6*(-1)+2*(-3)==-12,'zero-P rank1 kernel degree')
# Boolean support partition only: these are not selected actual coefficients.
from itertools import product
for aD,bD,aV,aP,bV,bP in product((False,True),repeat=6):
 strata=(aD and bD,aD and not bD,not aD and aV and aP,
         not aD and aV and not aP,not aD and not aV and aP,
         not aD and not aV and not aP)
 require(sum(strata)==1,'six strata are a disjoint exhaustive partition')
for bV,bP,bD in product((False,True),repeat=3):
 cases=(bV,not bV and bP and bD,not bV and bP and not bD,
        not bV and not bP and bD,not bV and not bP and not bD)
 require(sum(cases)==1,'P-only residual partition')
source={0,4};target={1,4}
require(source-target=={0},'m kernel character')
require(source-{0}=={4},'Euler kernel character differs')
root=Path(__file__).resolve().parent
for item in json.loads((root/'INPUTS.json').read_text()):
 b=(root/'audit-inputs'/(item['key']+'.md')).read_bytes()
 require(len(b)==item['bytes'],'input byte count')
 require(hashlib.sha256(b).hexdigest()==item['sha256'],'input SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['blob'],'input Git blob')
print('PASS: abstract channel/Ext/Euler characters, kernel degrees, exhaustive Boolean support partitions, stabilizer characters and five exact immutable originals. No actual instance evaluated.')
