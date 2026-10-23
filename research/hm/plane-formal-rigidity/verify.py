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

# Exact fixed abstract character arithmetic, not an actual deformation value.
h1={1:va(A,V,P,D),2:va(A,V,P,D),3:va(V,P,D),4:va(A,V)}
result=[]
for n in range(1,5):
    sw=[sym(n,x) for x in W]
    result.append(int(inner(sw,h1[n])[0]))
require(result==[0,1,0,0], 'only second-normal invariant difference space')
for n in range(1,9):
    require(sym(n,W[1])==z((-1)**n*(n+1)), 'center on normal symmetric power')
require(inner(D,va(A,V))==z(0),'fourth-normal difference space zero')
# H1 of all later layers is proved zero by Serre duality/Steiner, not sampled.
root=Path(__file__).resolve().parent
for item in json.loads((root/'INPUTS.json').read_text()):
    b=(root/'audit-inputs'/(item['key']+'.md')).read_bytes()
    require(len(b)==item['bytes'],'input size '+item['key'])
    require(hashlib.sha256(b).hexdigest()==item['sha256'],'input SHA256 '+item['key'])
    require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['blob'],'input Git blob '+item['key'])
print('PASS: exact character orthogonality, normal-layer dimensions 0/1/0/0, parity, and all immutable input bytes. No actual coefficient or deformation value evaluated.')
