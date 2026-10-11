"""Exact-arithmetic checks for the bounded plane-completion lemma.

Pinned commit 1db993943e07d615624edcf30bc2e169652453f5.
All identities are identities in the fraction field of Q[X, Y, W, z, u].
"""

from __future__ import annotations

import hashlib
import subprocess

import sympy as sp

X, Y, W, z, u = sp.symbols("X Y W z u")
e0, e1, e2 = sp.symbols("e0 e1 e2")
r1s, r2s, r3s, a_s = sp.symbols("r1 r2 r3 a")

S = X**2 + Y**2
F = X * Y
a = X**3 + Y**3
g = S - z * W**2
C = S**2 + z * S * W**2 + z**2 * W**4
T = -3 * S + 2 * F

PIN = "1db993943e07d615624edcf30bc2e169652453f5"
PIN_PREFIX = "research/carrier/plane-completion-lemma"
EXPECTED_SHA256 = {
    "PLANE_COMPLETION_LEMMA.md": "fcb28b552115339c62c4e751caebf6876ca33885db061e267ddde028c6c0cde0",
    "INDEPENDENT_REVIEW.md": "f1e7807f73437acb88615ef0412c15fc105c5cef4841f23f09d54e8f0c48ff4f",
    "manifest.json": "b4f8f4147c8fcec09789bf1e903c71171c6faa4b04fa2397a38ab57365bcdf93",
}
EXPECTED_BYTES = {
    "PLANE_COMPLETION_LEMMA.md": 12807,
    "INDEPENDENT_REVIEW.md": 5344,
}


def _num(expr):
    expr = sp.together(sp.expand(expr))
    num, _den = sp.fraction(expr)
    return sp.expand(num)


def _is_zero(expr) -> bool:
    return _num(expr) == 0


def omega(r, e, f):
    """L-valued pairing r · (e × f), matching the displayed skew matrix."""
    return (
        r[0] * (e[1] * f[2] - e[2] * f[1])
        + r[1] * (e[2] * f[0] - e[0] * f[2])
        + r[2] * (e[0] * f[1] - e[1] * f[0])
    )


def psi_on(r, scalar, index, e):
    return scalar * e[index] / r[index]


def b_edges(r, scalar):
    """Cyclic E-valued corrections b12, b23, b31."""
    b12 = (0, 0, scalar / (r[0] * r[1]))
    b23 = (scalar / (r[1] * r[2]), 0, 0)
    b31 = (0, scalar / (r[2] * r[0]), 0)
    return b12, b23, b31


def finite_r():
    return (W**6, -g, F)


def infinity_r():
    return (S**3, -u * S + W**2, F)


def generic_e():
    return (e0, e1, e2)


def pairing_residual(r, edge):
    """Numerator of Ω(e, b_ij) - (ψ_j - ψ_i)(e)."""
    b12, b23, b31 = b_edges(r, a)
    edges = {(1, 2): b12, (2, 3): b23, (3, 1): b31}
    i, j = edge
    b = edges[(i, j)]
    e = generic_e()
    return _num(omega(r, e, b) - (psi_on(r, a, j - 1, e) - psi_on(r, a, i - 1, e)))


def vector_sum_residuals(r):
    b12, b23, b31 = b_edges(r, a)
    target = tuple(a * r[k] / (r[0] * r[1] * r[2]) for k in range(3))
    return [_num(b12[k] + b23[k] + b31[k] - target[k]) for k in range(3)]


def finite_central_residual():
    r = finite_r()
    residual = a**2 / (r[0] * r[1] * r[2])
    c12 = T * F / (W**6 * g)
    c23 = z**3 / (g * F)
    c31 = C / (W**6 * F)
    return _num(c12 + c23 + c31 + residual)


def infinity_central_residual():
    r = infinity_r()
    residual = a**2 / (r[0] * r[1] * r[2])
    c12 = -T * F / (r[0] * r[1])
    c23 = -1 / (r[1] * r[2])
    c31 = 0
    return _num(c12 + c23 + c31 + residual)


