"""Synthetic receipts only. No mathematical producer or payload is imported."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
PINNED = HERE / 'pinned'
COMMIT = 'fce4a9139101cd88eb50842174580fcd4fc6e160'
PINS = {
    'q65_shards.py': '1d1abf9ca1b965b5a6467957b6875ae9e30c52d849daf0a3bac5d2b91373c393',
    'CONTRACT.json': 'c4ecc98cdad68bd2a7bef743778487adb6fd5b0a78b311aec2d85b9a330152ef',
    'execution-lock.json': '81c05e416284a4b4216c9daa164e9760708f01112efc36b4136d1a8038155350',
}
SCOPES = (
    'graded_module:all_assertions',
    'build_module:all_assertions',
    'transitive_initialization_helpers:all_assertions',
)
EXPECTED_OUTPUT = {
    'status': 'execution_receipts_complete', 'harmonic': 55, 'trace': 10, 'global': 8,
    'mathematical_claim': 'receipt accounting only; producer correctness requires independent review',
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()


def verify_pins():
    for name, expected in PINS.items():
        if sha((PINNED / name).read_bytes()) != expected:
            raise AssertionError('Pinned test input changed: ' + name)
    contract = json.loads((PINNED / 'CONTRACT.json').read_bytes())
    if len(contract['units']) != 73 or len({u['unit_id'] for u in contract['units']}) != 73:
        raise AssertionError('Not the complete 73-unit pinned catalogue')
    counts = {category: sum(u['category'] == category for u in contract['units'])
              for category in ('global', 'harmonic', 'trace')}
    if counts != {'global': 8, 'harmonic': 55, 'trace': 10}:
        raise AssertionError('Catalogue categories changed')
    if json.loads((PINNED / 'execution-lock.json').read_bytes())['execution_ready'] is not False:
        raise AssertionError('Shipped production execution gate is not disabled')


class Fixture:
    """A full synthetic packet, created only under a caller's TemporaryDirectory.

    fixture_only=False is deliberate: the pinned aggregate CLI exposes no fixture
    mode. This production-shaped metadata exercises the full production CLI, but
    every log says SYNTHETIC, hashes are fabricated, and no receipt is evidence of
    an execution. This module never runs a shard or changes the shipped lock.
    """
    def __init__(self, root):
        self.root = Path(root)
        self.root.mkdir()
        self.logs = self.root / 'logs'
        self.logs.mkdir()
        self.cwd = self.root / 'unrelated-cwd'
        self.cwd.mkdir()
        self.contract = json.loads((PINNED / 'CONTRACT.json').read_bytes())
        self.lock = {
            'execution_ready': True,
            'contract_sha256': self.contract['contract_sha256'],
            'adapter_sha256': sha(b'SYNTHETIC adapter: not executed'),
            'initializer_sha256': sha(b'SYNTHETIC initializer: not executed'),
            'initializer_provenance_sha256': sha(b'SYNTHETIC provenance: not evidence'),
            'helper_assertion_coverage': {
                'scopes': dict.fromkeys(SCOPES, 'separately-certified'),
                'coverage_manifest_sha256': sha(b'SYNTHETIC coverage: not evidence'),
                'independent_review_sha256': sha(b'SYNTHETIC review: not evidence'),
            },
            'python': 'SYNTHETIC metadata only', 'sympy': 'NOT IMPORTED',
        }
        self.receipts = []
        for index, unit in enumerate(self.contract['units']):
            marker = 'Q65_UNIT_COMPLETE ' + unit['unit_id']
            log = b'SYNTHETIC FIXTURE ONLY; NO MATHEMATICS EXECUTED\n' + marker.encode() + b'\n'
            name = f'logs/unit-{index:02d}.log'
            (self.root / name).write_bytes(log)
            self.receipts.append({
                'schema': 'q65-shards-v1/receipt', 'fixture_only': False,
                'synthetic_test_artifact': True,
                'unit_id': unit['unit_id'],
                'contract_sha256': self.contract['contract_sha256'],
                'runtime_lock_sha256': sha(canonical(self.lock)),
                'input_before_sha256': self.contract['input_bundle_sha256'],
                'input_after_sha256': self.contract['input_bundle_sha256'],
                'status': 'passed', 'exit_code': 0, 'timed_out': False,
                'terminated': False, 'assertions_enabled': True,
                'checks': dict.fromkeys(unit['check_ids'], 'passed'),
                'terminal_marker': marker, 'elapsed_seconds': 0.25,
                'log_path': name, 'log_sha256': sha(log),
            })

    def replace_log(self, data, index=0, refresh_digest=True):
        receipt = self.receipts[index]
        (self.root / receipt['log_path']).write_bytes(data)
        if refresh_digest:
            receipt['log_sha256'] = sha(data)

    def marker(self, index=0):
        return self.receipts[index]['terminal_marker'].encode()

    def read_log(self, index=0):
        return (self.root / self.receipts[index]['log_path']).read_bytes()

    def refresh_lock_bindings(self):
        for receipt in self.receipts:
            receipt['runtime_lock_sha256'] = sha(canonical(self.lock))

    def run(self):
        for name, obj in (('contract.json', self.contract), ('lock.json', self.lock)):
            (self.root / name).write_text(json.dumps(obj), encoding='utf-8')
        paths = []
        for index, receipt in enumerate(self.receipts):
            path = self.root / f'receipt-{index:02d}.json'
            path.write_text(json.dumps(receipt), encoding='utf-8')
            paths.append(str(path))
        # -I -S -B isolates Python from PYTHONPATH, site packages and bytecode writes.
        # The pinned validator imports standard-library modules only.
        command = [sys.executable, '-I', '-S', '-B', str(PINNED / 'q65_shards.py'),
                   'aggregate', str(self.root / 'contract.json'), str(self.root / 'lock.json'),
                   *paths]
        return subprocess.run(command, cwd=self.cwd, capture_output=True, text=True,
                              timeout=5, check=False)
