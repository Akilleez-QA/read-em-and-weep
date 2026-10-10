#!/usr/bin/env python3
"""Exact per-symbol denominator clearing; does not evaluate polynomials."""
import math
from fractions import Fraction


def build(normalized, compact, normalized_sha, compact_sha):
    if normalized['coefficientField'] != 'Q' or compact['coefficientField'] != 'Q':
        raise ValueError('Exact Q inputs required')
    if compact['sourceSHA256'] != normalized_sha:
        raise ValueError('Compact source does not bind to normalized input')
    denominators = {j: 1 for j in range(4)}

    def alpha(coefficient, factors):
        result = Fraction(int(coefficient[0]), int(coefficient[1]))
        for symbol, exponent in factors:
            if not (symbol < 4 or symbol >= 16) or exponent < 0:
                raise ValueError('Only nonnegative coordinate/sum factors are supported')
            result /= denominators[symbol] ** exponent
        return result

    for k, terms in enumerate(normalized['sumNodes']):
        denominators[k + 16] = math.lcm(*(alpha(c, f).denominator for c, f in terms))
    rows = []
    for node in compact['sumNodes']:
        symbol = node['sourceSymbol']
        denominator = denominators[symbol]
        weights = []
        for coefficient, shift, factors in node['terms']:
            value = denominator * alpha(coefficient, factors)
            if value.denominator != 1:
                raise ValueError('Nonintegral cleared weight')
            weights.append(str(value.numerator))
        rows.append({'sourceSymbol': symbol, 'denominator': str(denominator),
                     'integerWeights': weights})
    value = alpha(compact['root']['coefficient'], compact['root']['factors'])
    root_denominator = value.denominator
    root_weight = root_denominator * value
    if root_weight.denominator != 1:
        raise ValueError('Nonintegral cleared root')
    return {'schema': 'hm-exact-Q-per-node-integer-clearing-v1', 'field': 'Q',
            'normalizedSourceSHA256': normalized_sha, 'compactSourceSHA256': compact_sha,
            'nodes': rows,
            'root': {'denominator': str(root_denominator), 'integerWeight': str(root_weight.numerator)},
            'definition': 'Z_j=D_j*F_j; weights=D_node*c/product(D_child^e), checked integral exactly. D_node uses all original normalized terms.',
            'maximumNodeDenominatorBits': max(d.bit_length() for d in denominators.values()),
            'nodeCount': len(rows), 'termCount': sum(len(r['integerWeights']) for r in rows),
            'polynomialCoefficientsEvaluated': False}
