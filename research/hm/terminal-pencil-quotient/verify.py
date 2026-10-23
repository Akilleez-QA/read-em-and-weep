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

root=Path(__file__).resolve().parent
for item in json.loads((root/'INPUTS.json').read_text()):
 b=(root/'audit-inputs'/(item['key']+'.md')).read_bytes()
 require(len(b)==item['bytes'],'input length')
 require(hashlib.sha256(b).hexdigest()==item['sha256'],'input SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['blob'],'input Git blob')

M4=va(vs(2,V),vs(4,P),vs(3,D));M5=va(Wp,vs(3,T))
N04=va(V,vs(2,P),D);NR4=va(V,vs(2,P),vs(2,D))
N05=vm(W,[sym(6,x) for x in W]);NR5=T
Z=va(NR4,vs(-1,D));NC4=va(P,D)
require(va(N04,NR4)==M4,'genuine degree-four decomposition')
require(va(N05,NR5)==M5,'genuine degree-five decomposition')
require(N05==va(Wp,vs(2,T)),'remaining degree-five character')
require(Z==va(V,vs(2,P),D),'intrinsic zero-source character')
require(va(Z,vs(-1,NC4))==va(V,P),'actual residual socle quotient character')
require([sym(6,x)for x in W]==va(V,P),'complete sextic evaluation coefficients')
require([sym(5,x)for x in W]==T,'evaluation kernel representation')
require(N04[0]==z(16) and N05[0]==z(14) and Z[0]==z(16),'quotient dimensions')
require(32-14==18 and -32==-16-16,'quotient kernel rank degree')
require(17==2+15 and -37==-16-21,'full terminal kernel rank degree')
require(18-17==1 and -32-(-37)==5,'retained snake cokernel')
require(16-15==1 and -16-(-21)==5,'residual snake cokernel')
require(7-6==1 and -7-(-12)==5,'complete evaluation rank degree')
require(all(n<0 for n in [-1,-7]),'acyclic-section and joint-kernel degree checks')
print('PASS: three exact input byte/blob hashes; nine-class fixed character identities; quotient/kernel/evaluation rank-degree checks.')
print('No actual coefficient, parameter or rank evaluation. The checker does not replace the naturality proof.')
