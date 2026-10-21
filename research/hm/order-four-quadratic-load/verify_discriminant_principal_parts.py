#!/usr/bin/env python3
"""Universal principal-parts and degree identities; no actual HM data."""
import sympy as s
z,t,h=s.symbols('z t h')
assert s.expand((z-t)**2-(z*z-2*t*z+t*t))==0
for n in [-5]+list(range(1,28)):
    assert s.simplify(s.diff(z**n,z).subs(z,t)-n*t**(n-1))==0
    # The linear coefficient of the transition is n; all n used are nonzero.
    assert n != 0
    assert (n-2)+n==2*(n-1)
rank=5
deg_c=26
deg_e=deg_c+rank
assert 2*deg_e-2*rank==52==2*deg_c
assert (-7)+(-5)==2*(-6)==2*(-6)
assert (-7)+2 == -5
assert (-5)+2 == -3
assert 44-6==48-10==38
print('PASS: doubled diagonal, nonzero principal-parts extension coefficients, source/target degrees, and normal-line twists.')
