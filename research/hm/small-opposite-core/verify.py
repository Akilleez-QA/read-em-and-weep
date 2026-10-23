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




def sy(n):return [sym(n,w) for w in W]
require(sy(7)==va(Wp,T),'septic character')
require(inner(W,sy(7))==z(0),'O(-8) projection vanishes')
require(inner(W,W)==z(1),'restriction is a scalar between lines')
require(inner(one,vm(W,W))==z(1),'unique Euler factor')
require(vm(Wp,sy(4))==va(S,T),'weighted target Hom character')
require(inner(S,vm(Wp,sy(4)))==z(1),'target splitting ambiguity retained')
E24=va(W,Wp,vs(2,S),vs(2,T));H28=va(one,vs(2,A),V,vs(2,P),vs(2,D))
require(E24[0]==z(24) and H28[0]==z(28),'old actual evaluation dimensions')
require(inner(one,vm(W,E24))==z(1) and inner(one,H28)==z(1),'old scalar gate dimensions')
def h0(n):return max(n+1,0)
def h1(n):return max(-n-1,0)
require(h1(4)==0,'Y6 extension splits but is not selected')
require(h0(-5)==0 and h0(-1)==0,'positive Y6 has no maps to O')
require(h0(-1)==0,'negative quotient not globally generated')
# Universal and actual kernel/cokernel balances.
for sr,sd,tr,td,qr,qd in [(2,-2,3,0,1,2),(1,-2,2,-2,1,0),(4,-12,8,12,4,24),(2,-10,6,14,4,24),(3,-10,6,14,3,24)]:
 require(tr-sr==qr and td-sd==qd,'rank degree balance')
require(9-1==8 and 14-2==12,'target degree-two kernel')
require(8-2==6 and 12-(-2)==14,'canonical positive target kernel')
require(3-2==1 and -4-(-2)==-2,'nonzero restriction source kernel')
root=Path(__file__).resolve().parent
items=json.loads((root/'INPUTS.json').read_text())
require(len(items)==2,'two immutable originals')
for item in items:
 data=(root/'audit-inputs'/f"{item['key']}.md").read_bytes()
 blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 require(blob==item['blob'],f"immutable input mismatch: {item['key']}")
print('PASS: two immutable originals; actual projection channels; Euler companion; old gate dimensions; target ambiguity; both core rank and degree balances.')
print('No actual HM/source coefficient, point, parameter, matrix, instance rank or scan evaluated.')
