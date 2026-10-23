#!/usr/bin/env python3
"""Fixed abstract characters and multiplicity inequalities, no actual tensor evaluation."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json

def require(c,m):
 if not c:raise RuntimeError(m)
def z(a,b=0):return F(a),F(b)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[0],-x[1]
def sub(x,y):return add(x,neg(y))
def mul(x,y):return x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def scale(k,x):return k*x[0],k*x[1]
def total(xs):
 r=z(0)
 for x in xs:r=add(r,x)
 return r
def va(*cs):return [total(x) for x in zip(*cs)]
def vs(k,c):return [scale(k,x) for x in c]
def vm(c,d):return [mul(x,y) for x,y in zip(c,d)]
def sym(n,x):
 if n==0:return z(1)
 a,b=z(1),x
 for _ in range(2,n+1):a,b=b,sub(mul(x,b),a)
 return b
phi=z(F(1,2),F(1,2));phip=z(F(1,2),F(-1,2))
W=[z(2),z(-2),phi,neg(phi),phip,neg(phip),z(1),z(-1),z(0)]
one=[z(1)]*9;A=[sym(2,x) for x in W];D=[sym(4,x) for x in W]
P=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]));V=[sub(sym(6,x),p) for x,p in zip(W,P)]
square=[W.index(sub(mul(x,x),z(2))) for x in W]
sym2V=vs(F(1,2),va(vm(V,V),[V[i] for i in square]))
require(sym2V==va(one,D),'positive quadratic isotypic decomposition')
require(vm(V,V)==va(one,V,D),'V times V')
require(vm(V,P)==va(A,P,D),'V times P')
require(vm(V,D)==va(A,V,P,D),'V times D')
invariant_image=va(vs(2,V),vs(3,P),vs(3,D))
L=vm(V,invariant_image);K=va(one,vs(4,A),vs(2,V),vs(3,P),vs(3,D))
R=va(one,vs(2,A),vs(3,V),vs(3,P),vs(5,D))
require(L==va(vs(2,one),vs(6,A),vs(5,V),vs(6,P),vs(8,D)),'invariant curry')
require(va(K,R)==L,'required non-invariant curry character')
require((L[0],K[0],R[0])==(z(99),z(46),z(53)),'dimensions')
root=Path(__file__).parent;man=root/'audit-inputs'/'manifest.json'
if man.exists():
 for e in json.loads(man.read_text()):
  b=(root/'audit-inputs'/e['name']).read_bytes()
  require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['blob'],'input blob '+e['name'])
 print('PASS: both immutable input blobs authenticate exactly.')
print('PASS: Sym2 V=1+D and all three required tensor identities at nine fixed classes.')
print('PASS: invariant curry 99 minus actual middle46 equals forced character53.')
print('BOUNDARY:53 is a derived lower bound on curried image, not an actual matrix-rank evaluation or target-image dimension.')
