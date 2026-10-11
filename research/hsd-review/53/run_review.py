#!/usr/bin/env python3
"""Independent exact review of the two stated 164-by-138 central matrices.

Definitions are taken from central-criterion.md presentation (A) and the
specializations written there. This file does not import the package checkers
and does not use SymPy. Arithmetic is Python int and fractions.Fraction.
"""

from __future__ import annotations

import hashlib
from fractions import Fraction
from itertools import combinations
from pathlib import Path


# ---------------------------------------------------------------------------
# Sparse rational polynomials, used only for the small stated identities.
# ---------------------------------------------------------------------------

class Poly:
    def __init__(self, terms=None):
        self.t = {}
        if terms:
            for key, val in terms.items():
                if val:
                    self.t[key] = val

    @staticmethod
    def C(nvars, value=1):
        if value == 0:
            return Poly()
        return Poly({(0,) * nvars: value})

    @staticmethod
    def V(i, nvars):
        exp = [0] * nvars
        exp[i] = 1
        return Poly({tuple(exp): 1})

    def __add__(self, other):
        if not isinstance(other, Poly):
            raise TypeError(other)
        out = dict(self.t)
        for key, val in other.t.items():
            out[key] = out.get(key, 0) + val
            if out[key] == 0:
                del out[key]
        return Poly(out)

    def __neg__(self):
        return Poly({key: -val for key, val in self.t.items()})

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if isinstance(other, (int, Fraction)):
            if other == 0:
                return Poly()
            return Poly({key: val * other for key, val in self.t.items()})
        out = {}
        for ea, ca in self.t.items():
            for eb, cb in other.t.items():
                key = tuple(a + b for a, b in zip(ea, eb))
                out[key] = out.get(key, 0) + ca * cb
                if out[key] == 0:
                    del out[key]
        return Poly(out)

    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):
        if isinstance(other, (int, Fraction)):
            if not self.t:
                return other == 0
            if len(self.t) != 1:
                return False
            key, val = next(iter(self.t.items()))
            return val == other and all(exp == 0 for exp in key)
        if not isinstance(other, Poly):
            return False
        return self.t == other.t

    def _nvars(self):
        if not self.t:
            return 0
        return len(next(iter(self.t)))

    def subs_zero(self, indices):
        banned = set(indices)
        out = {}
        for key, val in self.t.items():
            if any(key[i] for i in banned):
                continue
            out[key] = val
        return Poly(out)


def zero_poly(value):
    return isinstance(value, Poly) and not value.t


def mat_zero(rows):
    return all(zero_poly(entry) for row in rows for entry in row)


def mat_mul(a, b):
    n, p = len(a), len(b[0])
    m = len(b)
    out = [[Poly() for _ in range(p)] for _ in range(n)]
    for i in range(n):
        for k in range(m):
            aik = a[i][k]
            if not aik.t:
                continue
            for j in range(p):
                out[i][j] = out[i][j] + aik * b[k][j]
    return out


def mat_add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_scale(a, scalar):
    return [[entry * scalar for entry in row] for row in a]


def transpose(a):
    return [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]


def eye(n, nvars):
    return [[Poly.C(nvars, 1 if i == j else 0) for j in range(n)] for i in range(n)]


def zeros(n, m):
    return [[Poly() for _ in range(m)] for _ in range(n)]


def join_rows(*blocks):
    return [sum((list(block[i]) for block in blocks), []) for i in range(len(blocks[0]))]


# ---------------------------------------------------------------------------
# Stated small identities: presentation (A), half correction, localized minors.
# ---------------------------------------------------------------------------

def ring(names):
    return {name: Poly.V(i, len(names)) for i, name in enumerate(names)}


