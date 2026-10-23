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
ext2V=vs(F(1,2),va(vm(V,V),vs(-1,[V[i] for i in square])))
require(ext2V==V,'exterior square of V')
U3=V;U2=va(vm(V,ext2V),vs(-1,one));U1=sym2V
require(U2==va(V,D),'Schur middle coefficient')
require([x[0] for x in [U3,U2,U1]]==list(map(z,[3,8,6])),'squared ideal resolution dimensions')
# Hilbert numerator of the square of a three-variable regular linear ideal.
def poly_mul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
h=poly_mul([1,3],[1,-3,3,-1])
num=[1-h[0]]+[-x for x in h[1:]]
require(num==[0,0,6,-8,3],'universal ideal-square Hilbert numerator')
# Restricted adjoint signs are inherited from F|L and physical twisting.
def line(t):return [(7+t,(-1)**(t+1)),(t,(-1)**t),(-7+t,(-1)**(t+1))]
require(line(3)==[(10,1),(3,-1),(-4,1)],'twist3 line parity')
require(line(4)==[(11,-1),(4,1),(-3,-1)],'twist4 line parity')
require(sum(max(d+1,0) for d,s in line(4) if s==1)==5,'positive H0 B_L4 dimension')
require(sum(max(-d-1,0) for d,s in line(4) if s==1)==0,'positive H1 B_L4 vanishes')
require(vm(V,A)==va(P,D),'conormal obstruction P+D')
require(va(P,D)[0]==z(9) and P[0]==z(4),'two possible doubled-line cokernels')
q_image=va(vs(2,V),vs(3,P),vs(3,D));target=va(vs(2,V),vs(4,P),vs(3,D))
require(target==va(q_image,P),'exact invariant quotient')
require(q_image[0]==z(33) and target[0]==z(37),'actual image and target dimensions imported')
XF=va(V,P,vs(2,D));Pi=va(V,P)
require(XF==va(Pi,vs(2,D)),'conditional invariant quotient kernel')
require((XF[0],Pi[0],vs(2,D)[0])==(z(17),z(7),z(10)),'conditional dimensions')
# High cohomology support bookkeeping only, not a sheaf proof.
for t in (0,1,2):
 require(all(-s-4 not in range(4) for s in (t-3,t-2)),'H3 E0 support')
 require(-t<3,'H4 E1 support')
 require(all(-s-4<3 for s in (t-3,t-2)),'H4 E0 support')
root=Path(__file__).parent;man=root/'audit-inputs'/'manifest.json'
if man.exists():
 entries=json.loads(man.read_text());require(len(entries)==4,'four input originals')
 for e in entries:
  b=(root/'audit-inputs'/e['name']).read_bytes()
  require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['blob'],'input blob '+e['name'])
 print('PASS: all four immutable input blobs authenticate exactly.')
print('PASS: fixed squared-ideal coefficient characters and universal Hilbert numerator 6t²-8t³+3t⁴.')
print('PASS: fixed-line parities, conormal P+D, invariant quotient P and image33.')
print('PASS: next-arrow quotient kernel D and conditional X_F quotient kernel 2D.')
print('BOUNDARY: exactness and image equality require the written proof; no actual HM tensor, coefficients, points or instance ranks are evaluated.')
