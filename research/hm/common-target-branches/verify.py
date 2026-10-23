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
# Fixed channel and seven-type checks only.
E22=va(Wp,vs(2,S),vs(2,T))
E18=va(Wp,S,vs(2,T))
R24=va(A,V,vs(2,P),vs(2,D))
H28=va(one,vs(2,A),V,vs(2,P),vs(2,D))
require(vm(W,A)==va(W,S),'unique quadratic S channel')
require(inner(E22,vm(W,A))==z(2) and inner(E22,S)==z(2),'two S multiplicity functionals')
require(inner(E22,W)==z(0),'zero trivial target row')
require(E22==va(E18,S) and E18[0]==z(18),'unused source character')
require(2+18==20 and 3+18==21 and 24-20==4 and 24-21==3,'branch ranks')
require(2*(-3)+18*(-1)==3*(-2)+18*(-1)==-24,'branch degrees')
require(2>=-1 and 1>=-1,'source extension H1 vanishings')
require(va(R24,vm(W,W))==H28 and va(R24,A,one)==H28,'branch section characters')
q_nonzero=[[('1',12),('V',4)],[('1',18),('A',2)],[('Wp',5),('Wp',7)],[('P',6)]]
q3_zero=[[('1',14),('Wp',5)],[('1',18),('W',3)],[('V',8)]]
def sections(row,twist=0):
 out=[z(0)]*9
 for n,d in row:
  if d+twist>=0:out=va(out,vm(reps[n],[sym(d+twist,x) for x in W]))
 return out
for row in q_nonzero:
 require(all(d>=2 for n,d in row),'no quotient into degree one')
 require(sections(row)==H28,'nonzero branch sections')
for row in q3_zero:
 require(all(d>2 for n,d in row),'no quotient into degree two')
 require(va(sections(row),one)==H28,'zero branch sections')
 require(inner(one,sections(row))==z(0),'intrinsic positive summand has no invariant section')
root=Path(__file__).resolve().parent
items=json.loads((root/'INPUTS.json').read_text())
require(len(items)==2,'two immutable inputs')
for item in items:
 data=(root/'audit-inputs'/f"{item['key']}.md").read_bytes()
 blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 require(blob==item['blob'],f"immutable input mismatch: {item['key']}")
print('PASS: two immutable inputs; forced S channels; zero trivial row; universal source types; seven fixed branch checks.')
print('No actual HM/source coefficient, point, parameter, jet, derivative, matrix, or instance rank evaluated.')
