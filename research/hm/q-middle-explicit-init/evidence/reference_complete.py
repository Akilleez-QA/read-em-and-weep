"""Independent complete-symbol initializer; build_symbols is defined, never called."""
import sympy as s

(S, T) = s.symbols('bs bt')

mon = lambda n: [S ** (n - j) * T ** j for j in range(n + 1)]

def coeff(p, n):
    return s.Matrix([s.Poly(s.expand(p), S, T).coeff_monomial(m) for m in mon(n)])

def tv(p, q, r):
    return s.expand(sum(((-1) ** j * s.binomial(r, j) * s.diff(p, S, r - j, T, j) * s.diff(q, S, j, T, r - j) for j in range(r + 1))))

def rep(fun, n):
    return s.Matrix.hstack(*[coeff(fun(p), n) for p in mon(n)])

E = rep(lambda p: S * s.diff(p, T), 3)

F = rep(lambda p: T * s.diff(p, S), 3)

HH = rep(lambda p: S * s.diff(p, S) - T * s.diff(p, T), 3)

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

def spinrep(X):
    return s.trace(F * X) * E1 / 10 + s.trace(E * X) * F1 / 10 + s.trace(HH * X) * H1 / 20

def mixedV(X):
    v = s.trace(F * X) * S * S / 10 - s.trace(HH * X) * S * T / 10 - s.trace(E * X) * T * T / 10
    return s.Matrix.hstack(*[coeff(v * z, 3) for z in mon(1)])

def casimir_mixed(B):
    action = lambda A, A1, X: A * X - X * A1
    return action(HH, H1, action(HH, H1, B)) + 2 * (action(E, E1, action(F, F1, B)) + action(F, F1, action(E, E1, B)))

def splitmixed(B):
    cb = casimir_mixed(B)
    return (simp((24 * B - cb) / 16), simp((cb - 8 * B) / 16))

def build_symbols(f, H0, D, N, a):
    neg = [simp(f * Z * f.inv()) for Z in (E, F, HH)]

    def psl(X, b):
        (e, g, h) = b
        return simp(s.trace(h * X) * h / 20 + (s.trace(g * X) * e + s.trace(e * X) * g) / 10)

    def pskew(X):
        v = psl(X, (E, F, HH))
        aa = psl(X, neg)
        return [aa, v, simp(X - aa - v)]
    JP = -J3 / 2
    JS = -J1 / 3
    zero = s.zeros(6)
    rq = []
    rh = []

    def EC(X):
        out = s.zeros(6)
        out[:4, :4] = X
        return out

    def ES(X):
        out = s.zeros(6)
        out[4:, 4:] = X
        return out

    def E10(B):
        out = s.zeros(6)
        out[:4, 4:] = B
        return out

    def E01(B):
        out = s.zeros(6)
        out[4:, :4] = JS.inv() * B.T * JP
        return out

    def add(lst, name, M):
        lst.append((name, simp(M)))
    hp = quartic(H0)
    B = mixed5(hp)
    assert simp(op4(hp) - H0) == s.zeros(4)
    for (name, M) in [('C', EC(H0)), ('10', E10(B)), ('01', E01(B))]:
        add(rq, 'scalarH_' + name, a * M)
    X = simp(D * N - N * D)
    anti = simp(H0 * X + X * H0)
    (PA, PV, P4) = pskew(anti)
    add(rq, 'A_C5', EC(H0 * X - X * H0))
    for (name, Q) in [('A', PA), ('V', PV), ('P4', P4)]:
        add(rq, 'A_C' + name, EC(Q))
    add(rq, 'A_SV', ES(spinrep(PV)))
    (Vmix, Dmix) = splitmixed(X * B)
    for (name, Y) in [('V', Vmix), ('D5', Dmix)]:
        add(rq, 'A_10' + name, E10(Y))
        add(rq, 'A_01' + name, E01(Y))
    Q = simp(D * N + N * D + 20 * a * s.eye(4))
    sp = quartic(Q)
    assert simp(op4(sp) - Q) == s.zeros(4)
    scalar = tv(hp, sp, 4) / s.factorial(4) ** 2
    add(rq, 'D_SC', EC(scalar * s.eye(4)))
    add(rq, 'D_SS', ES(scalar * s.eye(2)))
    (PA, PV, P4) = pskew(H0 * Q - Q * H0)
    for (name, Y) in [('A', PA), ('V', PV), ('P4', P4)]:
        add(rq, 'D_C' + name, EC(Y))
    add(rq, 'D_SV', ES(spinrep(PV)))
    MV = mixedV(PV)
    add(rq, 'D_10V', E10(MV))
    add(rq, 'D_01V', E01(MV))
    (R0, R1, Z0, Z1) = s.symbols('pr0 pr1 nw0 nw1')
    Fpol = s.expand((s.Matrix([[Z0 ** 3, Z0 ** 2 * Z1, Z0 * Z1 ** 2, Z1 ** 3]]) * f.inv() * s.Matrix([R0 ** 3, 3 * R0 ** 2 * R1, 3 * R0 * R1 ** 2, R1 ** 3]))[0])
    cf = s.factor((f.T * J3 * f)[0, 3])
    assert simp(f.T * J3 * f - cf * J3) == s.zeros(4)
    cs = [s.Poly(Fpol, Z0, Z1).coeff_monomial(Z0 ** (3 - j) * Z1 ** j) for j in range(4)]
    (aa, bb, cc, dd) = cs
    disc = s.factor(bb ** 2 * cc ** 2 - 4 * aa * cc ** 3 - 4 * bb ** 3 * dd - 27 * aa ** 2 * dd ** 2 + 18 * aa * bb * cc * dd)
    theta = s.expand((cf ** 2 * disc).subs({R0: -T, R1: S}, simultaneous=True))
    d1 = tv(hp, sp, 2) / 144
    d2 = tv(hp * sp, theta, 8) / (s.factorial(8) * s.factorial(12) / s.factorial(4))
    p4 = tv(hp * sp, theta, 7) / (s.factorial(8) / s.factorial(1) * (s.factorial(12) / s.factorial(5)))
    for (name, pp) in [('Jordan', d1), ('Theta5', d2)]:
        b = mixed5(pp)
        add(rq, 'D_C' + name, EC(op4(pp)))
        add(rq, 'D_10' + name, E10(b))
        add(rq, 'D_01' + name, E01(b))
    sext = op6(p4)
    assert psl(sext, neg) == s.zeros(4)
    assert psl(sext, (E, F, HH)) == s.zeros(4)
    add(rq, 'D_CTheta4', EC(sext))
    add(rh, 'Rh_SC', a * EC(s.eye(4)))
    add(rh, 'Rh_SS', a * ES(s.eye(2)))
    add(rh, 'Rh_A', EC(X))
    add(rh, 'Rh_D5', EC(Q))
    b = mixed5(sp)
    add(rh, 'Rh_10', E10(b))
    add(rh, 'Rh_01', E01(b))
    assert len(rq) == 27 and len(rh) == 6
    return (rq, rh, theta)
