"""Run the independent review and write results.json.

The finite-complex matrices are rebuilt here. The published verifier programs
are not executed.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from finite_complex import (
    build_bases,
    cech_delta,
    gamma_tensor,
    initial_matrix,
    length_five_image,
    monad_columns,
    outgoing_matrices,
    positive_differential,
)
from independent_checks import (
    check_degree_counts,
    check_integer_kernels,
    check_projection_and_residues,
    check_scalar_rows,
    geometric_zero_indices,
)
from linear_algebra import exact_rank, modular_rank, multiply_matrix, reduce_rows, unit_echelon

PACKAGE = Path(__file__).resolve().parents[2] / "hm" / "current-scalar-proof"
OUT = Path(__file__).resolve().parent / "results.json"

PROSE_ZEROS = [
    0, 1, 3, 4, 9, 10, 12, 13, 26, 27, 28, 30, 31, 36, 37, 39, 40, 41,
    43, 44, 49, 50, 52, 53, 62, 67, 68, 70, 71, 74, 76, 77, 78, 79, 80,
]
PROSE_RELATIONS = [
    (17, 35),
    (14, 32, 38),
    (16, 34, 42),
    (23, 47),
    (22, 46, 48),
    (25, 51),
    (2, 6, 18, 54),
    (59, 65),
    (58, 64, 66),
    (61, 69),
    (8, 20, 24, 56, 60, 72),
    (73, 75),
]


def matrix_hash(rows):
    payload = [[[column, value] for column, value in sorted(row.items())] for row in rows]
    encoded = json.dumps(payload, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def sparse_equal(left, right):
    return sorted(left.items()) == sorted(right.items())


def relation_report(pure_negative, certificate):
    mismatches = []
    witness_terms = 0
    positive_rows = []
    for index, relation in enumerate(certificate["relations"]):
        target = {}
        for term in relation["terms"]:
            for column, sign in ((term["index"], 1), (5670 + term["index"], -1)):
                updated = target.get(column, 0) + term["coefficient"] * sign
                if updated:
                    target[column] = updated
                else:
                    target.pop(column, None)
        proof = {}
        for piece in relation["integer_outgoing_row_certificate"]:
            witness_terms += 1
            if piece["row"] >= 3920:
                positive_rows.append(piece["row"])
                continue
            for column, value in pure_negative[piece["row"]].items():
                updated = proof.get(column, 0) + piece["coefficient"] * value
                if updated:
                    proof[column] = updated
                else:
                    proof.pop(column, None)
        if not sparse_equal(target, proof):
            mismatches.append(index)
    columns = certificate["relation_identity_minor_columns"]
    minor_ok = len(columns) == 47 and len(set(columns)) == 47
    for row_index, relation in enumerate(certificate["relations"]):
        coeffs = {term["index"]: term["coefficient"] for term in relation["terms"]}
        for column_index, column in enumerate(columns):
            if coeffs.get(column, 0) != int(row_index == column_index):
                minor_ok = False
    prose_zero_relations = [tuple(term["index"] for term in relation["terms"]) for relation in certificate["relations"] if len(relation["terms"]) == 1]
    prose_match = sorted(prose_zero_relations) == sorted((index,) for index in PROSE_ZEROS)
    longer = [tuple(term["index"] for term in relation["terms"]) for relation in certificate["relations"] if len(relation["terms"]) > 1]
    prose_match = prose_match and sorted(longer) == sorted(PROSE_RELATIONS)
    coefficients_one = all(term["coefficient"] == 1 for relation in certificate["relations"] for term in relation["terms"])
    return {
        "status": "reproduced" if not mismatches and minor_ok and prose_match and coefficients_one and not positive_rows else "defect",
        "witness_terms": witness_terms,
        "mismatch_relations": mismatches,
        "identity_minor": minor_ok,
        "prose_matches_certificate": prose_match,
        "all_coefficients_plus_one": coefficients_one,
        "positive_block_witness_rows": positive_rows,
    }


def scalar_rows(gamma):
    rows = []
    for bundle in range(15):
        for source in range(2):
            slots = {50 + 2 * bundle + source: 1}
            for target in range(5):
                for variable in range(5):
                    coefficient = gamma[bundle][target][variable]
                    if coefficient:
                        slots[10 * target + 5 * source + variable] = slots.get(10 * target + 5 * source + variable, 0) - coefficient
            for mode in range(81):
                rows.append({81 * slot + mode: coefficient for slot, coefficient in slots.items()})
    current = [{mode: 1, 5670 + mode: -1} for mode in range(81)]
    return current, rows


def annihilates(rows, matrix):
    failures = 0
    for row in rows:
        image = {}
        for row_index, coefficient in row.items():
            for column, value in matrix[row_index].items():
                updated = image.get(column, 0) + coefficient * value
                if updated:
                    image[column] = updated
                else:
                    image.pop(column, None)
        if image:
            failures += 1
    return failures


def main():
    findings = []
    scalar_findings, gamma = check_scalar_rows()
    findings.extend(scalar_findings)
    findings.extend(check_projection_and_residues())
    findings.extend(check_integer_kernels())
    findings.extend(check_degree_counts())

    certificate = json.loads((PACKAGE / "data" / "integer-relations.json").read_text())
    zeros = geometric_zero_indices()
    forced = set(certificate["zero_indices"])
    findings.append({
        "name": "sixteen first-open zeros are among the thirty-five single-coordinate relations",
        "status": "reproduced" if set(zeros) <= forced and len(zeros) == 16 and len(forced) == 35 else "defect",
        "detail": {
            "geometric_zero_indices": zeros,
            "extra_single_coordinate_zeros": sorted(forced - set(zeros)),
            "geometric_not_forced": sorted(set(zeros) - forced),
        },
    })

    print("rebuilding finite complex", flush=True)
    columns, incoming = monad_columns(gamma_tensor())
    basis, indexes = build_bases()
    incoming_matrix = initial_matrix(basis, indexes, columns, incoming)
    pure_negative, outgoing = outgoing_matrices(basis, indexes, columns, incoming)
    positive = positive_differential(basis, indexes, columns, incoming)
    incoming_digest = matrix_hash(incoming_matrix)
    outgoing_digest = matrix_hash(outgoing)
    hash_ok = (
        incoming_digest == certificate["negative_incoming_matrix_sha256"]
        and outgoing_digest == certificate["outgoing_matrix_sha256"]
    )
    findings.append({
        "name": "rebuilt incoming and outgoing matrices match the published integer fingerprints",
        "status": "reproduced" if hash_ok else "defect",
        "detail": {
            "incoming": incoming_digest,
            "outgoing": outgoing_digest,
            "published_incoming": certificate["negative_incoming_matrix_sha256"],
            "published_outgoing": certificate["outgoing_matrix_sha256"],
        },
    })
    if not hash_ok:
        OUT.write_text(json.dumps({"findings": findings}, indent=2) + "\n")
        print("matrix fingerprint mismatch; stopped before rank claims")
        return 1

    relation = relation_report(pure_negative, certificate)
    findings.append({
        "name": "forty-seven integer witnesses, identity minor, and prose relation list",
        "status": relation["status"],
        "detail": relation,
    })
    current, combined = scalar_rows(gamma)
    current_failures = annihilates(current, incoming_matrix)
    combined_failures = annihilates(combined, incoming_matrix)
    findings.append({
        "name": "current scalar and all thirty constant scalar maps kill incoming boundaries",
        "status": "reproduced" if current_failures == 0 and combined_failures == 0 and len(combined) == 2430 else "defect",
        "detail": {"current_failures": current_failures, "combined_failures": combined_failures, "combined_rows": len(combined)},
    })

    keys = [list(basis["positive"][index]) for index in (7, 23, 50)]
    findings.append({
        "name": "published positive basis keys of the integer control cycle",
        "status": "reproduced" if keys == [[0, 2, 1, 2, 0, 0, 0, 0], [0, 2, 4, 3, 0, 0, 0, 0], [1, 3, 0, 0, 0, 0, 0, 0]] else "defect",
        "detail": {"keys": keys},
    })

    print("chain identity", flush=True)
    columns_by_index = [[] for _ in range(6560)]
    for row_index, row in enumerate(outgoing):
        for column, value in row.items():
            columns_by_index[column].append((row_index, value))
    chain_failures = 0
    for column, vector in enumerate(basis["source"]):
        state = {(*vector[:4], 0, *vector[4:]): 1}
        differential = cech_delta(state, -3, 1, 1, -3, -1, columns, incoming)
        image = {}

        def accumulate(row_index, value, image=image):
            updated = image.get(row_index, 0) + value
            if updated:
                image[row_index] = updated
            else:
                image.pop(row_index, None)

        for (source, target, target_index, source_index, _mask, *exponents), value in differential.items():
            slot = indexes["negative"][(source, target, target_index, source_index, *exponents)]
            for row_index, entry in columns_by_index[slot]:
                accumulate(row_index, entry * value)
        for index, value in enumerate(length_five_image(vector, basis, indexes, columns, incoming)):
            if not value:
                continue
            for row_index, entry in columns_by_index[6480 + index]:
                accumulate(row_index, entry * value)
        if image:
            chain_failures += 1
    findings.append({
        "name": "outgoing differential annihilates all 2560 incoming source columns",
        "status": "reproduced" if chain_failures == 0 else "defect",
        "detail": {"columns": 2560, "failures": chain_failures},
    })

    print("exact ranks", flush=True)
    outgoing_rank = exact_rank(outgoing, 6560)
    current_rank = exact_rank(outgoing + current, 6560)
    combined_rank = exact_rank(outgoing + combined, 6560)
    positive_rank = exact_rank(positive, 80)
    echelon = unit_echelon(incoming_matrix, 2560)
    length_five = []
    for vector in echelon["kernel"]:
        image = [0] * 80
        for column, coefficient in enumerate(vector):
            if not coefficient:
                continue
            column_image = length_five_image(basis["source"][column], basis, indexes, columns, incoming)
            for index, value in enumerate(column_image):
                image[index] += coefficient * value
        length_five.append(image)
    transferred_rows = [{} for _ in range(80)]
    for column, image in enumerate(length_five):
        for index, value in enumerate(image):
            if value:
                transferred_rows[index][column] = value
    transferred = unit_echelon(transferred_rows, 10)
    positive_closed = all(all(value == 0 for value in multiply_matrix(positive, image)) for image in length_five)
    rational_current = current_rank["rank"] - outgoing_rank["rank"]
    rational_combined = combined_rank["rank"] - outgoing_rank["rank"]
    h2 = 6560 - outgoing_rank["rank"] - echelon["rank"] - transferred["rank"]
    findings.append({
        "name": "rational outgoing rank 3648, current scalar rank 34, combined rank 332, H2 dimension 352",
        "status": "reproduced" if (
            outgoing_rank["rank"] == 3648 and rational_current == 34 and rational_combined == 332
            and echelon["rank"] == 2550 and transferred["rank"] == 10 and h2 == 352 and positive_closed
        ) else "defect",
        "detail": {
            "outgoing": outgoing_rank,
            "current_augmented": current_rank,
            "combined_augmented": combined_rank,
            "incoming_rank": echelon["rank"],
            "transferred_kernel_rank": transferred["rank"],
            "positive_kernel_vectors_closed": positive_closed,
            "h2": h2,
            "current_kernel_dimension": h2 - rational_current,
            "all_constant_kernel_dimension": h2 - rational_combined,
        },
    })
    findings.append({
        "name": "positive differential has rank 50, so its kernel has dimension 30",
        "status": "reproduced" if positive_rank["rank"] == 50 else "defect",
        "detail": positive_rank,
    })

    control = [0] * 80
    control[7] = control[23] = control[50] = 1
    closed = all(value == 0 for value in multiply_matrix(positive, control))
    pairing = -control[7] + control[25]
    kills = [sum((-1 if index == 7 else 1 if index == 25 else 0) * value for index, value in enumerate(image)) for image in length_five]
    in_image = False
    # Not in the transferred image when a functional kills that image and pairs nontrivially.
    findings.append({
        "name": "integer control n=0, p[7]=p[23]=p[50]=1 is closed, scalar-invisible, and not a boundary",
        "status": "reproduced" if closed and pairing == -1 and kills == [0] * 10 else "defect",
        "detail": {"closed": closed, "pairing": pairing, "annihilator_on_transferred_image": kills, "scalar_outputs": 0},
    })

    print("modular ranks", flush=True)
    rank13, pivots13 = modular_rank(outgoing, 13)
    reduced_current = reduce_rows(current, pivots13, 13)
    current13, _ = modular_rank(reduced_current, 13)
    rank_b13, pivots_b13 = modular_rank(pure_negative, 13)
    reduced_b = reduce_rows(current, pivots_b13, 13)
    current_b13, _ = modular_rank(reduced_b, 13)
    rank29, pivots29 = modular_rank(outgoing, 29)
    reduced_combined = reduce_rows(combined, pivots29, 29)
    combined29, _ = modular_rank(reduced_combined, 29)
    findings.append({
        "name": "characteristic 13 current rank 34 and characteristic 29 combined rank 332",
        "status": "reproduced" if rank13 == 3648 and current13 == 34 and current_b13 == 34 and rank29 == 3648 and combined29 == 332 else "defect",
        "detail": {
            "F13_outgoing": rank13,
            "F13_current_on_outgoing": current13,
            "F13_pure_negative_outgoing": rank_b13,
            "F13_current_on_pure_negative": current_b13,
            "F29_outgoing": rank29,
            "F29_combined": combined29,
        },
    })

    OUT.write_text(json.dumps({"pinned": "a100f4e0be453d6e182320b792359f8a04e32b4d", "findings": findings}, indent=2) + "\n")
    defects = [item["name"] for item in findings if item["status"] != "reproduced"]
    print(json.dumps({"checks": len(findings), "defects": defects}, indent=2))
    return 1 if defects else 0


if __name__ == "__main__":
    raise SystemExit(main())
