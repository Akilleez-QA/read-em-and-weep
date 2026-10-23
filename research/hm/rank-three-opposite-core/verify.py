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
# Fixed universal characters; no actual instance coefficients.
def sy(n):return [sym(n,x) for x in W]
require(sy(6)==va(V,P),'complementary sextics')
require(vm(P,W)==va(Wp,T),'P first kernel bound')
require(inner(Wp,sy(5))==z(0),'P quotient factor impossible')
require(vm(P,A)==va(V,P,D) and sy(8)==va(P,D),'P kernel multiplicity')
require(vm(V,W)==T and vm(V,A)==va(P,D),'V kernel degree bounds')
require(inner(W,vm(V,S))==z(0),'V kernel excludes W')
require(vm(Wp,A)==T and vm(Wp,W)==P,'tensor contraction')
require(inner(V,vm(P,A))==z(1),'unique V-to-P channel')
require(inner(Wp,vm(Wp,D))==z(0),'no Wprime-to-Wprime channel')
require(inner(V,vm(Wp,S))==z(1),'unique V-to-Wprime channel')
types={9:[('1',12),('V',4)],10:[('1',18),('A',2)],14:[('Wp',5),('Wp',7)],15:[('P',6)],17:[('1',14),('Wp',5)],18:[('1',18),('W',3)],20:[('V',8)]}
for row,atoms in types.items():
 require(all(d>=2 for _,d in atoms),'positive quotient degrees')
 require(sum(int(inner(reps[r],sy(6-d))[0]) for r,d in atoms if d<=6)==0,'forbidden O6 quotient')
for source,target,power in [('Wp','S',4),('Wp','A',5),('1','S',9),('1','A',10),('Wp','W',6),('1','W',11)]:
 require(inner(reps[source],vm(reps[target],sy(power)))==z(1),'one-dimensional core channel')
# Each tuple records source rank/degree, target rank/degree, quotient rank/degree.
for sr,sd,tr,td,qr,qd in [(3,-6,4,0,1,6),(2,-6,3,0,1,6),(1,-8,3,-6,2,2),(3,-6,6,-6,3,0),(2,-6,6,-6,4,0),(3,-14,7,10,4,24),(3,-14,6,10,3,24)]:
 require(tr-sr==qr and td-sd==qd,'universal rank-degree balance')
require(max(-(-1)-1,0)==0 and max(-1+1,0)==0,'unique splitting H1/H0 O(-1)')
root=Path(__file__).resolve().parent
items=json.loads((root/'INPUTS.json').read_text())
require(len(items)==2,'two immutable inputs')
for item in items:
 data=(root/'audit-inputs'/f"{item['key']}.md").read_bytes()
 blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 require(blob==item['blob'],f"immutable input mismatch: {item['key']}")
print('PASS: two immutable inputs; complementary sextic kernels; seven forbidden O(6) quotients; forced channel supports; six core Hom identities; rank-degree balances.')
print('No actual HM/source coefficient, point, parameter, jet, derivative, matrix, or instance rank evaluated.')
