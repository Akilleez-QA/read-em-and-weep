#!/usr/bin/env python3
"""Verify every homogeneous primitive's carrier-owned denominator allocation."""
import argparse
import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
MODEL_SHA256 = 'b6b532c4bab5787397a4cddde34210c12fae71853b30cb73ecbe8a9c2b4826b2'


def verify(model, seeds):
    encoded = json.dumps(model, separators=(',', ':')).encode()
    if hashlib.sha256(encoded).hexdigest() != MODEL_SHA256:
        raise ValueError('Unexpected model')
    if len(seeds) != len(model['charts']):
        raise ValueError('Seed chart count')
    v = s.symbols('v0:5')

    def degree(poly):
        return max((sum(map(int, key.split(','))) for key, _ in poly), default=0)

    def homogeneous(poly, d):
        out = 0
        for key, coefficient in poly:
            powers = tuple(map(int, key.split(',')))
            if d < sum(powers):
                raise ValueError('Negative homogenizing exponent')
            out += coefficient * v[0] ** (d - sum(powers)) * s.prod(
                v[i + 1] ** e for i, e in enumerate(powers))
        return s.sympify(out)

    count = 0
    zeros = 0
    maxima = []
    for owner, chart in enumerate(model['charts']):
        factors = ([v[owner], v[owner] ** 4 - s.prod(v[k] for k in range(5) if k != owner)]
                   if owner < 5 else [v[0], v[1], v[3], v[4]])
        maximum = [0] * len(factors)
        for name, denominator_key in [('I', 'di'), ('P', 'dp'), ('H0', 'dh'), ('H1', 'dh')]:
            matrix = chart[name]
            if len(seeds[owner][name]) != len(matrix):
                raise ValueError('Seed row count')
            denominator = chart[denominator_key]
            d = degree(denominator)
            for i, row in enumerate(matrix):
                if len(seeds[owner][name][i]) != len(row):
                    raise ValueError('Seed column count')
                for j, polynomial in enumerate(row):
                    exponents = seeds[owner][name][i][j]
                    if not polynomial:
                        if exponents is not None:
                            raise ValueError('Nonzero seed for zero entry')
                        zeros += 1
                        continue
                    if (not isinstance(exponents, list) or len(exponents) != len(factors)
                            or any(type(e) is not int or e < 0 for e in exponents)):
                        raise ValueError('Invalid denominator exponents')
                    weight = ([0, 1][j] if name == 'I' else [0, -1][i] if name == 'P' else -1)
                    extra = max(0, degree(polynomial) - d - weight)
                    numerator = homogeneous(polynomial, d + extra + weight)
                    divisor = v[0] ** extra * homogeneous(denominator, d)
                    clearing = s.prod(factor ** e for factor, e in zip(factors, exponents))
                    cleared = s.cancel(clearing * numerator / divisor)
                    # A polynomial over Q, rather than a rational function, is the certificate.
                    s.Poly(cleared, *v, domain=s.QQ)
                    maximum = [max(a, b) for a, b in zip(maximum, exponents)]
                    count += 1
        maxima.append(maximum)
    if count != 451:
        raise ValueError('Unexpected nonzero primitive count')
    return {'status': 'PASS', 'modelCanonicalSHA256': MODEL_SHA256,
            'nonzeroHomogeneousEntries': count, 'zeroEntriesChecked': zeros,
            'carrierFactorMaxima': maxima,
            'factorOwnership': 'primary j: (v_j,F_j); auxiliary: (v_0,v_1,v_3,v_4)',
            'minimalityClaimed': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model', type=Path, default=ROOT / 'data/model.json')
    parser.add_argument('--seeds', type=Path, default=ROOT / 'data/divisor-seeds.json')
    args = parser.parse_args()
    print(json.dumps(verify(json.loads(args.model.read_text()), json.loads(args.seeds.read_text())), indent=2))
