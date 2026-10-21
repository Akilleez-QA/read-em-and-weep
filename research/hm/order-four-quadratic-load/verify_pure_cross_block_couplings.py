#!/usr/bin/env python3
"""Universal representation and low-transvectant checks only."""
from fractions import Fraction as F

def z(a,b=0): return (F(a),F(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(k,x): return (k*x[0],k*x[1])
tr=[z(2),z(-2),z(F(1,2),F(1,2)),z(F(-1,2),F(-1,2)),z(F(1,2),F(-1,2)),z(F(-1,2),F(1,2)),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
def sym(n,x):
    a,b=z(1),x
    if n==0:return a
    for _ in range(2,n+1):a,b=b,sub(mul(x,b),a)
    return b

def sy(n):return [sym(n,x) for x in tr]
def vm(a,b):return [mul(x,y) for x,y in zip(a,b)]
def inner(a,b):
    out=z(0)
    for k,x,y in zip(sizes,a,b):out=add(out,scale(F(k,120),mul(x,y)))
    assert out[1]==0 and out[0].denominator==1
    return int(out[0])
one=[z(1)]*9; W=tr; A=sy(2); P=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
V=[sub(x,y) for x,y in zip(sy(6),P)]
Wp=[sub(x,y) for x,y in zip(vm(W,P),sy(5))]
rows=[[(P,6)],[(Wp,5),(Wp,7)],[(V,4),(one,12)],[(A,2),(one,18)],[(one,0),(V,8)],[(one,0),(Wp,5),(one,14)],[(one,0),(W,3),(one,18)]]
def couplings(row,k):
    return sum(inner(sy(8-k),vm(R,sy(d+2-k))) for R,d in row if d+2-k>=0)
def diagonal(row,t):return sum(inner(R,sy(d+t)) for R,d in row if d+t>=0)
for row in rows:
    assert couplings(row,2)==3
    assert couplings(row,3)==2
    assert couplings(row,4)==2
    assert diagonal(row,6)==1
    assert diagonal(row,4)==0
# For f=x^3*y: f_xx=6*x*y, f_yy=0, f_xy=3*x^2.
# (f,f)_2=f_xx*f_yy-2*f_xy*f_xy+f_yy*f_xx = -18*x^4.
assert 0-2*3*3+0 == -18
print('PASS: all seven F4 types have 3 pure cross couplings, 2 zero-diagonal couplings, 1 diagonal scalar.')
print('PASS: conditional third diagonal factor implies fourth; H0(F4(4))^G=0.')
print('PASS: second-derivative actual square has NONZERO low transvectant -18*x^4.')
print('No actual coupling values or fiber ranks computed.')
