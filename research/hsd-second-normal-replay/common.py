"""Exact Laurent arithmetic and the pinned plane geometry.

The formulas are the ones displayed in the source chart at 6b69eefd
(formal-chart.md) and the first-normal covectors displayed at 22b80083.
No second-normal checker is imported.
"""

from fractions import Fraction


def F(value):
    if isinstance(value, Fraction):
        return value
    return Fraction(str(value))


def add(p, q):
    if not q:
        return p
    if not p:
        return dict(q)
    out = dict(p)
    for exp, coef in q.items():
        total = out.get(exp, 0) + coef
        if total:
            out[exp] = total
        else:
            out.pop(exp, None)
    return out


def scale(p, coef):
    coef = F(coef)
    if coef == 0 or not p:
        return {}
    return {exp: value * coef for exp, value in p.items()}


def mul(p, q):
    """Multiply two polynomials on the same exponent length."""
    if not p or not q:
        return {}
    out = {}
    for e, a in p.items():
        for f, b in q.items():
            g = tuple(x + y for x, y in zip(e, f))
            total = out.get(g, 0) + a * b
            if total:
                out[g] = total
            else:
                out.pop(g, None)
    return out


def mul_base(ham, scalar):
    """Multiply an 8-exponent Hamiltonian by a 4-exponent base scalar."""
    if not ham or not scalar:
        return {}
    out = {}
    for e, a in ham.items():
        for f, b in scalar.items():
            g = (e[0] + f[0], e[1] + f[1], e[2] + f[2], e[3] + f[3], *e[4:])
            total = out.get(g, 0) + a * b
            if total:
                out[g] = total
            else:
                out.pop(g, None)
    return out


def shift(p, dz=0, dX=0, dY=0, dW=0):
    if not p or (dz == dX == dY == dW == 0):
        return dict(p)
    return {
        (e[0] + dz, e[1] + dX, e[2] + dY, e[3] + dW, *e[4:]): c
        for e, c in p.items()
    }


def power(p, n):
    if not p:
        raise ValueError("power of the zero polynomial")
    width = len(next(iter(p)))
    ans = {tuple(0 for _ in range(width)): Fraction(1)}
    for _ in range(n):
        ans = mul(ans, p)
    return ans


def mono4(z=0, X=0, Y=0, W=0, coef=1):
    coef = F(coef)
    if coef == 0:
        return {}
    return {(z, X, Y, W): coef}


def mono8(base, frame, coef=1):
    coef = F(coef)
    if coef == 0:
        return {}
    return {tuple(base) + tuple(frame): coef}


ZERO4 = [{}, {}, {}, {}]
ONE4 = mono4()
Z4 = mono4(z=1)
X4 = mono4(X=1)
Y4 = mono4(Y=1)
W4 = mono4(W=1)


def deriv_frame(ham, index):
    pos = 4 + index
    out = {}
    for exp, coef in ham.items():
        n = exp[pos]
        if n:
            ee = list(exp)
            ee[pos] = n - 1
            out[tuple(ee)] = coef * n
    return out


def frame_basis(index):
    frame = [0, 0, 0, 0]
    frame[index] = 1
    return {(0, 0, 0, 0, *frame): Fraction(1)}


def to_vector(ham):
    """Read a fiber-linear Hamiltonian as a B-vector of base scalars."""
    vec = [{}, {}, {}, {}]
    for exp, coef in ham.items():
        frame = exp[4:]
        degree = sum(frame)
        if degree == 0:
            raise ValueError(f"scalar term in a vector: {exp} {coef}")
        if degree != 1:
            raise ValueError(f"frame degree {degree} in a vector: {exp}")
        slot = frame.index(1)
        base = exp[:4]
        vec[slot] = add(vec[slot], {base: coef})
    return vec


def add_vec(a, b):
    return [add(a[i], b[i]) for i in range(4)]


def scale_vec(vec, coef):
    return [scale(component, coef) for component in vec]


def mul_vec(vec, scalar):
    return [mul(component, scalar) for component in vec]


def vec_is_zero(vec):
    return all(not component for component in vec)


def vec_eq(a, b):
    return all(a[i] == b[i] for i in range(4))


