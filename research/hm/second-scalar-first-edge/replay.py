#!/usr/bin/env python3
"""Exact downstream replay of ONE supplied second-map quotient, using Fractions.

No source DAG is read or evaluated. Checks are explicit and remain active under -O.
"""
import hashlib
import itertools
import json
from fractions import Fraction
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAP = "X02[0,5]-X13[10,1]"
SHAPE = [9, 44, 23]
M = [2, 2, 2, 0]
ROLES = [0, 1, 2, 3]
DATA_FILES = {"quotient.json", "request.json", "expected.json", "kernels.json",
              "right-prefactor.json", "provenance.json", "model.json"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value):
    require(type(value) is str, "Exact integers must be decimal strings")
    try:
        answer = int(value)
    except ValueError as error:
        raise ValueError("Invalid integer") from error
    require(str(answer) == value, "Noncanonical integer")
    return answer


def encode(value):
    value = Fraction(value)
    return [str(value.numerator), str(value.denominator)]


def rational(value):
    require(type(value) is list and len(value) == 2, "Invalid rational pair")
    numerator, denominator = map(integer, value)
    require(denominator > 0, "Nonpositive denominator")
    answer = Fraction(numerator, denominator)
    require(encode(answer) == value, "Unreduced rational pair")
    return answer


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "Duplicate JSON key")
        result[key] = value
    return result


def load(path):
    return json.loads(Path(path).read_text(), object_pairs_hook=unique_object)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def verify_manifest(directory=HERE):
    directory = Path(directory)
    require(not (directory / "manifest.json").is_symlink(), "Symlinked manifest")
    manifest = load(directory / "manifest.json")
    require(manifest["schema"] == "second-scalar-first-edge-package-v1",
            "Wrong manifest schema")
    require(manifest["scope"] == "All distributed files except manifest.json itself",
            "Ambiguous manifest scope")
    files = manifest["files"]
    require(DATA_FILES <= set(files), "Missing data manifest entry")
    require(all(p.is_file() or (p.name == "__pycache__" and p.is_dir())
                for p in directory.iterdir()), "Unexpected package directory")
    actual = {p.name for p in directory.iterdir() if p.is_file()
              and p.name != "manifest.json"}
    require(actual == set(files), "Unexpected or missing distributed file")
    for name, record in files.items():
        require(Path(name).name == name and name not in (".", ".."),
                "Invalid manifest path")
        path = directory / name
        require(not path.is_symlink(), "Symlinked package file")
        require(record == {"sha256": digest(path), "bytes": path.stat().st_size},
                "Package digest mismatch: " + name)
    return len(files)


def multiply(a, b, shape=None):
    """Plain tuple convolution; all coefficients are exact Fraction objects."""
    result = {}
    for x, c in a.items():
        for y, d in b.items():
            require(len(x) == len(y), "Mixed polynomial dimensions")
            key = tuple(i + j for i, j in zip(x, y))
            if shape is None or all(i < bound for i, bound in zip(key, shape)):
                result[key] = result.get(key, Fraction(0)) + c * d
    return {key: coefficient for key, coefficient in result.items() if coefficient}


def power(polynomial, exponent, shape):
    require(type(exponent) is int and exponent >= 0, "Invalid power")
    result = {(0,) * len(shape): Fraction(1)}
    while exponent:
        if exponent % 2:
            result = multiply(result, polynomial, shape)
        exponent //= 2
        if exponent:
            polynomial = multiply(polynomial, polynomial, shape)
    return result


def kernel_polynomial(method="inverse"):
    shape = (9, 23)
    h = {(0, 1): Fraction(1), (1, 0): Fraction(1), (1, 1): Fraction(3),
         (1, 2): Fraction(1), (2, 1): Fraction(1), (2, 2): Fraction(1)}
    one = {(0, 0): Fraction(1)}
    current = dict(one)
    answer = dict(one)
    require(method in ("inverse", "binomial"), "Unknown kernel method")
    # Every term of H has positive total degree. T^9=z^23=0 gives H^31=0.
    for n in range(1, 31):
        current = multiply(current, h, shape)
        scalar = (-1) ** n
        if method == "binomial":
            scalar *= comb(69 + n, n)
        for key, coefficient in current.items():
            answer[key] = answer.get(key, Fraction(0)) + scalar * coefficient
    require(not multiply(current, h, shape), "Nilpotence bound failed")
    answer = {key: coefficient for key, coefficient in answer.items() if coefficient}
    g = {**one, **h}
    if method == "inverse":
        require(multiply(g, answer, shape) == one, "Inverse identity failed")
        answer = power(answer, 70, shape)
    require(multiply(power(g, 70, shape), answer, shape) == one,
            "Kernel inverse-power identity failed")
    require(all(c.denominator == 1 for c in answer.values()), "Nonintegral kernel")
    return answer


