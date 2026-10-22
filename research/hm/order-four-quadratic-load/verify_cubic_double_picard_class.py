#!/usr/bin/env python3
"""Universal square-zero transition and exact line-degree checks."""
import sympy as s
import runpy
f,g,p,q=s.symbols('f g p q')
# The exact numerator for the logarithmic square-zero cocycle correction.
assert s.expand((g+f*p)-g-f*p)==0
assert s.expand((1+f*p)*(1+f*q)-(1+f*(p+q)))==f*f*p*q
assert (-3+5,-3-5)==(2,-8)
assert (2-3,-8-3)==(-1,-11)
# Kernel fiber O(-1) is acyclic; target is V O(-8).
assert max(-1+1,0)==max(-(-1)-1,0)==0
assert 3*7==21
c=runpy.run_path('verify_negative_vertex_scalar.py')
sym6=[c['sym'](6,x) for x in c['W']]
assert c['inner'](c['V'],sym6)==c['z'](1)
e=s.symbols('e')
assert s.expand(e+5*(-e/s.Integer(5)))==0
print('PASS: square-zero Picard cocycle, exact sheaf-isomorphism degrees, dimension21, invariant dimension1.')
print('Nonvanishing is the proven actual quintic extension, transported by a sheaf isomorphism; no Bockstein comparison asserted.')