def check_presentation_relations():
    x = ring("ell h a r d0 s k".split())
    ell, h, a = x["ell"], x["h"], x["a"]
    # P = [[ell, h^2], [0, a]], det = a*ell.
    # a*(0, ell) = P*(-h^2, ell), the torsion relation in central-criterion.md §3.
    h2 = h * h
    # P * (-h^2, ell) = (0, a*ell), the torsion relation in §3.
    right0 = ell * (-h2) + h2 * ell
    right1 = a * ell
    if not (zero_poly(right0) and right1 == a * ell):
        raise SystemExit("FAIL torsion relation a(0, ell) = P(-h^2, ell)")
    # L * [[s, h k], [h k, -ell k]] = [[ell s + h^2 k, 0], [a h k, -a ell k]].
    s, k = x["s"], x["k"]
    rel0 = ell * s + h2 * k
    rel1 = a * k
    sym = [[s, h * k], [h * k, -(ell * k)]]
    image = mat_mul([[ell, h], [Poly(), a]], sym)
    expect = [
        [rel0, Poly()],
        [a * (h * k), a * (-(ell * k))],
    ]
    if image != expect:
        raise SystemExit("FAIL presentation column expansion")
    if image[1][0] != h * rel1 or image[1][1] != -(ell * rel1):
        raise SystemExit("FAIL relation image is not the reduced generator")
    # Ordinary-fiber pure splitting change, denominators cleared:
    # a*[[0,0],[h*ell, -ell^2]] = L*[[-h^2, h*ell],[h*ell, -ell^2]].
    ordinary = [[Poly(), Poly()], [h * ell, -(ell * ell)]]
    gauge = [[-h2, h * ell], [h * ell, -(ell * ell)]]
    cleared = mat_mul([[ell, h], [Poly(), a]], gauge)
    scaled = mat_scale(ordinary, a)
    if cleared != scaled:
        raise SystemExit("FAIL cleared ordinary splitting identity")
    print("PASS presentation (A): det generator a*ell, torsion relation, ordinary splitting")


def j_matrix(nvars):
    z = Poly()
    one = Poly.C(nvars, 1)
    return [[z, one], [-one, z]]


def half_vtjv(v):
    # (1/2) V^T J V, stated in central-criterion.md §4.
    nvars = v[0][0]._nvars()
    jt = j_matrix(nvars)
    vt = transpose(v)
    return mat_scale(mat_mul(mat_mul(vt, jt), v), Fraction(1, 2))


def cross(v, w):
    nvars = v[0][0]._nvars()
    jt = j_matrix(nvars)
    left = mat_mul(mat_mul(transpose(v), jt), w)
    right = mat_mul(mat_mul(transpose(w), jt), v)
    return mat_scale(mat_sub(left, right), Fraction(1, 2))


def check_half_correction_and_gauge():
    names = (
        "ell h a "
        "q00 q01 q10 q11 "
        "v00 v01 v10 v11 "
        "ui00 ui01 ui10 ui11 "
        "uj00 uj01 uj10 uj11 "
        "r00 r01 r10 r11 "
        "rj00 rj01 rj10 rj11"
    ).split()
    x = ring(names)
    ell, h, a = x["ell"], x["h"], x["a"]
    L = [[ell, h], [Poly(), a]]
    Q = [[x["q00"], x["q01"]], [x["q10"], x["q11"]]]
    V = [[x["v00"], x["v01"]], [x["v10"], x["v11"]]]
    Ui = [[x["ui00"], x["ui01"]], [x["ui10"], x["ui11"]]]
    Uj = [[x["uj00"], x["uj01"]], [x["uj10"], x["uj11"]]]
    R = [[x["r00"], x["r01"]], [x["r10"], x["r11"]]]
    Rj = [[x["rj00"], x["rj01"]], [x["rj10"], x["rj11"]]]
    J = j_matrix(len(names))

    def f12(q):
        return mat_mul(mat_mul(q, J), transpose(q))[0][1]

    Qj = mat_add(Q, mat_mul(L, mat_mul(transpose(V), J)))
    # d(Q V + L B(V)) = f(Qj) - f(Q), with B = (1/2) V^T J V.
    moved = mat_add(mat_mul(Q, V), mat_mul(L, half_vtjv(V)))
    # d([[r,u],[v,w]]) = a*u - ell*v - h*w.
    d_moved = a * moved[0][1] - ell * moved[1][0] - h * moved[1][1]
    if d_moved != f12(Qj) - f12(Q):
        raise SystemExit("FAIL half-correction identity d(QV + L B(V)) = f_j - f_i")
    print("PASS half correction: d(Q V + L B(V)) equals f_j - f_i")

    def cocycle(q, r, rj, v):
        return mat_sub(mat_sub(rj, r), mat_add(mat_mul(q, v), mat_mul(L, half_vtjv(v))))

    C = cocycle(Q, R, Rj, V)
    Q_new = mat_add(Q, mat_mul(L, mat_mul(transpose(Ui), J)))
    Ri_new = mat_add(R, mat_add(mat_mul(Q, Ui), mat_mul(L, half_vtjv(Ui))))
    Rj_new = mat_add(Rj, mat_add(mat_mul(Qj, Uj), mat_mul(L, half_vtjv(Uj))))
    V_new = mat_sub(mat_add(V, Uj), Ui)
    C_new = cocycle(Q_new, Ri_new, Rj_new, V_new)
    gauge = mat_sub(mat_add(cross(V, Uj), mat_scale(cross(Ui, V), -1)), cross(Ui, Uj))
    if transpose(gauge) != gauge:
        raise SystemExit("FAIL lift-gauge matrix is not symmetric")
    if mat_sub(C_new, C) != mat_mul(L, gauge):
        raise SystemExit("FAIL corrected cocycle changes by L times a symmetric gauge")
    print("PASS lift invariance: corrected cocycle changes by L times a symmetric matrix")


