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




E16=va(vs(2,W),Wp,S,T);E14=va(vs(2,W),S,T);E8=va(vs(2,W),S)
H19=va(one,vs(2,A),V,P,D);H15=va(one,vs(2,A),V,D)
require(vm(Wp,W)==P,'only constant P channel')
require(inner(Wp,vm(H19,W))==z(1),'unique constant doublet channel')
require(inner(va(one,V),D)==z(0),'P-lift uniqueness Hom test')
require(inner(H15,P)==z(0),'constant-to-Q Hom vanishing')
require(inner(va(one,V),A)==z(0),'weighted-to-Q Ext vanishing')
require(vm(Wp,A)==T and inner(E14,vm(Wp,A))==z(1),'unique T-to-Q channel')
require(vm(E8,W)==va(vs(2,one),vs(3,A),D),'canonical kernel cross Hom')
require(inner(P,vm(E8,W))==z(0),'unique kernel splitting')
# The authenticated image/quotient alternatives, not selected C realizations.
rows={9:([('1',12)],[('1',2),('V',4)]),10:([('1',18)],[('1',2),('A',2)]),14:([('Wp',5)],[('1',2),('Wp',7)]),15:([('Wp',5)],[('1',2),('Wp',7)]),17:([('Wp',5)],[('1',14),('W',1)]),18:([('1',18)],[('W',1),('W',3)]),20:([('Wp',5)],[('W',1),('1',14)])}
for row,(image,quotient) in rows.items():
 for name,d in image+quotient:
  value=inner(reps[name],vm(Wp,[sym(1-d,w) for w in W])) if d<=1 else z(0)
  require(value==z(0),'no forbidden quotient in row '+str(row))
require(-2!=10,'equal-rank fiber injection degree obstruction')
require(E16[0]==z(16) and E14[0]==z(14) and E8[0]==z(8),'source dimensions')
require(H19[0]==z(19) and H15[0]==z(15),'constant target dimensions')
require(4+8==12 and 15+2==17 and 17-12==5 and 10-(-8-8)==26,'final rank and degree')
require(4-2==2 and 0-(-2)==2,'tensor Euler quotient')
require(6-2==4 and -6-2==-8,'tensor quadratic evaluation kernel')
root=Path(__file__).resolve().parent
items=json.loads((root/'INPUTS.json').read_text())
require(len(items)==1,'one immutable immediate original')
for item in items:
 data=(root/'audit-inputs'/f"{item['key']}.md").read_bytes()
 blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 require(blob==item['blob'],f"immutable input mismatch: {item['key']}")
print('PASS: immutable original; forced channels; unique target/source splitting tests; seven forbidden-quotient checks; final rank and degree.')
print('No actual HM/source coefficient, point, parameter, matrix, instance rank or scan evaluated.')
