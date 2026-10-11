#!/usr/bin/env python3
"""Compare the frozen k=4,5,6 bases and maps with the shipped D4, D5 and D6 blocks.

The frozen certificate is an input. Shipped labels are read only here, after
that certificate was committed. Arithmetic is exact over Q.
"""
from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path

import generate_bases as bases
import generate_higher as higher
from compare_labels import entry_difference, square_determinant

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
DATA = REPO / "research" / "carrier" / "formal-five-parameter-chart" / "data"
FROZEN = HERE / "frozen" / "higher_certificate.json"


def freeze_commit():
    return subprocess.check_output(
        ["git", "log", "-1", "--format=%H", "--", FROZEN.relative_to(REPO)],
        cwd=REPO,
        text=True,
    ).strip()


def split_labels(order, kind):
    labels = []
    for line in order[f"filtration_{kind}"]:
        slot = line["slot"]
        slot = slot if isinstance(slot, int) else tuple(slot)
        for exponent, u, v, w, _weight, character in line["H2_monomials"]:
            labels.append(
                {
                    "slot": slot,
                    "e": exponent,
                    "dual": (u, v, w),
                    "character": character,
                }
            )
    return labels


def actual_of(dual):
    return [-dual[0] - 1, -dual[1] - 1, -dual[2] - 1]


def ordered_identity(frozen_rows, shipped_rows):
    """Change of basis sending the frozen ordered basis to the shipped one."""
    size = len(frozen_rows)
    equal = frozen_rows == shipped_rows
    missing = [row for row in frozen_rows if row not in set(map(tuple, shipped_rows))] if not equal else []
    extra = [row for row in shipped_rows if row not in set(map(tuple, frozen_rows))] if not equal else []
    # Identity is the only candidate once both lists are equal and aligned.
    determinant = "1" if equal and size else "0"
    return {
        "size": size,
        "ordered_equal": equal,
        "matrix": "identity" if equal else "not the identity",
        "determinant_over_Q": determinant,
        "frozen_not_shipped": len(missing),
        "shipped_not_frozen": len(extra),
    }


def raw_alpha_column(k, target_index, channel, exponent, dual):
    finite, _infinity = bases.representative("U", channel, exponent, dual, k)
    relation = bases.relation_polynomials()
    image = bases.empty_components("W")
    for source, poly in finite.items():
        if not poly:
            continue
        for index, factor in enumerate(relation):
            slot = tuple(sorted((source, index)))
            image[slot] = bases.add(image[slot], bases.mul(poly, factor))
    column = {}
    for slot, poly in image.items():
        for (power, x, y, w), coeff in bases.project_negative(poly).items():
            key = (slot, power, (-x - 1, -y - 1, -w - 1))
            if key in target_index and coeff:
                column[target_index[key]] = column.get(target_index[key], Fraction(0)) + coeff
    return column


def matrix_times(left, right):
    """Left is square. Right may be rectangular, with one row per left column."""
    height = len(left)
    width = len(right[0]) if right else 0
    return [
        [sum(left[i][k] * right[k][j] for k in range(height)) for j in range(width)]
        for i in range(height)
    ]


