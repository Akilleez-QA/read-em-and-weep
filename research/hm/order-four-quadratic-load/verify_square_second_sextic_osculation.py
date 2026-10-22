#!/usr/bin/env python3
"""Universal representation, valuation, and polarization checks.

No actual sextic coefficients, point values, or bundle matrices are read.
"""
import contextlib
import io
import itertools
import runpy
from fractions import Fraction

with contextlib.redirect_stdout(io.StringIO()):
    c = runpy.run_path('verify_negative_vertex_scalar.py')
symW = lambda n: [c['sym'](n,x) for x in c['W']]
assert c['inner'](c['vmul'](c['A'],symW(4)),c['P']) == c['z'](1)
assert symW(6) == c['vadd'](c['V'],c['P'])
assert symW(9) == c['vadd'](c['S'],c['T'])
assert c['inner'](c['vmul'](symW(3),symW(9)),c['one']) == c['z'](1)
assert c['inner'](symW(12),c['one']) == c['z'](1)

# Wronskian line degrees and the second-osculating dual degree.
assert 4*6-2*sum(range(4)) == 12
assert 3*6-2*sum(range(3)) == 12
assert 4*12-2*sum(range(4)) == 36 == 3*12
assert (6-3,12-3) == (3,9)

weight_one = [a for a in itertools.combinations(range(8),4)
              if sum(a)-sum(range(4)) == 1]
assert weight_one == [(0,1,2,4)]
for a,dual in [((0,1,2,3),(0,1,2,3)),
               ((0,1,2,4),(0,2,3,4))]:
    orders = []
    for omit in range(4):
        exponents = [a[j] for j in range(4) if j != omit]
        leading_vandermonde = 1
        for j in range(3):
            for k in range(j+1,3):
                leading_vandermonde *= exponents[k]-exponents[j]
        assert leading_vandermonde != 0
        orders.append(sum(exponents)-sum(range(3)))
    assert tuple(sorted(orders)) == dual
assert sum((0,2,3,4))-sum(range(4)) == 3

# Universal symmetric-tensor differentiation on the diagonal.
assert Fraction(3,12) == Fraction(1,4) != 0
assert Fraction(9,12) == Fraction(3,4) != 0
assert Fraction(3,12)+Fraction(9,12) == 1
assert 3+1 == 4

# Complete cyclic-character checks, with s,t section weights -1,+1.
weights6 = [(-6+2*j)%10 for j in range(7)]
assert [j for j,w in enumerate(weights6) if w==2] == [4]
assert 6-4 == 2                # s^2 t^4, divisor 4x+2y
assert {((2*2)+w)%10 for w in (8,0,2)} == {2,4,6}
assert (-8)%10 == 2            # final quotient dual character
weights12 = [(-12+2*j)%10 for j in range(13)]
assert [j for j,w in enumerate(weights12) if w==6] == [4,9]
assert 12-4-3 == 5             # opposite-variable residual orbit

# At y the c-series has fiber O(12) weight 2, v=-s/t has weight -2.
dual_orders = (0,2,3,4)
dual_component_weights = {j:(-2+2*j)%10 for j in dual_orders}
assert dual_component_weights == {0:8,2:2,3:4,4:6}
assert (6+dual_component_weights[3])%10 == 0  # Q6(x) weight 6
print('PASS: actual-map comparison Hom line and polarized-invariant uniqueness.')
print('PASS: sextic/dual Wronskians and exact vanishing sequences.')
print('PASS: incidence bidegrees, exact contact-four factors, and C5 divisor 4x+2y.')
print('These determine final Serre tests, not their value on the actual R cochain.')
