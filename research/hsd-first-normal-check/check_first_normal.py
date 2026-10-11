#!/usr/bin/env python3
"""Exact recheck of the first-normal claims in §5.1 at ec02aa73.

Arithmetic is rational. Nothing is read from the plane-completion tree:
the transition is rebuilt from the plane polynomials, the quotient
projection, and the mixed cocycle. The form identity is checked after
that derivation.

Pinned object:
  commit ec02aa73e875dddf092439655aad1233d5d884e5
  research/carrier/plane-completion-lemma/EXPLICIT_BASE_ISOMETRY.md
  sha256 d87e41b13d26fcfb32e1673e43c869d56c8bb10496d07a6b0c227e7f72a280e3
"""

from __future__ import annotations

import functools
import json
import sys

import sympy as sp

X, Y, W, z = sp.symbols("X Y W z")
S = X**2 + Y**2
F = X * Y
a = X**3 + Y**3
w = W**6

# C is the exact quotient (S^3 - z^3 W^6) / g, not a copied polynomial.
_g_open = S - z * W**2
_C_raw = sp.together(sp.cancel((S**3 - z**3 * w) / _g_open))
_C_num, _C_den = sp.fraction(sp.together(_C_raw))
if sp.expand(_C_den - 1) != 0:
    raise RuntimeError("C is not a polynomial")
C = sp.expand(_C_num)
g = _g_open
T = sp.expand(sp.cancel((a**2 - S**3) / F**2))

PIN = "ec02aa73e875dddf092439655aad1233d5d884e5"
NOTE_SHA256 = "d87e41b13d26fcfb32e1673e43c869d56c8bb10496d07a6b0c227e7f72a280e3"

# Filtration bidegrees (base, plane) of (P, E0, E1, E2), from the triangular
# frame whose base transitions are the diagonal of T_B.
B_BASE = (3, 0, 4, 3)
B_PLANE = (-3, 0, -4, -4)
I_BASE, I_PLANE = 0, -1
A_BASE, A_PLANE = 3, -6
D_BASE, D_PLANE = 1, 1


def _gb(gens, variables):
    return list(
        sp.groebner(
            [sp.expand(h) for h in gens],
            *variables,
            order="grlex",
            field=True,
        )
    )


def _membership_remainder(poly, gens, variables):
    basis = _gb(gens, variables)
    _, remainder = sp.reduced(sp.expand(poly), basis, *variables)
    return sp.expand(remainder)


def colon_generators(gens, element, variables):
    """Generators of (gens) : (element), via elimination of the intersection."""
    t = sp.symbols("t")
    mixed = [t * sp.expand(h) for h in gens] + [sp.expand((1 - t) * element)]
    eliminated = sp.groebner(mixed, t, *variables, order="lex", field=True)
    element_e = sp.expand(element)
    column = []
    for poly in eliminated:
        if t in poly.free_symbols:
            continue
        poly = sp.expand(poly)
        if poly == 0:
            continue
        quotients, remainder = sp.reduced(poly, [element_e], *variables)
        if sp.expand(remainder) != 0:
            raise RuntimeError(f"{poly} lies in the intersection but is not divisible by {element}")
        column.append(sp.expand(quotients[0]))
    return [item for item in column if item != 0]


def colon_extras(gens, element, variables):
    """Remainder witnesses that (gens):(element) is strictly larger than (gens)."""
    column = colon_generators(gens, element, variables)
    extras = []
    for poly in column:
        remainder = _membership_remainder(poly, gens, variables)
        if remainder != 0:
            extras.append(remainder)
    return extras


def contained(small, big, variables):
    for poly in small:
        if _membership_remainder(poly, big, variables) != 0:
            return False
    return True


def is_regular_sequence(elements, variables):
    """Successive colon test. Returns (ok, failing_step or None, extras)."""
    if any(sp.expand(element) == 0 for element in elements):
        return False, 0, [sp.Integer(0)]
    running = []
    for index, element in enumerate(elements):
        if index == 0:
            running = [element]
            continue
        extras = colon_extras(running, element, variables)
        if extras:
            return False, index, extras
        running = running + [element]
    return True, None, []


