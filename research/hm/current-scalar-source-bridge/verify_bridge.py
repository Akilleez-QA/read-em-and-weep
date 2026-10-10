#!/usr/bin/env python3
"""Regenerate the reduced model and exact carrier (2,3,4) coefficient DAG.

All source inputs are bundled. Generated data live only in a temporary directory.
No scalar numerator, quotient or obstruction coordinate is evaluated.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

if sys.flags.optimize:
    raise RuntimeError('Run assertion-enabled Python, without -O')
ROOT = Path(__file__).resolve().parent
EXPECTED = json.loads((ROOT / 'expected.json').read_text())
sha = lambda b: hashlib.sha256(b).hexdigest()


def split_model(text):
    before, tail = text.split('const MODEL=', 1)
    model, end = json.JSONDecoder().raw_decode(tail)
    return model, before + 'const MODEL=<MODEL>' + tail[end:]


def run(script, *args):
    return subprocess.run(['node', '--max-old-space-size=1536', str(ROOT / script), *args],
                          check=True, capture_output=True, timeout=300).stdout


def main():
    for name, digest in EXPECTED['files'].items():
        assert sha((ROOT / name).read_bytes()) == digest, name
    reducer = 'public_reduce_hm_primitive_factors.js'
    generator = 'public_generate_hm_mask_coefficients_reduced.js'
    original = 'generate-hm-mask-coefficients-original.js'
    old_model, old_body = split_model((ROOT / original).read_text())
    embedded_old, _ = split_model((ROOT / reducer).read_text())
    reduced_model, reduced_body = split_model((ROOT / generator).read_text())
    assert old_model == embedded_old
    original_model_sha = sha((json.dumps(old_model, separators=(',', ':')) + '\n').encode())
    assert original_model_sha == '9e808b52f263679a548656fa57bcb3a621f5264c20873621208b06acf4003614'
    assert old_body == reduced_body, 'Generator changed beyond the MODEL declaration'
    report = json.loads(run(reducer))
    assert report['identities'] == EXPECTED['primitiveIdentities'] == 1710
    reduced = run(reducer, '--emit-model')
    assert sha(reduced) == EXPECTED['reducedModelSHA256']
    assert json.loads(reduced) == reduced_model
    with tempfile.TemporaryDirectory(prefix='hm-source-bridge-') as tmp:
        target = Path(tmp) / 'carriers-234.json'
        with target.open('wb') as stream:
            subprocess.run(['node', '--max-old-space-size=1536', str(ROOT / generator),
                            '--carriers', '[2,3,4]', '--emit-dag'],
                           stdout=stream, check=True, timeout=300)
        raw = target.read_bytes()
        pin = EXPECTED['coefficientDAG']
        assert len(raw) == pin['bytes'] and sha(raw) == pin['sha256']
        dag = json.loads(raw)
        assert dag['carriers'] == EXPECTED['carriers'] == [2, 3, 4]
        assert dag['variables'] == ['x1', 'x2', 'x3', 'x4']
        assert len(dag['nodes']) == pin['nodes'] == 178251
        for i, node in enumerate(dag['nodes']):
            if node[0] in ('add', 'mul'):
                assert all(type(k) is int and 0 <= k < i for k in node[1:])
            elif node[0] == 'inv':
                assert type(node[1]) is int and 0 <= node[1] < i
            elif node[0] == 'var':
                assert type(node[1]) is int and 0 <= node[1] < 4
            else:
                assert node[0] == 'const'
        assert len(dag['coefficients']) == 2
        for row in dag['coefficients']:
            assert len(row) == 2
            for entries in row:
                assert entries == sorted(entries)
                assert len({code for code, _ in entries}) == len(entries)
                assert all(0 <= code < 256 and 0 <= index < len(dag['nodes']) for code, index in entries)
    print(json.dumps({'status': 'PASS', 'primitiveIdentities': report['identities'],
                      'originalModelSHA256': original_model_sha,
                      'generatorBodyUnchangedOutsideModel': True,
                      'reducedModelSHA256': sha(reduced),
                      'coefficientDAG': pin,
                      'actualCarrierDAGRegenerated': True,
                      'scalarNumeratorRegenerated': False,
                      'scalarCoordinatesEvaluated': False}, indent=2))


if __name__ == '__main__':
    main()
