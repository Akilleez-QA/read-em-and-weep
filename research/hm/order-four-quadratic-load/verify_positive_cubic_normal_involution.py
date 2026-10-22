#!/usr/bin/env python3
"""Universal character/sign identities; no actual-instance evaluation."""
import sympy as s
mu_exponent=6-s.Rational(8,2)
assert mu_exponent==2
intrinsic_square=-1
adjoint_comparison=-1
P=intrinsic_square*adjoint_comparison
A=-1; D5=1; Atiyah=1
probe=A*Atiyah
assert P==1 and probe==-1
assert A*D5*probe==P
x,b,v0,v1=s.symbols('x b v0 v1')
J=b-x
assert s.expand(b-J)==x
reflection_difference=s.expand((v0+x*v1)-(v0+J*v1))
assert s.diff(reflection_difference,x)==2*v1
assert s.solve(s.Eq(s.diff(reflection_difference,x),0),v1)==[0]
print('PASS: target +1, actual fixed probe -1, two input signs cancel.')
print('PASS: affine reflection invariance forces zero linear variation.')
print('Absolute cubic value is not selected by these identities.')
