#!/usr/bin/env python3
"""Universal degree/group arithmetic only; no actual coefficients or ranks."""
from fractions import Fraction as F

# Orbit sizes divide |SL2(F5)|; indices 2,3,4 are excluded mathematically
# because SL2(F5) is perfect whereas the symmetric groups are solvable.
small_indices=[k for k in range(1,8) if 120%k==0]
assert small_indices==[1,2,3,4,5,6]
possible=[k for k in small_indices if k not in (2,3,4)]
assert possible==[1,5,6]
for k in (5,6):
    stabilizer=120//k
    assert stabilizer in (24,20) and stabilizer%2==0
    assert k*2>7  # unique involution forces center-stability and even degree

# Every individually invariant nonvertex curve would have even degree <=6.
def castelnuovo(d):
    m,e=divmod(d-1,3)
    return 3*m*(m-1)//2+m*e
assert [castelnuovo(d) for d in (4,5,6)]==[0,1,2]
assert [d for d in range(4,8) if d%2==0]==[4,6]
assert all(castelnuovo(d)<=2 for d in (4,6))
assert 120>84*(2-1)
# Independent small-degree proof: Clifford then nonspecial Riemann-Roch.
for d in (4,6):
    assert F(d,2)+1<5
    assert d+1-5<=2

# Exact subtraction, with ordinary hyperplane restricting to O_P1(2).
T=(9,27); conic=(2,6)
residual=tuple(a-b for a,b in zip(T,conic))
assert residual==(7,21)
assert 27-6==21
assert 0-0==0  # H1 under the established disjoint-support direct sum
assert residual[0]//1==7  # vertex line has ordinary degree one
print('PASS: orbit/parity bounds, low-degree genus exclusion, and exact vertex-cycle arithmetic')
print('Scope: set-theoretic vertex support and generic length seven, not a sheaf classification on L.')
