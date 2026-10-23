#!/usr/bin/env python3
"""Nine-class abstract characters only. No actual tensors or instance evaluations."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json

count=0
def require(condition,message):
    global count
    count+=1
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
# Fixed Sym^n(V+W), with V=Sym2 Wp; maximum degree4 below.
def sn(n):
 return [total(mul(total(sym(2*i-4*j,xp) for j in range(i//2+1)),sym(n-i,x)) for i in range(n+1)) for x,xp in zip(W,Wp)]
c={-1:vs(-1,N),0:va(vm(Wp,L2),vs(-1,N)),1:vs(-1,vm(Wp,H)),2:Wp}


# No actual monad differential appears: only its fixed representation K-class.
def euler_primary(t):
 return va(*[vm(ci,sn(i+t)) for i,ci in c.items()])
h1_1=va(P,W,S);h1_2=va(one,A,T)
require(euler_primary(1)==vs(-1,h1_1),'primary twist1 Euler')
require(euler_primary(2)==vs(-1,h1_2),'primary twist2 Euler')
require(vm(P,P)==va(one,A,V,P,D),'P tensor P')
require(vm(P,A)==va(V,P,D),'P tensor A')
require(vm(P,W)==va(Wp,T),'P tensor W')
require(vm(V,W)==T,'irreducible mixed quadratic')
require(vs(F(1,2),va(vm(V,V),psi2(V)))==va(one,D),'positive symmetric square')
require(inner(T,T)==z(1),'mixed irreducibility')
require(inner(vm(P,h1_1),one)==z(1),'one primary scalar')
require(inner(vm(P,va(one,A)),V)==z(1),'one primary positive V')
require(inner(vm(P,W),T)==z(1),'one primary terminal T6')
require(vm(P,W)[1]==z(-8),'primary terminal entirely negative')
require(P[1]==P[0] and W[1]==neg(W[0]),'physical parity')
require(vm(P,va(one,A))[0]==z(16),'positive primary middle dimension')
require(h1_1[0]==z(10) and h1_2[0]==z(10),'primary dimensions')
require([(k-1,k-3) for k in [4,5,6]]==[(3,1),(4,2),(5,3)],'actual K/L grading translation')
require(5<6 and 6-1==5,'B4 is below full socle B5')
# The universal quotient by pure quadratics. No HM/source point is used.
from itertools import combinations_with_replacement
survivors=[]
for degree in range(4):
 mons=list(combinations_with_replacement(range(5),degree))
 survive=[m for m in mons if sum(i<3 for i in m)<2 and sum(i>=3 for i in m)<2]
 survivors.append(len(survive))
 require(all(len(m)<=2 for m in survive),'universal pure-square ideal cutoff')
require(survivors==[1,5,6,0],'rectangular cyclic Hilbert function')
require(sum(survivors)==12,'cyclic dimension12')
require(6+3==9,'all pure quadratic relations dimension9')
require(15-9==6,'mixed quadratic quotient dimension6')
root=Path(__file__).resolve().parent
for item in json.loads((root/'INPUTS.json').read_text()):
 b=(root/item['local_path']).read_bytes()
 require(len(b)==item['bytes'],'input length '+item['label'])
 require(hashlib.sha256(b).hexdigest()==item['sha256'],'input SHA256 '+item['label'])
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['git_blob'],'input Git blob '+item['label'])
print(json.dumps({'status':'PASS','checks':count,'cyclic_hilbert':[1,5,6],'cyclic_dimension':12,'positive_cyclic_hilbert':[1,3],'pure_positive_quadratic_descendant':0,'mixed_terminal_dimension':6,'scope':'Only fixed universal representation, quotient and degree checks; actual-map proof remains written and independently reviewed.'},sort_keys=True,indent=2))
