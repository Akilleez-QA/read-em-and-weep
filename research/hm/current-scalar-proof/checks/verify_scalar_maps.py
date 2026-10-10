#!/usr/bin/env python3
"""Exact homogeneous scalar-map identities; standard library only."""
if not __debug__:
    raise SystemExit('Verification requires assertions enabled; do not use python -O.')

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
model = json.loads((ROOT / 'data/model.json').read_text())
canonical = json.dumps(model, separators=(',', ':')).encode()
assert hashlib.sha256(canonical).hexdigest() == 'b6b532c4bab5787397a4cddde34210c12fae71853b30cb73ecbe8a9c2b4826b2'
one = [['0,0,0,0', 1]]
assert model['gamma'][10] == [one, [], [], [], []]
assert [row[0] for row in model['ev']] == [one, []]
for a in range(5):
    for b in range(2):
        assert (model['ev'][b][0] if a == 0 else []) == (model['gamma'][10][a] if b == 0 else [])
for c in (0, 5):
    chart = model['charts'][c]
    assert chart['pivot'] == 0
    assert chart['I'][10] == [[], []]
    assert chart['H0'][0][10] == chart['dh']
    assert all(not value for j, value in enumerate(chart['H0'][0]) if j != 10)


def variable(monomial):
    e = tuple(map(int, monomial.split(',')))
    assert all(z in (0, 1) for z in e) and sum(e) in (0, 1)
    return 0 if sum(e) == 0 else e.index(1) + 1


G = [[[0] * 5 for _ in range(5)] for _ in range(15)]
for i, row in enumerate(model['gamma']):
    for a, poly in enumerate(row):
        for monomial, coefficient in poly:
            G[i][a][variable(monomial)] += coefficient
for b, row in enumerate(model['ev']):
    for j, poly in enumerate(row):
        expected = [] if j // 5 != b else [[','.join(str(int(k + 1 == j % 5)) for k in range(4)), 1]]
        assert poly == expected
M = []
for a in range(5):
    for b in range(2):
        for k in range(5):
            row = [0] * 80
            row[10 * a + 5 * b + k] = 1
            for i in range(15):
                row[50 + 2 * i + b] = G[i][a][k]
            M.append(row)
assert all(sum(abs(M[r][c]) for r in range(50)) == 1 for c in range(50))
assert all(sum(abs(x) for x in row[:50]) == 1 for row in M)
for i in range(15):
    for b in range(2):
        vector = [0] * 80
        vector[50 + 2 * i + b] = 1
        for a in range(5):
            for k in range(5):
                vector[10 * a + 5 * b + k] = -G[i][a][k]
        assert all(sum(x * y for x, y in zip(row, vector)) == 0 for row in M)

print(json.dumps({'passed': True, 'bottom_matrix_unit_identities': 10,
                  'merged_anchor_row_checks': 2, 'constant_map_equations': 50,
                  'equation_rank_over_every_field': 50,
                  'constant_scalar_map_dimension_over_every_field': 30,
                  'scope': 'Polynomial row identities only; no geometric coefficient evaluation.'}, indent=2))
