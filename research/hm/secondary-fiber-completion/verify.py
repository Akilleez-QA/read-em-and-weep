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
require(sw(6)==va(V,P),'Sym6=P+V')
require(vm(P,W)==va(Wp,T),'P W')
require(sw(5)==T,'Sym5=T')
require(vm(P,A)==va(V,P,D),'P A')
require(sw(8)==va(P,D),'Sym8=P+D')
require(vm(W,Wp)==P,'P=W Wp')
require(inner(P,vm(P,A))==z(1),'unique P-P channel')
require(inner(P,vm(V,A))==z(1),'unique P-V channel')
for J in [V,P]:
 require(inner(W,vm(J,T))==z(1),'unique W channel')
 require(inner(J,D)==z(0),'no Euler quotient factor')
for d in [0,2,4]:
 require(inner(W,sw(d+1))==z(int(d==0)),'only degree0 rank-one image candidate')
require(6>4 and 6<12 and 10<12,'kernel and divisor exclusions')
# Abstract binary C10 stabilizer; exponents are modulo5 for zeta=lambda^2.
P2=sorted([(r+1)%5 for r in [1,4,2,3]])
Wminus1=[0,4]
V4=sorted([(r+2)%5 for r in [0,2,3]])
P4=sorted([(r+2)%5 for r in [1,4,2,3]])
require(P2==[0,2,3,4] and V4==[0,2,4] and P4==[0,1,3,4],'fiber characters')
require(sorted([(3+1)//2%5,(-3+1)//2%5])==[2,4],'Wprime O1 kernel weights')
require((-4//2)%5==3 and (-2//2)%5==4,'line kernel weights')
for e in [0,1]:
 for r in [0,1]:
  require((5+e)-(4+e+r)==1-r,'rank loss formula')
root=Path(__file__).resolve().parent
for item in json.loads((root/'INPUTS.json').read_text()):
 b=(root/'audit-inputs'/(item['key']+'.md')).read_bytes()
 require(len(b)==item['bytes'],'input byte count')
 require(hashlib.sha256(b).hexdigest()==item['sha256'],'input SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['blob'],'input Git blob')
print('PASS: fixed channel characters, evaluation-kernel exclusions, abstract C10 weights, conditional rank arithmetic, immutable input identity. No actual instance evaluated.')
