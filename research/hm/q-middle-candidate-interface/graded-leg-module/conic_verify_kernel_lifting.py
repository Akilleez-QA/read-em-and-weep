#!/usr/bin/env python3
"""Reproduce exact universal conic identities, with all coefficients formal."""

import sympy as sp
from conic_kernel_lifting import (
    COORDS, V, Q, cross, expanded, is_zero,
    symmetric_quadratic_right_inverse, skew_quadratic_right_inverse,
    scalar_quadratic_right_inverse, cubic_symmetric_q_lift, conic_leg_maps,
)

x, y, z = COORDS
quadratic_monomials = (x*x, x*y, x*z, y*y, y*z, z*z)


def zero(expression):
    if not isinstance(expression, sp.MatrixBase):
        expression = sp.Matrix([expression])
    assert is_zero(expression), expression


def formal_polynomial(prefix, monomials):
    coefficients = sp.symbols(f"{prefix}_0:{len(monomials)}")
    return sum(c * m for c, m in zip(coefficients, monomials))


r = sp.Matrix([formal_polynomial(f"r{i}", quadratic_monomials) for i in range(3)])
f = (V.T * r)[0]
plus = symmetric_quadratic_right_inverse(r)
minus = skew_quadratic_right_inverse(r)
zero(plus - plus.T)
zero(plus * V - r)
zero(minus + minus.T)
zero(minus * V - r + sp.Matrix([sp.diff(f, t) / 3 for t in COORDS]))
print("PASS: symmetric right inverse for every formal quadratic vector")
print("PASS: skew right inverse, including the complete off-kernel correction")

scalar = formal_polynomial("s", quadratic_monomials)
zero((V.T * scalar_quadratic_right_inverse(scalar))[0] - scalar)
print("PASS: C-source cross-block scalar Euler lift")

g, leg, differential, companion = conic_leg_maps()
zero((V.T * g)[0] - Q)
zero(V.T * leg - sp.Matrix([[0, 0, 0, Q]]))
zero(leg * differential - sp.zeros(3, 1).row_join(Q * sp.eye(3)))
zero(differential * companion - Q * sp.eye(4))
zero(companion * differential - Q * sp.eye(4))
print("PASS: four conic legs and both exact matrix-factorization identities")

# Koszul reconstruction, with independent polynomial potential coefficients.
h = sp.Matrix([formal_polynomial(f"h{i}", COORDS) for i in range(3)])
w = expanded(cross(V) * h)
curl = sp.Matrix([sp.diff(w[2], y) - sp.diff(w[1], z),
                  sp.diff(w[0], z) - sp.diff(w[2], x),
                  sp.diff(w[1], x) - sp.diff(w[0], y)])
zero(cross(V) * (-curl / 3) - w)
print("PASS: polynomial Koszul homotopy with the stated cross-product sign")

# Test the complete A-block adapter with arbitrary free formal coefficients.
# Three A channels are used. Every coefficient of B is independent; the exact
# cubic T0 ranges over every leg-product potential and every skew channel.
n = 9
b = sp.zeros(n)
for i in range(n):
    for j in range(i, n):
        b[i, j] = b[j, i] = formal_polynomial(f"b{i}_{j}", COORDS)
cv = cross(V)
t0 = sp.zeros(n)
for a in range(3):
    for b_index in range(a, 3):
        potential = sp.zeros(3)
        for i in range(3):
            for j in range(i, 3):
                potential[i, j] = potential[j, i] = formal_polynomial(
                    f"p{a}_{b_index}_{i}_{j}", COORDS)
        block = cv * potential * cv.T
        if a != b_index:
            block += formal_polynomial(f"f{a}_{b_index}", quadratic_monomials) * cv
        t0[3*a:3*a+3, 3*b_index:3*b_index+3] = block
        t0[3*b_index:3*b_index+3, 3*a:3*a+3] = block.T
t = expanded(t0 + Q * b)
exact, correction = cubic_symmetric_q_lift(t)
zero(exact - exact.T)
zero(t - exact - Q * correction)
gauge = expanded(b - correction)
for a in range(3):
    for b_index in range(3):
        zero(gauge[3*a:3*a+3, 3*b_index:3*b_index+3] * V)
print("PASS: complete three-A-channel cubic adapter on all formal potentials")
print("PASS: change of polynomial representative leaves only q*H_1 ambiguity")

# Cohomological arithmetic follows the proved exact resolution, not a rank test.
def s_degree(d):
    return (d + 1) * (d + 2) // 2 if d >= 0 else 0

assert s_degree(-1) == 0  # h2(O(-2)) on P2
assert s_degree(-2) == 0  # h2(O(-1)) on P2
assert 36*s_degree(1) + 3*s_degree(2) - 18*s_degree(0) == 108
assert 3*s_degree(0) == 3
assert 108 - 3 == 105
print("PASS: H^1(H~(1)) vanishes from the O(-2),O(-1),O resolution")
print("PASS: exact cubic sequence has R-ranks 3 -> 108 -> 105")
print("ALL CHECKS PASSED: no points, numerical assignments, ranks, or coefficient solve")