def parse_quotient(q):
    require(q["schema"] == "second-scalar-supplied-quotient-v1", "Wrong quotient schema")
    require(q["scalar_map"] == MAP and q["field"] == "Q", "Wrong map or field")
    require(q["roles"] == ROLES and all(type(x) is int for x in q["roles"]),
            "Wrong quotient orientation")
    require(q["shape"] == SHAPE and all(type(x) is int for x in q["shape"]),
            "Wrong quotient shape")
    require(q["homogeneous_degrees_separated"] is True and
            q["pairing_aggregated"] is False, "Lost homogeneous grading")
    denominator = integer(q["common_denominator"])
    require(denominator == 64, "Unexpected root denominator")
    rows = q["integer_coefficients"]
    require(type(rows) is list and len(rows) == 203, "Wrong full quotient term count")
    values = {}
    slots = []
    for row in rows:
        require(type(row) is list and len(row) == 4, "Invalid quotient row")
        slot = tuple(row[:3])
        require(all(type(x) is int and 0 <= x < limit for x, limit in zip(slot, SHAPE)),
                "Out-of-range quotient slot")
        coefficient = integer(row[3])
        require(coefficient != 0 and slot not in values, "Zero or duplicate quotient term")
        slots.append(slot)
        values[slot] = Fraction(coefficient, denominator)
    require(slots == sorted(slots), "Unsorted quotient terms")
    payload = json.dumps(rows, separators=(",", ":")).encode()
    require(hashlib.sha256(payload).hexdigest() == q["coefficient_array_sha256"],
            "Coefficient-array digest mismatch")
    return values


def selector_rows(values, kernels):
    """Only roles 0123 and m2220; unknown orientations cannot enter this API."""
    rows = []
    i, j, k, l = ROLES
    degree_sum = sum(M)
    d, low_degree, homogeneous_slot = 6 + M[j], 22 - M[l], 35 + degree_sum
    for r in range(d + 1):
        for ell in range(low_degree + 1):
            slot = (r, homogeneous_slot, ell)
            coefficient = values.get(slot, Fraction(0))
            weight = kernels.get((d - r, low_degree - ell), Fraction(0))
            require(weight.denominator == 1, "Nonintegral weight")
            exponents = [0] * 4
            exponents[i], exponents[j], exponents[k], exponents[l] = (
                272, 215 - r, 157 - degree_sum + r - ell, 47 + ell)
            require(sum(exponents) == 691 - degree_sum, "Wrong source homogeneous degree")
            rows.append({"slot": list(slot), "source_exponents": exponents,
                         "kernel_weight": str(weight.numerator),
                         "coefficient": encode(coefficient),
                         "weighted_contribution": encode(coefficient * weight)})
    return rows


def verify_request(request, values, kernels):
    require(request["schema"] == "second-scalar-first-edge-request-v1", "Wrong request schema")
    require(request["scalar_map"] == MAP and request["field"] == "Q", "Wrong request map")
    require(request["roles"] == ROLES and request["pairing_monomial"] == M,
            "Unsupported request")
    require(all(type(x) is int for x in request["roles"] + request["pairing_monomial"]),
            "Invalid request indices")
    for key, expected in {"target_index": 2, "permutation_sign": 1,
                          "d": 8, "L": 22, "w": 41}.items():
        require(type(request[key]) is int and request[key] == expected,
                "Wrong selector parameter: " + key)
    require(type(request["rows"]) is list, "Invalid request rows")
    for row in request["rows"]:
        require(type(row) is dict and set(row) == {
            "slot", "source_exponents", "kernel_weight", "coefficient", "weighted_contribution"},
            "Invalid request row")
        require(type(row["slot"]) is list and type(row["source_exponents"]) is list and
                all(type(x) is int for x in row["slot"] + row["source_exponents"]),
                "Invalid request exponents")
        integer(row["kernel_weight"])
        rational(row["coefficient"])
        rational(row["weighted_contribution"])
    rows = selector_rows(values, kernels)
    require(request["rows"] == rows, "Recorded request/coefficients differ from exact replay")
    return rows


