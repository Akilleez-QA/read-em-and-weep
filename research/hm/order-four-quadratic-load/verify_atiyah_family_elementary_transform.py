#!/usr/bin/env python3
"""Universal representation and Chern arithmetic, not actual-map testing."""
import runpy
import sympy as s
r=runpy.run_path('verify_negative_vertex_scalar.py')
assert r['inner'](r['V'],r['V'])==r['z'](1)
assert r['inner'](r['V'],r['A'])==r['z'](0)
assert r['vmul'](r['V'],r['A'])==r['vadd'](r['P'],r['D'])
H,n=s.symbols('H n')
exp=lambda d:1+d*H+s.Rational(d*d,2)*H**2
inner=s.expand(3*(3-exp(1))-5*exp(-1))
assert inner==1+2*H-4*H**2
assert s.expand(exp(2)-inner)==6*H**2
outer=s.expand(9-5*exp(-1))
assert s.expand(inner+3*exp(1))==outer
assert outer==4+5*H-s.Rational(5,2)*H**2
assert (s.Integer(5)**2-2*outer.coeff(H,2))/2==15
chi=lambda d:s.expand((d+2)*(d+1)/2)
assert s.expand(chi(n)-4*chi(n-3)+3*chi(n-4))==6
# Cohomology values of the indicated line bundles on P².
h0=lambda d:(d+2)*(d+1)//2 if d>=0 else 0
h2=lambda d:h0(-d-3)
assert h2(-3)==1 and h2(-2)==0
assert h0(-2)==h0(-1)==0
print('PASS: six-point defect length, rank-four Chern classes, unique nonzero Ext channel, and unique equivariant double-dual splitting.')
print('No actual coefficients, map matrices, ranks, or parameter scans were evaluated.')
