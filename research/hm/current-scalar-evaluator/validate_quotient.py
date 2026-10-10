#!/usr/bin/env python3
"""Validate exact result and reconstruct its terminal multiplication with Fractions."""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys
import exact_oracle as O
import evaluate_quotient as E

if sys.flags.optimize:
    raise RuntimeError('Assertion-enabled Python is required')


def validate(config_path, expected=True):
    cfg, d, k, contract = E.contract_and_inputs(config_path)
    out = Path(cfg['outputDirectory'])
    q = json.loads((out / 'quotient.json').read_text())
    state = E.decode_checkpoint((out / 'checkpoint.json').read_bytes())
    canonical = lambda obj: json.dumps(obj, sort_keys=True, separators=(',', ':'))
    assert canonical(q['contract']) == canonical(state['contract']) == canonical(contract)
    assert q['schema'] == 'hm-exact-Q-full-quotient-v1'
    assert q['status'] == 'EXACT_FULL_QUOTIENT_EXPORTED'
    assert q['field'] == 'Q'
    assert type(q['roles']) is list and len(q['roles']) == 4
    assert all(type(role) is int for role in q['roles']) and q['roles'] == contract['roles']
    assert type(q['quotientShape']) is list and all(type(n) is int for n in q['quotientShape'])
    assert q['quotientShape'] == [6, 37, 22]
    assert q['homogeneousDegreesRemainSeparated'] is True and q['pairingAggregated'] is False
    assert state['reason'] == 'finished' and state['nextIndex'] == len(d['sumNodes'])
    assert q['commonDenominator'] == k['root']['denominator']
    assert state['rootDenominator'] == int(k['root']['denominator'])
    assert state['denominatorMetadataSHA256'] == cfg['clearingMetadataSHA256']
    rows = q['integerQuotientCoefficients']
    assert type(q['retainedNonzeros']) is int
    assert rows == sorted(rows) and len(rows) == q['retainedNonzeros']
    assert len({tuple(row[:3]) for row in rows}) == len(rows)
    assert all(len(row) == 4 and all(type(x) is int for x in row[:3])
               and all(0 <= x < bound for x, bound in zip(row[:3], (6, 37, 22)))
               and type(row[3]) is str and str(int(row[3])) == row[3] and int(row[3]) for row in rows)
    digest = hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()
    assert digest == q['integerCoefficientSHA256']
    terminal = {(0, 0, 0): F(1)}
    for symbol, power in d['root']['factors']:
        poly = {(index % 11, (index // 11) % 73, index // 803): F(c)
                for index, c in state['vals'][symbol].items()}
        terminal = O.mul(terminal, O.power(poly, power))
    factor = F(int(k['root']['integerWeight']), int(k['root']['denominator']))
    shift = d['root']['reverseShift']
    terminal = {(r + shift, w, z): c * factor for (r, w, z), c in terminal.items() if r + shift < 6}
    terminal = {key: c for key, c in terminal.items() if c}
    actual = {tuple(row[:3]): F(int(row[3]), int(q['commonDenominator'])) for row in rows}
    assert actual == terminal, 'Independent Fraction terminal mismatch'
    if expected:
        pin = E.PINS['expectedQuotients'][''.join(map(str, contract['roles']))]
        assert {key: q[key] for key in pin} == pin, 'Historical exact quotient mismatch'
    return {'status': 'PASS', 'field': 'Q', 'roles': contract['roles'],
            'integerCoefficientSHA256': digest, 'retainedNonzeros': len(rows),
            'independentFractionTerminalMatched': True,
            'historicalExactCoefficientHashMatched': expected,
            'scope': 'Source quotient and terminal product only; no scalar coordinate selected.'}


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True)
    print(json.dumps(validate(parser.parse_args().config), indent=2))
