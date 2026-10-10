#!/usr/bin/env python3
"""Exact checks for the embedded primitive-triple obstruction.

Run with Python 3 and SymPy (tested with SymPy 1.14.0):
    python check_obstruction.py

This verifies identities and examples. The geometric nonexistence proof is in
primitive_triple_obstruction.md; finite examples are not a substitute for it.
"""

from itertools import product

import sympy as sp


def check_zero(expression, label):
    assert sp.cancel(sp.expand(expression)) == 0, label
    print(f"PASS: {label}")


s, t, h, y0, y1 = sp.symbols("s t h y0 y1")
a, b, c, d, e, f = coefficients = sp.symbols("a b c d e f")
p = a + b * t + c * t**2
q = d + e * t + f * t**2
relation = p * y1 - q * y0
wronskian = sp.expand(p * sp.diff(q, t) - q * sp.diff(p, t))
R = sp.expand((q - t * p) * wronskian)

# Start from the actual rational coordinate change, with h recording normal
# degree. Compare its first two coefficients with the claimed Taylor formula.
t_prime = (s * t + h * y1) / (s + h * y0)
z0 = -h * y0 / (s * (s + h * y0))
z1 = -h * y1 / (s * (s + h * y0))
relation_prime = p.subs(t, t_prime) * z1 - q.subs(t, t_prime) * z0
linear = sp.diff(relation_prime, h).subs(h, 0)
quadratic = sp.diff(relation_prime, h, 2).subs(h, 0) / 2
expected_quadratic = (
    y0 * relation
    - (y1 - t * y0) * (sp.diff(p, t) * y1 - sp.diff(q, t) * y0)
) / s**3
check_zero(linear + relation / s**2, "linear coordinate transition")
check_zero(quadratic - expected_quadratic, "quadratic coordinate transition")

# In I^2/(I J), y_i y_j maps to F_i F_j epsilon^2.
image_quadratic = quadratic.subs({y0: p, y1: q}, simultaneous=True)
check_zero(image_quadratic - R / s**3, "quadratic quotient gives R/s^3")
square_transition = sp.diff(z0**2, h, 2).subs(h, 0) / 2
check_zero(square_transition - y0**2 / s**4, "square-line transition s^-4")

# Homogeneous form and the degree-five bound.
x0, x1 = sp.symbols("x0 x1")
F0 = a * x0**2 + b * x0 * x1 + c * x1**2
F1 = d * x0**2 + e * x0 * x1 + f * x1**2
jacobian = sp.det(sp.Matrix([
    [sp.diff(F0, x0), sp.diff(F0, x1)],
    [sp.diff(F1, x0), sp.diff(F1, x1)],
]))
R_hom = sp.expand((x0 * F1 - x1 * F0) * jacobian / 2)
check_zero(R_hom.subs({x0: 1, x1: t}) - R,
           "homogeneous quintic identity in characteristic zero")
assert sp.Poly(R, t).degree() <= 5
assert sp.Poly(R_hom, x0, x1).is_homogeneous
print("PASS: homogeneous degree 5")


def homogeneous_resultant(values):
    aa, bb, cc, dd, ee, ff = values
    return sp.det(sp.Matrix([
        [cc, bb, aa, 0], [0, cc, bb, aa],
        [ff, ee, dd, 0], [0, ff, ee, dd],
    ]))


def example(name, values, expected_zero, expected_basepoint_free,
            modulus=None):
    substitutions = dict(zip(coefficients, values))
    value = sp.expand(R.subs(substitutions))
    determinant = homogeneous_resultant(values)
    if modulus is not None:
        value = sp.Poly(value, t, modulus=modulus).as_expr()
        determinant = int(determinant) % modulus
    is_zero = value == 0
    basepoint_free = determinant != 0
    assert is_zero == expected_zero, name
    assert basepoint_free == expected_basepoint_free, name
    field = "Q" if modulus is None else f"F_{modulus}"
    print(f"PASS: {name} over {field}: R={sp.factor(value)}, "
          f"basepoint-free={basepoint_free}")


example("valid pair (x0^2,x1^2)", (1, 0, 0, 0, 0, 1), False, True)
example("radial pair with common factor x0", (1, 0, 0, 0, 1, 0), True, False)
example("constant-map pair with common factor x0^2",
        (1, 0, 0, 1, 0, 0), True, False)
example("common factor need not kill R", (1, 0, 0, 1, 1, 0), False, False)
example("inseparable quadratic pair", (1, 0, 0, 0, 0, 1), True, True, 2)
example("separable characteristic-two pair", (1, 0, 0, 0, 1, 1),
        False, True, 2)

# A useful characteristic-two warning: the homogeneous Jacobian vanishes for
# the last separable example too, so division by 2 cannot be suppressed.
char2_values = dict(zip(coefficients, (1, 0, 0, 0, 1, 1)))
assert sp.Poly(jacobian.subs(char2_values), x0, x1, modulus=2).is_zero
assert not sp.Poly(R.subs(char2_values), t, modulus=2).is_zero
print("PASS: characteristic-two Jacobian formula cannot replace affine R")

# Exhaustive small-coefficient regression test; the theorem itself is proved
# by factorization and separability, not by this finite enumeration.
R_coefficients = sp.Poly(R, t).all_coeffs()
resultant_polynomial = homogeneous_resultant(coefficients)
resultant_eval = sp.lambdify(coefficients, resultant_polynomial, "sympy")
R_eval = sp.lambdify(coefficients, R_coefficients, "sympy")
valid_count = 0
for values in product((-1, 0, 1), repeat=6):
    if resultant_eval(*values) != 0:
        valid_count += 1
        assert any(value != 0 for value in R_eval(*values)), values
print(f"PASS: all {valid_count} basepoint-free pairs among 729 "
      "small-coefficient pairs have R != 0")

# The scalar Cech obstruction cannot be removed by regular lift changes.
# With e'_infinity=e_infinity+B(1/s) epsilon_infinity^2 and
# e'_0=e_0+A(s) epsilon_0^2, splitting would give
#     s R + B(1/s) + s^2 A(s) = 0.
# The second and third terms have no s^1 coefficient.
for degree in range(9):
    A = sum(sp.Symbol(f"A{i}") * s**i for i in range(degree + 1))
    B = sum(sp.Symbol(f"B{i}") * s**(-i) for i in range(degree + 1))
    assert sp.expand(B + s**2 * A).coeff(s, 1) == 0
print("PASS: Cech Laurent-degree obstruction (degrees 0 through 8 checked)")
print("All exact symbolic checks passed. Characteristic-two examples are "
      "tests of this obstruction only, not existence claims.")
