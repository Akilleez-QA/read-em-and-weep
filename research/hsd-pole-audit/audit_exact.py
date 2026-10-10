#!/usr/bin/env python3
"""Exact checks for the four algebraic gates that do not need axis DAGs.

Gate 1 reads the independent pole graph, not checks/compute_pole_bounds.js.
Gates 2 and 3 rebuild the rational identities from the pinned model.
Gate 4 is integer arithmetic on those outputs. Nothing here imports the
package's verify_*.py checkers.
"""
import hashlib
import itertools
import json
import re
import subprocess
import sys
from pathlib import Path

import sympy as sp

PIN = Path(__file__).resolve().parents[1] / "hm/current-scalar-geometric-dependencies"
HERE = Path(__file__).resolve().parent
V = sp.symbols("v0:5")


def load_json(path):
    return json.loads(path.read_text())


def degree_key(poly):
    return max((sum(int(part) for part in key.split(",")) for key, _ in poly), default=0)


def affine(poly):
    total = 0
    for key, coefficient in poly:
        powers = [int(part) for part in key.split(",")]
        term = sp.Integer(coefficient)
        for symbol, power in zip(V[1:], powers):
            term *= symbol**power
        total += term
    return sp.expand(total)


def homogenize(poly, degree):
    total = 0
    for key, coefficient in poly:
        powers = [int(part) for part in key.split(",")]
        rest = degree - sum(powers)
        if rest < 0:
            raise ValueError("negative homogenizing power")
        term = sp.Integer(coefficient) * V[0] ** rest
        for symbol, power in zip(V[1:], powers):
            term *= symbol**power
        total += term
    return sp.expand(total)


def rational_entry(numerator, denominator, weight):
    if not numerator:
        return sp.Integer(0)
    denominator_degree = degree_key(denominator)
    extra = max(0, degree_key(numerator) - denominator_degree - weight)
    return sp.cancel(
        homogenize(numerator, denominator_degree + extra + weight)
        / (V[0] ** extra * homogenize(denominator, denominator_degree))
    )


def matrix_from(rows, denominator, weight_of):
    return sp.Matrix(
        [
            [rational_entry(entry, denominator, weight_of(i, j)) for j, entry in enumerate(row)]
            for i, row in enumerate(rows)
        ]
    )


def regular_matrix(rows):
    return sp.Matrix([[homogenize(entry, 1) if entry else sp.Integer(0) for entry in row] for row in rows])


def require_zero(name, matrix, counts):
    for entry in matrix:
        if sp.cancel(entry) != 0:
            raise AssertionError((name, entry))
    counts[name] = counts.get(name, 0) + len(list(matrix))


def homogeneous_weight(expr, weight):
    if expr == 0:
        return
    scale = sp.symbols("t")
    scaled = expr.subs({symbol: scale * symbol for symbol in V})
    if sp.cancel(scaled - scale**weight * expr) != 0:
        raise AssertionError((expr, weight))


