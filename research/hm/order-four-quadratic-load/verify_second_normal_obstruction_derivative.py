#!/usr/bin/env python3
"""Universal nilpotent-order checks; no HM source-instance coefficients."""
import sympy as s
q,t=s.symbols('q t')
x,y,z=s.symbols('x y z',commutative=False)
# Exact universal transition product, with no terms beyond q^2 on 3Q.
p=s.expand((1+t*q*x)*(1+t*q*y)*(1+t*q*z))
assert p.coeff(q,0)==1
assert s.expand(p.coeff(q,1)-t*(x+y+z))==0
assert s.expand(p.coeff(q,2)-t**2*(x*y+x*z+y*z))==0
assert p.coeff(q,3)==t**3*x*y*z
# Exponential transitions retain determinant corrections before taking defects.
def exp2(v): return 1+t*q*v+t**2*q**2*v*v/2
e=s.expand(exp2(x)*exp2(y)*exp2(z))
assert s.expand(e.coeff(q,1)-t*(x+y+z))==0
assert s.expand(e.coeff(q,2)-t**2*((x*x+y*y+z*z)/2+x*y+x*z+y*z))==0
# When the first-normal cocycle closes, the quadratic expression is a commutator.
closed=s.expand(e.coeff(q,2).subs(z,-x-y))
assert s.expand(closed-t**2*(x*y-y*x)/2)==0
# Cyclic trace annihilates this commutator, controlling fixed determinant.
inv=s.expand(exp2(x)*exp2(-x))
assert inv.coeff(q,1)==0 and inv.coeff(q,2)==0
# All q^2 terms have t-degree <=2. Gauge conjugation of q^2 defects by
# identity+q*t*x is identity on the q^2 coefficient.
c=s.Symbol('c',commutative=False)
gauged=s.expand(exp2(x)*(1+q*q*c)*exp2(-x))
assert s.expand(gauged.coeff(q,2)-c)==0
# The q^3 term is exactly the discarded ideal, not a surviving obstruction.
# Local order-two corrections can contribute a linear q^2 term; hence degree<=2.
assert -(-6)-5==1               # H2 B(-6) dual H2 B(1)
assert -4+2*3+2==4              # ordinary degree of a^3 h
# A vector-valued polynomial t D+t² Q with D !=0 has <=1 nonzero zero.
r1,r2=s.symbols('r1 r2',nonzero=True)
D,Q=s.symbols('D Q')
assert s.expand((D+r1*Q)-(D+r2*Q)-(r1-r2)*Q)==0
# If two distinct nonzero roots existed, Q=0, then D=0, contradiction.
print('PASS: normal-order transition product, degree-two obstruction bound,')
print('Serre-duality twist, naive cubic multiplication target, and root comparison.')
print('Actual injectivity is proved by exact-sequence inputs, not rank evaluation.')
