#!/usr/bin/env python3
"""Universal integer checks for the conditional square third-gate theorem.

This verifier uses only the degree and dimension of a linear series and the
weights of Sym^4 of a two-dimensional representation. It contains no actual
HM/source coefficients, actual maps or matrices, point evaluations, rank tests,
or family-parameter scans. The proof supplies the geometric inputs; passing
these checks does not determine the actual square value or finish the repair.
"""

from collections import Counter
from itertools import combinations, product


def vanishing_sequences(weight):
    """All basepoint-free, strictly increasing 5-tuples of this weight."""
    return [
        a
        for a in combinations(range(5 + weight), 5)
        if a[0] == 0 and sum(a) - sum(range(5)) == weight
    ]


def stabilizer_compatible(sequence, order):
    """Compare exact binary-lift exponents, with no roots of unity needed.

    A binary lift has eigenvalues lambda, lambda^-1, with lambda^(2m)=1.
    Sym^4 has weights 4, 2, 0, -2, -4. In a compatible affine convention,
    the order-r term of an O(18) section has weight 2r-18. Reversing the
    generator changes both signs and does not change this comparison.
    """
    modulus = 2 * order
    source = Counter(w % modulus for w in (4, 2, 0, -2, -4))
    orders = Counter((2 * r - 18) % modulus for r in sequence)
    return source == orders


# Quadratic Veronese pullback: D5 O(-3) -> O(6) becomes
# D5 O(-6) -> O(12), or D5 O -> O(18).
degree = 2 * (6 + 3)
dimension = 5
wronskian_degree = dimension * degree - 2 * sum(range(dimension))
assert degree == 18
assert wronskian_degree == 70

# The only orbit lengths of the projective A5 action are 12, 20, 30, 60.
# This finite arithmetic enumeration is not a scan of geometric directions.
orbit_sizes = (12, 20, 30, 60)
partitions = [
    multiplicities
    for multiplicities in product(
        *(range(wronskian_degree // size + 1) for size in orbit_sizes)
    )
    if sum(s * n for s, n in zip(orbit_sizes, multiplicities))
    == wronskian_degree
]
assert partitions == [(0, 2, 1, 0)]
assert 2 * 20 + 30 == 70

ordinary = (0, 1, 2, 3, 4)
order_two = (0, 1, 2, 3, 5)
order_three = (0, 1, 2, 4, 5)
assert vanishing_sequences(0) == [ordinary]
assert vanishing_sequences(1) == [order_two]
assert vanishing_sequences(2) == [
    (0, 1, 2, 3, 6),
    order_three,
]
assert [a for a in vanishing_sequences(2) if stabilizer_compatible(a, 3)] == [
    order_three
]
assert stabilizer_compatible(order_two, 2)
assert stabilizer_compatible(order_three, 3)
assert stabilizer_compatible(ordinary, 5)

# Projective order-three residues on D5 are (0,1,2) with multiplicities 1,2,2.
assert Counter((w // 2) % 3 for w in (4, 2, 0, -2, -4)) == Counter(
    {0: 1, 1: 2, 2: 2}
)
assert Counter(r % 3 for r in (0, 1, 2, 3, 6)) == Counter(
    {0: 3, 1: 1, 2: 1}
)
assert Counter(r % 3 for r in order_three) == Counter({0: 1, 1: 2, 2: 2})

# These are deductions from the forced sequences, not tests of an actual map.
assert all(a[1] == 1 for a in (ordinary, order_two, order_three))
assert all(max(a) <= 5 for a in (ordinary, order_two, order_three))
jet_order = 5
jet_degrees = tuple(degree - 2 * j for j in range(jet_order + 1))
assert jet_degrees == (18, 16, 14, 12, 10, 8)
assert len(jet_degrees) == 6
assert sum(jet_degrees) == 78

print("PASS: degree-18 five-section Wronskian has degree 70.")
print("PASS: unique orbit partition is 0*12 + 2*20 + 1*30 + 0*60.")
print("PASS: weights 0, 1, 2 give exactly the stated candidate sequences.")
print("PASS: stabilizer residues select (0,1,2,4,5) at order three.")
print("PASS: order-two and order-five stabilizer residues also agree.")
print("PASS: every forced sequence starts (0,1) and ends at most at 5.")
print("PASS: fifth principal-parts rank is 6 and degree is 78.")
print("OPEN: the actual square value and final full repair are undetermined.")
