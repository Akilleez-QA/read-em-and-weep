#!/usr/bin/env python3
"""Independent support enclosure and integer-clearing sample.

Reads a regeneration directory produced by current-scalar-jet-sources.
Does not import that package. Large generated files are not committed.
"""
import argparse
import json
import math
from fractions import Fraction
from pathlib import Path


def enclosure(normalized):
    bounds = []
    for j in range(16):
        if j < 4:
            exp = [int(i == j) for i in range(4)]
            bounds.append((exp, exp[:], 1, 1))
        else:
            bounds.append(None)

    def product(factors):
        lo, hi, total_lo, total_hi = [0] * 4, [0] * 4, 0, 0
        for j, exponent in factors:
            a, b, c, d = bounds[j]
            lo = [x + exponent * y for x, y in zip(lo, a)]
            hi = [x + exponent * y for x, y in zip(hi, b)]
            total_lo += exponent * c
            total_hi += exponent * d
        return lo, hi, total_lo, total_hi

    for terms in normalized['sumNodes']:
        choices = [product(factors) for coef, factors in terms if int(coef[0])]
        bounds.append((
            [min(item[0][k] for item in choices) for k in range(4)],
            [max(item[1][k] for item in choices) for k in range(4)],
            min(item[2] for item in choices),
            max(item[3] for item in choices),
        ))
    roots = []
    for output in normalized['outputs']:
        lo, hi, lower, upper = product(output['factors'])
        roots.append({
            'coordinateMinimum': lo,
            'coordinateMaximum': hi,
            'totalMinimum': lower,
            'totalMaximum': upper,
        })
    return roots


def clearing_report(normalized, compact):
    denominators = {j: 1 for j in range(4)}

    def alpha(coefficient, factors):
        result = Fraction(int(coefficient[0]), int(coefficient[1]))
        for symbol, exponent in factors:
            result /= denominators[symbol] ** exponent
        return result

    for k, terms in enumerate(normalized['sumNodes']):
        denominators[k + 16] = math.lcm(*(alpha(coef, factors).denominator for coef, factors in terms))
    nonintegral = 0
    checked = 0
    for node in compact['sumNodes']:
        denominator = denominators[node['sourceSymbol']]
        for coefficient, _shift, factors in node['terms']:
            value = denominator * alpha(coefficient, factors)
            checked += 1
            nonintegral += value.denominator != 1
    root = alpha(compact['root']['coefficient'], compact['root']['factors'])
    weight = root.denominator * root
    return {
        'terms': checked,
        'nonintegral': nonintegral,
        'rootDenominator': str(root.denominator),
        'rootWeight': str(weight.numerator) if weight.denominator == 1 else 'NONINTEGRAL',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--jets', type=Path, required=True)
    parser.add_argument('--pins', type=Path, required=True)
    parser.add_argument('--pairs', default='01,10,30')
    args = parser.parse_args()
    pins = json.loads(args.pins.read_text())
    axes = []
    for axis in range(4):
        normalized = json.loads((args.jets / 'axes' / f'axis-{axis}.normalized.json').read_text())
        roots = enclosure(normalized)
        other = [j for j in range(4) if j != axis]
        factors = dict(normalized['outputs'][1]['factors'])
        axes.append({
            'axis': axis,
            'matchesPin': roots == pins['axes'][str(axis)]['rootSupports'],
            'exposed': {str(j): factors.get(j, 0) for j in other},
            'sharpFactoredCoordinate': max(roots[1]['coordinateMaximum'][j] for j in other) - 48,
            'sharpFactoredTotal': roots[1]['totalMaximum'] - 3 * 48,
        })
    pairs = []
    for pair in args.pairs.split(','):
        axis = int(pair[0])
        normalized = json.loads((args.jets / 'axes' / f'axis-{axis}.normalized.json').read_text())
        compact = json.loads((args.jets / 'pairs' / f'pair-{pair}' / 'graded-jet.compact.json').read_text())
        got = clearing_report(normalized, compact)
        got['pair'] = pair
        got['pinRoot'] = pins['pairs'][pair]['root']
        pairs.append(got)
    report = {'axes': axes, 'clearing': pairs}
    print(json.dumps(report, indent=2))
    if any(not row['matchesPin'] or row['sharpFactoredCoordinate'] != 164 or row['sharpFactoredTotal'] != 305
           for row in axes):
        raise SystemExit(1)
    if any(row['nonintegral'] or row['rootDenominator'] != row['pinRoot']['denominator']
           or row['rootWeight'] != row['pinRoot']['integerWeight'] for row in pairs):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
