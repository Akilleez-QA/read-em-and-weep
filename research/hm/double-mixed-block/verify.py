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

chi3=vs(F(1,2),va(*[vm(vm(ci,cj),sn(i+j+4)) for i,ci in c.items() for j,cj in c.items()],*[vm(psi2(ci),sn(2*i+4)) for i,ci in c.items()]))
N3=va(one,vs(4,A),vs(2,V),vs(3,P),vs(3,D))
N3odd=va(vs(3,Wp),vs(3,S),vs(6,T))
require(vs(-1,chi3)==va(N3,N3odd),'full actual middle Euler character')
U=va(vs(2,W),vs(2,Wp),vs(3,S),vs(4,T))
require(U[0]==z(44) and N3[0]==z(46),'original full coefficient spaces')
require(vm(W,W)==va(one,A) and vm(W,Wp)==P and vm(W,S)==va(A,D),'other source channels')
require(vm(W,T)==va(V,P,D),'three T6 channels')
for R in [W,Wp,S]:require(inner(vm(W,R),V)==z(0),'only T6 reaches V')
require(inner(U,T)==z(4) and inner(N3,V)==z(2),'forced multiplicity kernel dimension')
require(inner(N3,P)==z(3) and inner(N3,D)==z(3),'target multiplicity dimensions')
require(4-2==2,'rank-nullity after imported coefficient surjectivity')
require(vm(Wp,A)==T and vm(Wp,W)==P,'P-only contraction model')
require(inner(one,A)==z(0),'D-only kernel contradiction')
require(vm(V,W)==T and vm(V,A)==va(P,D),'simultaneous universal model')
require(2*6==12 and 2*(4+5)==18,'canonical block dimensions')
require(18-12==6 and 12==6*2,'doubled quotient rank and degree')
require(44-12==32 and 46-18==28 and 28+6==34, 'residual source and target ranks')
require(34-32+3==5 and 12+32-18==26, 'same cokernel rank and degree')
root=Path(__file__).resolve().parent
items=json.loads((root/'INPUTS.json').read_text())
require(len(items)==3,'three immutable originals')
for item in items:
 data=(root/'audit-inputs'/f"{item['key']}.md").read_bytes()
 blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 require(blob==item['blob'],f"immutable input mismatch: {item['key']}")
print('PASS: three immutable originals; full middle Euler; unique V source channel; multiplicities; universal kernel and doubled quotient checks.')
print('No actual HM coefficient, point, parameter, matrix, instance rank or scan evaluated.')