def connecting_change(k, target_labels, shipped):
    """Row change of basis between delta_inner and the E0E1 columns of C."""
    if k == 4:
        return {
            "compared": False,
            "reason": "order 4 has H^3(E0^2)=0, so there is no C block",
        }
    positions = [index for index, label in enumerate(target_labels) if label["slot"] == (1, 2)]
    duals, rows, columns, _sparse = higher.delta_inner_columns(k)
    height = len(rows)
    width = len(columns)
    if len(positions) != width:
        raise ValueError("E0E1 count disagrees with delta_inner")
    shipped_block = [[Fraction(0) for _ in range(width)] for _ in range(height)]
    position = {raw: column for column, raw in enumerate(positions)}
    for row, column, value in shipped[f"C{k}_sparse"]:
        if column in position:
            shipped_block[row][position[column]] = Fraction(value)
    generated = [[columns[j][i] for j in range(width)] for i in range(height)]
    # Solve A * generated = shipped_block. Both are full rank of height `height`.
    chosen = []
    for column in range(width):
        trial = [[generated[i][j] for j in chosen + [column]] for i in range(height)]
        if higher.matrix_rank(trial) > len(chosen):
            chosen.append(column)
        if len(chosen) == height:
            break
    minor = [[generated[i][j] for j in chosen] for i in range(height)]
    image = [[shipped_block[i][j] for j in chosen] for i in range(height)]
    minor_t = [list(column) for column in zip(*minor)]
    solved = []
    for column in range(height):
        solved.append(solve_square(minor_t, [image[column][row] for row in range(height)]))
    change = [[solved[column][row] for column in range(height)] for row in range(height)]
    product = matrix_times(change, generated)
    mismatch = []
    for row in range(height):
        for column in range(width):
            if product[row][column] != shipped_block[row][column]:
                mismatch.append(
                    {
                        "row": row,
                        "column": column,
                        "generated_after_change": str(product[row][column]),
                        "shipped": str(shipped_block[row][column]),
                    }
                )
    return {
        "compared": True,
        "E0E1_columns": len(positions),
        "H3_rows": height,
        "change_of_basis": [[str(entry) for entry in row] for row in change],
        "determinant_over_Q": str(square_determinant(list(range(height)), {
            (row, column): change[row][column] for row in range(height) for column in range(height)
        })),
        "matches_C_on_E0E1": not mismatch,
        "mismatches": mismatch,
        "duals_head": [list(dual) for dual in duals[:3]],
    }


def solve_square(matrix, vector):
    size = len(matrix)
    grid = [matrix[row][:] + [vector[row]] for row in range(size)]
    for column in range(size):
        host = next(row for row in range(column, size) if grid[row][column])
        if host != column:
            grid[column], grid[host] = grid[host], grid[column]
        pivot = grid[column][column]
        grid[column] = [entry / pivot for entry in grid[column]]
        for row in range(size):
            if row == column or not grid[row][column]:
                continue
            factor = grid[row][column]
            grid[row] = [a - factor * b for a, b in zip(grid[row], grid[column])]
    return [grid[row][size] for row in range(size)]


def character_block(rebuilt, source_labels, target_rows, required):
    columns = [index for index, label in enumerate(source_labels) if label["character"] == required]
    rows = target_rows
    block = [[Fraction(0) for _ in columns] for _ in rows]
    column_pos = {index: place for place, index in enumerate(columns)}
    row_pos = {index: place for place, index in enumerate(rows)}
    for (row, column), value in rebuilt.items():
        if row in row_pos and column in column_pos:
            block[row_pos[row]][column_pos[column]] = value
    return block


