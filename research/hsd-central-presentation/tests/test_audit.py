"""Pins, pairing identities, and the stop rule for the exported cokernel C."""

from __future__ import annotations

import json
import os
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
        self.assertFalse(pins["proposed_comparison"]["phi_mod_h3_exported"])
        self.assertEqual(pins["structure_group"]["lie_sheaf_rank"], 6)
        self.assertEqual(pins["structure_group"]["not_the_lie_sheaf"], "sp(G)")
        self.assertEqual(pins["torus_weights"]["wt_z_X_Y_W_h"], [2, 1, 1, 0, -1])
        self.assertEqual(pins["proposed_comparison"]["route"], "finite jet over D2 = {h^3 = 0}")
        self.assertFalse(pins["symbols"]["same_object"])
        self.assertIn("generator", pins["symbols"]["p"])
        self.assertIn("beta(s)=t0 h", pins["symbols"]["s"])
        self.assertEqual(pins["symbols"]["beta_of_alpha_p"], "0")
        joined = " ".join(pins["checks_mod_h3"])
        self.assertIn("phi(alpha(p))", joined)
        self.assertIn("phi(s) = s'", joined)
        self.assertIn("no section hypothesis and no H^0", joined)
        self.assertNotIn("v_i", joined)


class IdentityTest(unittest.TestCase):
    def test_transition_and_cubic_identities(self):
        identities = audit.evaluate_identities()
        self.assertTrue(identities["tb_ri_equals_z3_r0"])
        self.assertTrue(identities["g_C_plus_z3_W6_equals_S3"])
        self.assertTrue(identities["a0_square_identity"])
        self.assertTrue(identities["w1_column_matches_r0"])
        self.assertTrue(identities["column_independent_of_h"])
        self.assertEqual(identities["h_derivatives"], ["0", "0", "0", "0", "0"])
        self.assertTrue(identities["q_of_u_is_zero"])
        self.assertTrue(identities["q_after_section_is_identity"])
        self.assertTrue(identities["kernel_is_scalar_times_u"])
        self.assertTrue(identities["unit_entry_is_one"])
        self.assertEqual(identities["unit_entry_index"], 1)

    def test_marked_generator_is_not_the_paired_section(self):
        identities = audit.evaluate_identities()
        self.assertEqual(identities["beta_of_alpha_p"], "0")
        self.assertEqual(identities["beta_of_unchanged_s"], "0")
        self.assertNotEqual(identities["beta_of_alpha_p"], identities["required_finite_pairing"])

    def test_zero_section_pairing_is_not_the_required_value(self):
        identities = audit.evaluate_identities()
        self.assertEqual(identities["zero_section_pairing"], "0")
        self.assertEqual(identities["required_finite_pairing"], "h*z")
        self.assertFalse(identities["zero_section_matches_required"])
        self.assertTrue(identities["corrected_local_matches_required"])
        self.assertEqual(identities["psi_E0_coefficient_in_zero_section"], "0")
        z, h = sp.symbols("z h")
        self.assertNotEqual(sp.expand(z * h), 0)

    def test_stabilizer_is_rank_six_and_order0_frame_has_no_h(self):
        structure = audit.structure_group_counts()
        self.assertTrue(structure["line_is_isotropic"])
        self.assertEqual(structure["perpendicular_rank"], 3)
        self.assertEqual(structure["radical_of_perpendicular_rank"], 1)
        self.assertFalse(structure["P_is_lagrangian"])
        self.assertEqual(structure["stabilizer_lie_rank"], 6)
        self.assertEqual(structure["sym2_of_rank3_bundle_rank"], 6)
        self.assertTrue(structure["order0_frame_fixes_P_generator"])
        self.assertFalse(structure["order0_frame_depends_on_h"])


class StopRuleTest(unittest.TestCase):
    def test_report_stops_without_a_length(self):
        transcript = audit.run()
        report = transcript[2][1]
        decisions = report["reporting_decisions"]
        self.assertEqual(report["cokernel_name"], "C")
        self.assertNotIn("stopped", report)
        self.assertNotIn("gate_1_reflexivity", report)
        self.assertNotIn("gate_2_identification", report)
        self.assertIn("reporting decisions, not computed certificates", decisions["label"])
        self.assertFalse(decisions["labelled_R"])
        self.assertTrue(decisions["stopped"]["value"])
        self.assertEqual(decisions["gate_1_on_W_nonzero"]["status"], "passed")
        self.assertIn("does not identify C with R", decisions["gate_1_on_W_nonzero"]["consequence"])
        section = decisions["gate_2_structured_section"]
        self.assertEqual(section["status"], "computed")
        self.assertFalse(section["pairing_holds"])
        self.assertIn("s=E0", section["chosen_section"])
        self.assertIn("not the generator p", section["chosen_section"])
        underlying = decisions["gate_2_underlying_sheaf_comparison"]
        self.assertEqual(underlying["status"], "open")
        self.assertTrue(underlying["not_failed"])
        self.assertIn("phi(alpha(p))=alpha'(p)", underlying["missing_map"])
        self.assertIn("phi(s)=s'", underlying["missing_map"])
        self.assertIn("no section hypothesis and no H^0", underlying["missing_map"])
        self.assertNotIn("v_i", underlying["missing_map"])
        self.assertIn("not an input to check (d)", decisions["deformation_citation"])
        self.assertIn("Alper", decisions["deformation_citation"])
        self.assertNotIn("Koll", decisions["deformation_citation"])
        self.assertIn("conditional on phi", decisions["presentation_shape"])
        self.assertIn("Weil-class", report["scope"])
        for key in _walk_keys(report):
            self.assertNotIn("length", key.lower())


def _blob_missing(spec):
    probe = subprocess.run(
        ["git", "cat-file", "-e", spec],
        cwd=ROOT.parents[1],
        capture_output=True,
    )
    return probe.returncode != 0


def provenance_absence_count():
    """How many pinned-blob checks would skip. A skip is not verified provenance."""
    missing = 0
    for commit, path, _sentence in PinnedBlobTest.quotes:
        if _blob_missing(f"{commit}:{path}"):
            missing += 1
    order_1 = "research/carrier/formal-five-parameter-chart/data/order_1.json"
    if _blob_missing(f"{audit.FORMAL_CHART}:{order_1}"):
        missing += 1
    if _blob_missing(audit.EMPTY_DEFECT_BRANCH):
        missing += 1
    return missing


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
            "fixes P",
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

    def _require_blob(self, spec, message=None):
        if not _blob_missing(spec):
            return
        text = message or f"pinned blob absent: {spec}"
        text += ". A skip is not verified provenance."
        if os.environ.get("REQUIRE_PINNED_BLOBS") == "1":
            self.fail(text)
        self.skipTest(text)

    def test_provenance_skip_count(self):
        count = provenance_absence_count()
        print(f"provenance_skip_count={count}")
        if os.environ.get("REQUIRE_PINNED_BLOBS") == "1":
            self.assertEqual(count, 0)

    def test_cited_sentences_are_in_the_pinned_blobs(self):
        for commit, path, sentence in self.quotes:
            with self.subTest(commit=commit, path=path):
                self._require_blob(f"{commit}:{path}")
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
        self._require_blob(f"{commit}:{path}", "order_1.json blob absent")
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
        self._require_blob(audit.EMPTY_DEFECT_BRANCH, "defect-branch commit absent")
        show = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", audit.EMPTY_DEFECT_BRANCH, "--", "research"],
            cwd=ROOT.parents[1],
            capture_output=True,
            check=True,
        )
        self.assertEqual(show.stdout.decode().strip(), "")


if __name__ == "__main__":
    unittest.main()