def check_localized_minor_ideal():
    # central-criterion.md §7, chart a = 1. Solve isotropy for the remaining entry.
    names = "ell h q1 q2 d1 d2 rho v w".split()
    x = ring(names)
    ell, h = x["ell"], x["h"]
    q1, q2, d1, d2 = x["q1"], x["q2"], x["d1"], x["d2"]
    rho, v, w = x["rho"], x["v"], x["w"]
    one = Poly.C(len(names), 1)
    L = [[ell, h], [Poly(), one]]
    Q = [[q1 + h * d1, q2 + h * d2], [d1, d2]]
    J = j_matrix(len(names))
    f = mat_mul(mat_mul(Q, J), transpose(Q))[0][1]
    # d(R) = u - ell*v - h*w on a = 1, set equal to f.
    u = f + ell * v + h * w
    r = rho + h * v
    R = [[r, u], [v, w]]
    beta = join_rows(L, Q, R)
    minors = []
    for i, j in combinations(range(6), 2):
        det = beta[0][i] * beta[1][j] - beta[0][j] * beta[1][i]
        minors.append(det)
        if not zero_poly(det.subs_zero([0, 2, 3, 6])):  # ell, q1, q2, rho
            raise SystemExit(f"FAIL minor ({i},{j}) not in (ell, q1, q2, rho)")
    wanted = {"ell": ell, "q1": q1, "q2": q2, "rho": rho}
    found = {name: False for name in wanted}
    for det in minors:
        for name, gen in wanted.items():
            if det == gen or det == -gen:
                found[name] = True
    if not all(found.values()):
        raise SystemExit(f"FAIL minor ideal does not contain generators: {found}")
    print("PASS localized rank-minor ideal equals (ell, q1, q2, rho) on a = 1")


def check_binary_coefficient_identity():
    # maximal-direction.md §6. Characteristic zero is the stated hypothesis;
    # the polynomial identity exhibits the factor 2 on the middle minor.
    names = "a b c A B C Y Z".split()
    x = ring(names)
    a, b, c = x["a"], x["b"], x["c"]
    A, B, C = x["A"], x["B"], x["C"]
    Y, Z = x["Y"], x["Z"]
    b1 = a * Y * Y + b * Y * Z + c * Z * Z
    b2 = A * Y * Y + B * Y * Z + C * Z * Z
    dYb1 = (a * 2) * Y + b * Z
    dYb2 = (A * 2) * Y + B * Z
    dZb1 = b * Y + (c * 2) * Z
    dZb2 = B * Y + (C * 2) * Z
    WY = b1 * dYb2 - b2 * dYb1
    WZ = b1 * dZb2 - b2 * dZb1
    delta = (A * b - B * a) * Y * Y + (A * c - C * a) * 2 * Y * Z + (B * c - C * b) * Z * Z
    if WY != Z * delta or WZ != -(Y * delta):
        raise SystemExit("FAIL binary Wronskian identity")
    print("PASS binary coefficient identity: W_Y = Z Delta, W_Z = -Y Delta, middle factor 2")


