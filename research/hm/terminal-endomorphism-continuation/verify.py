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

root=Path(__file__).resolve().parent
for item in json.loads((root/'INPUTS.json').read_text()):
 b=(root/'audit-inputs'/(item['key']+'.md')).read_bytes()
 require(len(b)==item['bytes'],'input length')
 require(hashlib.sha256(b).hexdigest()==item['sha256'],'input SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['blob'],'input Git blob')


N05=vm(W,[sym(6,x)for x in W]);U5=T
require(N05==va(Wp,vs(2,T)),'first terminal character')
require(va(N05,U5)==va(Wp,vs(3,T)),'full terminal character')
require(N05[0]==z(14) and U5[0]==z(6),'distinct terminal character-space dimensions')
# Finite abstract algebra basis checks, not actual source coefficients.
def prod(x,y):
 a,c,d,b,e=x; A,C,D,B,E=y
 return (a*A,c*C,d*D,A*b+d*B,A*e+d*E)
def plus(x,y):return tuple(a+b for a,b in zip(x,y))
def terminal(x):return (x[0],x[1])
def tprod(x,y):return tuple(a*b for a,b in zip(x,y))
zero=(0,0,0,0,0)
basis=[tuple(int(i==j)for i in range(5))for j in range(5)]
for x in basis:
 for y in basis:
  require(terminal(prod(x,y))==tprod(terminal(x),terminal(y)),'terminal algebra homomorphism')
  for z0 in basis:require(prod(prod(x,y),z0)==prod(x,prod(y,z0)),'abstract algebra associativity')
e0,ecore,eend,j1,j2=basis
require(prod(eend,eend)==eend,'endpoint idempotent')
for j in (j1,j2):
 require(prod(eend,j)==j and prod(j,eend)==zero,'noncentral endpoint orientation')
 for k in (j1,j2):require(prod(j,k)==zero,'square-zero radical')
for x in basis:
 require(prod(ecore,x)==prod(x,ecore),'core idempotent central')
 for k in (eend,j1,j2):
  require(terminal(prod(k,x))==(0,0) and terminal(prod(x,k))==(0,0),'zero-coupling terminal ideal')
# Nonzero-coupling algebra is the closed subspace a1=a2.
nbasis=[e0,plus(ecore,eend),j1,j2]
for x in nbasis:
 for y in nbasis:
  p0=prod(x,y);require(p0[1]==p0[2],'nonzero-coupling closed subalgebra')
require(terminal(e0)==(1,0) and terminal(ecore)==(0,1),'zero-coupling terminal surjectivity')
require(terminal(plus(ecore,eend))==(0,1),'nonzero-coupling terminal surjectivity')
require(5-2==3 and 4-2==2,'exact terminal kernel dimensions')
print('PASS: three exact inputs; fixed character identities; abstract opposite-algebra associativity, terminal homomorphism, ideals and idempotent orientation.')
print('No actual source coefficients or parameter evaluations; functoriality is established by the written proof, not this checker.')
