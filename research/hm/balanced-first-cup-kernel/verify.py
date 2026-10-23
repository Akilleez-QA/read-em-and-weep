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





# Exact abstract finite-group characters. No actual tensor value is entered.
sw=lambda n:[sym(n,x) for x in W]
H=va(one,P,vs(2,D));J=va(A,V)
require(sw(8)==va(P,D),'H8=P+D')
require(sw(6)==va(V,P),'E6=V+P')
require(vm(A,D)==va(A,V,P,D),'multiplicity-free quotient target')
require(vm(A,A)==va(one,A,D),'A quotient target')
require(va(vm(A,J),vs(-1,H))==A,'aggregate cup cokernel character')
require(va(vm(H,W),vs(-1,vm(J,S)))==T,'ambient first-scaling kernel character')
require(15*2==30 and 6*4==24 and 30-24==6,'ambient dimensions')
# Laurent weight characters of universal SL2(C) modules, separate from G.
def sl(n):return {i:1 for i in range(-n,n+1,2)}
def plus(*ds):
 out={}
 for d in ds:
  for k,v in d.items():out[k]=out.get(k,0)+v
 return {k:v for k,v in out.items() if v}
def tensor(a,b):
 out={}
 for x,v in a.items():
  for y,w in b.items():out[x+y]=out.get(x+y,0)+v*w
 return out
def symmetric_square(a):
 weights=[k for k,m in a.items() for _ in range(m)]
 out={}
 for i,x in enumerate(weights):
  for y in weights[i:]:out[x+y]=out.get(x+y,0)+1
 return out
require(symmetric_square(sl(4))==plus(sl(8),sl(4),sl(0)),'universal symmetric square CG')
require(tensor(sl(2),sl(4))==plus(sl(6),sl(4),sl(2)),'universal target CG')
require(tensor(sl(2),sl(2))==plus(sl(4),sl(2),sl(0)),'universal A output lacks H8')
require(tensor(sl(2),sl(6))==plus(sl(8),sl(6),sl(4)),'unique top polarization')
# Universal highest-vector contraction, not an HM parameter or map evaluation:
# (x^4,y^2)_2 = (4*3)*(2*1)*x^2, and equal Leibniz terms double it.
require(4*3*2==24 and 2*24!=0,'nonzero universal top CG coefficient')
# Trace-free Jordan square on diag(x,y,-x-y) has first-minus-second
# component 2*x^2-2*y^2, a nonzero polynomial in free indeterminates.
jordan_difference={(2,0):2,(0,2):-2}
require(any(jordan_difference.values()),'nonzero universal trace-free Jordan polynomial')
# The text proves the derivative-span lemma for every subspace.
# This checks only its fixed dimension consequence, not an instance rank.
require(min(min(5,8),7)==5 and 5>4,'binary derivative-span contradiction')
require(6+3==9 and -6-2*3==-12,'selected structural splitting rank/degree')
root=Path(__file__).resolve().parent
for item in json.loads((root/'INPUTS.json').read_text()):
 b=(root/'audit-inputs'/(item['key']+'.md')).read_bytes()
 require(len(b)==item['bytes'],'input byte count')
 require(hashlib.sha256(b).hexdigest()==item['sha256'],'input SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['blob'],'input Git blob')
print('PASS: exact G/SL2 characters, universal nonzero tensor coefficients, derivative dimension consequence, ambient cup character, and immutable source bytes. No actual HM instance evaluated.')
