#!/usr/bin/env python3
"""Small exact fixtures and rejection tests; no large source generation."""
import copy
import json
from pathlib import Path

from verify_computed_bounds import verify as verify_bounds
from verify_divisor_seeds import verify as verify_seeds
from verify_factor48 import support

ROOT = Path(__file__).resolve().parents[1]


def main():
    passed = []

    def reject(name, operation):
        try:
            operation()
        except (ValueError, KeyError, TypeError, IndexError):
            passed.append(name)
        else:
            raise ValueError('Mutation accepted: ' + name)

    report = json.loads((ROOT / 'certificates/pole-bounds.json').read_text())
    verify_bounds(report)
    changed = copy.deepcopy(report)
    changed['completed'] = {'not_evidence': True}
    if verify_bounds(changed) != verify_bounds(report):
        raise ValueError('Declared completed field used')
    passed.append('declared completed field is not evidence')
    changed = copy.deepcopy(report)
    changed['tailPrimaryJ0'][0] = 12
    reject('changed computed tail', lambda: verify_bounds(changed))
    changed = copy.deepcopy(report)
    changed['q2'].pop()
    reject('missing prefix profile', lambda: verify_bounds(changed))
    changed = copy.deepcopy(report)
    changed['q2'][0]['scalar'][5] = 2
    reject('scalar auxiliary bound too large', lambda: verify_bounds(changed))
    model = json.loads((ROOT / 'data/model.json').read_text())
    seeds = json.loads((ROOT / 'data/divisor-seeds.json').read_text())
    changed = copy.deepcopy(model)
    changed['charts'][0]['pivot'] = 1
    reject('changed model', lambda: verify_seeds(changed, seeds))
    changed = copy.deepcopy(seeds)
    changed[0]['I'][0][0] = [-1, 0]
    reject('negative divisor exponent', lambda: verify_seeds(model, changed))
    changed = copy.deepcopy(seeds)
    changed[0]['I'][0][1] = [0, 0]
    reject('nonzero seed on zero primitive', lambda: verify_seeds(model, changed))

    # A small circuit with the same conservative support envelope as an axis source.
    monomials = [(0, 104, 105), (164, 141, 0), (0, 164, 141), (141, 0, 164)]
    fixture = {'coefficientField': 'Q', 'sumNodes': [
        [[['1', '1'], [[j + 1, e] for j, e in enumerate(es) if e]] for es in monomials]],
        'outputs': [None, {'coefficient': ['1', '1'],
                          'factors': [[1, 48], [2, 48], [3, 48], [16, 1]]}]}
    result = support(fixture, 0)
    if result['strippedTotalUpperBound'] != 305:
        raise ValueError('Fixture support')
    passed.append('exact support and exposed-factor fixture')
    changed = copy.deepcopy(fixture)
    changed['outputs'][1]['factors'][0][1] = 47
    reject('coordinate factor missing one power', lambda: support(changed, 0))
    changed = copy.deepcopy(fixture)
    changed['sumNodes'][0][0][1].append([16, 1])
    reject('self-referential support node', lambda: support(changed, 0))
    changed = copy.deepcopy(fixture)
    changed['sumNodes'][0][0][0] = ['1', '0']
    reject('zero rational denominator', lambda: support(changed, 0))
    print(json.dumps({'status': 'PASS', 'tests': len(passed), 'cases': passed}, indent=2))


if __name__ == '__main__':
    main()
