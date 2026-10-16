"""Independent repository-provenance follow-up; no actual source evaluation.

Run this file directly, normally and with -O. Historical reviews stay immutable.
"""
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import unittest
from unittest import mock

import domain as D

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASE = HERE.parent
SNAPSHOT = 'f65b2d680'
LANES = ('source-faithful-P', 'source-faithful-Q', 'source-domain-application')
MARKERS = {
    'source-faithful-P': '8150a3a02b529be8398ba857b7e9f3fcd993900be2f14cc6f3a5fe2722169c62',
    'source-faithful-Q': '5b9eec260415123bf2f42cc05ec8d569df0fb21d952c06bff23e2a9ba2546b6d',
    'source-domain-application': '31135b2e17f41b67580b1639afafd654ef8e1b5dc4ab87a968a4363d0d3f2c47',
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def original(path):
    return subprocess.check_output(
        ['git', 'show', SNAPSHOT+':'+str(path.relative_to(ROOT))],
        cwd=ROOT, timeout=10)


def producer_snapshot():
    result = {}
    for lane in LANES:
        marker = BASE/lane/'producer-ready.json'
        result[marker] = marker.read_bytes()
        for name in json.loads(result[marker])['files']:
            path = marker.parent/name
            result[path] = path.read_bytes()
    return result


class PinFollowup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.before = producer_snapshot()
        cls.Q = D._canonical_module('fd_repo_pin_followup_Q', BASE/'source-faithful-Q/q_binding.py')

    @classmethod
    def tearDownClass(cls):
        if producer_snapshot() != cls.before:
            raise RuntimeError('producer bytes changed during follow-up')

    def test_all_producer_markers(self):
        for lane, expected in MARKERS.items():
            marker = BASE/lane/'producer-ready.json'
            self.assertEqual(sha(marker.read_bytes()), expected)
            for name, expected_file in json.loads(marker.read_bytes())['files'].items():
                with self.subTest(lane=lane, name=name):
                    self.assertEqual(sha((marker.parent/name).read_bytes()), expected_file)

    def test_none_and_resolved_canonical_acceptance(self):
        sentinel = {'independent_authentication_spy': True}
        canonical = Path(self.Q.__file__).resolve().parents[3]
        self.assertEqual(canonical, ROOT)
        # Includes a non-normalized spelling that resolves to the same repo.
        inputs = (None, canonical, str(canonical), canonical/'research'/'..')
        with mock.patch.object(self.Q, 'authenticate', return_value=sentinel) as auth:
            with mock.patch.object(self.Q.QH, 'authenticate_sources') as source_auth:
                for repo in inputs:
                    self.assertIs(self.Q.ActualQBinding(repo).pins, sentinel)
                self.assertEqual(auth.call_args_list, [mock.call()]*len(inputs))
                source_auth.assert_not_called()

    def test_noncanonical_rejected_before_any_authentication(self):
        with mock.patch.object(self.Q, 'authenticate', side_effect=AssertionError('authentication reached')) as auth:
            with mock.patch.object(self.Q.QH, 'authenticate_sources', side_effect=AssertionError('source authentication reached')) as source_auth:
                for repo in (ROOT.parent, ROOT/'research', ROOT.parent/'not-this-repository', '/tmp'):
                    with self.subTest(repo=str(repo)):
                        with self.assertRaisesRegex(ValueError, 'only canonical workspace repository'):
                            self.Q.ActualQBinding(repo)
                auth.assert_not_called()
                source_auth.assert_not_called()

    def test_qb_constructor_is_the_only_implementation_delta(self):
        path = BASE/'source-faithful-Q/q_binding.py'
        old = original(path)
        removed = b'  if repo is not None:QH.authenticate_sources(repo)\n'
        added = (b'  canonical=Path(__file__).resolve().parents[3]\n'
                 b"  need(repo is None or Path(repo).resolve()==canonical,'only canonical workspace repository is supported')\n")
        self.assertEqual(old.count(removed), 1)
        self.assertEqual(path.read_bytes(), old.replace(removed, added, 1))

    def test_fd_pin_only_snapshot_delta(self):
        path = HERE/'source-pins.json'
        old_raw, new_raw = original(path), path.read_bytes()
        old, new = json.loads(old_raw), json.loads(new_raw)
        q_path = 'research/codex-swarm/source-faithful-Q/q_binding.py'
        old_rows = old['canonical_definition_workspace_inputs']
        new_rows = new['canonical_definition_workspace_inputs']
        self.assertEqual(len(old_rows), len(new_rows))
        changed = [(a, b) for a, b in zip(old_rows, new_rows) if a != b]
        self.assertEqual(len(changed), 1)
        a, b = changed[0]
        self.assertEqual(a['path'], q_path)
        expected = dict(a, sha256=sha((ROOT/q_path).read_bytes()))
        self.assertEqual(b, expected)
        self.assertNotEqual(a['sha256'], b['sha256'])
        self.assertEqual(new_raw, old_raw.replace(a['sha256'].encode(), b['sha256'].encode(), 1))
        self.assertEqual(sha(new_raw), '09b2f3af2112c8880950d465c89229b9c043c37f81c0f7a1d1ed8ef5529440cc')
        marker = HERE/'producer-ready.json'
        self.assertEqual(marker.read_bytes(), original(marker).replace(sha(old_raw).encode(), sha(new_raw).encode(), 1))

    def test_historical_files_and_other_producer_bytes_unchanged(self):
        allowed = {
            'source-faithful-P': set(),
            'source-faithful-Q': {'q_binding.py', 'PROOF.md', 'README.md', 'test_binding.py', 'producer-ready.json'},
            'source-domain-application': {'source-pins.json', 'producer-ready.json', 'test_independent.py'},
        }
        for lane in LANES:
            directory = BASE/lane
            names = subprocess.check_output(
                ['git', 'ls-tree', '-r', '--name-only', SNAPSHOT, '--', str(directory.relative_to(ROOT))],
                cwd=ROOT, timeout=10).decode().splitlines()
            changed = set()
            for name in names:
                path = ROOT/name
                if path.read_bytes() != original(path):
                    changed.add(str(path.relative_to(directory)))
            self.assertEqual(changed, allowed[lane])
        # The original FD independent test has only its two verified anchors updated.
        path = HERE/'test_independent.py'
        expected = original(path)
        for name in ('producer-ready.json', 'source-pins.json'):
            p = HERE/name
            expected = expected.replace(sha(original(p)).encode(), sha(p.read_bytes()).encode(), 1)
        self.assertEqual(path.read_bytes(), expected)


if __name__ == '__main__':
    resource.setrlimit(resource.RLIMIT_AS, (512*1024*1024, 512*1024*1024))
    resource.setrlimit(resource.RLIMIT_CPU, (59, 59))
    unittest.main()
