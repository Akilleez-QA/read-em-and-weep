#!/usr/bin/env python3
"""Compare the frozen k=2,3 bases with the shipped D2 and D3 labels.

The bijection and the alpha matrices are built from the frozen certificate.
Shipped labels and sparse maps are read only here, after that certificate
was committed. Arithmetic is exact over Q.
"""
from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path

import generate_bases as bases

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
DATA = REPO / "research" / "carrier" / "formal-five-parameter-chart" / "data"
FROZEN = HERE / "frozen" / "basis_certificate.json"
D_FINITE = (3, 0, 2, 2)


def freeze_commit():
    return subprocess.check_output(
        ["git", "log", "-1", "--format=%H", "--", FROZEN.relative_to(REPO)],
        cwd=REPO,
        text=True,
    ).strip()


def finite_from_record(kind, vector):
    slot = tuple(vector["slot"]) if isinstance(vector["slot"], list) else vector["slot"]
    finite = bases.empty_components(kind)
    actual = vector["actual"]
    finite[slot] = {(vector["e"], actual[0], actual[1], actual[2]): Fraction(1)}
    for term in vector["forced"]:
        lower = tuple(term["slot"]) if isinstance(term["slot"], list) else term["slot"]
        exponent = (term["e"], term["actual"][0], term["actual"][1], term["actual"][2])
        finite[lower] = bases.add(finite[lower], {exponent: Fraction(term["coefficient"])})
    return finite


def source_character(channel, exponent, dual):
    return 2 * exponent - dual[0] - dual[1] - 2 - D_FINITE[channel]


def target_character(slot, exponent, actual):
    return 2 * exponent + actual[0] + actual[1] - D_FINITE[slot[0]] - D_FINITE[slot[1]]


def entry_difference(rebuilt, shipped):
    """Exact symmetric difference of two sparse matrices of rationals."""
    only_rebuilt = []
    only_shipped = []
    disagreements = []
    for key in sorted(set(rebuilt) | set(shipped)):
        left = rebuilt.get(key, Fraction(0))
        right = shipped.get(key, Fraction(0))
        if left == right:
            continue
        row, column = key
        if key not in shipped:
            only_rebuilt.append({"row": row, "column": column, "rebuilt": str(left)})
        elif key not in rebuilt:
            only_shipped.append({"row": row, "column": column, "shipped": str(right)})
        else:
            disagreements.append(
                {"row": row, "column": column, "rebuilt": str(left), "shipped": str(right)}
            )
    return {
        "only_rebuilt": only_rebuilt,
        "only_shipped": only_shipped,
        "value_disagreements": disagreements,
        "equal": not only_rebuilt and not only_shipped and not disagreements,
    }


def matrix_rank(rows, columns, sparse):
    """Rank over Q of the submatrix with the given row and column index lists."""
    width = len(columns)
    column_index = {column: index for index, column in enumerate(columns)}
    grid = [[Fraction(0) for _ in range(width)] for _ in rows]
    row_index = {row: index for index, row in enumerate(rows)}
    for (row, column), value in sparse.items():
        if row in row_index and column in column_index and value:
            grid[row_index[row]][column_index[column]] = value
    rank = 0
    pivot_column = 0
    for row in range(len(rows)):
        while pivot_column < width:
            host = next((i for i in range(rank, len(rows)) if grid[i][pivot_column]), None)
            if host is None:
                pivot_column += 1
                continue
            grid[rank], grid[host] = grid[host], grid[rank]
            scale = grid[rank][pivot_column]
            grid[rank] = [entry / scale for entry in grid[rank]]
            for other in range(len(rows)):
                if other == rank or not grid[other][pivot_column]:
                    continue
                factor = grid[other][pivot_column]
                grid[other] = [a - factor * b for a, b in zip(grid[other], grid[rank])]
            rank += 1
            pivot_column += 1
            break
    return rank


def square_determinant(index_rows, sparse):
    size = len(index_rows)
    position = {row: index for index, row in enumerate(index_rows)}
    grid = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    for (row, column), value in sparse.items():
        if row in position and column in position:
            grid[position[row]][position[column]] = value
    det = Fraction(1)
    for pivot in range(size):
        host = next((i for i in range(pivot, size) if grid[i][pivot]), None)
        if host is None:
            return Fraction(0)
        if host != pivot:
            grid[pivot], grid[host] = grid[host], grid[pivot]
            det = -det
        scale = grid[pivot][pivot]
        det *= scale
        for lower in range(pivot + 1, size):
            if not grid[lower][pivot]:
                continue
            factor = grid[lower][pivot] / scale
            for column in range(pivot, size):
                grid[lower][column] -= factor * grid[pivot][column]
    return det


