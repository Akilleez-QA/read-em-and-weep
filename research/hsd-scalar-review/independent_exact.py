#!/usr/bin/env python3
"""Independent exact-rational audit of the pinned current-scalar identities.

Does not import the package validators. Polynomials are dicts of exponent
tuples to fractions.Fraction. Chart variables are substituted by the elementary
symmetric polynomials e1,e2,e3,e4 in x1,x2,x3,x4, with e0 = v0 = 1.
"""
import argparse
import json
import random
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path

ZERO = (0, 0, 0, 0)
ONE = {ZERO: Fraction(1)}
X = [{tuple(int(i == j) for j in range(4)): Fraction(1)} for i in range(4)]


def add(a, b):
    out = defaultdict(Fraction, a)
    for exp, coef in b.items():
        out[exp] += coef
    return {exp: coef for exp, coef in out.items() if coef}


def scale(a, coef):
    return {exp: value * coef for exp, value in a.items() if value * coef}


def mul(a, b):
    out = defaultdict(Fraction)
    for exp, coef in a.items():
        for other, value in b.items():
            out[tuple(x + y for x, y in zip(exp, other))] += coef * value
    return {exp: coef for exp, coef in out.items() if coef}


def power(poly, exponent):
    if exponent < 0:
        raise ValueError('negative polynomial power')
    result = ONE
    base = poly
    while exponent:
        if exponent & 1:
            result = mul(result, base)
        exponent >>= 1
        if exponent:
            base = mul(base, base)
    return result


def parse_sparse(rows):
    out = {}
    for key, value in rows:
        if isinstance(key, str):
            exp = tuple(int(part) for part in key.split(','))
        else:
            exp = tuple(int(part) for part in key)
        if len(exp) != 4 or any(part < 0 for part in exp):
            raise ValueError(key)
        coef = Fraction(value)
        if coef == 0 or exp in out:
            raise ValueError('noncanonical sparse row')
        out[exp] = coef
    return out


def elementary(degree):
    total = {}
    for subset in combinations(range(4), degree):
        term = ONE
        for index in subset:
            term = mul(term, X[index])
        total = add(total, term)
    return total or {}


# v0 = 1 and vj = ej(x) for j = 1..4.
E = [elementary(degree) for degree in range(5)]
V = [ONE] + E[1:]
F = []
for j in range(5):
    others = ONE
    for k in range(5):
        if k != j:
            others = mul(others, V[k])
    F.append(add(power(V[j], 4), scale(others, -1)))
TAGS = (
    X
    + [add(power(variable, 2), scale(ONE, -1)) for variable in X]
    + V[1:4]
    + F
)
H = [mul(V[j], F[j]) for j in range(5)]


def substitute(poly, variables):
    total = {}
    for exp, coef in poly.items():
        term = scale(ONE, coef)
        for variable, exponent in zip(variables, exp):
            if exponent:
                term = mul(term, power(variable, exponent))
        total = add(total, term)
    return total


def tag_product(coefficient, powers):
    result = scale(ONE, Fraction(coefficient))
    for tag, exponent in zip(TAGS, powers):
        if exponent:
            result = mul(result, power(tag, exponent))
    return result


def load_model(path):
    text = Path(path).read_text()
    if path.endswith('.js'):
        text = text.split('const MODEL=', 1)[1]
        model, _ = json.JSONDecoder().raw_decode(text)
        return model
    return json.loads(text)


def check_denominators(model, claimed):
    failures = []
    for chart_index, chart in enumerate(model['charts']):
        for key in ('di', 'dp', 'dh'):
            substituted = substitute(parse_sparse(chart[key]), E[1:])
            expected = tag_product(claimed[chart_index][key]['coefficient'],
                                   claimed[chart_index][key]['powers'])
            if substituted != expected:
                failures.append((chart_index, key, len(substituted), len(expected)))
    return failures


def matrix_sum(rows):
    total = {}
    for poly in rows:
        total = add(total, poly)
    return total


