#!/usr/bin/env python3
"""Positive reproduction plus deliberate corruptions; never edits package inputs."""
import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
from check_source_inputs import (verify_tags_and_inverses, verify_denominators,
                                 verify_prefactors, verify_moments, verify_mask_coverage)
from verify_numerator import ROOT, reproduce, validate_numerator, run_node


def rejected(call, label):
    try:
        call()
    except (AssertionError, ValueError, KeyError):
        return label
    raise AssertionError('Corruption was accepted: '+label)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--bridge', type=Path, default=ROOT.parent/'current-scalar-source-bridge')
    args = p.parse_args()
    read = lambda n: json.loads((ROOT/n).read_text())
    with tempfile.TemporaryDirectory(prefix='hm-numerator-negative-tests-') as tmp:
        work = Path(tmp)
        reproduce(args.bridge.resolve(), work)
        model = json.loads((work/'reduced-model.json').read_text())
        dag = json.loads((work/'carriers-234.json').read_text())
        seeds, den = read('inverse_seeds.json'), read('model_denominators.json')
        pref, features = read('public_hm_scalar_prefactors.json'), read('feature-moments.json')
        basis = json.loads(run_node(ROOT/'print_mask_basis.js'))
        cases = []
        bad = deepcopy(seeds); bad['tags'][0][0][1] = '2'
        cases.append(rejected(lambda: verify_tags_and_inverses(bad, dag), 'tag formula'))
        bad = deepcopy(seeds); bad['files']['carriers-234.json']['inverse_nodes']['315']['coefficient'] = '1'
        cases.append(rejected(lambda: verify_tags_and_inverses(bad, dag), 'inverse factor sign'))
        bad = deepcopy(seeds); del bad['files']['carriers-234.json']['inverse_nodes']['315']
        cases.append(rejected(lambda: verify_tags_and_inverses(bad, dag), 'missing inverse seed'))
        bad = deepcopy(den); bad[1]['di']['coefficient'] = '1'
        bad_seeds = deepcopy(seeds); bad_seeds['model_denominators'] = bad
        cases.append(rejected(lambda: verify_denominators(model, bad_seeds, bad), 'model denominator tie'))
        bad = deepcopy(pref); bad['aNumerators'][0][0][1] *= -1
        cases.append(rejected(lambda: verify_prefactors(model, bad), 'a prefactor sign'))
        bad = deepcopy(pref); bad['bNumerators'].reverse()
        cases.append(rejected(lambda: verify_prefactors(model, bad), 'b prefactor order'))
        bad = deepcopy(features); bad['moments']['2'][1]['topCoefficient'][0][1] += 1
        cases.append(rejected(lambda: verify_moments(bad), 'moment coefficient'))
        bad = deepcopy(features); bad['moments']['3'][0]['identity'] = False
        cases.append(rejected(lambda: verify_moments(bad), 'empty moment identity'))
        bad = deepcopy(basis); bad[1] = [0, 1, 0]
        cases.append(rejected(lambda: verify_mask_coverage(bad), 'carrier feature assignment'))
        bad = deepcopy(basis); bad.pop()
        cases.append(rejected(lambda: verify_mask_coverage(bad), 'omitted feature code'))
        raw = (work/'numerator'/'local-numerator.dag.json').read_bytes()
        cases.append(rejected(lambda: validate_numerator(raw+b'\n', seeds), 'nonmatching numerator bytes'))
        before = {q.name: hashlib.sha256(q.read_bytes()).hexdigest() for q in (work/'numerator').iterdir()}
        result = subprocess.run(['node', str(ROOT/'build_local_representative.js'),
                                 '--source', str(work/'carriers-234.json'),
                                 '--output-dir', str(work/'numerator')], capture_output=True, timeout=30)
        assert result.returncode != 0
        after = {q.name: hashlib.sha256(q.read_bytes()).hexdigest() for q in (work/'numerator').iterdir()}
        assert before == after
        cases.append('existing output directory preserved')
    print(json.dumps({'status': 'PASS', 'freshFullReproduction': True,
                      'corruptionsAndUnsafeOverwriteRejected': cases}, indent=2))


if __name__ == '__main__':
    main()
