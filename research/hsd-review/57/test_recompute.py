"""Locks the independent aggregate check of the pinned #57 package."""

import copy
import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("hsd57_recompute", HERE / "recompute_aggregate.py")
review = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(review)


class AggregateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contributions_path = review.PACKAGE / "contributions.json"
        cls.provenance_path = review.PACKAGE / "provenance.json"
        cls.digest = review.sha256(cls.contributions_path)
        cls.document = review.load_json(cls.contributions_path)
        cls.provenance = review.load_json(cls.provenance_path)
        cls.report = review.audit(cls.document, cls.provenance, cls.digest)

    def test_checker_does_not_import_the_package_replay(self):
        source = (HERE / "recompute_aggregate.py").read_text()
        self.assertNotIn("import replay", source)
        self.assertNotIn("second-scalar-m2220-complete.replay", source)

    def test_kernel_and_scope(self):
        self.assertTrue(self.report["kernel_methods_agree"])
        self.assertEqual(self.report["evidence_class"], "supplied-quotient replay")
        self.assertFalse(self.report["source_regeneration"])
        self.assertEqual(self.report["scope_flags"]["whole_scalar_map_computed"], False)
        self.assertEqual(self.report["scope_flags"]["full_obstruction_computed"], False)
        self.assertEqual(self.report["scope_flags"]["source_attribution_reproduced"], False)
        self.assertEqual(self.report["scope_flags"]["historical_source_nodes_reevaluated_by_comparison"], 0)
        self.assertEqual(self.report["contributions_sha256"], review.CONTRIBUTIONS_SHA256)

    def test_eighteen_signs_and_exact_zero(self):
        self.assertEqual(self.report["orientation_count"], 18)
        self.assertEqual(self.report["arithmetic_defects"], [])
        self.assertEqual(self.report["sum"], ["0", "1"])
        self.assertTrue(self.report["sum_is_zero"])
        self.assertEqual(
            self.report["signs"],
            {
                "0123": 1, "0132": -1, "0213": -1, "0231": 1, "0312": 1, "0321": -1,
                "1023": -1, "1032": 1, "1203": 1, "1230": -1, "1302": -1, "1320": 1,
                "2013": 1, "2031": -1, "2103": -1, "2130": 1, "2301": 1, "2310": -1,
            },
        )
        signed = {item["orientation"]: item["signed"] for item in self.report["orientations"]}
        self.assertEqual(
            signed,
            {
                "0123": ["8655", "16"], "0132": ["-2817", "16"], "0213": ["18831", "8"],
                "0231": ["-21601", "8"], "0312": ["1457", "8"], "0321": ["-803", "4"],
                "1023": ["15705", "16"], "1032": ["-5667", "16"], "1203": ["1953", "4"],
                "1230": ["-4313", "4"], "1302": ["407", "8"], "1320": ["-353", "4"],
                "2013": ["-41517", "16"], "2031": ["42869", "16"], "2103": ["-22917", "16"],
                "2130": ["21869", "16"], "2301": ["131", "2"], "2310": ["-169", "2"],
            },
        )
        edge_1302 = next(item for item in self.report["orientations"] if item["orientation"] == "1302")
        self.assertEqual(edge_1302["unsigned"], ["-407", "8"])
        self.assertEqual(edge_1302["sign"], -1)
        self.assertTrue(all(item["signed"] != ["0", "1"] for item in self.report["orientations"]))

    def test_published_partial_edges_agree(self):
        self.assertEqual(len(self.report["published_agreement"]), 13)
        self.assertTrue(all(item["agrees"] and item["coefficient_arrays_agree"] for item in self.report["published_agreement"]))
        by_pr = {}
        for item in self.report["published_agreement"]:
            by_pr.setdefault(item["pr"], []).append(item["orientation"])
        self.assertEqual(by_pr[43], ["0123"])
        self.assertEqual(by_pr[46], ["0132", "0213", "0231"])
        self.assertEqual(by_pr[50], ["0312", "0321", "1023"])
        self.assertEqual(by_pr[51], ["1032", "1203", "1230"])
        self.assertEqual(by_pr[55], ["1302", "1320", "2013"])

    def test_fresh_edges_are_selector_readings_of_copied_quotients(self):
        fresh = {item["orientation"]: item["signed"] for item in self.report["fresh_recomputations"]}
        self.assertEqual(
            fresh,
            {
                "2031": ["42869", "16"],
                "2103": ["-22917", "16"],
                "2130": ["21869", "16"],
                "2301": ["131", "2"],
                "2310": ["-169", "2"],
            },
        )
        groups = [tuple(group["orientations"]) for group in self.report["duplicate_quotient_groups"]]
        self.assertEqual(
            groups,
            [
                ("0123", "2301"),
                ("0132", "2310"),
                ("0213", "2031"),
                ("0231", "2013"),
                ("0312", "2130"),
                ("0321", "2103"),
            ],
        )
        self.assertTrue(all(group["lists_identical"] and group["relation"] == "add 2 mod 4" for group in self.report["duplicate_quotient_groups"]))
        self.assertEqual(self.report["distinct_coefficient_arrays"], 12)
        self.assertEqual(self.report["data_defects"], [
            "supplied coefficient arrays are not distinct across orientations: "
            "0123=2301, 0132=2310, 0213=2031, 0231=2013, 0312=2130, 0321=2103"
        ])
        raw = {
            review.orientation_key(tuple(edge["roles"])): edge["integer_coefficients"]
            for edge in self.document["edges"]
        }
        self.assertEqual(raw["0123"], raw["2301"])
        self.assertEqual(raw["0123"][0], [4, 27, 22, "-600"])
        self.assertNotEqual(
            self.report["duplicate_quotient_groups"][0]["original_quotient_sha256"]["0123"],
            self.report["duplicate_quotient_groups"][0]["original_quotient_sha256"]["2301"],
        )

    def test_counts(self):
        self.assertEqual(self.report["quotient_terms_in_file"], 4014)
        self.assertEqual(self.report["selector_rows"], 3258)
        self.assertEqual(self.report["distinct_source_exponents"], 3258)
        self.assertEqual(self.report["nonzero_selected_coefficients"], 288)

    def test_recorded_total_tamper_is_an_arithmetic_defect(self):
        document = copy.deepcopy(self.document)
        document["edges"][0]["signed_contribution"] = ["1", "1"]
        report = review.audit(document, self.provenance, self.digest)
        self.assertTrue(any("0123 recorded" in item for item in report["arithmetic_defects"]))

    def test_command_exits_one_on_the_duplicate_defect(self):
        completed = subprocess.run(
            [sys.executable, str(HERE / "recompute_aggregate.py")],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 1, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["sum"], ["0", "1"])
        self.assertEqual(payload["arithmetic_defects"], [])
        self.assertTrue(payload["data_defects"])


if __name__ == "__main__":
    unittest.main()
