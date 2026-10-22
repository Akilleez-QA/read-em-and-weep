#!/usr/bin/env python3
"""Universal torus/gauge character identities, never actual monad values."""
import sympy as s
# Weight order: lambda, mu, Wprime source gauge, A source gauge.
a=s.Matrix([3,0,1,0]); b=s.Matrix([1,2,1,0]); c=s.Matrix([2,1,0,1])
Delta=s.Matrix([3,2,0,0]); Rq=s.Matrix([2,0,0,0])
# Transport weights, not scalar function weights.
beta=-2*Delta+s.Matrix([0,0,-2,0]); eta=beta+Rq
coefficient=beta-2*eta
assert coefficient==s.Matrix([2,4,2,0])
x,y,z=s.symbols('x y z')
sol=s.solve(list(x*a+y*b+z*c-coefficient),(x,y,z),dict=True)
assert sol==[{x:0,y:2,z:0}]
assert coefficient==2*b
# Scalar coordinate change agrees with the common source gauge t^3.
assert coefficient[0]+coefficient[1]==3*(coefficient[2]+coefficient[3])
print('PASS: all determinant/equation/source weights match; sole monomial is b^2.')
print('The universal constant kappa, including whether it is zero, is NOT evaluated.')
