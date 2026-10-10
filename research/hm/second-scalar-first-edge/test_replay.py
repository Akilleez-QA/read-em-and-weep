"""Standalone arithmetic, routing, integrity, and corruption tests."""
import copy
import json
import shutil
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

import replay


class ReplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.q = replay.load(replay.HERE / "quotient.json")
        cls.request = replay.load(replay.HERE / "request.json")
        cls.values = replay.parse_quotient(cls.q)
        cls.kernels = replay.kernel_polynomial()

    def reject_quotient(self, change):
        q = copy.deepcopy(self.q)
        change(q)
        with self.assertRaises(ValueError):
            replay.parse_quotient(q)

    def reject_request(self, change):
        request = copy.deepcopy(self.request)
        change(request)
        with self.assertRaises(ValueError):
            replay.verify_request(request, self.values, self.kernels)

    def test_full_replay(self):
        report = replay.replay()
        self.assertEqual(report["signed_partial_edge"], ["8655", "16"])
        self.assertEqual(report["quotient_terms"], 203)
        self.assertEqual(report["nonzero_selections"], 24)
        self.assertEqual(report["remaining_target_orientations"], 17)
        self.assertIs(report["complete_scalar_pairing_computed"], False)
        self.assertIs(report["source_attribution_reproduced"], False)

    def test_second_independent_kernel_derivation(self):
        self.assertEqual(self.kernels, replay.kernel_polynomial("binomial"))
        for ell in range(23):
            self.assertEqual(self.kernels[0, ell], (-1)**ell * replay.comb(69 + ell, ell))

    def test_all_requests_derived(self):
        rows = replay.verify_request(self.request, self.values, self.kernels)
        self.assertEqual(len(rows), 207)
        self.assertEqual(len({tuple(row["slot"]) for row in rows}), 207)
        self.assertTrue(all(sum(row["source_exponents"]) == 685 for row in rows))
        self.assertEqual(rows[-1]["source_exponents"], [272, 207, 137, 69])
        self.assertEqual(rows[-1]["kernel_weight"], "1")

    def test_homogeneous_slots_stay_separate(self):
        values = {(r, w, ell): Fraction((r + 3) * 10**100, ell + 1)
                  for r in range(9) for w in (40, 42, 43) for ell in range(23)}
        rows = replay.selector_rows(values, self.kernels)
        self.assertTrue(all(row["coefficient"] == ["0", "1"] for row in rows))
        values[8, 41, 22] = Fraction(-5, 7)
        rows = replay.selector_rows(values, self.kernels)
        self.assertEqual(sum((replay.rational(row["weighted_contribution"]) for row in rows),
                             Fraction(0)), Fraction(-5, 7))

    def test_sparse_fraction_arithmetic(self):
        a = {(0, 0): Fraction(1, 3), (1, 0): Fraction(-2, 5)}
        b = {(0, 0): Fraction(3, 7), (0, 1): Fraction(4, 9)}
        self.assertEqual(replay.multiply(a, b, (2, 2)), {
            (0, 0): Fraction(1, 7), (0, 1): Fraction(4, 27),
            (1, 0): Fraction(-6, 35), (1, 1): Fraction(-8, 45)})
        self.assertEqual(replay.multiply({(8, 22): Fraction(1)}, {(1, 0): Fraction(1)}, (9, 23)), {})
        p = replay.power({(0, 0): Fraction(1), (1, 0): Fraction(1)}, 71, (9, 23))
        self.assertEqual(p[1, 0], 71)
        self.assertEqual(p[8, 0], replay.comb(71, 8))

    def test_role_and_sign_corruptions(self):
        self.reject_request(lambda d: d.update(roles=[0, 1, 3, 2]))
        self.reject_request(lambda d: d.update(permutation_sign=-1))
        self.reject_request(lambda d: d.update(permutation_sign=True))
        self.reject_quotient(lambda d: d.update(roles=[1, 0, 2, 3]))

    def test_interface_bound_corruptions(self):
        for key, value in (("d", 5), ("L", 21), ("w", 36), ("target_index", 1)):
            with self.subTest(key=key):
                self.reject_request(lambda d: d.update({key: value}))
        self.reject_quotient(lambda d: d.update(shape=[6, 37, 22]))
        self.reject_request(lambda d: d["rows"][0]["source_exponents"].__setitem__(3, 48))

    def test_coefficient_corruptions(self):
        self.reject_quotient(lambda d: d["integer_coefficients"][0].__setitem__(3, "-601"))
        self.reject_request(lambda d: d["rows"][-1].update(coefficient=["1", "3"]))
        self.reject_request(lambda d: d["rows"][-1].update(weighted_contribution=["1", "3"]))

    def test_weight_corruption(self):
        self.reject_request(lambda d: d["rows"][0].update(kernel_weight="1"))
        self.reject_request(lambda d: d["rows"][-1].update(kernel_weight="-1"))

    def test_malformed_quotients(self):
        changes = [lambda d: d.update(common_denominator="0"),
                   lambda d: d.update(common_denominator="-64"),
                   lambda d: d.update(common_denominator=64),
                   lambda d: d.update(scalar_map="X02[0,0]-X13[10,0]"),
                   lambda d: d.update(homogeneous_degrees_separated=False),
                   lambda d: d.update(pairing_aggregated=True),
                   lambda d: d["integer_coefficients"].pop(),
                   lambda d: d["integer_coefficients"].__setitem__(1, d["integer_coefficients"][0]),
                   lambda d: d["integer_coefficients"][0].__setitem__(0, 9),
                   lambda d: d["integer_coefficients"][0].__setitem__(0, True),
                   lambda d: d["integer_coefficients"][0].__setitem__(3, "0"),
                   lambda d: d["integer_coefficients"].reverse()]
        for index, change in enumerate(changes):
            with self.subTest(index=index):
                self.reject_quotient(change)

    def test_malformed_requests(self):
        self.reject_request(lambda d: d["rows"].pop())
        self.reject_request(lambda d: d["rows"][0]["slot"].__setitem__(0, False))
        self.reject_request(lambda d: d["rows"][0].update(coefficient=["0", "2"]))
        self.reject_request(lambda d: d["rows"][0].update(coefficient=["0", "0"]))
        self.reject_request(lambda d: d["rows"][0].update(kernel_weight="+1"))
        self.reject_request(lambda d: d.update(pairing_monomial=[2, 2, 2, 2]))

    def test_prefactor_and_mutation(self):
        data = replay.load(replay.HERE / "right-prefactor.json")
        self.assertEqual(replay.verify_prefactor(data), 2)
        data["numerators"][0][0][1] *= -1
        with self.assertRaises(ValueError):
            replay.verify_prefactor(data)

    def test_model_identities(self):
        model = replay.load(replay.HERE / "model.json")
        prefactor = replay.load(replay.HERE / "right-prefactor.json")
        report = replay.verify_model(model, prefactor)
        self.assertEqual(report["boundary_basis_checks"], 10)
        self.assertEqual(report["zero_E_row_entries"], 30)
        self.assertEqual(report["generic_Z_coefficient_checks"], 300)
        self.assertEqual(report["model_prefactor_ties"], 3)

    def test_model_identity_mutations(self):
        model = replay.load(replay.HERE / "model.json")
        prefactor = replay.load(replay.HERE / "right-prefactor.json")
        changes = [lambda m: m["gamma"][10].__setitem__(0, []),
                   lambda m: m["ev"][1].__setitem__(5, []),
                   lambda m: m["charts"][0]["I"][10].__setitem__(0, [["0,0,0,0", 1]]),
                   lambda m: m["charts"][5]["H0"][0].__setitem__(10, []),
                   lambda m: m["charts"][5]["H0"][0].__setitem__(11, [["0,0,0,0", 1]]),
                   lambda m: m["charts"][2]["P"][0].__setitem__(1, []),
                   lambda m: m["charts"][1]["H1"][3].__setitem__(5, []),
                   lambda m: m["charts"][2].update(dp=[])]
        for index, change in enumerate(changes):
            with self.subTest(index=index):
                changed = copy.deepcopy(model)
                change(changed)
                # Test actual algebra/model ties, not just the immutable digest.
                with self.assertRaises(ValueError):
                    replay.verify_model_identities(changed, prefactor)

    def test_duplicate_json_key(self):
        with self.assertRaises(ValueError):
            json.loads('{"a":1,"a":2}', object_pairs_hook=replay.unique_object)

    def test_manifest_detects_mutation_missing_and_extra(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            for source in replay.HERE.iterdir():
                if source.is_file():
                    shutil.copyfile(source, target / source.name)
            replay.verify_manifest(target)
            q = target / "quotient.json"
            q.write_bytes(q.read_bytes() + b"\n")
            with self.assertRaises(ValueError):
                replay.verify_manifest(target)
            shutil.copyfile(replay.HERE / "quotient.json", q)
            (target / "extra.json").write_text("{}")
            with self.assertRaises(ValueError):
                replay.verify_manifest(target)
            (target / "extra.json").unlink()
            q.unlink()
            with self.assertRaises(ValueError):
                replay.verify_manifest(target)


if __name__ == "__main__":
    unittest.main(verbosity=2)
