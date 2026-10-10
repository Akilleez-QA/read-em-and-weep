#!/usr/bin/env python3
"""Small exact fixtures; no sealed arrays or full quotient computation needed."""
import json
from fractions import Fraction
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from build_compact_secondary_jet import build
from build_clearing import build as clearing
from build_axis import compact_metadata, check_pin
from verify_support import verify

HERE = Path(__file__).resolve().parent


class SourceTests(unittest.TestCase):
    def test_reverse_shifts_and_discarding(self):
        # F=(3/2)u^3 + 2uv + 5v^2 + 7. K=3 retains degrees 3,2,1.
        source = {'sumNodes': [[[["3", "2"], [[1, 3]]],
                               [["2", "1"], [[1, 1], [2, 1]]],
                               [["5", "1"], [[2, 2]]],
                               [["7", "1"], []]]],
                  'outputs': [{'coefficient': ['1', '1'], 'factors': [[16, 1]]}]}
        result = build(source, axis=1, first=0, K=3, output=0, remove=0, target=3)
        self.assertEqual([t[1] for t in result['sumNodes'][0]['terms']], [0, 2])
        self.assertEqual(result['representationCounts']['termsDiscardedByCertifiedReverseShift'], 2)
        self.assertEqual(result['root']['reverseShift'], 0)
        self.assertEqual(result['outputs'][0]['layerSupport'], (0, 0, 0, 0, 0, 0))
        self.assertIsNone(result['outputs'][1]['layerSupport'])
        self.assertEqual(result['outputs'][2]['layerSupport'], (1, 1, 0, 0, 1, 1))
        self.assertFalse(result['coefficientEvaluationPerformed'])

    def test_clearing_includes_discarded_terms(self):
        # A discarded constant denominator must still affect D_16.
        source = {'coefficientField': 'Q',
                  'sumNodes': [[[["1", "2"], [[1, 5]]], [["1", "7"], []]]],
                  'outputs': [{'coefficient': ['3', '5'], 'factors': [[16, 2]]}]}
        compact = build(source, axis=1, first=0, K=2, output=0, remove=0, target=10)
        compact['sourceSHA256'] = 'normalized'
        result = clearing(source, compact, 'normalized', 'compact')
        self.assertEqual(result['nodes'][0]['denominator'], '14')
        self.assertEqual(result['nodes'][0]['integerWeights'], ['7'])
        self.assertEqual(result['root'], {'denominator': '980', 'integerWeight': '3'})
        self.assertFalse(result['polynomialCoefficientsEvaluated'])
        with self.assertRaises(ValueError):
            clearing(source, compact, 'wrong-source', 'compact')

    def test_historical_projection_metadata_is_not_executed(self):
        ordinary = compact_metadata(0, 1, 'hash')
        fourth = compact_metadata(3, 0, 'hash')
        self.assertEqual([g['remainingTotalDegree'] for g in ordinary['gradedOutputs']], list(range(105, 111)))
        self.assertFalse(fourth['sourceTotalDegreeFilterApplied'])
        self.assertFalse(fourth['pairingMonomialApplied'])
        self.assertNotIn('gradedOutputs', fourth)

    def test_support_and_bad_factor(self):
        source = {'coefficientField': 'Q', 'sumNodes': [], 'outputs': [
            {'coefficient': ['1', '1'], 'factors': [[1, 48], [2, 48], [3, 48]]} for _ in range(2)]}
        report = verify(source, 0)
        self.assertEqual(report['rootSupports'][1]['totalMaximum'], 144)
        self.assertFalse(report['degree273VanishingProved'])
        source['outputs'][1]['factors'][0] = [0, 48]
        with self.assertRaises(ValueError):
            verify(source, 0)

    def test_concrete_normalization_and_no_overwrite(self):
        # (x^2-1) - x^2 + 1 is exactly zero after concrete substitution.
        tag = lambda j: ['tags'] + [int(i == j) for i in range(16)]
        source = {'coefficientField': 'Q', 'tagNames': ['X', 'L'],
                  'tagPolynomials': [[[[1, 0, 0, 0], '1']],
                                     [[[2, 0, 0, 0], '1'], [[0, 0, 0, 0], '-1']]],
                  'nodes': [tag(0), ['mul', 0, 0], ['const', '-1', '1'],
                            ['mul', 1, 2], tag(1), ['add', 3, 4],
                            ['const', '1', '1'], ['add', 5, 6]],
                  'outputs': [{'numerator': 7, 'powers': [0] * 16}]}
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'input.json'
            output = Path(temp) / 'normalized.json'
            path.write_text(json.dumps(source))
            command = [sys.executable, str(HERE / 'normalize_free_tags.py'), str(path), '64',
                       '--concrete-tags', '--input-label', 'portable/input.json', '--export', str(output)]
            subprocess.run(command, check=True, capture_output=True)
            result = json.loads(output.read_text())
            self.assertEqual(result['input'], 'portable/input.json')
            self.assertEqual(result['outputs'][0]['coefficient'], ['0', '1'])
            self.assertEqual(result['sumNodes'], [])
            self.assertNotEqual(subprocess.run(command, capture_output=True).returncode, 0)
            with self.assertRaises(ValueError):
                check_pin(output, 'wrong-hash')


if __name__ == '__main__':
    unittest.main(verbosity=2)
