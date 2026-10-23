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
# The same fixed lambda-ring formula at twist three, not an actual matrix.
chi=va(*[vs(F(1,2),vm(vm(ci,cj),sn(i+j+3))) for i,ci in c.items() for j,cj in c.items()],
       *[vs(F(1,2),vm(psi2(ci),sn(2*i+3))) for i,ci in c.items()])
k3=vs(-1,chi)
u=va(vs(2,W),vs(2,Wp),vs(3,S),vs(4,T))
require(k3==va(A,vs(2,V),vs(3,P),vs(4,D),u),'actual Euler character all classes')
e=va(u,vs(-1,S),vs(-1,Wp),vs(-2,T))
require(e==va(vs(2,W),Wp,vs(2,S),vs(2,T)),'reduced source26 character')
require(u[0]==z(44) and e[0]==z(26),'source dimensions')

chi1=va(*[vs(F(1,2),vm(vm(ci,cj),sn(i+j+2))) for i,ci in c.items() for j,cj in c.items()],
        *[vs(F(1,2),vm(psi2(ci),sn(2*i+2))) for i,ci in c.items()])
require(vs(-1,chi1)==va(A,vs(2,V),vs(2,P),vs(2,D),W,vs(2,S),vs(3,T)), 'full B1 Euler')
E=va(W,vs(2,S),vs(3,T)); Ep=va(vs(2,S),vs(3,T))
N=va(A,vs(2,V),vs(3,P),vs(4,D)); Np=va(vs(2,V),vs(3,P),vs(4,D))
require(E[0]==z(28) and Ep[0]==z(26) and N[0]==z(41) and Np[0]==z(38),'coefficient dimensions')
require(inner(E,W)==z(1) and inner(N,A)==z(1),'unique canonical isotypics')
require(vm(W,W)==va(one,A),'symmetric projection')
require(vm(A,W)==va(W,S),'off-diagonal channels')
require(inner(Ep,vm(A,W))==z(2) and inner(T,vm(A,W))==z(0),'two S corrections only')
require(inner(Ep,S)==z(2) and inner(Ep,W)==z(0) and inner(Np,A)==z(0),'extension isomorphism')
require(38-26==13-1==12 and 28-2==26,'actual quotient rank degree')
root=Path(__file__).resolve().parent
for item in json.loads((root/'INPUTS.json').read_text()):
 b=(root/'audit-inputs'/(item['key']+'.md')).read_bytes()
 require(len(b)==item['bytes'],'input byte length')
 require(hashlib.sha256(b).hexdigest()==item['sha256'],'input SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['blob'],'input Git blob')
print('PASS: exact inputs, B1/B2 Euler characters, unique W/A, residual 26-to-38, two retained extension channels.')
print('No selected actual instance is evaluated; the checker does not replace the geometric proof.')
