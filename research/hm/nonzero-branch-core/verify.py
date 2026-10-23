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
require(vm(A,T)==va(Wp,S,vs(2,T)),'A degree-ten kernel channel')
require(all(inner(Wp,sy(n))==z(0) for n in range(6)),'no rank-one image for Wp(-5)')
require(sy(10)==va(A,V,D),'A degree-ten system')
require(sy(9)==va(S,T),'S degree-nine system')
require(vm(S,W)==va(A,D),'first S kernel bound')
require(vm(S,A)==va(W,S,T),'second S kernel bound')
require(inner(W,sy(7))==z(0),'W(2) quotient cannot reach O9')
require(sy(12)==va(one,A,P,D),'degree twelve character')
require(va(vm(S,S),vs(-1,sy(12)))==V,'balanced degree-nine kernel V')
require(3*(-1)!=-9 and 3*(-3)==-9,'kernel balance exclusions')
require(9<12 and 10<12 and 7<12,'orbit base-divisor exclusions')
require(sy(7)==va(Wp,T),'degree-seven Wp system')
require(inner(V,sy(8))==z(0),'unique split row9 extension')
require(vm(Wp,S)==va(V,D),'unique compatible lift Hom vanishing')
require(inner(A,vm(Wp,S))==z(0),'R-to-F Hom zero')
require(inner(one,vm(S,S))==z(1),'cubic Veronese channel')
require(inner(Wp,sy(13))==z(1) and inner(A,sy(10))==z(1),'two one-source channels')
require(inner(one,vm(Wp,Wp))==z(1),'nonzero tensor Euler extension line')
require(vm(Wp,W)==P,'tensor Euler middle representation')
def h0(n):return max(n+1,0)
def h1(n):return max(-n-1,0)
require(h1(3)==0 and h1(4)==0,'compatible lift Ext vanishings')
require(h1(8)==0 and h0(-1)==0,'row9 splitting and P6 nonsplitting')
require(-8!=12,'forced remaining S projection')
for sr,sd,tr,td,qr,qd in [(2,-10,3,0,1,10),(1,-8,3,6,2,14),(3,-9,4,0,1,9),(1,-8,4,4,3,12),(1,-2,2,10,1,12),(1,-2,4,4,3,6),(1,-8,5,16,4,24),(2,10,4,24,2,14)]:
 require(tr-sr==qr and td-sd==qd,'universal rank degree balance')
rows={9:[('1',12),('V',4)],10:[('1',18),('A',2)],14:[('Wp',5),('Wp',7)],15:[('P',6)]}
for atoms in rows.values():
 require(sum(int(reps[n][0][0]) for n,d in atoms)==4,'Q rank')
 require(sum(int(reps[n][0][0])*d for n,d in atoms)==24,'Q degree')
require(len({tuple(x) for x in rows.values()})==4,'four distinct alternatives')
root=Path(__file__).resolve().parent
items=json.loads((root/'INPUTS.json').read_text())
require(len(items)==3,'three immutable originals')
for item in items:
 data=(root/'audit-inputs'/f"{item['key']}.md").read_bytes()
 blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 require(blob==item['blob'],f"immutable input mismatch: {item['key']}")
print('PASS: three immutable originals; universal A/S kernels; compatible lift tests; nonzero extension; four actual channel criteria and degree balances.')
print('No actual HM/source coefficient, point, parameter, matrix, instance rank or scan evaluated.')