def plane_degrees(expr):
    """Total degrees in (X, Y, W), with z treated as a base coordinate."""
    polynomial = sp.Poly(sp.expand(expr), X, Y, W)
    if polynomial == 0:
        return set()
    return {sum(monomial) for monomial in polynomial.monoms()}


def h1_dimension(base, plane):
    """dim H^1(P1 x P2, O(base, plane)) by Künneth and Bott.

    H^1(P2, O(any)) = 0. H^1(P1, O(a)) is -a-1 for a <= -2 and 0 otherwise.
    H^0(P2, O(b)) is binom(b+2, 2) for b >= 0 and 0 otherwise.
    """
    h1_p1 = (-base - 1) if base <= -2 else 0
    h0_p2 = int(sp.binomial(plane + 2, 2)) if plane >= 0 else 0
    h1_p2 = 0
    h0_p1 = (base + 1) if base >= 0 else 0
    return h1_p1 * h0_p2 + h0_p1 * h1_p2


def _assert_poly_identities():
    if sp.expand(g * C + z**3 * w - S**3) != 0:
        raise RuntimeError("division identity for C failed")
    if sp.expand(C - (S**2 + z * S * W**2 + z**2 * W**4)) != 0:
        raise RuntimeError("C does not match the expanded quotient")
    if sp.expand(T - (-3 * S + 2 * F)) != 0:
        raise RuntimeError("T does not match -3S+2F")
    if sp.expand(a**2 - S**3 - T * F**2) != 0:
        raise RuntimeError("infinity numerator identity failed")
    if sp.expand(a**2 - g * C - z**3 * w - T * F**2) != 0:
        raise RuntimeError("finite numerator identity failed")


def relation(infinity=False):
    if infinity:
        return sp.Matrix([-a, S**3, -g / z, F])
    return sp.Matrix([-a, w, -g, F])


@functools.lru_cache(maxsize=1)
def transition_matrix():
    """Infinity-to-finite B transition. The off-diagonal entry is solved."""
    unknown = sp.symbols("u")
    matrix = sp.diag(z**3, sp.Integer(1), z**4, z**3)
    matrix[1, 2] = unknown
    residual = sp.simplify(matrix * relation(True) - z**3 * relation(False))
    solution = sp.solve([sp.expand(sp.together(entry)) for entry in residual], unknown)
    if unknown not in solution:
        raise RuntimeError(f"T_B off-diagonal is not determined: {residual}")
    matrix[1, 2] = sp.expand(solution[unknown])
    if sp.expand(matrix[1, 2] - z * C) != 0:
        raise RuntimeError("solved T_B[E0,E1] is not z C")
    if sp.simplify(matrix * relation(True) - z**3 * relation(False)) != sp.zeros(4, 1):
        raise RuntimeError("T_B r_infinity != z^3 r_finite")
    return matrix


def omega_e(r_components):
    r1, r2, r3 = r_components
    block = sp.zeros(3)
    block[0, 1] = r3
    block[0, 2] = -r2
    block[1, 2] = r1
    return block - block.T


def solve_b_vector(r_components, i, j):
    """Particular solution of Ω_E b = ψ_j - ψ_i supported on the third leg."""
    third = ({0, 1, 2} - {i, j}).pop()
    psi_diff = sp.zeros(3, 1)
    psi_diff[j] = a / r_components[j]
    psi_diff[i] -= a / r_components[i]
    coefficient = sp.symbols("t")
    vector = coefficient * sp.eye(3)[:, third]
    equations = list(sp.simplify(omega_e(r_components) * vector - psi_diff))
    solved = sp.solve(equations, coefficient)
    if coefficient not in solved:
        raise RuntimeError(f"no supported b for pair {(i, j)}")
    vector = vector.subs(coefficient, solved[coefficient])
    if sp.simplify(omega_e(r_components) * vector - psi_diff) != sp.zeros(3, 1):
        raise RuntimeError("solved b misses Ω b = ψ_j - ψ_i")
    return sp.Matrix(vector)


