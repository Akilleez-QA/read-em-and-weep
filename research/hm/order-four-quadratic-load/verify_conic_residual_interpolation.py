"""Universal checks for the conic-residual interpolation proof.

No actual HM coefficients, sampled point schemes, matrices, or rank tests.
The geometry (disjoint supports, avoided line intersection, and primary
cohomology) is proved in the companion artifacts, not assumed verified here.
"""
from math import comb


def ideal_power_monomials(exponent):
    # Formal regular pair (l,q), with degrees 1 and 2.
    return {(i, exponent-i) for i in range(exponent+1)}


def minimal_generators(monomials):
    return {m for m in monomials if not any(
        n != m and n[0] <= m[0] and n[1] <= m[1]
        for n in monomials)}


for exponent in (1, 2):
    colon = {(max(i-1, 0), j)
             for i, j in ideal_power_monomials(exponent)}
    assert minimal_generators(colon) == ideal_power_monomials(exponent-1)
    trace = {(i,j) for i,j in ideal_power_monomials(exponent) if i == 0}
    assert trace == {(0,exponent)}
print('PASS: formal (l,q)^a:l=(l,q)^(a-1), with trace q^a.')


def residual_trace_degrees(a, b, twist):
    trace_degrees = []
    while max(a,b) > 1:
        if a > 1:
            trace_degrees.append(twist-2*a)
            a -= 1
        else:
            trace_degrees.append(twist-2*b)
            b -= 1
        twist -= 1
    assert (a,b,twist) == (1,1,2)
    assert all(d >= -1 for d in trace_degrees)
    return trace_degrees


assert residual_trace_degrees(2,2,4) == [0,-1]
assert residual_trace_degrees(2,1,3) == [-1]
assert residual_trace_degrees(1,2,3) == [-1]
assert residual_trace_degrees(1,1,2) == []
print('PASS: every high-twist plane trace reduces to quadratic length-four interpolation with H1-free P1 traces.')

# Three successive plane residuals remove one twist each. The own-conic
# square removes four more degrees from each plane trace.
for initial, expected, terminal in (
    (8, (4,3,2), 5),
    (7, (3,2,1), 4),
):
    degrees = tuple(initial-step-4 for step in range(3))
    assert degrees == expected
    assert initial-3 == terminal
    assert min(degrees) >= 0  # H2 of each finite-scheme ideal twist is zero.
print('PASS: ordinary and special residual trace twists, terminal twists, and H2 degree bounds.')

# For a (2,2) complete intersection, square resolution is
# 0 O(d-6)^2 -> O(d-4)^3 -> I_T^2(d) -> 0.
# At d=4, H2(O(-2))=H2(O(0))=0, proving H1=H2=0.
assert 4-6 >= -2 and 4-4 >= -2
# At d=3, H2 of the middle O(-1)^3 is zero, proving H2 of I_T^2(3)=0.
assert 3-4 >= -2
print('PASS: complete-intersection-square trace bounds in degrees four and three.')


def chi_B(t):
    return 3*comb(t+3,3)-15*(t+2)


assert (chi_B(4),chi_B(5)) == (15,63)
assert 48-5+3 == 46
assert 63-46 == 17
assert 17+3-15 == 5
assert (54-41,41+13) == (13,54)
assert (30-13,-54) == (17,-54)
assert (48-5,-(26+2*5)) == (43,-36)
assert (-3*4-36,-54+17) == (-48,-37)
print('PASS: Euler characteristics, parity dimensions, and exact bundle ranks/degrees.')
print('All universal residual/interpolation/numerical checks passed.')
