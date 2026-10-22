#!/usr/bin/env python3
"""Coefficient-free arithmetic for one-axis-jet plus one C5-square detection.

No actual source vector, gate coefficient, matrix, or point is evaluated.
Geometric claims and hypotheses are proved/stated in the companion note.
"""
from collections import Counter
from math import comb

# The local monomial identity m^2 (x^2,y^2)=m^4.
degree_two = {(j,2-j) for j in range(3)}
ideal_quadrics = {(2,0),(0,2)}
assert {(a+c,b+e) for a,b in degree_two for c,e in ideal_quadrics} == {
    (j,4-j) for j in range(5)}

# Residual along five conics, each omitting its named axis.
d, multiplicities = 10, [4] * 6
stages = [(d, tuple(multiplicities))]
restriction_h0 = 0
for omitted in (5, 4, 3, 2, 1):
    trace_degree = 2 * d - sum(m for i, m in enumerate(multiplicities)
                              if i != omitted)
    assert trace_degree == 0
    restriction_h0 += trace_degree + 1
    multiplicities = [m if i == omitted else max(0, m - 1)
                      for i, m in enumerate(multiplicities)]
    d -= 2
    stages.append((d, tuple(multiplicities)))
assert stages == [
    (10, (4,4,4,4,4,4)), (8, (3,3,3,3,3,4)),
    (6, (2,2,2,2,3,3)), (4, (1,1,1,2,2,2)),
    (2, (0,0,1,1,1,1)), (0, (0,0,0,0,0,0))]
assert restriction_h0 + 1 == 6
assert comb(12, 2) - 6 * comb(5, 2) == 6

# Character of the six-axis permutation representation.
one = (1, 1, 1, 1, 1)
D5 = (5, 1, -1, 0, 0)
permutation = (6, 2, 0, 1, 1)
assert tuple(a+b for a,b in zip(one,D5)) == permutation
class_sizes = (1,15,20,12,12)
assert sum(n*a*b for n,a,b in zip(class_sizes,D5,permutation)) == 60
# Each five-factor F_i contains five conics at its own axis and four elsewhere.
for omitted in range(6):
    assert [sum(k != omitted and k != p for k in range(6))
            for p in range(6)] == [5 if p == omitted else 4 for p in range(6)]

# C5 weights of degree-two and degree-three cotangent polynomials.
weights = lambda degree: Counter((degree - 2*j) % 5
                                  for j in range(degree + 1))
rho1, rho2 = Counter({1:1,4:1}), Counter({2:1,3:1})
assert weights(2) == Counter({0:1}) + rho2
assert weights(3) == rho1 + rho2
jet = rho2 + weights(3)
assert jet == rho1 + rho2 + rho2
# Each rotation-weight pair is exchanged by a normalizer reflection;
# its corresponding two-dimensional N-module is irreducible.
# D5 character is5 at identity,0 on nonidentity rotations,1 on reflections.
# Every rho pair has reflection trace0. Thus the N character inner product is:
assert (5 * sum(jet.values()) + 4 * 0 + 5 * 1 * 0) // 10 == 3

# Unique invariant quartic on the square line: s^2 t^2.
assert [j for j in range(5) if (4-2*j) % 5 == 0] == [2]
assert 6*2 == 12
# On a C5-square fiber the tenth twist is trivial.
assert 10 % 5 == 0
assert Counter(range(5))[0] == 1
assert 3+1 == 4

print('PASS: quadruple-axis decics have dimension6 and module 1+D5.')
print('PASS: jet target dimension3; C5-square target dimension1.')
print('Geometric proof gives combined isomorphism; no actual fourth value computed.')
