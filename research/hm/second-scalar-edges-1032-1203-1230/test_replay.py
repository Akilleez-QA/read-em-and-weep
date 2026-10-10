import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
import replay as r


class ReplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = r.load(r.HERE / 'contributions.json')
        cls.weights = r.kernel()

    def rejected(self, change):
        data = copy.deepcopy(self.data)
        change(data)
        with self.assertRaises((ValueError, KeyError, TypeError)):
            r.verify(data)

    def test_full_replay(self):
        result = r.replay()
        self.assertEqual([e['nonzero_selected_coefficients'] for e in result['edges']], [16, 24, 16])
        self.assertEqual(sum(e['selector_rows'] for e in result['edges']), 585)
        self.assertEqual(sum(e['quotient_terms'] for e in result['edges']), 669)
        self.assertFalse(result['complete_scalar_pairing_computed'])

    def test_kernel_inverse_identity_independent_positive_power(self):
        # Build G^70 by 70 ordinary positive convolutions, then check G^70 K=1.
        g = {(0, 0): 1, (0, 1): 1, (1, 0): 1, (1, 1): 3,
             (1, 2): 1, (2, 1): 1, (2, 2): 1}
        def mul(a, b):
            result = {}
            for (i, j), c in a.items():
                for (k, l), d in b.items():
                    if i + k < 9 and j + l < 23:
                        key = i + k, j + l
                        result[key] = result.get(key, 0) + c*d
            return {k: v for k, v in result.items() if v}
        power = {(0, 0): 1}
        for _ in range(70):
            power = mul(power, g)
        self.assertEqual(mul(power, self.weights), {(0, 0): 1})

    def test_role_relabel_rejected(self):
        self.rejected(lambda d: d['edges'][0].update(roles=[0, 1, 2, 3]))

    def test_wrong_sign_rejected(self):
        self.rejected(lambda d: d['edges'][0].update(permutation_sign=-1))

    def test_boolean_sign_rejected(self):
        self.rejected(lambda d: d['edges'][0].update(permutation_sign=True))

    def test_old_window_rejected(self):
        self.rejected(lambda d: d['edges'][0].update(shape=[7, 36, 21]))

    def test_lost_grading_rejected(self):
        self.rejected(lambda d: d['edges'][0].update(homogeneous_degrees_separated=False))

    def test_coefficient_tamper_even_with_rehashed_array_rejected(self):
        def change(d):
            e = d['edges'][0]
            row = next(row for row in e['integer_coefficients'] if row[1] == 41 and row[2] <= 20)
            row[3] = str(int(row[3]) + 1)
            e['coefficient_array_sha256'] = hashlib.sha256(json.dumps(e['integer_coefficients'], separators=(',', ':')).encode()).hexdigest()
        self.rejected(change)

    def test_weight_rejected(self):
        self.rejected(lambda d: d['edges'][0]['rows'][0].update(kernel_weight='0'))

    def test_exponent_rejected(self):
        self.rejected(lambda d: d['edges'][0]['rows'][0].update(source_exponents=[0, 0, 0, 0]))

    def test_boolean_index_rejected(self):
        self.rejected(lambda d: d['edges'][0]['rows'][0].update(slot=[False, 41, 0]))

    def test_missing_row_rejected(self):
        self.rejected(lambda d: d['edges'][0]['rows'].pop())

    def test_rational_encodings_rejected(self):
        for pair in [['00', '1'], ['0', '2'], ['0', '-1'], [0, '1']]:
            with self.subTest(pair=pair):
                self.rejected(lambda d: d['edges'][0]['rows'][0].update(coefficient=pair))

    def test_duplicate_edge_rejected(self):
        self.rejected(lambda d: d['edges'].__setitem__(1, copy.deepcopy(d['edges'][0])))

    def test_total_claim_rejected(self):
        self.rejected(lambda d: d.update(complete_scalar_pairing_computed=True))

    def test_missing_edge_not_zero(self):
        self.rejected(lambda d: d.update(remaining_after_these_and_pr43_pr46_pr50=0))

    def test_json_duplicate_key_rejected(self):
        with self.assertRaises(ValueError):
            json.loads('{"x":1,"x":2}', object_pairs_hook=r.unique)


    def test_disjoint_cumulative_coverage(self):
        result = r.verify(self.data)
        self.assertEqual(result['cumulative_published_orientations'], 10)
        self.assertEqual(result['remaining_after_these_and_pr43_pr46_pr50'], 8)

    def test_overlapping_prior_coverage_rejected(self):
        self.rejected(lambda d: d['previously_published_orientations'].__setitem__(0, [1, 0, 3, 2]))

    def test_1230_unsigned_contraction(self):
        edge = self.data['edges'][2]
        self.assertEqual(sum((r.rat(row['weighted_contribution']) for row in edge['rows']), r.F(0)), r.F(4313, 4))
        self.assertEqual(edge['permutation_sign'], -1)

    def test_1230_double_sign_rejected(self):
        self.rejected(lambda d: d['edges'][2].update(signed_contribution=['4313', '4']))

    def test_package_integrity_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory)
            for p in r.HERE.iterdir():
                if p.is_file():
                    (out / p.name).write_bytes(p.read_bytes())
            with (out / 'contributions.json').open('a') as f:
                f.write(' ')
            with self.assertRaises(ValueError):
                r.verify_manifest(out)


if __name__ == '__main__':
    unittest.main()
