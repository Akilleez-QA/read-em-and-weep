#!/usr/bin/env python3
"""Independent exact check of one recorded edge on PR #43.

This file does not import or call the package under review. It reads the
supplied quotient as data and recomputes the displayed selector with its own
exact integer arithmetic.

Finite claim under test, and nothing else:
    the supplied quotient, under the displayed selector for roles (0,1,2,3)
    and m=(2,2,2,0), equals the rational 8655/16.

That number is a partial term. This program does not evaluate a scalar class.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path


PACKAGE = (
    Path(__file__).resolve().parents[2]
    / "hm"
    / "second-scalar-first-edge"
)
T_BOUND = 9
Z_BOUND = 23
QUOTIENT_SHAPE = (9, 44, 23)
STATED_SUM = (8655, 16)
STATED_DENOMINATOR = 64
STATED_SIGN = 1
ROLES = (0, 1, 2, 3)
MONOMIAL = (2, 2, 2, 0)


class Fraction:
    """Reduced rational with arbitrary-precision integer entries."""

    __slots__ = ("numerator", "denominator")

    def __init__(self, numerator: int, denominator: int = 1) -> None:
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Fraction entries must be int")
        if denominator == 0:
            raise ZeroDivisionError("zero denominator")
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        common = math.gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common

    def __add__(self, other: Fraction) -> Fraction:
        return Fraction(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def __neg__(self) -> Fraction:
        return Fraction(-self.numerator, self.denominator)

    def __sub__(self, other: Fraction) -> Fraction:
        return self + (-other)

    def __mul__(self, other: Fraction) -> Fraction:
        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return (
            self.numerator == other.numerator
            and self.denominator == other.denominator
        )

    def __bool__(self) -> bool:
        return self.numerator != 0

    def __repr__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    def pair(self) -> list[str]:
        return [str(self.numerator), str(self.denominator)]


ZERO = Fraction(0)
ONE = Fraction(1)
Poly = dict[tuple[int, int], Fraction]


def trim(poly: Poly) -> Poly:
    return {exponents: coefficient for exponents, coefficient in poly.items() if coefficient}


def multiply(left: Poly, right: Poly, t_bound: int = T_BOUND, z_bound: int = Z_BOUND) -> Poly:
    product: Poly = {}
    for (t1, z1), a in left.items():
        for (t2, z2), b in right.items():
            exponents = (t1 + t2, z1 + z2)
            if exponents[0] >= t_bound or exponents[1] >= z_bound:
                continue
            product[exponents] = product.get(exponents, ZERO) + a * b
    return trim(product)


def negate(poly: Poly) -> Poly:
    return {exponents: -coefficient for exponents, coefficient in poly.items()}


def add_constant(poly: Poly, constant: Fraction) -> Poly:
    updated = dict(poly)
    updated[(0, 0)] = updated.get((0, 0), ZERO) + constant
    return trim(updated)


def generator() -> Poly:
    """G(T,z) = 1 + z + (1 + 3z + z^2) T + z(1+z) T^2."""
    return {
        (0, 0): ONE,
        (0, 1): ONE,
        (1, 0): ONE,
        (1, 1): Fraction(3),
        (1, 2): ONE,
        (2, 1): ONE,
        (2, 2): ONE,
    }


def perturbation(g: Poly) -> Poly:
    h = dict(g)
    h[(0, 0)] = h.get((0, 0), ZERO) - ONE
    return trim(h)


def invert_by_newton(g: Poly, rounds: int = 8) -> Poly:
    """Reciprocal by Newton: y <- y * (2 - G y), exact once the error passes the nilpotent order."""
    reciprocal = {(0, 0): ONE}
    for _ in range(rounds):
        residual = multiply(g, reciprocal)
        correction = add_constant(negate(residual), Fraction(2))
        reciprocal = multiply(reciprocal, correction)
    identity = multiply(g, reciprocal)
    if identity != {(0, 0): ONE}:
        raise RuntimeError("Newton reciprocal failed the identity G * G^{-1} = 1")
    return reciprocal


def binomial_inverse_power(h: Poly, exponent: int = 70) -> Poly:
    """(1+H)^{-exponent} = sum binom(-exponent, n) H^n, truncated by nilpotence."""
    if exponent != 70:
        raise ValueError("this edge asks for the power -70")
    power = {(0, 0): ONE}
    total = {(0, 0): ONE}
    coefficient = ONE
    degree = 0
    while power:
        degree += 1
        if degree > 64:
            raise RuntimeError("nilpotence bound failed")
        power = multiply(power, h)
        if not power:
            break
        coefficient = coefficient * Fraction(-exponent - degree + 1, degree)
        for exponents, term in power.items():
            total[exponents] = total.get(exponents, ZERO) + coefficient * term
        total = trim(total)
    return total


def binary_power(poly: Poly, exponent: int) -> Poly:
    if exponent < 0:
        raise ValueError("negative power")
    result = {(0, 0): ONE}
    base = dict(poly)
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = multiply(result, base)
        remaining >>= 1
        if remaining:
            base = multiply(base, base)
    return result


def kernel_by_newton(g: Poly) -> Poly:
    reciprocal = invert_by_newton(g)
    powered = binary_power(reciprocal, 70)
    check = multiply(binary_power(g, 70), powered)
    if check != {(0, 0): ONE}:
        raise RuntimeError("Newton path failed G^{70} * G^{-70} = 1")
    return powered


def kernel_by_binomial(g: Poly) -> Poly:
    series = binomial_inverse_power(perturbation(g), 70)
    check = multiply(binary_power(g, 70), series)
    if check != {(0, 0): ONE}:
        raise RuntimeError("binomial path failed G^{70} * G^{-70} = 1")
    return series


def require_integral(kernel: Poly) -> None:
    for coefficient in kernel.values():
        if coefficient.denominator != 1:
            raise RuntimeError(f"non-integral kernel coefficient {coefficient}")


def load_json(path: Path) -> object:
    return json.loads(path.read_text())


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def permutation_sign(roles: tuple[int, ...]) -> int:
    inversions = 0
    for left in range(len(roles)):
        for right in range(left + 1, len(roles)):
            if roles[left] > roles[right]:
                inversions += 1
    return 1 if inversions % 2 == 0 else -1


def selector_parameters(roles: tuple[int, int, int, int], monomial: tuple[int, int, int, int]) -> dict:
    i, j, _k, l = roles
    if monomial[i] != 2:
        raise RuntimeError("displayed selector requires the first role to carry exponent 2")
    degree_sum = sum(monomial)
    return {
        "S": degree_sum,
        "d": 6 + monomial[j],
        "L": 22 - monomial[l],
        "w": 35 + degree_sum,
        "sign": permutation_sign(roles),
    }


def parse_quotient(document: dict) -> dict[tuple[int, int, int], Fraction]:
    if document.get("common_denominator") != str(STATED_DENOMINATOR):
        raise RuntimeError("stated common denominator is not 64")
    if document.get("shape") != list(QUOTIENT_SHAPE):
        raise RuntimeError("stated quotient window is not 9 x 44 x 23")
    rows = document["integer_coefficients"]
    if not isinstance(rows, list) or len(rows) != 203:
        raise RuntimeError("stated quotient does not have 203 terms")
    values: dict[tuple[int, int, int], Fraction] = {}
    slots = []
    for row in rows:
        if not isinstance(row, list) or len(row) != 4:
            raise RuntimeError("malformed quotient row")
        slot = (row[0], row[1], row[2])
        if not all(isinstance(part, int) and 0 <= part < bound for part, bound in zip(slot, QUOTIENT_SHAPE)):
            raise RuntimeError(f"quotient slot outside the stated window: {slot}")
        raw = row[3]
        if not isinstance(raw, str):
            raise RuntimeError("quotient numerator is not a decimal string")
        numerator = int(raw)
        if str(numerator) != raw or numerator == 0:
            raise RuntimeError("quotient numerator is zero or noncanonical")
        if slot in values:
            raise RuntimeError(f"duplicate quotient slot {slot}")
        slots.append(slot)
        values[slot] = Fraction(numerator, STATED_DENOMINATOR)
    if slots != sorted(slots):
        raise RuntimeError("quotient terms are not sorted")
    payload = json.dumps(rows, separators=(",", ":")).encode()
    digest = hashlib.sha256(payload).hexdigest()
    if digest != document.get("coefficient_array_sha256"):
        raise RuntimeError("coefficient-array pin does not match the term list")
    return values


def physical_exponents(roles: tuple[int, int, int, int], degree_sum: int, r: int, ell: int) -> list[int]:
    i, j, k, l = roles
    exponents = [0, 0, 0, 0]
    exponents[i] = 272
    exponents[j] = 215 - r
    exponents[k] = 157 - degree_sum + r - ell
    exponents[l] = 47 + ell
    return exponents


def evaluate_edge(values: dict[tuple[int, int, int], Fraction], kernel: Poly, roles, monomial) -> dict:
    parameters = selector_parameters(roles, monomial)
    d = parameters["d"]
    low = parameters["L"]
    homogeneous = parameters["w"]
    sign = parameters["sign"]
    rows = []
    total = ZERO
    for r in range(d + 1):
        for ell in range(low + 1):
            slot = (r, homogeneous, ell)
            coefficient = values.get(slot, ZERO)
            weight = kernel.get((d - r, low - ell), ZERO)
            if weight.denominator != 1:
                raise RuntimeError("selector weight is not an integer")
            contribution = Fraction(sign) * coefficient * weight
            exponents = physical_exponents(roles, parameters["S"], r, ell)
            if sum(exponents) != 691 - parameters["S"]:
                raise RuntimeError("physical exponents missed the stated degree")
            rows.append(
                {
                    "slot": list(slot),
                    "source_exponents": exponents,
                    "kernel_weight": str(weight.numerator),
                    "coefficient": coefficient.pair(),
                    "weighted_contribution": contribution.pair(),
                    "coefficient_sign": (coefficient.numerator > 0) - (coefficient.numerator < 0),
                    "weight_sign": (weight.numerator > 0) - (weight.numerator < 0),
                    "contribution_sign": (contribution.numerator > 0) - (contribution.numerator < 0),
                }
            )
            total += contribution
    nonzero = [row for row in rows if row["coefficient"] != ["0", "1"]]
    return {
        "parameters": parameters,
        "rows": rows,
        "nonzero": nonzero,
        "total": total,
    }


def recorded_kernel_rows(kernel: Poly) -> list[list[str]]:
    return [
        [str(kernel.get((t, z), ZERO).numerator) for z in range(Z_BOUND)]
        for t in range(T_BOUND)
    ]


def compare_request(recorded: dict, derived_rows: list[dict]) -> list[str]:
    mismatches = []
    rows = recorded.get("rows")
    if not isinstance(rows, list) or len(rows) != len(derived_rows):
        return [f"recorded row count {len(rows) if isinstance(rows, list) else None} != {len(derived_rows)}"]
    stated = {
        "roles": list(ROLES),
        "pairing_monomial": list(MONOMIAL),
        "target_index": 2,
        "permutation_sign": STATED_SIGN,
        "d": 8,
        "L": 22,
        "w": 41,
    }
    for key, expected in stated.items():
        if recorded.get(key) != expected:
            mismatches.append(f"recorded {key} = {recorded.get(key)!r}, displayed selector gives {expected!r}")
    for index, (recorded_row, derived) in enumerate(zip(rows, derived_rows)):
        for key in ("slot", "source_exponents", "kernel_weight", "coefficient", "weighted_contribution"):
            if recorded_row.get(key) != derived[key]:
                mismatches.append(
                    f"row {index} {key}: recorded {recorded_row.get(key)!r} != derived {derived[key]!r}"
                )
                if len(mismatches) > 12:
                    return mismatches
    return mismatches


def main() -> int:
    quotient_path = PACKAGE / "quotient.json"
    request_path = PACKAGE / "request.json"
    kernels_path = PACKAGE / "kernels.json"
    manifest_path = PACKAGE / "manifest.json"
    expected_path = PACKAGE / "expected.json"

    quotient_digest = sha256(quotient_path)
    manifest = load_json(manifest_path)
    expected = load_json(expected_path)
    g = generator()
    newton = kernel_by_newton(g)
    binomial = kernel_by_binomial(g)
    require_integral(newton)
    methods_agree = newton == binomial
    if not methods_agree:
        raise RuntimeError("Newton and binomial kernels disagree")

    values = parse_quotient(load_json(quotient_path))
    edge = evaluate_edge(values, newton, ROLES, MONOMIAL)
    total = edge["total"]
    request_mismatches = compare_request(load_json(request_path), edge["rows"])
    kernel_document = load_json(kernels_path)
    kernel_matches = kernel_document.get("rows") == recorded_kernel_rows(newton)

    manifest_pin = manifest["files"]["quotient.json"]["sha256"]
    defects = []
    if total.numerator != STATED_SUM[0] or total.denominator != STATED_SUM[1]:
        defects.append(f"weighted sum is {total}, stated pin is {STATED_SUM[0]}/{STATED_SUM[1]}")
    if edge["parameters"]["sign"] != STATED_SIGN:
        defects.append(f"orientation sign is {edge['parameters']['sign']}, stated pin is {STATED_SIGN}")
    if not kernel_matches:
        defects.append("derived integer kernel differs from kernels.json")
    if request_mismatches:
        defects.extend(request_mismatches)
    if quotient_digest != manifest_pin:
        defects.append("quotient.json bytes differ from the manifest pin")
    if expected.get("signed_partial_edge_contribution") != [str(STATED_SUM[0]), str(STATED_SUM[1])]:
        defects.append("expected.json does not pin 8655/16")
    if expected.get("complete_scalar_pairing_computed") is not False:
        defects.append("expected.json asserts a complete scalar pairing")
    if len(edge["nonzero"]) != 24:
        defects.append(f"nonzero selected coefficients: {len(edge['nonzero'])}, stated pin 24")

    denominators = sorted({row["coefficient"][1] for row in edge["nonzero"]})
    report = {
        "evidence_class": "supplied-quotient replay",
        "scalar_class_claimed": False,
        "partial_term": True,
        "orientation": list(ROLES),
        "pairing_monomial": list(MONOMIAL),
        "selector": edge["parameters"],
        "quotient_terms": len(values),
        "selector_rows": len(edge["rows"]),
        "nonzero_selected_coefficients": len(edge["nonzero"]),
        "sum": total.pair(),
        "sum_sign": (total.numerator > 0) - (total.numerator < 0),
        "sum_denominator": total.denominator,
        "nonzero_coefficient_denominators": denominators,
        "common_denominator": STATED_DENOMINATOR,
        "kernel_methods_agree": methods_agree,
        "kernel_matches_recorded_rows": kernel_matches,
        "request_rows_match": not request_mismatches,
        "quotient_sha256": quotient_digest,
        "manifest_quotient_sha256": manifest_pin,
        "coefficient_array_sha256": load_json(quotient_path)["coefficient_array_sha256"],
        "nonzero_terms": [
            {
                "slot": row["slot"],
                "coefficient": row["coefficient"],
                "kernel_weight_sign": row["weight_sign"],
                "contribution": row["weighted_contribution"],
                "contribution_sign": row["contribution_sign"],
            }
            for row in edge["nonzero"]
        ],
        "defects": defects,
        "reproduced": not defects,
    }
    json.dump(report, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0 if report["reproduced"] else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        print(f"checker failed: {error}", file=sys.stderr)
        sys.exit(2)
