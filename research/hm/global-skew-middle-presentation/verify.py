"""Universal dimension checks; no actual HM coefficients or points."""
from math import comb
from itertools import combinations
from collections import defaultdict

def h0_projective(n, degree):
    return comb(n + degree, n) if degree >= 0 else 0

g0, g1, g2 = (2 * comb(5, k) for k in (3, 4, 5))
assert (g0, g1, g2) == (20, 10, 2)
# Symmetric square of the Koszul resolution, homological degrees 0..4.
ranks = [comb(g0+1, 2), g1*g0, comb(g1, 2)+g2*g0,
         g2*g1, comb(g2+1, 2)]
degrees = [3, 2, 1, 0, -1]
assert ranks == [210, 200, 85, 20, 3]
# On P4, line bundles have no intermediate cohomology; H4 starts at -5.
assert all(d > -5 for d in degrees)
sections = [r*h0_projective(4, d) for r, d in zip(ranks, degrees)]
assert sections == [7350, 3000, 425, 20, 0]
global_operators = sum((-1)**i * s for i, s in enumerate(sections))
assert global_operators == 4755
assert sections[0] - global_operators == 2595
vertex_operators = comb(7, 2)*6 + 6*6*5 + comb(7, 2)*4
assert vertex_operators == 390
assert global_operators - vertex_operators == 4365
assert sections[0] - vertex_operators == 6960
# E(1)|P1 = 6 O(1) + 6 O; exactly eighteen restricted generators.
assert 6*2+6 == g0-2

# Check i_x^2=0 on every constant three-form with free coordinate symbols.
for triple in combinations(range(5), 3):
    terms = defaultdict(int)
    for i, first in enumerate(triple):
        remaining = triple[:i]+triple[i+1:]
        for j, second in enumerate(remaining):
            output = remaining[:j]+remaining[j+1:]
            monomial = tuple(sorted((first, second)))
            terms[(output, monomial)] += (-1)**(i+j)
    assert all(value == 0 for value in terms.values())

# Formal symplectic transvection identity. Variables are the four independent
# pairings beta(p,eta), beta(p,zeta), beta(q,eta), beta(q,zeta).
skew_terms = defaultdict(int)
for coefficient, factors in [(1, ('qe','pz')), (1, ('pe','qz')),
                             (-1, ('qz','pe')), (-1, ('pz','qe'))]:
    skew_terms[tuple(sorted(factors))] += coefficient
assert all(value == 0 for value in skew_terms.values())
print('PASS: universal contraction, skewness, Koszul-square dimensions, and vertex dimensions')