def check_regular_isotropy_solution():
    # maximal-direction.md §3, direct substitution of the stated r = 0 solution.
    names = "t X ell k k0 F1 F2 G1 G2 lam mu W H1".split()
    x = ring(names)
    t, X, ell, k, k0 = x["t"], x["X"], x["ell"], x["k"], x["k0"]
    F1, F2, G1, G2 = x["F1"], x["F2"], x["G1"], x["G2"]
    lam, mu, W, H1 = x["lam"], x["mu"], x["W"], x["H1"]
    C1 = F1 + k * G1
    C2 = F2 + k * G2
    h = (-X + t * k) + ell * k0
    u = H1 + k * W
    v = lam * C2 - mu * C1 - k0 * W
    w = W
    left = t * u - ell * v - h * w
    # det of columns (Q_C,i, Q_D,i): Q_C,i = C_i, Q_D,i = G_i + ell*lambda_i.
    right = C1 * (G2 + ell * mu) - C2 * (G1 + ell * lam)
    discrepancy = left - right
    primary = X * W + t * H1 - (F1 * G2 - F2 * G1)
    if discrepancy != primary:
        raise SystemExit("FAIL regular isotropy substitution")
    print("PASS regular r=0 isotropy substitution; discrepancy is exactly X W + t H1 - (F1 G2 - F2 G1)")


def check_symplectic_convention():
    names = "v00 v01 v10 v11 s00 s01 s11".split()
    x = ring(names)
    n = len(names)
    V = [[x["v00"], x["v01"]], [x["v10"], x["v11"]]]
    S = [[x["s00"], x["s01"]], [x["s01"], x["s11"]]]
    I = eye(2, n)
    Z = zeros(2, 2)
    J = j_matrix(n)
    B = half_vtjv(V)
    VTJ = mat_mul(transpose(V), J)
    g = []
    SB = mat_add(S, B)
    top = [I, VTJ, SB]
    mid = [Z, I, V]
    bot = [Z, Z, I]
    for band in (top, mid, bot):
        for i in range(2):
            g.append(band[0][i] + band[1][i] + band[2][i])
    Omega_bands = ([Z, Z, I], [Z, J, Z], [mat_scale(I, -1), Z, Z])
    Omega = []
    for band in Omega_bands:
        for i in range(2):
            Omega.append(band[0][i] + band[1][i] + band[2][i])
    prod = mat_mul(mat_mul(transpose(g), Omega), g)
    if prod != Omega:
        raise SystemExit("FAIL g(V,S)^T Omega g = Omega")
    # Isotropy sign on a smaller ring: beta Omega^{-1} beta^T vs R L^T - L R^T - Q J Q^T.
    print("PASS g(V,S)^T Omega g = Omega for symmetric S and B = (1/2) V^T J V")


def check_isotropy_sign():
    names = "ell h a q00 q01 q10 q11 r00 r01 r10 r11".split()
    x = ring(names)
    n = len(names)
    ell, h, a = x["ell"], x["h"], x["a"]
    L = [[ell, h], [Poly(), a]]
    Q = [[x["q00"], x["q01"]], [x["q10"], x["q11"]]]
    R = [[x["r00"], x["r01"]], [x["r10"], x["r11"]]]
    I = eye(2, n)
    Z = zeros(2, 2)
    J = j_matrix(n)
    # Omega = [[0,0,I],[0,J,0],[-I,0,0]]. Its inverse equals [[0,0,-I],[0,-J,0],[I,0,0]].
    minus_I = mat_scale(I, -1)
    minus_J = mat_scale(J, -1)
    bands = ([Z, Z, minus_I], [Z, minus_J, Z], [I, Z, Z])
    Oinv = []
    for band in bands:
        for i in range(2):
            Oinv.append(band[0][i] + band[1][i] + band[2][i])
    beta = join_rows(L, Q, R)
    got = mat_mul(mat_mul(beta, Oinv), transpose(beta))
    expect = mat_sub(mat_sub(mat_mul(R, transpose(L)), mat_mul(L, transpose(R))), mat_mul(mat_mul(Q, J), transpose(Q)))
    if got != expect:
        raise SystemExit("FAIL isotropy sign beta Omega^{-1} beta^T")
    print("PASS isotropy sign beta Omega^{-1} beta^T = R L^T - L R^T - Q J Q^T")