def polynomial_finite_residual():
    return sp.expand(a**2 - (g * C + z**3 * W**6 + T * F**2))


def polynomial_infinity_residual():
    return sp.expand(a**2 - (S**3 + T * F**2))


def eleven_residuals():
    """The eleven symbolic checks: six pairings, two vector sums, two cancellations, one polynomial."""
    out = {}
    for chart, r in (("finite", finite_r()), ("infinity", infinity_r())):
        for edge in ((1, 2), (2, 3), (3, 1)):
            out[f"pair_{chart}_{edge[0]}{edge[1]}"] = pairing_residual(r, edge)
        marker = sp.symbols("m")
        components = vector_sum_residuals(r)
        out[f"vector_sum_{chart}"] = sum(comp * marker**k for k, comp in enumerate(components))
    out["central_finite"] = finite_central_residual()
    out["central_infinity"] = infinity_central_residual()
    out["polynomial_finite"] = polynomial_finite_residual()
    if len(out) != 11:
        raise RuntimeError(f"expected 11 residuals, got {len(out)}")
    return out


def omega_chart_residuals():
    """Displayed chart entries minus the skew-matrix entries."""
    e0v, e1v, e2v = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    rf = finite_r()
    ri = infinity_r()
    finite = [
        _num(omega(rf, e0v, e1v) - F),
        _num(omega(rf, e0v, e2v) - g),
        _num(omega(rf, e1v, e2v) - W**6),
    ]
    infinity = [
        _num(omega(ri, e0v, e1v) - F),
        _num(omega(ri, e0v, e2v) - (u * S - W**2)),
        _num(omega(ri, e1v, e2v) - S**3),
    ]
    return finite, infinity


def auxiliary_identity_residuals():
    r = finite_r()
    product = _num(r[0] * r[1] * r[2] - (-(W**6) * g * F))
    cubes = sp.expand(g * C - (S**3 - z**3 * W**6))
    r2_match = _num(((-u * S + W**2) - (-g / z)).subs(u, 1 / z))
    return {
        "finite_r_product": product,
        "difference_of_cubes": cubes,
        "infinity_r2_matches_minus_g_over_z": r2_match,
        "polynomial_infinity": polynomial_infinity_residual(),
    }


def transition_residuals():
    """TB r_infinity - z^3 r_finite, with the displayed E0←E1 entry z C."""
    ri_e1 = -g / z
    tb = (
        z**3 * (-a),
        S**3 + z * C * ri_e1,
        z**4 * ri_e1,
        z**3 * F,
    )
    target = tuple(z**3 * comp for comp in (-a, W**6, -g, F))
    return [_num(tb[i] - target[i]) for i in range(4)]


def _scaling_degree(expr, substitutions, parameter):
    """Degree of expr under a one-parameter scaling, allowing negative degree."""
    scaled = sp.together(expr.subs(substitutions))
    base = sp.together(expr)
    ratio = sp.together(sp.simplify(scaled / base))
    num, den = sp.fraction(ratio)
    return int(sp.degree(sp.expand(num), parameter) - sp.degree(sp.expand(den), parameter))


def plane_degree(expr):
    t = sp.symbols("t", positive=True)
    return _scaling_degree(expr, {X: t * X, Y: t * Y, W: t * W}, t)


def correction_plane_degrees():
    rf = finite_r()
    ri = infinity_r()
    finite = {
        "c12": T * F / (W**6 * g),
        "c23": z**3 / (g * F),
        "c31": C / (W**6 * F),
    }
    infinity = {
        "c12": -T * F / (ri[0] * ri[1]),
        "c23": -1 / (ri[1] * ri[2]),
    }
    out = {f"finite_{k}": plane_degree(v) for k, v in finite.items()}
    out.update({f"infinity_{k}": plane_degree(v) for k, v in infinity.items()})
    out["finite_residual"] = plane_degree(a**2 / (rf[0] * rf[1] * rf[2]))
    return out


def bidegree_sum(left, right):
    return (left[0] + right[0], left[1] + right[1])


