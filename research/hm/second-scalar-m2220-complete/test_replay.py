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
        self.assertEqual([e['nonzero_selected_coefficients'] for e in result['edges']], [24, 16, 24, 16, 8, 8, 24, 16, 24, 16, 8, 8, 24, 16, 24, 16, 8, 8])
        self.assertEqual(sum(e['selector_rows'] for e in result['edges']), 3258)
        self.assertEqual(sum(e['quotient_terms'] for e in result['edges']), 4014)
        self.assertFalse(result['whole_scalar_map_computed'])

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
        self.rejected(lambda d: d['edges'][0].update(roles=[0, 1, 3, 2]))

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
        self.rejected(lambda d: d.update(whole_scalar_map_computed=True))

    def test_missing_edge_not_zero(self):
        self.rejected(lambda d: d.update(remaining_target_orientations=1))

    def test_json_duplicate_key_rejected(self):
        with self.assertRaises(ValueError):
            json.loads('{"x":1,"x":2}', object_pairs_hook=r.unique)


    def test_exact_total_and_complete_coverage(self):
        result = r.verify(self.data)
        self.assertEqual(result['verified_orientations'], 18)
        self.assertEqual(result['remaining_target_orientations'], 0)
        self.assertEqual(result['selected_coordinate'], ['0', '1'])
        self.assertEqual(result['distinct_source_exponents'], 3258)

    def test_missing_last_edge_rejected(self):
        self.rejected(lambda d: d['edges'].pop())

    def test_missing_negative_edge_cannot_be_zero_filled(self):
        self.rejected(lambda d: d['edges'][-1].update(signed_contribution=['0', '1']))

    def test_wrong_total_rejected(self):
        self.rejected(lambda d: d.update(selected_coordinate=['1', '1']))

    def test_inactive_orientation_rejected(self):
        self.rejected(lambda d: d['edges'][-1].update(roles=[3, 2, 1, 0]))

    def test_row_count_tamper_rejected(self):
        self.rejected(lambda d: d.update(source_rows=3257))

    def test_nonzero_count_tamper_rejected(self):
        self.rejected(lambda d: d.update(nonzero_source_rows=287))

    def test_source_attribution_claim_rejected(self):
        self.rejected(lambda d: d.update(source_attribution_reproduced=True))

    def test_historical_hashes_do_not_prove_public_regeneration(self):
        data = r.load(r.HERE / 'provenance.json')
        data['new_map_source_regeneration_distributed'] = True
        with self.assertRaises(ValueError):
            r.verify_provenance(data)

    def test_1302_unsigned_contraction(self):
        edge = self.data['edges'][10]
        self.assertEqual(sum((r.rat(row['weighted_contribution']) for row in edge['rows']), r.F(0)), r.F(-407, 8))
        self.assertEqual(edge['permutation_sign'], -1)

    def test_1302_double_sign_rejected(self):
        self.rejected(lambda d: d['edges'][10].update(signed_contribution=['-407', '8']))

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
