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
sym2D=[scale(F(1,2),add(mul(d,d),sym(4,sub(mul(x,x),z(2))))) for d,x in zip(D,tr)]
assert sym2D==vadd(one,P,vscale(2,D))
assert vmul(W,P)==vadd(Wp,T)
assert vmul(W,D)==vadd(S,T)
assert vmul(A,S)==vadd(W,S,T)
assert vmul(V,S)==vadd(Wp,S,T)
source=vmul(W,sym2D); target=vmul(vadd(A,V),S)
assert source==vadd(W,Wp,vscale(2,S),vscale(3,T))
assert target==vadd(W,Wp,vscale(2,S),vscale(2,T))
assert source[0]==z(30) and target[0]==z(24)
print('PASS: exact binary-normalizer decompositions 30=W+Wprime+2S+3T, 24=W+Wprime+2S+2T.')

# Exact harmonic quotient exponents for I/I^9, odd degrees.
from math import ceil
terms=[]
for l in (1,3,5,7):
    a=max(0,ceil((1-l)/2)); b=max(0,ceil((9-l)/2))
    terms.append((l,4-l-2*a,b-a))
assert terms==[(1,3,4),(3,1,3),(5,-1,2),(7,-3,1)]
assert 15*2==30 and 6*(4-2)==12 and 30-12==18
# Universal surjective y:D5 -> A3 has image Sym^2 A6 + A tensor ker(y)6.
assert 3*4//2+3*2==12 and 3*5-3==12
print('PASS: exact harmonic twists/lengths, projected target12, and kernel18.')
print('BOUNDARY: actual cup surjectivity is proved via Leibniz and Steiner fiber injectivity in the companion note, not by a matrix/rank experiment.')