def central_scalars(infinity=False):
    """Partial-fraction splitting of -a^2 / (r1 r2 r3)."""
    r_components = relation(infinity)[1:4, 0]
    r1, r2, r3 = r_components
    target = sp.together(-a**2 / (r1 * r2 * r3))
    if infinity:
        # a^2 = S^3 + T F^2 and r2 = -g/z, so the two nonzero overlaps are explicit.
        c12 = sp.together(-T * F / (r1 * r2))
        c23 = sp.together(-1 / (r2 * r3))
        c31 = sp.Integer(0)
    else:
        c12 = sp.together(T * F / (w * g))
        c23 = sp.together(z**3 / (g * F))
        c31 = sp.together(C / (w * F))
    if sp.simplify(sp.together(c12 + c23 + c31 - target)) != 0:
        raise RuntimeError(f"central sum fails (infinity={infinity})")
    return {(0, 1): c12, (1, 2): c23, (2, 0): c31}


def forward_transition(infinity, pair):
    """5×5 map sending q_j to q_i + b_ij + c_ij P. Inverse pairs use the shear inverse."""
    i, j = pair
    if i == j:
        return sp.eye(5)
    forward = (i, j) in {(0, 1), (1, 2), (2, 0)}
    if not forward:
        return forward_transition(infinity, (j, i)).inv()
    r_components = list(relation(infinity)[1:4, 0])
    b_e = solve_b_vector(r_components, i, j)
    scalar = central_scalars(infinity)[pair]
    b = sp.zeros(5, 1)
    b[0] = scalar
    b[1] = b_e[0]
    b[2] = b_e[1]
    b[3] = b_e[2]
    return sp.eye(5) + b * sp.eye(5)[4, :]


def form5(r4, chart):
    block = sp.zeros(5)
    block[1, 2] = r4[3]
    block[1, 3] = -r4[2]
    block[2, 3] = r4[1]
    block[0, 4] = 1
    block[chart + 1, 4] = a / r4[chart + 1]
    return block - block.T


def quotient_data(r4, chart):
    rhat = sp.Matrix.vstack(r4, sp.Matrix([0]))
    keep = [index for index in range(5) if index != chart + 1]
    inclusion = sp.eye(5)[:, keep]
    projection = inclusion.T * (
        sp.eye(5) - rhat * sp.eye(5)[chart + 1, :] / rhat[chart + 1]
    )
    form = inclusion.T * form5(r4, chart) * inclusion
    return sp.simplify(projection), inclusion, sp.simplify(form)


def five_by_five(correction, base):
    matrix = sp.zeros(5)
    matrix[:4, :4] = base
    matrix[:4, 4] = sp.Matrix(correction)
    matrix[4, 4] = z  # value-line transition of D = O(1, 1)
    return matrix


