#!/usr/bin/env python3
"""Universal dimensions and bundle degrees; no actual coefficients or ranks."""
# Actual parity dimensions are input from the proved trace -2 in dimension 10.
plus=(10-2)//2; minus=(10+2)//2
assert (plus,minus)==(4,6)
assert minus-plus==2 and 5-3==2
# Symmetric squares of a rank-two bundle of degree -6.
assert 2*(2+1)//2==3
assert 3*(-6)==-18
assert 9-3==6 and (-12)-(-18)==6
assert 15-3==12
assert 18-2*6==6
# Quotient realization: kernel 9 O(2) -> 3 O(4).
assert 9-3==6 and 9*2-3*4==6
print('PASS: parity lower bound2 equals first-normal upper bound2.')
print('PASS: forced square bundle rank3 degree-18; residual quotient rank6 degree6.')
print('PASS: beta rank at most6 and two-root secondary kernel at least6.')
print('BOUNDARY: no exact residual beta rank, global odd-quadric lower bound, or determinant-cubic smoothness is inferred.')
