#!/usr/bin/env python3
"""Recompute the current-L contractions from the 24 supplied exact quotients.

This is a read-only downstream replay. It does not regenerate geometric source
DAGs or prove that the supplied quotients are coefficients of that source.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import sys
import exact_oracle as O

if sys.flags.optimize:
    raise RuntimeError('Run assertion-enabled Python, without -O')
HERE = Path(__file__).resolve().parent
load = lambda p: json.loads(p.read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
enc = lambda x: [str(x.numerator), str(x.denominator)]


def verify(root=HERE):
    pins = load(root / 'data-pins.json')
    for name, digest in pins['files'].items():
        assert sha(root / name) == digest, 'File digest mismatch: ' + name
    expected = load(root / 'final-result.json')
    assert sha(root / 'final-result.json') == pins['originalFinalResultSHA256']
    relations = load(root / 'relation-rows.json')
    matrix = []
    for relation in relations['relations']:
        row = [0] * 81
        for term in relation['terms']:
            row[term['index']] += term['coefficient']
        matrix.append(row)
    pivots = relations['relation_identity_minor_columns']
    assert len(matrix) == len(pivots) == 47
    assert [[row[p] for p in pivots] for row in matrix] == [[int(i == j) for j in range(47)] for i in range(47)]
    zeros = sorted(r['terms'][0]['index'] for r in relations['relations'] if r['kind'] == 'coordinate_zero')
    assert len(set(zeros)) == 35 and zeros == expected['theoremDerivedZeroIndices']
    numerical = sorted(set(range(81)) - set(zeros))
    assert numerical == expected['numericallyEvaluatedIndices'] and len(numerical) == 46
    # The identity minor checks relation arithmetic. Its application to the
    # actual geometric class is a separate proof hypothesis, not a mod-p lift.
    polynomials = {}
    for roles in permutations(range(4)):
        q = load(root / 'quotients' / ('edge-' + ''.join(map(str, roles)) + '.json'))
        assert q['roles'] == list(roles) and q['field'] == 'Q'
        assert q['quotientShape'] == [6, 37, 22]
        assert q['homogeneousDegreesRemainSeparated'] and not q['pairingAggregated']
        assert q['commonDenominator'] == '64'
        rows = q['integerQuotientCoefficients']
        assert rows == sorted(rows) and len(rows) == q['retainedNonzeros']
        assert hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest() == q['integerCoefficientSHA256']
        assert all(len(r) == 4 and all(type(x) is int for x in r[:3]) and all(0 <= x < b for x, b in zip(r, [6, 37, 22])) and type(r[3]) is str and str(int(r[3])) == r[3] and int(r[3]) for r in rows)
        poly = {tuple(r[:3]): F(int(r[3]), 64) for r in rows}
        assert len(poly) == len(rows)
        polynomials[roles] = poly
    kernels = O.kernels()  # Exact Z, never reductions modulo a prime.
    values = [F(0)] * 81
    seen = {}
    row_count = nonzero_rows = edge_count = nonzero_edges = 0
    degree_counts = Counter()
    for m in product(range(3), repeat=4):
        index = sum((2 - m[i]) * 3**(3 - i) for i in range(4))
        attribution = expected['coordinateAttribution'][index]
        assert attribution['index'] == index and attribution['m'] == list(m)
        assert attribution['laurentExponents'] == [-x - 1 for x in m]
        if index in zeros:
            continue
        S = sum(m)
        assert 3 <= S <= 6
        degree_counts[S] += 1
        for roles, poly in polynomials.items():
            i, j, k, ell_axis = roles
            if m[i] != 2:
                continue
            sign = (-1)**sum(roles[a] > roles[b] for a in range(4) for b in range(a + 1, 4))
            d, limit, w = 3 + m[j], 21 - m[ell_axis], 30 + S
            unsigned = F(0)
            for r in range(d + 1):
                for ell in range(limit + 1):
                    ex = [0] * 4
                    ex[i], ex[j], ex[k], ex[ell_axis] = 272, 212-r, 159-S+r-ell, 48+ell
                    assert sum(ex) == 691-S
                    assert (212-ex[j], 449-sum(ex[a] for a in (j, k, ell_axis)), ex[ell_axis]-48) == (r, w, ell)
                    coefficient = poly.get((r, w, ell), F(0))
                    unsigned += coefficient * kernels[d-r][limit-ell]
                    ex = tuple(ex)
                    if ex in seen:
                        assert seen[ex] == coefficient
                    seen[ex] = coefficient
                    row_count += 1
                    nonzero_rows += bool(coefficient)
            values[index] += sign * unsigned
            edge_count += 1
            nonzero_edges += bool(unsigned)
    assert degree_counts == {3: 12, 4: 18, 5: 12, 6: 4}
    assert [enc(v) for v in values] == expected['coordinates']
    assert not any(values)
    assert all(sum(a*b for a,b in zip(row, values)) == 0 for row in matrix)
    stats = {'acceptedFullQuotients': len(polynomials), 'requests': edge_count,
             'sourceRows': row_count, 'distinctSourceExponents': len(seen),
             'nonzeroSourceRows': nonzero_rows,
             'nonzeroDistinctSourceCoefficients': sum(bool(v) for v in seen.values()),
             'nonzeroSignedEdgeSelections': nonzero_edges}
    for key, value in stats.items():
        assert value == expected[key], (key, value, expected[key])
    return {'status': 'PASS', 'field': 'Q', **stats,
            'numericalCoordinatesReplayed': 46, 'theoremDerivedZerosUsed': 35,
            'relationRowsChecked': 47, 'all81ScalarCoordinatesZero': True,
            'sourceDAGsRegenerated': False, 'fullObstructionVanishingProved': False}


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
