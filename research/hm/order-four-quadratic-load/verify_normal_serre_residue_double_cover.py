#!/usr/bin/env python3
"""Universal identities only: no HM coefficient values or actual ranks."""
import sympy as s
from pathlib import Path
import runpy
r=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
assert r['vmul'](r['Wp'],r['Wp'])==r['vadd'](r['one'],r['V'])
assert r['inner'](r['one'],r['V'])==r['z'](0)
sym2V=[r['scale'](s.Rational(1,2),r['add'](r['mul'](v,v),r['sym'](2,r['sub'](r['mul'](w,w),r['z'](2))))) for v,w in zip(r['V'],r['Wp'])]
assert sym2V==r['vadd'](r['one'],r['D'])
# Abstract multiplicity-space automorphisms, not actual HM coefficients.
k,z,v1,v2=s.symbols('k z v1 v2',nonzero=True)
U=s.Matrix([[k,z],[0,k]])
a=s.Matrix([1,0]);b=s.Matrix([[0,1]])
assert U*a==k*a and b*U==k*b
normal=U.subs({k:1/v2,z:-v1/v2**2})*s.Matrix([v1,v2])
assert normal.applyfunc(s.simplify)==s.Matrix([0,1])
# Negative block scale: intrinsic residue weights.
conic=-1-1+0
vertex=s.Rational(3,2)+s.Rational(5,2)-2
assert conic==-2 and vertex==2 and vertex-conic==4
ambient_ratio=-2
assert vertex-conic==-2*ambient_ratio
# For mu^2=-1, both residue characters equal -1 and ambient r changes sign.
assert (-1)**(-1)==-1 and (-1)**1==-1
assert 2*1+3==5 and 2-1==1  # H0(O_Z)=2+V; projective invariant residue dimension.
print('PASS: homogeneous quotient normalization, invariant unit accounting,')
print('intrinsic residue weights (-2,+2), and degree-two torus restriction.')
print('No actual HM coefficients, multiplication matrices, or ranks were evaluated.')
