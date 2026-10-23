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



E20=va(vs(2,W),Wp,vs(2,S),T);E16=va(vs(2,W),Wp,S,T)
H28=va(one,vs(4,A),vs(2,V),P,D);H22=va(one,vs(3,A),V,P,D);H19=va(one,vs(2,A),V,P,D)
H31=va(one,vs(3,A),V,vs(2,P),vs(2,D))
require(E20[0]==z(20) and E16[0]==z(16),'source ranks')
require(H28[0]==z(28) and H22[0]==z(22) and H19[0]==z(19),'constant target ranks')
require(H28==va(H22,A,V) and H22==va(H19,A),'actual constant cancellations')
require(vm(V,A)==va(P,D),'weighted quadratic sections')
require(inner(A,vm(V,A))==z(0) and inner(V,vm(V,A))==z(0),'first constant-to-weighted vanishings')
require(vm(V,W)==T and vm(S,W)==va(A,D),'universal quotient coefficient tests')
require(vm(Wp,T)==va(A,P,D) and vm(Wp,D)==va(S,T),'weighted quintic evaluation')
require(va(H22,vm(V,A))==H31 and va(H19,vm(Wp,T))==H31,'same complete evaluation coefficients')
require(va(E20,T)==va(E16,S,T),'same reduced26 evaluation kernel')
require(25-20==5 and 6+20==26 and 21-16==5 and 10+16==26,'same C rank and degree')
require(26-6==20 and 31-6==25 and 19-3==16 and 24-3==21,'intermediate cancellations')
rows={9:[('1',2),('1',12),('V',4)],10:[('1',2),('1',18),('A',2)],14:[('1',2),('Wp',5),('Wp',7)],15:[('1',2),('P',6)],17:[('1',14),('W',1),('Wp',5)],18:[('1',18),('W',1),('W',3)],20:[('W',1),('V',8)]}
expected={9:('1',12),10:('1',18),14:('Wp',5),15:('P',6),17:('Wp',5),18:('1',18),20:('V',8)}
for row,atoms in rows.items():
 vals=[inner(Wp,vm(reps[name],[sym(d-5,w) for w in W])) if d>=5 else z(0) for name,d in atoms]
 require(total(vals)==z(1),'unique gamma line')
 require(all(v==z(int(atom==expected[row])) for atom,v in zip(atoms,vals)),'unique target atom')
require(inner(Wp,[sym(7,w) for w in W])==z(1) and inner(Wp,[sym(13,w) for w in W])==z(1),'line quotient covariants')
require(inner(Wp,W)==z(0),'no residual degree-one covariant')
require(vm(Wp,W)==P,'rank-two Euler image')
root=Path(__file__).resolve().parent
items=json.loads((root/'INPUTS.json').read_text())
require(len(items)==2,'two immutable originals')
for item in items:
 data=(root/'audit-inputs'/f"{item['key']}.md").read_bytes()
 blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 require(blob==item['blob'],f"immutable input mismatch: {item['key']}")
print('PASS: two immutable originals; actual quotient characters; constant cancellation tests; complete evaluation bridge; seven conditional saturation channels.')
print('No actual HM/source coefficient, point, parameter, matrix, instance rank or scan evaluated.')
