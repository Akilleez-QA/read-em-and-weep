#!/usr/bin/env python3
"""Exact control of the original-cover D3 reducer.

Reruns the producer projection / reduce_target / vector path on the nine
alpha-multiplied lifted source columns at order 3, rebuilds that block over
Q, and compares it with the pinned certificate. A reducer that returns the
zero cochain must fail the same check.

Basis-list sizes and per-character multiplicities are recorded from the
supplied label lists. Those counts are an input boundary: this script does
not prove the lists are geometrically complete.

The producer directory is imported and is not modified.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

import sympy as sp

REVIEW = Path(__file__).resolve().parent
PKG = REVIEW.parent / "carrier" / "formal-five-parameter-chart"
AUDIT = PKG / "audit_original_cover"
# Finite frame weights d = (P, E0, E1, E2), the same tuple rebuilt_block uses.
FRAME = (3, 0, 2, 2)


def load_producer():
    spec = importlib.util.spec_from_file_location(
        "original_cover_audit", AUDIT / "check_original_cover.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_json(path: Path):
    return json.loads(path.read_text())


def source_character(label) -> int:
    """Relative character 2b - p0 - p1 - 2 - d_ch of a source label [ch, b, p]."""
    chart, degree, plane = label
    return 2 * degree - plane[0] - plane[1] - 2 - FRAME[chart]


def target_character(label) -> int:
    """Relative character 2b + p0 + p1 - d_i - d_j of a target label [[i, j], b, p]."""
    slot, degree, plane = label
    return 2 * degree + plane[0] + plane[1] - FRAME[slot[0]] - FRAME[slot[1]]


def character_census(order: int) -> dict:
    """Sizes and multiplicities of the label lists rebuilt_block reads at this order."""
    data = load_json(PKG / "data" / f"order_{order}.json")
    source = data[f"D{order}_source_basis"]
    target = data[f"D{order}_target_basis"]
    source_weights = [source_character(label) for label in source]
    target_weights = [target_character(label) for label in target]
    prescribed = order - 4
    source_index = [i for i, weight in enumerate(source_weights) if weight == prescribed]
    target_index = [i for i, weight in enumerate(target_weights) if weight == prescribed]
    return {
        "order": order,
        "prescribed_character": prescribed,
        "source_length": len(source),
        "target_length": len(target),
        "source_multiplicities": dict(sorted(Counter(source_weights).items())),
        "target_multiplicities": dict(sorted(Counter(target_weights).items())),
        "source_columns": source_index,
        "target_rows": target_index,
    }


def projected_lifts(producer, data: dict, order: int):
    """project(alpha * lifted source) on the prescribed-character source columns."""
    source = data[f"D{order}_source_basis"]
    target = data[f"D{order}_target_basis"]
    columns = [i for i, label in enumerate(source) if source_character(label) == order - 4]
    rows = [i for i, label in enumerate(target) if target_character(label) == order - 4]
    lookup = {
        (degree, *plane, *tuple(slot.count(i) for i in range(4))): index
        for index, (slot, degree, plane) in enumerate(target)
    }
    lifts = [
        producer.project(producer.times(producer.alpha[0], producer.make_source(source[index])))
        for index in columns
    ]
    return lifts, columns, rows, lookup


def apply_reducer(lifts, rows, lookup, reducer) -> sp.Matrix:
    """Producer vector extraction: reduce_target, then coordinates along `rows`."""
    vectors = []
    allowed = set(rows)
    for lift in lifts:
        reduced = reducer(lift, lookup)
        if not set(reduced) <= allowed:
            raise ValueError("Coefficient leaves the prescribed target rows.")
        vectors.append(sp.Matrix([sp.Rational(reduced.get(index, 0)) for index in rows]))
    return sp.Matrix.hstack(*vectors)


def zero_reducer(_value, _lookup) -> dict:
    """Deliberately vacuous reducer: every class is sent to the zero vector."""
    return {}


def certificate_d3() -> sp.Matrix:
    certificate = load_json(AUDIT / "certificate.json")
    rows = certificate["lambda_order_three"]["D3_hom"]
    matrix = sp.Matrix([[sp.Rational(entry) for entry in row] for row in rows])
    if any(not entry.is_rational for entry in matrix):
        raise ValueError("Certificate D3 is not rational.")
    return matrix


def require_invertible_match(rebuilt: sp.Matrix, expected: sp.Matrix) -> sp.Expr:
    """Exact check over Q. A zero or disagreeing block fails."""
    if rebuilt.shape != expected.shape:
        raise ValueError(f"shape {rebuilt.shape} != {expected.shape}")
    determinant = rebuilt.det()
    if determinant == 0:
        raise ValueError("rebuilt D3 is singular")
    if rebuilt != expected:
        raise ValueError("rebuilt D3 differs from the certificate")
    if determinant != expected.det():
        raise ValueError("determinant differs from the certificate")
    return determinant


def format_census(census: dict) -> str:
    lines = [
        f"order {census['order']}: source list {census['source_length']}, "
        f"target list {census['target_length']}, "
        f"prescribed character {census['prescribed_character']}: "
        f"{len(census['source_columns'])} columns, {len(census['target_rows'])} rows"
    ]
    lines.append("  source multiplicities " + _mult(census["source_multiplicities"]))
    lines.append("  target multiplicities " + _mult(census["target_multiplicities"]))
    return "\n".join(lines)


def _mult(weights: dict) -> str:
    return ", ".join(f"{weight}:{count}" for weight, count in weights.items())


def run_control() -> dict:
    producer = load_producer()
    data = load_json(PKG / "data" / "order_3.json")
    lifts, columns, rows, lookup = projected_lifts(producer, data, 3)
    rebuilt = apply_reducer(lifts, rows, lookup, producer.reduce_target)
    block, producer_columns, producer_rows, _vector = producer.rebuilt_block(data, 3)
    if rebuilt != block:
        raise ValueError("reducer path disagrees with producer.rebuilt_block")
    if columns != list(producer_columns) or rows != list(producer_rows):
        raise ValueError("prescribed character slice disagrees with producer.rebuilt_block")
    expected = certificate_d3()
    determinant = require_invertible_match(rebuilt, expected)
    stub = apply_reducer(lifts, rows, lookup, zero_reducer)
    stub_failed = False
    stub_error = ""
    try:
        require_invertible_match(stub, expected)
    except ValueError as error:
        stub_failed = True
        stub_error = str(error)
    if not stub_failed:
        raise ValueError("zero reducer was accepted")
    saved = producer.reduce_target
    producer.reduce_target = zero_reducer
    try:
        try:
            producer.rebuilt_block(data, 3)
        except ValueError as error:
            producer_stub_error = str(error)
        else:
            raise ValueError("producer.rebuilt_block accepted a zero reducer")
    finally:
        producer.reduce_target = saved
    census = [character_census(2), character_census(3)]
    return {
        "shape": list(rebuilt.shape),
        "determinant": str(determinant),
        "matches_certificate": True,
        "entries_in_Q": True,
        "stub_shape": list(stub.shape),
        "stub_determinant": str(stub.det()),
        "stub_is_zero": stub == sp.zeros(*stub.shape),
        "stub_check_failed": stub_failed,
        "stub_error": stub_error,
        "producer_stub_error": producer_stub_error,
        "source_columns": columns,
        "target_rows": rows,
        "census": census,
    }


def main() -> int:
    result = run_control()
    print(
        f"D3 {result['shape'][0]}x{result['shape'][1]} "
        f"det {result['determinant']} matches certificate: {result['matches_certificate']}"
    )
    print(
        f"zero reducer: {result['stub_shape'][0]}x{result['stub_shape'][1]} "
        f"det {result['stub_determinant']} zero matrix: {result['stub_is_zero']}; "
        f"check failed: {result['stub_check_failed']} ({result['stub_error']})"
    )
    print(f"producer.rebuilt_block(zero reducer) failed: {result['producer_stub_error']}")
    print("basis lists are a stated input; geometric completeness is not established")
    for census in result["census"]:
        print(format_census(census))
    ok = (
        result["determinant"] != "0"
        and result["matches_certificate"]
        and result["stub_check_failed"]
        and result["stub_determinant"] == "0"
    )
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
