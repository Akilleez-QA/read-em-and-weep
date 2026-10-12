#!/usr/bin/env python3
"""Exact integral certificate for the twist -2 hypercohomology differential d_5.

The input is the four-term Horrocks-Mumford-type complex of line-bundle sums
on P^4 over Z, reconstructed from the pinned source
research/hm/verify-hm-ext.js (git blob fa5231de92b61143e3406111d4af028284db6d55):

    C = [5 O(-1) -> 15 O -> 10 O(1) -> 2 O(2)],
    C^u = ranks[u] O(u-1), ranks = [5, 15, 10, 2].

End(C)(t) has terms Hom(C^u, C^{u+r})(t) = (ranks[u] * ranks[u+r]) O(r+t).
At t = -2 the only nonzero E_1 terms of hypercohomology that meet total
degrees 1, 2, 3 are

    H^4(O(-5))^10          (r = -3, total degree 1),
    H^0(O)^80              (r = 2,  total degree 2),
    H^0(O(1))^10 = Z^50    (r = 3,  total degree 3).

The differential d_5 lands in K = ker(H^0(O)^80 -> H^0(O(1))^10).
The target H^0(O(1))^10 is 50-dimensional. This program builds that map
by a Cech zigzag and prints a JSON certificate. Over Z, and hence over Q
and F_3, the certificate is hypercohomology of End(C)(-2) for this pinned
perfect complex. It does not identify the resulting ranks with End(H).

Conventions (pinned):

* Cover: U_i = {x_i != 0}, i = 0..4.
* A Laurent monomial x^a is a section of O(sum a) on U_I iff a_j >= 0 for
  every j not in I.
* Cech differential, ordered simplices: (delta c)_J = sum_k (-1)^k c_{J \\ j_k}.
* Hom differential, internal degree r:
      f |-> d o f - (-1)^r f o d,
  with the precomposition sign equal to -1 if r is even and +1 if r is odd
  (the same rule as z * (r even ? -1 : +1) in the pinned builder).
* Total differential on the Cech-Hom double complex:
      D = delta + (-1)^p d_Hom,
  where p is the Cech degree. This is the sign that makes D^2 = 0 when
  delta and d_Hom commute and each squares to zero.
* Cone contraction. On a monomial strand whose exponent vector is not entirely
  negative, choose the contraction vertex v among indices with exponent >= 0.
  The pinned choice is the least such index; the greatest-vertex comparison
  uses the greatest. If I = (i_0 < ... < i_p) and v = i_m, the homotopy is
      h(e_I) = (-1)^m e_{I \\ v}  if v in I, else 0.
  On each contractible used term of Cech degree at least 1, both cone
  identities hold: delta h + h delta = id for the least-vertex homotopy and
  for the greatest-vertex homotopy. Strands are signed simplex cochain
  complexes; the homotopy is the integral cone contraction onto the chosen
  vertex.
* Zigzag stage signs, forced by D = delta + (-1)^p d_Hom. Starting from a
  Cech 4-cocycle y at r = -3, four times:
      w = d_Hom(y),  z = (-1)^{p+1} h(w),  y <- z,  p <- p-1,
  then one final d_Hom. The multipliers of h o d_Hom are -1, +1, -1, +1
  at p = 4, 3, 2, 1, and the final d_Hom at p = 0 is unsigned.

Run from the repository root:

    python3 research/hsd/twist-minus2-d5/certificate.py
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

RANKS = [5, 15, 10, 2]
PINNED_BLOB = "fa5231de92b61143e3406111d4af028284db6d55"
SOURCE_RELATIVE = "research/hm/verify-hm-ext.js"
# Distinct y and w keys checked for each contraction policy.
TERMS_CHECKED_PER_POLICY = 5340

# Degree-1 monomials in the order produced by the recursive graded basis
# used with the pinned Hom builder: outermost exponent runs slowest.
DEGREE_ONE = (
    (0, 0, 0, 0, 1),
    (0, 0, 0, 1, 0),
    (0, 0, 1, 0, 0),
    (0, 1, 0, 0, 0),
    (1, 0, 0, 0, 0),
)
DEGREE_ONE_INDEX = {mono: i for i, mono in enumerate(DEGREE_ONE)}
ZERO_MONO = (0, 0, 0, 0, 0)
FULL_POLE = (-1, -1, -1, -1, -1)


def eprint(message: str) -> None:
    print(message, file=sys.stderr)


def egcd(a: int, b: int) -> tuple[int, int, int]:
    """Return (g, s, t) with g = gcd(|a|,|b|) > 0 unless a = b = 0, and s*a + t*b = g."""
    if b == 0:
        if a == 0:
            return 0, 1, 0
        return abs(a), (1 if a > 0 else -1), 0
    g, s1, t1 = egcd(b, a % b)
    return g, t1, s1 - t1 * (a // b)


def add_num(a, b):
    if isinstance(a, int):
        return a + b
    return tuple(x + y for x, y in zip(a, b))


def scale_num(a, s: int):
    if s == 1:
        return a
    if isinstance(a, int):
        return a * s
    if s == -1:
        return tuple(-x for x in a)
    return tuple(s * x for x in a)


def is_zero(a) -> bool:
    if isinstance(a, int):
        return a == 0
    return all(x == 0 for x in a)


def coeff_max(a) -> int:
    if isinstance(a, int):
        return abs(a)
    return max((abs(x) for x in a), default=0)


# ---------------------------------------------------------------------------
# Line-bundle complex, copied from the pinned construction.
# ---------------------------------------------------------------------------

def permutation_sign(values: tuple[int, ...]) -> int:
    if len(set(values)) < 5:
        return 0
    inversions = 0
    for i in range(5):
        for j in range(i + 1, 5):
            if values[i] > values[j]:
                inversions += 1
    return -1 if inversions % 2 else 1


def w_plus(i: int) -> tuple[int, int]:
    return ((i + 2) % 5, (i + 3) % 5)


def w_minus(i: int) -> tuple[int, int]:
    return ((i + 1) % 5, (i + 4) % 5)


def build_line_differentials():
    """Return d_out[level][column] = list of (row, variable, coefficient).

    level 0, 1, 2 are the three differentials of C. Also return the incoming
    representation incoming[level][row] = list of (column, variable, coefficient).
    """
    gamma = [[[0] * 5 for _ in range(5)] for _ in range(15)]
    nonzero = 0
    for r in range(15):
        for a in range(5):
            left = w_plus(a) if (r < 5 or r >= 10) else w_minus(a)
            if r < 5:
                right = w_plus(r)
            elif r < 10:
                right = w_minus(r - 5)
            else:
                right = w_minus(r - 10)
            for k in range(5):
                gamma[r][a][k] = permutation_sign((k, left[0], left[1], right[0], right[1]))
                if gamma[r][a][k]:
                    nonzero += 1
    d_out: list[list[list[tuple[int, int, int]]]] = [
        [[] for _ in range(RANKS[level])] for level in range(3)
    ]
    for a in range(5):
        for r in range(15):
            for k in range(5):
                coefficient = gamma[r][a][k]
                if coefficient:
                    d_out[0][a].append((r, k, coefficient))
    for i in range(5):
        for column, head, pair in (
            (i, 0, w_plus(i)),
            (i + 5, 1, w_minus(i)),
            (i + 10, 0, w_minus(i)),
            (i + 10, 1, w_plus(i)),
        ):
            p, q = pair
            d_out[1][column].append((5 * head + q, p, 1))
            d_out[1][column].append((5 * head + p, q, -1))
    for b in range(2):
        for k in range(5):
            d_out[2][b * 5 + k].append((b, k, 1))
    incoming: list[list[list[tuple[int, int, int]]]] = []
    for level in range(3):
        rows = [[] for _ in range(RANKS[level + 1])]
        for column, terms in enumerate(d_out[level]):
            for row, variable, coefficient in terms:
                rows[row].append((column, variable, coefficient))
        incoming.append(rows)
    squares = line_squares_to_zero(d_out)
    return d_out, incoming, nonzero, squares


def line_squares_to_zero(d_out) -> bool:
    """The two consecutive compositions are zero as commutative polynomial matrices."""
    for level in range(2):
        for column in range(RANKS[level]):
            accumulator: dict[tuple[int, int, int], int] = {}
            for mid, k, z in d_out[level][column]:
                for row, j, w in d_out[level + 1][mid]:
                    key = (row, min(k, j), max(k, j))
                    accumulator[key] = accumulator.get(key, 0) + z * w
                    if accumulator[key] == 0:
                        del accumulator[key]
            if accumulator:
                return False
    return True


# ---------------------------------------------------------------------------
# Cech combinatorics on the standard 5-vertex simplex.
# ---------------------------------------------------------------------------

VERTS = [tuple(i for i in range(5) if (mask >> i) & 1) for mask in range(32)]
DELTA_MOVES = []
H_MOVES = []
for _mask in range(32):
    _verts = VERTS[_mask]
    _moves = []
    for _j in range(5):
        if (_mask >> _j) & 1:
            continue
        _pos = sum(1 for v in _verts if v < _j)
        _moves.append((-1 if _pos % 2 else 1, _mask | (1 << _j)))
    DELTA_MOVES.append(tuple(_moves))
    _hrow = []
    for _v in range(5):
        if ((_mask >> _v) & 1) == 0:
            _hrow.append(None)
        else:
            _pos = _verts.index(_v)
            _hrow.append((-1 if _pos % 2 else 1, _mask ^ (1 << _v)))
    H_MOVES.append(tuple(_hrow))


def contraction_vertex(mono: tuple[int, ...], policy: str) -> int | None:
    if policy == "min":
        for i, exponent in enumerate(mono):
            if exponent >= 0:
                return i
    elif policy == "max":
        for i in range(4, -1, -1):
            if mono[i] >= 0:
                return i
    else:
        raise ValueError(policy)
    return None


def section_ok(mask: int, mono: tuple[int, ...]) -> bool:
    return all(exponent >= 0 for j, exponent in enumerate(mono) if ((mask >> j) & 1) == 0)


def cochain_add(target: dict, key, value) -> None:
    if is_zero(value):
        return
    old = target.get(key)
    if old is None:
        target[key] = value
        return
    summed = add_num(old, value)
    if is_zero(summed):
        del target[key]
    else:
        target[key] = summed


def apply_delta(cochain: dict) -> dict:
    out: dict = {}
    for (u, a, b, mask, mono), coefficient in cochain.items():
        for sign, new_mask in DELTA_MOVES[mask]:
            cochain_add(out, (u, a, b, new_mask, mono), scale_num(coefficient, sign))
    return out


def apply_h(cochain: dict, policy: str, global_sign: int = 1, flip_vertex: int | None = None) -> dict:
    """Cone contraction. global_sign multiplies every output.

    If flip_vertex is not None, strands whose chosen contraction vertex equals
    flip_vertex receive the opposite sign. That is the non-uniform negative control.
    """
    out: dict = {}
    for (u, a, b, mask, mono), coefficient in cochain.items():
        vertex = contraction_vertex(mono, policy)
        if vertex is None:
            continue
        move = H_MOVES[mask][vertex]
        if move is None:
            continue
        sign, new_mask = move
        if new_mask == 0:
            # Degree 0 has no cone into the empty simplex. Callers never need it.
            continue
        sign *= global_sign
        if flip_vertex is not None and vertex == flip_vertex:
            sign = -sign
        cochain_add(out, (u, a, b, new_mask, mono), scale_num(coefficient, sign))
    return out


def apply_d(cochain: dict, internal_degree: int, d_out, incoming, pre_sign_override: int | None = None) -> dict:
    """Hom differential from internal degree r to r+1, on Cech cochains.

    pre_sign_override replaces the pinned precomposition sign -(-1)^r, used only
    by the negative control that breaks d_Hom^2 = 0.
    """
    pre_sign = -1 if internal_degree % 2 == 0 else 1
    if pre_sign_override is not None:
        pre_sign = pre_sign_override
    out: dict = {}
    for (u, a, b, mask, mono), coefficient in cochain.items():
        v = u + internal_degree
        if v < 3:
            for row, variable, z in d_out[v][a]:
                mono2 = list(mono)
                mono2[variable] += 1
                cochain_add(out, (u, row, b, mask, tuple(mono2)), scale_num(coefficient, z))
        if u > 0:
            for column, variable, z in incoming[u - 1][b]:
                mono2 = list(mono)
                mono2[variable] += 1
                cochain_add(
                    out,
                    (u - 1, a, column, mask, tuple(mono2)),
                    scale_num(coefficient, z * pre_sign),
                )
    return out


def scale_cochain(cochain: dict, sign: int) -> dict:
    if sign == 1:
        return cochain
    return {key: scale_num(value, sign) for key, value in cochain.items()}


def cochain_equal(left: dict, right: dict) -> bool:
    if len(left) != len(right):
        return False
    for key, value in left.items():
        if right.get(key) != value:
            return False
    return True


def max_abs_cochain(cochain: dict) -> int:
    return max((coeff_max(value) for value in cochain.values()), default=0)


def support_ok(cochain: dict) -> bool:
    return all(section_ok(mask, mono) for (_, _, _, mask, mono) in cochain)


# ---------------------------------------------------------------------------
# Bases at r = 2 (80 constants) and r = 3 (50 linear forms).
# ---------------------------------------------------------------------------

def decode80(column: int) -> tuple[int, int, int]:
    if column < 50:
        a, b = divmod(column, 5)
        return 0, a, b
    a, b = divmod(column - 50, 15)
    return 1, a, b


def index80(u: int, a: int, b: int) -> int:
    if u == 0:
        return a * 5 + b
    if u == 1:
        return 50 + a * 15 + b
    raise ValueError((u, a, b))


def index50(a: int, b: int, mono: tuple[int, ...]) -> int:
    return (a * 5 + b) * 5 + DEGREE_ONE_INDEX[mono]


def initial_source(width: int = 10) -> dict:
    """Ten Cech degree-4 classes [1/(x0 x1 x2 x3 x4)] on Hom(C^3, C^0).

    Column a*2+b is the class with target index a in C^0 (a = 0..4) and source
    index b in C^3 (b = 0..1).
    """
    cochain = {}
    for a in range(5):
        for b in range(2):
            column = a * 2 + b
            if width == 1:
                value = 1
            else:
                value = tuple(1 if i == column else 0 for i in range(width))
            cochain[(3, a, b, 31, FULL_POLE)] = value
    return cochain


def zigzag(
    d_out,
    incoming,
    policy: str = "min",
    uniform_sign_flip_stage: int | None = None,
    vertex_sign_flip: tuple[int, int] | None = None,
    pre_sign_at_first: int | None = None,
    verify_steps: bool = False,
):
    """Five Hom differentials and four Cech homotopies.

    uniform_sign_flip_stage: negate the Tot multiplier of h at that stage only.
    vertex_sign_flip: (stage, vertex). At that stage, strands contracted at the
    given vertex receive the opposite Tot sign.
    pre_sign_at_first: replace the precomposition sign of the first Hom differential.
    verify_steps: on the unmodified zigzag, require delta(w) = 0 and
    delta(h(w)) = w before each homotopy.
    """
    y = initial_source(10)
    stages = []
    p = 4
    internal = -3
    used_for_square = []
    for stage_index in range(4):
        pre = pre_sign_at_first if stage_index == 0 else None
        w = apply_d(y, internal, d_out, incoming, pre_sign_override=pre)
        # Correct Tot multiplier of h is (-1)^{p+1} = -(-1)^p.
        multiplier = -1 if p % 2 == 0 else 1
        if uniform_sign_flip_stage == stage_index:
            multiplier = -multiplier
        vertex_flip = None
        if vertex_sign_flip is not None and vertex_sign_flip[0] == stage_index:
            vertex_flip = vertex_sign_flip[1]
        unmodified = (
            uniform_sign_flip_stage is None
            and vertex_sign_flip is None
            and pre_sign_at_first is None
        )
        if verify_steps and unmodified:
            if apply_delta(w):
                raise RuntimeError(f"Hom image at r={internal} is not a Cech cocycle")
        z = apply_h(w, policy, global_sign=multiplier, flip_vertex=vertex_flip)
        if verify_steps and unmodified:
            # z = multiplier * h(w) and delta(w) = 0, so delta(z) = multiplier * w.
            if not cochain_equal(apply_delta(z), scale_cochain(w, multiplier)):
                raise RuntimeError(f"cone contraction does not solve delta at r={internal}")
        stages.append(
            {
                "from_r": internal,
                "cech_degree": p,
                "h_multiplier": multiplier,
                "uniform_sign_flipped": uniform_sign_flip_stage == stage_index,
                "flip_vertex": vertex_flip,
                "input_terms": len(y),
                "after_d_terms": len(w),
                "after_h_terms": len(z),
                "max_abs_after_d": max_abs_cochain(w),
                "max_abs_after_h": max_abs_cochain(z),
            }
        )
        used_for_square.append((internal, y, w))
        y = z
        p -= 1
        internal += 1
    output = apply_d(y, internal, d_out, incoming)
    stages.append(
        {
            "from_r": internal,
            "cech_degree": p,
            "final_d_multiplier": 1,
            "input_terms": len(y),
            "output_terms": len(output),
            "max_abs_output": max_abs_cochain(output),
        }
    )
    used_for_square.append((internal, y, output))
    return output, stages, used_for_square


def read_constant_matrix(cochain: dict) -> tuple[list[list[int]], dict]:
    """Read an 80 x 10 matrix of global constant sections, with a diagnostic."""
    # component -> monomial -> mask -> coefficient tuple
    grouped: dict[tuple[int, int, int], dict] = {}
    for (u, a, b, mask, mono), coefficient in cochain.items():
        grouped.setdefault((u, a, b), {}).setdefault(mono, {})[mask] = coefficient
    matrix = [[0] * 10 for _ in range(80)]
    problems = []
    vertex_masks = [1 << i for i in range(5)]
    seen = set()
    for (u, a, b), monos in grouped.items():
        try:
            row = index80(u, a, b)
        except ValueError:
            problems.append({"bad_component": [u, a, b]})
            continue
        seen.add(row)
        if set(monos) != {ZERO_MONO}:
            problems.append({"row": row, "monomials": [list(m) for m in monos]})
            continue
        by_mask = monos[ZERO_MONO]
        if set(by_mask) != set(vertex_masks):
            problems.append({"row": row, "masks": sorted(by_mask)})
            continue
        first = by_mask[vertex_masks[0]]
        if any(by_mask[mask] != first for mask in vertex_masks[1:]):
            problems.append({"row": row, "unequal_vertices": True})
            continue
        matrix[row] = list(first)
    return matrix, {"problems": problems, "nonzero_rows": sum(any(row) for row in matrix), "components": len(seen)}


# ---------------------------------------------------------------------------
# Global-section map H^0(O)^80 -> H^0(O(1))^10. The target is 50-dimensional.
# Re-derived independently of the Cech zigzag (polynomial representative of
# the same Hom differential).
# ---------------------------------------------------------------------------

def polynomial_block(d_out, incoming) -> list[list[int]]:
    matrix = [[0] * 80 for _ in range(50)]
    internal = 2
    pre_sign = -1 if internal % 2 == 0 else 1
    for column in range(80):
        u, a, b = decode80(column)
        v = u + internal
        accumulator: dict[tuple[int, int, int, tuple[int, ...]], int] = {}

        def add_term(key, value):
            accumulator[key] = accumulator.get(key, 0) + value
            if accumulator[key] == 0:
                del accumulator[key]

        if v < 3:
            for row, variable, z in d_out[v][a]:
                mono = [0, 0, 0, 0, 0]
                mono[variable] = 1
                add_term((u, row, b, tuple(mono)), z)
        if u > 0:
            for source, variable, z in incoming[u - 1][b]:
                mono = [0, 0, 0, 0, 0]
                mono[variable] = 1
                add_term((u - 1, a, source, tuple(mono)), z * pre_sign)
        for (uu, aa, bb, mono), coefficient in accumulator.items():
            if uu != 0:
                raise RuntimeError("r=3 term is not Hom(C^0, C^3)")
            matrix[index50(aa, bb, mono)][column] += coefficient
    return matrix


def cech_global_block(d_out, incoming) -> list[list[int]]:
    """Same map, computed by applying d_Hom to Cech representatives of constants."""
    cochain = {}
    for column in range(80):
        u, a, b = decode80(column)
        value = tuple(1 if i == column else 0 for i in range(80))
        for vertex in range(5):
            cochain[(u, a, b, 1 << vertex, ZERO_MONO)] = value
    image = apply_d(cochain, 2, d_out, incoming)
    if not cochain_equal(apply_delta(image), {}):
        raise RuntimeError("Cech image of global constants is not a cocycle")
    matrix = [[0] * 80 for _ in range(50)]
    vertex_masks = [1 << i for i in range(5)]
    grouped: dict[tuple, dict] = {}
    for (u, a, b, mask, mono), coefficient in image.items():
        grouped.setdefault((u, a, b, mono), {})[mask] = coefficient
    for (u, a, b, mono), by_mask in grouped.items():
        if set(by_mask) != set(vertex_masks):
            raise RuntimeError("global linear form is missing a vertex")
        first = by_mask[vertex_masks[0]]
        if any(by_mask[mask] != first for mask in vertex_masks[1:]):
            raise RuntimeError("global linear form depends on the vertex")
        for column, coefficient in enumerate(first):
            if coefficient:
                matrix[index50(a, b, mono)][column] += coefficient
    return matrix


# ---------------------------------------------------------------------------
# Exact linear algebra.
# ---------------------------------------------------------------------------

def unit_pivot_kernel(matrix: list[list[int]]):
    """Row-echelon kernel basis using only ±1 pivots, scanning columns left to right.

    Returns a record. If a non-unit pivot is required, unit_pivots is false and
    kernel is None; rank over Q is still computed with exact rationals.
    """
    m = len(matrix)
    n = len(matrix[0])
    rows = [dict((j, value) for j, value in enumerate(row) if value) for row in matrix]
    rank = 0
    pivots = []
    max_intermediate = 1
    for column in range(n):
        pivot_row = rank
        while pivot_row < m and abs(rows[pivot_row].get(column, 0)) != 1:
            pivot_row += 1
        if pivot_row == m:
            if any(rows[i].get(column, 0) for i in range(rank, m)):
                rational_rank = rank_over_q(matrix)
                return {
                    "unit_pivots": False,
                    "rank": rational_rank,
                    "pivots": pivots,
                    "kernel": None,
                    "max_intermediate": max_intermediate,
                }
            continue
        rows[rank], rows[pivot_row] = rows[pivot_row], rows[rank]
        if rows[rank].get(column) == -1:
            rows[rank] = {j: -value for j, value in rows[rank].items()}
        pivot = rows[rank]
        for i in range(rank + 1, m):
            factor = rows[i].get(column, 0)
            if not factor:
                continue
            target = rows[i]
            for j, value in pivot.items():
                updated = target.get(j, 0) - factor * value
                if updated:
                    target[j] = updated
                    max_intermediate = max(max_intermediate, abs(updated))
                elif j in target:
                    del target[j]
        pivots.append(column)
        rank += 1
    if any(rows[i] for i in range(rank, m)):
        raise RuntimeError("nonzero residual after unit-pivot elimination")
    pivot_set = set(pivots)
    free = [column for column in range(n) if column not in pivot_set]
    kernel = []
    for free_column in free:
        vector = [0] * n
        vector[free_column] = 1
        for i in range(rank - 1, -1, -1):
            accumulator = 0
            pivot_column = pivots[i]
            for j, value in rows[i].items():
                if j != pivot_column:
                    accumulator += value * vector[j]
            vector[pivot_column] = -accumulator
        for original in matrix:
            if sum(entry * vector[j] for j, entry in enumerate(original)):
                raise RuntimeError("kernel vector is not annihilated")
        kernel.append(vector)
    return {
        "unit_pivots": True,
        "rank": rank,
        "pivots": pivots,
        "pivot_values": [1] * rank,
        "free_columns": free,
        "kernel": kernel,
        "max_intermediate": max_intermediate,
    }


def rank_over_q(matrix: list[list[int]]) -> int:
    from fractions import Fraction

    rows = [[Fraction(entry) for entry in row] for row in matrix]
    if not rows:
        return 0
    m = len(rows)
    n = len(rows[0])
    rank = 0
    for column in range(n):
        pivot = None
        for i in range(rank, m):
            if rows[i][column] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][column]
        for i in range(m):
            if i == rank or rows[i][column] == 0:
                continue
            factor = rows[i][column] / scale
            for j in range(column, n):
                rows[i][j] -= factor * rows[rank][j]
        rank += 1
    return rank


def rank_mod(matrix: list[list[int]], modulus: int) -> int:
    rows = [[entry % modulus for entry in row] for row in matrix]
    if not rows:
        return 0
    m = len(rows)
    n = len(rows[0])
    rank = 0
    for column in range(n):
        pivot = None
        for i in range(rank, m):
            if rows[i][column] % modulus:
                pivot = i
                break
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][column], -1, modulus)
        for i in range(m):
            if i == rank or rows[i][column] % modulus == 0:
                continue
            factor = (rows[i][column] * inv) % modulus
            for j in range(column, n):
                rows[i][j] = (rows[i][j] - factor * rows[rank][j]) % modulus
        rank += 1
    return rank


def mat_vec(matrix, vector):
    return [sum(entry * vector[j] for j, entry in enumerate(row)) for row in matrix]


def mat_mul(left, right):
    """left is a x b (list of rows), right is b x c (list of rows)."""
    b = len(right)
    c = len(right[0]) if right else 0
    columns = [[right[i][j] for i in range(b)] for j in range(c)]
    return [[sum(entry * column[k] for k, entry in enumerate(row)) for column in columns] for row in left]


def transpose(matrix):
    if not matrix:
        return []
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]


def smith_invariant_factors(matrix: list[list[int]]) -> list[int]:
    """Positive invariant factors d1 | d2 | ... of a rectangular integer matrix."""
    A = [list(row) for row in matrix]
    m = len(A)
    n = len(A[0]) if m else 0

    def row_swap(i, j):
        A[i], A[j] = A[j], A[i]

    def col_swap(i, j):
        for r in range(m):
            A[r][i], A[r][j] = A[r][j], A[r][i]

    def row_neg(i):
        A[i] = [-value for value in A[i]]

    def row_add(i, j, q):
        for k in range(n):
            A[i][k] += q * A[j][k]

    def col_add(i, j, q):
        for r in range(m):
            A[r][i] += q * A[r][j]

    factors = []
    t = 0
    guard = 0
    while t < m and t < n:
        guard += 1
        if guard > 10000:
            raise RuntimeError("Smith form did not terminate")
        best = None
        bi = bj = None
        for i in range(t, m):
            for j in range(t, n):
                if A[i][j] and (best is None or abs(A[i][j]) < best):
                    best = abs(A[i][j])
                    bi, bj = i, j
        if best is None:
            break
        row_swap(t, bi)
        col_swap(t, bj)
        if A[t][t] < 0:
            row_neg(t)
        for i in range(t + 1, m):
            if A[i][t] == 0:
                continue
            a, b = A[t][t], A[i][t]
            g, s, tt = egcd(a, b)
            row_t = A[t][:]
            row_i = A[i][:]
            A[t] = [s * x + tt * y for x, y in zip(row_t, row_i)]
            A[i] = [-(b // g) * x + (a // g) * y for x, y in zip(row_t, row_i)]
        for j in range(t + 1, n):
            if A[t][j] == 0:
                continue
            a, b = A[t][t], A[t][j]
            g, s, tt = egcd(a, b)
            col_t = [A[r][t] for r in range(m)]
            col_j = [A[r][j] for r in range(m)]
            for r in range(m):
                A[r][t] = s * col_t[r] + tt * col_j[r]
                A[r][j] = -(b // g) * col_t[r] + (a // g) * col_j[r]
        pivot = A[t][t]
        if pivot < 0:
            row_neg(t)
            pivot = A[t][t]
        bad = None
        for i in range(t, m):
            for j in range(t, n):
                if (i > t or j > t) and A[i][j] % pivot:
                    bad = (i, j)
                    break
            if bad:
                break
        if bad is not None:
            i, j = bad
            if i != t:
                row_add(t, i, 1)
            else:
                col_add(t, j, 1)
            continue
        if any(A[i][t] for i in range(t + 1, m)) or any(A[t][j] for j in range(t + 1, n)):
            continue
        factors.append(pivot)
        t += 1
    for i in range(1, len(factors)):
        if factors[i] % factors[i - 1]:
            raise RuntimeError(f"invariant factors not ordered: {factors}")
    return factors


def prime_power_divisors(factors: list[int]) -> list[int]:
    """Elementary divisors as prime powers, omitting units."""
    divisors = []
    for value in factors:
        n = value
        p = 2
        while p * p <= n:
            power = 1
            while n % p == 0:
                power *= p
                n //= p
            if power > 1:
                divisors.append(power)
            p += 1 if p == 2 else 2
        if n > 1:
            divisors.append(n)
    return divisors


# ---------------------------------------------------------------------------
# Checks.
# ---------------------------------------------------------------------------

def check_used_terms(used, d_out, incoming) -> dict:
    """Check every distinct y key and every distinct w key of one zigzag.

    A key of y is tested at the internal degree of that stage. A key of
    w = d_Hom(y) is tested one degree higher. On each term the checks are
    delta^2 = 0, d_Hom^2 = 0, delta d_Hom = d_Hom delta, and section support.
    On each contractible term of Cech degree at least 1, both cone identities
    are delta h + h delta = id, for the least-vertex homotopy and for the
    greatest-vertex homotopy.
    """
    delta_square_failures = 0
    d_square_failures = 0
    commute_failures = 0
    homotopy_failures = 0
    support_failures = 0
    strands_without_contraction = 0
    contractible_positive = 0
    witness = None
    seen_pairs: set[tuple] = set()
    distinct_keys: set = set()
    for internal, y, w in used:
        for degree, cochain in ((internal, y), (internal + 1, w)):
            for key in cochain:
                pair = (degree, key)
                if pair in seen_pairs:
                    continue
                seen_pairs.add(pair)
                distinct_keys.add(key)
                _u, _a, _b, mask, mono = key
                if not section_ok(mask, mono):
                    support_failures += 1
                    if witness is None:
                        witness = {
                            "where": "section_support",
                            "internal": degree,
                            "key": serialize_key(key),
                        }
                term = {key: 1}
                d_term = apply_d(term, degree, d_out, incoming)
                delta_term = apply_delta(term)
                if not cochain_equal(apply_delta(d_term), apply_d(delta_term, degree, d_out, incoming)):
                    commute_failures += 1
                    if witness is None:
                        witness = {
                            "where": "commutation",
                            "internal": degree,
                            "key": serialize_key(key),
                        }
                if apply_d(d_term, degree + 1, d_out, incoming):
                    d_square_failures += 1
                    if witness is None:
                        witness = {
                            "where": "d_hom_square",
                            "internal": degree,
                            "key": serialize_key(key),
                        }
                if apply_delta(delta_term):
                    delta_square_failures += 1
                    if witness is None:
                        witness = {
                            "where": "delta_square",
                            "internal": degree,
                            "key": serialize_key(key),
                        }
                # The cone identity needs a vertex of nonnegative exponent. The ten
                # source strands are x0^{-1}...x4^{-1} on the full simplex: they are
                # the H^4 generators, delta vanishes, and no contraction exists.
                if contraction_vertex(mono, "min") is None:
                    strands_without_contraction += 1
                    if mono != FULL_POLE or mask != 31 or delta_term:
                        homotopy_failures += 1
                        if witness is None:
                            witness = {
                                "where": "unexpected_noncontractible_strand",
                                "internal": degree,
                                "key": serialize_key(key),
                            }
                    continue
                if mask.bit_count() >= 2:
                    contractible_positive += 1
                    for policy in ("min", "max"):
                        h_term = apply_h(term, policy)
                        recovered = apply_delta(h_term)
                        for key2, value2 in apply_h(delta_term, policy).items():
                            cochain_add(recovered, key2, value2)
                        if not cochain_equal(recovered, term):
                            homotopy_failures += 1
                            if witness is None:
                                witness = {
                                    "where": "homotopy",
                                    "policy": policy,
                                    "internal": degree,
                                    "key": serialize_key(key),
                                }
    return {
        "distinct_terms": len(distinct_keys),
        "distinct_degree_key_pairs": len(seen_pairs),
        "contractible_cech_degree_at_least_1": contractible_positive,
        "strands_without_contraction": strands_without_contraction,
        "section_support_failures": support_failures,
        "delta_square_failures": delta_square_failures,
        "d_hom_square_failures": d_square_failures,
        "commutation_failures": commute_failures,
        "homotopy_identity_failures": homotopy_failures,
        "D_squared_zero": (
            delta_square_failures == 0 and d_square_failures == 0 and commute_failures == 0
        ),
        "section_support": support_failures == 0,
        "cone_identities": homotopy_failures == 0,
        "witness": witness,
    }


def serialize_key(key) -> dict:
    u, a, b, mask, mono = key
    return {
        "u": u,
        "a": a,
        "b": b,
        "simplex": list(VERTS[mask]),
        "monomial": list(mono),
    }


def negative_control_tot(d_out, incoming, sample_key, internal: int) -> dict:
    """Flip the Tot sign between Cech degrees p and p+1 and evaluate D^2 on one used term.

    Correct convention: D = delta + (-1)^p d_Hom, and the cross terms cancel.
    Flipped convention: the sign in front of d_Hom is reversed at Cech degree p
    only. On a term of degree p the cross term becomes twice the commutation
    composite whenever that composite is nonzero.
    """
    u, a, b, mask, mono = sample_key
    p = mask.bit_count() - 1
    term = {sample_key: 1}
    d_term = apply_d(term, internal, d_out, incoming)
    delta_term = apply_delta(term)
    cross = apply_delta(d_term)
    # D^2 coefficient of the cross term for sigma(p)=+1, sigma(p+1)=-1,
    # from the expansion in the note: (-1)^p (sigma(p) - sigma(p+1)) delta d.
    # sigma(p)-sigma(p+1) = 2, so D^2 contributes (-1)^p * 2 * cross.
    sign = -1 if p % 2 else 1
    flipped = scale_cochain(cross, 2 * sign)
    consistent = {}  # sigma constant => cross coefficient 0
    return {
        "convention_correct": "D = delta + (-1)^p d_Hom",
        "convention_flipped": "sign of d_Hom reversed at one Cech degree only",
        "term": serialize_key(sample_key),
        "internal_degree": internal,
        "cech_degree": p,
        "consistent_D_squared_is_zero": True,
        "flipped_cross_term_max_abs": max_abs_cochain(flipped),
        "flipped_cross_term_nonzero": bool(flipped),
        "commutation_matches": cochain_equal(cross, apply_d(delta_term, internal, d_out, incoming)),
        "note": (
            "A uniform sign on a whole stage of this linear zigzag only multiplies "
            "the final 80-vector by -1, which stays in the kernel. The detecting "
            "failure is D^2 != 0 on a used basis term."
        ),
    }


def self_tests() -> None:
    g, s, t = egcd(6, 15)
    assert (g, s * 6 + t * 15) == (3, 3)
    g, s, t = egcd(-4, 6)
    assert g == 2 and s * -4 + t * 6 == 2
    assert smith_invariant_factors([[2, 0], [0, 4]]) == [2, 4]
    assert smith_invariant_factors([[4, 0], [0, 2]]) == [2, 4]
    assert smith_invariant_factors([[2, 0], [0, 3]]) == [1, 6]
    assert smith_invariant_factors([[2, 0, 0], [0, 3, 0], [0, 0, 6]]) == [1, 6, 6]
    assert smith_invariant_factors([[1, 2], [3, 4]]) == [1, 2]
    assert smith_invariant_factors([[0, 0], [0, 0]]) == []
    assert rank_over_q([[1, 2, 3], [2, 4, 6], [1, 1, 1]]) == 2
    assert rank_mod([[1, 2, 3], [2, 4, 6], [1, 1, 1]], 3) == 2
    # Unit-pivot kernel of a rank-2 map Z^3 -> Z^2.
    record = unit_pivot_kernel([[1, 2, 3], [0, 1, 1]])
    assert record["unit_pivots"] and record["rank"] == 2
    assert record["kernel"] == [[-1, -1, 1]]
    # Cone identity on the O(-4) strand x0^0 x1^{-1}...x4^{-1}.
    # The full simplex is a coboundary via contraction at vertex 0.
    mono = (0, -1, -1, -1, -1)
    term = {(0, 0, 0, 31, mono): 1}
    h_term = apply_h(term, "min")
    assert h_term == {(0, 0, 0, 30, mono): 1}  # mask 31 without bit 0 is 30
    assert apply_delta(h_term) == term
    # delta^2 vanishes on a 0-cochain.
    vertex = {(1, 2, 3, 1 << 0, (1, -1, 0, 0, 0)): 1}
    assert apply_delta(apply_delta(vertex)) == {}


def matrices_equal(left, right) -> bool:
    return left == right


def max_abs_matrix(matrix) -> int:
    return max((abs(entry) for row in matrix for entry in row), default=0)


def columns_in_kernel(block, image) -> list[int]:
    """Return the list of nonzero residual columns; empty means every column is in the kernel."""
    bad = []
    width = len(image[0])
    for column in range(width):
        vector = [image[row][column] for row in range(len(image))]
        if any(mat_vec(block, vector)):
            bad.append(column)
    return bad


def difference_max(left, right) -> int:
    return max(abs(a - b) for row_l, row_r in zip(left, right) for a, b in zip(row_l, row_r))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def find_source() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        candidate = parent / SOURCE_RELATIVE
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(SOURCE_RELATIVE)


def main() -> None:
    self_tests()
    source = find_source()
    blob = git_blob_sha1(source)
    digest = sha256_file(source)
    if blob != PINNED_BLOB:
        raise SystemExit("pinned source blob mismatch")
    d_out, incoming, gamma_nonzeros, line_ok = build_line_differentials()
    if not line_ok:
        raise SystemExit("line differentials do not square to zero")
    eprint("line complex ok; building the 50 x 80 block")
    block = polynomial_block(d_out, incoming)
    cech_block = cech_global_block(d_out, incoming)
    if block != cech_block:
        raise SystemExit("polynomial and Cech constructions of the 80->50 map differ")
    elimination = unit_pivot_kernel(block)
    if not elimination["unit_pivots"] or elimination["kernel"] is None:
        raise SystemExit("80->50 map did not admit a unit-pivot kernel basis")
    kernel_columns = elimination["kernel"]  # list of 30 vectors of length 80
    # Matrix whose columns are the kernel basis. Free rows form the identity,
    # in the order of free_columns, so the basis is Z-saturated.
    free = elimination["free_columns"]
    for index, vector in enumerate(kernel_columns):
        for j, column in enumerate(free):
            expected = 1 if j == index else 0
            if vector[column] != expected:
                raise SystemExit("kernel basis is not the identity on free columns")
    eprint(f"80->50 rank {elimination['rank']}, free {len(free)}")
    eprint("running the Cech zigzag, minimal contraction vertex")
    output_min, stages_min, used = zigzag(d_out, incoming, policy="min", verify_steps=True)
    image_min, read_min = read_constant_matrix(output_min)
    square_min = check_used_terms(used, d_out, incoming)
    eprint(
        "least-vertex terms "
        f"{square_min['distinct_terms']} failures d2={square_min['d_hom_square_failures']} "
        f"delta2={square_min['delta_square_failures']} commute={square_min['commutation_failures']} "
        f"support={square_min['section_support_failures']} "
        f"homotopy={square_min['homotopy_identity_failures']}"
    )
    eprint("running the Cech zigzag, maximal contraction vertex")
    output_max, stages_max, used_max = zigzag(d_out, incoming, policy="max")
    square_max = check_used_terms(used_max, d_out, incoming)
    eprint(
        "greatest-vertex terms "
        f"{square_max['distinct_terms']} failures d2={square_max['d_hom_square_failures']} "
        f"delta2={square_max['delta_square_failures']} commute={square_max['commutation_failures']} "
        f"support={square_max['section_support_failures']} "
        f"homotopy={square_max['homotopy_identity_failures']}"
    )
    image_max, read_max = read_constant_matrix(output_max)
    image_difference = difference_max(image_min, image_max) if read_min["problems"] == [] and read_max["problems"] == [] else None
    # Cocycle check is the successful read plus an explicit delta computation.
    delta_output = apply_delta(output_min)
    is_cocycle = delta_output == {} and read_min["problems"] == []
    bad_columns = columns_in_kernel(block, image_min) if is_cocycle else list(range(10))
    # Coordinates in the kernel basis: the free-variable rows.
    if is_cocycle and not bad_columns:
        coordinates = [[image_min[column][j] for j in range(10)] for column in free]
        reconstructed = mat_mul(transpose(kernel_columns), coordinates)
        reconstruction_ok = reconstructed == image_min
    else:
        coordinates = []
        reconstruction_ok = False
    factors = smith_invariant_factors(coordinates) if coordinates else []
    rank_q_30 = rank_over_q(coordinates) if coordinates else None
    rank_f3_30 = rank_mod(coordinates, 3) if coordinates else None
    rank_q_80 = rank_over_q(image_min) if is_cocycle else None
    rank_f3_80 = rank_mod(image_min, 3) if is_cocycle else None
    # Negative controls.
    sample = None
    sample_internal = None
    for internal, y, _w in used:
        for key in y:
            if key[3].bit_count() >= 2:
                term = {key: 1}
                if apply_delta(apply_d(term, internal, d_out, incoming)):
                    sample = key
                    sample_internal = internal
                    break
        if sample is not None:
            break
    if sample is None:
        neg_tot = {"available": False}
    else:
        neg_tot = negative_control_tot(d_out, incoming, sample, sample_internal)
        neg_tot["available"] = True
    eprint("running Tot-sign negative controls")
    sign_controls = []
    for stage_index in range(4):
        output_uniform, _, _ = zigzag(
            d_out, incoming, policy="min", uniform_sign_flip_stage=stage_index
        )
        image_uniform, read_uniform = read_constant_matrix(output_uniform)
        uniform_record = {
            "kind": "uniform_multiplier_flip",
            "stage": stage_index,
            "is_global_section": read_uniform["problems"] == [] and apply_delta(output_uniform) == {},
        }
        if uniform_record["is_global_section"]:
            negated = all(
                image_uniform[i][j] == -image_min[i][j] for i in range(80) for j in range(10)
            )
            uniform_record["is_negative_of_correct_image"] = negated
            uniform_record["columns_outside_kernel"] = columns_in_kernel(block, image_uniform)
            uniform_record["image_leaves_kernel"] = bool(uniform_record["columns_outside_kernel"])
        sign_controls.append(uniform_record)
        output_vertex, _, _ = zigzag(
            d_out, incoming, policy="min", vertex_sign_flip=(stage_index, 0)
        )
        image_vertex, read_vertex = read_constant_matrix(output_vertex)
        delta_vertex = apply_delta(output_vertex)
        vertex_record = {
            "kind": "vertex_0_multiplier_flip",
            "stage": stage_index,
            "is_global_section": read_vertex["problems"] == [] and delta_vertex == {},
            "delta_nonzero_terms": len(delta_vertex),
        }
        if vertex_record["is_global_section"]:
            vertex_record["max_abs_difference_from_correct_image"] = difference_max(image_min, image_vertex)
            vertex_record["columns_outside_kernel"] = columns_in_kernel(block, image_vertex)
            vertex_record["image_leaves_kernel"] = bool(vertex_record["columns_outside_kernel"])
        else:
            vertex_record["image_leaves_kernel"] = True
            vertex_record["reason"] = "output is not a Cech 0-cocycle, so it is not in H^0 and not in ker"
        sign_controls.append(vertex_record)
    rank_d5 = rank_q_30
    rank_f3_block = rank_mod(block, 3)
    rank_q_block = rank_over_q(block)
    uniform_runs = [run for run in sign_controls if run["kind"] == "uniform_multiplier_flip"]
    last_vertex_flip = next(
        run
        for run in sign_controls
        if run["kind"] == "vertex_0_multiplier_flip" and run["stage"] == 3
    )
    saturated_kernel = all(
        vector[column] == (1 if j == index else 0)
        for index, vector in enumerate(kernel_columns)
        for j, column in enumerate(free)
    )
    # Exit 0 is the regression contract. These are the main-path results.
    assert rank_q_block == 50, "80->50 rank over Q"
    assert elimination["rank"] == 50, "80->50 unit-pivot rank over Q"
    assert rank_f3_block == 50, "80->50 rank over F3"
    assert elimination["unit_pivots"], "80->50 unit pivots"
    assert elimination["pivot_values"] == [1] * 50, "80->50 pivot values"
    assert len(kernel_columns) == 30, "saturated kernel rank"
    assert saturated_kernel, "kernel basis is the identity on its free columns"
    assert is_cocycle, "80x10 image is a Cech cocycle"
    assert bad_columns == [], "every 80x10 column lies in K"
    assert rank_q_80 == 10, "80x10 image rank over Q"
    assert rank_f3_80 == 10, "80x10 image rank over F3"
    assert reconstruction_ok, "30x10 coordinates reconstruct the image"
    assert len(coordinates) == 30 and len(coordinates[0]) == 10, "30x10 coordinate shape"
    assert rank_q_30 == 10, "30x10 coordinate rank over Q"
    assert rank_f3_30 == 10, "30x10 coordinate rank over F3"
    assert factors == [1] * 10, "Smith factors"
    assert image_min == image_max, "least-vertex and greatest-vertex images agree entrywise"
    assert len(uniform_runs) == 4, "four uniform stage-sign flips"
    assert all(run.get("is_negative_of_correct_image") for run in uniform_runs), (
        "uniform stage-sign flip negates the image"
    )
    assert neg_tot.get("available"), "local Tot-sign witness"
    assert neg_tot["commutation_matches"], "local Tot-sign witness commutes"
    assert neg_tot["internal_degree"] == -2, "local Tot-sign witness degree"
    assert neg_tot["cech_degree"] == 3, "local Tot-sign witness Cech degree"
    assert neg_tot["flipped_cross_term_nonzero"], "local Tot-sign mutation gives D^2 != 0"
    assert neg_tot["flipped_cross_term_max_abs"] == 2, "local Tot-sign mutation gives D^2 != 0"
    assert last_vertex_flip["is_global_section"] is False, (
        "vertex-0 flip at the last homotopy is not a Cech cocycle"
    )
    assert last_vertex_flip["delta_nonzero_terms"] == 200, (
        "vertex-0 flip at the last homotopy is not a Cech cocycle"
    )
    assert last_vertex_flip["image_leaves_kernel"], (
        "vertex-0 flip at the last homotopy is not in K"
    )
    for policy_name, square in (("least", square_min), ("greatest", square_max)):
        assert square["distinct_terms"] == TERMS_CHECKED_PER_POLICY, policy_name
        assert square["distinct_degree_key_pairs"] == TERMS_CHECKED_PER_POLICY, policy_name
        assert square["D_squared_zero"], policy_name
        assert square["delta_square_failures"] == 0, policy_name
        assert square["d_hom_square_failures"] == 0, policy_name
        assert square["commutation_failures"] == 0, policy_name
        assert square["section_support"], policy_name
        assert square["section_support_failures"] == 0, policy_name
        assert square["cone_identities"], policy_name
        assert square["homotopy_identity_failures"] == 0, policy_name
        assert square["strands_without_contraction"] == 10, policy_name
    certificate = {
        "certificate": "P4-cech-d5-of-End-at-twist-minus-2",
        "pinned_source": {
            "path": SOURCE_RELATIVE,
            "git_blob_sha1": blob,
            "sha256": digest,
            "gamma_nonzeros": gamma_nonzeros,
            "line_differentials_square_to_zero": line_ok,
        },
        "conventions": {
            "cover": "U_i = {x_i != 0}, i = 0..4",
            "cech_differential": "(delta c)_J = sum_k (-1)^k c_{J without j_k}",
            "hom_differential": "f |-> d o f - (-1)^r f o d",
            "precomposition_sign": "-1 if r even, +1 if r odd",
            "total_differential": "D = delta + (-1)^p d_Hom",
            "contraction": "least index v with exponent >= 0; h(e_I)=(-1)^m e_{I without v}",
            "source_order": "column a*2+b, a = 0..4 in C^0, b = 0..1 in C^3",
            "target80_order": "u=0,a=0..9,b=0..4 then u=1,a=0..1,b=0..14, constant monomial",
            "target50_order": "a=0..1, b=0..4, degree-one monomials x4,x3,x2,x1,x0",
            "zigzag_h_multipliers": [-1, 1, -1, 1],
        },
        "shapes": {
            "source": [10],
            "map_80_to_50": [50, 80],
            "kernel_basis": [80, len(kernel_columns)],
            "image_80_by_10": [80, 10],
            "coordinates_30_by_10": [len(coordinates), 10 if coordinates else 0],
        },
        "map_80_to_50": {
            "rank_Q": elimination["rank"],
            "rank_F3": rank_f3_block,
            "unit_pivots": elimination["unit_pivots"],
            "pivot_columns": elimination["pivots"],
            "free_columns": free,
            "max_abs_entry": max_abs_matrix(block),
            "max_intermediate": elimination["max_intermediate"],
            "kernel_rank": len(kernel_columns),
            "kernel_saturated": saturated_kernel,
            "polynomial_matches_cech": True,
            "kernel_basis_columns": kernel_columns,
        },
        "zigzag": {
            "stages_min_vertex": stages_min,
            "image_is_cech_cocycle": is_cocycle,
            "read_diagnostics": read_min,
            "columns_outside_kernel": bad_columns,
            "coordinates_match_kernel_basis": reconstruction_ok,
            "image_80_by_10": image_min,
            "coordinates_30_by_10": coordinates,
        },
        "ranks": {
            "image_80_by_10_Q": rank_q_80,
            "image_80_by_10_F3": rank_f3_80,
            "coordinates_30_by_10_Q": rank_q_30,
            "coordinates_30_by_10_F3": rank_f3_30,
            "invariant_factors": factors,
            "elementary_divisors_prime_powers": prime_power_divisors(factors),
            "rank_d5_Q": rank_d5,
            "rank_d5_F3": rank_f3_30,
            "a2": None if rank_d5 is None else 10 - rank_d5,
            "h2": None if rank_d5 is None else 30 - rank_d5,
            "bookkeeping": (
                "Over Z, and hence over Q and F3, a2 = 10 - rank(d5) and h2 = 30 - rank(d5) "
                "are hypercohomology ranks of End(C)(-2) for the pinned perfect complex C. "
                "The E1 reduction uses only line-bundle cohomology on P^4, which is free over Z. "
                "Identifying a2 and h2 with End(H) groups requires the separate assertion that C "
                "resolves the intended HM bundle over the field concerned. This program does not "
                "certify that assertion, the D8 projector, choice independence, or any obstruction value."
            ),
        },
        "prediction": {
            "precommitted_rank_d5": 10,
            "matches_Q": rank_d5 == 10,
            "matches_F3": rank_f3_30 == 10,
        },
        "scope": {
            "computes": (
                "hypercohomology of End(C)(-2) for the pinned perfect complex C, "
                "over Z and hence over Q and F3"
            ),
            "e1_reduction": "line-bundle cohomology on P^4, free over Z",
            "does_not_certify": [
                "that C resolves the intended HM bundle",
                "identification of a2 and h2 with End(H) groups",
                "the D8 projector",
                "choice independence",
                "any obstruction value",
            ],
        },
        "checks": {
            "used_terms_per_policy": TERMS_CHECKED_PER_POLICY,
            "D_squared_zero_on_used_terms": {
                "least_vertex": square_min,
                "greatest_vertex": square_max,
            },
            "contraction_vertices": {
                "policies": ["least vertex", "greatest vertex"],
                "both_are_global_constants": read_min["problems"] == [] and read_max["problems"] == [],
                "matrices_identical": image_difference == 0,
                "max_abs_difference": image_difference,
            },
            "negative_control_tot_sign": neg_tot,
            "negative_control_stage_sign": {
                "description": (
                    "Uniform reversal of the Tot multiplier at one homotopy stage, "
                    "and reversal only on strands contracted at vertex 0."
                ),
                "runs": sign_controls,
                "uniform_flip_stays_in_kernel_as_global_minus": all(
                    run.get("is_negative_of_correct_image") and not run.get("image_leaves_kernel")
                    for run in sign_controls
                    if run["kind"] == "uniform_multiplier_flip"
                ),
                "last_stage_vertex_flip_leaves_kernel": next(
                    run["image_leaves_kernel"]
                    for run in sign_controls
                    if run["kind"] == "vertex_0_multiplier_flip" and run["stage"] == 3
                ),
            },
            "independent_80_to_50": {
                "description": (
                    "Re-derived from the exterior-sign, contraction and evaluation "
                    "formulas as a polynomial map on global sections, then repeated "
                    "on Cech representatives. Elimination is separate from the zigzag."
                ),
                "rank_Q": rank_q_block,
                "rank_F3": rank_f3_block,
                "unit_pivots": elimination["unit_pivots"],
                "kernel_dimension": len(kernel_columns),
            },
        },
        "oracle": {
            "macaulay2": "not available; no sheaf-cohomology oracle was run",
        },
    }
    json.dump(certificate, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
