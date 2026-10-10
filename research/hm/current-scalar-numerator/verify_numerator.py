#!/usr/bin/env python3
"""Regenerate the exact current-L scalar numerator in a fresh workspace.

Python 3.10+, Node.js 18+, standard libraries only. Run without Python -O.
The sibling source-bridge package from PR #35 is an explicit dependency.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
from check_source_inputs import (verify_tags_and_inverses, verify_denominators,
                                 verify_prefactors, verify_moments, verify_mask_coverage)

if sys.flags.optimize:
    raise RuntimeError('Run assertion-enabled Python, without -O')
ROOT = Path(__file__).resolve().parent
EXPECTED = json.loads((ROOT/'expected.json').read_text())
sha = lambda data: hashlib.sha256(data).hexdigest()


def run_node(script, *args, stdout=subprocess.PIPE):
    return subprocess.run(['node', '--max-old-space-size=1536', str(script), *map(str, args)],
                          stdout=stdout, stderr=subprocess.PIPE, check=True, timeout=300).stdout


def validate_numerator(raw, seeds):
    pin = EXPECTED['numerator']
    assert sha(raw) == pin['sha256'], 'Numerator byte hash mismatch'
    assert len(raw) == pin['bytes']
    dag = json.loads(raw)
    assert len(dag['nodes']) == dag['retainedNodes'] == pin['nodes']
    assert dag['allNodes'] == dag['allPolynomialNodes'] == pin['allNodes']
    for i, node in enumerate(dag['nodes']):
        if node[0] in ('add', 'mul'):
            assert len(node) == 3
            assert all(type(k) is int and 0 <= k < i for k in node[1:])
        elif node[0] == 'const':
            assert len(node) == 3 and int(node[2]) > 0
            from math import gcd
            assert gcd(int(node[1]), int(node[2])) == 1
        else:
            assert node[0] == 'tags' and len(node) == 17
            assert all(type(e) is int and e >= 0 for e in node[1:])
    assert dag['outputs'] == pin['outputs']
    assert dag['sourceTail'] == [2, 3, 4] and dag['sourceUnsigned'] is True
    assert dag['sourceCoefficientSHA256'] == EXPECTED['carrierDAG']['sha256']
    assert dag['coefficientField'] == 'Q'
    assert dag['explicitScalarJ2MinusCount'] == 1
    assert dag['featureCodes'] == 256 and dag['nonzeroFeatureMoments'] == 242
    assert dag['all4096MaskChoicesRetainedByExactMoments'] is True
    assert dag['carrierDenominatorOrders'] == [13, 14, 14, 14]
    assert dag['remainingDenominatorTags'] == []
    assert all(e >= 0 for e in dag['numeratorTagPowers'])
    assert dag['tagNames'] == seeds['tag_names'] and dag['tagPolynomials'] == seeds['tags']
    assert dag['coefficientExtractionPerformed'] is False
    return pin


def reproduce(bridge, workspace):
    for name, digest in EXPECTED['files'].items():
        assert sha((ROOT/name).read_bytes()) == digest, ('Package input pin', name)
    bridge_expected = json.loads((bridge/'expected.json').read_text())
    for name, digest in EXPECTED['bridgeFiles'].items():
        assert sha((bridge/name).read_bytes()) == digest, ('PR35 dependency pin', name)
    assert bridge_expected['coefficientDAG'] == EXPECTED['carrierDAG']
    # Run the dependency's complete primitive/model/generator bridge first.
    p = subprocess.run([sys.executable, '-B', str(bridge/'verify_bridge.py')],
                       check=True, capture_output=True, timeout=900)
    bridge_report = json.loads(p.stdout)
    assert bridge_report['status'] == 'PASS'
    assert bridge_report['primitiveIdentities'] == 1710
    model_raw = run_node(bridge/'public_reduce_hm_primitive_factors.js', '--emit-model')
    assert sha(model_raw) == EXPECTED['reducedModelSHA256']
    model = json.loads(model_raw)
    (workspace/'reduced-model.json').write_bytes(model_raw)
    carrier_path = workspace/'carriers-234.json'
    with carrier_path.open('xb') as stream:
        run_node(bridge/'public_generate_hm_mask_coefficients_reduced.js',
                 '--carriers', '[2,3,4]', '--emit-dag', stdout=stream)
    carrier_raw = carrier_path.read_bytes()
    assert sha(carrier_raw) == EXPECTED['carrierDAG']['sha256']
    assert len(carrier_raw) == EXPECTED['carrierDAG']['bytes']
    carrier = json.loads(carrier_raw)
    read = lambda name: json.loads((ROOT/name).read_text())
    seeds = read('inverse_seeds.json')
    assert seeds['files']['carriers-234.json']['sha256'] == sha(carrier_raw)
    checks = verify_tags_and_inverses(seeds, carrier)
    checks.update(verify_denominators(model, seeds, read('model_denominators.json')))
    checks.update(verify_prefactors(model, read('public_hm_scalar_prefactors.json')))
    checks.update(verify_moments(read('feature-moments.json')))
    basis = json.loads(run_node(ROOT/'print_mask_basis.js'))
    checks.update(verify_mask_coverage(basis))
    fixtures = json.loads(run_node(ROOT/'test_constructor.js'))
    assert fixtures['status'] == 'PASS' and fixtures['scalarJ2MinusCallsPerFixture'] == 1
    run_node(ROOT/'build_local_representative.js', '--source', carrier_path,
             '--output-dir', workspace/'numerator')
    raw = (workspace/'numerator'/'local-numerator.dag.json').read_bytes()
    pin = validate_numerator(raw, seeds)
    result = {'status': 'PASS', 'coefficientField': 'Q',
              'bridgePrimitiveIdentities': bridge_report['primitiveIdentities'],
              'exactSourceInputChecks': checks, 'constructorFixtures': fixtures,
              'carrierDAGRegenerated': True, 'numeratorRegenerated': True,
              'numerator': pin, 'sourceAttribution': 'Exact algebraic input identities checked; '
              'geometric comparison and pole hypotheses are separate proofs.',
              'scalarCoordinatesEvaluated': False, 'fullObstructionDetermined': False}
    (workspace/'verification.json').write_text(json.dumps(result, indent=2)+'\n')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bridge', type=Path, default=ROOT.parent/'current-scalar-source-bridge',
                        help='PR #35 source-bridge folder (default: public sibling path)')
    parser.add_argument('--output-dir', type=Path,
                        help='retain generated files in this new, nonexistent directory')
    args = parser.parse_args()
    bridge = args.bridge.resolve()
    if not (bridge/'verify_bridge.py').is_file():
        parser.error('PR #35 source bridge is required; pass --bridge PATH')
    if args.output_dir:
        workspace = args.output_dir.resolve()
        workspace.mkdir()  # exclusive; never overwrite an existing result
        result = reproduce(bridge, workspace)
    else:
        with tempfile.TemporaryDirectory(prefix='hm-current-scalar-numerator-') as tmp:
            result = reproduce(bridge, Path(tmp))
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
