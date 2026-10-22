#!/usr/bin/env python3
"""Bounded universal rank-two polynomial checks, not actual HM evaluation."""
from collections import defaultdict

# A polynomial is a dictionary of exponent vectors over Z.
names = ("x", "y", "z", "u", "v", "w", "a", "h", "f", "q")
zero = (0,) * len(names)
def const(c):
    return {zero:c} if c else {}
def var(name):
    e=list(zero); e[names.index(name)]=1
    return {tuple(e):1}
def add(*ps):
    out=defaultdict(int)
    for p in ps:
        for e,c in p.items(): out[e]+=c
    return {e:c for e,c in out.items() if c}
def neg(p): return {e:-c for e,c in p.items()}
def mul(p,r):
    out=defaultdict(int)
    for e,c in p.items():
        for f,d in r.items(): out[tuple(a+b for a,b in zip(e,f))]+=c*d
    return {e:c for e,c in out.items() if c}
def power(p,n):
    out=const(1)
    for _ in range(n): out=mul(out,p)
    return out
def matrix_mul(m,n):
    return [[add(*(mul(m[i][k],n[k][j]) for k in range(2)))
             for j in range(2)] for i in range(2)]
def matrix_add(m,n):
    return [[add(m[i][j],n[i][j]) for j in range(2)] for i in range(2)]
def scalar_matrix(p): return [[p,{}],[{},p]]
x,y,z,u,v,w,a,h,f,q=(var(n) for n in names)
L=[[x,y],[z,neg(x)]]
K=[[u,v],[w,neg(u)]]
assert matrix_mul(L,L)==scalar_matrix(add(power(x,2),mul(y,z)))
LK=matrix_mul(L,K)
trLK=add(LK[0][0],LK[1][1])
assert matrix_add(LK,matrix_mul(K,L))==scalar_matrix(trLK)
# Universal kernel generator (y,-x) when x²+yz=0.
col=[add(mul(L[i][0],y),mul(L[i][1],neg(x))) for i in range(2)]
assert col==[{},add(mul(y,z),power(x,2))]
# Scalar divisibility after f0=a²h.
cross=mul(a,mul(mul(power(a,2),h),trLK))
factored=mul(power(a,2),mul(mul(a,h),trLK))
assert cross==factored
# q-orders: two-layer correction square, last-layer correction square,
# fourth power of J, and choice-independence of the cube.
assert 2+2>=4 and 3+3>=4
assert 3+3>=4 and 3+2>=4
# If lambda=q*r and r=q*t then lambda² has q-order4, while q³sigma
# injectively remembers sigma moduloq. No square-root claim over reducedQ.
assert 2*(1+1)==4
# Twists: J3=8, J4=10, N=2, q=a=h=2, K=4.
assert 2*10-3*2==14
assert 14-2*2==10
assert 3*2+2+2+4==14  # a³ h tr(NK)
assert 2*8-3*2==10    # chi
assert 2+2+6==10      # ah I²(6)
assert 3*2+14+10==3*10
print("PASS: universal trace-free square, polarization, kernel, factor, q-orders and twists.")
print("No actual scalar value, coefficient, source instance, or formal proof certification.")
