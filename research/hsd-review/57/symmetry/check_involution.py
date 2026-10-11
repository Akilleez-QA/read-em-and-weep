#!/usr/bin/env python3
"""Decide whether the +2 (mod 4) quotient copies are the carrier involution.

Public inputs used here are the role conventions and the supplied coefficient
arrays of the pinned #57 package. The symmetry itself is the one named in the
carrier atlas, the six-chart transitions, and the full-sign cochain:

- #2: Y maps through (P^1)^4 -> Sym^4 P^1 = P^4, degree 24 on that arrow.
  The Heisenberg/cyclic action on the HM monad is by +1 modulo 5, not +2
  modulo 4.
- #14: the N-gerbe class is a multiple of q1 cup q2 + q3 cup q4.
- #31: pi = V1^V2 + V3^V4, and the full-sign residual is the cross term of
  those two pairs.
- #34: the scalar functional sums active orientations and does not assume a
  permutation symmetry of the source.
- #36/#37: the numerator is one polynomial in the four x-coordinates; axis
  jets are extractions. Axis 3 is special only after the monomial
  m=(2,2,2,0) is applied.

The involution iota(i)=i+2 (mod 4) is the pair swap (0 2)(1 3). It preserves
pi and has sign +1, so it identifies reversed quotients and does not negate
them. It does not identify signed selector readings, because m is not
iota-invariant.
"""

from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
SPEC = importlib.util.spec_from_file_location("hsd57_recompute", PARENT / "recompute_aggregate.py")
review = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(review)

MONOMIAL = (2, 2, 2, 0)


def iota(index: int) -> int:
    return (index + 2) % 4


