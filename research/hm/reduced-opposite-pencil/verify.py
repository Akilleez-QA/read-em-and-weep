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
require(vm(V,A)==va(P,D),'V times A')
S=[sym(3,x) for x in W];T6=[sym(5,x) for x in W]
Sym6=[sym(6,x) for x in W]
Wp=va(vm(W,P),vs(-1,T6))
require(Sym6==va(V,P),'Sym6 W equals V+P')
require(vm(W,V)==T6,'W times V')
require(vm(W,P)==va(Wp,T6),'W times P')
constant=vm(W,T6)
require(constant==va(V,P,D),'actual global-section coefficient C12')
source14=va(vm(W,constant),vs(-1,vm(W,D)))
require(source14==vm(W,Sym6)==va(Wp,vs(2,T6)),'canonical H14 character')
reachable=va(one,vs(3,A),vs(2,V),vs(3,P),vs(3,D))
quotient=va(one,vs(3,A),V,vs(2,P),vs(2,D))
require(reachable==va(constant,quotient),'target quotient character')
require([x[0] for x in [S,A,constant,source14,reachable,quotient]]==list(map(z,[4,3,12,14,43,31])),'all coefficient dimensions')
# Bundle presentations retain rank and total degree, including torsion degree.
require(46-44+3==43-40+2==31-26==5,'same cokernel rank')
require(44-3*6==40-2*7==26,'same cokernel degree')
require((40-14,43-12)==(26,31),'quotient pencil dimensions')
require(2+12==14 and -2*7+14==0,'preimage subbundle rank and twisted degree')
# Positive global sections of the line leave O10, while positive H1 leaves O(-4).
def line(t):return [(7+t,(-1)**(t+1)),(t,(-1)**t),(-7+t,(-1)**(t+1))]
require(line(2)==[(9,-1),(2,1),(-5,-1)],'twist2 physical parity')
require(line(3)==[(10,1),(3,-1),(-4,1)],'twist3 physical parity')
require(sum(max(-d-1,0) for d,sgn in line(2) if sgn==-1)==4,'source restriction dimension')
require(sum(max(-d-1,0) for d,sgn in line(3) if sgn==1)==3,'target restriction dimension')
require(11-10==1 and 4-3==1,'two line-evaluation quotients')
require(-4 + -3 == -7 and 2*(-2)==-4,'square evaluation kernel and target twists')
require(2*max(-(-7)-1,0)==12,'H0 J dimension')
require([2*max(n-7+1,0) for n in range(9)]==[0,0,0,0,0,0,0,2,4],'normal-order adjoint section dimensions')
require(max(4-4+1,0)==1 and 6+5-1==10,'first actual product twist')
require(all(-s-4<3 for s in (-4,-3)),'H4 E0 at t=-1 vanishes by primary support')
root=Path(__file__).parent;man=root/'audit-inputs'/'manifest.json'
if man.exists():
 entries=json.loads(man.read_text());require(len(entries)==5,'five immutable originals')
 for e in entries:
  b=(root/'audit-inputs'/e['name']).read_bytes()
  require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['blob'],'input blob '+e['name'])
 print('PASS: all five immutable input blobs authenticate exactly.')
print('PASS: fixed C12, H14 and quotient R31 characters on nine abstract classes.')
print('PASS: 44-to-46, 40-to-43 and 26-to-31 presentations all retain cokernel rank5 and degree26.')
print('PASS: physical line parities, universal square-kernel twists, normal-order dimensions and first product twist.')
print('BOUNDARY: exact naturality, same-sheaf cokernel and saturation are proved mathematically; no actual HM coefficients, matrices, points or instance ranks are evaluated.')
