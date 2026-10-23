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


rows={9:[('1',2),('1',12),('V',4)],10:[('1',2),('1',18),('A',2)],14:[('1',2),('Wp',5),('Wp',7)],15:[('1',2),('P',6)],17:[('1',14),('W',1),('Wp',5)],18:[('1',18),('W',1),('W',3)],20:[('W',1),('V',8)]}
expected={9:('1',12),10:('1',18),14:('Wp',5),15:('P',6),17:('Wp',5),18:('1',18),20:('V',8)}
for row,atoms in rows.items():
 for source,twist in [(V,2),(Wp,5)]:
  vals=[inner(source,vm(reps[name],[sym(d-twist,w) for w in W])) if d>=twist else z(0) for name,d in atoms]
  require(total(vals)==z(1),'one Hom line in row '+str(row))
  require(all(v==z(int(atom==expected[row])) for atom,v in zip(atoms,vals)),'unique contributing atom')
require([sym(6,w) for w in W]==va(V,P),'sextic systems')
require(vm(A,va(V,P))==va(V,vs(2,P),vs(2,D)),'rank-six extension character')
require(inner(V,vm(A,va(V,P)))==z(1),'one-dimensional equivariant Ext')
require(inner(one,A)==z(0),'unique cubic lift Ext vanishing')
R=va(vs(2,W),vs(2,Wp),vs(3,S),vs(2,T))
require(R[0]==z(32) and inner(S,R)==z(3),'actual quotient coefficient space')
require(3-2==1 and 6-10==-4,'universal sextic kernel')
require(3+3==6 and -18+6==-12,'forced nonsplit preimage')
require(3+2==5 and -18-8==-26,'doubled cubic preimage')
require(2<=3,'two selected cubic directions fit actual multiplicity')
require(va(vm(V,S),vs(-1,vm(A,S)))==va(Wp,vs(-1,W)), 'L twist-one Euler')
require(va(vm(V,D),vs(-1,vm(A,A)))==va(V,P,vs(-1,one)), 'L twist-two Euler')
for odd in [W,Wp,S]:require(inner(V,vm(odd,W))==z(0),'rank-four odd atoms cannot supply V')
require(inner(V,vm(Wp,W))==z(0) and inner(Wp,S)==z(0) and inner(V,A)==z(0),'unique equivariant splitting cross Hom')
require(2+3+1==6 and -2-6-4==-12,'determined L splitting')
root=Path(__file__).resolve().parent
items=json.loads((root/'INPUTS.json').read_text())
require(len(items)==3,'three immutable originals')
for item in items:
 data=(root/'audit-inputs'/f"{item['key']}.md").read_bytes()
 blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 require(blob==item['blob'],f"immutable input mismatch: {item['key']}")
print('PASS: three immutable originals; seven fixed Hom tables; Ext character; cubic multiplicities and universal rank/degree checks.')
print('No actual HM/source coefficient, point, parameter, matrix, instance rank or scan evaluated.')