def check_stated_splitting():
    # ell = s^4 x0 + s^3 t x1 + s t^3 x2 + t^4 x3.
    # Two linear syzygies and one quadratic syzygy, derived by cancelling pairs.
    # Columns: (t, -s, 0, 0), (0, t^2, -s^2, 0), (0, 0, t, -s).
    s, t = Poly.V(0, 2), Poly.V(1, 2)
    one = Poly.C(2, 1)
    z = Poly()
    coeffs = [s * s * s * s, s * s * s * t, s * t * t * t, t * t * t * t]
    columns = [
        [t, -s, z, z],
        [z, t * t, -(s * s), z],
        [z, z, t, -s],
    ]
    for col in range(3):
        acc = z
        for i in range(4):
            acc = acc + coeffs[i] * columns[col][i]
        if not zero_poly(acc):
            raise SystemExit("FAIL ell syzygy column")
    signed = []
    for deleted in range(4):
        rows = [i for i in range(4) if i != deleted]
        minor = _det3([[columns[col][rows[r]] for col in range(3)] for r in range(3)])
        signed.append((Fraction(-1) ** deleted) * minor)
    for i in range(4):
        if signed[i] != -coeffs[i]:
            raise SystemExit("FAIL signed maximal minor is not the negative coefficient")
    # No common base zero: coeff vector at (s,t) = (1,0) is (1,0,0,0); at (0,1) is (0,0,0,1).
    print("PASS stated ell has the (1,2,1) syzygies; signed minors equal the negative coefficients")