def polynomial(terms):
    answer = {}
    for key, coefficient in terms:
        exponents = tuple(int(x) for x in key.split(","))
        require(len(exponents) == 4 and min(exponents) >= 0, "Invalid polynomial exponent")
        require(type(coefficient) is int and coefficient != 0, "Invalid polynomial coefficient")
        require(exponents not in answer, "Duplicate polynomial term")
        answer[exponents] = Fraction(coefficient)
    return answer


def add(a, b):
    result = dict(a)
    for key, coefficient in b.items():
        result[key] = result.get(key, Fraction(0)) + coefficient
    return {key: coefficient for key, coefficient in result.items() if coefficient}


def verify_model_identities(model, prefactor):
    """Tiny exact identities in the supplied reduced MODEL (v0=1)."""
    one = {(0, 0, 0, 0): Fraction(1)}
    gamma, epsilon = model["gamma"], model["ev"]
    require(len(gamma) == 15 and all(len(row) == 5 for row in gamma), "Wrong gamma shape")
    require(len(epsilon) == 2 and all(len(row) == 10 for row in epsilon), "Wrong epsilon shape")
    require([polynomial(p) for p in gamma[10]] == [one, {}, {}, {}, {}],
            "Wrong gamma row 10")
    require([polynomial(row[5]) for row in epsilon] == [{}, one], "Wrong epsilon column 5")
    # Coefficients of the ten independent W[a,b] in L_minus(d_End W).
    for a in range(5):
        for b in range(2):
            left = polynomial(epsilon[b][5]) if a == 0 else {}
            right = polynomial(gamma[10][a]) if b == 1 else {}
            require(left == right, "Chain-map coefficient identity failed")

    charts = model["charts"]
    require(len(charts) == 6, "Wrong chart count")
    for index in (0, 5):
        chart = charts[index]
        require(chart["pivot"] == 0, "Wrong merged-anchor pivot")
        require(len(chart["I"]) == 15 and all(len(row) == 2 for row in chart["I"]),
                "Wrong inclusion dimensions")
        require(len(chart["P"]) == 2 and all(len(row) == 15 for row in chart["P"]),
                "Wrong projection dimensions")
        require(len(chart["H0"]) == 5 and all(len(row) == 15 for row in chart["H0"]),
                "Wrong H0 dimensions")
        require(all(polynomial(chart[d]) for d in ("di", "dp", "dh")),
                "Zero merged-anchor denominator")
        require([polynomial(p) for p in chart["I"][10]] == [{}, {}],
                "Nonzero merged-anchor inclusion row")
        for column in range(15):
            entry = {}
            for t in range(2):
                entry = add(entry, multiply(polynomial(chart["I"][10][t]),
                                            polynomial(chart["P"][t][column])))
            require(not entry, "Nonzero E=IP row 10")
        dh = polynomial(chart["dh"])
        require(all(polynomial(p) == (dh if r == 10 else {})
                    for r, p in enumerate(chart["H0"][0])), "Wrong H0 row 0")
        # Multiplying by the common dh checks each coefficient for arbitrary Z.
        for r in range(15):
            for s in range(10):
                coefficient = polynomial(chart["H0"][0][r]) if s == 5 else {}
                require(coefficient == (dh if (r, s) == (10, 5) else {}),
                        "Generic-Z row reduction failed")

    require(prefactor["P2Numerator"] == charts[2]["P"], "Prefactor P2/MODEL mismatch")
    require(prefactor["H1Column5Numerator"] == [row[5] for row in charts[1]["H1"]],
            "Prefactor H1 column 5/MODEL mismatch")
    require(prefactor["denominatorFactors"] == [charts[2]["dp"], charts[1]["dh"]],
            "Prefactor denominator/MODEL mismatch")
    return {"boundary_basis_checks": 10, "merged_anchor_checks": 2,
            "zero_E_row_entries": 30, "generic_Z_coefficient_checks": 300,
            "model_prefactor_ties": 3}


def verify_model(model, prefactor):
    canonical = hashlib.sha256(json.dumps(model, separators=(",", ":")).encode()).hexdigest()
    require(canonical == "b6b532c4bab5787397a4cddde34210c12fae71853b30cb73ecbe8a9c2b4826b2",
            "Canonical MODEL digest mismatch")
    require(prefactor["modelSha256"] == canonical, "Prefactor model pin mismatch")
    return verify_model_identities(model, prefactor)


