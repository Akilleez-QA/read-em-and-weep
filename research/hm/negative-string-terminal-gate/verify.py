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

chi5=va(*[vs(F(1,2),vm(vm(ci,cj),sn(i+j+6))) for i,ci in c.items() for j,cj in c.items()],
        *[vs(F(1,2),vm(psi2(ci),sn(2*i+6))) for i,ci in c.items()])
require(chi5==va(P,vs(-1,A),vs(-1,V),vs(-1,Wp),vs(-3,T)), 'degree-five Euler')
h0=va(one,P,D); h1=va(h0,vs(-1,chi5))
require(h1==va(one,A,V,D,Wp,vs(3,T)), 'actual H1 character with section input')
M3=va(vs(3,Wp),vs(3,S),vs(6,T)); M4=va(vs(2,V),vs(4,P),vs(3,D)); M5=va(Wp,vs(3,T))
require(va(vm(W,M4),vs(-1,M3))==M5,'exact Koszul character')
require(vm(W,D)==va(S,T),'Euler source character')
require(vm(W,M5)==va(vs(3,V),vs(4,P),vs(3,D)),'joint-kernel limitation')
require(inner(T,M5)==z(3),'unselected terminal multiplicity')
R3=va(vs(3,Wp),vs(2,S),vs(5,T)); R4=va(vs(2,V),vs(4,P),vs(2,D))
require(va(M3,vs(-1,S),vs(-1,T))==R3 and va(M4,vs(-1,D))==R4,'canonical quotient characters')
require(R3[0]==z(44) and R4[0]==z(32),'quotient ranks')
require(54-37==17 and 44-32==12 and -54-(-10)==-44,'kernel ranks and degrees')
root=Path(__file__).resolve().parent
for item in json.loads((root/'INPUTS.json').read_text()):
 b=(root/'audit-inputs'/(item['key']+'.md')).read_bytes()
 require(len(b)==item['bytes'],'input length')
 require(hashlib.sha256(b).hexdigest()==item['sha256'],'input SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['blob'],'input Git blob')
print('PASS: exact inputs, degree-five Euler/sections, exact Koszul characters, terminal multiplicity, Euler-subpencil quotient.')
print('No actual instance evaluated and no terminal branch selected.')
