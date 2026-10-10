#!/usr/bin/env python3
"""Read-only exact support and exposed-factor check of a regenerated normalized axis."""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def support(data, axis):
    if type(axis) is not int or axis not in range(4) or data['coefficientField'] != 'Q':
        raise ValueError('Expected an exact-Q axis')
    bounds = {i: ([int(k == i) for k in range(4)], [int(k == i) for k in range(4)], 1, 1)
              for i in range(4) if i != axis}

    def term(coefficient, factors, limit):
        numerator, denominator = map(int, coefficient)
        if denominator <= 0 or Fraction(numerator, denominator) == 0:
            raise ValueError('Zero or invalid rational term')
        if [str(Fraction(numerator, denominator).numerator), str(Fraction(numerator, denominator).denominator)] != coefficient:
            raise ValueError('Noncanonical rational coefficient')
        lo, hi, lower, upper = [0] * 4, [0] * 4, 0, 0
        seen = set()
        for symbol, exponent in factors:
            if (type(symbol) is not int or type(exponent) is not int or exponent < 1
                    or symbol not in bounds or symbol >= limit or symbol in seen):
                raise ValueError('Invalid polynomial factor or topological order')
            seen.add(symbol)
            a, b, c, d = bounds[symbol]
            lo = [u + exponent * v for u, v in zip(lo, a)]
            hi = [u + exponent * v for u, v in zip(hi, b)]
            lower += exponent * c
            upper += exponent * d
        return lo, hi, lower, upper

    for k, terms in enumerate(data['sumNodes']):
        values = [term(c, f, 16 + k) for c, f in terms]
        if not values:
            raise ValueError('Empty sum')
        bounds[16 + k] = ([min(v[0][i] for v in values) for i in range(4)],
                          [max(v[1][i] for v in values) for i in range(4)],
                          min(v[2] for v in values), max(v[3] for v in values))
    output = data['outputs'][1]
    lo, hi, lower, upper = term(output['coefficient'], output['factors'], 16 + len(data['sumNodes']))
    exposed = dict(output['factors'])
    if any(exposed.get(i) != 48 for i in range(4) if i != axis):
        raise ValueError('Missing explicit coordinate factor 48')
    if (lo != [0 if i == axis else 48 for i in range(4)]
            or hi != [0 if i == axis else 212 for i in range(4)] or (lower, upper) != (353, 449)):
        raise ValueError('Unexpected conservative support')
    return {'axis': axis, 'field': 'Q', 'normalizedSumSymbols': len(data['sumNodes']),
            'coordinateLowerBounds': lo, 'coordinateUpperBounds': hi,
            'totalDegreeBounds': [lower, upper],
            'exposedCoordinatePowers': {str(i): exposed[i] for i in range(4) if i != axis},
            'strippedCoordinateUpperBound': 164, 'strippedTotalUpperBound': 305,
            'minimalFactorMultiplicityClaimed': False, 'degree273VanishingChecked': False}


def verify(path, axis):
    pins = json.loads((ROOT / 'pins.json').read_text())['axes'][str(axis)]
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != pins['normalizedSHA256']:
        raise ValueError('Normalized axis hash mismatch')
    data = json.loads(raw)
    if data['inputSHA256'] != pins['leadingSHA256']:
        raise ValueError('Leading axis source mismatch')
    report = support(data, axis)
    return {'status': 'PASS', 'normalizedSHA256': digest, **report}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--axis', type=int, choices=range(4), required=True)
    parser.add_argument('--normalized', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(verify(args.normalized, args.axis), indent=2))