def verify_prefactor(data):
    require(data["map"] == MAP, "Wrong prefactor map")
    require(data["identity"] == "b_minus=P2*H1_chart1[:,5]", "Wrong prefactor column")
    require(data["modelSha256"] ==
            "b6b532c4bab5787397a4cddde34210c12fae71853b30cb73ecbe8a9c2b4826b2",
            "Wrong canonical-model pin")

    matrix, column, targets = data["P2Numerator"], data["H1Column5Numerator"], data["numerators"]
    require(len(matrix) == len(targets) == 2 and len(column) == 15 and
            all(len(row) == 15 for row in matrix), "Invalid prefactor dimensions")
    for matrix_row, target in zip(matrix, targets):
        result = {}
        for a, b in zip(matrix_row, column):
            for key, coefficient in multiply(polynomial(a), polynomial(b)).items():
                result[key] = result.get(key, Fraction(0)) + coefficient
        result = {key: coefficient for key, coefficient in result.items() if coefficient}
        require(result == polynomial(target), "Prefactor polynomial contraction failed")
    require([len(p) for p in targets] == [4, 6], "Wrong prefactor support")
    denominator = data["denominatorFactors"]
    require(len(denominator) == 2 and all(polynomial(p) for p in denominator),
            "Invalid denominator factors")
    return 2


def replay(directory=HERE):
    directory = Path(directory)
    checked = verify_manifest(directory)
    values = parse_quotient(load(directory / "quotient.json"))
    kernels = kernel_polynomial()
    supplied = load(directory / "kernels.json")
    require(supplied["schema"] == "second-scalar-boundary-kernel-v1" and
            supplied["field"] == "Z" and supplied["shape"] == [9, 23],
            "Wrong supplied kernel metadata")
    generated = [[str(kernels.get((t, z), Fraction(0)).numerator)
                  for z in range(23)] for t in range(9)]
    require(supplied["rows"] == generated, "Supplied kernels differ from exact derivation")
    rows = verify_request(load(directory / "request.json"), values, kernels)
    total = sum((rational(row["weighted_contribution"]) for row in rows), Fraction(0))
    active = [p for p in itertools.permutations(range(4)) if M[p[0]] == 2]
    require(len(active) == 18 and tuple(ROLES) in active, "Wrong orientation count")
    expected = load(directory / "expected.json")
    require(all(expected[key] is False for key in (
        "complete_scalar_pairing_computed", "full_obstruction_computed", "source_attribution_reproduced")),
        "Overbroad completion claim")
    require(expected == {"schema": "second-scalar-first-edge-expected-v1",
            "scalar_map": MAP, "field": "Q", "roles": ROLES, "pairing_monomial": M,
            "signed_partial_edge_contribution": encode(total), "quotient_nonzeros": len(values),
            "selector_rows": len(rows),
            "nonzero_selected_coefficients": sum(rational(r["coefficient"]) != 0 for r in rows),
            "active_target_orientations": 18, "computed_target_orientations": 1,
            "remaining_target_orientations": 17, "complete_scalar_pairing_computed": False,
            "full_obstruction_computed": False, "source_attribution_reproduced": False},
            "Unexpected result or overbroad scope")
    require(total == Fraction(8655, 16), "Wrong first-edge result")
    require(expected["nonzero_selected_coefficients"] == 24, "Wrong nonzero selection count")
    prefactor = load(directory / "right-prefactor.json")
    require(digest(directory / "model.json") ==
            "635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926",
            "Reduced MODEL byte digest mismatch")
    model_checks = verify_model(load(directory / "model.json"), prefactor)
    prefactors = verify_prefactor(prefactor)
    return {"status": "PASS_SUPPLIED_QUOTIENT_REPLAY", "signed_partial_edge": encode(total),
            "quotient_terms": len(values), "selected_rows": len(rows), "nonzero_selections": 24,
            "independently_derived_kernel_coefficients": 207,
            "embedded_prefactor_contractions": prefactors, "manifest_files_verified": checked,
            "exact_reduced_model_checks": model_checks,
            "remaining_target_orientations": 17, "source_attribution_reproduced": False,
            "complete_scalar_pairing_computed": False, "full_obstruction_computed": False}


if __name__ == "__main__":
    print(json.dumps(replay(), indent=2))