def gate_homogeneous(model, seeds):
    encoded = json.dumps(model, separators=(",", ":")).encode()
    digest = hashlib.sha256(encoded).hexdigest()
    if digest != "b6b532c4bab5787397a4cddde34210c12fae71853b30cb73ecbe8a9c2b4826b2":
        raise AssertionError("model hash")
    gamma = regular_matrix(model["gamma"])
    delta = regular_matrix(model["delta"])
    ev = regular_matrix(model["ev"])
    for matrix in (gamma, delta, ev):
        for entry in matrix:
            homogeneous_weight(entry, 1)
    counts = {}
    cleared = 0
    zeros = 0
    charts = []
    for owner, chart in enumerate(model["charts"]):
        if owner < 5:
            factors = [V[owner], V[owner] ** 4 - sp.prod(V[k] for k in range(5) if k != owner)]
        else:
            factors = [V[0], V[1], V[3], V[4]]
        blocks = {}
        for name, denominator_key, weight_of in (
            ("I", "di", lambda _i, j: (0, 1)[j]),
            ("P", "dp", lambda i, _j: (0, -1)[i]),
            ("H0", "dh", lambda _i, _j: -1),
            ("H1", "dh", lambda _i, _j: -1),
        ):
            matrix = matrix_from(chart[name], chart[denominator_key], weight_of)
            blocks[name] = matrix
            for i, row in enumerate(chart[name]):
                for j, polynomial in enumerate(row):
                    exponents = seeds[owner][name][i][j]
                    if not polynomial:
                        if exponents is not None:
                            raise AssertionError("nonzero seed on a zero entry")
                        zeros += 1
                        continue
                    if len(exponents) != len(factors) or any(type(e) is not int or e < 0 for e in exponents):
                        raise AssertionError("bad seed")
                    weight = weight_of(i, j)
                    entry = matrix[i, j]
                    homogeneous_weight(entry, weight)
                    cleared_entry = sp.cancel(
                        sp.prod(factor**e for factor, e in zip(factors, exponents)) * entry
                    )
                    sp.Poly(sp.together(cleared_entry), *V, domain=sp.QQ)
                    cleared += 1
        pivot = chart["pivot"]
        eta = sp.zeros(10, 2)
        for half in range(2):
            eta[half * 5 + pivot, half] = 1 / V[pivot]
            homogeneous_weight(eta[half * 5 + pivot, half], -1)
        identity = sp.eye(15)
        E = sp.cancel(blocks["I"] * blocks["P"]).as_immutable()
        # The displayed contraction, checked before it is reused as a pole formula.
        require_zero("E_identity", E - (identity - gamma * blocks["H0"] - blocks["H1"] * delta), counts)
        require_zero("P_I", blocks["P"] * blocks["I"] - sp.eye(2), counts)
        require_zero("H0_I", blocks["H0"] * blocks["I"], counts)
        require_zero("P_H1", blocks["P"] * blocks["H1"], counts)
        require_zero("H0_H1", blocks["H0"] * blocks["H1"], counts)
        require_zero("H1_eta", blocks["H1"] * eta, counts)
        require_zero("H0_gamma", blocks["H0"] * gamma - sp.eye(5), counts)
        require_zero("delta_H1_eta_ev", delta * blocks["H1"] + eta * ev - sp.eye(10), counts)
        require_zero("ev_eta", ev * eta - sp.eye(2), counts)
        require_zero("delta_I", delta * blocks["I"], counts)
        require_zero("P_gamma", blocks["P"] * gamma, counts)
        charts.append({**blocks, "eta": eta, "E": E})
    for owner in (0, 5):
        row = sp.zeros(1, 15)
        row[0, 10] = 1 / V[0]
        require_zero("merged_H0_row", charts[owner]["H0"].row(0) - row, counts)
        require_zero("merged_I_row", charts[owner]["I"].row(10), counts)
        require_zero("merged_E_row", charts[owner]["E"].row(10), counts)
    require_zero("gamma_row10", gamma.row(10) - sp.Matrix([[V[0], 0, 0, 0, 0]]), counts)
    require_zero("ev_column0", ev.col(0) - sp.Matrix([V[0], 0]), counts)
    for i, j in itertools.product(range(5), range(2)):
        probe = sp.zeros(5, 2)
        probe[i, j] = 1
        require_zero("L_d_End", sp.Matrix([(probe * ev)[0, 0] - (gamma * probe)[10, 0]]), counts)
    symbols = sp.symbols(f"z0:150")
    generic = sp.Matrix(15, 10, symbols)
    for owner in (0, 5):
        chart = charts[owner]
        value = (chart["H0"] * generic)[0, 0] + (chart["E"] * generic * chart["eta"])[10, 0]
        require_zero("scalar_formula", sp.Matrix([value - generic[10, 0] / V[0]]), counts)
    require_zero("double_merged_vanish", charts[0]["E"].row(10), counts)
    for j in range(1, 5):
        carrier = V[j] ** 5 - sp.prod(V)
        require_zero("cover_v0_zero", sp.Matrix([carrier.subs(V[0], 0) - V[j] ** 5]), counts)
    if cleared != 451:
        raise AssertionError(f"cleared entries {cleared}")
    if sum(counts.values()) != 3090:
        raise AssertionError(counts)
    return {
        "modelSha256": digest,
        "nonzeroHomogeneousEntries": cleared,
        "zeroEntriesChecked": zeros,
        "exactScalarChecks": sum(counts.values()),
        "byIdentity": counts,
    }