def derive_corrections(base):
    """Unique q-corrections for the mixed cocycle in the stated gauge.

    Gauge, not read off a matrix: charts 1 and 2 carry the pure value-line
    factor z, and the chart-0 correction has no component on the eliminated
    E0 coordinate. The cocycle is imposed modulo the finite relation.
    """
    names = sp.symbols("c0_0 c0_1 c0_2 c0_3 c1_0 c1_1 c1_2 c1_3 c2_0 c2_1 c2_2 c2_3")
    lambdas = sp.symbols("l01 l12 l20")
    corrections = [sp.Matrix(names[4 * i : 4 * i + 4]) for i in range(3)]
    pairs = ((0, 1), (1, 2), (2, 0))
    equations = []
    finite_relation = sp.Matrix.vstack(relation(False), sp.Matrix([0]))
    for index, pair in enumerate(pairs):
        i, j = pair
        update = sp.zeros(5)
        update[:, 4] = lambdas[index] * finite_relation
        residual = (
            five_by_five(corrections[i], base) * forward_transition(True, pair)
            - forward_transition(False, pair) * five_by_five(corrections[j], base)
            - update
        )
        for entry in residual:
            numerator, _denominator = sp.fraction(sp.together(sp.expand(entry)))
            equations.append(sp.expand(numerator))
    # Pure value line on charts 1 and 2; no eliminated-E0 component on chart 0.
    gauge = [names[4 + k] for k in range(4)] + [names[8 + k] for k in range(4)] + [names[1]]
    equations.extend(gauge)
    solution = sp.solve(equations, list(names) + list(lambdas), dict=True)
    if len(solution) != 1:
        raise RuntimeError(f"expected one cocycle solution, got {len(solution)}")
    solved = solution[0]
    free = [name for name in list(names) + list(lambdas) if name not in solved]
    if free:
        raise RuntimeError(f"cocycle gauge is not unique: {free}")
    vectors = []
    for i in range(3):
        vectors.append(
            sp.Matrix([sp.factor(sp.together(solved[names[4 * i + k]])) for k in range(4)])
        )
    lam = [sp.factor(sp.together(solved[item])) for item in lambdas]
    return vectors, lam


@functools.lru_cache(maxsize=1)
def derive_tau():
    _assert_poly_identities()
    base = transition_matrix()
    corrections, lambdas = derive_corrections(base)
    # Closed form of the chart-0 correction, from the same partial fractions.
    expected0 = sp.Matrix(
        [
            sp.together(z * C * T * F / (w * S**3)),
            0,
            0,
            sp.together(-z * C * a / (w * S**3)),
        ]
    )
    if sp.simplify(corrections[0] - expected0) != sp.zeros(4, 1):
        raise RuntimeError("chart-0 correction did not simplify to the partial-fraction vector")
    if corrections[1] != sp.zeros(4, 1) or corrections[2] != sp.zeros(4, 1):
        raise RuntimeError("charts 1 and 2 are not pure value-line")
    taus = []
    forms_f = []
    forms_i = []
    for chart in range(3):
        projection, _inclusion_f, form_f = quotient_data(relation(False), chart)
        _projection_i, inclusion_i, form_i = quotient_data(relation(True), chart)
        tau = sp.simplify(
            sp.expand(projection * five_by_five(corrections[chart], base) * inclusion_i)
        )
        taus.append(tau)
        forms_f.append(form_f)
        forms_i.append(form_i)
    return {
        "TB": base,
        "corrections": corrections,
        "lambdas": lambdas,
        "tau": taus,
        "omega_finite": forms_f,
        "omega_infinity": forms_i,
    }


def form_residual(tau, omega_finite, omega_infinity):
    return sp.simplify(sp.expand(tau.T * omega_finite * tau - z**4 * omega_infinity))


@functools.lru_cache(maxsize=1)
def check_numerator_and_sequence():
    """Check 1. a is outside (W^6, S-W^2, XY), and that sequence is regular."""
    variables = [X, Y, W]
    g1 = S - W**2
    generators = [w, g1, F]
    remainder = _membership_remainder(a, generators, variables)
    regular, step, extras = is_regular_sequence(generators, variables)
    monomials = [
        X**i * Y**j * W ** (3 - i - j)
        for i in range(4)
        for j in range(4 - i)
    ]
    columns = []
    for linear in (X, Y, W):
        for factor in (g1, F):
            poly = sp.expand(linear * factor)
            columns.append([sp.Poly(poly, X, Y, W).coeff_monomial(m) for m in monomials])
    matrix = sp.Matrix(columns).T
    augmented = matrix.row_join(
        sp.Matrix([sp.Poly(sp.expand(a), X, Y, W).coeff_monomial(m) for m in monomials])
    )
    return {
        "remainder": sp.factor(remainder),
        "outside": remainder != 0,
        "regular": regular,
        "failing_step": step,
        "extras": extras,
        "rank": int(matrix.rank()),
        "rank_with_a": int(augmented.rank()),
        "monomials": 10,
        "columns": 6,
    }


