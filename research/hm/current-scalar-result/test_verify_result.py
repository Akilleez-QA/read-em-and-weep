#!/usr/bin/env python3
"""Regression checks for successful replay and rejection of altered inputs."""
from pathlib import Path
import json
import shutil
import tempfile
import unittest
import verify_result as V


class ReplayTests(unittest.TestCase):
    def test_complete_replay(self):
        self.assertEqual(V.verify()['sourceRows'], 44280)

    def test_quotient_mutation_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'package'
            shutil.copytree(V.HERE, root, ignore=shutil.ignore_patterns('__pycache__'))
            p = root / 'quotients' / 'edge-0123.json'
            q = json.loads(p.read_text())
            q['integerQuotientCoefficients'][0][3] = '601'
            p.write_text(json.dumps(q))
            with self.assertRaisesRegex(AssertionError, 'File digest mismatch'):
                V.verify(root)

    def test_result_mutation_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'package'
            shutil.copytree(V.HERE, root, ignore=shutil.ignore_patterns('__pycache__'))
            p = root / 'final-result.json'
            q = json.loads(p.read_text())
            q['coordinates'][2] = ['1', '1']
            p.write_text(json.dumps(q))
            with self.assertRaisesRegex(AssertionError, 'File digest mismatch'):
                V.verify(root)


if __name__ == '__main__':
    unittest.main()
