#!/usr/bin/env python3
"""Independent small exact polynomial source identities (standard library only).

These checks establish the algebraic substitutions consumed by the constructor.
They do not establish the geometric carrier-comparison or regular-section theorem.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product

ZERO = (0, 0, 0, 0)
ONE = {ZERO: 1}
X = [{tuple(int(i == j) for j in range(4)): 1} for i in range(4)]


def add(a, b):
    d = defaultdict(int, a)
    for e, c in b.items():
        d[e] += c
    return {e: c for e, c in d.items() if c}


def scale(a, c):
    return {e: v*c for e, v in a.items() if v*c}


def mul(a, b):
    d = defaultdict(int)
    for e, c in a.items():
        for f, v in b.items():
            d[tuple(x+y for x, y in zip(e, f))] += c*v
    return {e: c for e, c in d.items() if c}


def power(a, n):
    assert type(n) is int and n >= 0
    out = ONE
    while n:
        if n % 2:
            out = mul(out, a)
        n //= 2
        if n:
            a = mul(a, a)
    return out


def times(items):
    out = ONE
    for a in items:
        out = mul(out, a)
    return out


def plus(items):
    out = {}
    for a in items:
        out = add(out, a)
    return out


def poly(rows):
    out = {}
    for key, value in rows:
        e = tuple(map(int, key.split(','))) if isinstance(key, str) else tuple(key)
        assert len(e) == 4 and all(type(x) is int and x >= 0 for x in e)
        c = Fraction(value)
        assert c and e not in out, 'Noncanonical sparse polynomial'
        out[e] = c
    return out


def substitute(p, variables):
    return plus(scale(times(power(v, e) for v, e in zip(variables, key)), c)
                for key, c in p.items())


def elementary(indices, degree):
    if degree < 0 or degree > len(indices):
        return {}
    return plus(times(X[i] for i in subset) for subset in combinations(indices, degree))


V = [elementary(tuple(range(4)), j) for j in range(5)]
F = [add(power(V[j], 4), scale(times(V[k] for k in range(5) if k != j), -1))
     for j in range(5)]
TAGS = X + [add(power(x, 2), scale(ONE, -1)) for x in X] + V[1:4] + F
NAMES = ['X1', 'X2', 'X3', 'X4', 'L1', 'L2', 'L3', 'L4',
         'V1', 'V2', 'V3', 'F0', 'F1', 'F2', 'F3', 'F4']
H = [mul(V[j], F[j]) for j in range(5)]


def factored(f):
    assert len(f['powers']) == 16
    assert Fraction(f['coefficient']) != 0
    return scale(times(power(p, n) for p, n in zip(TAGS, f['powers'])),
                 Fraction(f['coefficient']))


def verify_tags_and_inverses(seeds, dag):
    assert seeds['tag_names'] == NAMES
    assert len(seeds['tags']) == len(TAGS) == 16
    for supplied, expected in zip(seeds['tags'], TAGS):
        assert poly(supplied) == expected, 'Tag polynomial is not its declared formula'
    assert set(seeds['files']) == {'carriers-234.json'}, 'Only this carrier is in scope'
    seed = seeds['files']['carriers-234.json']
    nodes = dag['nodes']
    assert seed['nodes'] == len(nodes) == 178251
    inverse_ids = {str(i) for i, n in enumerate(nodes) if n[0] == 'inv'}
    assert set(seed['inverse_nodes']) == inverse_ids

    @lru_cache(None)
    def expand(i):
        n = nodes[i]
        if n[0] == 'const':
            return scale(ONE, Fraction(int(n[1]), int(n[2])))
        if n[0] == 'var':
            return X[n[1]]
        if n[0] == 'add':
            return add(expand(n[1]), expand(n[2]))
        if n[0] == 'mul':
            return mul(expand(n[1]), expand(n[2]))
        raise AssertionError('An inverse denominator contains a nested inverse')

    positive_seeds = {}
    for key in sorted(inverse_ids, key=int):
        source_id = nodes[int(key)][1]
        expected = factored(seed['inverse_nodes'][key])
        assert expand(source_id) == expected, f'Incorrect factorization of inverse {key}'
        # The tagged importer substitutes positive denominator nodes too.
        if source_id in positive_seeds:
            assert positive_seeds[source_id] == seed['inverse_nodes'][key]
        positive_seeds[source_id] = seed['inverse_nodes'][key]
    assert seeds['exact_inverse_checks'] == len(inverse_ids) == 18
    return {'tagIdentities': 16, 'inverseFactorIdentities': len(inverse_ids)}


def verify_denominators(model, seeds, denominators):
    assert denominators == seeds['model_denominators']
    assert len(denominators) == len(model['charts']) == 6
    checks = 0
    for j, chart in enumerate(model['charts']):
        assert set(denominators[j]) == {'di', 'dp', 'dh'}
        for key in ['di', 'dp', 'dh']:
            assert substitute(poly(chart[key]), V[1:]) == factored(denominators[j][key]), (j, key)
            checks += 1
    return {'modelDenominatorIdentities': checks}


def verify_prefactors(model, pref):
    assert pref['variables'] == ['v1/v0', 'v2/v0', 'v3/v0', 'v4/v0']
    b, c = model['charts'][1:3]
    checks = 0
    for i in range(2):
        p = plus(mul(poly(b['I'][10][t]), mul(poly(b['P'][t][k]), poly(c['I'][k][i])))
                 for t in range(2) for k in range(15))
        assert p == mul(poly(b['dp']), poly(pref['aNumerators'][i])), ('a', i)
        checks += 1
    for i in range(2):
        p = plus(mul(poly(c['P'][i][k]), poly(b['H1'][k][0])) for k in range(15))
        assert mul(X[0], p) == mul(poly(b['dh']), poly(pref['bNumerators'][i])), ('b', i)
        checks += 1
    for k in range(15):
        expected = scale(poly(b['dh']), -1) if k == 3 else {}
        assert mul(X[0], poly(b['H1'][k][0])) == expected, ('H1 column', k)
        checks += 1
    for supplied, expected in zip(pref['aDenominatorFactors'], [b['di'], c['di']]):
        assert poly(supplied) == poly(expected)
        checks += 1
    assert len(pref['aDenominatorFactors']) == len(pref['bDenominatorFactors']) == 2
    assert poly(pref['bDenominatorFactors'][0]) == X[0]
    assert poly(pref['bDenominatorFactors'][1]) == poly(c['dp'])
    return {'scalarPrefactorIdentities': checks+2}


def T(p, axis):
    """(x_i^5-x_i^3) times the x_i^5 coefficient; no sampling."""
    out = {}
    for e, c in p.items():
        if e[axis] == 5:
            low = tuple(v if i != axis else 3 for i, v in enumerate(e))
            out = add(out, {e: c, low: -c})
    return out


def verify_moments(features):
    assert features['schema'] == 'hm-line-projection-feature-moments-v1'
    assert set(features['moments']) == {'1', '2', '3', '4'}
    checks = 0
    for j in range(1, 5):
        rows = features['moments'][str(j)]
        assert len(rows) == 16
        for subset, row in enumerate(rows):
            assert row['subset'] == subset
            if not subset:
                assert row == {'subset': 0, 'identity': True}
                continue
            assert 'identity' not in row
            assert row['selectedCoordinatePowers'] == 3 and row['selectedLineFactorPowers'] == 1
            selected = [i for i in range(4) if subset >> i & 1]
            remaining = tuple(i for i in range(4) if i not in selected)
            top = {tuple(0 if i in selected else v for i, v in enumerate(e)): c
                   for e, c in H[j].items() if all(e[i] == 5 for i in selected)}
            closed = power(elementary(remaining, j-len(selected)), 5)
            assert poly(row['topCoefficient']) == top == closed, (j, subset)
            checks += 1
        weights = []
        for mask in range(16):
            p = H[j]
            for i in range(4):
                q = T(p, i)
                p = q if mask >> i & 1 else add(p, scale(q, -1))
            weights.append(p)
        assert plus(weights) == H[j]
        checks += 1
        for subset in range(16):
            direct = plus(p for mask, p in enumerate(weights) if mask & subset == subset)
            expected = H[j]
            for i in range(4):
                if subset >> i & 1:
                    expected = T(expected, i)
            assert direct == expected, ('all-mask feature moment', j, subset)
            if subset:
                row = rows[subset]
                formula = mul(poly(row['topCoefficient']), times(
                    mul(power(X[i], 3), TAGS[4+i]) for i in range(4) if subset >> i & 1))
                assert expected == formula
            checks += 1
    assert checks == 128
    return {'featureMomentIdentities': checks, 'featureMoments': 64}


def verify_mask_coverage(js_basis):
    """Universal identity by coefficient incidence in 48 formal mask weights.

For every feature code, both sides contain exactly the same monomials
w2[m2]*w3[m3]*w4[m4]. The 4096 masks are not sampled or truncated.
"""
    assert len(js_basis) == 256
    masks = list(product(range(16), repeat=3))
    universe = set(masks)
    checked_terms = 0
    for code, supplied in enumerate(js_basis):
        digits = [(code // 4**i) % 4 for i in range(4)]
        subsets = [sum(1 << i for i, d in enumerate(digits) if d == j+1) for j in range(3)]
        assert supplied == subsets
        direct = {m for m in masks if all(d == 0 or (m[d-1] >> i & 1)
                                         for i, d in enumerate(digits))}
        moment_product = set(product(*[[m for m in range(16) if m & s == s] for s in subsets]))
        assert direct == moment_product
        if code == 0:
            assert direct == universe and len(direct) == 4096
        checked_terms += len(direct)
    return {'maskTriples': len(masks), 'featureCodes': len(js_basis),
            'universalMaskCoefficientIncidences': checked_terms}
