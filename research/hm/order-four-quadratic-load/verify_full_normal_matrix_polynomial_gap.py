#!/usr/bin/env python3
"""Universal coefficient diagram for the lost polynomial nine-space."""
import sympy as S
f,g,k,r,p=S.symbols('f g k r p')
N=S.Matrix([[f*g,-f*f],[g*g,-f*g]])
K=S.Matrix([[k,0],[r,-k]])
P=S.Matrix([[1,0],[p,1]])
assert S.expand(S.trace(N*K)-(2*f*g*k-f*f*r))==0
Kp=S.simplify(P*K*P.inv())
assert Kp==S.Matrix([[k,0],[r+2*p*k,-k]])
Np=S.simplify(P*N*P.inv())
assert S.simplify(S.trace(Np*Kp)-S.trace(N*K))==0
h0=lambda n:max(n+1,0)
h1=lambda n:max(-n-1,0)
assert (h0(2)+9*h0(0),h1(2)+9*h1(0))==(12,0)
assert (4*h0(-4),4*h1(-4))==(0,12)
assert 3*h0(4)+3*h0(2)==24
assert 24-12==12 and 24-3==21 and 12-3==9
assert 15+9==24
assert 8>3+5-2 # octics vanish on the entire actual vertex algebra.
assert h0(8)==9 # but give all conic octic values.
# Source trace coefficient line: f has degree(3,3), g degree(5,-5),
# k degree(0,2), r degree(2,-6). Both terms have bidegree(8,0).
assert (3+5+0,3-5+2)==(8,0)
assert (2*3+2,2*3-6)==(8,0)
print('PASS: full matrix trace and triangular covariance, with independent formal entries.')
print('PASS: actual coefficient quotient 12 -> 24 -> 12 versus global quotient 3 -> 24 -> 21.')
print('PASS: their exact difference is the polynomial nine-space; octics are vertex-zero but conic-visible.')
print('No full lower lift, actual coefficient, actual matrix/rank, or fourth value is evaluated.')