@functools.lru_cache(maxsize=1)
def check_cech_and_chart():
    """Check 2. Triple overlap, and regularity of (W^6, -g, F) at z=1.

    The colon is computed in Q[X,Y,W], not after inverting a generic element.
    """
    variables = [X, Y, W]
    g1 = S - W**2
    signed = [w, sp.expand(-g1), F]
    # Coprimeness: none of the three denominator factors divides the numerator.
    numerator = z * a
    g_open = g
    coprime = {
        "W": sp.expand(numerator.subs(W, 0)) != 0,
        "X_in_F": sp.expand(a.subs(X, 0)) != 0,
        "Y_in_F": sp.expand(a.subs(Y, 0)) != 0,
        "g": _membership_remainder(numerator, [g_open], [z, X, Y, W]) != 0,
        "g_at_z1": _membership_remainder(a, [g1], variables) != 0,
    }
    denominator = sp.expand(w * (-g_open) * F)
    den_degrees = plane_degrees(denominator)
    num_degrees = plane_degrees(numerator)
    regular, step, extras = is_regular_sequence(signed, variables)
    # Also the unspecialized sequence, so specialization is not the only test.
    regular_z, step_z, extras_z = is_regular_sequence(
        [w, sp.expand(-g_open), F], [z, X, Y, W]
    )
    product = sp.expand(w * (-g1) * F)
    squared = [sp.expand(factor**2) for factor in signed]
    colon = colon_generators(squared, product, variables)
    colon_inside = contained(colon, signed, variables)
    ideal_inside_colon = contained(signed, colon, variables)
    killed = _membership_remainder(sp.expand(a * product), squared, variables) == 0
    basis = _gb(signed, variables)
    pure_powers = {}
    for var in variables:
        found = None
        for poly in basis:
            lead = sp.LM(poly, X, Y, W, order=sp.grlex)
            if lead == var ** sp.total_degree(lead) and sp.degree(lead, var) > 0:
                # LM may still involve only one variable.
                if all(sp.degree(lead, other) == 0 for other in variables if other != var):
                    found = int(sp.degree(lead, var))
                    break
        pure_powers[str(var)] = found
    return {
        "coprime": coprime,
        "denominator_plane_degrees": sorted(den_degrees),
        "numerator_plane_degrees": sorted(num_degrees),
        "regular_at_z1": regular,
        "failing_step": step,
        "extras": [sp.factor(item) for item in extras],
        "regular_with_z": regular_z,
        "z_failing_step": step_z,
        "z_extras": extras_z,
        "colon_equals_ideal": colon_inside and ideal_inside_colon,
        "a_killed_in_first_limit_step": killed,
        "leading_pure_powers": pure_powers,
        "groebner": [sp.factor(poly) for poly in basis],
    }


@functools.lru_cache(maxsize=1)
def check_injectivity():
    """Check 3. Re-derive H^1(GI) -> H^2(AI) from the flag and Künneth."""
    base = transition_matrix()
    # Flag ⟨P⟩ ⊂ ⟨P,E0⟩ ⊂ ⟨P,E0,E1⟩ ⊂ B, read off triangularity.
    flag = {
        "E2_decoupled_from_flag": all(base[3, col] == 0 for col in range(3))
        and all(base[row, 3] == 0 for row in range(3)),
        "P_invariant": base[1, 0] == 0 and base[2, 0] == 0 and base[3, 0] == 0,
        "P_E0_invariant": base[2, 0] == 0 and base[2, 1] == 0 and base[3, 0] == 0 and base[3, 1] == 0,
        "P_E0_E1_invariant": base[3, 0] == 0 and base[3, 1] == 0 and base[3, 2] == 0,
    }
    lines = []
    for index in range(4):
        bidegree = (B_BASE[index] + I_BASE, B_PLANE[index] + I_PLANE)
        lines.append(
            {
                "summand": ("P", "E0", "E1", "E2")[index],
                "bidegree": bidegree,
                "h1": h1_dimension(*bidegree),
            }
        )
    ai = (A_BASE + I_BASE, A_PLANE + I_PLANE)
    return {
        "flag": flag,
        "lines": lines,
        "all_h1_zero": all(line["h1"] == 0 for line in lines),
        "AI": ai,
    }