def compare_order(document, k):
    order = document["orders"][str(k)]
    shipped = json.loads((DATA / f"order_{k}.json").read_text(encoding="utf-8"))
    source = split_labels(order, "U")
    target = split_labels(order, "W")
    shipped_source = [(channel, exponent, tuple(dual)) for channel, exponent, dual in shipped[f"D{k}_source_basis"]]
    frozen_source = [(label["slot"], label["e"], label["dual"]) for label in source]
    source_basis = ordered_identity(frozen_source, shipped_source)
    if k == 4:
        shipped_target = []
        for slot, exponent, actual in shipped["D4_target_basis"]:
            dual = tuple(-value - 1 for value in actual)
            shipped_target.append((tuple(slot), exponent, dual))
        free = list(range(len(target)))
        pivots = set()
    else:
        shipped_target = [
            (tuple(slot), exponent, tuple(dual)) for slot, exponent, dual in shipped[f"raw_W{k}_labels"]
        ]
        free = shipped[f"W{k}_kernel_free_columns"]
        pivots = set(shipped[f"C{k}_pivot_columns"])
    frozen_target = [(label["slot"], label["e"], label["dual"]) for label in target]
    target_basis = ordered_identity(frozen_target, shipped_target)
    index = {
        (label["slot"], label["e"], label["dual"]): position for position, label in enumerate(target)
    }
    rebuilt_raw = {}
    for column, label in enumerate(source):
        coeffs = raw_alpha_column(k, index, label["slot"], label["e"], label["dual"])
        for row, value in coeffs.items():
            if value:
                rebuilt_raw[(row, column)] = value
    kernel_free_ordered = free == [index for index in range(len(target)) if index not in pivots]
    free_pos = {raw: position for position, raw in enumerate(free)}
    rebuilt = {}
    pivot_nonzeros = 0
    for (row, column), value in rebuilt_raw.items():
        if row in pivots:
            pivot_nonzeros += 1
            continue
        rebuilt[(free_pos[row], column)] = value
    supplied = {
        (row, column): Fraction(value) for row, column, value in shipped[f"D{k}_sparse"]
    }
    difference = entry_difference(rebuilt, supplied)
    # Every alpha column lies in the kernel of C when that block exists.
    kernel_failures = 0
    if k > 4:
        entries = shipped[f"C{k}_sparse"]
        height = 1 + max(row for row, _column, _value in entries)
        for column in range(len(source)):
            total = [Fraction(0) for _ in range(height)]
            present = {row: value for (row, col), value in rebuilt_raw.items() if col == column}
            for row, raw, value in entries:
                if raw in present:
                    total[row] += Fraction(value) * present[raw]
            if any(total):
                kernel_failures += 1
    required = k - 4
    required_rows = [
        free_pos[index[(label["slot"], label["e"], label["dual"])]]
        for label in target
        if label["character"] == required
    ]
    block = character_block(rebuilt, source, required_rows, required)
    frozen_block = [[Fraction(entry) for entry in row] for row in order["alpha_matrix"]]
    block_equal = block == frozen_block
    return {
        "k": k,
        "map": f"D{k}",
        "shipped_shape": shipped[f"D{k}_shape"],
        "frozen_dimension_U": order["cohomology_dimensions"]["dimension_U"],
        "frozen_dimension_W": order["cohomology_dimensions"]["dimension_W"],
        "source_change_of_basis": source_basis,
        "target_change_of_basis": target_basis,
        "kernel_free_rows": len(free),
        "kernel_free_is_ordered_complement_of_pivots": kernel_free_ordered,
        "full_matrix": difference,
        "full_nonzero_rebuilt": len(rebuilt),
        "full_nonzero_shipped": len(supplied),
        "pivot_coordinates_in_raw_image": pivot_nonzeros,
        "alpha_columns_outside_C_kernel": kernel_failures,
        "required_character": required,
        "required_block_matches_frozen_alpha": block_equal,
        "required_block_determinant_over_Q": str(higher.square_determinant(block)) if block else None,
        "connecting_change_of_basis": connecting_change(k, target, shipped),
    }


def summarize(document):
    orders = [compare_order(document, k) for k in (4, 5, 6)]
    maximum = document["generated_max_character"]
    ok = True
    for item in orders:
        ok = ok and item["source_change_of_basis"]["ordered_equal"]
        ok = ok and item["target_change_of_basis"]["ordered_equal"]
        ok = ok and item["kernel_free_is_ordered_complement_of_pivots"]
        ok = ok and item["kernel_free_rows"] == item["shipped_shape"][0]
        ok = ok and item["full_matrix"]["equal"]
        ok = ok and item["alpha_columns_outside_C_kernel"] == 0
        ok = ok and item["required_block_matches_frozen_alpha"]
        change = item["connecting_change_of_basis"]
        if change["compared"]:
            ok = ok and change["matches_C_on_E0E1"]
            ok = ok and Fraction(change["determinant_over_Q"]) != 0
    return {
        "frozen_certificate": str(FROZEN.relative_to(REPO)),
        "content_sha256": document["content_sha256"],
        "freeze_commit": freeze_commit(),
        "arithmetic": "exact rational",
        "generated_max_character": maximum,
        "weight_cutoff_from_k": document["weight_cutoff_from_k"],
        "weight_cutoff_uses_generated_maximum": all(
            row["required_character"] > max(maximum["U"], maximum["W"])
            for row in document["weight_cutoff_checks"]
        ),
        "orders": orders,
        "mismatch": not ok,
    }