def bidegree_sub(left, right):
    return (left[0] - right[0], left[1] - right[1])


LINE = {
    "A": (3, -6),
    "P": (3, -3),
    "L": (4, -2),
    "E0": (0, 0),
    "E1": (4, -4),
    "E2": (3, -4),
}


def derived_bundles():
    D = bidegree_sub(LINE["L"], LINE["P"])
    M_from_hom = bidegree_sub(LINE["P"], D)
    P2 = bidegree_sum(LINE["P"], LINE["P"])
    M_from_formula = bidegree_sub(P2, LINE["L"])
    PL_inv = bidegree_sub(LINE["P"], LINE["L"])
    filtration = {
        "P": bidegree_sum(LINE["P"], PL_inv),
        "E0": bidegree_sum(LINE["E0"], PL_inv),
        "E1": bidegree_sum(LINE["E1"], PL_inv),
        "E2": bidegree_sum(LINE["E2"], PL_inv),
    }
    hom_E1_P = bidegree_sub(LINE["P"], LINE["E1"])
    hom_E2_P = bidegree_sub(LINE["P"], LINE["E2"])
    hom_E0_P = bidegree_sub(LINE["P"], LINE["E0"])
    hom_A_P = bidegree_sub(LINE["P"], LINE["A"])
    return {
        "D": D,
        "M": M_from_hom,
        "M_formula": M_from_formula,
        "filtration": filtration,
        "Hom_E0_P": hom_E0_P,
        "Hom_E1_P": hom_E1_P,
        "Hom_E2_P": hom_E2_P,
        "Hom_A_P": hom_A_P,
    }


def h0_projective(n, degree):
    if degree < 0:
        return 0
    # dim Sym^degree k^{n+1} = C(degree + n, n)
    return sp.binomial(degree + n, n)


def h_top_projective(n, degree):
    return h0_projective(n, -degree - n - 1)


def cohomology_p1_p2(base, plane):
    """Künneth dimensions of O(base, plane) on P1 × P2, through degree 3."""
    h_base = [h0_projective(1, base), h_top_projective(1, base) if True else 0]
    # Intermediate cohomology of P1 vanishes; H^1 is the top group.
    h_base = [int(h0_projective(1, base)), int(h_top_projective(1, base))]
    h_plane = [
        int(h0_projective(2, plane)),
        0,
        int(h_top_projective(2, plane)),
    ]
    dims = [0, 0, 0, 0]
    parts = {0: [], 1: [], 2: [], 3: []}
    for i, left in enumerate(h_base):
        for j, right in enumerate(h_plane):
            dims[i + j] += left * right
            parts[i + j].append(((i, j), left, right, left * right))
    return dims, parts


def character_weight(expr):
    """Weight for wt(z, X, Y, W) = (2, 1, 1, 0), extended by wt(u) = -2."""
    t = sp.symbols("t", positive=True)
    return _scaling_degree(
        expr,
        {z: t**2 * z, u: t ** (-2) * u, X: t * X, Y: t * Y},
        t,
    )


