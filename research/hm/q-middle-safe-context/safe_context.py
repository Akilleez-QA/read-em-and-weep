"""Explicit universal context factories; importing this module does no symbolic work."""
from pathlib import Path
from types import SimpleNamespace
import hashlib
import json

HERE = Path(__file__).resolve().parent
PAYLOAD = HERE.with_name('q-middle-candidate-interface')
PROVENANCE_SHA256 = 'b0d8dfec8abec5290128c2def4eb21bbd35f9ae1f483fa67f8e3de555f54b0ab'

def validate_inputs(root=PAYLOAD):
    raw = (HERE / 'provenance.json').read_bytes()
    if hashlib.sha256(raw).hexdigest() != PROVENANCE_SHA256:
        raise ValueError('Context provenance changed')
    records = json.loads(raw)['inputs']
    for name, digest in records.items():
        if hashlib.sha256((Path(root) / name).read_bytes()).hexdigest() != digest:
            raise ValueError('Pinned input changed: ' + name)


def _construct(include_helpers):
    import sympy as s
    from math import comb
    import sympy as s
    (x, y, z, u, w) = s.symbols('x y z u w')
    coords = [x, y, z, u, w]
    zero = {}
    def add(*fs):
        out = {}
        for f in fs:
            for (I, c) in f.items():
                out[I] = out.get(I, 0) + c
        return {I: s.expand(c) for (I, c) in out.items() if s.expand(c) != 0}
    def scale(c, f):
        return add({I: c * d for (I, d) in f.items()})
    def wedge(f, g):
        out = {}
        for (I, c) in f.items():
            for (J, d) in g.items():
                if set(I) & set(J):
                    continue
                k = sum((i > j for i in I for j in J))
                key = tuple(sorted(I + J))
                out[key] = out.get(key, 0) + (-1) ** k * c * d
        return add(out)
    def contract(v, f):
        return add(*[{I[:j] + I[j + 1:]: (-1) ** j * v[i] * c} for (I, c) in f.items() for (j, i) in enumerate(I)])
    def action(P, f):
        out = {}
        for (I, c) in f.items():
            for (j, i) in enumerate(I):
                for k in range(5):
                    term = {(k,): P[k, i]}
                    out = add(out, scale(c, wedge(wedge({I[:j]: 1}, term), {I[j + 1:]: 1})))
        return out
    def eq(f, g):
        assert not add(f, scale(-1, g)), add(f, scale(-1, g))
    def pair(F, G):
        return add(wedge(F[0], G[1]), scale(-1, wedge(F[1], G[0])))
    def vecform(M):
        return [{(i,): M[i][j] for i in range(3)} for j in range(2)]
    tau = {(0, 1, 2): 1}
    omega = {(3, 4): 1}
    Omega = wedge(tau, omega)
    ixOmega = contract(coords, Omega)
    M0 = s.Matrix([[0, 1], [0, 0]])
    M1 = s.Matrix([[0, 0], [1, 0]])
    M2 = s.Matrix([[1, 0], [0, -1]])
    Ms = [M0, M1, M2]
    M = x * M0 + y * M1 + z * M2
    Q = z * z + x * y
    assert M * M == Q * s.eye(2)
    J = s.Matrix([[0, 1], [-1, 0]])
    assert M.T * J + J * M == s.zeros(2)
    nu = s.symbols('nu', nonzero=True)
    M_pair_new = M / nu
    assert (M_pair_new * M_pair_new - Q / nu ** 2 * s.eye(2)).applyfunc(s.simplify) == s.zeros(2)
    assert nu * M_pair_new == M
    def A(v):
        return [scale(v[i], contract(coords, tau)) for i in range(2)]
    def Bcoef(v):
        return [wedge({(j,): (Ms[j] * v)[i] for j in range(3)}, omega) for i in range(2)]
    def B(v):
        return [contract(coords, f) for f in Bcoef(v)]
    (p0, p1, q0, q1) = s.symbols('p0 p1 q0 q1')
    p = s.Matrix([p0, p1])
    q = s.Matrix([q0, q1])
    eq(pair(A(p), B(q)), scale((p.T * J * M * q)[0], ixOmega))
    eq(pair(B(p), A(q)), scale(-(p.T * J * M * q)[0], ixOmega))
    eq(pair(A(p), A(q)), zero)
    eq(pair(B(p), B(q)), zero)
    cs = s.symbols('c0:8')
    C = [{}, {}]
    for k in range(2):
        (c0, c1, c2, c3) = cs[4 * k:4 * k + 4]
        sv = [s.Matrix([c0, c1]), s.Matrix([c2, c3]), s.Matrix([-c1, c2])]
        assert sum((Ms[j] * sv[j] for j in range(3)), s.zeros(2, 1)) == s.zeros(2, 1)
        for j in range(2):
            cv = contract([sv[i][j] for i in range(3)] + [0, 0], tau)
            C[j] = add(C[j], wedge(cv, {(3 + k,): 1}))
    Cx = [contract(coords, f) for f in C]
    eq(pair(A(p), Cx), zero)
    eq(pair(B(p), Cx), zero)
    (h, k, l) = s.symbols('h k l')
    D = s.zeros(5)
    D[3, 3] = h
    D[3, 4] = k
    D[4, 3] = l
    D[4, 4] = -h
    theta = s.symbols('theta', nonzero=True)
    phys = Q / theta
    r = s.Matrix([y / (2 * theta), x / (2 * theta), z / theta, 0, 0])
    ell = s.Matrix(1, 5, list(s.Matrix(1, 5, coords) * D))
    P = phys * D - r * ell
    assert s.simplify((s.Matrix(1, 5, coords) * r)[0] - phys) == 0
    assert all((s.simplify(v) == 0 for v in s.Matrix(1, 5, coords) * P))
    assert s.trace(P) == 0
    assert action(P, ixOmega) == {}
    from itertools import combinations
    basis = list(combinations(range(5), 3))
    zs = s.symbols('Z0:10')
    Z = dict(zip(basis, zs))
    eq(contract(coords, action(D, Z)), add(action(D, contract(coords, Z)), contract(list(ell), Z)))
    lhs = add(scale(phys, contract(coords, action(D, Z))), scale(-1, action(P, contract(coords, Z))))
    rform = {(i,): r[i] for i in range(5)}
    rhs = contract(coords, wedge(rform, contract(list(ell), Z)))
    eq(lhs, rhs)
    t = contract(list(ell), omega)
    for j in range(2):
        bcoef = Bcoef(p)[j]
        defect = contract(coords, wedge(rform, contract(list(ell), bcoef)))
        Lv = {(i,): (Ms[i] * p)[j] for i in range(3)}
        eq(defect, contract(coords, wedge(wedge(Lv, rform), t)))
        rc = wedge(rform, contract(list(ell), C[j]))
        assert set(rc).issubset({(0, 1, 2)})
        sD = rc.get((0, 1, 2), 0)
        eq(contract(coords, rc), scale(sD, contract(coords, tau)))
    (a_m, b_m, c_m, chi) = s.symbols('a_m b_m c_m chi', nonzero=True)
    assert s.simplify(-2 * b_m / (a_m * chi) * (-a_m * Q) - 2 * b_m * Q / chi) == 0
    left_sign = 1
    adjoint_skew_sign = -1
    right_required_sign = -1
    assert left_sign * adjoint_skew_sign == right_required_sign
    assert s.simplify(-c_m + a_m * c_m / a_m) == 0
    assert s.simplify(b_m * c_m / a_m - b_m * c_m / a_m) == 0
    if include_helpers:
        G = s.Matrix([[0, s.Rational(1, 2), 0], [s.Rational(1, 2), 0, 0], [0, 0, 1]])
        Kinc = s.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, -1, 0, 0], [0, 0, 1, 0]])
        cliff = Ms[0].row_join(Ms[1]).row_join(Ms[2])
        spin = s.Matrix.vstack(2 * M1, 2 * M0, M2) / 3
        assert cliff * spin == s.eye(2)
        Pi = s.eye(6) - spin * cliff
        extract = s.eye(6)[:4, :] * Pi
        assert Kinc * extract == Pi and Pi * Pi == Pi
        up = s.kronecker_product(G, s.eye(2))
        low = up.inv()
        J4 = Kinc.T * s.kronecker_product(G, J) * Kinc
        assert J4.T == -J4 and J4.det() != 0
        def getp(F, extra=()):
            return s.Matrix([F[j].get(tuple(sorted(I + extra)), 0) * sgn for (I, sgn) in [((1, 2), 1), ((0, 2), -1), ((0, 1), 1)] for j in range(2)])
        def putp(p, extra=()):
            return [{tuple(sorted(I + extra)): sgn * p[2 * i + j] for (i, (I, sgn)) in enumerate([((1, 2), 1), ((0, 2), -1), ((0, 1), 1)])} for j in range(2)]
        def getY(F, extra):
            return s.Matrix([F[j].get((i,) + extra, 0) for i in range(3) for j in range(2)])
        def putY(Y, extra):
            return [{(i,) + extra: Y[2 * i + j] for i in range(3)} for j in range(2)]
        def adds(*Fs):
            return [add(*(F[j] for F in Fs)) for j in range(2)]
        def sc(c, F):
            return [scale(c, f) for f in F]
        def eqvec(F, G):
            for (f, g) in zip(F, G):
                eq(f, g)
        def zero_matrix(M):
            assert M.applyfunc(s.expand) == s.zeros(*M.shape)
        def embeddings(R):
            Radj = J4.inv() * R.T * J4
            return (Kinc * R * extract, up * Kinc * Radj * extract * low)
        def E_R(R, F):
            (Rp, RadjY) = embeddings(R)
            out = putp(Rp * getp(F))
            for i in [3, 4]:
                out = adds(out, putY(-RadjY * getY(F, (i,)), (i,)))
            return out
        def F_R(R, F):
            (Rp, RadjY) = embeddings(R)
            out = [{}, {}]
            for i in [3, 4]:
                out = adds(out, putp(Rp * getp(F, (i,)), (i,)))
            return adds(out, putY(-RadjY * getY(F, (3, 4)), (3, 4)))
        J6 = s.kronecker_product(G, J)
        def adj6(R):
            return J6.inv() * R.T * J6
        def fullE(R, F):
            out = putp(R * getp(F))
            for i in [3, 4]:
                out = adds(out, putY(-up * adj6(R) * low * getY(F, (i,)), (i,)))
            return out
        def fullF(R, F):
            out = [{}, {}]
            for i in [3, 4]:
                out = adds(out, putp(R * getp(F, (i,)), (i,)))
            return adds(out, putY(-up * adj6(R) * low * getY(F, (3, 4)), (3, 4)))
        def fullT(R, degree, F):
            out = [{}, {}]
            for (wi, i) in [(u, 3), (w, 4)]:
                out = adds(out, [contract(coords, wedge({(i,): 1}, ff)) for ff in fullE(R.diff(wi) / degree, F)])
            return out
        (ha, hb, hc, hd, hf) = s.symbols('ha hb hc hd hf')
        H3 = s.Matrix([[ha, hb, hc], [hd, ha, hf], [2 * hf, 2 * hc, -2 * ha]])
        H5 = s.zeros(5)
        H5[:3, :3] = H3
        HH = s.kronecker_product(-H3.T, s.eye(2))
        rh = H5 * r
        jw = contract(coords, omega)
        jvec = s.Matrix([jw.get((i,), 0) for i in range(5)])
        Hb = (s.Matrix(1, 5, coords) * D * jvec)[0]
        abase = Hb / 2
        def FW(K, F):
            out = [{}, {}]
            for i in [3, 4]:
                for j in [3, 4]:
                    out = adds(out, putp(D[j, i] * K * getp(F, (i,)), (j,)))
            return out
        def FWadj(K, F):
            out = [{}, {}]
            for i in [3, 4]:
                for j in [3, 4]:
                    out = adds(out, putY(-D[j, i] * up * adj6(K) * low * getY(F, (i,)), (j,)))
            return out
        def TP(K, F):
            out = [{}, {}]
            for i in range(3):
                ffirst = FW(K, [wedge({(i,): 1}, ff) for ff in F])
                fsecond = [wedge({(i,): 1}, ff) for ff in FWadj(K, F)]
                out = adds(out, sc(abase * rh[i], [contract(coords, ff) for ff in adds(ffirst, sc(-1, fsecond))]))
            return out
        (S, T) = s.symbols('bs bt')
        mon = lambda n: [S ** (n - j) * T ** j for j in range(n + 1)]
        def coeff(p, n):
            return s.Matrix([s.Poly(s.expand(p), S, T).coeff_monomial(m) for m in mon(n)])
        def tv(p, q, r):
            return s.expand(sum(((-1) ** j * s.binomial(r, j) * s.diff(p, S, r - j, T, j) * s.diff(q, S, j, T, r - j) for j in range(r + 1))))
        def rep(fun, n):
            return s.Matrix.hstack(*[coeff(fun(p), n) for p in mon(n)])
        binary_E = rep(lambda p: S * s.diff(p, T), 3)
        binary_F = rep(lambda p: T * s.diff(p, S), 3)
        binary_H = rep(lambda p: S * s.diff(p, S) - T * s.diff(p, T), 3)
        E1 = s.Matrix([[0, 1], [0, 0]])
        F1 = E1.T
        H1 = s.diag(1, -1)
        J1 = s.Matrix([[0, 1], [-1, 0]])
        J3 = s.zeros(4)
        for j in range(4):
            J3[j, 3 - j] = (-1) ** j / s.binomial(3, j)
        def simp(X):
            return X.applyfunc(s.factor)
        def op4(p):
            return rep(lambda z: tv(p, z, 2) / 12, 3)
        def op6(p):
            return rep(lambda z: tv(p, z, 3) / 120, 3)
        g = s.symbols('g0:5')
        gen4 = sum((c * m for (c, m) in zip(g, mon(4))))
        OG = op4(gen4)
        entries = [(0, 2), (0, 1), (0, 0), (1, 0), (2, 0)]
        GG = s.symbols('o0:5')
        recovery = s.solve([OG[i, j] - v for ((i, j), v) in zip(entries, GG)], g, dict=True)[0]
        def quartic(Q):
            vals = dict(zip(GG, [Q[i, j] for (i, j) in entries]))
            return s.expand(sum((recovery[c].subs(vals) * m for (c, m) in zip(g, mon(4)))))
        assert s.expand(quartic(OG) - gen4) == 0
        def mixed5(p):
            return s.Matrix.hstack(*[coeff(tv(p, z, 1) / 4, 3) for z in mon(1)])
    bindings = locals().copy()
    return SimpleNamespace(**{name: value for name, value in bindings.items()
                              if name != 'include_helpers'})


def load_clifford_api():
    """Construct the entire Clifford context and run all its initialization assertions."""
    validate_inputs()
    return _construct(False)


def load_source_balance_api():
    """Construct the full shared Clifford/helper frame, including quartic recovery."""
    validate_inputs()
    return _construct(True)