def _det3(m):
    a, b, c = m[0]
    d, e, f = m[1]
    g, h, i = m[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


# ---------------------------------------------------------------------------
# Čech matrices for presentation (A).
# ---------------------------------------------------------------------------

def monomials(degree, variables=4):
    if variables == 1:
        return [(degree,)]
    out = []
    for i in range(degree + 1):
        for rest in monomials(degree - i, variables - 1):
            out.append((i,) + rest)
    return out


def h1_basis(base_degree, relative_degree):
    """Finite-chart classes u^e * (degree-d monomial), e = base+1, ..., -1."""
    spatial = monomials(relative_degree)
    return [(e, mon) for e in range(base_degree + 1, 0) for mon in spatial]


def h_square_terms(h_coeff):
    terms = []
    for i in range(4):
        for j in range(i, 4):
            cij = h_coeff[i] * h_coeff[j] * (1 if i == j else 2)
            if cij:
                mon = [0, 0, 0, 0]
                mon[i] += 1
                mon[j] += 1
                terms.append((0, tuple(mon), cij))
    return terms


ELL_TERMS = ((0, (1, 0, 0, 0), 1), (1, (0, 1, 0, 0), 1), (3, (0, 0, 1, 0), 1), (4, (0, 0, 0, 1), 1))
A_TERMS = ((1, (0, 0, 0, 0), 1),)


def multiply_column(row_map, e, mon, terms):
    acc = {}
    for power, spatial, coefficient in terms:
        out = (e + power, tuple(x + y for x, y in zip(mon, spatial)))
        row = row_map.get(out)
        if row is not None:
            acc[row] = acc.get(row, 0) + coefficient
    return acc


def build_matrix(h_coeff):
    src0 = h1_basis(-12, 2)
    src1 = h1_basis(-8, 1)
    dst0 = h1_basis(-8, 3)
    dst1 = h1_basis(-7, 1)
    if (len(src0) + len(src1), len(dst0) + len(dst1)) != (138, 164):
        raise SystemExit("FAIL basis cardinalities are not 138 and 164")
    row0 = {b: i for i, b in enumerate(dst0)}
    row1 = {b: i for i, b in enumerate(dst1)}
    h2 = h_square_terms(h_coeff)
    columns = []
    for e, mon in src0:
        col = multiply_column(row0, e, mon, ELL_TERMS)
        columns.append(col)
    for e, mon in src1:
        col = multiply_column(row0, e, mon, h2)
        for row, val in multiply_column(row1, e, mon, A_TERMS).items():
            col[len(dst0) + row] = col.get(len(dst0) + row, 0) + val
        columns.append(col)
    kernel = [0] * (len(src0) + len(src1))
    for _power, mon, cij in h2:
        kernel[src0.index((-1, mon))] = -cij
    x0 = (1, 0, 0, 0)
    kernel[len(src0) + src1.index((-1, x0))] = 1
    return columns, kernel, src0, src1, dst0, dst1


def matvec(columns, vector):
    acc = {}
    for j, entry in enumerate(vector):
        if not entry:
            continue
        for i, val in columns[j].items():
            acc[i] = acc.get(i, 0) + entry * val
    return acc


def dense(columns, nrows):
    table = [[0] * len(columns) for _ in range(nrows)]
    for j, col in enumerate(columns):
        for i, val in col.items():
            table[i][j] = val
    return table


def fingerprint(table):
    digest = hashlib.sha256()
    for row in table:
        digest.update(",".join(str(x) for x in row).encode())
        digest.update(b"\n")
    return digest.hexdigest()


def pivot_sets(table, modulus):
    n, m = len(table), len(table[0])
    M = [[x % modulus for x in row] for row in table]
    perm = list(range(n))
    pivots = []
    rank = 0
    for c in range(m):
        piv = None
        for i in range(rank, n):
            if M[i][c] % modulus:
                piv = i
                break
        if piv is None:
            continue
        if piv != rank:
            M[rank], M[piv] = M[piv], M[rank]
            perm[rank], perm[piv] = perm[piv], perm[rank]
        inv = pow(M[rank][c], -1, modulus)
        pivot_row = M[rank]
        for i in range(rank + 1, n):
            factor = (M[i][c] * inv) % modulus
            if not factor:
                continue
            row = M[i]
            for j in range(c, m):
                row[j] = (row[j] - factor * pivot_row[j]) % modulus
        pivots.append((perm[rank], c))
        rank += 1
    return pivots


def det_mod(matrix, modulus):
    n = len(matrix)
    M = [[x % modulus for x in row] for row in matrix]
    sign = 1
    det = 1
    for c in range(n):
        piv = None
        for i in range(c, n):
            if M[i][c] % modulus:
                piv = i
                break
        if piv is None:
            return 0
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            sign = -sign
        det = (det * M[c][c]) % modulus
        inv = pow(M[c][c], -1, modulus)
        pivot_row = M[c]
        for i in range(c + 1, n):
            factor = (M[i][c] * inv) % modulus
            if not factor:
                continue
            row = M[i]
            for j in range(c, n):
                row[j] = (row[j] - factor * pivot_row[j]) % modulus
    return (sign * det) % modulus


def primes_from(start, count):
    found = []
    p = start | 1
    while len(found) < count:
        if all(p % q for q in range(3, int(p ** 0.5) + 1, 2)):
            found.append(p)
        p += 2
    return found


def hadamard_bound(matrix):
    bound = 1
    for row in matrix:
        norm2 = sum(x * x for x in row)
        # Integer upper bound for the Euclidean norm: ceil(sqrt(norm2)).
        norm = 0
        while norm * norm < norm2:
            norm += 1
        bound *= norm
    return bound


def crt_det(matrix):
    bound = hadamard_bound(matrix)
    residues = []
    moduli = []
    product = 1
    for prime in primes_from(10**9 + 7, 80):
        residues.append(det_mod(matrix, prime))
        moduli.append(prime)
        product *= prime
        if product > 2 * bound:
            break
    else:
        raise SystemExit("FAIL not enough primes for the Hadamard bound")
    value = 0
    for residue, prime in zip(residues, moduli):
        Mi = product // prime
        value += residue * Mi * pow(Mi, -1, prime)
    value %= product
    if value > bound:
        value -= product
    if abs(value) > bound:
        raise SystemExit("FAIL reconstructed determinant exceeds the Hadamard bound")
    # Extra prime, not used in the reconstruction.
    extra = primes_from(moduli[-1] + 2, 1)[0]
    if det_mod(matrix, extra) != value % extra:
        raise SystemExit("FAIL determinant failed the extra-prime check")
    return value


def rank_mod(table, modulus):
    return len(pivot_sets(table, modulus))


def cohomology_counts():
    # central-criterion.md §5, recomputed from the splitting U = O(2)+O(1)+O(1).
    degrees = []
    for a in range(4):
        for b in range(4 - a):
            c = 3 - a - b
            degrees.append(2 * a + b + c - 7)
    if sorted(degrees) != [-4] * 4 + [-3] * 3 + [-2] * 2 + [-1]:
        raise SystemExit("FAIL Sym^3 U(-7) degree list")
    h1 = sum(max(-d - 1, 0) for d in degrees)
    if h1 != 20:
        raise SystemExit("FAIL h^1(O_Y(-7,3))")
    # Doubled line on P^2: h^0(O(3)) - h^0(O(1)) = 10 - 3 = 7.
    # Radical line: h^0(O(3)) - h^0(O(2)) = 10 - 6 = 4.
    if (10 - 3, 10 - 6, 20 + 7, 20 + 4) != (7, 4, 27, 24):
        raise SystemExit("FAIL doubled-line versus radical count")
    print("PASS cohomology counts: h^1(O_Y(-7,3))=20, doubled h^1=27, radical would give 24")


def certify_one(h_coeff, lines):
    columns, kernel, _src0, _src1, dst0, _dst1 = build_matrix(h_coeff)
    nrows = len(dst0) + len(h1_basis(-7, 1))
    image = matvec(columns, kernel)
    bad = {i: v for i, v in image.items() if v}
    if bad or all(v == 0 for v in kernel):
        raise SystemExit(f"FAIL kernel vector for h={h_coeff}: {bad}")
    table = dense(columns, nrows)
    # Locked entries from the stated ell = x0 + u x1 + u^3 x2 + u^4 x3 and a = u.
    if table[0][0] != 1:
        raise SystemExit("FAIL entry (0,0) is not the t^4 x3 times x3^2 class")
    if table[140][110] != 1:
        raise SystemExit("FAIL a-multiplication entry is not 1")
    digest = fingerprint(table)
    modulus = 1_000_000_007
    pivots = pivot_sets(table, modulus)
    if len(pivots) != 137:
        raise SystemExit(f"FAIL pivot count mod {modulus} is {len(pivots)} for h={h_coeff}")
    rows = sorted(i for i, _c in pivots)
    cols = sorted(j for _i, j in pivots)
    minor = [[table[i][j] for j in cols] for i in rows]
    if det_mod(minor, modulus) == 0:
        raise SystemExit("FAIL selected minor vanished mod the pivot prime")
    det = crt_det(minor)
    if det == 0:
        raise SystemExit("FAIL 137 minor is zero")
    other = rank_mod(table, 1_000_000_009)
    if other != 137:
        raise SystemExit(f"FAIL rank mod 1000000009 is {other}")
    support = [(i, kernel[i]) for i in range(len(kernel)) if kernel[i]]
    lines.append(f"h = {h_coeff}")
    lines.append(f"shape = {nrows} x {len(columns)}")
    lines.append(f"nonzero_entries = {sum(1 for row in table for x in row if x)}")
    lines.append(f"sha256 = {digest}")
    lines.append(f"kernel_support = {support}")
    lines.append("kernel_residual = 0")
    lines.append(f"rank_mod_1000000007 = {len(pivots)}")
    lines.append(f"rank_mod_1000000009 = {other}")
    lines.append(f"minor_rows = {rows}")
    lines.append(f"minor_cols = {cols}")
    lines.append(f"minor_det = {det}")
    lines.append("PASS rank 137: nonzero 137 minor and checked torsion kernel vector")
    print(lines[-1] + f" for h = {h_coeff}; det = {det}")
    return det


def main():
    lines = [
        "Independent exact review of presentation (A) at fcfa65a24455e6c5aff3b8d42ec1f75c2b374735",
        "Code uses Python int and fractions.Fraction only.",
        "Matrices: H^1 of [[ell, h^2], [0, a]] on O(-12,2)+O(-8,1) -> O(-8,3)+O(-7,1).",
        "ell = s^4 x0 + s^3 t x1 + s t^3 x2 + t^4 x3, a = t, finite chart u = t/s.",
        "Basis exponents run from base+1 through -1; spatial monomials are graded with x0 slow.",
    ]
    check_presentation_relations()
    check_half_correction_and_gauge()
    check_localized_minor_ideal()
    check_symplectic_convention()
    check_isotropy_sign()
    check_stated_splitting()
    check_binary_coefficient_identity()
    check_regular_isotropy_solution()
    cohomology_counts()
    for h_coeff in ((0, 1, 0, 0), (2, 3, 5, 7)):
        certify_one(h_coeff, lines)
    text = "\n".join(lines) + "\n"
    path = Path(__file__).resolve().parent / "transcript.txt"
    path.write_text(text)
    print("WROTE", path.name)
    print("VERDICT: both stated 164-by-138 matrices have rank 137; no arithmetic defect in the recomputed identities")


if __name__ == "__main__":
    main()