def shift_roles(roles: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(iota(index) for index in roles)


def key(roles: tuple[int, ...]) -> str:
    return "".join(str(index) for index in roles)


def active() -> list[tuple[int, int, int, int]]:
    return [roles for roles in itertools.permutations(range(4)) if MONOMIAL[roles[0]] == 2]


def selector(roles: tuple[int, int, int, int]) -> dict:
    _i, j, _k, l = roles
    return {
        "orientation": key(roles),
        "sign": review.permutation_sign(roles),
        "d": 6 + MONOMIAL[j],
        "L": 22 - MONOMIAL[l],
        "m_j": MONOMIAL[j],
        "m_l": MONOMIAL[l],
    }


def decide(document: dict, provenance: dict, contributions_sha256: str) -> tuple[dict, int]:
    roles = active()
    active_keys = {key(item) for item in roles}
    sign_iota = review.permutation_sign((2, 3, 0, 1))
    if sign_iota != 1:
        raise RuntimeError("iota = (0 2)(1 3) is not an even permutation")

    orbits = []
    seen = set()
    for item in roles:
        name = key(item)
        if name in seen:
            continue
        partner = key(shift_roles(item))
        seen.add(name)
        if partner in active_keys:
            seen.add(partner)
            orbits.append(sorted((name, partner)))
        else:
            orbits.append([name, partner])

    by_orientation = {key(tuple(edge["roles"])): edge for edge in document["edges"]}
    digest = {
        name: review.coefficient_digest(edge["integer_coefficients"])
        for name, edge in by_orientation.items()
    }
    report_audit = review.audit(document, provenance, contributions_sha256)
    signed = {
        item["orientation"]: review.Fraction(int(item["signed"][0]), int(item["signed"][1]))
        for item in report_audit["orientations"]
    }

    paired = []
    unpaired = []
    mismatches = []
    for orbit in orbits:
        left, right = orbit
        if left not in by_orientation:
            mismatches.append(f"missing orientation {left}")
            continue
        if right in active_keys and right not in by_orientation:
            mismatches.append(f"missing orientation {right}")
            continue
        if right in active_keys:
            same_list = by_orientation[left]["integer_coefficients"] == by_orientation[right]["integer_coefficients"]
            same_digest = digest[left] == digest[right]
            left_sign = review.permutation_sign(tuple(int(character) for character in left))
            right_sign = review.permutation_sign(tuple(int(character) for character in right))
            if not same_list or not same_digest or left_sign != right_sign:
                mismatches.append(f"{left}/{right} breaks the even involution identification")
            if left not in signed or right not in signed:
                mismatches.append(f"missing orientation {left if left not in signed else right}")
                continue
            total = signed[left] + signed[right]
            paired.append(
                {
                    "orientations": [left, right],
                    "signs": [left_sign, right_sign],
                    "selectors": [
                        selector(tuple(int(character) for character in left)),
                        selector(tuple(int(character) for character in right)),
                    ],
                    "signed": [signed[left].pair(), signed[right].pair()],
                    "pair_sum": total.pair(),
                    "pair_sum_is_zero": total == review.ZERO,
                    "quotients_identical": same_list,
                    "coefficient_sha256": digest[left],
                }
            )
        else:
            partner_roles = tuple(int(character) for character in right)
            if MONOMIAL[partner_roles[0]] == 2:
                mismatches.append(f"{right} was classified inactive but m starts at 2")
            if left not in signed:
                mismatches.append(f"missing orientation {left}")
                continue
            unpaired.append(
                {
                    "orientation": left,
                    "sign": review.permutation_sign(tuple(int(character) for character in left)),
                    "inactive_partner": right,
                    "partner_starts_at": partner_roles[0],
                    "signed": signed[left].pair(),
                    "coefficient_sha256": digest[left],
                }
            )

    distinct_lists = len(set(digest.values()))
    pair_total = review.ZERO
    for item in paired:
        pair_total += review.Fraction(int(item["pair_sum"][0]), int(item["pair_sum"][1]))
    single_total = review.ZERO
    for item in unpaired:
        single_total += review.Fraction(int(item["signed"][0]), int(item["signed"][1]))

    failures = list(mismatches)
    failures.extend(review.acceptance_failures(report_audit))
    code = review.exit_status(report_audit)
    if mismatches and code == 0:
        code = 1
    report = {
        "symmetry": "iota(i)=i+2 mod 4",
        "cycle_type": "(0 2)(1 3)",
        "preserves": "pi = V1 wedge V2 + V3 wedge V4",
        "not_the_heisenberg_cycle": "HM charts cycle coordinates modulo 5",
        "sign_iota": sign_iota,
        "quotient_relation": "Q(iota e)=Q(e), not -Q(e)",
        "signed_relation": "same permutation sign, different (d,L) because m=(2,2,2,0) sends axis 1 to axis 3",
        "paired_readings": paired,
        "unpaired_readings": unpaired,
        "paired_reading_count": 2 * len(paired),
        "distinct_lists": distinct_lists,
        "independent_quotients": distinct_lists,
        "active_singleton_count": len(unpaired),
        "distinct_singleton_lists": len({item["coefficient_sha256"] for item in unpaired}),
        "sum_of_pair_sums": pair_total.pair(),
        "sum_of_unpaired": single_total.pair(),
        "audit_orientation_count": report_audit["orientation_count"],
        "audit_sum": report_audit["sum"],
        "audit_sum_is_zero": report_audit["sum_is_zero"],
        "every_pair_sum_nonzero": all(not item["pair_sum_is_zero"] for item in paired) if paired else False,
        "mismatches": mismatches,
        "failures": failures,
        "classification": "expected symmetry" if code == 0 else "defect",
    }
    return report, code


def main() -> int:
    document = review.load_json(review.PACKAGE / "contributions.json")
    provenance = review.load_json(review.PACKAGE / "provenance.json")
    digest = review.sha256(review.PACKAGE / "contributions.json")
    report, code = decide(document, provenance, digest)
    json.dump(report, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return code


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        print(f"checker failed: {error}", file=sys.stderr)
        sys.exit(2)
