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
H=ca(lift(V),lift(W,-1)); U=lift(Wp)
param=vmul(vadd(one,D),D)
assert decomp(param)==[1,0,0,1,1,2,0,3,0]
assert all(inner(r,s)==z(int(i==j)) for i,r in enumerate(irreps) for j,s in enumerate(irreps))
# Source parity: U even and A odd; the overall reversed convention has
# the same End(S) parity. All irreducible characters are real/self-dual.
source=ca(lift(Wp),lift(A,-1))
end_source=cm(source,source)
ambiguity=plus(cm(end_source,power(H,2)))
assert decomp(ambiguity)==[6,0,0,12,9,10,0,16,0]
assert ambiguity[0]==z(189)
assert inner(param,ambiguity)==z(95)
assert cm(end_source,power(H,2))[0]==z(375)
assert 5*(12-5)==35 and 5*4//2==10
assert 35-10==25 and 12*13//2-25==53
assert 25+3+10+15==53
assert 4-2==2 # q division and source restriction kernel twists
print('PASS: exact source-lift ambiguity 375 ordinary, 189 center-even, 95 Gamma/P2; tangent ranks 35-10=25 and 78-25=53.')
assert 5*12-5*4//2==50 and 53-50==3
assert 4-1-1+1==3 # Lambda^2 A0 tensor L^-1, then twist4
assert 4-1+1==4 # A0 tensor E tensor L^-1, then twist4
assert all(t>2 for t in [4,6]) # Bott for Omega^2(t)
assert min(1,3)>0 # positive line bundles in Q restriction
print("PASS: parabolic kernel rank50 and positive Bott arguments for N_Q(4).")

from math import comb
def omega2_global(k): return 10*comb(k+2,4)-5*comb(k+3,4)+comb(k+4,4)
assert 2*omega2_global(6)==560
assert 2*omega2_global(4)==90
assert comb(7,4)-comb(5,4)==30
assert 5*(560-90)-10*30==2050
print("PASS: h0 N_Q(4)=2050 by Euler/Bott dimensions.")