def check_prefactors(model, prefactors):
    chart_b = model['charts'][1]
    chart_c = model['charts'][2]
    failures = []
    identities = 0
    for column in range(2):
        terms = []
        for t in range(2):
            for k in range(15):
                terms.append(mul(parse_sparse(chart_b['I'][10][t]),
                                 mul(parse_sparse(chart_b['P'][t][k]),
                                     parse_sparse(chart_c['I'][k][column]))))
        contracted = matrix_sum(terms)
        expected = mul(parse_sparse(chart_b['dp']), parse_sparse(prefactors['aNumerators'][column]))
        identities += 1
        if contracted != expected:
            failures.append(('a-row', column))
    first = X[0]
    for column in range(2):
        terms = []
        for k in range(15):
            terms.append(mul(parse_sparse(chart_c['P'][column][k]),
                             parse_sparse(chart_b['H1'][k][0])))
        contracted = matrix_sum(terms)
        expected = mul(parse_sparse(chart_b['dh']), parse_sparse(prefactors['bNumerators'][column]))
        identities += 1
        if mul(first, contracted) != expected:
            failures.append(('b-column', column))
    for k in range(15):
        got = mul(first, parse_sparse(chart_b['H1'][k][0]))
        expected = scale(parse_sparse(chart_b['dh']), -1) if k == 3 else {}
        identities += 1
        if got != expected:
            failures.append(('H1-column0', k))
    if parse_sparse(prefactors['aDenominatorFactors'][0]) != parse_sparse(chart_b['di']):
        failures.append(('a-denominator', 0))
    if parse_sparse(prefactors['aDenominatorFactors'][1]) != parse_sparse(chart_c['di']):
        failures.append(('a-denominator', 1))
    identities += 2
    if parse_sparse(prefactors['bDenominatorFactors'][0]) != first:
        failures.append(('b-denominator', 0))
    if parse_sparse(prefactors['bDenominatorFactors'][1]) != parse_sparse(chart_c['dp']):
        failures.append(('b-denominator', 1))
    identities += 2
    # Rational cancellation after the chart substitution: dp and di of chart 1
    # must agree, otherwise dividing the a-numerator by di would not cancel dp.
    for key_left, key_right, label in (
        ('di', 'dp', 'chart1-di-dp'),
        ('di', 'dh', 'chart1-di-dh'),
        ('dp', 'dh', 'chart1-dp-dh'),
    ):
        left = substitute(parse_sparse(chart_b[key_left]), E[1:])
        right = substitute(parse_sparse(chart_b[key_right]), E[1:])
        identities += 1
        if left != right:
            failures.append((label, len(left), len(right)))
    return identities, failures


def axis_extract(poly, axis):
    """(x_i^5 - x_i^3) times the coefficient of x_i^5."""
    out = {}
    for exp, coef in poly.items():
        if exp[axis] == 5:
            lowered = tuple(value if index != axis else 3 for index, value in enumerate(exp))
            out = add(out, {exp: coef, lowered: -coef})
    return out


def check_moments(features, sample_pairs):
    failures = []
    checked = 0
    for carrier, subset in sample_pairs:
        row = features['moments'][str(carrier)][subset]
        if subset == 0:
            if row != {'subset': 0, 'identity': True}:
                failures.append((carrier, subset, 'empty'))
            checked += 1
            continue
        selected = [i for i in range(4) if subset >> i & 1]
        top = {}
        for exp, coef in H[carrier].items():
            if all(exp[i] == 5 for i in selected):
                reduced = tuple(0 if i in selected else value for i, value in enumerate(exp))
                top[reduced] = coef
        claimed = parse_sparse(row['topCoefficient'])
        weight = ONE
        for i in selected:
            weight = mul(weight, mul(power(X[i], 3), TAGS[4 + i]))
        operator = H[carrier]
        for i in selected:
            operator = axis_extract(operator, i)
        checked += 1
        if claimed != top or operator != mul(top, weight):
            failures.append((carrier, subset))
    return checked, failures