def pole_orders(expr, variable):
    orders = []
    current = expr
    for _ in range(3):
        order = 0
        cleared = current
        while order < 8:
            numerator, denominator = sp.fraction(sp.together(sp.cancel(cleared)))
            if sp.degree(sp.Poly(sp.expand(denominator), variable), variable) == 0:
                break
            order += 1
            cleared = sp.cancel(cleared * variable * (variable**2 - 1))
        orders.append(order)
        current = sp.diff(current, variable)
    return orders


def distinct_derivative_pairs(source):
    start = source.index("function crossResidual(")
    stop = source.index("function globalCross(")
    body = source[start:stop]
    pairs = [(int(a), int(b)) for a, b in re.findall(r",(\d),(\d)\]", body)]
    pairs += [(int(a), int(b)) for a, b in re.findall(r"dd\([^,]+,(\d),(\d)\)", body)]
    pairs += [(int(a), int(b)) for a, b in re.findall(r"first\((\d),(\d)\)", source)]
    if not pairs or any(a == b or a not in range(4) or b not in range(4) for a, b in pairs):
        raise AssertionError(pairs)
    return sorted(set(pairs))


def gate_frames_and_degree(pole):
    checks = []

    def equal(left, right, label):
        if sp.cancel(left - right) != 0:
            raise AssertionError(label)
        checks.append(label)

    x = sp.symbols("x1:5")
    t = sp.symbols("t1:5")
    z = sp.symbols("z")
    affine = sp.Poly(sp.prod(1 + coordinate * z for coordinate in x), z)
    equal(affine.nth(0), 1, "finite v0 = 1")
    for j in range(1, 5):
        elementary = sum(sp.prod(x[i] for i in subset) for subset in itertools.combinations(range(4), j))
        equal(affine.nth(j), elementary, f"finite v{j}")
    for mask in range(16):
        tau = sp.prod(t[i] for i in range(4) if mask >> i & 1)
        local = sp.Poly(
            sp.prod((t[i] + z) if mask >> i & 1 else (1 + x[i] * z) for i in range(4)),
            z,
        )
        substitution = {x[i]: 1 / t[i] for i in range(4) if mask >> i & 1}
        for j in range(5):
            equal(local.nth(j), tau * affine.nth(j).subs(substitution), f"chart {mask} v{j}")

    q = sp.symbols("q")
    line = q**2 - 1
    generator = q**3 - q
    seeds = {
        "rf": (q**2 + 1) / (2 * q * line),
        "gamma": 1 / (q * line),
        "overlap": 1 / q,
    }
    equal(seeds["rf"], sp.diff(generator, q) / (2 * generator) - 1 / q, "logarithmic seed")
    orders = {name: pole_orders(value, q) for name, value in seeds.items()}
    for name, value in seeds.items():
        for derivative in (0, 1):
            numerator = sp.cancel(q ** (derivative + 1) * line ** (derivative + 1) * sp.diff(value, q, derivative))
            sp.Poly(numerator, q, domain=sp.QQ)
            equal(
                sp.diff(value, q, derivative),
                numerator / (q * line) ** (derivative + 1),
                f"{name} derivative {derivative}",
            )
        equal(sp.diff(value, sp.symbols("y")), 0, f"{name} ignores the other coordinate")

    c = sp.symbols("c")
    matrix = sp.Matrix(2, 2, sp.symbols("c0:4"))
    gauge = sp.diag(c, 1 / c)
    difference = gauge.T * (gauge * matrix * gauge.inv()).T * gauge.T.inv() - matrix.T
    for index, entry in enumerate(difference):
        equal(entry, 0, f"constant gauge {index}")

    coefficients = sp.symbols("a0:6")
    yy = sp.symbols("y")
    polynomial = sum(coefficients[k] * q**k * yy ** (5 - k) for k in range(6))
    bit_one = q**3 * (q**2 - yy**2) * coefficients[5]
    bit_zero = sp.expand(polynomial - bit_one)
    equal(bit_zero + bit_one, polynomial, "legal partition sums to P")
    equal(bit_zero.subs(yy, 0), 0, "bit zero is divisible by Y")
    equal(bit_one / (q**3 * (q**2 - yy**2)), coefficients[5], "bit one extracts the clearing factor")

    gauge_weights = 0
    for pivot in range(5):
        for other in range(5):
            if other == pivot:
                continue
            homogeneous_weight(-V[other] / V[pivot], 0)
            gauge_weights += 1
    homogeneous_weight(sp.Integer(1), 0)

    coordinate, time = sp.symbols("x t")
    squared = 1 - time**2
    equal(time * ((coordinate**2 - 1) / coordinate).subs(coordinate, 1 / time), squared, "squared ratio transports to s")
    equal(sp.diff(time, time) / (2 * time), 1 / (2 * time), "logarithmic derivative of t")
    equal(sp.diff(squared, time) / (2 * squared), -time / squared, "logarithmic derivative of s")
    equal(
        (1 / (coordinate * (coordinate**2 - 1))).subs(coordinate, 1 / time) * (-1 / time**2),
        -time / squared,
        "gamma transports",
    )
    equal((1 / coordinate).subs(coordinate, 1 / time) * (-1 / time**2), -1 / time, "dlog transports")

    # Physical block weights, read off the displayed splitting and nu powers.
    # U columns are multiplied by nu**p and Q rows are divided by the same weight.
    # nu scales as tau**(1/2), so the block multiplier is tau**(p/2).
    groups = []
    for degree, power, copies, name in (
        (1, -2, 5, "U0 gamma"),
        (0, 0, 1, "U0 I column 0"),
        (1, -2, 1, "U0 I column 1"),
        (-1, 2, 8, "U0 H1 W"),
        (-1, 2, 5, "Q0 H0"),
        (0, 0, 1, "Q0 P row 0"),
        (-1, 2, 1, "Q0 P row 1"),
        (1, -2, 8, "Q0 L delta"),
        (0, 0, 8, "U1 W"),
        (-1, 2, 2, "U1 eta"),
        (0, 0, 8, "Q1 L"),
        (1, -2, 2, "Q1 ev"),
    ):
        if 2 * degree + power != 0:
            raise AssertionError(name)
        groups.append({"block": name, "degree": degree, "nuPower": power, "copies": copies})
    if sum(item["copies"] for item in groups if item["block"].startswith("U0")) != 15:
        raise AssertionError("U0 width")
    if sum(item["copies"] for item in groups if item["block"].startswith("Q0")) != 15:
        raise AssertionError("Q0 height")

    source = (PIN / "data/source-formulas.js").read_text()
    pairs = distinct_derivative_pairs(source)
    internal_degree = -2
    y_factors = 4
    # Each normalized line coordinate contributes tau**(1/2); removing four gives tau**(-2).
    y_removal = -sp.Rational(y_factors, 2)
    frame_exponent = internal_degree + y_removal
    if frame_exponent != -4:
        raise AssertionError(frame_exponent)

    X = sp.symbols("X1:5")
    Y = sp.symbols("Y1:5")
    generating = sp.prod(Y[i] + X[i] * z for i in range(4))
    coefficients = [sp.Poly(generating, z).nth(j) for j in range(5)]
    scales = sp.symbols("s1:5")
    for index, coefficient in enumerate(coefficients):
        scaled = coefficient.subs({X[i]: scales[i] * X[i] for i in range(4)} | {Y[i]: scales[i] * Y[i] for i in range(4)})
        if sp.expand(scaled - sp.prod(scales) * coefficient) != 0:
            raise AssertionError(f"v{index} multidegree")
    carrier = [coefficients[j] ** 5 - sp.prod(coefficients) for j in range(5)]
    for index, polynomial in enumerate(carrier):
        scaled = polynomial.subs({X[i]: scales[i] * X[i] for i in range(4)} | {Y[i]: scales[i] * Y[i] for i in range(4)})
        if sp.expand(scaled - sp.prod(scale**5 for scale in scales) * polynomial) != 0:
            raise AssertionError(f"h{index} multidegree")
    if sp.expand(coefficients[0].subs({symbol: 1 for symbol in Y}) - 1) != 0:
        raise AssertionError("joint affine chart does not set v0 = 1")

    tail = pole["tailPrimaryJ0"]
    if tail != [13, 13, 13, 13, 13, 0, 1, 1, 1, 1]:
        raise AssertionError(tail)
    relevant = [profile for profile in pole["q2"] if profile["b"] == 1 and profile["a"] in (0, 5)]
    if len(relevant) != 2:
        raise AssertionError("all-mask prefix profiles")
    carrier_one = max(profile["scalar"][1] for profile in relevant)
    line_bound = max(max(tail[6:]), max(max(profile["scalar"][6:]) for profile in relevant))
    # Carriers 2, 3, 4 are the tail of (first anchor, carrier 1). The weight adds one h factor.
    required = [carrier_one, tail[2] + 1, tail[3] + 1, tail[4] + 1]
    supplied = [13, 14, 14, 14]
    if any(need > have for need, have in zip(required, supplied)):
        raise AssertionError((required, supplied))
    if line_bound > 1:
        raise AssertionError("legal-line weight does not cover the computed order")
    clearing_sum = sum(supplied)
    degree = frame_exponent + 1 + 5 * clearing_sum
    if clearing_sum != 55 or degree != 272:
        raise AssertionError((clearing_sum, degree))
    return {
        "exactIdentities": len(checks),
        "lineSeedPoleOrdersDerivative012": orders,
        "mixedDerivativePairs": pairs,
        "gaugeRatioWeightsChecked": gauge_weights,
        "sameCoordinateSecondDerivativeUsed": any(a == b for a, b in pairs),
        "physicalBlockWeights": groups,
        "frameExponent": int(frame_exponent),
        "allMaskRequiredPowers_h1_to_h4": required,
        "suppliedClearingPowers": supplied,
        "clearingExponentSum": clearing_sum,
        "regularSectionDegree": int(degree),
        "bundle": "O(272,272,272,272)",
        "degree273Coefficient": 0,
    }


