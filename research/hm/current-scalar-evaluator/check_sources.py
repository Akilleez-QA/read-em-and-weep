#!/usr/bin/env python3
"""Check all 24 portable input contracts without evaluating source polynomials."""
import argparse
from itertools import permutations
import json
from pathlib import Path
import tempfile
import evaluate_quotient as E


def check(sources):
    sources = Path(sources).resolve()
    checked = []
    with tempfile.TemporaryDirectory(prefix='hm-contract-check-') as temp:
        config = Path(temp) / 'config.json'
        for roles in permutations(range(4)):
            pair = ''.join(map(str, roles[:2]))
            directory = sources / 'pairs' / ('pair-' + pair)
            config.write_text(json.dumps({'roles': list(roles),
                'input': str(directory / 'graded-jet.compact.json'),
                'clearingMetadata': str(directory / 'integer-clearing.json'),
                'outputDirectory': 'unused-output'}) + '\n')
            cfg, d, k, contract = E.contract_and_inputs(config)
            checked.append({'roles': list(roles), 'sourceNodes': len(d['sumNodes']),
                            'commonDenominator': k['root']['denominator']})
    return {'status': 'PASS', 'contracts': checked, 'actualSourceNodesEvaluated': 0}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--sources', required=True)
    print(json.dumps(check(parser.parse_args().sources), indent=2))
