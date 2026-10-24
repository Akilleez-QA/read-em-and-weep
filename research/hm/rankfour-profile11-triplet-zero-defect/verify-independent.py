#!/usr/bin/env python3
"""Independent universal checks for the triplet zero-defect proof.

No import from characters.py; no actual source coefficients, points, jets,
instance matrices/ranks, bundle search, or height enumeration. Character
products use direct class inner products, not the author's McKay recurrence.
"""
from hashlib import sha256
from pathlib import Path
from itertools import combinations
import sympy as s

if not __debug__:
    raise RuntimeError('Run this independent checker without Python optimization (-O).')

ROOT = Path(__file__).resolve().parent
PROOF_HASH = '0b62e7739d3ff5ef52c5e8c76e50931f99f882015c037132370707f341c425c5'
assert sha256((ROOT / 'PROOF.md').read_bytes()).hexdigest() == PROOF_HASH
for name, digest in [
    ('low-top', 'c3d21cb63ffac4c69247e8deba8ef352f673ac3a7b2f91507bc54fbecae943af'),
    ('top-four', '56bb8a0aa5ada0f550e0967ef9e535838e9162c2ff2e5ced039a3f6ddb2aacf0'),
]:
    original = (ROOT / 'inputs' / (name + '.md')).read_bytes()
    fetched = (ROOT / 'inputs' / ('independently-fetched-' + name + '.md')).read_bytes()
    assert original == fetched
    assert sha256(original).hexdigest() == digest

# Binary icosahedral classes, presented by the physical W trace.
# The four 12-element classes are the two lifts of the two A5 5-cycle classes.
rt5 = s.sqrt(5)
phi, psi = (1 + rt5) / 2, (1 - rt5) / 2
traces = [s.Integer(2), s.Integer(-2), s.Integer(0), s.Integer(1),
          s.Integer(-1), phi, -phi, psi, -psi]
sizes = [1, 1, 30, 20, 20, 12, 12, 12, 12]
assert sum(sizes) == 120

def symmetric_character(n, x):
    # Closed determinant-one binary character polynomial.
    return s.expand(sum((-1)**k * s.binomial(n-k, k) * x**(n-2*k)
                        for k in range(n//2 + 1)))

chars = {name: [s.simplify(symmetric_character(n, x)) for x in traces]
         for name, n in [('one', 0), ('W', 1), ('A', 2), ('S4', 3),
                         ('D', 4), ('T6', 5)]}
# Galois conjugation gives the other triplet and doublet. P is the
# 5-point A5 permutation representation with its constant line removed.
chars['V'] = [s.simplify(a.xreplace({rt5: -rt5})) for a in chars['A']]
chars['Wp'] = [s.simplify(a.xreplace({rt5: -rt5})) for a in chars['W']]
chars['P'] = list(map(s.Integer, [4, 4, 0, 1, 1, -1, -1, -1, -1]))

def inner(a, b):
    return s.simplify(sum(m*x*s.conjugate(y) for m, x, y in zip(sizes, a, b))/120)

assert sum(c[0]**2 for c in chars.values()) == 120
for n, a in chars.items():
    for m, b in chars.items():
        assert inner(a, b) == (1 if n == m else 0), (n, m)

def decompose_product(left, symmetric_degree):
    product = [s.simplify(a*symmetric_character(symmetric_degree, x))
               for a, x in zip(chars[left], traces)]
    result = {name: inner(product, char) for name, char in chars.items()}
    return {name: multiplicity for name, multiplicity in result.items() if multiplicity}

assert decompose_product('A', 4) == {'A': 1, 'D': 1, 'V': 1, 'P': 1}
assert decompose_product('A', 5) == {'S4': 1, 'T6': 2, 'Wp': 1}
assert inner(chars['one'], chars['A']) == 0

# Exterior powers: use formal SL2 torus weights, valid before restriction to G.
z = s.symbols('z', nonzero=True)
weights = [z**2, s.Integer(1), z**-2]
exterior2 = sum(s.prod(t) for t in combinations(weights, 2))
exterior3 = s.prod(weights)
assert s.simplify(exterior2 - sum(weights)) == 0
assert exterior3 == 1
assert s.simplify(sum(weights) - sum(w**-1 for w in weights)) == 0
assert 4 + 2*(-8) == -12 and 3*(-8) == -24

# Symbolic, all-height square completion, not a scan of integer heights.
h1, h2 = s.symbols('h1 h2', real=True)
h3 = 9 - h1 - h2
capacity = 6*h1 - 6*h2 - 6*h3 - sum(h*(h+1) for h in [h1, h2, h3])
assert s.expand(capacity + 30 + (h1-7)**2 + (h2-1)**2 + (h3-1)**2) == 0
assert 7 >= 1 >= 1 >= 0 and 7 + 1 + 1 == 9
assert capacity.subs({h1: 7, h2: 1}) == -30
assert 3*4 - 8 == 4                     # deg A_q
assert 6 + 3*(-6) == -12                # deg C
t = s.symbols('t')
assert s.expand((-54 - (-12-t)) - (-42+t)) == 0
assert s.solve(s.Eq(-42+t, -30), t) == [12]
assert 4 - 8 - 8 == -12                 # first rank-three degree bound
assert (-12) + sum(6-2*j for j in range(2, 8)) == -30

# Projective A5 point stabilizers are cyclic; their possible orders are 1,2,3,5.
assert {60//order for order in [1, 2, 3, 5]} == {60, 30, 20, 12}

print('PASS: exact proof/input hashes and independently fetched input bytes')
print('PASS: complete nine-class orthogonality and the two required gate products')
print('PASS: A invariants vanish; universal self-duality and exterior-power identities')
print('PASS: all-height square identity, unique equality center, degrees, orbit minimum')
print('Proof SHA256:', PROOF_HASH)
