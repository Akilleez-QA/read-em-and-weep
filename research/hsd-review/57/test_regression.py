"""Each corrupted fixture fails after its iota-pair symmetry has survived."""

import copy
import importlib.util
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
AGGREGATE_SPEC = importlib.util.spec_from_file_location(
    "hsd57_recompute_regression", HERE / "recompute_aggregate.py"
)
review = importlib.util.module_from_spec(AGGREGATE_SPEC)
AGGREGATE_SPEC.loader.exec_module(review)
SYMMETRY_SPEC = importlib.util.spec_from_file_location(
    "hsd57_iota_regression", HERE / "symmetry" / "check_involution.py"
)
check = importlib.util.module_from_spec(SYMMETRY_SPEC)
SYMMETRY_SPEC.loader.exec_module(check)


def orientation_edges(document):
    return {
        "".join(str(part) for part in edge["roles"]): edge
        for edge in document["edges"]
    }


def pair_symmetry_survives(document) -> bool:
    edges = orientation_edges(document)
    for left, right in review.EXPECTED_EQUAL_PAIRS:
        if left not in edges or right not in edges:
            return False
        if edges[left]["integer_coefficients"] != edges[right]["integer_coefficients"]:
            return False
        left_sign = review.permutation_sign(tuple(int(character) for character in left))
        right_sign = review.permutation_sign(tuple(int(character) for character in right))
        if left_sign != right_sign:
            return False
    return True


def replace_list(document, source: str, target: str):
    edges = orientation_edges(document)
    edges[target]["integer_coefficients"] = copy.deepcopy(edges[source]["integer_coefficients"])
    edges[target]["coefficient_array_sha256"] = review.coefficient_digest(
        edges[target]["integer_coefficients"]
    )


