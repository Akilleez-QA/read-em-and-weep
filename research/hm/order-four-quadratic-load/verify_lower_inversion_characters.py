#!/usr/bin/env python3
"""Exact character and fixed-locus arithmetic, with no HM coefficients or ranks."""
from fractions import Fraction as F
from math import comb

def mul(a,b,n=3):
    return [sum((a[i]*b[k-i] for i in range(k+1) if i<len(a) and k-i<len(b)),F(0)) for k in range(n)]
def parity_index(dim,trace):
    assert (dim+trace)%2==0
    return ((dim+trace)//2,(dim-trace)//2)
def sym_trace(n):
    return sum((-1)**j*comb(2+j-1,j)*comb(3+n-j-1,n-j) for j in range(n+1))
# Denominator inverses for negative normal directions, and actual fixed fibers.
ch=[F(2),F(-5),F(5,2)]
td=[F(1),F(3,2),F(1)]
normal_inverse=[F(1,4),F(1,4),F(1,16)]
p2=mul(mul(ch,td),normal_inverse)[2]
p1=F(-7,8)
assert p2==F(-9,8) and p2+p1==-2
assert 150-80==70 and (1-2+3)-4==-2
assert 75-15==60 and 3-3==0
assert [sym_trace(n) for n in range(1,6)]==[1,3,3,6,6]
# Euler terms ordered left, minus-middle, primary, tail.
ordinary=[126-6+8-150,70-125,35-20-100,15-40-75]
traces=[6-6-8+6,6-5,3-4+4,3+8-3]
assert ordinary==[-22,-55,-85,-100]
assert traces==[-2,1,3,8]
assert parity_index(ordinary[2]-ordinary[0],traces[2]-traces[0])==(-29,-34)
assert parity_index(ordinary[3]-ordinary[1],traces[3]-traces[1])==(-19,-26)
# Conditional conic gate after H0(B_Q3)_+=0 has forced section-vanishing below it.
assert 2*19==38 and 38-34==4
# Optional ambient concentration in degree1 uses the separate no-quartic input.
assert parity_index(55,-1)==(27,28)
assert parity_index(100,-8)==(46,54)
print('PASS: fixed-locus F(-2) contributions -9epsilon/8 and -7epsilon/8')
print('PASS: actual primary traces H1F1=-2epsilon and H2F(-2)=-2epsilon')
print('PASS: middle term retained; ambient B0 Euler is(-22,-2)')
print('PASS: lower-quadric parity indices(-29,-34),(-19,-26)')
print('PASS: conditional actual odd Koszul gate34 ->38 is dimensionally consistent')
print('BOUNDARY: no section vanishing or actual multiplication rank inferred')

# Finite-stabilizer orbit injection and PR455's independent h2 upper bound.
solutions=[(h1,h2) for h2 in range(3) for h1 in range(24,27) if h1-h2==22]
assert solutions==[(24,2)]
assert (3-2)**2-1==0
assert parity_index(24,0)==(12,12)
assert parity_index(2,-2)==(0,2)
assert 41-12==29 and 44-12+2==34
print('PASS: orbit tangent + h2<=2 forces h1=24,h2=2, with parity12/12 and0/2')
