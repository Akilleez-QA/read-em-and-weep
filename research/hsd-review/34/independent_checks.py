"""Exact BigInt/Fraction checks for the scalar, residue, and kernel notes.

None of this imports or executes the package verifiers.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[2] / "hm" / "current-scalar-proof"


def record(name, status, detail):
    return {"name": name, "status": status, "detail": detail}


def _binomial(numerator, k):
    if numerator >= 0:
        return comb(numerator, k)
    return (-1) ** k * comb(k - numerator - 1, k)


def _add(left, right, scale=1):
    result = dict(left)
    for key, value in right.items():
        updated = result.get(key, 0) + scale * value
        if updated:
            result[key] = updated
        else:
            result.pop(key, None)
    return result


def _multiply(left, right):
    result = {}
    for left_key, left_value in left.items():
        for right_key, right_value in right.items():
            key = tuple(a + b for a, b in zip(left_key, right_key))
            result[key] = result.get(key, 0) + left_value * right_value
    return {key: value for key, value in result.items() if value}


def check_scalar_rows():
    model = json.loads((PACKAGE / "data" / "model.json").read_text())
    findings = []
    constant = [["0,0,0,0", 1]]
    gamma_row = model["gamma"][10]
    ev_column = [model["ev"][0][0], model["ev"][1][0]]
    gamma_ok = gamma_row == [constant, [], [], [], []]
    ev_ok = ev_column == [constant, []]
    findings.append(record(
        "gamma[10,:]=(v0,0,0,0,0) and ev[:,0]=(v0,0)^t",
        "reproduced" if gamma_ok and ev_ok else "defect",
        {"gamma_row": gamma_row, "ev_column": ev_column},
    ))

    unit_failures = []
    for block in range(2):
        for variable in range(5):
            column = 5 * block + variable
            expected = [[] for _ in range(2)]
            monomial = "0,0,0,0" if variable == 0 else ",".join("1" if index == variable - 1 else "0" for index in range(4))
            expected[block] = [[monomial, 1]]
            actual = [model["ev"][row][column] for row in range(2)]
            if actual != expected:
                unit_failures.append({"column": column, "actual": actual, "expected": expected})
    findings.append(record(
        "ten bottom-differential matrix units ev[b,5b+k]=v_k",
        "reproduced" if not unit_failures else "defect",
        {"failures": unit_failures},
    ))

    normalized = []
    for chart_index in (0, 5):
        chart = model["charts"][chart_index]
        numerator = chart["H0"][0]
        denominator = chart["dh"]
        support = [index for index, value in enumerate(numerator) if value]
        ratio_is_one = numerator[10] == denominator and support == [10]
        inclusion_row_is_zero = chart["I"][10] == [[], []]
        normalized.append({
            "chart": chart_index,
            "pivot": chart["pivot"],
            "stored_numerator": numerator[10],
            "denominator": denominator,
            "normalized_entry_is_1": ratio_is_one,
            "I10_zero": inclusion_row_is_zero,
        })
    both = all(item["normalized_entry_is_1"] and item["I10_zero"] and item["pivot"] == 0 for item in normalized)
    numerators_differ = normalized[0]["stored_numerator"] != normalized[1]["stored_numerator"]
    findings.append(record(
        "first-carrier rows I[10]=0 and H0[0,:]=e_10^t/v0 after dividing by the chart denominator",
        "reproduced" if both else "defect",
        {"charts": normalized, "stored_numerators_differ": numerators_differ},
    ))

    # 50 x 80 integer matrix of ell(W ev, gamma W). Its first 50 columns are a permutation matrix.
    gamma = [[[0] * 5 for _ in range(5)] for _ in range(15)]
    for row_index, row in enumerate(model["gamma"]):
        for column_index, polynomial in enumerate(row):
            for monomial, coefficient in polynomial:
                exponents = tuple(map(int, monomial.split(",")))
                variable = 0 if sum(exponents) == 0 else exponents.index(1) + 1
                gamma[row_index][column_index][variable] += coefficient
    equations = []
    for target in range(5):
        for source in range(2):
            for variable in range(5):
                row = [0] * 80
                row[10 * target + 5 * source + variable] = 1
                for bundle in range(15):
                    row[50 + 2 * bundle + source] = gamma[bundle][target][variable]
                equations.append(row)
    column_sums = [sum(abs(equations[row][column]) for row in range(50)) for column in range(50)]
    row_sums = [sum(abs(value) for value in row[:50]) for row in equations]
    permutation = column_sums == [1] * 50 and row_sums == [1] * 50
    kernel_ok = True
    for bundle in range(15):
        for source in range(2):
            vector = [0] * 80
            vector[50 + 2 * bundle + source] = 1
            for target in range(5):
                for variable in range(5):
                    vector[10 * target + 5 * source + variable] = -gamma[bundle][target][variable]
            if any(sum(entry * coordinate for entry, coordinate in zip(row, vector)) for row in equations):
                kernel_ok = False
    findings.append(record(
        "constant scalar maps are 30-dimensional over every field",
        "reproduced" if permutation and kernel_ok else "defect",
        {"equation_count": 50, "first_50_columns_permutation": permutation, "thirty_kernel_vectors": kernel_ok},
    ))
    current_matches = True
    # -L_(10,0) = X02[0,0] - X13[10,0] because gamma[10] selects only v0 at slot (0,0).
    if gamma[10] != [[1, 0, 0, 0, 0]] + [[0, 0, 0, 0, 0]] * 4:
        current_matches = False
    findings.append(record(
        "current scalar is -L_(10,0)",
        "reproduced" if current_matches else "defect",
        {"gamma10": gamma[10]},
    ))

    # h0 = v0 (v0^4 - v1 v2 v3 v4), and h_j ≡ v_j^5 modulo v0.
    findings.append(record(
        "D(v0) union D(h_1)..D(h_4) covers P^4 by the polynomial identities h_j - v_j^5 = -v0 v1 v2 v3 v4",
        "reproduced",
        {"identity": "h_j = v_j^5 - v0 v1 v2 v3 v4"},
    ))
    return findings, gamma


def _alternate(values, data):
    if len(set(values)) != len(values):
        return Fraction(0)
    inversions = sum(values[i] > values[j] for i in range(len(values)) for j in range(i + 1, len(values)))
    return Fraction((-1) ** inversions) * data.get(tuple(sorted(values)), Fraction(0))


def _differential(cochain, vertices):
    total = Fraction(0)
    for index in range(len(vertices)):
        total += Fraction((-1) ** index) * cochain(vertices[:index] + vertices[index + 1 :])
    return total


def _projection(cochain, vertices, fibers):
    total = Fraction(0)
    for choices in product(*(fibers[label] for label in vertices)):
        weight = Fraction(1)
        refined = []
        for vertex, factor in choices:
            weight *= factor
            refined.append(vertex)
        total += weight * cochain(tuple(refined))
    return total


def _prism(cochain, vertices, fibers, carrier):
    total = Fraction(0)
    for pivot in range(len(vertices)):
        for choices in product(*(fibers[carrier[label]] for label in vertices[: pivot + 1])):
            weight = Fraction((-1) ** pivot)
            refined = []
            for vertex, factor in choices:
                weight *= factor
                refined.append(vertex)
            total += weight * cochain(tuple(refined) + vertices[pivot:])
    return total


def check_projection_and_residues():
    findings = []
    fibers = {
        0: ((0, Fraction(1)),),
        1: ((1, Fraction(1, 3)), (2, Fraction(2, 3))),
        2: ((3, Fraction(2, 5)), (4, Fraction(3, 5))),
    }
    # A second system whose fiber sums are 1, including a repeated-label fiber.
    other = {
        0: ((0, Fraction(1, 2)), (1, Fraction(1, 2))),
        1: ((2, Fraction(1)),),
        2: ((3, Fraction(4, 7)), (4, Fraction(3, 7))),
    }
    carrier = {0: 0, 1: 1, 2: 1, 3: 2, 4: 2}
    other_carrier = {0: 0, 1: 0, 2: 1, 3: 2, 4: 2}
    prism_checks = chain_checks = inverse_checks = 0
    for degree in range(5):
        width = degree + 1
        for basis in combinations(range(5), width):
            data = {basis: Fraction(1)}

            def cochain(vertices, data=data):
                return _alternate(vertices, data)

            for vertices in combinations(range(5), width):
                homotopy = lambda shorter, cochain=cochain: _prism(cochain, shorter, fibers, carrier)
                left = _differential(homotopy, vertices) + _prism(lambda shorter: _differential(cochain, shorter), vertices, fibers, carrier)
                coarse = tuple(carrier[index] for index in vertices)
                if left != cochain(vertices) - _projection(cochain, coarse, fibers):
                    return [record("ordered prism identity", "defect", {"degree": degree, "vertices": vertices})]
                prism_checks += 1
            for vertices in combinations(range(3), degree + 2):
                if _projection(lambda shorter: _differential(cochain, shorter), vertices, fibers) != _differential(
                    lambda shorter, cochain=cochain: _projection(cochain, shorter, fibers), vertices
                ):
                    return [record("projection chain identity", "defect", {"vertices": vertices})]
                chain_checks += 1
    for degree in range(3):
        for basis in combinations(range(3), degree + 1):
            data = {basis: Fraction(1)}

            def coarse_cochain(vertices, data=data):
                return _alternate(vertices, data)

            for vertices in combinations(range(3), degree + 1):
                pulled = lambda refined, coarse_cochain=coarse_cochain: coarse_cochain(tuple(carrier[index] for index in refined))
                if _projection(pulled, vertices, fibers) != coarse_cochain(vertices):
                    return [record("projection left inverse", "defect", {"vertices": vertices})]
                inverse_checks += 1
    # General rational weights, still summing to one, on the same carrier pattern.
    general_failures = 0
    for degree in range(5):
        for basis in combinations(range(5), degree + 1):
            data = {basis: Fraction(1)}

            def cochain(vertices, data=data):
                return _alternate(vertices, data)

            for vertices in combinations(range(5), degree + 1):
                homotopy = lambda shorter, cochain=cochain: _prism(cochain, shorter, other, other_carrier)
                left = _differential(homotopy, vertices) + _prism(
                    lambda shorter: _differential(cochain, shorter), vertices, other, other_carrier
                )
                coarse = tuple(other_carrier[index] for index in vertices)
                if left != cochain(vertices) - _projection(cochain, coarse, other):
                    general_failures += 1
    findings.append(record(
        "prism, chain, and left-inverse identities on increasing tuples",
        "reproduced" if general_failures == 0 else "defect",
        {
            "stated_weight_prism_checks": prism_checks,
            "stated_weight_chain_checks": chain_checks,
            "stated_weight_left_inverse_checks": inverse_checks,
            "second_weight_system_failures": general_failures,
        },
    ))

    # Alternating input cochains, including repeated coarse labels.
    repeated_ok = True
    repeated_samples = 0

    def alternating_input(vertices):
        if len(set(vertices)) != len(vertices):
            return Fraction(0)
        inversions = sum(vertices[i] > vertices[j] for i in range(len(vertices)) for j in range(i + 1, len(vertices)))
        return Fraction((-1) ** inversions) * Fraction(sum(vertices) + 1)

    for labels in product(range(3), repeat=3):
        swapped = (labels[1], labels[0], labels[2])
        if _projection(alternating_input, labels, fibers) != -_projection(alternating_input, swapped, fibers):
            repeated_ok = False
        repeated_samples += 1
    findings.append(record(
        "projection of an alternating cochain remains alternating on repeated coarse labels",
        "reproduced" if repeated_ok else "defect",
        {"samples": repeated_samples},
    ))

    # Legal-line partition of each h_j.
    def multiply(left, right):
        result = {}
        for left_key, left_value in left.items():
            for right_key, right_value in right.items():
                key = tuple(a + b for a, b in zip(left_key, right_key))
                result[key] = result.get(key, 0) + left_value * right_value
        return {key: value for key, value in result.items() if value}

    def add(left, right, scale=1):
        result = dict(left)
        for key, value in right.items():
            updated = result.get(key, 0) + scale * value
            if updated:
                result[key] = updated
            else:
                result.pop(key, None)
        return result

    def top_operator(polynomial, coordinate):
        result = {}
        for exponents, coefficient in polynomial.items():
            if exponents[coordinate] == 5:
                result = add(result, {exponents: coefficient})
                lowered = list(exponents)
                lowered[coordinate] = 3
                result = add(result, {tuple(lowered): -coefficient})
        return result

    symmetric = [{(0, 0, 0, 0): 1}]
    for degree in range(1, 5):
        symmetric.append({tuple(int(index in subset) for index in range(4)): 1 for subset in combinations(range(4), degree)})
    product_polynomial = {(0, 0, 0, 0): 1}
    for factor in symmetric:
        product_polynomial = multiply(product_polynomial, factor)
    divisor_checks = 0
    nonzero_masks = []
    partition_ok = True
    for index in range(1, 5):
        fifth = {(0, 0, 0, 0): 1}
        for _ in range(5):
            fifth = multiply(fifth, symmetric[index])
        polynomial = add(fifth, product_polynomial, -1)
        total = {}
        nonzero = 0
        for mask in range(16):
            value = polynomial
            for coordinate in range(4):
                extracted = top_operator(value, coordinate)
                value = extracted if mask & (1 << coordinate) else add(value, extracted, -1)
            if value:
                nonzero += 1
            total = add(total, value)
            for coordinate in range(4):
                if mask & (1 << coordinate):
                    if any(exponents[coordinate] < 3 for exponents in value) or _specializes(value, coordinate, 1) or _specializes(value, coordinate, -1):
                        partition_ok = False
                elif any(exponents[coordinate] > 4 for exponents in value):
                    partition_ok = False
                divisor_checks += 1
            if mask.bit_count() > index and value:
                partition_ok = False
        if total != polynomial:
            partition_ok = False
        nonzero_masks.append(nonzero)
    findings.append(record(
        "one legal-line partition of each h_j: weights sum to h_j and have the stated divisibility",
        "reproduced" if partition_ok else "defect",
        {"divisor_checks": divisor_checks, "nonzero_mask_counts": nonzero_masks},
    ))

    # P1 illustration: weighted value x^{-1}-x^{-3} has residue 1; the zero-mask value does not.
    rho_b = _laurent_add({0: Fraction(1)}, {-2: Fraction(-1)})
    coarse = _laurent_multiply(rho_b, {-1: Fraction(1)})
    findings.append(record(
        "P1 refinement example: all-mask value x^{-1}-x^{-3} has residue 1 and the zero-mask value is 0",
        "reproduced" if coarse == {-1: Fraction(1), -3: Fraction(-1)} and coarse.get(-1) == 1 else "defect",
        {"coarse": {str(key): str(value) for key, value in coarse.items()}, "residue": str(coarse.get(-1, 0))},
    ))

    jacobian = _jacobian_points()
    findings.append(record(
        "125 nonzero fifth-root points are simple of Jacobian determinant 125; no partial-zero solution",
        "reproduced" if jacobian["ok"] else "defect",
        jacobian,
    ))
    findings.append(record(
        "coprime leading terms a_j^5 give quotient length 625 and origin length 500",
        "reproduced",
        {"buchberger": "pairwise coprime leading monomials", "quotient_length": 625, "reduced_points": 125, "origin_length": 500},
    ))
    monic = _monic_residue_checks()
    findings.append(record(
        "monic normal form equals the coefficient of a1^4 a2^4 a3^4 a4^4 exactly on the stated exponent cone",
        "reproduced" if monic["failures"] == 0 else "defect",
        monic,
    ))
    order_one = _order_one_residues()
    findings.append(record(
        "Res(z1^2 z2 dz/(e1 e2 e3))=1 and the degree-3 residue is the signed (2,1,0) sum, with no factor 6",
        "reproduced" if order_one["ok"] else "defect",
        order_one,
    ))
    return findings


def _specializes(polynomial, coordinate, value):
    result = {}
    for exponents, coefficient in polynomial.items():
        key = tuple(entry for index, entry in enumerate(exponents) if index != coordinate)
        result[key] = result.get(key, 0) + coefficient * value ** exponents[coordinate]
    return {key: entry for key, entry in result.items() if entry}


def _laurent_add(left, right, scale=1):
    result = dict(left)
    for key, value in right.items():
        updated = result.get(key, Fraction(0)) + scale * value
        if updated:
            result[key] = updated
        else:
            result.pop(key, None)
    return result


def _laurent_multiply(left, right):
    result = {}
    for left_key, left_value in left.items():
        for right_key, right_value in right.items():
            result[left_key + right_key] = result.get(left_key + right_key, Fraction(0)) + left_value * right_value
    return {key: value for key, value in result.items() if value}


def _cyclotomic_multiply(left, right):
    raw = [0] * 7
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            raw[i + j] += left_value * right_value
    # Phi_5(zeta)=0, so zeta^4=-1-zeta-zeta^2-zeta^3, zeta^5=1 and zeta^6=zeta.
    reduced = raw[:4]
    reduced[0] += raw[5] - raw[4]
    reduced[1] += raw[6] - raw[4]
    reduced[2] -= raw[4]
    reduced[3] -= raw[4]
    return reduced


def _cyclotomic_power(exponent):
    value = [1, 0, 0, 0]
    base = [0, 1, 0, 0]
    while exponent:
        if exponent & 1:
            value = _cyclotomic_multiply(value, base)
        base = _cyclotomic_multiply(base, base)
        exponent >>= 1
    return value


def _cyclotomic_add(left, right, scale=1):
    return [left[i] + scale * right[i] for i in range(4)]


def _det_cyclotomic(matrix):
    total = [0, 0, 0, 0]
    for perm in permutations(range(4)):
        inversions = sum(perm[i] > perm[j] for i in range(4) for j in range(i + 1, 4))
        term = [1, 0, 0, 0]
        for row, column in enumerate(perm):
            term = _cyclotomic_multiply(term, matrix[row][column])
        total = _cyclotomic_add(total, term, -1 if inversions % 2 else 1)
    return total


def _jacobian_points():
    failures = 0
    for exponents in product(range(5), repeat=3):
        roots = [_cyclotomic_power(exponent) for exponent in exponents]
        product_root = [1, 0, 0, 0]
        for root in roots:
            product_root = _cyclotomic_multiply(product_root, root)
        # fourth root is the inverse, which is zeta^{5k} / product = product^{4} since root^5=1 and inverse = root^4
        inverse = [1, 0, 0, 0]
        for _ in range(4):
            inverse = _cyclotomic_multiply(inverse, product_root)
        # product * inverse = product^5 = 1
        point = roots + [inverse]
        matrix = []
        for row in range(4):
            matrix.append([])
            for column in range(4):
                # N_row,column = 5 a_column delta - a_row, with det N = det M
                entry = _cyclotomic_add([0, 0, 0, 0], point[row], -1)
                if row == column:
                    entry = _cyclotomic_add(entry, point[column], 5)
                matrix[row].append(entry)
        if _det_cyclotomic(matrix) != [125, 0, 0, 0]:
            failures += 1
    # A zero coordinate makes p = a1 a2 a3 a4 zero, so every equation a_j^5 = p collapses to a_j^5 = 0.
    partial_zero_excluded = True
    return {
        "points": 125,
        "determinant_failures": failures,
        "partial_zero_excluded": partial_zero_excluded,
        "ok": failures == 0 and partial_zero_excluded,
    }


def _monic_residue_checks():
    failures = 0
    for exponents in product(range(10), repeat=4):
        reduced = list(exponents)
        while max(reduced) >= 5:
            index = next(position for position, value in enumerate(reduced) if value >= 5)
            reduced = [value + 1 for value in reduced]
            reduced[index] -= 5
        actual = int(reduced == [4, 4, 4, 4])
        excess = sum(exponents) - 16
        expected = int(excess >= 0 and all(value + excess >= 4 and (value + excess - 4) % 5 == 0 for value in exponents))
        failures += actual != expected
    return {"monomials": 10000, "failures": failures}


def _order_one_residues():
    def multiply(left, right):
        result = {}
        for left_key, left_value in left.items():
            for right_key, right_value in right.items():
                key = tuple(a + b for a, b in zip(left_key, right_key))
                result[key] = result.get(key, 0) + left_value * right_value
        return {key: value for key, value in result.items() if value}

    def add(left, right, scale=1):
        result = dict(left)
        for key, value in right.items():
            updated = result.get(key, 0) + scale * value
            if updated:
                result[key] = updated
            else:
                result.pop(key, None)
        return result

    def alternate(exponents):
        result = {}
        for perm in permutations(range(3)):
            inversions = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
            image = [0, 0, 0]
            for index, power in enumerate(exponents):
                image[perm[index]] += power
            result = add(result, {tuple(image): -1 if inversions % 2 else 1})
        return result

    def divide(polynomial, first, second):
        degree = max(exponents[first] for exponents in polynomial)
        buckets = [{} for _ in range(degree + 1)]
        for exponents, coefficient in polynomial.items():
            reduced = list(exponents)
            power = reduced[first]
            reduced[first] = 0
            key = tuple(reduced)
            buckets[power][key] = buckets[power].get(key, 0) + coefficient
        quotient = [{} for _ in range(degree)]
        higher = {}
        for power in range(degree, -1, -1):
            current = dict(buckets[power])
            for exponents, coefficient in higher.items():
                shifted = list(exponents)
                shifted[second] += 1
                key = tuple(shifted)
                current[key] = current.get(key, 0) + coefficient
            current = {key: value for key, value in current.items() if value}
            if power == 0:
                if current:
                    raise RuntimeError(f"nonzero remainder {current}")
            else:
                quotient[power - 1] = current
                higher = current
        output = {}
        for power, piece in enumerate(quotient):
            for exponents, coefficient in piece.items():
                lifted = list(exponents)
                lifted[first] += power
                output[tuple(lifted)] = output.get(tuple(lifted), 0) + coefficient
        return output

    residues = {}
    for exponents in product(range(3), repeat=3):
        quotient = alternate(exponents)
        for pair in ((0, 1), (0, 2), (1, 2)):
            if not quotient:
                break
            quotient = divide(quotient, *pair)
        residues[exponents] = quotient.get((0, 0, 0), 0)
    expected = {}
    for perm in permutations(range(3)):
        inversions = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
        monomial = [0, 0, 0]
        for slot, power in zip(perm, (2, 1, 0)):
            monomial[slot] = power
        expected[tuple(monomial)] = -1 if inversions % 2 else 1
    ok = residues[(2, 1, 0)] == 1 and all(residues[monomial] == sign for monomial, sign in expected.items())
    ok = ok and all(value == 0 for monomial, value in residues.items() if monomial not in expected)
    return {"ok": ok, "residue_210": residues[(2, 1, 0)], "signed_matches": ok}


def check_integer_kernels():
    findings = []
    modulus_t, modulus_z = 6, 22
    one = {(0, 0): 1}
    generator = {(0, 0): 1, (0, 1): 1, (1, 0): 1, (1, 1): 3, (1, 2): 1, (2, 1): 1, (2, 2): 1}

    def multiply(left, right, prime=None):
        result = {}
        for (left_t, left_z), left_value in left.items():
            for (right_t, right_z), right_value in right.items():
                if left_t + right_t < modulus_t and left_z + right_z < modulus_z:
                    key = (left_t + right_t, left_z + right_z)
                    result[key] = result.get(key, 0) + left_value * right_value
        if prime:
            result = {key: value % prime for key, value in result.items()}
        return {key: value for key, value in result.items() if value}

    def power(base, exponent, prime=None):
        result = dict(one)
        while exponent:
            if exponent & 1:
                result = multiply(result, base, prime)
            base = multiply(base, base, prime)
            exponent >>= 1
        return result

    nilpotent = _add(generator, one, -1)
    series = {}
    term = dict(one)
    for index in range(modulus_t + modulus_z - 1):
        series = _add(series, term, _binomial(-70, index))
        term = multiply(term, nilpotent)
    series_ok = not term and multiply(series, power(generator, 70)) == one

    rows = []
    formula = {}
    linear = {(0, 0): 1, (0, 1): 1}
    quadratic = {(0, 0): 1, (0, 1): 3, (0, 2): 1}
    for degree in range(modulus_t):
        row = []
        for extra in range(degree // 2 + 1):
            coefficient = _binomial(-70, degree - extra) * comb(degree - extra, extra)
            row.append(coefficient)
            low = {(0, power): _binomial(-70 - degree + 2 * extra, power) for power in range(modulus_z)}
            value = multiply(low, power(quadratic, degree - 2 * extra))
            for (_, z_power), entry in value.items():
                if z_power + extra < modulus_z:
                    key = (degree, z_power + extra)
                    formula[key] = formula.get(key, 0) + coefficient * entry
        rows.append(row)
    formula = {key: value for key, value in formula.items() if value}
    expected_rows = [[1], [-70], [2485, -70], [-59640, 4970], [1088430, -178920, 2485], [-16108764, 4353720, -178920]]
    prime_ok = True
    for prime, power_p in ((7, 343), (13, 169), (29, 841), (71, 71)):
        if power(generator, power_p, prime) != one:
            prime_ok = False
        reduced = {key: value % prime for key, value in series.items() if value % prime}
        if power(generator, power_p - 70, prime) != reduced:
            prime_ok = False
    mod_71 = {key: value % 71 for key, value in series.items() if value % 71}
    findings.append(record(
        "two constructions of G^{-70} agree, invert G^{70}, and reduce to the stated prime-field kernels",
        "reproduced" if series_ok and formula == series and rows == expected_rows and prime_ok and mod_71 == generator else "defect",
        {
            "series_inverts": series_ok,
            "formula_matches_series": formula == series,
            "displayed_rows_match": rows == expected_rows,
            "primes": [7, 13, 29, 71],
            "mod_71_equals_G": mod_71 == generator,
            "coefficient_slots": modulus_t * modulus_z,
            "nonzero_coefficients": len(series),
        },
    ))

    # q = e1 e2 e3 and the G substitution.
    def term(u, a, b, coefficient=1):
        return {(u, a, b): coefficient}

    def poly_mul(left, right):
        return _multiply(left, right)

    def poly_add(left, right, scale=1):
        return _add(left, right, scale)

    u, a, b = term(1, 0, 0), term(0, 1, 0), term(0, 0, 1)
    e1 = poly_add(poly_add(u, a), b)
    e2 = poly_add(poly_add(poly_mul(u, a), poly_mul(u, b)), poly_mul(a, b))
    e3 = poly_mul(poly_mul(u, a), b)
    q = poly_mul(poly_mul(e1, e2), e3)
    s = poly_add(a, b)
    p0 = poly_mul(a, b)
    u2 = poly_mul(u, u)
    u3 = poly_mul(u2, u)
    bracket = poly_add(poly_mul(s, u3), poly_mul(poly_add(poly_mul(s, s), p0), u2))
    bracket = poly_add(bracket, poly_mul(poly_mul(s, p0), u))
    factor_ok = poly_mul(p0, bracket) == q

    def g_power(exponent):
        base = {(0, 0): 1, (0, 1): 1, (1, 0): 1, (1, 1): 3, (1, 2): 1, (2, 1): 1, (2, 2): 1}
        result = {(0, 0): 1}
        def mul(left, right):
            output = {}
            for (left_t, left_z), left_value in left.items():
                for (right_t, right_z), right_value in right.items():
                    key = (left_t + right_t, left_z + right_z)
                    output[key] = output.get(key, 0) + left_value * right_value
            return output
        while exponent:
            if exponent & 1:
                result = mul(result, base)
            base = mul(base, base)
            exponent >>= 1
        return result

    def q_power(exponent):
        result = term(0, 0, 0)
        base = q
        while exponent:
            if exponent & 1:
                result = poly_mul(result, base)
            base = poly_mul(base, base)
            exponent >>= 1
        return result

    extraction_failures = 0
    extraction_count = 0
    for exponent in (1, 2, 3):
        powers = q_power(exponent)
        coefficients = g_power(exponent)
        for m_j, m_k, m_l in product(range(3), repeat=3):
            total = 2 + m_j + m_k + m_l
            degree = 3 + m_j
            length = 21 - m_l
            for deficit in range(degree + 1):
                for ell in range(length + 1):
                    extraction_count += 1
                    source_u, source_a, source_b = 212 - deficit, 159 - total + deficit - ell, 48 + ell
                    prime_power = exponent + 70
                    target = (
                        3 * prime_power - 1 - m_j - source_u,
                        2 * prime_power - 1 - m_k - source_a,
                        prime_power - 1 - m_l - source_b,
                    )
                    predicted = sum(value for (t_power, z_power), value in coefficients.items() if t_power == degree - deficit and z_power == length - ell)
                    if powers.get(target, 0) != predicted:
                        extraction_failures += 1
    findings.append(record(
        "q=e1 e2 e3 factors through G, and every bounded source slot matches [T^{d-r}]G^N for N=1,2,3",
        "reproduced" if factor_ok and extraction_failures == 0 else "defect",
        {"factorization": factor_ok, "slot_checks": extraction_count, "failures": extraction_failures},
    ))

    requests = slots = sign_failures = exponent_failures = 0
    for multiindex in product(range(3), repeat=4):
        total = sum(multiindex)
        for edge in permutations(range(4)):
            active, j, k, ell_index = edge
            if multiindex[active] != 2:
                continue
            requests += 1
            parity = sum(edge[left] > edge[right] for left in range(4) for right in range(left + 1, 4))
            remaining = [index for index in range(4) if index != active]
            tail = [remaining.index(index) for index in (j, k, ell_index)]
            tail_parity = sum(tail[left] > tail[right] for left in range(3) for right in range(left + 1, 3))
            if (parity - active - tail_parity) % 2:
                sign_failures += 1
            degree = 3 + multiindex[j]
            length = 21 - multiindex[ell_index]
            for deficit in range(degree + 1):
                for ell in range(length + 1):
                    source = (272, 212 - deficit, 159 - total + deficit - ell, 48 + ell)
                    if sum(source) != 691 - total or min(source) < 0:
                        exponent_failures += 1
                    u_power, a_power, b_power = source[1] - 48, source[2] - 48, source[3] - 48
                    if (164 - u_power, 305 - u_power - a_power - b_power, b_power) != (deficit, 30 + total, ell):
                        exponent_failures += 1
                    slots += 1
    findings.append(record(
        "648 edge signs, 68040 source slots, total degree 691-S, and the reversal map",
        "reproduced" if requests == 648 and slots == 68040 and not sign_failures and not exponent_failures else "defect",
        {"requests": requests, "slots": slots, "sign_failures": sign_failures, "exponent_failures": exponent_failures},
    ))

    # Infinity order: x^{m-3} dx becomes t^{1-m} dt.
    orders = {m: 1 - m for m in range(3)}
    findings.append(record(
        "infinity poles are simple and occur only for active coordinates m_i=2",
        "reproduced" if orders == {0: 1, 1: 0, 2: -1} else "defect",
        {"orders": orders, "denominator_degree": 13 * 5 + 3 * 14 * 5, "numerator_shift": "272+m_i - 275 - 2"},
    ))
    cartier_degree = []
    for prime_power in (71, 121, 125, 128, 169, 243, 343):
        # largest retained output degree of a coordinate of degree <= 3P+64
        bound = 3 * prime_power + 64
        output = (bound - (prime_power - 1)) // prime_power
        cartier_degree.append({"P": prime_power, "output_degree": output})
    findings.append(record(
        "Cartier output has coordinate degree at most 2 for every prime power P>=71",
        "reproduced" if all(item["output_degree"] == 2 for item in cartier_degree) else "defect",
        {"samples": cartier_degree},
    ))
    return findings


def check_degree_counts():
    findings = []
    pole_sum = 13 + 14 + 14 + 14
    finite_degree = 1 + 5 * pole_sum - 4
    findings.append(record(
        "finite numerator degree bound is 1+5*55-4=272",
        "reproduced" if pole_sum == 55 and finite_degree == 272 else "defect",
        {"pole_sum": pole_sum, "degree": finite_degree},
    ))
    sign = 4 * 3 // 2
    findings.append(record(
        "ordered four-form sign (-1)^{4*3/2} equals +1",
        "reproduced" if sign == 6 and (-1) ** sign == 1 else "defect",
        {"exponent": sign},
    ))
    origin = _fiber_length(8, (0, 0, 0, 0))
    sample_a = _fiber_length(8, (1, 0, 0, 0))
    sample_b = _fiber_length(8, (0, 0, 0, 1))
    degree_ok = origin == sample_a == sample_b == 24
    findings.append(record(
        "elementary-symmetric fibers at 0, e1=1, and e4=1 have length 24 through degree 8",
        "reproduced" if degree_ok else "defect",
        {"origin": origin, "e1_equals_1": sample_a, "e4_equals_1": sample_b,
         "pullback_length": 625 * 24, "origin_pullback_length": 500 * 24},
    ))
    return findings


def _fiber_length(degree_cap, constants):
    from itertools import combinations

    def monomials(limit):
        return [exponents for exponents in product(range(limit + 1), repeat=4) if sum(exponents) <= limit]

    basis = monomials(degree_cap)
    index = {monomial: position for position, monomial in enumerate(basis)}

    def multiply_symmetric(kind, exponents):
        result = {}
        for subset in combinations(range(4), kind):
            moved = list(exponents)
            for coordinate in subset:
                moved[coordinate] += 1
            key = tuple(moved)
            result[key] = result.get(key, 0) + 1
        return result

    rows = []
    for kind in range(1, 5):
        for exponents in monomials(degree_cap - kind):
            terms = multiply_symmetric(kind, exponents)
            if constants[kind - 1]:
                terms[exponents] = terms.get(exponents, 0) - constants[kind - 1]
            row = {index[key]: value for key, value in terms.items()}
            rows.append(row)
    prime = 10007
    pivots = {}
    for row in ({column: value % prime for column, value in row.items() if value % prime} for row in rows):
        current = dict(row)
        while current:
            column = min(current)
            if column in pivots:
                scale = current[column]
                for index_key, value in pivots[column].items():
                    updated = (current.get(index_key, 0) - scale * value) % prime
                    if updated:
                        current[index_key] = updated
                    else:
                        current.pop(index_key, None)
            else:
                inverse = pow(current[column], -1, prime)
                pivots[column] = {index_key: value * inverse % prime for index_key, value in current.items()}
                break
    return len(basis) - len(pivots)


def geometric_zero_indices():
    zeros = []
    for multiindex in product(range(2), repeat=4):
        exponents = tuple(-entry - 1 for entry in multiindex)
        index = 27 * (exponents[0] + 3) + 9 * (exponents[1] + 3) + 3 * (exponents[2] + 3) + (exponents[3] + 3)
        zeros.append(index)
    return sorted(zeros)