def compare_order(document, k, prefix):
    shipped = json.loads((DATA / f"order_{k}.json").read_text(encoding="utf-8"))
    source = shipped[f"{prefix}_source_basis"]
    target = shipped[f"{prefix}_target_basis"]
    order = document["orders"][str(k)]
    our_source = [(vector["slot"], vector["e"], vector["dual"]) for vector in order["U"]]
    ship_source = [(channel, exponent, dual) for channel, exponent, dual in source]
    our_target = [(vector["slot"], vector["e"], vector["actual"]) for vector in order["W"]]
    ship_target = [(slot, exponent, actual) for slot, exponent, actual in target]
    frozen_source_set = {(slot, exponent, tuple(dual)) for slot, exponent, dual in our_source}
    shipped_source_set = {(channel, exponent, tuple(dual)) for channel, exponent, dual in ship_source}
    frozen_target_set = {(tuple(slot), exponent, tuple(actual)) for slot, exponent, actual in our_target}
    shipped_target_set = {(tuple(slot), exponent, tuple(actual)) for slot, exponent, actual in ship_target}
    source_missing = sorted(frozen_source_set - shipped_source_set)
    source_extra = sorted(shipped_source_set - frozen_source_set)
    target_missing = sorted(frozen_target_set - shipped_target_set)
    target_extra = sorted(shipped_target_set - frozen_target_set)
    source_identity = our_source == ship_source
    target_identity = our_target == ship_target
    target_index = {
        (tuple(slot), exponent, tuple(actual)): index
        for index, (slot, exponent, actual) in enumerate(target)
    }
    rebuilt = {}
    outside = []
    for column, vector in enumerate(order["U"]):
        finite = finite_from_record("U", vector)
        for key, value in bases.alpha_image(k, finite).items():
            slot = (key[0], key[1])
            dual = key[3:]
            actual = tuple(-n - 1 for n in dual)
            label = (slot, key[2], actual)
            if label not in target_index:
                outside.append({"column": column, "label": [list(slot), key[2], list(actual)], "value": str(value)})
                continue
            if value:
                rebuilt[(target_index[label], column)] = value
    supplied = {
        (row, column): Fraction(value)
        for row, column, value in shipped[f"{prefix}_sparse"]
    }
    difference = entry_difference(rebuilt, supplied)
    character = k - 4
    source_columns = [
        index
        for index, (channel, exponent, dual) in enumerate(source)
        if source_character(channel, exponent, dual) == character
    ]
    target_rows = [
        index
        for index, (slot, exponent, actual) in enumerate(target)
        if target_character(slot, exponent, actual) == character
    ]
    slice_rebuilt = {
        key: value
        for key, value in rebuilt.items()
        if key[0] in set(target_rows) and key[1] in set(source_columns)
    }
    slice_supplied = {
        key: value
        for key, value in supplied.items()
        if key[0] in set(target_rows) and key[1] in set(source_columns)
    }
    slice_difference = entry_difference(slice_rebuilt, slice_supplied)
    rank = matrix_rank(target_rows, source_columns, rebuilt)
    determinant = None
    if len(target_rows) == len(source_columns):
        compressed = {}
        row_pos = {row: index for index, row in enumerate(target_rows)}
        col_pos = {column: index for index, column in enumerate(source_columns)}
        for (row, column), value in slice_rebuilt.items():
            compressed[(row_pos[row], col_pos[column])] = value
        determinant = str(square_determinant(list(range(len(target_rows))), compressed))
    return {
        "k": k,
        "map": prefix,
        "frozen_dimension_U": order["dimension_U"],
        "frozen_dimension_W": order["dimension_W"],
        "shipped_shape": shipped[f"{prefix}_shape"],
        "source_set_equal": not source_missing and not source_extra,
        "target_set_equal": not target_missing and not target_extra,
        "source_only_frozen": [[item[0], item[1], list(item[2])] for item in source_missing],
        "source_only_shipped": [[item[0], item[1], list(item[2])] for item in source_extra],
        "target_only_frozen": [[list(item[0]), item[1], list(item[2])] for item in target_missing],
        "target_only_shipped": [[list(item[0]), item[1], list(item[2])] for item in target_extra],
        "ordered_source_identity": source_identity,
        "ordered_target_identity": target_identity,
        "bijection": "identity on the ordered labels" if source_identity and target_identity else "not the identity",
        "alpha_coordinates_outside_target": outside,
        "full_matrix": difference,
        "full_nonzero_rebuilt": len(rebuilt),
        "full_nonzero_shipped": len(supplied),
        "character": character,
        "slice_source_columns": len(source_columns),
        "slice_target_rows": len(target_rows),
        "slice_matrix": slice_difference,
        "slice_rank_over_Q": rank,
        "slice_determinant_over_Q": determinant,
    }


