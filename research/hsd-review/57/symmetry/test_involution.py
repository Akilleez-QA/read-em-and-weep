"""The +2 (mod 4) quotient copies are the orbits of iota, and they do not cancel."""

import contextlib
import importlib.util
import io
import json
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("hsd57_iota", HERE / "check_involution.py")
check = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check)


class InvolutionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            cls.status = check.main()
        cls.report = json.loads(buffer.getvalue())

    def test_orbits_match_and_do_not_cancel(self):
        self.assertEqual(self.status, 0)
        report = self.report
        self.assertEqual(report["classification"], "expected symmetry")
        self.assertEqual(report["mismatches"], [])
        self.assertEqual(report["sign_iota"], 1)
        self.assertEqual(report["independent_quotients"], 12)
        self.assertEqual(report["distinct_lists"], 12)
        self.assertEqual(report["active_singleton_count"], 6)
        self.assertEqual(report["distinct_singleton_lists"], 6)
        self.assertEqual(report["audit_sum"], ["0", "1"])
        self.assertTrue(report["audit_sum_is_zero"])
        self.assertEqual(report["audit_orientation_count"], 18)
        self.assertEqual(report["failures"], [])
        self.assertTrue(report["every_pair_sum_nonzero"])
        self.assertEqual(report["sum_of_pair_sums"], ["0", "1"])
        self.assertEqual(report["sum_of_unpaired"], ["0", "1"])
        self.assertEqual(
            [tuple(item["orientations"]) for item in report["paired_readings"]],
            [
                ("0123", "2301"),
                ("0132", "2310"),
                ("0213", "2031"),
                ("0231", "2013"),
                ("0312", "2130"),
                ("0321", "2103"),
            ],
        )
        self.assertEqual(
            [item["pair_sum"] for item in report["paired_readings"]],
            [
                ["9703", "16"],
                ["-4169", "16"],
                ["80531", "16"],
                ["-84719", "16"],
                ["24783", "16"],
                ["-26129", "16"],
            ],
        )
        partners = {item["orientation"]: item["inactive_partner"] for item in report["unpaired_readings"]}
        self.assertEqual(
            partners,
            {
                "1023": "3201",
                "1032": "3210",
                "1203": "3021",
                "1230": "3012",
                "1302": "3120",
                "1320": "3102",
            },
        )


if __name__ == "__main__":
    unittest.main()
