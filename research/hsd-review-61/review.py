"""Independent exact review of the five-parameter formal chart.

Reads JSON under research/carrier/formal-five-parameter-chart/data and compares
with the shipped certificates. Does not import the package's checkers.

Arithmetic is exact: linear algebra over fractions.Fraction, integer
determinants by a Hadamard bound plus the Chinese remainder theorem, and
polynomial identities in Q[a,b,c,d,lambda] via SymPy.
"""

from __future__ import annotations

import argparse
import json
import math
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations

PKG = Path(__file__).resolve().parents[1] / "carrier" / "formal-five-parameter-chart"
DATA = PKG / "data"
CERT = PKG / "certificates"

# Finite frame weights d(P, E0, E1, E2), from the fixed linearization.
FRAME = (3, 0, 2, 2)
# Bundle bidegrees (base, plane) of the ordered B summands P, E0, E1, E2.
BASE_B = (3, 0, 4, 3)
PLANE_B = (-3, 0, -4, -4)
NAMES = ("P", "E0", "E1", "E2")

A_SYM, B_SYM, C_SYM, D_SYM, LAM = sp.symbols("a b c d lambda")
GENS = (A_SYM, B_SYM, C_SYM, D_SYM, LAM)
PARSE_LOCALS = {"a": A_SYM, "b": B_SYM, "c": C_SYM, "d": D_SYM, "lambda": LAM}

EXPECTED_MINOR = {2: 16, 3: -512, 4: -16384}
EXPECTED_BLOCK = {3: 9, 4: 5, 5: 2, 6: 1}


def Q(value) -> Fraction:
    text = str(value)
    if any(ch.isalpha() for ch in text):
        raise ValueError(f"non-constant coefficient: {text}")
    return Fraction(text)


def load(name: str):
    return json.loads((DATA / name).read_text())


def load_cert(name: str):
    return json.loads((CERT / name).read_text())


def parse_poly(text: str):
    # Integer/Rational are the parser's own number constructors, not parameters.
    expr = parse_expr(
        str(text),
        local_dict=PARSE_LOCALS,
        global_dict={"Integer": sp.Integer, "Rational": sp.Rational},
        transformations=standard_transformations,
    )
    expr = sp.expand(expr)
    extra = expr.free_symbols - set(GENS)
    if extra:
        raise ValueError(f"unexpected symbols {extra} in {text}")
    return expr


