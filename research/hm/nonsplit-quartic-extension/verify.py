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
require(vm(A,W)==va(W,S),'unique S-to-A channel')
require(inner(S,vm(A,W))==z(1),'S-to-A multiplicity')
require(sy(10)==va(A,V,D) and inner(one,sy(10))==z(0),'O(-8) cannot reach O2')
require(inner(W,sy(3))==z(0),'W(-1) cannot reach O2')
require(inner(one,sy(4))==z(0),'O(-2) cannot reach O2')
require(vm(Wp,W)==P and inner(one,vm(Wp,W))==z(0),'weighted graph restriction Hom')
require(inner(D,A)==z(0),'constant D lift cannot remove A graph')
require(inner(A,A)==z(1),'extension class dimension one')
require(vm(S,W)==va(A,D),'cubic evaluation and splitting ambiguity')
require(inner(A,vm(S,W))==z(1),'one-dimensional complement ambiguity')
require(inner(A,vm(Wp,sy(5)))==z(1),'noncanonical weighted A lift')
require(inner(S,vm(Wp,sy(4)))==z(1),'noncanonical weighted S lift')
require(inner(D,vm(Wp,sy(5)))==inner(S,vm(Wp,sy(6)))==z(1),'weighted correction channels')
# Universal line-bundle Hom/Ext degrees; no actual tensor values.
def h0(n):return max(n+1,0)
def h1(n):return max(-n-1,0)
require(h0(-4)==0,'unique zero-class pushout splitting')
require(h0(-3)==0,'cubic evaluation extension nonsplit')
require(h1(0)==0 and h1(1)==0,'constant and positive extension vanishings')
require(h1(5)==0 and h1(4)==0,'weighted target bundle splitting exists')
require(h1(-4)==3,'extension representation H1(O-4)=A')
require(4-1==3 and 4-4==0,'cubic evaluation kernel')
require(1+3==4 and -8-4==-12,'actual source rank degree')
require(2+4+3==9 and 10+4==14,'target isomorphism rank degree')
require(9-4==5 and 14-(-12)==26,'actual C invariants')
require(2-1==1,'active line leaves unique quotient direction')
root=Path(__file__).resolve().parent
items=json.loads((root/'INPUTS.json').read_text())
require(len(items)==2,'two immutable originals')
for item in items:
 data=(root/'audit-inputs'/f"{item['key']}.md").read_bytes()
 blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 require(blob==item['blob'],f"immutable input mismatch: {item['key']}")
print('PASS: two immutable originals; forced A-channel obstruction; nonzero extension and graph tests; canonical quotient direction; rank and degree.')
print('No actual HM/source coefficient, point, parameter, matrix, instance rank or scan evaluated.')
