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
N2=va(A,vs(2,V),vs(3,P),vs(4,D))
source=vm(V,N2)
expected_source=va(vs(2,one),vs(7,A),vs(6,V),vs(8,P),vs(10,D))
require(source==expected_source,'positive first-arrow source character')
middle=va(one,vs(4,A),vs(2,V),vs(3,P),vs(3,D))
reachable=va(one,vs(3,A),vs(2,V),vs(3,P),vs(3,D))
relations=va(one,vs(4,A),vs(4,V),vs(5,P),vs(7,D))
require(middle==va(reachable,A),'restriction quotient A')
require(source==va(relations,reachable),'first-arrow exact sequence')
inv_kernel=vm(V,va(A,D))
require(inv_kernel==va(A,V,vs(2,P),vs(2,D)),'invariant curry kernel')
forced=va(one,vs(3,A),vs(3,V),vs(3,P),vs(5,D))
require(relations==va(inv_kernel,forced),'canonical cancellation deficit')
inv_image=vm(V,va(vs(2,V),vs(3,P),vs(3,D)))
require(inv_image==va(reachable,forced),'independent image-sum check')
require([c[0] for c in [source,middle,reachable,relations,inv_kernel,forced,inv_image]]==list(map(z,[123,46,43,80,24,56,99])),'all dimensions')
# The three line summands come from Hom degrees and physical twist sign.
line=[(3-(-4)+3,(-1)*(+1)*(-1)),(3,(+1)*(-1)),((-4)-3+3,(+1)*(-1)*(-1))]
require(line==[(10,1),(3,-1),(-4,1)],'restricted adjoint degree/sign calculation')
require(sum(max(-d-1,0) for d,sgn in line if sgn==1)==3,'positive H1 on the line')
# Check only the support-based diagonal bookkeeping, not sheaf exactness.
for t in (0,1):
 require(all(-s-4 not in range(4) for s in (t-3,t-2)),'H3 E0 primary support')
 require(-(t-4)-4<3,'H4 E1 primary section support')
require(all(-s-4<3 for s in (-3,-2)),'H4 E0 at zero')
root=Path(__file__).parent;man=root/'audit-inputs'/'manifest.json'
if man.exists():
 entries=json.loads(man.read_text())
 require(len(entries)==5,'exactly five authenticated inputs')
 for e in entries:
  b=(root/'audit-inputs'/e['name']).read_bytes()
  require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['blob'],'input blob '+e['name'])
 print('PASS: all five immutable input blobs authenticate exactly.')
print('PASS: four fixed tensor identities, source123, middle46, reachable43, relations80.')
print('PASS: invariant kernel24, canonical common cancellation lower bound56, independent 99-43 check.')
print('PASS: fixed-line parity/degrees and primary-support bookkeeping.')
print('BOUNDARY: no actual tensor, coefficient, matrix, parameter, point or instance-rank evaluation; no full-module relation claim.')
