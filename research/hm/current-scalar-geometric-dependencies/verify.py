#!/usr/bin/env python3
"""Reproduce the bundled geometric-dependency checks from any working directory."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

if sys.flags.optimize:
    raise RuntimeError('Run this verifier with assertion-enabled Python (without -O or -OO).')

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--public-generator', type=Path,
                        help='Optional pinned PR35 generator file for whole-file/excerpt binding')
    args = parser.parse_args()
    manifest = json.loads((ROOT / 'manifest.json').read_text())
    for name, expected in manifest['sha256'].items():
        if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != expected:
            raise ValueError('Package file hash mismatch: ' + name)
    results = {}
    with tempfile.TemporaryDirectory(prefix='scalar-geometric-checks-') as directory:
        def run(name, command):
            completed = subprocess.run(command, cwd=directory, text=True, capture_output=True, timeout=300,
                                       env={**__import__('os').environ, 'PYTHONDONTWRITEBYTECODE': '1'})
            if completed.returncode:
                raise RuntimeError(name + ': ' + completed.stderr)
            results[name] = json.loads(completed.stdout)
            return results[name]

        py = sys.executable
        run('divisor-seeds', [py, str(ROOT / 'checks/verify_divisor_seeds.py')])
        run('homogeneous-identities', [py, str(ROOT / 'checks/verify_homogeneous_identities.py')])
        run('chart-and-lines', [py, str(ROOT / 'checks/verify_chart_and_lines.py')])
        command = [py, str(ROOT / 'checks/verify_source_alignment.py')]
        if args.public_generator is not None:
            command.extend(['--public-generator', str(args.public_generator.resolve())])
        run('source-alignment', command)
        bound = run('pole-bounds', ['node', '--max-old-space-size=512', str(ROOT / 'checks/compute_pole_bounds.js')])
        bound_path = Path(directory) / 'bounds.json'
        bound_path.write_text(json.dumps(bound))
        run('computed-bounds', [py, str(ROOT / 'checks/verify_computed_bounds.py'), str(bound_path)])
        run('fixtures', [py, str(ROOT / 'checks/test_certificates.py')])
    for name in ['divisor-seeds', 'homogeneous-identities', 'chart-and-lines', 'pole-bounds', 'computed-bounds']:
        expected = json.loads((ROOT / 'certificates' / (name + '.json')).read_text())
        if results[name] != expected:
            raise ValueError('Recomputed certificate mismatch: ' + name)
    print(json.dumps({'status': 'PASS', 'checks': list(results),
                      'homogeneousScalarIdentities': results['homogeneous-identities']['exactScalarChecks'],
                      'homogeneousDivisorEntries': results['divisor-seeds']['nonzeroHomogeneousEntries'],
                      'abstractScalars': results['pole-bounds']['abstractScalars'],
                      'fixtures': results['fixtures']['tests'],
                      'publicGeneratorCompared': args.public_generator is not None,
                      'ambientDeformationAttributionProved': False,
                      'normalizedAxesReevaluated': False,
                      'quotientOrScalarCoordinatesEvaluated': False}, indent=2))


if __name__ == '__main__':
    main()
