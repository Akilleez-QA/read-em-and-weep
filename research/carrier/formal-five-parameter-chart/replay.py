"""Rebuild the published certificates from this directory's complete inputs."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
CERTIFICATES = ('early_parameters.json', 'quadratic_certificate.json',
                'higher_certificate.json', 'weight_certificate.json')


def verify_integrity(root=ROOT):
    checked = 0
    for line in (root/'SHA256SUMS').read_text().splitlines():
        digest, name = line.split('  ', 1)
        path = root/name
        if path.is_symlink() or not path.is_file():
            raise ValueError(f'Missing or invalid package file: {name}')
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError(f'Integrity mismatch: {name}')
        checked += 1
    return checked


def main():
    if not __debug__:
        raise RuntimeError('Run without -O: exact checks use assertions.')
    count = verify_integrity()
    print(f'Package integrity: {count} files verified', flush=True)
    for script in ('check_early.py', 'check_higher.py', 'check_weights.py'):
        subprocess.run([sys.executable, str(ROOT/script)], check=True, cwd=ROOT)
    for name in CERTIFICATES:
        expected = json.loads((ROOT/'certificates'/name).read_text())
        actual = json.loads((ROOT/'build'/name).read_text())
        if expected != actual:
            raise ValueError(f'Regenerated certificate differs: {name}')
    print('PASS: all four regenerated certificates exactly match.', flush=True)


if __name__ == '__main__':
    main()
