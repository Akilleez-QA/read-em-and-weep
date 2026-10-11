"""Compare the frozen selector with the pinned package outputs.

The selector module was committed before this comparison. This file does not
import the package replay. Row digests use the canonical JSON row
`[[r, w, ell], physical, weight, coefficient, weighted]`.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

from selector import (
    all_orientations,
    apply_sigma_tuple,
    certified_kernel_weights,
    documented_duplicate_pairs,
    equal_array_pairs,
    iter_boundary,
    load_quotients,
    monomials,
    permute_roles,
)


BINDING_CROSSWALK = {
    "configuration_sha256": "configurationSHA256",
    "normalized_source_sha256": "normalizedSourceSHA256",
    "compact_source_sha256": "compactSourceSHA256",
    "checkpoint_sha256": "checkpointSHA256",
    "original_quotient_sha256": "quotientSHA256",
    "completion_receipt_sha256": "independentCompletionReceiptSHA256",
}


def enc(value):
    return [str(value.numerator), str(value.denominator)]


def digest(value):
    payload = json.dumps(value, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def canonical_rows(target, quotient, weights):
    rows = []
    for *_, row in iter_boundary(target, quotient, weights):
        rows.append([
            [row.r, row.w, row.ell],
            list(row.physical),
            str(row.weight),
            enc(row.coefficient),
            enc(row.weighted),
        ])
    return rows


def _fraction(pair):
    return Fraction(int(pair[0]), int(pair[1]))


def compare(package_dir):
    package_dir = Path(package_dir)
    quotients = load_quotients(package_dir)
    weights = certified_kernel_weights()
    expected = json.loads((package_dir / "expected.json").read_text())
    binding = json.loads((package_dir / "duplicate-binding.json").read_text())
    mismatches = []

    if expected.get("schema") != "Lminus-all81-expected-v1":
        mismatches.append(("schema", expected.get("schema")))
    if expected.get("source_regeneration_reproduced") is not False:
        mismatches.append(("source-regeneration-flag", True))
    if expected.get("full_obstruction_computed") is not False:
        mismatches.append(("full-obstruction-flag", True))
    if len(expected.get("targets", [])) != 81:
        mismatches.append(("target-count", len(expected.get("targets", []))))

    stats = {
        "quotients": 24,
        "targets": 81,
        "computed_targets": 0,
        "empty_boundary_targets": 0,
        "requests": 0,
        "rows": 0,
        "distinct_exponents": set(),
        "nonzero_rows": 0,
        "distinct_nonzero_coefficients": set(),
        "nonzero_signed_selections": 0,
    }
    for index, target in monomials():
        record = expected["targets"][index]
        active = [roles for roles in all_orientations() if target[roles[0]] == 2]
        empty = not active
        if record.get("index") != index:
            mismatches.append(("index", index, record.get("index")))
        if record.get("m") != list(target):
            mismatches.append(("m", index, record.get("m"), list(target)))
        laurent = [-entry - 1 for entry in target]
        if record.get("laurent") != laurent:
            mismatches.append(("laurent", index, record.get("laurent"), laurent))
        if record.get("empty_boundary") is not empty:
            mismatches.append(("empty", index, record.get("empty_boundary"), empty))
        total = Fraction(0)
        edges = record.get("edges", [])
        if len(edges) != len(active):
            mismatches.append(("edge-count", index, len(edges), len(active)))
        for roles, edge in zip(active, edges):
            rows = canonical_rows(target, quotients[roles], weights)
            signed = sum(
                (row.signed for *_, row in iter_boundary(target, quotients[roles], weights)),
                Fraction(0),
            )
            total += signed
            nonzero = sum(row[3] != ["0", "1"] for row in rows)
            actual = {
                "roles": list(roles),
                "sign": quotients[roles].sign,
                "signed": enc(signed),
                "rows": len(rows),
                "nonzero_rows": nonzero,
                "rows_sha256": digest(rows),
            }
            for key, value in actual.items():
                if edge.get(key) != value:
                    mismatches.append((key, index, roles, edge.get(key), value))
            stats["requests"] += 1
            stats["rows"] += len(rows)
            stats["nonzero_rows"] += nonzero
            if signed != 0:
                stats["nonzero_signed_selections"] += 1
            for row in rows:
                exponent = tuple(row[1])
                stats["distinct_exponents"].add(exponent)
                if row[3] != ["0", "1"]:
                    stats["distinct_nonzero_coefficients"].add(exponent)
        if enc(total) != record.get("value"):
            mismatches.append(("value", index, record.get("value"), enc(total)))
        if empty:
            stats["empty_boundary_targets"] += 1
        else:
            stats["computed_targets"] += 1

    flat_stats = {
        "quotients": stats["quotients"],
        "targets": stats["targets"],
        "computed_targets": stats["computed_targets"],
        "empty_boundary_targets": stats["empty_boundary_targets"],
        "requests": stats["requests"],
        "rows": stats["rows"],
        "distinct_exponents": len(stats["distinct_exponents"]),
        "nonzero_rows": stats["nonzero_rows"],
        "distinct_nonzero_coefficients": len(stats["distinct_nonzero_coefficients"]),
        "nonzero_signed_selections": stats["nonzero_signed_selections"],
    }
    if expected.get("statistics") != flat_stats:
        mismatches.append(("statistics", expected.get("statistics"), flat_stats))

    pairs = equal_array_pairs(quotients)
    named = {("".join(map(str, left)), "".join(map(str, right))) for left, right in documented_duplicate_pairs()}
    recorded = {tuple(pair["roles"]) for pair in binding["duplicatePairs"]}
    if recorded != named:
        mismatches.append(("duplicate-pair-set", sorted(recorded), sorted(named)))
    if binding.get("sourceSymmetryProved") is not False:
        mismatches.append(("source-symmetry-flag", binding.get("sourceSymmetryProved")))
    if binding.get("actualSourceNodesReevaluated") != 0:
        mismatches.append(("reevaluated-nodes", binding.get("actualSourceNodesReevaluated")))
    mapped_rows = 0
    fixed = (2, 2, 2, 0)
    image = apply_sigma_tuple(fixed)
    for pair in binding["duplicatePairs"]:
        left_roles = tuple(int(character) for character in pair["roles"][0])
        right_roles = tuple(int(character) for character in pair["roles"][1])
        if permute_roles(left_roles) != right_roles:
            mismatches.append(("sigma", left_roles, right_roles))
        left_rows = canonical_rows(fixed, quotients[left_roles], weights)
        right_rows = canonical_rows(image, quotients[right_roles], weights)
        mapped_rows += len(left_rows)
        if len(left_rows) != pair["mappedRowCount"] or len(left_rows) != len(right_rows):
            mismatches.append(("mapped-count", pair["roles"], len(left_rows), pair["mappedRowCount"]))
        for left_row, right_row in zip(left_rows, right_rows):
            pushed = [0, 0, 0, 0]
            for axis, value in enumerate(left_row[1]):
                pushed[(2, 3, 0, 1)[axis]] = value
            if right_row != [left_row[0], pushed, *left_row[2:]]:
                mismatches.append(("covariance-row", pair["roles"], left_row[0]))
                break
        left_signed = enc(sum(
            (row.signed for *_, row in iter_boundary(fixed, quotients[left_roles], weights)),
            Fraction(0),
        ))
        image_signed = enc(sum(
            (row.signed for *_, row in iter_boundary(image, quotients[right_roles], weights)),
            Fraction(0),
        ))
        fixed_signed = enc(sum(
            (row.signed for *_, row in iter_boundary(fixed, quotients[right_roles], weights)),
            Fraction(0),
        ))
        if left_signed != pair["originalSignedValue"] or image_signed != pair["permutedTargetSignedValue"]:
            mismatches.append(("binding-value", pair["roles"], left_signed, image_signed))
        if fixed_signed != pair["sameFixedM2220TargetOnSecondRole"]:
            mismatches.append(("fixed-target", pair["roles"], fixed_signed))
        if fixed_signed == left_signed:
            mismatches.append(("same-target-collapsed", pair["roles"]))
        historical = binding["roles"]
        for label, roles in ((pair["roles"][0], left_roles), (pair["roles"][1], right_roles)):
            receipt = historical[label]
            quotient = quotients[roles]
            pins = dict(quotient.bindings)
            pins["array_sha256"] = quotient.array_sha256
            for public, original in {**BINDING_CROSSWALK, "array_sha256": "coefficientArraySHA256"}.items():
                if pins[public] != receipt[original]:
                    mismatches.append(("binding-pin", label, public))
        for field in (
            "configuration_sha256",
            "normalized_source_sha256",
            "compact_source_sha256",
            "checkpoint_sha256",
        ):
            if quotients[left_roles].bindings[field] == quotients[right_roles].bindings[field]:
                mismatches.append(("shared-binding", pair["roles"], field))
    if mapped_rows != binding.get("exactMappedSelectorRowsCompared") or mapped_rows != 1086:
        mismatches.append(("mapped-total", mapped_rows, binding.get("exactMappedSelectorRowsCompared")))
    if len(pairs) != 12:
        mismatches.append(("equal-array-pairs", len(pairs)))

    return {
        "mismatches": mismatches,
        "statistics": flat_stats,
        "equal_array_pairs": len(pairs),
        "documented_mapped_rows": mapped_rows,
    }


def main():
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument("package_dir")
    args = parser.parse_args()
    result = compare(args.package_dir)
    print(json.dumps({
        "mismatches": len(result["mismatches"]),
        "statistics": result["statistics"],
        "equal_array_pairs": result["equal_array_pairs"],
        "documented_mapped_rows": result["documented_mapped_rows"],
    }, indent=2))
    if result["mismatches"]:
        for item in result["mismatches"][:20]:
            print(item, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