class RegressionFixtures(unittest.TestCase):
    def test_verdict_states_limits_without_stale_claims(self):
        text = (HERE / "VERDICT.md").read_text()
        self.assertIn("The tests do not regenerate the source DAG.", text)
        self.assertIn("Distinct does not mean linearly independent.", text)
        self.assertNotIn("copied-file", text)
        self.assertNotIn("Copied pair", text)
        self.assertNotIn("permutation sign differ", text)
        lowered = text.lower()
        self.assertNotIn("opposite sign", lowered)
        self.assertNotIn("opposite-sign", lowered)

    @classmethod
    def setUpClass(cls):
        cls.provenance = review.load_json(review.PACKAGE / "provenance.json")
        cls.digest = review.sha256(review.PACKAGE / "contributions.json")
        cls.document = review.load_json(review.PACKAGE / "contributions.json")

    def gate(self, document):
        self.assertTrue(pair_symmetry_survives(document))
        aggregate = review.audit(document, self.provenance, self.digest)
        symmetry, symmetry_code = check.decide(document, self.provenance, self.digest)
        return aggregate, review.exit_status(aggregate), symmetry, symmetry_code

    def assert_both_reject(self, document, aggregate, aggregate_code, symmetry, symmetry_code):
        self.assertTrue(pair_symmetry_survives(document))
        self.assertNotEqual(aggregate_code, 0)
        self.assertNotEqual(symmetry_code, 0)
        self.assertNotEqual(symmetry["classification"], "expected symmetry")
        self.assertEqual(symmetry["mismatches"], [])
        self.assertTrue(symmetry["failures"])
        self.assertTrue(aggregate["acceptance_failures"])

    def test_wrong_sign_exits_nonzero(self):
        document = copy.deepcopy(self.document)
        orientation_edges(document)["0123"]["permutation_sign"] = -1
        aggregate, aggregate_code, symmetry, symmetry_code = self.gate(document)
        self.assert_both_reject(document, aggregate, aggregate_code, symmetry, symmetry_code)
        self.assertEqual(aggregate["sum"], ["0", "1"])
        self.assertEqual(aggregate["data_defects"], [])
        self.assertEqual(aggregate["orbit_equalities"]["role"], "informational")
        self.assertIn("0123 recorded sign -1 != 1", aggregate["arithmetic_defects"])
        self.assertIn("0123 recorded sign -1 != 1", symmetry["failures"])

    def test_changed_pin_exits_nonzero(self):
        document = copy.deepcopy(self.document)
        edge = orientation_edges(document)["1203"]
        tweaked = False
        for row in edge["integer_coefficients"]:
            if row[1] != review.HOMOGENEOUS:
                updated = int(row[3]) + 1
                row[3] = str(updated if updated != 0 else 1)
                tweaked = True
                break
        self.assertTrue(tweaked)
        edge["coefficient_array_sha256"] = review.coefficient_digest(edge["integer_coefficients"])
        aggregate, aggregate_code, symmetry, symmetry_code = self.gate(document)
        self.assert_both_reject(document, aggregate, aggregate_code, symmetry, symmetry_code)
        self.assertEqual(aggregate["sum"], ["0", "1"])
        self.assertEqual(aggregate["distinct_coefficient_arrays"], 12)
        self.assertEqual(aggregate["data_defects"], [])
        self.assertTrue(any("1203 disagrees with published" in item for item in aggregate["arithmetic_defects"]))
        self.assertTrue(any("1203 disagrees with published" in item for item in symmetry["failures"]))

    def test_missing_orientation_exits_nonzero(self):
        document = copy.deepcopy(self.document)
        document["edges"] = [
            edge for edge in document["edges"]
            if "".join(str(part) for part in edge["roles"]) != "1320"
        ]
        self.assertTrue(pair_symmetry_survives(document))
        aggregate, aggregate_code, symmetry, symmetry_code = self.gate(document)
        self.assertNotEqual(aggregate_code, 0)
        self.assertNotEqual(symmetry_code, 0)
        self.assertEqual(aggregate["orientation_count"], 17)
        self.assertTrue(any("orientation count 17 != 18" in item for item in aggregate["acceptance_failures"]))
        self.assertTrue(any("1320" in item for item in symmetry["failures"]))
        self.assertNotEqual(symmetry["classification"], "expected symmetry")

    def test_unexpected_pair_exits_nonzero(self):
        document = copy.deepcopy(self.document)
        replace_list(document, "0123", "1023")
        aggregate, aggregate_code, symmetry, symmetry_code = self.gate(document)
        self.assert_both_reject(document, aggregate, aggregate_code, symmetry, symmetry_code)
        self.assertEqual(aggregate["orbit_equalities"]["role"], "rejected")
        self.assertTrue(any(item.startswith("unexpected equal-list partition") for item in aggregate["data_defects"]))
        self.assertFalse(any("within-singleton collision" in item for item in aggregate["data_defects"]))
        self.assertTrue(any(item.startswith("unexpected equal-list partition") for item in symmetry["failures"]))

    def test_within_singleton_collision_exits_nonzero(self):
        document = copy.deepcopy(self.document)
        replace_list(document, "1023", "1032")
        aggregate, aggregate_code, symmetry, symmetry_code = self.gate(document)
        self.assert_both_reject(document, aggregate, aggregate_code, symmetry, symmetry_code)
        self.assertEqual(aggregate["sum"], ["567", "8"])
        self.assertEqual(aggregate["distinct_coefficient_arrays"], 11)
        self.assertIn("within-singleton collision", aggregate["data_defects"])
        self.assertEqual(symmetry["distinct_lists"], 11)
        self.assertNotEqual(symmetry["independent_quotients"], 12)
        self.assertEqual(symmetry["distinct_singleton_lists"], 5)
        self.assertIn("within-singleton collision", symmetry["failures"])
        self.assertIn("total 567/8 is not 0", symmetry["failures"])

    def test_wrong_distinct_count_exits_nonzero(self):
        document = copy.deepcopy(self.document)
        replace_list(document, "1023", "1032")
        replace_list(document, "1023", "1203")
        aggregate, aggregate_code, symmetry, symmetry_code = self.gate(document)
        self.assert_both_reject(document, aggregate, aggregate_code, symmetry, symmetry_code)
        self.assertEqual(aggregate["distinct_coefficient_arrays"], 10)
        self.assertIn("distinct lists 10 != 12", aggregate["data_defects"])
        self.assertEqual(symmetry["distinct_lists"], 10)
        self.assertNotEqual(symmetry["independent_quotients"], 12)
        self.assertIn("distinct lists 10 != 12", symmetry["failures"])

    def test_nonzero_total_exits_nonzero(self):
        document = copy.deepcopy(self.document)
        edge = orientation_edges(document)["1302"]
        tweaked = False
        for row in edge["integer_coefficients"]:
            if row[1] == review.HOMOGENEOUS:
                updated = int(row[3]) + 1
                row[3] = str(updated if updated != 0 else 1)
                tweaked = True
                break
        self.assertTrue(tweaked)
        edge["coefficient_array_sha256"] = review.coefficient_digest(edge["integer_coefficients"])
        aggregate, aggregate_code, symmetry, symmetry_code = self.gate(document)
        self.assert_both_reject(document, aggregate, aggregate_code, symmetry, symmetry_code)
        self.assertEqual(aggregate["distinct_coefficient_arrays"], 12)
        self.assertEqual(aggregate["data_defects"], [])
        self.assertEqual(aggregate["orbit_equalities"]["role"], "informational")
        self.assertFalse(aggregate["sum_is_zero"])
        self.assertTrue(any(item.startswith("total ") and item.endswith(" is not 0") for item in aggregate["acceptance_failures"]))
        self.assertTrue(any(item.startswith("total ") and item.endswith(" is not 0") for item in symmetry["failures"]))
        self.assertEqual(symmetry["distinct_lists"], 12)


if __name__ == "__main__":
    unittest.main()