def weight_ledger():
    """Finite target 4 and infinity target 8, with the pinned frame weights."""
    d_finite = {"P": 3, "E0": 0, "E1": 2, "E2": 2}
    d_infinity = {"P": 3, "E0": 6, "E1": 0, "E2": 2}
    rf = finite_r()
    ri = infinity_r()
    psi_f = [character_weight(a / rf[i]) for i in range(3)]
    psi_i = [character_weight(a / ri[i]) for i in range(3)]
    d_D_finite = 4 - d_finite["P"]
    d_D_infinity = 8 - d_infinity["P"]
    finite_sums = [
        psi_f[i] + d_finite[name] + d_D_finite for i, name in enumerate(("E0", "E1", "E2"))
    ]
    infinity_sums = [
        psi_i[i] + d_infinity[name] + d_D_infinity for i, name in enumerate(("E0", "E1", "E2"))
    ]
    e0v, e1v, e2v = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    form_f = [
        character_weight(omega(rf, e0v, e1v)) + d_finite["E0"] + d_finite["E1"],
        character_weight(omega(rf, e0v, e2v)) + d_finite["E0"] + d_finite["E2"],
        character_weight(omega(rf, e1v, e2v)) + d_finite["E1"] + d_finite["E2"],
    ]
    form_i = [
        character_weight(omega(ri, e0v, e1v)) + d_infinity["E0"] + d_infinity["E1"],
        character_weight(omega(ri, e0v, e2v)) + d_infinity["E0"] + d_infinity["E2"],
        character_weight(omega(ri, e1v, e2v)) + d_infinity["E1"] + d_infinity["E2"],
    ]
    return {
        "psi_finite": psi_f,
        "psi_infinity": psi_i,
        "d_D_finite": d_D_finite,
        "d_D_infinity": d_D_infinity,
        "sums_finite": finite_sums,
        "sums_infinity": infinity_sums,
        "form_totals_finite": form_f,
        "form_totals_infinity": form_i,
        "P_D_finite": d_finite["P"] + d_D_finite,
        "P_D_infinity": d_infinity["P"] + d_D_infinity,
    }


def cover_polynomials():
    """On XY = F = 0 and S = 0, both X^3 and Y^3 are zero as polynomial consequences."""
    return {
        "X3": sp.expand(X * S - Y * F - X**3),
        "Y3": sp.expand(Y * S - X * F - Y**3),
    }


def form_matrix(r, psi, lam=1):
    """Skew matrix on the ordered basis (P, E0, E1, E2, D)."""
    M = sp.zeros(5)
    for i in range(3):
        for j in range(3):
            ei = tuple(int(k == i) for k in range(3))
            ej = tuple(int(k == j) for k in range(3))
            M[1 + i, 1 + j] = omega(r, ei, ej)
    M[0, 4] = lam
    M[4, 0] = -lam
    for i in range(3):
        M[1 + i, 4] = psi[i]
        M[4, 1 + i] = -psi[i]
    return sp.simplify(M)


def radical_generator(r, psi, lam=1):
    M = form_matrix(r, psi, lam)
    space = M.nullspace()
    return M, space


def local_psi(index, r, scalar):
    psi = [0, 0, 0]
    psi[index] = scalar / r[index]
    return tuple(psi)


def graph_vector():
    return sp.Matrix([-a_s, r1s, r2s, r3s, 0])


def vertical_vector():
    return sp.Matrix([0, r1s, r2s, r3s, 0])


def degree3_coords(poly):
    poly = sp.expand(poly)
    coords = []
    for i in range(4):
        for j in range(4 - i):
            k = 3 - i - j
            coords.append(sp.Integer(poly.coeff(X, i).coeff(Y, j).coeff(W, k)))
    return sp.Matrix(coords)


def hom_image_matrix():
    columns = [degree3_coords(mult * F) for mult in (X, Y, W)]
    return sp.Matrix.hstack(*columns)


def monomial_index(i, j, k):
    index = 0
    for ii in range(4):
        for jj in range(4 - ii):
            kk = 3 - ii - jj
            if (ii, jj, kk) == (i, j, k):
                return index
            index += 1
    raise KeyError((i, j, k))


def scalar_pairing_obstruction():
    """λ(X^3+Y^3) lies in the image of ℓ ↦ ℓ·XY iff λ = 0."""
    image = hom_image_matrix()
    target = degree3_coords(a)
    augmented = image.row_join(target)
    x3 = monomial_index(3, 0, 0)
    y3 = monomial_index(0, 3, 0)
    return {
        "image_rank": int(image.rank()),
        "augmented_rank": int(augmented.rank()),
        "x3_row_of_image_is_zero": all(image.row(x3)[c] == 0 for c in range(3)),
        "y3_row_of_image_is_zero": all(image.row(y3)[c] == 0 for c in range(3)),
        "x3_coefficient_of_a": int(target[x3]),
        "y3_coefficient_of_a": int(target[y3]),
    }