def render_markdown(report):
    lines = [
        "# Comparison receipt for orders 4, 5 and 6",
        "",
        "The bases and connecting matrices were frozen before this comparison.",
        "Shipped labels and sparse maps were not inputs to the enumeration.",
        "",
        f"- Frozen certificate: `{report['frozen_certificate']}`",
        f"- Content SHA-256: `{report['content_sha256']}`",
        f"- Freeze commit: `{report['freeze_commit']}`",
        "",
        "The change of basis on each ordered source list, and on each raw target list, is the identity.",
        "Its determinant over Q is 1. No integrality claim is made beyond that explicit matrix.",
        "At orders 5 and 6 the shipped row order is the kernel-free subsequence of that raw list.",
        "Deleting the pivot rows leaves the identity on the surviving classes.",
        "",
        f"Generated maximum character: U {report['generated_max_character']['U']}, "
        f"W {report['generated_max_character']['W']}.",
        f"Weight-only vanishing from k ≥ {report['weight_cutoff_from_k']} uses this generated maximum: "
        f"{report['weight_cutoff_uses_generated_maximum']}.",
        "",
    ]
    for item in report["orders"]:
        source = item["source_change_of_basis"]
        target = item["target_change_of_basis"]
        full = item["full_matrix"]
        connecting = item["connecting_change_of_basis"]
        lines.extend(
            [
                f"## {item['map']}",
                "",
                f"- Frozen dimensions: source {item['frozen_dimension_U']}, target {item['frozen_dimension_W']}.",
                f"- Shipped shape: {item['shipped_shape'][0]} target rows by {item['shipped_shape'][1]} source columns.",
                f"- Source change of basis: {source['matrix']} of size {source['size']}, determinant {source['determinant_over_Q']}.",
                f"- Raw target change of basis: {target['matrix']} of size {target['size']}, determinant {target['determinant_over_Q']}.",
                f"- Kernel-free rows: {item['kernel_free_rows']}, the ordered complement of the pivots: {item['kernel_free_is_ordered_complement_of_pivots']}.",
                f"- Nonzero entries: rebuilt {item['full_nonzero_rebuilt']}, shipped {item['full_nonzero_shipped']}.",
                f"- Map equal over Q: {full['equal']}.",
                f"- Raw image meets a C-pivot coordinate: {item['pivot_coordinates_in_raw_image']} times.",
                f"- Alpha columns outside the C kernel: {item['alpha_columns_outside_C_kernel']}.",
                f"- Required character {item['required_character']} block matches the frozen alpha matrix: {item['required_block_matches_frozen_alpha']}.",
                f"- Required block determinant over Q: {item['required_block_determinant_over_Q']}.",
                "",
            ]
        )
        if connecting["compared"]:
            lines.extend(
                [
                    f"- E0E1 columns of C{item['k']} equal the frozen inner connecting map after the row change",
                    f"  `{connecting['change_of_basis']}`, determinant {connecting['determinant_over_Q']}.",
                    f"- That identification matches entrywise: {connecting['matches_C_on_E0E1']}.",
                    "",
                ]
            )
        if not full["equal"]:
            lines.append("Matrix mismatches:")
            lines.append("```")
            lines.append(json.dumps(full, indent=2))
            lines.append("```")
            lines.append("")
    if report["mismatch"]:
        lines.append("A mismatch is recorded above.")
    else:
        lines.append(
            "No mismatch. Ordered labels agree, both full maps agree over Q, and the "
            "connecting-map change of basis is invertible."
        )
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json-output", type=Path, required=True)
    parser.add_argument("--markdown-output", type=Path, required=True)
    args = parser.parse_args()
    digest = higher.verify_certificate(FROZEN)
    document = json.loads(FROZEN.read_text(encoding="utf-8"))
    if document["content_sha256"] != digest:
        raise SystemExit("frozen certificate hash mismatch")
    report = summarize(document)
    args.json_output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    args.markdown_output.write_text(render_markdown(report), encoding="utf-8")
    print(render_markdown(report))
    if report["mismatch"]:
        raise SystemExit("label or matrix mismatch")


if __name__ == "__main__":
    main()
