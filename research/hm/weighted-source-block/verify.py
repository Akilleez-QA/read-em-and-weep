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
# Only fixed character, extension and rank/degree identities.
require(vm(W,S)==va(A,D),'W weighted support')
require(vm(A,A)==va(one,A,D),'A weighted support')
require(vm(W,A)==va(W,S),'nonzero middle section character')
require(inner(D,A)==z(0),'no equivariant D to A lift')
require(inner(W,vm(A,S))==z(1),'one W-branch A channel')
require(inner(A,vm(A,A))==z(1),'one A-branch A channel')
require(inner(A,A)==z(1) and inner(W,vm(A,W))==z(1),'one-dimensional invariant Ext spaces')
E18=va(Wp,S,vs(2,T));R16=va(V,vs(2,P),D)
require(inner(S,E18)==z(1),'unique S source')
require(vm(S,W)==va(A,D),'S coefficient support')
require(inner(W,vm(E18,A))==z(1),'one-dimensional W complement shifts')
require(inner(A,vm(E18,W))==z(1),'one-dimensional A complement shifts')
require(E18[0]==z(18) and R16[0]==z(16),'residual dimensions')
# Four middle bundles, with their splitting degrees and multiplicity representations.
blocks=[ [('A',0),('A',2)], [('W',1),('S',1)], [('A',0),('W',3)], [('S',1),('1',2)] ]
for j,row in enumerate(blocks):
 rank=sum(reps[n][0][0] for n,d in row);degree=sum(d*reps[n][0][0] for n,d in row)
 require(rank==(6 if j<2 else 5) and degree==6,'middle rank/degree')
 require(all(d>=0 for n,d in row),'middle H1 zero and global generation')
 if j in (1,3):
  chars=[z(0)]*9
  for n,d in row:chars=va(chars,vm(reps[n],[sym(d-1,x) for x in W]))
  require(chars==va(W,S),'ample middle section representation')
require(16+6-18==4 and 16+5-18==3 and 6+18==24,'actual residual rank degree')
root=Path(__file__).resolve().parent
items=json.loads((root/'INPUTS.json').read_text())
require(len(items)==1,'one immutable input')
for item in items:
 data=(root/'audit-inputs'/f"{item['key']}.md").read_bytes()
 blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 require(blob==item['blob'],f"immutable input mismatch: {item['key']}")
print('PASS: immutable PR1009 input; fixed weighted supports; one-dimensional extension spaces; all four block and residual identities.')
print('No actual HM/source coefficient, point, parameter, jet, derivative, matrix, or instance rank evaluated.')
