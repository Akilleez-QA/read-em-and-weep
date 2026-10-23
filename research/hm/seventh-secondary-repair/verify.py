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


# Dimensions and degrees of fixed bundles, not actual map ranks.
Urank=3+3+4+5; Jrank=3+4+5
Krank=6+3; Kdeg=-6-6; Lrank=3; Ldeg=-18
Qrank=Krank-Lrank; Qdeg=Kdeg-Ldeg
require((Urank,Jrank,Krank,Kdeg,Qrank,Qdeg)==(15,12,9,-12,6,6),'fixed bundles')
require(Urank+Jrank-Qrank==21,'seventh middle rank')
require(4*Urank+6*Jrank-Qdeg==126,'seventh middle degree')
require(18*8-42==102 and 102+3*8==126,'ninth dual twist and quotient')
def h1line(d):return max(-d-1,0)
require(h1line(6-4)==0,'equivariant correction lift has no Ext1 obstruction')
require((6%2,8%2)==(0,0),'added layers positive')
require(3-6==-3 and 3-8==-5,'B3 normal twists')
require(9-4-3==2 and 9-1==8,'Cartier ninth dual coefficient and base twist')
for generic_rank in range(7):
 n=6-generic_rank; m=12-n
 require(m==6+generic_rank,'canonical correction quotient rank')
 require(m+(15-generic_rank)==21,'middle rank exact sequence')
for generic_rank in range(1,7):
 require((9-(generic_rank-1))-3==(6-generic_rank)+1,'extra fiber class increases next obstruction rank by one')
require(vm(A,D)==va(A,V,P,D),'secondary target character')
root=Path(__file__).resolve().parent
for item in json.loads((root/'INPUTS.json').read_text()):
 b=(root/'audit-inputs'/(item['key']+'.md')).read_bytes()
 require(len(b)==item['bytes'],'input byte count')
 require(hashlib.sha256(b).hexdigest()==item['sha256'],'input SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['blob'],'input Git blob')
print('PASS: fixed characters, bundle ranks/degrees, parity/twists, Ext vanishing, abstract rank identities and four exact originals. No actual map or instance evaluated.')