@functools.lru_cache(maxsize=1)
def check_bidegree():
    """Check 4. The Čech representative has the bidegree of O(3,-7)."""
    numerator = z * a
    denominator = sp.expand(w * (-g) * F)
    num_deg = plane_degrees(numerator)
    den_deg = plane_degrees(denominator)
    plane = next(iter(num_deg)) - next(iter(den_deg))
    hom_da = (A_BASE - D_BASE, A_PLANE - D_PLANE)
    di = (D_BASE + I_BASE, D_PLANE + I_PLANE)
    ai_from_hom = (hom_da[0] + di[0], hom_da[1] + di[1])
    ai = (A_BASE + I_BASE, A_PLANE + I_PLANE)
    # The single visible z is t0's finite frame, base degree 1, not the base degree of AI.
    z_exponent = sp.degree(sp.Poly(sp.expand(numerator), z))
    base_from_frames = B_BASE[0]  # P-component of T_B is z^3, the A-frame base degree
    return {
        "numerator_degrees": sorted(num_deg),
        "denominator_degrees": sorted(den_deg),
        "plane_degree": plane,
        "term_count_denominator": len(sp.Add.make_args(denominator)),
        "AI": ai,
        "HomDA_tensor_DI": ai_from_hom,
        "visible_z_exponent": int(z_exponent),
        "A_frame_base_degree": base_from_frames,
        "value_line_base": D_BASE,
        "L_base": B_BASE[0] + D_BASE,
    }


@functools.lru_cache(maxsize=1)
def check_tau():
    """Check 5. Re-derived τ satisfies τ^T Ω_finite τ = z^4 Ω_∞."""
    derived = derive_tau()
    residuals = []
    all_zero = True
    pq_entries = []
    for chart in range(3):
        residual = form_residual(
            derived["tau"][chart],
            derived["omega_finite"][chart],
            derived["omega_infinity"][chart],
        )
        residuals.append(residual)
        if residual != sp.zeros(4):
            all_zero = False
        pq_entries.append(sp.factor(sp.together(derived["tau"][chart].T * derived["omega_finite"][chart] * derived["tau"][chart])[0, 3]))
    # Official must-fail: scale the E-leg on chart 1 (frame P, E0, E2, q).
    # This doubles Ω(E0, E2) and does not change the P–q entry.
    chart = 1
    scale = sp.diag(1, 1, 2, 1)
    omega = derived["omega_infinity"][chart]
    tau = derived["tau"][chart]
    predicted = sp.simplify(z**4 * (scale.T * omega * scale - omega))
    actual = form_residual(tau * scale, derived["omega_finite"][chart], omega)
    break_entry = sp.factor(sp.together(predicted[1, 2]))
    pq_defect = sp.simplify(predicted[0, 3])
    # Shear control: q ↦ q + P preserves Ω, so the identity survives.
    shear = sp.eye(4)
    shear[0, 3] = 1
    shear_residual = form_residual(tau * shear, derived["omega_finite"][chart], omega)
    # Disallowed control: scaling q by 2 rescales the P–D pairing.
    pd = sp.diag(1, 1, 1, 2)
    pd_defect = sp.simplify((pd.T * omega * pd - omega)[0, 3])
    value_line = sp.simplify(derived["tau"][chart][3, 3] - z) == 0
    return {
        "derived": derived,
        "identity": all_zero,
        "pq_entries": pq_entries,
        "break_matches_prediction": sp.simplify(actual - predicted) == sp.zeros(4),
        "break_entry": break_entry,
        "break_entry_nonzero": sp.expand(sp.together(break_entry)) != 0,
        "break_pq_defect": pq_defect,
        "shear_still_holds": shear_residual == sp.zeros(4),
        "pd_pairing_defect": pd_defect,
        "value_line_slot_is_z": bool(value_line),
        "pair31_lambda": derived["lambdas"][2],
    }


