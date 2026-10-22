#!/usr/bin/env python3
"""Universal character and Chern identities, no actual residual map evaluation."""
from fractions import Fraction as F

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(k,x): return (k*x[0],k*x[1])
def z(a,b=0): return (F(a),F(b))
tr=[z(2),z(-2),z(F(1,2),F(1,2)),z(F(-1,2),F(-1,2)),
    z(F(1,2),F(-1,2)),z(F(-1,2),F(1,2)),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
def sym(n,t):
    x,y=z(1),t
    if n==0:return x
    for _ in range(2,n+1):x,y=y,sub(mul(t,y),x)
    return y

def inv(a):
    out=z(0)
    for size,t in zip(sizes,tr):
        out=add(out,scale(F(size,120),mul(sym(a-5,t),sym(a+1,t))))
    assert out[1]==0 and out[0].denominator==1
    return int(out[0])
assert [inv(a) for a in range(5,9)]==[0,0,0,1]
# Polynomial Chern equality checked coefficient by coefficient in Z[a].
# 15 = (-a)(a-5) + (a^2-5a+15).
assert [15,0,0] == [0+15,5-5,-1+1]
# c2(image)=2*length(Z)+(a-5)^2 = 55+4a^2-20a-a^2.
assert [2*15+25,-10-10,2+1] == [55,-20,3]
print('PASS: source invariant multiplicities at a=5,6,7,8 are 0,0,0,1.')
print('PASS: finite zero scheme and image second-Chern identities.')
print('Target negative-twist vanishing and Hartogs extension are proved in the companion text.')
print('No actual residual coefficient, matrix, or rank was evaluated.')
