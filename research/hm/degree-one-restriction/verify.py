#!/usr/bin/env python3
"""Universal character and dimension checks, with no HM coefficient evaluation."""
from fractions import Fraction as F

def z(a,b=0): return (F(a),F(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(k,x): return (k*x[0],k*x[1])
def seq_sum(xs):
    out=z(0)
    for x in xs: out=add(out,x)
    return out
# SU2 traces on the nine conjugacy classes of the abstract binary A5.
phi=z(F(1,2),F(1,2)); phip=z(F(1,2),F(-1,2))
tr=[z(2),z(-2),phi,neg(phi),phip,neg(phip),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
assert sum(sizes)==120

def sym(n,x):
    if n==0:return z(1)
    a,b=z(1),x
    for _ in range(2,n+1): a,b=b,sub(mul(x,b),a)
    return b

def inner(a,b):return scale(F(1,120),seq_sum(scale(k,mul(x,y)) for k,x,y in zip(sizes,a,b)))
def vadd(*args):return [seq_sum(v) for v in zip(*args)]
def vmul(a,b):return [mul(x,y) for x,y in zip(a,b)]
def vscale(k,a):return [scale(k,x) for x in a]

one=[z(1)]*9; W=tr; A=[sym(2,x) for x in tr]
S=[sym(3,x) for x in tr]; D=[sym(4,x) for x in tr]; T=[sym(5,x) for x in tr]
P=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
V=[sub(sym(6,x),p) for x,p in zip(tr,P)]
Wp=[sub(mul(w,p),t) for w,p,t in zip(W,P,T)]
for chi in (W,Wp,A,V,P,S,D,T): assert inner(chi,chi)==z(1)
assert inner(A,V)==z(0)
# Characters of Gamma x physical C2, stored by evaluation at epsilon=+1,-1.
irreps=[one,W,Wp,A,V,P,S,D,T]
names=['1','W','U','A','V','P','S','D','T']
def ca(*cs):return vadd(*cs)
def cm(*cs):
 r=one+one
 for c in cs:r=vmul(r,c)
 return r
def cs(k,c):return vscale(k,c)
def lift(c,parity=1):return c+vscale(parity,c)
# Abstract representation identities only. No actual monad, point or matrix inputs.
def eq(a,b): assert a==b
U=Wp
eq(vmul(vmul(U,V),W),vadd(A,P,D))
eq(vmul(U,vadd(one,V)),vadd(vscale(2,U),S))
eq(vmul(U,[sym(5,x) for x in tr]),vadd(A,P,D))
eq([sym(8,x) for x in tr],vadd(P,D))
eq(vmul(D,P),vadd(A,V,P,vscale(2,D)))
# Therefore binary multiplication D tensor P -> U tensor Sym5 W
# has kernel V+D, and the upper-only octic image is P+D.
def sym2(c):
 return [scale(F(1,2),add(mul(c[i],c[i]),c[tr.index(sub(mul(t,t),z(2)))])) for i,t in enumerate(tr)]
Ge=vadd(A,P,D); Go=vadd(vscale(2,U),S)
Re=vadd(sym2(Ge),sym2(Go))
assert Re[0]==z(114)
image=vadd(A,vscale(2,P),vscale(2,D)); kernel=[sub(x,y) for x,y in zip(Re,image)]
assert image[0]==z(21) and kernel[0]==z(93)
for chi in (one,A,V,P,D): assert inner(kernel,chi)[0]>=0 and inner(kernel,chi)[1]==0
# Frobenius reciprocity on the abstract C10 stabilizer.
weights={'1':[0],'A':[2,0,-2],'V':[6,0,-6],
         'P':[4,2,-2,-4],'D':[4,2,0,-2,-4]}
def induced(exponent):
 return {name:sum((w+exponent)%10==0 for w in ws) for name,ws in weights.items()}
assert induced(8)=={'1':0,'A':1,'V':0,'P':1,'D':1}
assert induced(14)=={'1':0,'A':0,'V':1,'P':1,'D':1}
assert (3*4-2)%10==0 and (3*5-5)%10==0
# Binary multiplication monomials span each target degree.
assert {i+j for i in range(5) for j in range(2)}==set(range(6))
assert {i+j for i in range(5) for j in range(5)}==set(range(9))
# Six positive roots leave six values; octics interpolate any <=9 values.
assert 12-6==6 and 6<=8+1
# Receiving/source dimensions and exact kernels after proved surjectivity.
P2=vadd(one,A,V,vscale(2,P),vscale(3,D))
receiving=vscale(3,vadd(V,P,D))
assert receiving[0]==z(36) and inner(P2,receiving)==z(18)
assert 1203-18==1185 and 1113-18==1095
assert 2409-36==2373 and 2229-36==2193
assert 1203-(90+18)==1095 and 2409-(180+36)==2193
print('PASS: universal characters, binary monomial products, interpolation counts, and exact kernel dimensions. No actual instance evaluated.')