S4 = add(power(X4, 2), power(Y4, 2))
F4 = mul(X4, Y4)
A0 = add(power(X4, 3), power(Y4, 3))
G4 = add(S4, scale(mul(Z4, power(W4, 2)), -1))
C4 = add(
    add(power(S4, 2), mul(mul(Z4, S4), power(W4, 2))),
    mul(power(Z4, 2), power(W4, 4)),
)
W6 = power(W4, 6)
S3 = power(S4, 3)


def L_U(variable):
    """L_U = F (F^2 - S^2 - 2 S U^2), U = X or Y."""
    inside = add(
        add(power(F4, 2), scale(power(S4, 2), -1)),
        scale(mul(S4, power(variable, 2)), -2),
    )
    return mul(F4, inside)


LX = L_U(X4)
LY = L_U(Y4)


def lambda_covector(chart, index):
    """Covector on (E0, E1, E2) with λ(r_E) = 1, displayed at 22b80083."""
    if chart == "finite":
        if index == 0:
            return [shift(power(Z4, 3), dX=-6), shift(scale(C4, -1), dX=-6), shift(LX, dX=-8)]
        if index == 1:
            return [shift(power(Z4, 3), dY=-6), shift(scale(C4, -1), dY=-6), shift(LY, dY=-8)]
        if index == 2:
            return [shift(ONE4, dW=-6), {}, {}]
    elif chart == "infinity":
        if index == 0:
            return [shift(ONE4, dX=-6), {}, shift(LX, dX=-8)]
        if index == 1:
            return [shift(ONE4, dY=-6), {}, shift(LY, dY=-8)]
        if index == 2:
            return [shift(ONE4, dz=-3, dW=-6), shift(C4, dz=-2, dW=-6), {}]
    raise ValueError((chart, index))


def relation(chart):
    """r = (-a0, r_E) in (P, E0, E1, E2)."""
    if chart == "finite":
        return [scale(A0, -1), W6, scale(G4, -1), F4]
    if chart == "infinity":
        return [scale(A0, -1), S3, scale(shift(G4, dz=-1), -1), F4]
    raise ValueError(chart)


def dot3(covector, vector):
    total = {}
    for left, right in zip(covector, vector):
        total = add(total, mul(left, right))
    return total


def omega_pairs(chart):
    """Ω(Ei, Ej) for i < j, frame indices 0=P, 1=E0, 2=E1, 3=E2."""
    if chart == "finite":
        return {(1, 2): F4, (1, 3): G4, (2, 3): W6}
    if chart == "infinity":
        return {(1, 2): F4, (1, 3): shift(G4, dz=-1), (2, 3): S3}
    raise ValueError(chart)


def omega_on_q(chart, index):
    """Ω(B, q) = (1, a0 λ0, a0 λ1, a0 λ2) on the named coordinate chart."""
    lam = lambda_covector(chart, index)
    return [ONE4, mul(A0, lam[0]), mul(A0, lam[1]), mul(A0, lam[2])]


def poisson(p, q, omega):
    """grad(p)^T Ω grad(q). p and q are 8-exponent Hamiltonians."""
    dp = [deriv_frame(p, i) for i in range(4)]
    dq = [deriv_frame(q, i) for i in range(4)]
    ans = {}
    for (i, j), weight in omega.items():
        bracket = add(mul(dp[i], dq[j]), scale(mul(dp[j], dq[i]), -1))
        ans = add(ans, mul_base(bracket, weight))
    return ans


def action_on_vector(eta, vec, omega):
    if not eta or vec_is_zero(vec):
        return [{}, {}, {}, {}]
    acc = [{}, {}, {}, {}]
    fields = []
    for k in range(4):
        if not vec[k]:
            fields.append(None)
            continue
        fields.append(to_vector(poisson(eta, frame_basis(k), omega)))
    for k, field in enumerate(fields):
        if field is None:
            continue
        for i in range(4):
            acc[i] = add(acc[i], mul(field[i], vec[k]))
    return acc


def action_on_q(eta, q_coeff, omega_q):
    if not eta or not q_coeff:
        return [{}, {}, {}, {}]
    acc = [{}, {}, {}, {}]
    for i in range(4):
        if not omega_q[i]:
            continue
        deriv = mul_base(deriv_frame(eta, i), omega_q[i])
        field = to_vector(deriv)
        for j in range(4):
            acc[j] = add(acc[j], mul(field[j], q_coeff))
    return acc