def feature_digits(code):
    return [(code // 4**i) % 4 for i in range(4)]


def feature_subsets(code):
    subsets = [0, 0, 0]
    for coordinate, digit in enumerate(feature_digits(code)):
        if digit:
            subsets[digit - 1] |= 1 << coordinate
    return subsets


def mask_membership_by_coordinate(code, masks):
    digits = feature_digits(code)
    accepted = set()
    for mask in masks:
        if all(digit == 0 or (mask[digit - 1] >> coordinate) & 1
               for coordinate, digit in enumerate(digits)):
            accepted.add(mask)
    return accepted


def mask_membership_by_moment_product(code, masks):
    subsets = feature_subsets(code)
    return {mask for mask in masks if all((mask[j] & subsets[j]) == subsets[j] for j in range(3))}


def check_masks(sample_codes, all_masks):
    failures = []
    incidences = 0
    for code in sample_codes:
        by_coordinate = mask_membership_by_coordinate(code, all_masks)
        by_moment = mask_membership_by_moment_product(code, all_masks)
        if by_coordinate != by_moment:
            failures.append(code)
        incidences += len(by_coordinate)
    return incidences, failures


def expand_inverses(dag, seeds):
    nodes = dag['nodes']
    inverse_ids = [i for i, node in enumerate(nodes) if node[0] == 'inv']

    @lru_cache(None)
    def expand(index):
        node = nodes[index]
        kind = node[0]
        if kind == 'const':
            return scale(ONE, Fraction(int(node[1]), int(node[2])))
        if kind == 'var':
            return X[node[1]]
        if kind == 'add':
            return add(expand(node[1]), expand(node[2]))
        if kind == 'mul':
            return mul(expand(node[1]), expand(node[2]))
        raise AssertionError(f'nested inverse at {index}')

    failures = []
    for inverse_id in inverse_ids:
        source = nodes[inverse_id][1]
        claim = seeds['files']['carriers-234.json']['inverse_nodes'][str(inverse_id)]
        expected = tag_product(claim['coefficient'], claim['powers'])
        if expand(source) != expected:
            failures.append(inverse_id)
    return len(inverse_ids), failures


def cross_check(original, reduced):
    """new_entry * old_denominator == old_entry * new_denominator, entrywise."""
    unchanged = (
        original['gamma'] == reduced['gamma']
        and original['delta'] == reduced['delta']
        and original['ev'] == reduced['ev']
    )
    denominator_of = {'I': 'di', 'P': 'dp', 'H0': 'dh', 'H1': 'dh'}
    checked = 0
    failures = []
    for chart_index, (old_chart, new_chart) in enumerate(zip(original['charts'], reduced['charts'])):
        if old_chart['pivot'] != new_chart['pivot']:
            failures.append(('pivot', chart_index))
        for name, den_name in denominator_of.items():
            for row_index, (old_row, new_row) in enumerate(zip(old_chart[name], new_chart[name])):
                for col_index, (old_entry, new_entry) in enumerate(zip(old_row, new_row)):
                    left = mul(parse_sparse(old_entry), parse_sparse(new_chart[den_name]))
                    right = mul(parse_sparse(new_entry), parse_sparse(old_chart[den_name]))
                    checked += 1
                    if left != right:
                        failures.append((chart_index, name, row_index, col_index))
    return checked, failures, unchanged


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--numerator-package', type=Path,
                        default=here.parent / 'hm' / 'current-scalar-numerator')
    parser.add_argument('--bridge', type=Path,
                        default=here.parent / 'hm' / 'current-scalar-source-bridge')
    parser.add_argument('--reduced-model', type=Path,
                        help='optional regenerated reduced-model.json; compared with the embedded model')
    parser.add_argument('--carrier', type=Path,
                        help='optional regenerated carriers-234.json for the 18 inverse expansions')
    args = parser.parse_args()
    root = args.numerator_package
    bridge = args.bridge
    claimed = json.loads((root / 'model_denominators.json').read_text())
    prefactors = json.loads((root / 'public_hm_scalar_prefactors.json').read_text())
    features = json.loads((root / 'feature-moments.json').read_text())
    seeds = json.loads((root / 'inverse_seeds.json').read_text())
    reduced = load_model(str(bridge / 'public_generate_hm_mask_coefficients_reduced.js'))
    original = load_model(str(bridge / 'generate-hm-mask-coefficients-original.js'))
    embedded_matches_emission = None
    if args.reduced_model:
        embedded_matches_emission = reduced == load_model(str(args.reduced_model))

    tag_failures = []
    stored_tags = seeds['tags']
    for index, tag in enumerate(TAGS):
        if parse_sparse(stored_tags[index]) != tag:
            tag_failures.append(index)

    denominator_failures = {
        'reduced': check_denominators(reduced, claimed),
        'original': check_denominators(original, claimed),
    }
    prefactor_count, prefactor_failures = check_prefactors(reduced, prefactors)
    _, original_prefactor_failures = check_prefactors(original, prefactors)

    rng = random.Random(20261010)
    moment_sample = [(carrier, subset) for carrier in range(1, 5) for subset in range(16)]
    # The reported sample is this fixed draw; the full 64-row table is checked too.
    reported_moment_sample = rng.sample(moment_sample, 8)
    moment_checked, moment_failures = check_moments(features, moment_sample)
    sample_checked, sample_failures = check_moments(features, reported_moment_sample)

    all_masks = list(product(range(16), repeat=3))
    all_codes = list(range(256))
    reported_codes = rng.sample(all_codes, 32)
    full_incidences, full_mask_failures = check_masks(all_codes, all_masks)
    sample_incidences, sample_mask_failures = check_masks(reported_codes, all_masks)
    # Also classify 128 individually drawn triples on codes outside the structural identity.
    drawn = []
    drawn_failures = 0
    for _ in range(128):
        code = rng.randrange(256)
        mask = tuple(rng.randrange(16) for _ in range(3))
        left = mask in mask_membership_by_coordinate(code, [mask])
        right = mask in mask_membership_by_moment_product(code, [mask])
        drawn.append({'code': code, 'mask': mask, 'agree': left == right, 'inside': left})
        drawn_failures += int(left != right)

    cross_count, cross_failures, gamma_delta_ev = cross_check(original, reduced)
    if args.carrier:
        inverse_count, inverse_failures = expand_inverses(json.loads(args.carrier.read_text()), seeds)
    else:
        inverse_count, inverse_failures = 0, []

    report = {
        'tagFormulaMismatches': tag_failures,
        'reducedDenominatorFailures': denominator_failures['reduced'],
        'originalDenominatorTiesThatDiffer': len(denominator_failures['original']),
        'prefactorIdentitiesOnReducedModel': prefactor_count,
        'prefactorFailuresReduced': prefactor_failures,
        'originalPrefactorRowsThatDiffer': len(original_prefactor_failures),
        'crossIdentities': cross_count,
        'crossFailures': cross_failures,
        'gammaDeltaEvUnchanged': gamma_delta_ev,
        'embeddedReducedModelMatchesEmission': embedded_matches_emission,
        'momentRowsChecked': moment_checked,
        'momentFailures': moment_failures,
        'momentSample': reported_moment_sample,
        'momentSampleFailures': sample_failures,
        'momentSampleChecked': sample_checked,
        'maskCodesChecked': 256,
        'maskTriples': 4096,
        'maskIncidences': full_incidences,
        'maskFailures': full_mask_failures,
        'maskSampleCodes': reported_codes,
        'maskSampleIncidences': sample_incidences,
        'maskSampleFailures': sample_mask_failures,
        'drawnTripleFailures': drawn_failures,
        'drawnTriples': drawn[:8],
        'inverseChecks': inverse_count,
        'inverseFailures': inverse_failures,
        'rngSeed': 20261010,
    }
    print(json.dumps(report, indent=2))
    # Unreduced chart polynomials are larger than the cancelled tag products.
    # That gap is the content of the 1,710 cross-multiplications, not a reduced-model failure.
    hard = (
        tag_failures
        or denominator_failures['reduced']
        or prefactor_failures
        or cross_failures
        or not gamma_delta_ev
        or embedded_matches_emission is False
        or moment_failures
        or sample_failures
        or full_mask_failures
        or sample_mask_failures
        or drawn_failures
        or inverse_failures
    )
    if hard:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
