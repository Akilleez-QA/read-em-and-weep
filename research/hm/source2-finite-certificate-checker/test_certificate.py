#!/usr/bin/env python3
"""All data below are universal/synthetic, not an HM source realization."""
import copy
import json
import math
import unittest
from fractions import Fraction

import check_certificate as c


def mat(rows, cols, terms=()):
    return {"rows": rows, "cols": cols, "terms": list(terms)}


def term(r, col, e, num=1, den=1):
    q = Fraction(num, den)
    return [r, col, list(e), [q.numerator, q.denominator]]


def constant(rows, cols, values):
    return mat(rows, cols, (term(r, col, c.ZERO, v.numerator, v.denominator)
                           for (r, col), value in values.items()
                           if (v := Fraction(value))))


def seal(data):
    return {"schema": c.SCHEMA,
            "binding": {"theorem_commit": c.COMMIT,
                        "theorem_sha256": c.THEOREM_SHA256,
                        "data_sha256": c.canonical_digest(data)},
            "data": data}


def fixture():
    # Q has a free third column. Its image coordinates scale by 2 and 3.
    # T = Q diag((a0+a2)/2,(a1+a2)/2,0). A C2 action swaps a0,a1.
    # x_i = ((-(a0+a2)/2)^i, (-(a1+a2)/2)^i, a2^i/7).
    # The third component is omitted at i=0. No HM map is modeled here.
    q = constant(2, 3, {(0, 0): 2, (1, 1): 3})
    t = mat(2, 3, [term(0, 0, (1, 0, 0)), term(0, 0, (0, 0, 1)),
                   term(1, 1, (0, 1, 0), 3, 2), term(1, 1, (0, 0, 1), 3, 2)])
    s = constant(3, 1, {(0, 0): 1, (1, 0): 1})
    inc = constant(2, 1, {(0, 0): 2, (1, 0): 3})
    xs = []
    for i in range(24):
        terms = []
        for j in range(i + 1):
            num = (-1) ** i * math.comb(i, j)
            terms += [term(0, 0, (j, 0, i - j), num, 2 ** i),
                      term(1, 0, (0, j, i - j), num, 2 ** i)]
        if i:
            terms.append(term(2, 0, (0, 0, i), 1, 7))
        xs.append(mat(3, 1, terms))
    g = {"name": "synthetic coordinate swap",
         "A": constant(3, 3, {(0, 1): 1, (1, 0): 1, (2, 2): 1}),
         "N": constant(3, 3, {(0, 1): 1, (1, 0): 1, (2, 2): 1}),
         "M": constant(2, 2, {(0, 1): Fraction(2, 3), (1, 0): Fraction(3, 2)}),
         "P": constant(1, 1, {(0, 0): 1})}
    return seal({"variables": ["a0", "a1", "a2"], "dimensions": {"N": 3, "M": 2, "P": 1},
                 "maps": {"Q": q, "T": t, "s": s, "i_P": inc},
                 "corrections": xs, "generators": [g]})


