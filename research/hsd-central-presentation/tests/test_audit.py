"""Pins, pairing identities, and the stop rule for the exported cokernel C."""

from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
import sys

sys.path.insert(0, str(ROOT))

import audit


def _walk_keys(value):
    if isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from _walk_keys(item)
    elif isinstance(value, list):
        for item in value:
            yield from _walk_keys(item)


class TranscriptOrderTest(unittest.TestCase):
    def test_pins_precede_identities(self):
        transcript = audit.run()
        labels = [label for label, _ in transcript]
        self.assertEqual(labels, ["pins", "identities", "report"])
        pins = transcript[0][1]
        self.assertEqual(pins["module"]["name"], "C")
        self.assertFalse(pins["module"]["labelled_R"])
        self.assertIn(audit.FORMAL_CHART, json.dumps(pins))
        self.assertIn(audit.PLANE_COMPLETION, json.dumps(pins))
        self.assertEqual(pins["central_equation"]["equation"], "t0 = 0")
        self.assertEqual(pins["central_equation"]["finite_representative"], "z")
        self.assertEqual(pins["proposed_comparison"]["hm_pullback_on_C4"], "excluded")


class IdentityTest(unittest.TestCase):
    def test_transition_and_cubic_identities(self):
        identities = audit.evaluate_identities()
        self.assertTrue(identities["tb_ri_equals_z3_r0"])
        self.assertTrue(identities["g_C_plus_z3_W6_equals_S3"])
        self.assertTrue(identities["a0_square_identity"])
        self.assertTrue(identities["w1_column_matches_r0"])
        self.assertTrue(identities["column_independent_of_h"])

    def test_zero_section_pairing_is_not_the_required_value(self):
        identities = audit.evaluate_identities()
        self.assertEqual(identities["zero_section_pairing"], "0")
        self.assertEqual(identities["required_finite_pairing"], "h*z")
        self.assertFalse(identities["zero_section_matches_required"])
        self.assertTrue(identities["corrected_local_matches_required"])
        self.assertEqual(identities["psi_E0_coefficient_in_zero_section"], "0")
        z, h = sp.symbols("z h")
        self.assertNotEqual(sp.expand(z * h), 0)


class StopRuleTest(unittest.TestCase):
    def test_report_stops_without_a_length(self):
        transcript = audit.run()
        report = transcript[2][1]
        self.assertEqual(report["cokernel_name"], "C")
        self.assertFalse(report["labelled_R"])
        self.assertTrue(report["stopped"])
        self.assertEqual(report["gate_1_reflexivity"]["status"], "not_run")
        self.assertIsNone(report["gate_1_reflexivity"]["failed_inequality"])
        self.assertEqual(report["gate_2_identification"]["status"], "failed")
        self.assertFalse(report["gate_2_identification"]["actual_isomorphism_exported"])
        self.assertIn("phi: C|U -> E|U", report["gate_2_identification"]["missing_map"])
        self.assertIn("Weil-class", report["scope"])
        for key in _walk_keys(report):
            self.assertNotIn("length", key.lower())


class PinnedBlobTest(unittest.TestCase):
    quotes = [
        (
            audit.FORMAL_CHART,
            "research/carrier/formal-five-parameter-chart/formal-chart.md",
            "beta(v)=+t0 h",
        ),
        (
            audit.FORMAL_CHART,
            "research/carrier/formal-five-parameter-chart/formal-chart.md",
            "None of those operations is computed here.",
        ),
        (
            audit.PLANE_COMPLETION,
            "research/carrier/plane-completion-lemma/PLANE_COMPLETION_LEMMA.md",
            "Leaving v=E0 unchanged gives zero normal pairing.",
        ),
        (
            audit.PLANE_COMPLETION,
            "research/carrier/plane-completion-lemma/PLANE_COMPLETION_LEMMA.md",
            "These local sections do not automatically glue",
        ),
        (
            audit.PLANE_COMPLETION,
            "research/carrier/plane-completion-lemma/PLANE_COMPLETION_LEMMA.md",
            "does not supply the chart's prescribed nonzero first-normal pairing",
        ),
        (
            audit.PLANE_COMPLETION,
            "research/carrier/plane-completion-lemma/EXPLICIT_BASE_ISOMETRY.md",
            "admit a global section reducing to E0 and satisfying",
        ),
        (
            audit.PLANE_COMPLETION,
            "research/carrier/plane-completion-lemma/first-normal-comparison/FIRST_NORMAL_COMPARISON.md",
            "It does not identify an ancestor, carrier or defect",
        ),
        (
            audit.PLANE_COMPLETION,
            "research/carrier/plane-completion-lemma/second-normal-comparison/SECOND_NORMAL_COMPARISON.md",
            "It does not construct an ancestor or algebraic carrier",
        ),
        (
            audit.PLANE_COMPLETION,
            "research/carrier/plane-completion-lemma/third-normal-comparison/THIRD_NORMAL_SECTION.md",
            "It does not identify an ancestor or algebraic carrier",
        ),
        (
            audit.HM_ATLAS,
            "research/hm-carrier-and-atlas.md",
            "X=C⁴",
        ),
    ]

    def test_cited_sentences_are_in_the_pinned_blobs(self):
        for commit, path, sentence in self.quotes:
            with self.subTest(commit=commit, path=path):
                probe = subprocess.run(
                    ["git", "cat-file", "-e", f"{commit}:{path}"],
                    cwd=ROOT.parents[1],
                    capture_output=True,
                )
                if probe.returncode != 0:
                    self.skipTest(f"pinned blob absent: {commit}:{path}")
                show = subprocess.run(
                    ["git", "show", f"{commit}:{path}"],
                    cwd=ROOT.parents[1],
                    capture_output=True,
                    check=True,
                )
                text = show.stdout.decode()
                self.assertIn(sentence, text)

    def test_order_1_is_a_deformation_complex_not_phi(self):
        commit = audit.FORMAL_CHART
        path = "research/carrier/formal-five-parameter-chart/data/order_1.json"
        probe = subprocess.run(
            ["git", "cat-file", "-e", f"{commit}:{path}"],
            cwd=ROOT.parents[1],
            capture_output=True,
        )
        if probe.returncode != 0:
            self.skipTest("order_1.json blob absent")
        show = subprocess.run(
            ["git", "show", f"{commit}:{path}"],
            cwd=ROOT.parents[1],
            capture_output=True,
            check=True,
        )
        payload = json.loads(show.stdout.decode())
        self.assertEqual(
            set(payload),
            {
                "AI_basis",
                "BI_basis",
                "D_shape",
                "D_sparse",
                "Ev_shape",
                "Ev_sparse",
                "N_shape",
                "N_sparse",
                "preimage_x_sparse",
                "source_basis",
                "target_b_sparse",
                "target_basis",
            },
        )

    def test_named_defect_branch_has_no_research_files(self):
        probe = subprocess.run(
            ["git", "cat-file", "-e", audit.EMPTY_DEFECT_BRANCH],
            cwd=ROOT.parents[1],
            capture_output=True,
        )
        if probe.returncode != 0:
            self.skipTest("defect-branch commit absent")
        show = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", audit.EMPTY_DEFECT_BRANCH, "--", "research"],
            cwd=ROOT.parents[1],
            capture_output=True,
            check=True,
        )
        self.assertEqual(show.stdout.decode().strip(), "")


if __name__ == "__main__":
    unittest.main()
