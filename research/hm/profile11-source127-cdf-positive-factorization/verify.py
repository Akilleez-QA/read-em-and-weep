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
H=va(V,W)
L2=vs(F(1,2),va(vm(H,H),vs(-1,psi2(H))))
require(L2==va(V,vm(V,W),one),'exterior square H')
N=va(A,Wp)
# Sym^n(V+W), with V=Sym2 Wp; degrees only 2 through 8.
def sn(n):
 return [total(mul(total(sym(2*i-4*j,xp) for j in range(i//2+1)),sym(n-i,x)) for i in range(n+1)) for x,xp in zip(W,Wp)]
c={-1:vs(-1,N),0:va(vm(Wp,L2),vs(-1,N)),1:vs(-1,vm(Wp,H)),2:Wp}
chi=va(*[vs(F(1,2),vm(vm(ci,cj),sn(i+j+4))) for i,ci in c.items() for j,cj in c.items()],
       *[vs(F(1,2),vm(psi2(ci),sn(2*i+4))) for i,ci in c.items()])
k4=vs(-1,chi)
positive=va(one,vs(4,A),vs(2,V),vs(3,P),vs(3,D))
negative=va(vs(3,Wp),vs(3,S),vs(6,T))
require(k4==va(positive,negative),'actual Euler character all nine classes')
require(positive[0]==z(46) and negative[0]==z(54),'middle parity dimensions')
require(positive[1]==z(46) and negative[1]==z(-54),'central parity signs')
require(vm(V,V)==va(one,V,D),'V square')
require(vm(V,P)==va(A,P,D),'V tensor P')
minimal=vm(V,va(V,P)); expected_min=va(one,A,V,P,vs(2,D))
complement=va(vs(3,A),V,vs(2,P),D)
require(minimal==expected_min,'minimal positive factor character')
require(va(minimal,complement)==positive,'prescribed middle containment')
require(minimal[0]==z(21) and complement[0]==z(25),'minimal/complement dimensions')
for label,ch in [('K4+',positive),('K4-',negative),('minimal',minimal),('complement',complement)]:
 mult={name:inner(ch,r) for name,r in reps.items()}
 require(all(b==0 and a.denominator==1 and a>=0 for a,b in mult.values()),label+' genuine character')
 print(label, {name:int(a) for name,(a,b) in mult.items() if a})
# Input authentication is optional only when audit copies have not been downloaded.
root=Path(__file__).parent; manifest=root/'audit-inputs'/'manifest.json'
if manifest.exists():
 for e in json.loads(manifest.read_text()):
  data=(root/'audit-inputs'/e['name']).read_bytes()
  blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
  require(blob==e['blob'],'input blob mismatch: '+e['name'])
 print('PASS: five exact original input blobs authenticated.')
print('PASS: fixed nine-class Euler derivation and 21+25=46 containment.')
print('BOUNDARY: factor theorem, cohomological vanishing and mixed-map distinctions require the written proof.')
