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



# Symmetric powers of the actual ambient V+W, where V=Sym²Wprime.
def symmetric_three(n,trace_two):
    return seq_sum(sym(2*n-4*j,trace_two) for j in range(n//2+1))
def ambient_sym(n):
    return [seq_sum(mul(symmetric_three(i,xp),sym(n-i,x)) for i in range(n+1))
            for x,xp in zip(W,Wp)]
H=vadd(V,W)
L2=vadd(V,vmul(V,W),one)
O4,O5,O6,O7=[ambient_sym(n) for n in (4,5,6,7)]
Omega=vadd(vmul(L2,O5),vscale(-1,vmul(H,O6)),O7)
N=vadd(A,Wp)
F5=vadd(vmul(Wp,Omega),vscale(-1,vmul(N,vadd(O4,O5))))
assert F5==vadd(A,vscale(4,V),vscale(4,P),vscale(5,D),vscale(3,W),Wp,vscale(3,S),vscale(4,T))
assert F5[0]==z(100) and inner(W,F5)==z(3)
M1=vadd(vmul(N,vadd(one,H)),vscale(-1,vmul(Wp,L2)))
assert M1==vadd(P,W,S) and M1==vmul(W,N)
source1=vmul(N,vmul(A,V))
source2=vmul(N,vmul(S,V))
target=vmul(M1,vmul(S,V))
higher=vmul(Wp,A)
assert inner(W,source1)==inner(W,source2)==z(1)
assert inner(W,target)==z(2)
assert inner(W,higher)==z(0)
assert higher==T
restriction_target=vadd([sym(8,x) for x in W],W)
assert inner(W,restriction_target)==z(1)
print('PASS: actual monad character at twist five has dimension100 and three W copies.')
print('PASS: independent twist-one check gives H1(F(1))=P+W+Sym3W=W tensor H1(F).')
print('PASS: product-ideal W multiplicities are source1+1, target2, higher0.')
print('PASS: the full negative-line restriction target contains exactly one W.')
print('No actual multiplication scalar, source-instance coefficient, or rank was evaluated.')
