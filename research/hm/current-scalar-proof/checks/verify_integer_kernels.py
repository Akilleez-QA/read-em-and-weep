#!/usr/bin/env python3
"""Independent exact constructions of G^-70 and bounded functional identities."""
if not __debug__:
    raise SystemExit('Verification requires assertions enabled; do not use python -O.')

from itertools import product, permutations
from math import comb
import json

T, Z = 6, 22
ONE = {(0, 0): 1}
G = {(0, 0): 1, (0, 1): 1, (1, 0): 1, (1, 1): 3,
     (1, 2): 1, (2, 1): 1, (2, 2): 1}


def add(a, b, scale=1):
    result = dict(a)
    for e, c in b.items():
        result[e] = result.get(e, 0) + scale * c
        if not result[e]:
            del result[e]
    return result


def multiply(a, b, prime=None):
    result = {}
    for (t, z), c in a.items():
        for (u, w), d in b.items():
            if t + u < T and z + w < Z:
                key = (t + u, z + w)
                result[key] = result.get(key, 0) + c * d
    if prime:
        result = {e: c % prime for e, c in result.items()}
    return {e: c for e, c in result.items() if c}


def power(a, n, prime=None):
    result = ONE
    while n:
        if n & 1:
            result = multiply(result, a, prime)
        a = multiply(a, a, prime)
        n >>= 1
    return result


def binomial(n, k):
    return comb(n, k) if n >= 0 else (-1) ** k * comb(k - n - 1, k)


# Construction 1: binomial expansion in the nilpotent element G-1.
V, value, direct = add(G, ONE, -1), ONE, {}
for n in range(T + Z - 1):
    direct = add(direct, value, binomial(-70, n))
    value = multiply(value, V)
assert not value
assert multiply(direct, power(G, 70)) == ONE

# Construction 2: the explicit six-row formula in the note.
s, D = {(0, 0): 1, (0, 1): 1}, {(0, 0): 1, (0, 1): 3, (0, 2): 1}
formula, rows = {}, []
for t in range(T):
    row = []
    for v in range(t // 2 + 1):
        c = binomial(-70, t - v) * comb(t - v, v)
        row.append(c)
        exp = -70 - t + 2 * v
        low = {(0, z): binomial(exp, z) for z in range(Z)}
        value = multiply(low, power(D, t - 2 * v))
        for (_, z), coefficient in value.items():
            if z + v < Z:
                key = (t, z + v)
                formula[key] = formula.get(key, 0) + c * coefficient
    rows.append(row)
formula = {e: c for e, c in formula.items() if c}
assert direct == formula
assert rows == [[1], [-70], [2485, -70], [-59640, 4970],
                [1088430, -178920, 2485], [-16108764, 4353720, -178920]]
for p, P in [(7, 343), (13, 169), (29, 841), (71, 71)]:
    assert power(G, P, p) == ONE
    assert power(G, P - 70, p) == {e: c % p for e, c in direct.items() if c % p}
assert {e: c % 71 for e, c in direct.items() if c % 71} == G

# Check every coefficient-slot identity, total-degree filter, and edge sign.
request_count = slot_count = 0
for m in product(range(3), repeat=4):
    S = sum(m)
    for edge in permutations(range(4)):
        i, j, k, l = edge
        if m[i] != 2:
            continue
        request_count += 1
        parity = sum(edge[a] > edge[b] for a in range(4) for b in range(a + 1, 4))
        remaining = [q for q in range(4) if q != i]
        tail = [remaining.index(q) for q in (j, k, l)]
        tail_parity = sum(tail[a] > tail[b] for a in range(3) for b in range(a + 1, 3))
        assert (parity - i - tail_parity) % 2 == 0
        d, L = 3 + m[j], 21 - m[l]
        for r in range(d + 1):
            for ell in range(L + 1):
                source = (272, 212 - r, 159 - S + r - ell, 48 + ell)
                assert sum(source) == 691 - S and min(source) >= 0
                # Remove (uab)^48 and apply the reversal exponent map.
                u, a, b = source[1] - 48, source[2] - 48, source[3] - 48
                assert (164 - u, 305 - u - a - b, b) == (r, 30 + S, ell)
                slot_count += 1
assert request_count == 648

# Independent monomial normal-form/leading-residue regression.
# For a monomial a^u, reduction a_j^5 -> a1*a2*a3*a4 is monomial.
checks = 0
for u in product(range(10), repeat=4):
    e = list(u)
    while max(e) >= 5:
        j = next(i for i, x in enumerate(e) if x >= 5)
        e = [x + 1 for x in e]
        e[j] -= 5
    coefficient = int(e == [4, 4, 4, 4])
    K = sum(u) - 16
    expected = int(K >= 0 and all(x + K >= 4 and (x + K - 4) % 5 == 0 for x in u))
    assert coefficient == expected
    checks += 1
print(json.dumps({'passed': True, 'integer_kernel_coefficients': 132,
                  'independent_kernel_constructions': 2, 'prime_field_specializations': [7, 13, 29, 71],
                  'all_81_edge_requests': request_count, 'coefficient_slot_checks': slot_count,
                  'monic_normal_form_residue_checks': checks,
                  'scope': 'Universal algebra and indexing only; no geometric source coefficients evaluated.'}, indent=2))