def wrong_overlap_denominators():
    """Each nonzero correction keeps a denominator factor that its own overlap inverts and the other overlaps do not.

    A unit gcd means the numerator does not cancel that factor.
    """
    return {
        "finite_c12_keeps_W": sp.gcd(sp.expand(T * F), W),
        "finite_c23_keeps_g_against_F": sp.gcd(sp.expand(g), F),
        "finite_c31_keeps_F": sp.gcd(sp.expand(C), F),
        "infinity_c12_keeps_S": sp.gcd(sp.expand(T * F), S),
    }


def overlap_values():
    """Exact values on Q-points of the stated double overlaps, and poles of swapped terms."""
    points = {
        "U12": {X: 0, Y: 1, W: 1, z: 0},
        "U23": {X: 1, Y: 1, W: 0, z: 0},
        "U31": {X: 1, Y: 1, W: 1, z: 2},
        "infinity_U12_u0": {X: 1, Y: 1, W: 1, u: 0},
    }
    c_finite = {
        "c12": T * F / (W**6 * g),
        "c23": z**3 / (g * F),
        "c31": C / (W**6 * F),
    }
    c_infinity = {
        "c12": -T * F / (S**3 * (-u * S + W**2)),
        "c23": -1 / ((-u * S + W**2) * F),
    }

    def ev(expr, point):
        value = expr.subs(point)
        if value in (sp.zoo, sp.nan, sp.oo, -sp.oo):
            return None
        value = sp.together(sp.simplify(value))
        if value in (sp.zoo, sp.nan, sp.oo, -sp.oo):
            return None
        if value.free_symbols:
            return None
        num, den = sp.fraction(value)
        if den == 0:
            return None
        return sp.Integer(num) / sp.Integer(den)

    return {
        "finite_c12_on_U12": ev(c_finite["c12"], points["U12"]),
        "finite_c31_pole_on_U12": ev(c_finite["c31"], points["U12"]) is None
        and sp.simplify(C.subs(points["U12"])) != 0,
        "finite_c23_on_U23": ev(c_finite["c23"], points["U23"]),
        "finite_c12_pole_on_U23": ev(c_finite["c12"], points["U23"]) is None
        and sp.simplify((T * F).subs(points["U23"])) != 0,
        "finite_c31_on_U31": ev(c_finite["c31"], points["U31"]),
        "finite_c23_pole_on_U31": ev(c_finite["c23"], points["U31"]) is None
        and sp.simplify((z**3).subs(points["U31"])) != 0,
        "infinity_c12_at_u0": ev(c_infinity["c12"], points["infinity_U12_u0"]),
        "infinity_c23_at_u0": ev(c_infinity["c23"], points["infinity_U12_u0"]),
    }


def sign_flip_does_not_cancel():
    r = finite_r()
    residual = a**2 / (r[0] * r[1] * r[2])
    csum = T * F / (W**6 * g) + z**3 / (g * F) + C / (W**6 * F)
    flipped = _num(-csum + residual)
    return flipped != 0


def isometry_status(h0_dim, h1_dim):
    """Torsor bookkeeping for an M-band. Existence uses H1; uniqueness uses H0."""
    if h1_dim != 0:
        return "not-settled-by-vanishing"
    if h0_dim == 0:
        return "unique"
    return "exists-not-unique"


def git_object_bytes(path):
    return subprocess.check_output(["git", "show", f"{PIN}:{PIN_PREFIX}/{path}"])


def pinned_digests():
    digests = {}
    for name in EXPECTED_SHA256:
        raw = git_object_bytes(name)
        digests[name] = (hashlib.sha256(raw).hexdigest(), len(raw))
    return digests


def flipped_pairing_is_nonzero():
    """The opposite Čech direction Ω(e, b12) - (ψ1 - ψ2) is not the zero form."""
    r = finite_r()
    b12, _b23, _b31 = b_edges(r, a)
    e = generic_e()
    return _num(omega(r, e, b12) - (psi_on(r, a, 0, e) - psi_on(r, a, 1, e))) != 0
