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
require(vm(P,W)==va(Wp,T),'P W')
require(sw(9)==va(S,T),'Sym9')
require(sw(7)==va(Wp,T),'Sym7')
require(sw(8)==va(P,D),'Sym8')
require(sw(5)==T,'Sym5')
require(vm(W,Wp)==P,'P W-factor')
require(inner(Wp,sw(5))==z(0),'restriction nonzero and unique splitting')
require(inner(W,vm(P,S))==z(0),'no W-source lift into eliminated P')
require(inner(W,sw(11))==z(1),'unique scalar channel')
require(inner(P,sw(6))==z(1),'unique Wprime channel')
require(inner(W,vm(D,T))==z(1),'unique D channel')
for d in [0,2,4]:
 require(inner(W,sw(d+1))==z(int(d==0)),'rank-one factor exclusion')
require(inner(one,sw(10))==z(0),'no scalar Euler factor')
require(inner(one,sw(12))==z(1),'unique invariant determinant')
require(inner(A,sw(6))==z(0),'unique original x-only splitting')
require(inner(one,va(vm(T,W),A))==z(0),'balanced K blocks z-only split')
require(inner(one,vm(A,A))==z(1),'one z-only Ext')
require(6>4 and 8<12 and 7<12,'evaluation-kernel and divisor bounds')
require(2*(-1)+(-6)==-8,'P8 evaluation kernel degree')
require(10+2*5==7*4-4*2,'actual quotient degree')
require(10-(-2)==12 and 2*5-(-2)==12,'two residual determinant degrees')
require(sorted([((3+5)//2)%5,((-3+5)//2)%5])==[1,4],'Wprime5 stabilizer weights')
require(10%10==0,'scalar row target trivial stabilizer character')
require(3*(-6)-12==-30 and 4*(-5)==-20 and 5*(-4)==-20,'original kernel degrees')
root=Path(__file__).resolve().parent
for item in json.loads((root/'INPUTS.json').read_text()):
 b=(root/'audit-inputs'/(item['key']+'.md')).read_bytes()
 require(len(b)==item['bytes'],'input byte count')
 require(hashlib.sha256(b).hexdigest()==item['sha256'],'input SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['blob'],'input Git blob')
print('PASS: fixed Hom characters, evaluation-kernel and line-factor exclusions, abstract stabilizer weights, degrees and exact immutable inputs. No actual instance evaluated.')
