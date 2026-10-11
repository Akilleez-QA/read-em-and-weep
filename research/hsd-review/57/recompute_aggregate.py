#!/usr/bin/env python3
"""Independent exact aggregate check of PR #57.

This file does not import or call the package under review. It reads the
supplied quotients as data and reapplies the displayed selector with its own
exact integer arithmetic.

Finite claim under test:
    for L_minus(X) = X02[0,5] - X13[10,1] and m = (2,2,2,0), the eighteen
    supplied quotients, each under its orientation sign and selector, sum to 0.

That sum is a supplied-quotient contraction. It is not a source regeneration
and it is not a full-obstruction value.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import sys
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[2] / "hm" / "second-scalar-m2220-complete"
PINNED_HEAD = "b1fdcdd666ed188250d6def3616733f1417fca81"
CONTRIBUTIONS_SHA256 = "72b08646afaf3a493243698583ee1f434a9dd78707d775d4fd0206593a5b87f0"
T_BOUND = 9
Z_BOUND = 23
QUOTIENT_SHAPE = (9, 44, 23)
COMMON_DENOMINATOR = 64
MONOMIAL = (2, 2, 2, 0)
LAURENT = (-3, -3, -3, -1)
DEGREE_SUM = sum(MONOMIAL)
HOMOGENEOUS = 35 + DEGREE_SUM
PHYSICAL_SUM = 691 - DEGREE_SUM

# Signed values and coefficient-array digests read from the pinned partial-edge
# packages, not from PR #57's table. Digests are SHA-256 of the compact JSON
# integer-coefficient lists.
PUBLISHED = {
    "0123": {"pr": 43, "sha": "b29c6aec939e4ee270da1bdadd8b3e2469b6e5cc", "signed": (8655, 16), "digest": "dfc8ee5bbabef051a9c18708f0b93b758ed34943ace9ee7ee448a0b33640da71"},
    "0132": {"pr": 46, "sha": "99c271053c98f50633a3d4dd7927fb8c8d9852a8", "signed": (-2817, 16), "digest": "40cf406681bbeedad3681da604300dd99ff9975b6a6fd3b403dcee5a3d92d9af"},
    "0213": {"pr": 46, "sha": "99c271053c98f50633a3d4dd7927fb8c8d9852a8", "signed": (18831, 8), "digest": "cae19babdc6803c0c161f93ff2ff61221c108e23ecdb1808df0c701d3bf5bf4f"},
    "0231": {"pr": 46, "sha": "99c271053c98f50633a3d4dd7927fb8c8d9852a8", "signed": (-21601, 8), "digest": "862a4435777b4e5ab98b8dd5000bcccab4d8b83dcd0203af14531fda9b47eaf6"},
    "0312": {"pr": 50, "sha": "abc79ba07db1a36883547528c59ba9609bb412fa", "signed": (1457, 8), "digest": "5691e1144b4eab9fbddcd249f4d8675faf50cac382864c0c1b9f4d116ae7fd05"},
    "0321": {"pr": 50, "sha": "abc79ba07db1a36883547528c59ba9609bb412fa", "signed": (-803, 4), "digest": "3277c1d8a6ca67a8b69f2d0a29007e47f6d7287679e75339fae0fa99fd3dd7cc"},
    "1023": {"pr": 50, "sha": "abc79ba07db1a36883547528c59ba9609bb412fa", "signed": (15705, 16), "digest": "535445abc2c6f8319f81e2c2d60eafc36757219871be9beea33667879659b128"},
    "1032": {"pr": 51, "sha": "cc094c174a2ae3d5bd2abc99b95e0a8366d599ae", "signed": (-5667, 16), "digest": "8bbae6e21f65135a0ae9df651f2bcdc2892a381bec51976a842fa7f177202703"},
    "1203": {"pr": 51, "sha": "cc094c174a2ae3d5bd2abc99b95e0a8366d599ae", "signed": (1953, 4), "digest": "69d5ef5351901ac5ff830b0a203c3accc3db315164a17f223224528875429a0b"},
    "1230": {"pr": 51, "sha": "cc094c174a2ae3d5bd2abc99b95e0a8366d599ae", "signed": (-4313, 4), "digest": "904eb24ef229bd7e24dbb73d78f250dc750dbd26ebf90a5f6f67e8c709d1a748"},
    "1302": {"pr": 55, "sha": "60daad77179e93b2eb4adf7c2c77cfe298053fc5", "signed": (407, 8), "digest": "0a8f9f403355b39b0e6b1b635015841d392408a58fe9105de7feae2f8fea5972"},
    "1320": {"pr": 55, "sha": "60daad77179e93b2eb4adf7c2c77cfe298053fc5", "signed": (-353, 4), "digest": "3cbb5220013f9dc68fead586da06baebc91647a4bcb69077ba60052b4370fc06"},
    "2013": {"pr": 55, "sha": "60daad77179e93b2eb4adf7c2c77cfe298053fc5", "signed": (-41517, 16), "digest": "862a4435777b4e5ab98b8dd5000bcccab4d8b83dcd0203af14531fda9b47eaf6"},
}


class Fraction:
    """Reduced rational whose entries are arbitrary-precision integers."""

    __slots__ = ("numerator", "denominator")

    def __init__(self, numerator: int, denominator: int = 1) -> None:
        if type(numerator) is not int or type(denominator) is not int:
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

    def __mul__(self, other: Fraction) -> Fraction:
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator == other.numerator and self.denominator == other.denominator

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


def multiply(left: Poly, right: Poly) -> Poly:
    product: Poly = {}
    for (t1, z1), left_coefficient in left.items():
        for (t2, z2), right_coefficient in right.items():
            exponents = (t1 + t2, z1 + z2)
            if exponents[0] >= T_BOUND or exponents[1] >= Z_BOUND:
                continue
            product[exponents] = product.get(exponents, ZERO) + left_coefficient * right_coefficient
    return trim(product)


def generator() -> Poly:
    """G(T,z) = 1 + z + T + 3Tz + Tz^2 + T^2 z + T^2 z^2."""
    return {
        (0, 0): ONE,
        (0, 1): ONE,
        (1, 0): ONE,
        (1, 1): Fraction(3),
        (1, 2): ONE,
        (2, 1): ONE,
        (2, 2): ONE,
    }


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


def kernel_by_newton(polynomial: Poly, rounds: int = 8) -> Poly:
    """G^{-70} = (G^{-1})^{70}, with the reciprocal from Newton iteration."""
    reciprocal = {(0, 0): ONE}
    for _ in range(rounds):
        residual = multiply(polynomial, reciprocal)
        correction = {(0, 0): Fraction(2)}
        for exponents, coefficient in residual.items():
            correction[exponents] = correction.get(exponents, ZERO) + (-coefficient)
        reciprocal = multiply(reciprocal, trim(correction))
    identity = multiply(polynomial, reciprocal)
    if identity != {(0, 0): ONE}:
        raise RuntimeError("Newton reciprocal failed G * G^{-1} = 1")
    powered = binary_power(reciprocal, 70)
    check = multiply(binary_power(polynomial, 70), powered)
    if check != {(0, 0): ONE}:
        raise RuntimeError("Newton path failed G^{70} * G^{-70} = 1")
    return powered


def kernel_by_binomial(polynomial: Poly) -> Poly:
    """(1+H)^{-70} by the generalized binomial series, truncated at nilpotence."""
    perturbation = dict(polynomial)
    perturbation[(0, 0)] = perturbation.get((0, 0), ZERO) + Fraction(-1)
    perturbation = trim(perturbation)
    power = {(0, 0): ONE}
    total = {(0, 0): ONE}
    coefficient = ONE
    degree = 0
    while power:
        degree += 1
        if degree > 64:
            raise RuntimeError("nilpotence bound failed")
        power = multiply(power, perturbation)
        if not power:
            break
        coefficient = coefficient * Fraction(-70 - degree + 1, degree)
        for exponents, term in power.items():
            total[exponents] = total.get(exponents, ZERO) + coefficient * term
        total = trim(total)
    check = multiply(binary_power(polynomial, 70), total)
    if check != {(0, 0): ONE}:
        raise RuntimeError("binomial path failed G^{70} * G^{-70} = 1")
    return total


def require_integral(kernel: Poly) -> None:
    for coefficient in kernel.values():
        if coefficient.denominator != 1:
            raise RuntimeError(f"non-integral kernel coefficient {coefficient}")


def canonical_integer(value: object) -> int:
    if type(value) is not str:
        raise ValueError("integer encoding is not a decimal string")
    parsed = int(value)
    if str(parsed) != value:
        raise ValueError("noncanonical integer")
    return parsed


def canonical_rational(value: object) -> Fraction:
    if type(value) is not list or len(value) != 2:
        raise ValueError("rational encoding is not a pair")
    numerator = canonical_integer(value[0])
    denominator = canonical_integer(value[1])
    if denominator <= 0:
        raise ValueError("nonpositive denominator")
    result = Fraction(numerator, denominator)
    if result.pair() != value:
        raise ValueError("unreduced rational")
    return result


def unique_object_pairs(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key {key}")
        result[key] = value
    return result


def load_json(path: Path) -> object:
    return json.loads(path.read_text(), object_pairs_hook=unique_object_pairs)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def coefficient_digest(terms: list) -> str:
    payload = json.dumps(terms, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def orientation_key(roles: tuple[int, ...]) -> str:
    return "".join(str(index) for index in roles)


def active_orientations() -> list[tuple[int, int, int, int]]:
    """Permutations whose first role carries monomial weight 2, in lex order."""
    return [
        roles
        for roles in itertools.permutations(range(4))
        if MONOMIAL[roles[0]] == 2
    ]


def permutation_sign(roles: tuple[int, ...]) -> int:
    inversions = 0
    for left in range(len(roles)):
        for right in range(left + 1, len(roles)):
            if roles[left] > roles[right]:
                inversions += 1
    return 1 if inversions % 2 == 0 else -1


def parse_quotient(terms: object) -> dict[tuple[int, int, int], Fraction]:
    if type(terms) is not list or not terms:
        raise ValueError("quotient term list is empty")
    values: dict[tuple[int, int, int], Fraction] = {}
    slots = []
    for row in terms:
        if type(row) is not list or len(row) != 4:
            raise ValueError("malformed quotient row")
        slot = (row[0], row[1], row[2])
        if not all(type(part) is int and 0 <= part < bound for part, bound in zip(slot, QUOTIENT_SHAPE)):
            raise ValueError(f"quotient slot outside the window: {slot}")
        numerator = canonical_integer(row[3])
        if numerator == 0:
            raise ValueError("sparse quotient contains a zero")
        if slot in values:
            raise ValueError(f"duplicate quotient slot {slot}")
        slots.append(slot)
        values[slot] = Fraction(numerator, COMMON_DENOMINATOR)
    if slots != sorted(slots):
        raise ValueError("quotient terms are not sorted")
    return values


def physical_exponents(roles: tuple[int, int, int, int], r: int, ell: int) -> list[int]:
    i, j, k, l = roles
    exponents = [0, 0, 0, 0]
    exponents[i] = 272
    exponents[j] = 215 - r
    exponents[k] = 157 - DEGREE_SUM + r - ell
    exponents[l] = 47 + ell
    return exponents


def contract(values: dict[tuple[int, int, int], Fraction], kernel: Poly, roles: tuple[int, int, int, int]) -> dict:
    i, j, k, l = roles
    del i, k
    degree = 6 + MONOMIAL[j]
    low = 22 - MONOMIAL[l]
    sign = permutation_sign(roles)
    rows = []
    unsigned = ZERO
    for r in range(degree + 1):
        for ell in range(low + 1):
            slot = (r, HOMOGENEOUS, ell)
            coefficient = values.get(slot, ZERO)
            weight = kernel.get((degree - r, low - ell), ZERO)
            if weight.denominator != 1:
                raise RuntimeError("selector weight is not an integer")
            contribution = coefficient * weight
            exponents = physical_exponents(roles, r, ell)
            if sum(exponents) != PHYSICAL_SUM:
                raise RuntimeError("physical exponents missed degree 685")
            rows.append(
                {
                    "slot": list(slot),
                    "source_exponents": exponents,
                    "kernel_weight": str(weight.numerator),
                    "coefficient": coefficient.pair(),
                    "weighted_contribution": contribution.pair(),
                }
            )
            unsigned += contribution
    signed = Fraction(sign) * unsigned
    nonzero = sum(row["coefficient"] != ["0", "1"] for row in rows)
    return {
        "roles": list(roles),
        "orientation": orientation_key(roles),
        "sign": sign,
        "d": degree,
        "L": low,
        "w": HOMOGENEOUS,
        "rows": rows,
        "selector_rows": len(rows),
        "nonzero_selected": nonzero,
        "unsigned": unsigned,
        "signed": signed,
    }


def shift_orientation(orientation: str) -> str:
    """Add 2 (mod 4) to every role index."""
    return "".join(str((int(character) + 2) % 4) for character in orientation)


def duplicate_groups(digests: dict[str, str]) -> list[list[str]]:
    grouped: dict[str, list[str]] = {}
    for orientation, digest in digests.items():
        grouped.setdefault(digest, []).append(orientation)
    return [sorted(group) for group in grouped.values() if len(group) > 1]


def audit(document: dict, provenance: dict, contributions_sha256: str) -> dict:
    arithmetic_defects: list[str] = []
    if document.get("schema") != "second-scalar-m2220-complete-v1":
        arithmetic_defects.append("unexpected contributions schema")
    if document.get("scalar_map") != "X02[0,5]-X13[10,1]":
        arithmetic_defects.append("unexpected scalar map")
    if document.get("pairing_monomial") != list(MONOMIAL):
        arithmetic_defects.append("unexpected pairing monomial")
    if document.get("laurent_exponents") != list(LAURENT):
        arithmetic_defects.append("unexpected Laurent exponents")
    for flag in ("whole_scalar_map_computed", "full_obstruction_computed", "source_attribution_reproduced"):
        if document.get(flag) is not False:
            arithmetic_defects.append(f"{flag} is not false")
    if provenance.get("new_map_source_regeneration_distributed") is not False:
        arithmetic_defects.append("package claims distributed new-map source regeneration")
    if provenance.get("terminal_checkpoints_distributed") is not False:
        arithmetic_defects.append("package claims distributed terminal checkpoints")
    if provenance.get("historical_source_nodes_reevaluated_by_comparison") != 0:
        arithmetic_defects.append("provenance does not record zero source-node reevaluations")
    if contributions_sha256 != CONTRIBUTIONS_SHA256:
        arithmetic_defects.append("contributions.json SHA-256 differs from the pinned head")

    polynomial = generator()
    newton = kernel_by_newton(polynomial)
    binomial = kernel_by_binomial(polynomial)
    require_integral(newton)
    if newton != binomial:
        raise RuntimeError("Newton and binomial kernels disagree")

    expected_roles = active_orientations()
    edges = document.get("edges")
    if type(edges) is not list:
        raise ValueError("edges are not a list")
    found_roles = []
    for edge in edges:
        roles = edge.get("roles")
        if type(roles) is not list or len(roles) != 4 or any(type(part) is not int for part in roles):
            raise ValueError("malformed roles")
        found_roles.append(tuple(roles))
    if found_roles != expected_roles:
        arithmetic_defects.append(
            f"orientation list {[''.join(map(str, roles)) for roles in found_roles]} "
            f"!= active lex list {[''.join(map(str, roles)) for roles in expected_roles]}"
        )

    derived_edges = []
    digests: dict[str, str] = {}
    total = ZERO
    all_rows = []
    for edge, roles in zip(edges, found_roles):
        if edge.get("shape") != list(QUOTIENT_SHAPE):
            arithmetic_defects.append(f"{orientation_key(roles)} shape is not (9,44,23)")
        if canonical_integer(edge.get("common_denominator")) != COMMON_DENOMINATOR:
            arithmetic_defects.append(f"{orientation_key(roles)} common denominator is not 64")
        if edge.get("homogeneous_degrees_separated") is not True or edge.get("pairing_aggregated") is not False:
            arithmetic_defects.append(f"{orientation_key(roles)} grading flags are wrong")
        terms = edge["integer_coefficients"]
        digest = coefficient_digest(terms)
        if digest != edge.get("coefficient_array_sha256"):
            arithmetic_defects.append(f"{orientation_key(roles)} coefficient digest does not match its list")
        values = parse_quotient(terms)
        derived = contract(values, newton, roles)
        digests[derived["orientation"]] = digest
        if edge.get("permutation_sign") != derived["sign"]:
            arithmetic_defects.append(
                f"{derived['orientation']} recorded sign {edge.get('permutation_sign')} != {derived['sign']}"
            )
        recorded_signed = canonical_rational(edge.get("signed_contribution"))
        if recorded_signed != derived["signed"]:
            arithmetic_defects.append(
                f"{derived['orientation']} recorded {recorded_signed} != recomputed {derived['signed']}"
            )
        if edge.get("rows") != derived["rows"]:
            arithmetic_defects.append(f"{derived['orientation']} selector rows differ from the derived selector")
        provenance_row = edge.get("source_provenance") or {}
        if provenance_row.get("source_nodes_reevaluated_by_original_completion_audit") != 0:
            arithmetic_defects.append(f"{derived['orientation']} records a nonzero source-node reevaluation")
        derived_edges.append(
            {
                "orientation": derived["orientation"],
                "sign": derived["sign"],
                "d": derived["d"],
                "L": derived["L"],
                "w": derived["w"],
                "quotient_terms": len(values),
                "selector_rows": derived["selector_rows"],
                "nonzero_selected": derived["nonzero_selected"],
                "unsigned": derived["unsigned"].pair(),
                "signed": derived["signed"].pair(),
                "coefficient_sha256": digest,
                "previously_published": derived["orientation"] in PUBLISHED,
            }
        )
        total += derived["signed"]
        all_rows.extend(derived["rows"])

    published_agreement = []
    for orientation, pin in PUBLISHED.items():
        match = next((item for item in derived_edges if item["orientation"] == orientation), None)
        agrees = (
            match is not None
            and tuple(int(part) for part in match["signed"]) == pin["signed"]
            and match["coefficient_sha256"] == pin["digest"]
        )
        if not agrees:
            arithmetic_defects.append(f"{orientation} disagrees with published PR #{pin['pr']}")
        published_agreement.append(
            {
                "orientation": orientation,
                "pr": pin["pr"],
                "pinned_sha": pin["sha"],
                "published_signed": [str(pin["signed"][0]), str(pin["signed"][1])],
                "recomputed_signed": None if match is None else match["signed"],
                "coefficient_arrays_agree": match is not None and match["coefficient_sha256"] == pin["digest"],
                "agrees": agrees,
            }
        )

    copies = []
    for group in duplicate_groups(digests):
        digest = digests[group[0]]
        raw = {
            orientation_key(tuple(edge["roles"])): edge["integer_coefficients"]
            for edge in edges
            if orientation_key(tuple(edge["roles"])) in group
        }
        lists_equal = len({json.dumps(raw[name], separators=(",", ":")) for name in group}) == 1
        relation = "add 2 mod 4" if all(shift_orientation(name) in group for name in group) else "unstructured"
        copies.append(
            {
                "orientations": group,
                "coefficient_sha256": digest,
                "lists_identical": lists_equal,
                "relation": relation,
                "original_quotient_sha256": {
                    name: next(
                        edge["source_provenance"]["original_quotient_sha256"]
                        for edge in edges
                        if orientation_key(tuple(edge["roles"])) == name
                    )
                    for name in group
                },
            }
        )

    distinct_exponents = len({tuple(row["source_exponents"]) for row in all_rows})
    nonzero_rows = sum(row["coefficient"] != ["0", "1"] for row in all_rows)
    data_defects = []
    if copies:
        rendered = ", ".join("=".join(group["orientations"]) for group in copies)
        data_defects.append(
            "supplied coefficient arrays are not distinct across orientations: " + rendered
        )
    fresh = [item for item in derived_edges if not item["previously_published"]]
    report = {
        "evidence_class": "supplied-quotient replay",
        "source_regeneration": False,
        "pinned_head": PINNED_HEAD,
        "contributions_sha256": contributions_sha256,
        "kernel_methods_agree": True,
        "kernel_identity": "G^70 * G^{-70} = 1 modulo (T^9, z^23)",
        "orientations": derived_edges,
        "orientation_count": len(derived_edges),
        "signs": {item["orientation"]: item["sign"] for item in derived_edges},
        "sum": total.pair(),
        "sum_is_zero": total == ZERO,
        "published_agreement": published_agreement,
        "fresh_recomputations": fresh,
        "duplicate_quotient_groups": copies,
        "quotient_terms_in_file": sum(item["quotient_terms"] for item in derived_edges),
        "distinct_coefficient_arrays": len(set(digests.values())),
        "selector_rows": len(all_rows),
        "distinct_source_exponents": distinct_exponents,
        "nonzero_selected_coefficients": nonzero_rows,
        "arithmetic_defects": arithmetic_defects,
        "data_defects": data_defects,
        "scope_flags": {
            "whole_scalar_map_computed": document.get("whole_scalar_map_computed"),
            "full_obstruction_computed": document.get("full_obstruction_computed"),
            "source_attribution_reproduced": document.get("source_attribution_reproduced"),
            "new_map_source_regeneration_distributed": provenance.get("new_map_source_regeneration_distributed"),
            "terminal_checkpoints_distributed": provenance.get("terminal_checkpoints_distributed"),
            "historical_source_nodes_reevaluated_by_comparison": provenance.get(
                "historical_source_nodes_reevaluated_by_comparison"
            ),
        },
    }
    return report


def main() -> int:
    contributions_path = PACKAGE / "contributions.json"
    provenance_path = PACKAGE / "provenance.json"
    digest = sha256(contributions_path)
    report = audit(load_json(contributions_path), load_json(provenance_path), digest)
    json.dump(report, sys.stdout, indent=2)
    sys.stdout.write("\n")
    if report["arithmetic_defects"]:
        return 2
    if report["data_defects"] or not report["sum_is_zero"]:
        return 1
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        print(f"checker failed: {error}", file=sys.stderr)
        sys.exit(2)
