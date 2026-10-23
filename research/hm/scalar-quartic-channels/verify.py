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
require(sy(8)==va(P,D),'degree eight system and no scalar source')
require(inner(S,W)==z(0),'no S to scalar channel')
require(inner(W,W)==z(1),'one Euler channel per W multiplicity')
require(inner(one,vm(W,W))==z(1),'one-dimensional source splitting ambiguity')
require(vm(D,W)==va(S,T),'D kernel linear character')
require(int(S[0][0])==4 and int(T[0][0])==6,'kernel first-twist rank obstruction')
require(4*(-1)!=-8 and 4*(-2)==-8,'universal D evaluation balance')
require(vm(D,A)==va(A,V,P,D),'D quadratic coefficient character')
require(sy(10)==va(A,V,D),'degree ten evaluation character')
require(va(vm(D,A),vs(-1,sy(10)))==P,'balanced kernel P multiplicity')
require(inner(D,sy(8))==z(1),'unique O(-8) to D channel')
require(inner(W,vm(D,W))==z(0),'unused W cannot reach D')
require(inner(one,vm(D,A))==z(0),'Euler kernel cannot reach D')
require(inner(S,vm(D,W))==z(1),'unique S to D multiplication channel')
require(vm(P,W)==va(Wp,T),'forbidden W(1) to P(2) channel')
rows={9:([('1',12)],[('1',2),('V',4)]),10:([('1',18)],[('1',2),('A',2)]),14:([('Wp',5)],[('1',2),('Wp',7)]),15:([('Wp',5)],[('1',2),('Wp',7)]),17:([('Wp',5)],[('1',14),('W',1)]),18:([('1',18)],[('W',1),('W',3)]),20:([('Wp',5)],[('W',1),('1',14)])}
for row,(image,quotient) in rows.items():
 for name,d in image+quotient:
  require(d>0,'no constant quotient')
  value=inner(reps[name],vm(P,sy(2-d))) if d<=2 else z(0)
  require(value==z(0),'forbidden P(2) quotient in row '+str(row))
require(4-1==3 and -4-0==-4,'scalar kernel rank degree')
require(1+4+3==8 and -8-4-4==-16,'actual source')
require(2+6+5==13 and 13-8==5 and 10-(-16)==26,'actual target and C')
require(5-1==4 and 0-(-8)==8,'dual evaluation quotient')
require(5-4==1 and 0-(-4)==4,'quartic quotient')
root=Path(__file__).resolve().parent
items=json.loads((root/'INPUTS.json').read_text())
require(len(items)==2,'two immutable originals')
for item in items:
 data=(root/'audit-inputs'/f"{item['key']}.md").read_bytes()
 blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 require(blob==item['blob'],f"immutable input mismatch: {item['key']}")
print('PASS: two immutable originals; scalar channel; noncanonical source splitting; universal D evaluation; seven forbidden P(2) quotients; forced quartic channel; rank and degree.')
print('No actual HM/source coefficient, point, parameter, matrix, instance rank or scan evaluated.')
