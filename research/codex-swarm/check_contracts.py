"""Small exact controls for certificate contracts, never a physical-source runner.

Only the reconstructed ownership partition, elementary coefficient functional,
and finite-dimensional detector theorem are exercised. No HM coefficients,
source jets, or obstruction values are computed here.
"""
from fractions import Fraction as Q
from itertools import permutations
import json
from pathlib import Path

ROWS = {
    2: (("M11", 9, 3, 1), ("M11", 10, 4, 1), ("M11", 12, 6, -2)),
    3: (("M10", 0, 3, 1), ("M10", 2, 6, 2), ("M21", 10, 1, 1), ("M21", 12, 5, 2)),
    # These are terminal-row coefficients, before the lift sign. The source
    # fingerprint has +orientation for BOTH q4 factored words; the M20 minus
    # cancels the negative second lift. bind_seed_fingerprints.py checks that.
    4: (("M20", 0, 0, -1), ("M31", 10, 0, 1)),
}


def rank(rows, columns):
    """Exact rational rank. This helper is bounded to tiny control matrices."""
    rows = [list(map(Q, row)) for row in rows]
    if columns < 0 or any(len(row) != columns for row in rows):
        raise ValueError("matrix shape")
    if len(rows) * max(columns, 1) > 4096:
        raise ValueError("toy-control matrix cap; no dense model runs")
    pivot = 0
    for column in range(columns):
        found = next((r for r in range(pivot, len(rows)) if rows[r][column]), None)
        if found is None:
            continue
        rows[pivot], rows[found] = rows[found], rows[pivot]
        scale = rows[pivot][column]
        rows[pivot] = [x / scale for x in rows[pivot]]
        for r in range(len(rows)):
            if r != pivot:
                factor = rows[r][column]
                rows[r] = [x - factor * y for x, y in zip(rows[r], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot


def dot(a, b):
    if len(a) != len(b):
        raise ValueError("vector shape")
    return sum((Q(x) * Q(y) for x, y in zip(a, b)), Q(0))


def complete_detector_contract(boundary_columns, differential_rows, detector_rows, n):
    """Check AB=LB=0 and rank([A;L])=n-rank(B), over Q.

    This says NOTHING about a geometric source unless its source-to-model bridge
    and membership in this exact complex are separately authenticated.
    """
    boundary_columns = [tuple(c) for c in boundary_columns]
    all_rows = [tuple(r) for r in differential_rows] + [tuple(r) for r in detector_rows]
    if any(len(v) != n for v in boundary_columns + all_rows):
        raise ValueError("matrix shape")
    if any(dot(row, col) for row in all_rows for col in boundary_columns):
        raise ValueError("not a complex or a boundary-annihilating detector")
    b = rank(boundary_columns, n)  # rank(B^t)=rank(B)
    return rank(all_rows, n) == n - b


def coefficient_weight(kappa, exponent, a_multiplier, b_multipliers):
    """Exact w(a) for explicitly supplied finite Laurent multipliers.

    The caller must authenticate the actual cleared expression and the complete
    permitted exponent domain before using this identity for an exclusion.
    """
    d = len(kappa)
    if len(exponent) != d or len(b_multipliers) != d:
        raise ValueError("exponent dimension")
    if any(len(k) != d for p in [a_multiplier, *b_multipliers] for k in p):
        raise ValueError("multiplier dimension")
    target = tuple(k - a for k, a in zip(kappa, exponent))
    value = Q(a_multiplier.get(target, 0))
    for i, multiplier in enumerate(b_multipliers):
        shifted = tuple(x + (j == i) for j, x in enumerate(target))
        value += exponent[i] * Q(multiplier.get(shifted, 0))
    return value


def reconstructed_partition():
    """Proposed tuple keys; NOT the unpublished original generator numbering."""
    result = {}
    worker = 0
    for q, rows in ROWS.items():
        seeds = [(q, row, p) for row in rows for p in permutations(range(1, q + 1))]
        for channel in ("E12", "E34"):
            for half in range(2):
                worker += 1
                lo, hi = half * len(seeds) // 2, (half + 1) * len(seeds) // 2
                result[f"Codex-C{worker:02}"] = [(*seed, channel) for seed in seeds[lo:hi]]
    return result


def check(condition, message):
    # Explicit checks remain active under python -O.
    if not condition:
        raise ValueError(message)


def self_test():
    partition = reconstructed_partition()
    keys = [key for cells in partition.values() for key in cells]
    check(len(keys) == len(set(keys)) == 156, "seed-channel ownership")
    check([len(v) for v in partition.values()] == [3]*4 + [12]*4 + [24]*4, "half sizes")
    roster = json.loads(Path(__file__).with_name("workers.json").read_text())
    ids = [w["identity"] for w in roster]
    check(len(ids) == len(set(ids)) == 36, "worker identities")
    check(set(partition).issubset(ids), "sector owners missing")

    b = [(1, 0, 0, 0)]
    a = [(0, 0, 0, 1)]
    ell, extra = (0, 1, 0, 0), (0, 0, 1, 0)
    check(not complete_detector_contract(b, a, [ell], 4), "incomplete detector accepted")
    check(not complete_detector_contract(b, a, [tuple(j*x for x in ell) for j in range(1,79)], 4), "duplicate detectors accepted")
    check(complete_detector_contract(b, a, [ell, extra], 4), "complete detector rejected")
    check(rank(b + [extra], 4) == 2 and dot(ell, extra) == dot(a[0], extra) == 0, "invisible nonboundary control")
    try:
        complete_detector_contract(b, a, [(1, 0, 0, 0)], 4)
    except ValueError:
        pass
    else:
        raise ValueError("invalid detector accepted")

    check(coefficient_weight((2,), (1,), {}, [{(2,): 1}]) == 1, "derivative shift")
    check(coefficient_weight((-1,), (-1,), {}, [{(1,): 1}]) == -1, "Laurent derivative")
    # [-x^1] is NOT used: [-P+x P'] has zero x^1 coefficient for every P.
    check(coefficient_weight((1,), (1,), {(0,): -1}, [{(1,): 1}]) == 0, "overlap cancellation")
    check(coefficient_weight((1,), (1,), {(0,): -1}, [{(1,): 2}]) == 1, "cancellation negative control")
    print(json.dumps({"status": "pass", "identities": 36, "proposed_seed_channel_cells": 156,
                      "source_label_coverage": "unproved", "incumbent_binding": "checked separately by bind_seed_fingerprints.py",
                      "physical_source_evaluated": False, "obstruction": "undecided"}, sort_keys=True))


if __name__ == "__main__":
    self_test()
