#!/usr/bin/env python3
"""All model SL2 transition identities by integer polynomial multiplication."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path


def polynomial(encoded):
    result = {}
    for monomial, coefficient in encoded:
        exponent = tuple(map(int, monomial.split(',')))
        if len(exponent) != 4 or min(exponent) < 0 or type(coefficient) is not int:
            raise ValueError('Invalid integer polynomial')
        if exponent in result:
            raise ValueError('Duplicate polynomial exponent')
        if coefficient:
            result[exponent] = coefficient
    return result


def add(a, b, sign=1):
    c = dict(a)
    for e, value in b.items():
        c[e] = c.get(e, 0) + sign * value
    return {e: value for e, value in c.items() if value}


def multiply(a, b):
    c = defaultdict(int)
    for e, value in a.items():
        for f, other in b.items():
            c[tuple(x+y for x,y in zip(e,f))] += value * other
    return {e: value for e, value in c.items() if value}


def verify_model(model):
    if len(model['charts']) != 6:
        raise ValueError('Expected six exact model charts')
    charts = []
    for raw in model['charts']:
        item = {key: [[polynomial(p) for p in row] for row in raw[key]]
                for key in ['I','P']}
        item.update({key: polynomial(raw[key]) for key in ['di','dp']})
        if len(item['I']) != 15 or any(len(r) != 2 for r in item['I']):
            raise ValueError('Bad inclusion dimensions')
        if len(item['P']) != 2 or any(len(r) != 15 for r in item['P']):
            raise ValueError('Bad projection dimensions')
        if not item['di'] or not item['dp']:
            raise ValueError('Zero transition denominator')
        charts.append(item)
    pairs = []
    for i, a in enumerate(charts):
        for j, b in enumerate(charts):
            n = [[{} for _ in range(2)] for _ in range(2)]
            for r in range(2):
                for t in range(2):
                    for k in range(15):
                        n[r][t] = add(n[r][t], multiply(a['P'][r][k], b['I'][k][t]))
            det = add(multiply(n[0][0], n[1][1]), multiply(n[0][1], n[1][0]), -1)
            den = multiply(a['dp'], b['di'])
            if det != multiply(den, den):
                raise ValueError('Determinant identity failed for pair %s' % ((i,j),))
            pairs.append([i,j])
    return {'status':'PASS', 'exactDeterminantOneIdentities':len(pairs),
            'coefficientRing':'Z[v1,v2,v3,v4]', 'orderedPairs':pairs,
            'identity':'det(P_i I_j)=1 after exact denominator cross multiplication',
            'pointSamplesUsedAsProof':False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model', type=Path, required=True)
    args = parser.parse_args()
    raw = args.model.read_bytes()
    result = verify_model(json.loads(raw))
    result['modelSHA256'] = hashlib.sha256(raw).hexdigest()
    print(json.dumps(result, indent=2))