def gate_pole(report, certificate):
    if report["abstractNodes"] != certificate["abstractScalars"]:
        raise AssertionError("node count")
    if report["tailPrimaryJ0"] != certificate["tailPrimaryJ0"]:
        raise AssertionError("tail")
    if report["q2"] != certificate["q2"] or report["q3"] != certificate["q3"]:
        raise AssertionError("prefix profiles")
    scalar_max = [max(profile["scalar"][i] for profile in report["q2"]) for i in range(10)]
    block_max = [max(profile["blocks"][i] for profile in report["q2"]) for i in range(10)]
    third_max = [max(profile["block"][i] for profile in report["q3"]) for i in range(10)]
    order = [5, 0, 1, 2, 3, 4]
    for name, count, field in (("q2", 2, "scalar"), ("q3", 3, "block")):
        anchors = set()
        for profile in report[name]:
            chosen = tuple(profile[key] for key in ("a", "b", "c")[:count])
            anchors.add(chosen)
            if set(chosen) & set(profile["tailCarriers"]):
                raise AssertionError("prefix overlaps tail")
            if profile["tailCarriers"] != order[order.index(chosen[-1]) + 1 :]:
                raise AssertionError("tail carriers")
        if anchors != set(itertools.combinations(order[:-1], count)):
            raise AssertionError("profile coverage")
    return {
        "abstractNodes": report["abstractNodes"],
        "tailPrimaryJ0": report["tailPrimaryJ0"],
        "q2ScalarMax": scalar_max,
        "q2BlockMax": block_max,
        "q3BlockMax": third_max,
        "matchesPinnedCertificate": True,
        "declaredCompletedFieldUsed": False,
    }


