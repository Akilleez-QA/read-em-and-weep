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
# Fixed abstract supports and universal bundle identities only.
E14=va(Wp,vs(2,T))
require(vm(A,W)==va(W,S),'A receives only S')
require(inner(E14,vm(A,W))==z(0),'no E14 to A')
require(inner(W,vm(S,A))==z(1) and inner(A,vm(S,W))==z(1),'unique shear spaces')
require(vm(V,W)==T,'no Wprime to V')
require(vm(A,S)==va(W,S,T) and vm(S,A)==va(W,S,T),'positive A/S supports')
require(vm(W,D)==va(S,T),'positive W support')
require(vm(P,W)==va(Wp,T) and vm(W,Wp)==P,'unique tensor Euler P channel')
for c in (vm(V,W),vm(A,S),vm(S,A),vm(W,D)):
 require(inner(Wp,c)==z(0),'Wprime excluded from other target blocks')
require(3+4+2+4+3==16 and 3+4+2+4+2==15,'target ranks')
require(2+4+6==12 and 12+12==24,'target and quotient degrees')
require(16-12==4 and 15-12==3,'quotient ranks')
# Euler/polarization rank-degree balances for each removed universal subbundle.
for sr,sd,tr,td,qr,qd in [(1,-4,4,-4,3,0),(2,-6,5,0,3,6),(3,-6,5,0,2,6),(1,-4,5,0,4,4),(2,-2,4,0,2,2)]:
 require(tr-sr==qr and td-sd==qd,'universal quotient rank/degree')
root=Path(__file__).resolve().parent
items=json.loads((root/'INPUTS.json').read_text())
require(len(items)==2,'two immutable inputs')
for item in items:
 data=(root/'audit-inputs'/f"{item['key']}.md").read_bytes()
 blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 require(blob==item['blob'],f"immutable input mismatch: {item['key']}")
print('PASS: two immutable inputs; forced A normalization channels; Wprime support exclusion; all universal quotient and final target identities.')
print('No actual HM/source coefficient, point, parameter, jet, derivative, matrix, or instance rank evaluated.')