def summarize(document):
    orders = []
    ok = True
    for k, prefix in ((2, "D2"), (3, "D3")):
        item = compare_order(document, k, prefix)
        orders.append(item)
        ok = ok and item["source_set_equal"] and item["target_set_equal"]
        ok = ok and item["ordered_source_identity"] and item["ordered_target_identity"]
        ok = ok and not item["alpha_coordinates_outside_target"]
        ok = ok and item["full_matrix"]["equal"] and item["slice_matrix"]["equal"]
    return {
        "frozen_certificate": str(FROZEN.relative_to(REPO)),
        "content_sha256": document["content_sha256"],
        "freeze_commit": freeze_commit(),
        "arithmetic": "exact rational",
        "bijection_rule": {
            "source": "frozen U (slot, z exponent, dual indices) equals shipped [slot, exponent, dual]",
            "target": "frozen W (slot, z exponent, actual exponents) equals shipped [slot, exponent, actual]",
        },
        "orders": orders,
        "mismatch": not ok,
    }


def render_markdown(report):
    lines = [
        "# Comparison receipt",
        "",
        "The bases were frozen before this comparison. Shipped labels and sparse",
        "maps were not inputs to the enumeration.",
        "",
        f"- Frozen certificate: `{report['frozen_certificate']}`",
        f"- Content SHA-256: `{report['content_sha256']}`",
        f"- Freeze commit: `{report['freeze_commit']}`",
        "",
        "The bijection is the identity on ordered labels.",
        "A frozen U record `(slot, e, dual)` is the shipped source label `[slot, e, dual]`.",
        "A frozen W record `(slot, e, actual)` is the shipped target label `[slot, e, actual]`.",
        "The change-of-basis matrix is the identity, so the rebuilt alpha matrix is",
        "compared in that common order.",
        "",
        "Alpha multiplication uses the frozen finite representative of each U basis",
        "vector, the finite relation `(-a0, W^6, -g, XY)`, the all-negative projection,",
        "and removal of forced lower terms with the same cutoff as the basis.",
        "",
    ]
    for item in report["orders"]:
        full = item["full_matrix"]
        sl = item["slice_matrix"]
        lines.extend(
            [
                f"## {item['map']}",
                "",
                f"- Frozen dimensions: source {item['frozen_dimension_U']}, target {item['frozen_dimension_W']}.",
                f"- Shipped shape: {item['shipped_shape'][0]} target rows by {item['shipped_shape'][1]} source columns.",
                f"- Label sets equal: source {item['source_set_equal']}, target {item['target_set_equal']}.",
                f"- Ordered identity: source {item['ordered_source_identity']}, target {item['ordered_target_identity']}.",
                f"- Nonzero entries: rebuilt {item['full_nonzero_rebuilt']}, shipped {item['full_nonzero_shipped']}.",
                f"- Full matrix equal over Q: {full['equal']}.",
                f"- Character {item['character']} slice: {item['slice_target_rows']} rows by {item['slice_source_columns']} columns.",
                f"- Slice equal over Q: {sl['equal']}.",
                f"- Slice rank over Q: {item['slice_rank_over_Q']}.",
                "- Slice determinant over Q: "
                + (
                    item["slice_determinant_over_Q"]
                    if item["slice_determinant_over_Q"] is not None
                    else "the slice is not square"
                )
                + ".",
                "",
            ]
        )
        if not full["equal"]:
            lines.append("Full-matrix mismatches:")
            lines.append("```")
            lines.append(json.dumps(full, indent=2))
            lines.append("```")
            lines.append("")
        if not sl["equal"]:
            lines.append("Slice mismatches:")
            lines.append("```")
            lines.append(json.dumps(sl, indent=2))
            lines.append("```")
            lines.append("")
    if report["mismatch"]:
        lines.append("A mismatch is recorded in the lists above and in the JSON receipt.")
    else:
        lines.append("No mismatch. The ordered labels and both full matrices agree exactly over Q.")
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json-output", type=Path, required=True)
    parser.add_argument("--markdown-output", type=Path, required=True)
    args = parser.parse_args()
    digest = bases.verify_certificate(FROZEN)
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
