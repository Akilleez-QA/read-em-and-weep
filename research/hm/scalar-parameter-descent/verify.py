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
unit=lift(one)
def adams(c,k):
 out=[]
 for eps in [1,-1]:
  for t in tr:
   # trace(g^k) = Sym^k(trace g)-Sym^(k-2)(trace g)
   tk=sub(sym(k,t),sym(k-2,t)) if k>=2 else t
   j=tr.index(tk)
   out.append(c[j+(0 if eps**k==1 else 9)])
 return out
def power(c,n,exterior=False):
 vals=[unit]
 for j in range(1,n+1):
  vals.append(cs(F(1,j),ca(*[cs((-1)**(k-1) if exterior else 1,cm(vals[j-k],adams(c,k))) for k in range(1,j+1)])))
 return vals[n]
def plus(c):return vscale(F(1,2),vadd(c[:9],c[9:]))
def decomp(c):
 out=[inner(c,r) for r in irreps]
 assert all(y==0 and x.denominator==1 and x>=0 for x,y in out),out
 return [int(x) for x,y in out]

# Only abstract binary-icosahedral representations enter below.
positive_binary=Wp
assert [sym(4,x) for x in positive_binary]==D
assert [sym(8,x) for x in positive_binary]==vadd(P,D)
scalar_target=vmul([sym(8,x) for x in positive_binary],A)
parameter=vmul(plus(power(lift(A),3)),D)
discriminant_kernel=vmul(A,D)
square_parameter=vmul([sym(6,x) for x in W],D)
assert decomp(scalar_target)==[0,0,0,1,2,2,0,2,0]
assert decomp(parameter)==[0,0,0,3,3,3,0,4,0]
assert decomp(discriminant_kernel)==[0,0,0,1,1,1,0,1,0]
assert parameter==vadd(discriminant_kernel,square_parameter)
assert scalar_target[0]==z(27) and parameter[0]==z(50)
assert discriminant_kernel[0]==z(15) and square_parameter[0]==z(35)
assert inner(parameter,scalar_target)==z(23)
assert inner(discriminant_kernel,scalar_target)==z(7)
assert inner(square_parameter,scalar_target)==z(16)
assert plus(power(lift(A),3))==vadd(A,[sym(6,x) for x in W])
print('PASS: target27; cubic-linear family23; discriminant kernel7; square-visible quotient16.')
print('Only exact abstract characters were checked; no actual HM/source evaluation or formal proof check.')
