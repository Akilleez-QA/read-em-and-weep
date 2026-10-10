#!/usr/bin/env python3
"""Exact chart, finite-line, constant-gauge, and section-degree identities."""
import itertools
import json

import sympy as s


def verify():
    checks = []

    def equal(a, b, label):
        if s.cancel(a - b) != 0:
            raise ValueError(label)
        checks.append(label)

    x = s.symbols('x1:5')
    t = s.symbols('t1:5')
    z = s.symbols('z')
    affine = s.Poly(s.prod(1 + q * z for q in x), z)
    equal(affine.nth(0), 1, 'finite v0 = 1')
    for j in range(1, 5):
        ej = sum(s.prod(x[i] for i in subset) for subset in itertools.combinations(range(4), j))
        equal(affine.nth(j), ej, f'finite v{j} = e{j}(x)')
    for mask in range(16):
        tau = s.prod(t[i] for i in range(4) if mask >> i & 1)
        local = s.Poly(s.prod((t[i] + z) if mask >> i & 1 else (1 + x[i] * z)
                             for i in range(4)), z)
        substitution = {x[i]: 1 / t[i] for i in range(4) if mask >> i & 1}
        for j in range(5):
            equal(local.nth(j), tau * affine.nth(j).subs(substitution), f'chart {mask} v{j}')

    q, y, c = s.symbols('q y c')
    line = q * q - 1
    f = q ** 3 - q
    rf = (q * q + 1) / (2 * q * line)
    gamma = 1 / (q * line)
    equal(rf, s.diff(f, q) / (2 * f) - 1 / q, 'physical logarithmic seed')
    cleared = {}
    for name, value in [('rf', rf), ('gamma', gamma), ('overlap', 1 / q)]:
        for derivative in (0, 1):
            polynomial = s.cancel(q ** (derivative + 1) * line ** (derivative + 1)
                                  * s.diff(value, q, derivative))
            s.Poly(polynomial, q, domain=s.QQ)
            equal(s.diff(value, q, derivative), polynomial / (q * line) ** (derivative + 1),
                  f'{name} derivative {derivative} clearance')
            cleared[f'{name}:{derivative}'] = str(s.expand(polynomial))
        equal(s.diff(value, y), 0, f'{name} unrelated derivative')
    C = s.Matrix(2, 2, s.symbols('c0:4'))
    S = s.diag(c, 1 / c)
    difference = S.T * (S * C * S.inv()).T * S.T.inv() - C.T
    for k, entry in enumerate(difference):
        equal(entry, 0, f'constant-gauge transpose cancellation {k}')
    coefficients = s.symbols('a0:6')
    P = sum(coefficients[k] * q ** k * y ** (5 - k) for k in range(6))
    P1 = q ** 3 * (q * q - y * y) * coefficients[5]
    P0 = s.expand(P - P1)
    equal(P0 + P1, P, 'partition sum')
    equal(P0.subs(y, 0), 0, 'bit-zero Y divisibility')
    equal(P1 / (q ** 3 * (q * q - y * y)), coefficients[5], 'bit-one divisibility')
    powers = [13, 14, 14, 14]
    degree = -4 + 1 + 5 * sum(powers)
    if degree != 272:
        raise ValueError('Section-degree arithmetic')
    return {'status': 'PASS', 'exactIdentities': len(checks), 'checks': checks,
            'finiteSeedClearedNumerators': cleared, 'primaryClearingOrders': powers,
            'conditionalRegularSectionDegree': degree,
            'regularityProvedByDegreeArithmeticAlone': False}


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