def rat(q: Fraction) -> sp.Rational:
    return sp.Rational(q.numerator, q.denominator)


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            step = p
            start = p * p
            sieve[start::step] = b"\x00" * ((limit - start) // step + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


PRIMES = primes_upto(5000)


def isqrt(n: int) -> int:
    return int(math.isqrt(n))


def crt(residues: list[int], moduli: list[int]) -> tuple[int, int]:
    x = 0
    modulus = 1
    for residue, prime in zip(residues, moduli):
        reduced = modulus % prime
        inverse = pow(reduced, -1, prime)
        add = ((residue - x) * inverse) % prime
        x += modulus * add
        modulus *= prime
    return x, modulus


def det_mod(matrix: list[list[int]], prime: int) -> int:
    size = len(matrix)
    rows = [[entry % prime for entry in row] for row in matrix]
    sign = 1
    for col in range(size):
        pivot = next((row for row in range(col, size) if rows[row][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            rows[col], rows[pivot] = rows[pivot], rows[col]
            sign = -sign
        pivot_inverse = pow(rows[col][col], -1, prime)
        pivot_row = rows[col]
        for row in range(col + 1, size):
            factor = rows[row][col]
            if factor == 0:
                continue
            factor = (factor * pivot_inverse) % prime
            target = rows[row]
            for j in range(col, size):
                target[j] = (target[j] - factor * pivot_row[j]) % prime
    det = sign % prime
    for i in range(size):
        det = (det * rows[i][i]) % prime
    return det


def hadamard_bound(matrix: list[list[int]]) -> int:
    """Return B such that |det| <= B. A zero column gives B = 0."""
    size = len(matrix)
    product = 1
    for col in range(size):
        norm_sq = 0
        for row in range(size):
            value = matrix[row][col]
            norm_sq += value * value
        if norm_sq == 0:
            return 0
        product *= norm_sq
    return isqrt(product)


def integer_det(matrix: list[list[int]]) -> int:
    bound = hadamard_bound(matrix)
    if bound == 0:
        return 0
    residues: list[int] = []
    moduli: list[int] = []
    covered = 1
    target = 2 * bound
    for prime in PRIMES:
        residues.append(det_mod(matrix, prime))
        moduli.append(prime)
        covered *= prime
        if covered > target:
            break
    else:
        raise RuntimeError("prime list exhausted before the Hadamard bound was covered")
    value, modulus = crt(residues, moduli)
    if value * 2 > modulus:
        value -= modulus
    if abs(value) > bound:
        raise RuntimeError(f"centered determinant {value} exceeds Hadamard bound {bound}")
    return value


def rational_det(matrix: list[list[Fraction]]) -> tuple[Fraction, dict]:
    cleared: list[list[int]] = []
    row_denominators = []
    entry_denominators = set()
    for row in matrix:
        denominator = 1
        for entry in row:
            entry_denominators.add(entry.denominator)
            denominator = math.lcm(denominator, entry.denominator)
        row_denominators.append(denominator)
        cleared.append([int(entry * denominator) for entry in row])
    det_int = integer_det(cleared)
    det = Fraction(det_int, 1)
    for denominator in row_denominators:
        det /= denominator
    meta = {
        "entry_denominators": sorted(entry_denominators),
        "cleared_integer_det": str(det_int),
        "hadamard_bound_of_cleared": str(hadamard_bound(cleared)),
    }
    return det, meta


def rref(matrix: list[list[Fraction]]):
    rows = [list(row) for row in matrix]
    m = len(rows)
    n = len(rows[0]) if m else 0
    pivots = []
    rank = 0
    for col in range(n):
        pivot = next((row for row in range(rank, m) if rows[row][col] != 0), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][col]
        rows[rank] = [entry / scale for entry in rows[rank]]
        for row in range(m):
            if row == rank or rows[row][col] == 0:
                continue
            factor = rows[row][col]
            rows[row] = [a - factor * b for a, b in zip(rows[row], rows[rank])]
        pivots.append(col)
        rank += 1
        if rank == m:
            break
    return rows, pivots


def nullspace(matrix: list[list[Fraction]]):
    reduced, pivots = rref(matrix)
    if not matrix:
        return []
    width = len(matrix[0])
    pivot_row = {col: row for row, col in enumerate(pivots)}
    basis = []
    for free in range(width):
        if free in pivot_row:
            continue
        vector = [Fraction(0)] * width
        vector[free] = Fraction(1)
        for col, row in pivot_row.items():
            vector[col] = -reduced[row][free]
        basis.append(vector)
    return basis


def invert(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    size = len(matrix)
    augmented = [
        list(row) + [Fraction(int(i == j)) for j in range(size)]
        for i, row in enumerate(matrix)
    ]
    reduced, pivots = rref(augmented)
    if pivots != list(range(size)):
        raise ValueError(f"singular or mis-pivoted matrix, pivots {pivots}")
    return [row[size:] for row in reduced]


def matmul(left, right):
    rows = len(left)
    cols = len(right[0])
    mid = len(right)
    return [
        [sum(left[i][k] * right[k][j] for k in range(mid)) for j in range(cols)]
        for i in range(rows)
    ]


def identity(size: int):
    return [[Fraction(int(i == j)) for j in range(size)] for i in range(size)]


def source_weight(label) -> int:
    channel, exponent, (u, v, _w) = label
    return 2 * exponent - u - v - 2 - FRAME[channel]


def target_actual_weight(label) -> int:
    (left, right), exponent, (p, q, _r) = label
    return 2 * exponent + p + q - FRAME[left] - FRAME[right]


def raw_dual_weight(label) -> int:
    (left, right), exponent, (u, v, _w) = label
    return 2 * exponent - u - v - 2 - FRAME[left] - FRAME[right]


def sparse_matrix(shape, triples) -> list[list[Fraction]]:
    rows, cols = shape
    matrix = [[Fraction(0) for _ in range(cols)] for _ in range(rows)]
    seen = set()
    for i, j, value in triples:
        if not (0 <= i < rows and 0 <= j < cols):
            raise ValueError(f"index {(i, j)} outside {shape}")
        if (i, j) in seen:
            raise ValueError(f"duplicate entry {(i, j)}")
        seen.add((i, j))
        entry = Q(value)
        if entry == 0:
            raise ValueError(f"explicit zero at {(i, j)}")
        matrix[i][j] = entry
    return matrix


def submatrix(matrix, row_index, col_index):
    return [[matrix[i][j] for j in col_index] for i in row_index]


def constant_entries(matrix) -> dict:
    denominators = sorted({entry.denominator for row in matrix for entry in row})
    numerators_ok = all(isinstance(entry, Fraction) for row in matrix for entry in row)
    return {
        "constant_rationals": numerators_ok,
        "parameter_symbols": [],
        "entry_denominators": denominators,
    }


def factor_int(number: int) -> list[int]:
    factors = []
    rest = abs(number)
    prime = 2
    while prime * prime <= rest:
        while rest % prime == 0:
            factors.append(prime)
            rest //= prime
        prime += 1 if prime == 2 else 2
    if rest > 1:
        factors.append(rest)
    return factors


def homogeneous_block(order: int):
    data = load(f"order_{order}.json")
    prefix = "D" if order == 1 else f"D{order}"
    matrix = sparse_matrix(data[f"{prefix}_shape"], data[f"{prefix}_sparse"])
    source = data[f"{prefix}_source_basis"]
    if len(source) != len(matrix[0]):
        raise ValueError(f"D{order} source basis does not match column count")
    source_weights = [source_weight(label) for label in source]
    columns = [j for j, weight in enumerate(source_weights) if weight == order - 4]
    pivot_report = None
    if order < 5:
        target = data[f"{prefix}_target_basis"]
        if len(target) != len(matrix):
            raise ValueError(f"D{order} target basis does not match row count")
        target_weights = [target_actual_weight(label) for label in target]
        rows = [i for i, weight in enumerate(target_weights) if weight == order - 4]
    else:
        raw = data[f"raw_W{order}_labels"]
        raw_weights = [raw_dual_weight(label) for label in raw]
        supplied_free = data[f"W{order}_kernel_free_columns"]
        supplied_pivots = data[f"C{order}_pivot_columns"]
        c_entries = data[f"C{order}_sparse"]
        c_rows = 1 + max(i for i, _j, _v in c_entries)
        c_matrix = sparse_matrix([c_rows, len(raw)], c_entries)
        _reduced, pivots = rref(c_matrix)
        free_set = [j for j in range(len(raw)) if j not in set(pivots)]
        pivot_report = {
            "recomputed_pivots": pivots,
            "supplied_pivots": supplied_pivots,
            "pivots_match": pivots == supplied_pivots,
            "free_set_matches_supplied_set": set(free_set) == set(supplied_free),
            "supplied_free_equals_sorted_complement": list(supplied_free) == free_set,
            "supplied_free_is_complement": set(supplied_free).isdisjoint(pivots)
            and set(supplied_free).union(pivots) == set(range(len(raw))),
            "raw_weight_selected_columns": [j for j, weight in enumerate(raw_weights) if weight == order - 4],
        }
        if len(supplied_free) != len(matrix):
            raise ValueError(f"D{order} row count is not the free-column count")
        target_weights = [raw_weights[j] for j in supplied_free]
        rows = [i for i, weight in enumerate(target_weights) if weight == order - 4]
    graded = all(
        target_weights[i] == source_weights[j]
        for i, row in enumerate(matrix)
        for j, entry in enumerate(row)
        if entry != 0
    )
    block = submatrix(matrix, rows, columns)
    return {
        "matrix": block,
        "rows": rows,
        "columns": columns,
        "graded": graded,
        "pivots": pivot_report,
        "shape": [len(rows), len(columns)],
    }


def check_inverses():
    certificate = load_cert("higher_certificate.json")
    report = {}
    ok = True
    for order in (3, 4, 5, 6):
        extracted = homogeneous_block(order)
        block = extracted["matrix"]
        size = EXPECTED_BLOCK[order]
        inverse = invert(block)
        product = matmul(block, inverse)
        other = matmul(inverse, block)
        eye = identity(size)
        det = rational_det(block)[0]
        witness = certificate["blocks"][str(order)]
        witness_inverse = [[Q(entry) for entry in row] for row in witness["right_inverse"]]
        witness_matrix = [[Q(entry) for entry in row] for row in witness["matrix"]]
        info = constant_entries(block)
        info_inv = constant_entries(inverse)
        item = {
            "shape": extracted["shape"],
            "rows": extracted["rows"],
            "columns": extracted["columns"],
            "rows_match_certificate": extracted["rows"] == witness["target_rows"],
            "columns_match_certificate": extracted["columns"] == witness["source_columns"],
            "matrix_matches_certificate": block == witness_matrix,
            "determinant": str(det),
            "D_times_inverse_is_I": product == eye,
            "inverse_times_D_is_I": other == eye,
            "block_entries": info,
            "inverse_entries": info_inv,
            "inverse_matches_certificate": inverse == witness_inverse,
            "weight_homogeneous_nonzero_entries": extracted["graded"],
            "pivot_check": extracted["pivots"],
        }
        passed = (
            extracted["shape"] == [size, size]
            and product == eye
            and other == eye
            and block == witness_matrix
            and inverse == witness_inverse
            and info["constant_rationals"]
            and info_inv["constant_rationals"]
            and info["parameter_symbols"] == []
            and info_inv["parameter_symbols"] == []
            and extracted["graded"]
            and extracted["rows"] == witness["target_rows"]
            and extracted["columns"] == witness["source_columns"]
        )
        if extracted["pivots"] is not None:
            passed = passed and extracted["pivots"]["pivots_match"] and extracted["pivots"]["supplied_free_is_complement"]
        item["pass"] = passed
        ok = ok and passed
        report[str(order)] = item
        print(
            f"D{order}: {extracted['shape'][0]}x{extracted['shape'][1]} "
            f"det {det} D*R=I {product == eye} entries in Q denominators {info_inv['entry_denominators']} "
            f"matches witness {inverse == witness_inverse}",
            flush=True,
        )
    report["pass"] = ok
    return report


def check_minors():
    report = {}
    ok = True
    for order, expected in EXPECTED_MINOR.items():
        data = load(f"order_{order}.json")
        shape = data[f"N{order}_shape"]
        matrix = sparse_matrix(shape, data[f"N{order}_sparse"])
        minor = data[f"N{order}_rank_minor"]
        rows, columns = minor["rows"], minor["columns"]
        if columns != list(range(shape[1])) or len(rows) != shape[1] or len(set(rows)) != shape[1]:
            raise ValueError(f"N{order} index set is not a maximal column minor")
        block = submatrix(matrix, rows, columns)
        det, meta = rational_det(block)
        factors = factor_int(det.numerator) if det.denominator == 1 else factor_int(det.numerator)
        stored = minor.get("exact_determinant")
        item = {
            "ambient_shape": shape,
            "minor_shape": [len(rows), len(columns)],
            "determinant": str(det),
            "expected": str(expected),
            "matches_expected": det == expected,
            "constant": constant_entries(block),
            "prime_factors_of_numerator": factors,
            "denominator": det.denominator,
            "only_prime_2": factors == [] or set(factors) == {2},
            "stored_exact_determinant": stored,
            "matches_stored_exact": None if stored is None else det == Q(stored),
            "meta": meta,
        }
        if "determinant_mod_prime" in minor:
            prime = int(minor["prime"])
            item["stored_det_mod_prime"] = {
                "prime": prime,
                "stored": minor["determinant_mod_prime"],
                "recomputed": int(det) % prime,
                "matches": int(det) % prime == int(minor["determinant_mod_prime"]) % prime,
            }
        passed = det == expected and det.denominator == 1 and item["only_prime_2"] and item["constant"]["parameter_symbols"] == []
        item["pass"] = passed
        ok = ok and passed
        report[str(order)] = item
        print(
            f"N{order}: maximal minor det {det} expected {expected} "
            f"denominator {det.denominator} primes {factors}",
            flush=True,
        )
    report["pass"] = ok
    return report


def monomial_support(expr) -> list[str]:
    polynomial = sp.Poly(sp.expand(expr), *GENS)
    if polynomial.is_zero:
        return []
    rendered = []
    for exponents, coefficient in sorted(polynomial.as_dict().items()):
        rendered.append(f"{coefficient}*a^{exponents[0]}*b^{exponents[1]}*c^{exponents[2]}*d^{exponents[3]}*lambda^{exponents[4]}")
    return rendered


def check_quadratic():
    data_block = homogeneous_block(2)
    block = data_block["matrix"]
    certificate = load_cert("quadratic_certificate.json")
    witness_matrix = [[Q(entry) for entry in row] for row in certificate["D2_hom"]]
    obstruction = [parse_poly(entry) for entry in certificate["obstruction_vector"]]
    preimage = [parse_poly(entry) for entry in certificate["polynomial_preimage"]]
    if len(block) != 16 or len(block[0]) != 15:
        raise ValueError(f"unexpected D2 shape {data_block['shape']}")
    if block != witness_matrix:
        raise ValueError("D2 homogeneous block from data disagrees with the certificate matrix")

    image = []
    for row in block:
        total = 0
        for entry, coordinate in zip(row, preimage):
            total += rat(entry) * coordinate
        image.append(sp.expand(total))
    residual = [sp.expand(got - want) for got, want in zip(image, obstruction)]
    residual_zero = all(sp.Poly(entry, *GENS).is_zero for entry in residual)

    left = nullspace(list(map(list, zip(*block))))
    scalars = []
    for vector in left:
        total = sum(rat(coeff) * component for coeff, component in zip(vector, obstruction))
        scalars.append(sp.expand(total))
    scalar_zero = all(sp.Poly(entry, *GENS).is_zero for entry in scalars)
    support = sorted({str(symbol) for component in obstruction for symbol in component.free_symbols})
    degrees = []
    for component in obstruction:
        polynomial = sp.Poly(sp.expand(component), *GENS)
        degrees.append(-1 if polynomial.is_zero else polynomial.total_degree())
    detector = [Q(entry) for entry in certificate["left_cokernel_detector"]]
    detector_kills_rows = matmul([detector], block) == [[Fraction(0)] * 15]
    detector_scalar = sp.expand(sum(rat(coeff) * component for coeff, component in zip(detector, obstruction)))
    primitive = None
    if len(left) == 1:
        cleared = math.lcm(*(coeff.denominator for coeff in left[0]))
        primitive = [int(coeff * cleared) for coeff in left[0]]
        content = math.gcd(*primitive)
        primitive = [entry // content for entry in primitive]

    _reduced, pivots = rref(block)
    if len(pivots) != 15:
        raise ValueError(f"D2 column rank is {len(pivots)}, expected 15")
    minor = submatrix(block, pivots, list(range(15)))
    minor_inverse = invert(minor)
    recomputed = []
    for row in minor_inverse:
        total = 0
        for coeff, index in zip(row, pivots):
            total += rat(coeff) * obstruction[index]
        recomputed.append(sp.expand(total))
    preimage_matches = all(sp.expand(got - want) == 0 for got, want in zip(recomputed, preimage))
    full_residual_of_recomputed = []
    for row in block:
        total = 0
        for entry, coordinate in zip(row, recomputed):
            total += rat(entry) * coordinate
        full_residual_of_recomputed.append(sp.expand(total))
    recomputed_solves = all(
        sp.Poly(sp.expand(got - want), *GENS).is_zero
        for got, want in zip(full_residual_of_recomputed, obstruction)
    )

    item = {
        "D2_shape": data_block["shape"],
        "D2_matches_certificate_matrix": True,
        "column_rank": len(pivots),
        "left_kernel_dimension": len(left),
        "primitive_left_kernel": primitive,
        "certificate_detector": [str(entry) for entry in detector],
        "certificate_detector_annihilates_D2": detector_kills_rows,
        "supplied_preimage_residual_is_zero": residual_zero,
        "recomputed_preimage_matches_supplied": preimage_matches,
        "recomputed_preimage_solves_equation": recomputed_solves,
        "scalar_is_zero_polynomial_in_five_parameters": scalar_zero and sp.Poly(detector_scalar, *GENS).is_zero,
        "scalar_coefficient_dict": monomial_support(scalars[0] if scalars else detector_scalar),
        "detector_scalar_coefficient_dict": monomial_support(detector_scalar),
        "obstruction_free_symbols": support,
        "obstruction_total_degrees": degrees,
        "lambda_appears_in_supplied_obstruction": "lambda" in support,
        "pass": bool(
            residual_zero
            and scalar_zero
            and sp.Poly(detector_scalar, *GENS).is_zero
            and preimage_matches
            and recomputed_solves
            and detector_kills_rows
            and len(left) == 1
            and len(pivots) == 15
        ),
    }
    print(
        f"quadratic: residual 0 {residual_zero}; scalar 0 in Q[a,b,c,d,lambda] "
        f"{item['scalar_is_zero_polynomial_in_five_parameters']}; "
        f"symbols in obstruction {support}; preimage matches {preimage_matches}",
        flush=True,
    )
    return item


def line_cutoff(base: int, weight_sum: int):
    """Largest order whose required character weight can still meet the H^2 bound.

    A Čech H^2 representative on O(b, *) with b >= 0 has secondary weight at most
    2b - 2. The required finite weight at order k is k - 4 + weight_sum. Such a
    term can exist only for k <= 2b + 2 - weight_sum. Negative base degree has no H^2.
    """
    if base < 0:
        return None
    return 2 * base + 2 - weight_sum


def check_weights():
    from itertools import combinations_with_replacement

    w_lines = []
    for i, j in combinations_with_replacement(range(4), 2):
        base = BASE_B[i] + BASE_B[j] - 4
        plane = PLANE_B[i] + PLANE_B[j] + 2
        cutoff = line_cutoff(base, FRAME[i] + FRAME[j])
        max_weight = None if base < 0 else 2 * base - 2
        required_at_7 = 7 - 4 + FRAME[i] + FRAME[j]
        w_lines.append(
            {
                "slot": [NAMES[i], NAMES[j]],
                "base_degree": base,
                "plane_degree_before_minus_k": plane,
                "frame_weight_sum": FRAME[i] + FRAME[j],
                "max_H2_weight": max_weight,
                "cutoff": cutoff,
                "required_weight_at_order_7": required_at_7,
                "vanishes_for_all_k_ge_7": max_weight is None or required_at_7 > max_weight,
            }
        )
    u_lines = []
    for i in range(4):
        base = BASE_B[i] - 1
        plane = PLANE_B[i] - 4
        cutoff = line_cutoff(base, FRAME[i])
        max_weight = None if base < 0 else 2 * base - 2
        required_at_7 = 7 - 4 + FRAME[i]
        u_lines.append(
            {
                "slot": "A" + NAMES[i],
                "base_degree": base,
                "plane_degree_before_minus_k": plane,
                "frame_weight": FRAME[i],
                "max_H2_weight": max_weight,
                "cutoff": cutoff,
                "required_weight_at_order_7": required_at_7,
                "vanishes_for_all_k_ge_7": max_weight is None or required_at_7 > max_weight,
            }
        )
    section_max = 2 * 3 - 2
    certificate = load_cert("weight_certificate.json")
    cert_w = [(row["slot"], row["base_degree"], row["H2_weight_cutoff"]) for row in certificate["W_filtration"]]
    got_w = [(row["slot"], row["base_degree"], row["cutoff"]) for row in w_lines]
    cert_u = [(row["slot"], row["base_degree"], row["H2_weight_cutoff"]) for row in certificate["U_filtration"]]
    got_u = [(row["slot"], row["base_degree"], row["cutoff"]) for row in u_lines]
    finite_cutoffs = [row["cutoff"] for row in w_lines + u_lines if row["cutoff"] is not None]
    item = {
        "W_lines": w_lines,
        "U_lines": u_lines,
        "max_finite_cutoff": max(finite_cutoffs),
        "all_lines_vanish_for_k_ge_7": all(row["vanishes_for_all_k_ge_7"] for row in w_lines + u_lines),
        "parameter_symbols_in_the_inequality": [],
        "section_base_degree": 3,
        "section_max_weight": section_max,
        "section_vanishes_for_k_ge_5": 5 > section_max,
        "matches_weight_certificate": cert_w == got_w and cert_u == got_u,
        "pass": all(row["vanishes_for_all_k_ge_7"] for row in w_lines + u_lines) and max(finite_cutoffs) <= 6,
    }
    print(
        f"weights: max cutoff {item['max_finite_cutoff']}; "
        f"all 14 lines vanish for order >= 7: {item['all_lines_vanish_for_k_ge_7']}; "
        f"certificate match {item['matches_weight_certificate']}",
        flush=True,
    )
    return item


def self_test():
    sample = [[Fraction(1), Fraction(2)], [Fraction(3), Fraction(4)]]
    if rational_det(sample)[0] != -2:
        raise RuntimeError("determinant self-test failed")
    inverse = invert(sample)
    if matmul(sample, inverse) != identity(2):
        raise RuntimeError("inverse self-test failed")
    zero = sp.expand(A_SYM * LAM - LAM * A_SYM)
    if not sp.Poly(zero, *GENS).is_zero:
        raise RuntimeError("polynomial self-test failed")
    parsed = parse_poly("-a/2 + b**2 - 3/4")
    if parsed.free_symbols - {A_SYM, B_SYM}:
        raise RuntimeError("parser self-test failed")


def run_replay():
    replay = subprocess.run(
        [sys.executable, str(PKG / "replay.py")],
        cwd=PKG,
        check=False,
        capture_output=True,
        text=True,
    )
    tests = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=PKG,
        check=False,
        capture_output=True,
        text=True,
    )
    print(replay.stdout)
    print(replay.stderr)
    print(tests.stdout)
    print(tests.stderr)
    return {"replay_exit": replay.returncode, "tests_exit": tests.returncode}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--replay", action="store_true", help="also run the package replay and its unit tests")
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()
    self_test()
    report = {
        "package": str(PKG),
        "inverses": check_inverses(),
        "minors": check_minors(),
        "quadratic": check_quadratic(),
        "weights": check_weights(),
    }
    if args.replay:
        report["replay"] = run_replay()
    checks = {
        "2_inverses": report["inverses"]["pass"],
        "3_minors": report["minors"]["pass"],
        "4_quadratic": report["quadratic"]["pass"],
        "5_weights": report["weights"]["pass"],
    }
    report["independent_checks_pass"] = all(checks.values())
    print(
        "scope: checks 2–5 recompute linear algebra from data/*.json. "
        "The order-2 cocycle, the omitted ancestor plane model, and replay.py "
        "are not reconstructed here; the quadratic witness is the shipped certificate.",
        flush=True,
    )
    print(json.dumps({"checks": checks, "independent_checks_pass": report["independent_checks_pass"]}, indent=2))
    if args.json_out:
        args.json_out.write_text(json.dumps(report, indent=2) + "\n")
    return 0 if report["independent_checks_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
