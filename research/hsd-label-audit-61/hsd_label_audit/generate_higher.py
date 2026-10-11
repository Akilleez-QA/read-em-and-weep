#!/usr/bin/env python3
"""Blind H^2 bases and connecting maps for orders k=4,5,6.

The fixed bidegrees, frame weights, original plane cover and triangular
transport are the only inputs. Shipped label lists, stored maps, pivot sets
and expected dimensions are not read. Arithmetic is exact over Q.

    python generate_higher.py --output frozen/higher_certificate.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from itertools import combinations_with_replacement
from pathlib import Path

import generate_bases as bases

ORDERS = (4, 5, 6)
GAP_POWERS = (-3, -2, -1)
U_NAME = {0: "AP", 1: "AE0", 2: "AE1", 3: "AE2"}
W_NAME = {
    (0, 0): "P^2",
    (0, 1): "PE0",
    (0, 2): "PE1",
    (0, 3): "PE2",
    (1, 1): "E0^2",
    (1, 2): "E0E1",
    (1, 3): "E0E2",
    (2, 2): "E1^2",
    (2, 3): "E1E2",
    (3, 3): "E2^2",
}


def Q(value=0):
    return Fraction(value)


def all_slots(kind):
    if kind == "U":
        return list(range(4))
    return list(combinations_with_replacement(range(4), 2))


def slot_name(kind, slot):
    return U_NAME[slot] if kind == "U" else W_NAME[slot]


def raw_weight(exponent, dual):
    """Finite weight chi = 2s + x + y. W has weight 0, so it does not appear."""
    u, v, _w = dual
    return 2 * exponent + (-u - 1) + (-v - 1)


def character_of(exponent, dual, frame):
    return raw_weight(exponent, dual) - frame


def h0_line(degree):
    return degree + 1 if degree >= 0 else 0


def h1_line(degree):
    return -degree - 1 if degree <= -2 else 0


def h0_plane(degree):
    return bases.monomial_count(degree) if degree >= 0 else 0


def h2_plane(degree):
    return bases.monomial_count(-degree - 3) if degree <= -3 else 0


def cohomology_dimensions(base, plane):
    """Kunneth dimensions of an external line O(base, plane)."""
    return {
        "H0": h0_line(base) * h0_plane(plane),
        "H1": h1_line(base) * h0_plane(plane),
        "H2": h0_line(base) * h2_plane(plane),
        "H3": h1_line(base) * h2_plane(plane),
    }


def h2_monomials(base, plane):
    if base < 0 or plane > -3:
        return
    total = -plane - 3
    for exponent in range(base + 1):
        for dual in bases.enumerate_dual(total):
            yield exponent, dual


def h3_monomials(base, plane):
    if base > -2 or plane > -3:
        return
    total = -plane - 3
    # Cohomology basis of H^1(P^1, O(base)): z^{-1}, ..., z^{base+1}.
    for exponent in range(-1, base, -1):
        for dual in bases.enumerate_dual(total):
            yield exponent, dual


def monomial_record(exponent, dual, frame):
    u, v, w = dual
    actual = [-u - 1, -v - 1, -w - 1]
    weight = raw_weight(exponent, dual)
    return {
        "e": exponent,
        "dual": [u, v, w],
        "actual": actual,
        "weight": weight,
        "character": weight - frame,
    }


def gap_terms(poly):
    """All-negative terms whose z power lies in the H^1(P^1, O(-4)) gap."""
    out = {}
    for (exponent, x, y, w), coeff in bases.project_negative(poly).items():
        if exponent not in GAP_POWERS or not coeff:
            continue
        dual = (-x - 1, -y - 1, -w - 1)
        key = (exponent, dual)
        total = out.get(key, Q(0)) + coeff
        if total:
            out[key] = total
        elif key in out:
            del out[key]
    return out


def matrix_rank(rows):
    """Rank over Q of a list of rows of Fraction."""
    if not rows or not rows[0]:
        return 0
    grid = [row[:] for row in rows]
    height = len(grid)
    width = len(grid[0])
    rank = 0
    column = 0
    while rank < height and column < width:
        host = next((i for i in range(rank, height) if grid[i][column]), None)
        if host is None:
            column += 1
            continue
        grid[rank], grid[host] = grid[host], grid[rank]
        pivot = grid[rank][column]
        grid[rank] = [entry / pivot for entry in grid[rank]]
        for other in range(height):
            if other == rank or not grid[other][column]:
                continue
            factor = grid[other][column]
            grid[other] = [a - factor * b for a, b in zip(grid[other], grid[rank])]
        rank += 1
        column += 1
    return rank


def kernel_basis(columns):
    """Kernel basis of the matrix given by a list of columns.

    Returns rank and a list of sparse vectors {column index: coefficient}.
    """
    height = len(columns[0]) if columns else 0
    width = len(columns)
    if width == 0:
        return 0, []
    grid = [[columns[j][i] for j in range(width)] for i in range(height)]
    rank = 0
    pivot_of_column = {}
    column = 0
    while rank < height and column < width:
        host = next((i for i in range(rank, height) if grid[i][column]), None)
        if host is None:
            column += 1
            continue
        if host != rank:
            grid[rank], grid[host] = grid[host], grid[rank]
        pivot = grid[rank][column]
        grid[rank] = [entry / pivot for entry in grid[rank]]
        for other in range(height):
            if other == rank or not grid[other][column]:
                continue
            factor = grid[other][column]
            grid[other] = [a - factor * b for a, b in zip(grid[other], grid[rank])]
        pivot_of_column[column] = rank
        rank += 1
        column += 1
    pivots = sorted(pivot_of_column)
    basis = []
    for free in range(width):
        if free in pivot_of_column:
            continue
        vector = {free: Q(1)}
        for pivot in pivots:
            row = grid[pivot_of_column[pivot]]
            value = -row[free]
            if value:
                vector[pivot] = value
        basis.append({str(index): str(coeff) for index, coeff in sorted(vector.items())})
    return rank, basis


def delta_inner_columns(k):
    """Columns of delta: H^2(E0E1) -> H^3(E0^2), indexed by plane duals.

    The extension class is the off-diagonal z^{-3} C of
    0 -> E0^2 -> span{E0^2, E0E1} -> E0E1 -> 0.
    A class z^0 m on E0E1 transports to z^{-3} C m on E0^2. Its class in
    H^3 is the part on z in {-1,-2,-3}.
    """
    total = k - 1  # u+v+w for E0E1, plane degree -2-k
    duals = list(bases.enumerate_dual(total))
    h3_total = k - 5
    rows = []
    if h3_total >= 0:
        for exponent in GAP_POWERS:
            for dual in bases.enumerate_dual(h3_total):
                rows.append((exponent, dual))
    columns = []
    sparse = []
    for index, dual in enumerate(duals):
        image = gap_terms(bases.mul(bases.shift(bases.C, z=-3), bases.plane_monomial(dual)))
        column = [image.get(key, Q(0)) for key in rows]
        columns.append(column)
        for row_index, key in enumerate(rows):
            if column[row_index]:
                sparse.append((row_index, index, column[row_index]))
    return duals, rows, columns, sparse


def outer_obstruction(exponent, dual):
    """Class in H^3(E0^2) of one E1^2 monomial, after the E0E1 cochain homotopy.

    Transport of z^{e-4} m produces an E0^2 component z^{e-6} C^2 m and an
    E0E1 component 2 z^{e-3} C m. The E0E1 component is a coboundary on the
    line of base degree 0. Subtracting a primitive changes E0^2 by the
    off-diagonal z^{-3} C. With the finite/infinity split of that primitive,
    the remaining gap is

        z^{-3} C (psi_{z>=1} - psi_{z<=0}),    psi = z^{e-3} C m.

    A residual z^0 E0E1 class can still be added; that subtracts a column of
    delta_inner. The class in H^3(span) is this gap modulo im delta_inner.
    """
    monomial = bases.plane_monomial(dual)
    psi = bases.mul(bases.shift(bases.C, z=exponent - 3), monomial)
    positive = {}
    nonpositive = {}
    for exp, coeff in psi.items():
        if exp[0] >= 1:
            positive[exp] = coeff
        else:
            nonpositive[exp] = coeff
    difference = bases.add(positive, bases.scale(nonpositive, -1))
    return gap_terms(bases.mul(bases.shift(bases.C, z=-3), difference))


def transport_gap(exponent, dual):
    """Raw E0^2 gap of the triangular transport, before the E0E1 homotopy."""
    infinity = bases.empty_components("W")
    infinity[(2, 2)] = bases.shift(bases.plane_monomial(dual), z=exponent - 4)
    full = bases.transport_W(infinity)
    return gap_terms(full[(1, 1)])


def finite_threshold(kind, slot):
    return max(bases.base_degree(kind, slot) + 1, 0)


def lift_lower(kind, slot, symbol):
    """Finite all-negative lower terms of the normalized transport of symbol."""
    beta = bases.base_degree(kind, slot)
    infinity = bases.empty_components(kind)
    infinity[slot] = bases.shift(symbol, z=-beta)
    full = bases.transport_U(infinity) if kind == "U" else bases.transport_W(infinity)
    lower = {}
    for other, poly in full.items():
        if other == slot:
            continue
        kept = {}
        gap = {}
        threshold = finite_threshold(kind, other)
        other_beta = bases.base_degree(kind, other)
        for exp, coeff in bases.project_negative(poly).items():
            if exp[0] >= threshold:
                kept[exp] = coeff
            elif other_beta < exp[0] < 0:
                gap[exp] = coeff
        if gap:
            raise ValueError(f"transport of {slot} leaves an H^3 gap on {other}: {gap}")
        if kept:
            lower[other] = kept
    return lower


def reduced_coordinates(kind, k, finite):
    """Coordinates on the free-line basis, subtracting full transport lifts.

    The k=2,3 reducer subtracts only the first off-diagonal z^{-3} C. From
    k=6 the E1^2 lift also has an all-negative E0^2 term, through C^2. That
    term is not an H^2 class (base degree -4). It is removed with the lift.
    """
    residual = {slot: dict(poly) for slot, poly in finite.items()}
    allowed = {}
    for slot, beta, plane, _total in bases.iter_lines(kind, k):
        allowed[slot] = (beta, plane)
    coords = {}
    symbols = {}
    for slot, (beta, plane) in allowed.items():
        symbol = {}
        for exp, coeff in bases.project_negative(residual.get(slot, {})).items():
            if 0 <= exp[0] <= beta and exp[1] + exp[2] + exp[3] == plane and coeff:
                symbol[exp] = coeff
                coords[bases.coordinate_key(kind, slot, exp)] = coeff
        symbols[slot] = symbol
    for slot, symbol in symbols.items():
        if not symbol:
            continue
        for other, poly in lift_lower(kind, slot, symbol).items():
            current = residual.get(other, {})
            for exp, coeff in poly.items():
                updated = current.get(exp, Q(0)) - coeff
                if updated:
                    current[exp] = updated
                elif exp in current:
                    del current[exp]
            residual[other] = current
        current = residual.get(slot, {})
        for exp, coeff in symbol.items():
            updated = current.get(exp, Q(0)) - coeff
            if updated:
                current[exp] = updated
            elif exp in current:
                del current[exp]
        residual[slot] = current
    for slot, poly in residual.items():
        negative = bases.project_negative(poly)
        if negative:
            raise ValueError(f"cocycle has a residual component on {slot}: {negative}")
    return coords


def alpha_coordinates(k, finite_u):
    relation = bases.relation_polynomials()
    image = bases.empty_components("W")
    for channel, poly in finite_u.items():
        if not poly:
            continue
        for index, factor in enumerate(relation):
            slot = tuple(sorted((channel, index)))
            image[slot] = bases.add(image[slot], bases.mul(poly, factor))
    image = {slot: bases.project_negative(poly) for slot, poly in image.items()}
    return reduced_coordinates("W", k, image)


def required_vectors(kind, k):
    required = k - 4
    vectors = []
    for slot, _beta, _plane, _total in bases.iter_lines(kind, k):
        frame = bases.frame_weight(kind, slot, "finite")
        beta = bases.base_degree(kind, slot)
        plane = bases.plane_degree(kind, slot, k)
        total = -plane - 3
        for exponent in range(beta + 1):
            for dual in bases.enumerate_dual(total):
                if character_of(exponent, dual, frame) != required:
                    continue
                finite, infinity = bases.representative(kind, slot, exponent, dual, k)
                key = bases.coordinate_key(
                    kind,
                    slot,
                    (exponent, -dual[0] - 1, -dual[1] - 1, -dual[2] - 1),
                )
                coords = reduced_coordinates(kind, k, finite)
                if coords != {key: Q(1)}:
                    raise ValueError(f"required vector is not a unit coordinate: {coords}")
                record = {
                    "slot": slot if isinstance(slot, int) else list(slot),
                    "e": exponent,
                    "dual": list(dual),
                    "actual": [-dual[0] - 1, -dual[1] - 1, -dual[2] - 1],
                    "weight": raw_weight(exponent, dual),
                    "character": required,
                    "forced": bases.forced_terms(finite, slot),
                    "_finite": finite,
                    "_infinity": infinity,
                }
                vectors.append(record)
    return vectors


def alpha_matrix(k, source, target):
    index = {}
    for column, vector in enumerate(target):
        slot = tuple(vector["slot"])
        dual = tuple(vector["dual"])
        key = bases.coordinate_key(
            "W",
            slot,
            (vector["e"], -dual[0] - 1, -dual[1] - 1, -dual[2] - 1),
        )
        index[key] = column
    rows = [[Q(0) for _ in source] for _ in target]
    for column, vector in enumerate(source):
        coords = alpha_coordinates(k, vector["_finite"])
        for key, value in coords.items():
            if key not in index:
                raise ValueError(f"alpha image leaves the required W basis at {key}")
            rows[index[key]][column] = value
    return rows


def square_determinant(rows):
    size = len(rows)
    if any(len(row) != size for row in rows):
        return None
    grid = [row[:] for row in rows]
    det = Q(1)
    for pivot in range(size):
        host = next((i for i in range(pivot, size) if grid[i][pivot]), None)
        if host is None:
            return Q(0)
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


def public_vector(vector):
    return {key: value for key, value in vector.items() if not key.startswith("_")}


def line_report(kind, k):
    required = k - 4
    rows = []
    attained = []
    for slot in all_slots(kind):
        base = bases.base_degree(kind, slot)
        plane = bases.plane_degree(kind, slot, k)
        frame = bases.frame_weight(kind, slot, "finite")
        dims = cohomology_dimensions(base, plane)
        h2 = [monomial_record(exponent, dual, frame) for exponent, dual in h2_monomials(base, plane)]
        h3 = [monomial_record(exponent, dual, frame) for exponent, dual in h3_monomials(base, plane)]
        if len(h2) != dims["H2"] or len(h3) != dims["H3"]:
            raise ValueError(f"enumeration disagrees with Kunneth on {slot}")
        characters = defaultdict(int)
        for record in h2:
            characters[record["character"]] += 1
            attained.append(record["character"])
        required_rows = [record for record in h2 if record["character"] == required]
        bound = None if base < 0 or plane > -3 else 2 * base - 2 - frame
        if h2 and max(record["character"] for record in h2) != bound:
            raise ValueError("attained H^2 character is not the monomial bound")
        rows.append(
            {
                "kind": kind,
                "name": slot_name(kind, slot),
                "slot": slot if isinstance(slot, int) else list(slot),
                "base_degree": base,
                "plane_degree": plane,
                "finite_frame_weight": frame,
                "dimensions": dims,
                "H2_character_bound": bound,
                "H2_character_histogram": {str(key): characters[key] for key in sorted(characters)},
                "required_character": required,
                "required_H2": required_rows,
                "H3_monomials": h3,
                "H2_monomials": [
                    [record["e"], *record["dual"], record["weight"], record["character"]] for record in h2
                ],
            }
        )
    return rows, attained


def e02_weight_table(k):
    """Every Cech monomial of H^3(E0^2), grouped by plane dual."""
    base = bases.w_base(1, 1)
    plane = bases.w_plane(1, 1, k)
    frame = bases.frame_weight("W", (1, 1), "finite")
    if (base, plane) != (-4, 2 - k):
        raise ValueError("E0^2 is not O(-4, 2-k)")
    grouped = []
    for dual in bases.enumerate_dual(max(k - 5, -1)) if k >= 5 else []:
        terms = []
        for exponent, same in h3_monomials(base, plane):
            if same != dual:
                continue
            record = monomial_record(exponent, dual, frame)
            terms.append(record)
        if terms:
            grouped.append(
                {
                    "dual": list(dual),
                    "actual": terms[0]["actual"],
                    "weights": [term["weight"] for term in terms],
                    "monomials": terms,
                }
            )
    flat = [term for group in grouped for term in group["monomials"]]
    dims = cohomology_dimensions(base, plane)
    if len(flat) != dims["H3"]:
        raise ValueError("E0^2 weight table misses a Cech monomial")
    return {
        "line": "O(-4, 2-k)",
        "base_degree": base,
        "plane_degree": plane,
        "frame_weight": frame,
        "dimension": dims["H3"],
        "groups": grouped,
        "weights": [term["weight"] for term in flat],
        "characters": [term["character"] for term in flat],
    }


def character_block_ranks(duals, rows, columns):
    """Rank of delta_inner on each character. The map preserves character."""
    source_character = [-dual[0] - dual[1] - 4 for dual in duals]
    target_character = []
    for exponent, dual in rows:
        target_character.append(raw_weight(exponent, dual))  # frame weight of E0^2 is 0
    for row_index, column_index, _value in (
        (i, j, columns[j][i]) for j in range(len(columns)) for i in range(len(rows)) if columns[j][i]
    ):
        if source_character[column_index] != target_character[row_index]:
            raise ValueError("delta_inner sends a class to a different character")
    characters = sorted(set(source_character) | set(target_character))
    report = []
    for character in characters:
        source_index = [j for j, value in enumerate(source_character) if value == character]
        target_index = [i for i, value in enumerate(target_character) if value == character]
        block = [[columns[j][i] for j in source_index] for i in target_index]
        rank = matrix_rank(block) if block and block[0] else 0
        report.append(
            {
                "character": character,
                "source_dimension": len(source_index),
                "target_dimension": len(target_index),
                "rank": rank,
                "kernel_dimension": len(source_index) - rank,
                "cokernel_dimension": len(target_index) - rank,
            }
        )
    return report


def zero_map(source_dimension, target_dimension):
    return {
        "shape": [target_dimension, source_dimension],
        "entries": [],
        "rank": 0,
        "kernel_dimension": source_dimension,
        "cokernel_dimension": target_dimension,
    }


def extension_reports(k, inner):
    """Long exact sequences of the invariant extensions, in total and in chi=k-4."""
    required = k - 4
    reports = []

    def dimensions_of(kind, slot):
        return cohomology_dimensions(
            bases.base_degree(kind, slot),
            bases.plane_degree(kind, slot, k),
        )

    def required_h2(kind, slot):
        frame = bases.frame_weight(kind, slot, "finite")
        base = bases.base_degree(kind, slot)
        plane = bases.plane_degree(kind, slot, k)
        return sum(1 for exponent, dual in h2_monomials(base, plane) if character_of(exponent, dual, frame) == required)

    simple = (
        ("U", "AE0 inside span{AE0, AE1}", 1, 2),
        ("W", "PE0 inside span{PE0, PE1}", (0, 1), (0, 2)),
        ("W", "E0E2 inside span{E0E2, E1E2}", (1, 3), (2, 3)),
    )
    for kind, name, sub, quot in simple:
        sub_dims = dimensions_of(kind, sub)
        quot_dims = dimensions_of(kind, quot)
        if sub_dims["H3"] or sub_dims["H2"] or quot_dims["H1"]:
            raise ValueError(f"unexpected cohomology on the split extension {name}")
        total = {
            "H1_Q_to_H2_S": zero_map(quot_dims["H1"], sub_dims["H2"]),
            "delta_H2_Q_to_H3_S": zero_map(quot_dims["H2"], sub_dims["H3"]),
        }
        total["H2_E_dimension"] = total["H1_Q_to_H2_S"]["cokernel_dimension"] + total["delta_H2_Q_to_H3_S"]["kernel_dimension"]
        if total["H2_E_dimension"] != quot_dims["H2"]:
            raise ValueError("dimension identity failed on a split extension")
        required_source = required_h2(kind, quot)
        required_block = {
            "H1_Q_to_H2_S": zero_map(0, 0),
            "delta_H2_Q_to_H3_S": zero_map(required_source, 0),
            "H2_E_dimension": required_source,
        }
        reports.append(
            {
                "name": name,
                "sub_dimensions": sub_dims,
                "quotient_dimensions": quot_dims,
                "all_characters": total,
                "required_character": required_block,
            }
        )

    # Inner extension 0 -> E0^2 -> span -> E0E1 -> 0.
    sub_dims = dimensions_of("W", (1, 1))
    quot_dims = dimensions_of("W", (1, 2))
    rank = inner["rank"]
    kernel = quot_dims["H2"] - rank
    cokernel = sub_dims["H3"] - rank
    if kernel < 0 or cokernel < 0:
        raise ValueError("inner connecting rank exceeds a dimension")
    h1_to_h2 = zero_map(quot_dims["H1"], sub_dims["H2"])
    delta = {
        "shape": [sub_dims["H3"], quot_dims["H2"]],
        "entries": [[row, column, str(value)] for row, column, value in inner["sparse"]],
        "rank": rank,
        "kernel_dimension": kernel,
        "cokernel_dimension": cokernel,
        "row_labels": [
            {"e": exponent, "dual": list(dual), "weight": raw_weight(exponent, dual), "character": raw_weight(exponent, dual)}
            for exponent, dual in inner["rows"]
        ],
        "column_labels": [
            {"e": 0, "dual": list(dual), "character": -dual[0] - dual[1] - 4} for dual in inner["duals"]
        ],
        "kernel_basis": inner["kernel_basis"],
        "by_character": inner["by_character"],
    }
    h2_span = h1_to_h2["cokernel_dimension"] + kernel
    if h2_span != kernel:
        raise ValueError("inner dimension identity failed")
    required_characters = [block for block in inner["by_character"] if block["character"] == required]
    required_inner = {
        "H1_Q_to_H2_S": zero_map(0, 0),
        "delta_H2_Q_to_H3_S": {
            "shape": [
                sum(block["target_dimension"] for block in required_characters),
                sum(block["source_dimension"] for block in required_characters),
            ],
            "entries": [],
            "rank": sum(block["rank"] for block in required_characters),
            "kernel_dimension": sum(block["kernel_dimension"] for block in required_characters),
            "cokernel_dimension": sum(block["cokernel_dimension"] for block in required_characters),
        },
    }
    required_inner["H2_E_dimension"] = (
        required_inner["H1_Q_to_H2_S"]["cokernel_dimension"]
        + required_inner["delta_H2_Q_to_H3_S"]["kernel_dimension"]
    )
    reports.append(
        {
            "name": "E0^2 inside span{E0^2, E0E1}",
            "sub_dimensions": sub_dims,
            "quotient_dimensions": quot_dims,
            "all_characters": {
                "H1_Q_to_H2_S": h1_to_h2,
                "delta_H2_Q_to_H3_S": delta,
                "H2_E_dimension": h2_span,
            },
            "required_character": required_inner,
        }
    )

    # Outer extension. H^3(span) = coker(delta_inner).
    quot_dims = dimensions_of("W", (2, 2))
    if quot_dims["H1"] or quot_dims["H3"]:
        raise ValueError("E1^2 has unexpected H^1 or H^3")
    h3_span = cokernel
    h2_s = h2_span
    # Every naive obstruction class was checked to lie in im delta_inner.
    if not inner["outer_obstructions_in_image"]:
        raise ValueError("an E1^2 class does not lift")
    outer_delta = zero_map(quot_dims["H2"], h3_span)
    h1_map = zero_map(quot_dims["H1"], h2_s)
    h2_e = h1_map["cokernel_dimension"] + outer_delta["kernel_dimension"]
    required_h2_q = required_h2("W", (2, 2))
    # Required-character image in the full H^3(E0^2), not merely in the empty slice.
    image_rows = []
    for label, image in inner["required_E1_images"]:
        if image:
            raise ValueError(f"required E1^2 class has a nonzero H^3 image: {label} {image}")
        image_rows.append({"source": label, "image_in_H3_E0^2": []})
    required_outer = {
        "H1_Q_to_H2_S": zero_map(0, 0),
        "delta_H2_Q_to_H3_S": zero_map(required_h2_q, 0),
        "image_in_full_H3_E0^2": {
            "target_dimension": sub_dims["H3"],
            "columns": image_rows,
            "rank": 0,
        },
        "H2_E_dimension": required_h2_q,
    }
    reports.append(
        {
            "name": "span{E0^2, E0E1} inside the E1^2 extension",
            "sub_H2_dimension": h2_s,
            "sub_H3_dimension": h3_span,
            "quotient_dimensions": quot_dims,
            "naive_obstruction_outside_required_character": inner["naive_obstruction_counts"],
            "all_characters": {
                "H1_Q_to_H2_S": h1_map,
                "delta_H2_Q_to_H3_S": outer_delta,
                "H2_E_dimension": h2_e,
            },
            "required_character": required_outer,
        }
    )
    return reports


def connecting_inner(k):
    duals, rows, columns, sparse = delta_inner_columns(k)
    rank, kernel = kernel_basis(columns)
    by_character = character_block_ranks(duals, rows, columns)
    # Required-character E1^2 classes, and the full obstruction count.
    frame = bases.frame_weight("W", (2, 2), "finite")
    plane = bases.w_plane(2, 2, k)
    total = -plane - 3
    required = k - 4
    required_images = []
    naive_nonzero = 0
    naive_zero = 0
    outside_image = 0
    height = len(rows)
    # Precompute for membership tests only when the target is nonzero and we
    # need more than surjectivity. Surjectivity is rank == height.
    surjective = rank == height
    for exponent in range(5):
        for dual in bases.enumerate_dual(total):
            gap = outer_obstruction(exponent, dual)
            if any(key not in rows for key in gap):
                raise ValueError(f"outer obstruction leaves the H^3 basis: {gap}")
            if gap:
                naive_nonzero += 1
            else:
                naive_zero += 1
            if character_of(exponent, dual, frame) == required:
                raw = transport_gap(exponent, dual)
                if gap or raw:
                    raise ValueError(
                        f"required character {required} has a nonzero E1^2 connecting image at e={exponent} dual={dual}"
                    )
                required_images.append(
                    (
                        {"e": exponent, "dual": list(dual), "character": required},
                        [],
                    )
                )
    if not surjective:
        raise ValueError("delta_inner is not surjective; outer kernel must be recomputed")
    if outside_image:
        raise ValueError("outer obstruction left the image of delta_inner")
    return {
        "duals": duals,
        "rows": rows,
        "sparse": sparse,
        "rank": rank,
        "kernel_basis": kernel,
        "by_character": by_character,
        "required_E1_images": required_images,
        "outer_obstructions_in_image": surjective and outside_image == 0,
        "naive_obstruction_counts": {
            "zero_after_E0E1_homotopy": naive_zero,
            "nonzero_before_quotient_by_inner_image": naive_nonzero,
            "outside_inner_image": outside_image,
        },
    }


def corrected_dimensions(k, inner_rank):
    u_lines = []
    w_lines = []
    for kind, bucket in (("U", u_lines), ("W", w_lines)):
        for slot, beta, plane, total in bases.iter_lines(kind, k):
            count = (beta + 1) * bases.monomial_count(total)
            bucket.append(
                {
                    "slot": slot if isinstance(slot, int) else list(slot),
                    "name": slot_name(kind, slot),
                    "base_degree": beta,
                    "plane_degree": plane,
                    "dimension": count,
                }
            )
    u_dim = sum(row["dimension"] for row in u_lines)
    w_split = sum(row["dimension"] for row in w_lines)
    # The inner connecting map kills rank(delta) classes inside H^2(E0E1).
    # No other H^2 summand is reduced: H^1(Q)=0 and the outer target is the
    # cokernel of a surjective inner map.
    w_dim = w_split - inner_rank
    return {
        "lines_U": u_lines,
        "lines_W_split": w_lines,
        "dimension_U": u_dim,
        "dimension_W_split": w_split,
        "inner_connecting_rank": inner_rank,
        "dimension_W": w_dim,
    }


def max_character_of(lines):
    values = []
    for line in lines:
        for row in line["H2_monomials"]:
            values.append(row[-1])
    return max(values) if values else None


def certificate_payload():
    bases.assert_relation_transition()
    homotopy_checks = bases.assert_plane_homotopy()
    orders = {}
    attained_max = {"U": [], "W": []}
    for k in ORDERS:
        inner = connecting_inner(k)
        dims = corrected_dimensions(k, inner["rank"])
        u_lines, u_chars = line_report("U", k)
        w_lines, w_chars = line_report("W", k)
        attained_max["U"].extend(u_chars)
        attained_max["W"].extend(w_chars)
        source = required_vectors("U", k)
        target = required_vectors("W", k)
        block = alpha_matrix(k, source, target)
        determinant = square_determinant(block)
        if determinant is None or determinant == 0:
            raise ValueError(f"required alpha block at order {k} is not invertible over Q")
        weight_table = e02_weight_table(k)
        extensions = extension_reports(k, inner)
        orders[str(k)] = {
            "k": k,
            "required_character": k - 4,
            "cohomology_dimensions": dims,
            "E0^2_H3_weights": weight_table,
            "extensions": extensions,
            "filtration_U": u_lines,
            "filtration_W": w_lines,
            "required_U": [public_vector(vector) for vector in source],
            "required_W": [public_vector(vector) for vector in target],
            "alpha_matrix": [[str(entry) for entry in row] for row in block],
            "alpha_determinant": str(determinant),
            "alpha_rank": matrix_rank(block),
        }
    max_u = max(attained_max["U"])
    max_w = max(attained_max["W"])
    if max_u != 2 or max_w != 2:
        raise ValueError(f"generated max characters are U {max_u}, W {max_w}")
    cutoff = []
    for k in range(7, 13):
        cutoff.append(
            {
                "k": k,
                "required_character": k - 4,
                "exceeds_generated_max": k - 4 > max(max_u, max_w),
            }
        )
    if not all(row["exceeds_generated_max"] for row in cutoff):
        raise ValueError("weight cutoff does not start at k>=7")
    return {
        "relation_transition_identity": True,
        "plane_homotopy_support_checks": homotopy_checks,
        "scope": "k=4,5,6 connecting maps and required characters",
        "arithmetic": "exact rational",
        "character_convention": "finite weight chi=2s+x+y with W of weight 0; character is chi minus the finite frame weight",
        "inputs": {
            "base_bidegrees_B": list(bases.BASE_B),
            "plane_bidegrees_B": list(bases.PLANE_B),
            "finite_frame_weights": list(bases.D_FINITE),
            "infinity_frame_weights": list(bases.D_INFINITY),
            "weights_z_X_Y_W": [2, 1, 1, 0],
            "transport": "TU=z^{-1} TB, TW=z^{-4} Sym^2(TB), TB=diag(z^3,1,z^4,z^3) with TB[E0,E1]=z C",
            "C": "S^2 + z S W^2 + z^2 W^4",
            "excluded": "shipped order label lists, stored maps, pivot sets, expected dimensions",
        },
        "generated_max_character": {"U": max_u, "W": max_w},
        "weight_cutoff_from_k": 7,
        "weight_cutoff_checks": cutoff,
        "orders": orders,
    }


def canonical_bytes(payload):
    return json.dumps(payload, indent=2, sort_keys=True).encode("utf-8") + b"\n"


def body_of(document):
    return {key: value for key, value in document.items() if key != "content_sha256"}


def digest_of(document):
    return hashlib.sha256(canonical_bytes(body_of(document))).hexdigest()


def attach_hash(payload):
    return {"content_sha256": digest_of(payload), **payload}


def verify_certificate(path):
    document = json.loads(Path(path).read_text(encoding="utf-8"))
    digest = digest_of(document)
    if digest != document.get("content_sha256"):
        raise ValueError("certificate hash mismatch")
    return digest


def write_certificate(path):
    payload = attach_hash(certificate_payload())
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload["content_sha256"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    digest = write_certificate(args.output)
    stored = json.loads(args.output.read_text(encoding="utf-8"))
    for k in ("4", "5", "6"):
        order = stored["orders"][k]
        dims = order["cohomology_dimensions"]
        weights = order["E0^2_H3_weights"]["weights"]
        inner = next(item for item in order["extensions"] if item["name"].startswith("E0^2"))
        delta = inner["all_characters"]["delta_H2_Q_to_H3_S"]
        print(
            f"k={k} dim U={dims['dimension_U']} dim W={dims['dimension_W']} "
            f"(split {dims['dimension_W_split']}) required {len(order['required_U'])}x{len(order['required_W'])} "
            f"det {order['alpha_determinant']} inner rank {delta['rank']} "
            f"ker {delta['kernel_dimension']} H3 weights {weights}"
        )
    print(f"content_sha256 {digest}")
    print(f"generated max character U {stored['generated_max_character']['U']} W {stored['generated_max_character']['W']}")


if __name__ == "__main__":
    main()
