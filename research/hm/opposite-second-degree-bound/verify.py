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
# Only fixed abstract characters, universal dimension arithmetic, and nine rows.
N=va(A,Wp)
wedgeN=vs(F(1,2),va(vm(N,N),vs(-1,psi2(N))))
require(wedgeN==va(one,A,T),'current exterior target')
require(inner(one,wedgeN)==z(1),'single possible invariant quotient')
require(inner(one,va(A,V))==z(0),'no invariant exceptional H1')
require(5*10-5==45,'universal degree-four Koszul dimensions')
rows={
7:[('1',2),('1',4),('1',18),('W',1)],
9:[('1',2),('1',12),('V',4)],
10:[('1',2),('1',18),('A',2)],
12:[('1',2),('W',1),('Wp',11)],
14:[('1',2),('Wp',5),('Wp',7)],
15:[('1',2),('P',6)],
17:[('1',14),('W',1),('Wp',5)],
18:[('1',18),('W',1),('W',3)],
20:[('W',1),('V',8)]}
values={}
for number,row in rows.items():
 require(sum(reps[n][0][0] for n,d in row)==5,'rank')
 require(sum(d*reps[n][0][0] for n,d in row)==26,'degree')
 values[number]=sum(inner(one,vm(reps[n],[sym(2-d,x) for x in W]))[0] for n,d in row if d<=2)
require(list(values.values())==[2,1,1,2,1,1,1,1,1],'exact invariant dimensions')
survive=[n for n in rows if values[n]<=1]
require(survive==[9,10,14,15,17,18,20],'seven survivors')
require(all(values[n]==1 for n in survive),'unique invariant quotient on every survivor')
kernels={
9:[('1',12),('V',4)],10:[('1',18),('A',2)],
14:[('Wp',5),('Wp',7)],15:[('P',6)],
17:[('1',0),('1',14),('Wp',5)],
18:[('1',0),('1',18),('W',3)],20:[('1',0),('V',8)]}
for n,row in kernels.items():
 require(sum(reps[a][0][0] for a,d in row)==4,'canonical kernel rank')
 require(sum(d*reps[a][0][0] for a,d in row)==24,'canonical kernel degree')
require(vm(W,W)==va(one,A),'unique Euler quotient channel')
root=Path(__file__).resolve().parent
items=json.loads((root/'INPUTS.json').read_text())
require(len(items)==4,'four immutable inputs')
for item in items:
 data=(root/'audit-inputs'/f"{item['key']}.md").read_bytes()
 blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 require(blob==item['blob'],f"immutable input mismatch: {item['key']}")
print('PASS: four immutable inputs; fixed abstract character identities; nine-row invariant filter.')
print('Surviving rows:',survive)
print('No actual HM/source coefficients, points, parameters, jets, derivatives, matrices, or instance ranks evaluated.')
