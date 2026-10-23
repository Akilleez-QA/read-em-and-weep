"""Relocated metadata-only smoke; the payload is read but never imported."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--payload', type=Path, required=True)
    args = parser.parse_args()
    payload = args.payload.resolve(strict=True)
    source = Path(__file__).resolve().parent
    expected = json.loads((source / 'CONTRACT.json').read_text())
    disabled_bytes = (source / 'execution-lock.json').read_bytes()
    require(json.loads(disabled_bytes)['execution_ready'] is False, 'shipped execution gate must stay disabled')
    with tempfile.TemporaryDirectory(prefix='q65-portability-') as td:
        root = Path(td)
        package = root / 'research' / 'hm' / 'q-middle-shard-contract'
        package.mkdir(parents=True)
        for name in ('q65_shards.py', 'test_receipts.py', 'CONTRACT.json', 'execution-lock.json'):
            shutil.copyfile(source / name, package / name)
        unrelated_cwd = root / 'unrelated-working-directory'
        unrelated_cwd.mkdir()
        rebuilt = root / 'rebuilt.json'
        command = [sys.executable, str(package / 'q65_shards.py'), 'catalogue',
                   '--payload', str(payload), '--output', str(rebuilt)]
        result = subprocess.run(command, cwd=unrelated_cwd, capture_output=True, text=True, timeout=10)
        require(result.returncode == 0, result.stderr)
        require(json.loads(rebuilt.read_text()) == expected, 'relocated catalogue changed')
        missing = subprocess.run([sys.executable, str(package / 'q65_shards.py'), 'catalogue',
                                  '--output', str(root / 'must-not-exist.json')],
                                 cwd=unrelated_cwd, capture_output=True, text=True, timeout=5)
        require(missing.returncode == 2 and '--payload' in missing.stderr, 'payload path was inferred')
        require(not (root / 'must-not-exist.json').exists(), 'missing-payload call wrote an output')
        fixtures = subprocess.run([sys.executable, str(package / 'test_receipts.py')],
                                  cwd=unrelated_cwd, capture_output=True, text=True, timeout=10)
        require(fixtures.returncode == 0, fixtures.stderr)
        report = json.loads(fixtures.stdout)
        require(report['payload_imported'] is False and report['mathematical_maps_checked'] == 0,
                'metadata fixture scope changed')
        require(len(report['negative_cases']) == 22, 'negative fixture coverage changed')
        require((package / 'execution-lock.json').read_bytes() == disabled_bytes, 'disabled gate changed')
        require((package / 'CONTRACT.json').read_bytes() == (source / 'CONTRACT.json').read_bytes(),
                'checked-in contract changed')
    print(json.dumps({'status': 'metadata-portability-pass', 'negative_fixture_cases': 22,
                      'catalogue_units': 73, 'execution_gate': 'disabled',
                      'payload_imported': False, 'mathematical_maps_checked': 0}, indent=2))


if __name__ == '__main__':
    main()