def verdicts():
    first = check_numerator_and_sequence()
    cech = check_cech_and_chart()
    injection = check_injectivity()
    degree = check_bidegree()
    tau = check_tau()
    v1 = "pass" if first["outside"] and first["regular"] and first["rank"] == 6 and first["rank_with_a"] == 7 else "fail"
    coprime_ok = all(cech["coprime"].values())
    limit_ok = cech["colon_equals_ideal"] and not cech["a_killed_in_first_limit_step"]
    support_ok = cech["denominator_plane_degrees"] == [10] and cech["numerator_plane_degrees"] == [3]
    v2 = (
        "pass"
        if coprime_ok and support_ok and cech["regular_at_z1"] and limit_ok and cech["regular_with_z"]
        else "fail"
    )
    if cech["regular_with_z"] and not cech["regular_at_z1"]:
        v2 = "fail"
    v3 = (
        "pass"
        if injection["all_h1_zero"]
        and all(injection["flag"].values())
        and injection["AI"] == (3, -7)
        else "fail"
    )
    v4 = (
        "pass"
        if degree["plane_degree"] == -7
        and degree["AI"] == (3, -7)
        and degree["HomDA_tensor_DI"] == (3, -7)
        and degree["numerator_degrees"] == [3]
        and degree["denominator_degrees"] == [10]
        and degree["visible_z_exponent"] == 1
        and degree["L_base"] == 4
        else "fail"
    )
    v5 = (
        "pass"
        if tau["identity"]
        and tau["break_matches_prediction"]
        and tau["break_entry_nonzero"]
        and tau["break_pq_defect"] == 0
        and tau["shear_still_holds"]
        and tau["pd_pairing_defect"] != 0
        and tau["value_line_slot_is_z"]
        and all(sp.simplify(entry - z**4) == 0 for entry in tau["pq_entries"])
        else "fail"
    )
    return {
        "pin": PIN,
        "note_sha256": NOTE_SHA256,
        "verdicts": {"1": v1, "2": v2, "3": v3, "4": v4, "5": v5},
        "check1": {k: first[k] for k in ("remainder", "outside", "regular", "rank", "rank_with_a")},
        "check2": {
            "coprime": cech["coprime"],
            "regular_at_z1": cech["regular_at_z1"],
            "regular_with_z": cech["regular_with_z"],
            "colon_equals_ideal": cech["colon_equals_ideal"],
            "a_killed_in_first_limit_step": cech["a_killed_in_first_limit_step"],
            "leading_pure_powers": cech["leading_pure_powers"],
            "kernel_risk": not (cech["regular_at_z1"] and cech["colon_equals_ideal"]),
        },
        "check3": {
            "proved": v3 == "pass",
            "lines": [(line["summand"], line["bidegree"], line["h1"]) for line in injection["lines"]],
            "flag": injection["flag"],
            "AI": injection["AI"],
        },
        "check4": {
            "plane_degree": degree["plane_degree"],
            "AI": degree["AI"],
            "visible_z_exponent": degree["visible_z_exponent"],
            "L_base": degree["L_base"],
        },
        "check5": {
            "identity": tau["identity"],
            "break_entry": str(tau["break_entry"]),
            "break_pq_defect": str(tau["break_pq_defect"]),
            "shear_still_holds": tau["shear_still_holds"],
            "pd_pairing_defect": str(tau["pd_pairing_defect"]),
            "value_line_slot_is_z": tau["value_line_slot_is_z"],
        },
    }


def main():
    result = verdicts()
    printable = json.loads(json.dumps(result, default=str))
    print(json.dumps(printable, indent=2))
    failed = [key for key, value in result["verdicts"].items() if value != "pass"]
    if failed:
        print(f"FAILED checks: {failed}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
