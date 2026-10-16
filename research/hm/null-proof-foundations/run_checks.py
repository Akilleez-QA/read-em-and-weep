#!/usr/bin/env python3
"""Replay abstract controls and exact public metadata; never physical sources."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

def main():
    if not __debug__ or os.environ.get('PYTHONOPTIMIZE'):
        raise SystemExit('Assertions must be enabled; remove -O/-OO and PYTHONOPTIMIZE.')
    snapshots = {
        'test_scalar_homotopy_adjoint.py': 'scalar-homotopy-adjoint-test-results.json',
        'test_scalar_cover_adjoint.py': 'scalar-cover-adjoint-test-results.json',
        'test_owned_denominator_complex.py': 'owned-denominator-test-results.json',
        'test_jet_quotient_dual_certificate.py': 'jet-quotient-dual-test-results.json',
    }
    results = []
    for path in sorted(ROOT.glob('test_*.py')):
        run = subprocess.run([sys.executable, path.name], cwd=ROOT,
                             capture_output=True, text=True)
        results.append({'file': path.name, 'exit_code': run.returncode,
                        'stdout': run.stdout, 'stderr': run.stderr})
        print(path.name + ': ' + ('PASS' if run.returncode == 0 else 'FAIL'), flush=True)
        if run.returncode:
            print(run.stdout + run.stderr)
            return 1
        if path.name in snapshots:
            expected = json.loads((ROOT / snapshots[path.name]).read_text())
            if json.loads(run.stdout) != expected:
                raise SystemExit('Mathematical result mismatch: ' + path.name)
    for source, artifact in [('compile_refined_detector_metadata.py', 'refined-detector-metadata.json'),
                             ('prune_refined_selector_paths.py', 'refined-selector-pruning.json')]:
        run = subprocess.run([sys.executable, source], cwd=ROOT, capture_output=True)
        if run.returncode or run.stdout != (ROOT / artifact).read_bytes():
            raise SystemExit('Regeneration mismatch: ' + artifact)
        print(artifact + ': exact regeneration PASS', flush=True)
    for line in (ROOT / 'SHA256SUMS').read_text().splitlines():
        digest, name = line.split('  ', 1)
        if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != digest:
            raise SystemExit('Hash mismatch: ' + name)
    print('All file hashes verified. No physical-source evaluation.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