class CertificateTests(unittest.TestCase):
    def bad_data(self, mutate, pattern):
        cert = fixture()
        mutate(cert["data"])
        cert = seal(cert["data"])
        with self.assertRaisesRegex(c.InvalidCertificate, pattern):
            c.check(cert)

    def test_synthetic_rational_equivariant_chain(self):
        cert = fixture()
        result = c.check(cert, cert["binding"]["data_sha256"])
        self.assertEqual(result["status"], "ALGEBRAIC_IDENTITIES_VERIFIED")
        self.assertEqual(result["correction_equations"], 24)
        self.assertEqual(result["supplied_generator_equivariance"], "CHECKED")
        self.assertEqual(result["actual_original_positive_rank"], "NOT_DETERMINED")
        self.assertFalse(result["original_positive_shape"])

    def test_nonzero_tail_is_permitted(self):
        cert = fixture()
        b = c.Budget()
        t = c.matrix(cert["data"]["maps"]["T"], 2, 3, 1, b, "T")
        x23 = c.matrix(cert["data"]["corrections"][23], 3, 1, 23, b, "x23")
        self.assertTrue(c.product(t, x23, b))
        c.check(cert)

    def test_exact_truncated_series_residual(self):
        # Direct coefficient collection verifies (Q+tT) sum(t^i x_i)
        # = i_P + t^24 T*x23. It does not infer that T*x23 is zero.
        data = fixture()["data"]
        b = c.Budget()
        q = c.matrix(data["maps"]["Q"], 2, 3, 0, b, "Q")
        t = c.matrix(data["maps"]["T"], 2, 3, 1, b, "T")
        xs = [c.matrix(x, 3, 1, i, b, "x") for i, x in enumerate(data["corrections"])]
        coefficients = [{} for _ in range(25)]
        for i, x in enumerate(xs):
            for key, value in c.product(q, x, b).items():
                c.accumulate(coefficients[i], key, value)
            for key, value in c.product(t, x, b).items():
                c.accumulate(coefficients[i + 1], key, value)
        self.assertEqual(coefficients[0], c.matrix(data["maps"]["i_P"], 2, 1, 0, b, "i_P"))
        self.assertTrue(all(not p for p in coefficients[1:24]))
        self.assertEqual(coefficients[24], c.product(t, xs[23], b))
        self.assertGreater(3 * 2 + 25, 30)

    def test_optional_equivariance_is_not_claimed(self):
        cert = fixture()
        cert["data"]["generators"] = []
        r = c.check(seal(cert["data"]))
        self.assertEqual(r["supplied_generator_equivariance"], "NOT_CHECKED")

    def test_original_truncation_has_first_possible_term_at_order25(self):
        # A second synthetic example checks the original one-order shift:
        # Q=[1,0], T=[a0,a1], s=(1,0), d=(0,1), L=a1.
        b = c.Budget()
        q = {(0, 0, c.ZERO): Fraction(1)}
        t = {(0, 0, (1, 0, 0)): Fraction(1), (0, 1, (0, 1, 0)): Fraction(1)}
        d = {(1, 0, c.ZERO): Fraction(1)}
        L = {(0, 0, (0, 1, 0)): Fraction(1)}
        xs = [{(0, 0, (i, 0, 0)): Fraction((-1) ** i)} for i in range(24)]
        coefficients = [{} for _ in range(26)]
        for key, value in c.product(q, d, b).items():
            c.accumulate(coefficients[0], key, value)
        for key, value in c.product(t, d, b).items():
            c.accumulate(coefficients[1], key, value)
        for i, x in enumerate(xs):
            xL = c.product(x, L, b)
            for key, value in c.product(q, xL, b).items():
                c.accumulate(coefficients[i + 1], key, -value)
            for key, value in c.product(t, xL, b).items():
                c.accumulate(coefficients[i + 2], key, -value)
        self.assertTrue(all(not p for p in coefficients[:25]))
        self.assertEqual(coefficients[25], {(0, 0, (24, 1, 0)): Fraction(1)})

    def test_zero_formal_data_does_not_authenticate_geometry(self):
        # Shapes alone do not identify the actual 37-by41 original pencil.
        data = {"variables": ["a0", "a1", "a2"], "dimensions": {"N": 41, "M": 37, "P": 4},
                "maps": {"Q": mat(37, 41), "T": mat(37, 41), "s": mat(41, 4), "i_P": mat(37, 4)},
                "corrections": [mat(41, 4) for _ in range(24)], "generators": []}
        result = c.check(seal(data))
        self.assertTrue(result["original_positive_shape"])
        self.assertEqual(result["actual_map_authentication"], "NOT_ESTABLISHED")
        self.assertEqual(result["actual_original_positive_rank"], "NOT_DETERMINED")

    def test_unsorted_terms_have_unambiguous_meaning(self):
        cert = fixture()
        for x in cert["data"]["corrections"]:
            x["terms"].reverse()
        c.check(seal(cert["data"]))

    def test_serialization_round_trip(self):
        cert = fixture()
        self.assertEqual(c.check(c.load_bytes(json.dumps(cert).encode())), c.check(cert))

    def test_substitution_mixes_all_three_coordinates_exactly(self):
        b = c.Budget()
        # (a0+2*a1-3*a2)^2 expands with six independently specified terms.
        a = {(0, 0, (2, 0, 0)): Fraction(1)}
        action = {(0, 0, c.ZERO): Fraction(1), (0, 1, c.ZERO): Fraction(2),
                  (0, 2, c.ZERO): Fraction(-3), (1, 1, c.ZERO): Fraction(1),
                  (2, 2, c.ZERO): Fraction(1)}
        expected = {(0, 0, e): Fraction(v) for e, v in
                    [((2, 0, 0), 1), ((0, 2, 0), 4), ((0, 0, 2), 9),
                     ((1, 1, 0), 4), ((1, 0, 1), -6), ((0, 1, 1), -12)]}
        self.assertEqual(c.substitute(a, action, b), expected)

    def test_wrong_last_coefficient_rejected_even_when_rehashed(self):
        self.bad_data(lambda d: d["corrections"][23]["terms"][0].__setitem__(3, [1, 1]), "identity fails at x23")

    def test_wrong_sign_rejected(self):
        self.bad_data(lambda d: d["corrections"][1]["terms"][0].__setitem__(3, [1, 2]), "identity fails at x1")

    def test_wrong_inclusion_rejected(self):
        self.bad_data(lambda d: d["maps"]["i_P"]["terms"][0].__setitem__(3, [5, 1]), "Q\\*x0")

    def test_wrong_seed_rejected(self):
        self.bad_data(lambda d: d["maps"]["s"]["terms"].append(term(2, 0, c.ZERO)), "x0 does not equal")

    def test_fewer_corrections_rejected(self):
        self.bad_data(lambda d: d["corrections"].pop(), "exactly x0")

    def test_extra_correction_rejected(self):
        self.bad_data(lambda d: d["corrections"].append(mat(3, 1)), "exactly x0")

    def test_wrong_homogeneity_rejected(self):
        self.bad_data(lambda d: d["corrections"][2]["terms"][0].__setitem__(2, [0, 0, 1]), "homogeneous")

    def test_negative_exponent_rejected(self):
        self.bad_data(lambda d: d["corrections"][1]["terms"][0].__setitem__(2, [-1, 0, 2]), "exponent")

    def test_wrong_exponent_length_rejected(self):
        self.bad_data(lambda d: d["corrections"][1]["terms"][0].__setitem__(2, [1, 0]), "exponent")

    def test_zero_denominator_rejected(self):
        self.bad_data(lambda d: d["maps"]["Q"]["terms"][0].__setitem__(3, [1, 0]), "denominator")

    def test_negative_denominator_rejected(self):
        self.bad_data(lambda d: d["maps"]["Q"]["terms"][0].__setitem__(3, [-2, -1]), "denominator")

    def test_unreduced_coefficient_rejected(self):
        self.bad_data(lambda d: d["maps"]["Q"]["terms"][0].__setitem__(3, [4, 2]), "reduced")

    def test_explicit_zero_rejected(self):
        self.bad_data(lambda d: d["maps"]["Q"]["terms"][0].__setitem__(3, [0, 1]), "nonzero")

    def test_bool_coefficient_rejected(self):
        self.bad_data(lambda d: d["maps"]["Q"]["terms"][0].__setitem__(3, [True, 1]), "rational pair")

    def test_duplicate_monomial_rejected(self):
        self.bad_data(lambda d: d["maps"]["Q"]["terms"].append(copy.deepcopy(d["maps"]["Q"]["terms"][0])), "duplicate entry")

    def test_shape_rejected(self):
        self.bad_data(lambda d: d["maps"]["Q"].__setitem__("rows", 3), "shape")

    def test_bool_shape_rejected(self):
        self.bad_data(lambda d: d["maps"]["s"].__setitem__("cols", True), "shape")

    def test_out_of_range_index_rejected(self):
        self.bad_data(lambda d: d["maps"]["Q"]["terms"][0].__setitem__(0, 2), "index")

    def test_bool_index_rejected(self):
        self.bad_data(lambda d: d["maps"]["Q"]["terms"][0].__setitem__(0, False), "index")

    def test_zero_dimension_rejected(self):
        self.bad_data(lambda d: d["dimensions"].__setitem__("P", 0), "dimension")

    def test_bool_dimension_rejected(self):
        self.bad_data(lambda d: d["dimensions"].__setitem__("P", True), "dimension")

    def test_unknown_fields_rejected(self):
        self.bad_data(lambda d: d.__setitem__("actual_maps_authenticated", True), "fields")

    def test_singular_action_rejected(self):
        self.bad_data(lambda d: d["generators"][0].__setitem__("A", mat(3, 3)), "singular")

    def test_duplicate_generator_name_rejected(self):
        self.bad_data(lambda d: d["generators"].append(copy.deepcopy(d["generators"][0])), "unique")

    def test_generator_equivariance_rejected(self):
        # A kernel correction preserves all q equations but breaks equivariance.
        self.bad_data(lambda d: d["corrections"][1]["terms"].append(term(2, 0, (1, 0, 0))), "equivariance fails for x1")

    def test_wrong_target_action_rejected(self):
        self.bad_data(lambda d: d["generators"][0].__setitem__("M", constant(2, 2, {(0, 0): 1, (1, 1): 1})), "equivariance fails for Q")

    def test_stale_digest_rejected(self):
        cert = fixture()
        cert["data"]["generators"] = []
        with self.assertRaisesRegex(c.InvalidCertificate, "data digest mismatch"):
            c.check(cert)

    def test_wrong_expected_digest_rejected(self):
        with self.assertRaisesRegex(c.InvalidCertificate, "caller-supplied"):
            c.check(fixture(), "0" * 64)

    def test_wrong_theorem_pin_rejected(self):
        cert = fixture()
        cert["binding"]["theorem_commit"] = "0" * 40
        with self.assertRaisesRegex(c.InvalidCertificate, "theorem pin"):
            c.check(cert)

    def test_duplicate_json_key_rejected(self):
        with self.assertRaisesRegex(c.InvalidCertificate, "duplicate JSON key"):
            c.load_bytes(b'{"schema":"a","schema":"b"}')

    def test_float_and_nonfinite_json_rejected(self):
        for number in (b"1.0", b"NaN", b"Infinity", b"-Infinity"):
            with self.subTest(number=number), self.assertRaises(c.InvalidCertificate):
                c.load_bytes(b'{"n":' + number + b'}')

    def test_byte_limit_is_inconclusive(self):
        with self.assertRaises(c.ResourceLimit):
            c.load_bytes(b" " * (c.MAX_BYTES + 1))

    def test_coefficient_bit_limit_is_inconclusive(self):
        self.bad_data(lambda d: d["maps"]["Q"]["terms"][0].__setitem__(3, [2 ** 513, 1]), "bit bound")

    def test_operation_limit_is_inconclusive(self):
        b = c.Budget()
        with self.assertRaises(c.ResourceLimit):
            b.tick(c.MAX_OPERATIONS + 1)

    def test_dimension_limit_is_inconclusive(self):
        cert = fixture()
        cert["data"]["dimensions"]["N"] = c.MAX_DIM + 1
        with self.assertRaises(c.ResourceLimit):
            c.check(seal(cert["data"]))

    def test_generator_count_limit_is_inconclusive(self):
        cert = fixture()
        cert["data"]["generators"] *= 9
        with self.assertRaises(c.ResourceLimit):
            c.check(seal(cert["data"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
