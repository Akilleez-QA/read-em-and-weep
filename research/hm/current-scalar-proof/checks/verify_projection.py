#!/usr/bin/env python3
"""Exact small Čech regression and coefficientwise legal-line partition checks."""
if not __debug__:
    raise SystemExit('Verification requires assertions enabled; do not use python -O.')

from fractions import Fraction as Q
from itertools import combinations, product
import json

carrier = {0: 0, 1: 1, 2: 1, 3: 2, 4: 2}
choices = {0: [(0, Q(1))], 1: [(1, Q(1, 3)), (2, Q(2, 3))],
           2: [(3, Q(2, 5)), (4, Q(3, 5))]}


def alternate(values, data):
    if len(set(values)) != len(values):
        return Q(0)
    parity = sum(values[i] > values[j] for i in range(len(values)) for j in range(i + 1, len(values)))
    return (-1) ** parity * data.get(tuple(sorted(values)), Q(0))


def differential(c, a):
    return sum((-1) ** k * c(a[:k] + a[k + 1:]) for k in range(len(a)))


def projection(c, a):
    total = Q(0)
    for bs in product(*(choices[j] for j in a)):
        weight = Q(1)
        for _, q in bs:
            weight *= q
        total += weight * c(tuple(b for b, _ in bs))
    return total


def prism(c, a):
    # All target tuples supplied here are increasing, as the theorem requires.
    assert tuple(sorted(a)) == a
    total = Q(0)
    for k in range(len(a)):
        for bs in product(*(choices[carrier[j]] for j in a[:k + 1])):
            weight = Q((-1) ** k)
            for _, q in bs:
                weight *= q
            total += weight * c(tuple(b for b, _ in bs) + a[k:])
    return total


counts = dict(prism_basis_checks=0, projection_chain_checks=0, left_inverse_checks=0,
              homogeneous_partition_divisor_checks=0)
for degree in range(5):
    for basis in combinations(range(5), degree + 1):
        c = lambda a, basis=basis: alternate(a, {basis: Q(1)})
        for a in combinations(range(5), degree + 1):
            lhs = differential(lambda b: prism(c, b), a) + prism(lambda b: differential(c, b), a)
            assert lhs == c(a) - projection(c, tuple(carrier[i] for i in a))
            counts['prism_basis_checks'] += 1
        for a in combinations(range(3), degree + 2):
            assert projection(lambda b: differential(c, b), a) == differential(lambda b: projection(c, b), a)
            counts['projection_chain_checks'] += 1
for degree in range(3):
    for basis in combinations(range(3), degree + 1):
        c = lambda a, basis=basis: alternate(a, {basis: Q(1)})
        for a in combinations(range(3), degree + 1):
            assert projection(lambda b: c(tuple(carrier[i] for i in b)), a) == c(a)
            counts['left_inverse_checks'] += 1

# Sparse polynomials in four variables, represented by integer coefficient maps.
def add(a, b, scale=1):
    result = dict(a)
    for e, c in b.items():
        result[e] = result.get(e, 0) + scale * c
        if not result[e]:
            del result[e]
    return result


def multiply(a, b):
    result = {}
    for e, c in a.items():
        for f, d in b.items():
            key = tuple(x + y for x, y in zip(e, f))
            result[key] = result.get(key, 0) + c * d
    return {e: c for e, c in result.items() if c}


def power(a, n):
    result = {(0, 0, 0, 0): 1}
    for _ in range(n):
        result = multiply(result, a)
    return result


def T1(a, i):
    result = {}
    for e, c in a.items():
        if e[i] == 5:
            result = add(result, {e: c})
            f = list(e)
            f[i] = 3
            result = add(result, {tuple(f): -c})
    return result


def specialize(a, i, value):
    result = {}
    for e, c in a.items():
        key = tuple(z for j, z in enumerate(e) if j != i)
        result[key] = result.get(key, 0) + c * value ** e[i]
    return {e: c for e, c in result.items() if c}


v = [{(0, 0, 0, 0): 1}]
for j in range(1, 5):
    v.append({tuple(int(i in subset) for i in range(4)): 1 for subset in combinations(range(4), j)})
p = v[0]
for value in v[1:]:
    p = multiply(p, value)
mask_counts = []
for j in range(1, 5):
    h = add(power(v[j], 5), p, -1)
    weights = []
    for mask in range(16):
        value = h
        for i in range(4):
            one = T1(value, i)
            value = one if mask & (1 << i) else add(value, one, -1)
        weights.append(value)
        for i in range(4):
            if mask & (1 << i):
                assert all(e[i] >= 3 for e in value)
                assert not specialize(value, i, 1) and not specialize(value, i, -1)
            else:
                assert all(e[i] <= 4 for e in value)  # homogeneous Y_i divisibility
            counts['homogeneous_partition_divisor_checks'] += 1
        if mask.bit_count() > j:
            assert not value
    total = {}
    for value in weights:
        total = add(total, value)
    assert total == h
    mask_counts.append(sum(bool(value) for value in weights))
print(json.dumps({'passed': True, **counts, 'nonzero_mask_counts': mask_counts,
                  'scope': 'Projection/prism and partition algebra only; no geometric pole-bound or residue evaluation.'}, indent=2))
