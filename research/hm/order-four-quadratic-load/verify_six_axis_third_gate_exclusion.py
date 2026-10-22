#!/usr/bin/env python3
"""Representation weights and geometric counts; no actual map evaluations."""
from math import comb
A={8,0,2}; P={2,4,6,8}
assert A&P=={2,8}
assert P-(A&P)=={4,6}
assert {2,8}.isdisjoint({4,6})
assert 6*comb(3+1,2)==36>24
assert comb(6,2)//comb(3,2)==5
# A4 has three characters of degree one; the order-three character
# values do not matter because the restricted 3-character is zero there.
assert 3+3*(-1)+8*0==0
assert 5*3>2*7
assert 6*2>7
assert 9-2==7
print('PASS: axis rank alternatives, first-jet weight exclusion, and length contradiction.')
print('PASS: six-point line count, A4 obstruction, and six-conic septic exclusion.')
print('Actual cochain fiber vanishing is a separate hypothesis, not tested here.')