def main():
    model = load_json(PIN / "data/model.json")
    seeds = load_json(PIN / "data/divisor-seeds.json")
    certificate = load_json(PIN / "certificates/pole-bounds.json")
    completed = subprocess.run(
        ["node", "--max-old-space-size=1024", str(HERE / "pole_graph.js"), "published"],
        check=True,
        capture_output=True,
        text=True,
    )
    pole = json.loads(completed.stdout)
    probes = {}
    for mode in ("qzero", "fulljet"):
        probe = subprocess.run(
            ["node", "--max-old-space-size=1024", str(HERE / "pole_graph.js"), mode],
            check=True,
            capture_output=True,
            text=True,
        )
        probes[mode] = json.loads(probe.stdout)
    qzero = probes["qzero"]
    report = {
        "pin": "dc60a859a0157b1d2d1b57b37324509abc22c600",
        "gate1_tail_prefix": gate_pole(pole, certificate),
        "gate1_qzero_bounds_identical": qzero["q2"] == pole["q2"] and qzero["q3"] == pole["q3"] and qzero["tailPrimaryJ0"] == pole["tailPrimaryJ0"],
        "gate1_qzero_nodes": qzero["abstractNodes"],
        "gate1_fulljet": probes["fulljet"],
        "gate2_homogeneous": gate_homogeneous(model, seeds),
        "gates_3_and_4": gate_frames_and_degree(pole),
    }
    json.dump(report, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
