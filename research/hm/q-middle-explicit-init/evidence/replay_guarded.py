"""Optional guarded replay; execution is namespace-only, never sparse/q65."""
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

if not __debug__:
    raise RuntimeError("Run without -O; provenance checks require assertions.")
HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--package', type=Path, default=HERE.parent)
parser.add_argument('--payload', type=Path)
parser.add_argument('--guard', type=Path, required=True, help='Reviewed burn_guard.py; SHA256 checked before launch.')
parser.add_argument('--python', type=Path, default=Path(sys.executable), help='Python 3.12 with SymPy 1.14.0 and mpmath 1.3.0.')
parser.add_argument('--out', type=Path, required=True, help='New output directory; any existing path is rejected.')
args = parser.parse_args()
package = args.package.resolve()
payload = (args.payload or package.parent / 'q-middle-candidate-interface').resolve()
roots = {'package': package, 'payload': payload, 'reference': HERE}
pins = json.loads((HERE / 'pins.json').read_text())
provenance = json.loads((HERE / 'PROVENANCE.json').read_text())
assert hashlib.sha256(args.guard.read_bytes()).hexdigest() == provenance['original_guard']['sha256']
inputs = []
for item in pins['inputs']:
    path = roots[item['role']] / item['path']
    assert hashlib.sha256(path.read_bytes()).hexdigest() == item['sha256'], item
    inputs.append(path)
inputs.extend(HERE / name for name in ('pins.json', 'verify_namespace.py', 'replay_guarded.py', 'PROVENANCE.json'))
args.out.mkdir(parents=True, exist_ok=False)
command = [str(args.python.resolve()), '-B', str(args.guard.resolve()),
           '--receipt', str(args.out / 'receipt.json'), '--stdout', str(args.out / 'stdout.txt'),
           '--stderr', str(args.out / 'stderr.txt')]
for path in inputs:
    command.extend(('--input', str(path)))
command.extend(('--', str(args.python.resolve()), '-B', str(HERE / 'verify_namespace.py'),
                '--package', str(package), '--payload', str(payload)))
# Keep the reviewed guard defaults: CPU 60 s / wall 75 s / sampled group RSS 1.5 GiB.
sys.exit(subprocess.run(command).returncode)
