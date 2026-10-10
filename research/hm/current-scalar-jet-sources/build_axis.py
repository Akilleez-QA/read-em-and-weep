#!/usr/bin/env python3
"""Regenerate one axis, its three ordered compact jets and clearing metadata."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

if sys.flags.optimize:
    raise RuntimeError('Run assertion-enabled Python, without -O')

from build_compact_secondary_jet import build as compact_build
from build_clearing import build as clearing_build
from verify_support import verify as support_verify

HERE = Path(__file__).resolve().parent
PINS = json.loads((HERE / 'pins.json').read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    with path.open('x') as stream:
        stream.write(json.dumps(value, separators=(',', ':')) + '\n')


def check_pin(path, expected):
    digest = sha(path)
    if digest != expected:
        raise ValueError(f'Pin mismatch: {path.name}: {digest} != {expected}')
    return {'sha256': digest, 'bytes': path.stat().st_size}


def compact_metadata(first, second, normalized_sha):
    metadata = {'sourceSHA256': normalized_sha}
    if first == 3:
        metadata.update({'targetFamily': 'nonvacuous46_scalar_coordinates',
                         'allHomogeneousDegreesRetainedSeparately': True,
                         'pairingMonomialApplied': False, 'sourceTotalDegreeFilterApplied': False})
    else:
        metadata.update({'sourceTotalDegreeConstraint': 413,
                         'factoredSourceTotalDegreeConstraint': 269,
                         'sourceOriginalTotalDegreeConstraint': 685,
                         'pairingMonomial': [2, 2, 2, 0],
                         'gradedOutputs': [{'polynomialOutput': r,
                                           'operator': 'exact_homogeneous_projection',
                                           'remainingTotalDegree': 105 + r,
                                           'sourceFirstDegree': 272,
                                           'sourceSecondDegree': 212 - r,
                                           'sourceOriginalTotalDegree': 685} for r in range(6)]})
        if (first, second) == (0, 1):
            metadata['queryEdges'] = [{'roles': [0, 1, 2, 3],
                                       'maximumBExponent': 21, 'permutationSign': 1}]
    return metadata


def run_axis(numerator, ring, output, axis, timeout):
    started = time.monotonic()
    pin = PINS['axes'][str(axis)]
    if sha(numerator) != PINS['numeratorSHA256']:
        raise ValueError('Exact numerator pin mismatch')
    (output / 'axes').mkdir(exist_ok=True)
    leading = output / 'axes' / f'axis-{axis}.dag.json'
    normalized = output / 'axes' / f'axis-{axis}.normalized.json'
    subprocess.run(['node', '--max-old-space-size=1024', str(HERE / 'build_leading_source.js'),
                    str(numerator), str(leading), str(axis), str(ring)], check=True, timeout=timeout)
    subprocess.run([sys.executable, str(HERE / 'normalize_free_tags.py'), str(leading), '64',
                    '--concrete-tags', '--input-label', pin['normalizedInputLabel'],
                    '--export', str(normalized)], check=True, timeout=timeout)
    leading_result = check_pin(leading, pin['leadingSHA256'])
    normalized_result = check_pin(normalized, pin['normalizedSHA256'])
    N = json.loads(normalized.read_text())
    support = support_verify(N, axis)
    if support['rootSupports'] != pin['rootSupports']:
        raise ValueError('Support enclosure does not match the sealed reference')
    if len(N['sumNodes']) != pin['normalizedSumSymbols']:
        raise ValueError('Unexpected normalized sum-symbol count')
    write_json(output / 'axes' / f'axis-{axis}.support.json', support)
    pairs = {}
    for second in range(4):
        if second == axis:
            continue
        pair = f'{axis}{second}'
        pair_start = time.monotonic()
        directory = output / 'pairs' / f'pair-{pair}'
        directory.mkdir(parents=True, exist_ok=False)
        compact = directory / 'graded-jet.compact.json'
        clearing = directory / 'integer-clearing.json'
        C = compact_build(N, axis=second, K=6, first=axis)
        C.update(compact_metadata(axis, second, normalized_result['sha256']))
        write_json(compact, C)
        compact_result = check_pin(compact, PINS['pairs'][pair]['compactSHA256'])
        R = clearing_build(N, C, normalized_result['sha256'], compact_result['sha256'])
        write_json(clearing, R)
        clearing_result = check_pin(clearing, PINS['pairs'][pair]['clearingSHA256'])
        pairs[pair] = {'compact': compact_result, 'clearing': clearing_result,
                       'elapsedSeconds': round(time.monotonic() - pair_start, 3)}
        print(json.dumps({'pair': pair, 'exactPinsMatch': True,
                          'elapsedSeconds': pairs[pair]['elapsedSeconds']}), flush=True)
    result = {'axis': axis, 'leading': leading_result, 'normalized': normalized_result,
              'supportVerified': True, 'pairs': pairs,
              'elapsedSeconds': round(time.monotonic() - started, 3)}
    write_json(output / 'axes' / f'axis-{axis}.receipt.json', result)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--numerator', type=Path, required=True)
    parser.add_argument('--tagged-ring', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--axis', type=int, choices=range(4), required=True)
    parser.add_argument('--stage-timeout', type=int, default=120)
    args = parser.parse_args()
    run_axis(args.numerator.resolve(), args.tagged_ring.resolve(), args.output_dir.resolve(),
             args.axis, args.stage_timeout)
