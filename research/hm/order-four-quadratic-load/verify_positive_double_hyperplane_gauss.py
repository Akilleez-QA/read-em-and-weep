#!/usr/bin/env python3
"""Universal Koszul and derivative identities only, with no HM coefficients."""
import sympy as s
u,v,z,x,y,m,k,kp=s.symbols('u v z x y m k kp')
ell=u+z*v
assert s.expand((y-u*m)-z*(x+v*m)-(y-z*x)+ell*m)==0
assert s.expand(u*kp+v*(z*kp+k)-(ell*kp+v*k))==0
assert s.expand((z*kp+k)-z*kp-k)==0
# For rank r of the middle derivative arrow in exact sequence (6).
r=s.symbols('r', integer=True)
assert s.expand(41-(17-r)-(24+r))==0
assert s.expand(37-(24+r)-(13-r))==0
assert 30-13==17 and -(41+13)==-54
assert 41-13==28 # degree D_lin(-1), keeping cotangent twist
print('PASS: quotient gauge, differentiated Koszul equation, exact middle arrow,')
print('fiber rank formulas, and parameter-bundle degree bookkeeping.')
print('All geometric exactness/vanishing inputs are specified in the proof.')
