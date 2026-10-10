#!/usr/bin/env python3
"""Conservative exact support induction on a normalized polynomial circuit."""

def verify(normalized, axis):
    if axis not in range(4) or normalized['coefficientField'] != 'Q':
        raise ValueError('Expected an axis 0..3 and an exact Q source')
    bounds = []
    for j in range(16):
        exponent = [int(i == j) for i in range(4)]
        bounds.append((exponent, exponent, 1, 1) if j < 4 else None)

    def product(factors):
        lo, hi, total_lo, total_hi = [0] * 4, [0] * 4, 0, 0
        for j, e in factors:
            if j == axis or not (j < 4 or j >= 16) or e < 0:
                raise ValueError('Nonpolynomial or eliminated-coordinate factor')
            a, b, c, d = bounds[j]
            lo = [x + e * y for x, y in zip(lo, a)]
            hi = [x + e * y for x, y in zip(hi, b)]
            total_lo += e * c
            total_hi += e * d
        return lo, hi, total_lo, total_hi

    for terms in normalized['sumNodes']:
        choices = [product(f) for c, f in terms if int(c[0])]
        if not choices:
            raise ValueError('Empty normalized sum')
        bounds.append(([min(x[0][k] for x in choices) for k in range(4)],
                       [max(x[1][k] for x in choices) for k in range(4)],
                       min(x[2] for x in choices), max(x[3] for x in choices)))
    roots = []
    for output in normalized['outputs']:
        lo, hi, lower, upper = product(output['factors'])
        roots.append({'coordinateMinimum': lo, 'coordinateMaximum': hi,
                      'totalMinimum': lower, 'totalMaximum': upper})
    other = [j for j in range(4) if j != axis]
    factors = dict(normalized['outputs'][1]['factors'])
    exposed = {str(j): factors.get(j, 0) for j in other}
    if not (all(exposed[str(j)] == 48 for j in other)
            and all(roots[1]['coordinateMaximum'][j] <= 212 for j in other)
            and roots[1]['totalMaximum'] <= 449):
        raise ValueError('Required support/coordinate-factor enclosure failed')
    return {'axis': axis, 'field': 'Q', 'rootSupports': roots,
            'exactExposedCoordinateFactors': exposed,
            'factoredCoordinateUpperBound': 164, 'factoredTotalUpperBound': 305,
            'degree273VanishingProved': False, 'polynomialCoefficientsEvaluated': False}