def action(eta, vec, omega, q_coeff=None, omega_q=None):
    out = action_on_vector(eta, vec, omega)
    if q_coeff and omega_q is not None:
        out = add_vec(out, action_on_q(eta, q_coeff, omega_q))
    return out


V_E0 = [{}, ONE4, {}, {}]


def apply_TB(vec):
    """Infinity-to-finite matrix: diag(z^3, 1, z^4, z^3) plus TB[E0, E1] = z C."""
    p, e0, e1, e2 = vec
    return [
        shift(p, dz=3),
        add(e0, mul(mul(Z4, C4), e1)),
        shift(e1, dz=4),
        shift(e2, dz=3),
    ]


def apply_TU(vec):
    """Vector transport TU = z^{-1} TB."""
    return [shift(component, dz=-1) for component in apply_TB(vec)]


def quotient_by_F(residual):
    """Candidate scalar f = (E2 component) / (X Y), since r_E2 = F = XY."""
    return shift(residual[3], dX=-1, dY=-1)


def relation_holds(residual, chart):
    """Exact equality residual = f r over the Laurent polynomial ring."""
    if vec_is_zero(residual):
        return True, {}
    scalar = quotient_by_F(residual)
    produced = mul_vec(relation(chart), scalar)
    return vec_eq(produced, residual), scalar


def plane_regular(poly, inverted):
    """Non-inverted plane coordinates X=1, Y=2, W=3 keep nonnegative exponents."""
    for exp in poly:
        for offset, index in ((1, 1), (2, 2), (3, 3)):
            if index not in inverted and exp[offset] < 0:
                return False
    return True


def scalar_regular_on(poly, open_indices, z_mode):
    # Opens 0, 1, 2 invert X, Y, W, which sit at exponent positions 1, 2, 3.
    inverted = {index + 1 for index in open_indices}
    if not plane_regular(poly, inverted):
        return False
    for exp in poly:
        if z_mode == "nonnegative" and exp[0] < 0:
            return False
        if z_mode == "nonpositive" and exp[0] > 0:
            return False
    return True


def frac_str(coef):
    coef = F(coef)
    if coef.denominator == 1:
        return str(coef.numerator)
    return f"{coef.numerator}/{coef.denominator}"


def pack_poly(poly):
    return [[list(exp), frac_str(coef)] for exp, coef in sorted(poly.items())]


def unpack_poly(packed):
    poly = {}
    for exp, coef in packed:
        value = F(coef)
        if value:
            poly[tuple(exp)] = poly.get(tuple(exp), 0) + value
    return poly


def pack_vec(vec):
    return [pack_poly(component) for component in vec]


def unpack_vec(packed):
    return [unpack_poly(component) for component in packed]


PAIRS = ((0, 1), (0, 2), (1, 2))
PLANES = (0, 1, 2)
DIRECTIONS = ("1", "a", "b", "c", "d")
MONOMIALS = (
    "1",
    "a",
    "b",
    "c",
    "d",
    "a*a",
    "a*b",
    "a*c",
    "a*d",
    "b*b",
    "b*c",
    "b*d",
    "c*c",
    "c*d",
    "d*d",
)


def monomial_key(left, right):
    a, b = DIRECTIONS[left], DIRECTIONS[right]
    if a == "1" and b == "1":
        return "1"
    if a == "1":
        return b
    if b == "1":
        return a
    if DIRECTIONS.index(a) > DIRECTIONS.index(b):
        a, b = b, a
    if a == b:
        return f"{a}*{b}"
    return f"{a}*{b}"


def transport_identity_literal():
    """Hand expansion of S^3 - z^3 W^6.

    S = X^2 + Y^2, so S^3 = X^6 + 3 X^4 Y^2 + 3 X^2 Y^4 + Y^6.
    The cross terms in g C cancel, leaving this polynomial.
    """
    return {
        (0, 6, 0, 0): Fraction(1),
        (0, 4, 2, 0): Fraction(3),
        (0, 2, 4, 0): Fraction(3),
        (0, 0, 6, 0): Fraction(1),
        (3, 0, 0, 6): Fraction(-1),
    }


def g_times_c():
    return mul(G4, C4)
