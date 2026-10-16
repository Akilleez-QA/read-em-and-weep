"""Independent abstract checks. No physical source inputs or imports."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations
import json

Z = ((F(0), F(0)), (F(0), F(0)))
h = ((F(1), F(0)), (F(0), F(-1)))
e = ((F(0), F(1)), (F(0), F(0)))
f = ((F(0), F(0)), (F(1), F(0)))
PERMS = tuple(permutations(range(4)))
PATTERN = ((0, 2, 1, 3, 1), (0, 3, 1, 2, -1),
           (1, 2, 0, 3, -1), (1, 3, 0, 2, 1))


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))


def add(*xs):
    return tuple(tuple(sum(x[i][j] for x in xs) for j in range(2)) for i in range(2))


def scale(c, a):
    return tuple(tuple(c * x for x in row) for row in a)


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def tr(a):
    return a[0][0] + a[1][1]


def bracket(a, b):
    return add(mul(a, b), scale(-1, mul(b, a)))


def omega(H, J, a, b, c, d):
    terms = ((a, c, b, d, 1), (a, d, b, c, -1),
             (b, c, a, d, -1), (b, d, a, c, 1))
    return scale(F(1, 8), add(*(scale(s, bracket(J[tuple(sorted((i, j)))],
                                                     H[tuple(sorted((k, l)))]))
                               for i, j, k, l, s in terms)))


def omega_checks():
    slots = tuple(combinations(range(4), 2))
    count = 0
    for hs in slots:
        for js in slots:
            for hb in (h, e, f):
                for jb in (h, e, f):
                    H = {s: Z for s in slots}
                    J = {s: Z for s in slots}
                    H[hs], J[js] = hb, jb
                    total = add(*(scale(sign(p), omega(H, J, *p)) for p in PERMS))
                    require(total == Z, "24-term Omega alternation")
                    value = omega(H, J, 0, 1, 2, 3)
                    require(omega(H, J, 1, 0, 2, 3) == scale(-1, value), "pair reversal")
                    require(omega(H, J, 2, 3, 0, 1) == value, "pair exchange")
                    count += 1
    return count


def atom(name, *indices):
    return (name,) + (tuple(sorted(indices)) if name in ("H", "J") else indices)


def q2_terms(a, b, c, d):
    Ua, Ub, Uc, Ud = (atom("U", i) for i in (a, b, c, d))
    La, Lb, Lc, Ld = (atom("L", i) for i in (a, b, c, d))
    H, J = atom("H", c, d), atom("J", a, b)
    # A term is coefficient * trace(first * second) * matrix_factor.
    return ((1, Ua, Ub, H), (1, Ua, Lb, H), (1, Ub, La, H),
            (-1, H, Ua, Lb), (-1, H, Ub, La),
            (1, Lc, Ld, J), (1, Uc, Ld, J), (1, Ud, Lc, J),
            (-1, J, Lc, Ud), (-1, J, Ld, Uc))


def q2_check():
    coefficients = Counter()
    for p in PERMS:
        for a, b, c, d, s in PATTERN:
            for coefficient, x, y, z in q2_terms(p[a], p[b], p[c], p[d]):
                key = (tuple(sorted((x, y))), z)
                coefficients[key] += sign(p) * s * coefficient
    require(all(c == 0 for c in coefficients.values()), "formal Q2 alternation")
    return len(coefficients)


def K(A, a, b):
    return scale(F(1, 4), bracket(A[a], A[b]))


def T4(L, U, a, b, c, d):
    return scale(F(1, 4), add(
        scale(tr(mul(U[a], K(U, c, d))), L[b]),
        scale(-tr(mul(U[b], K(U, c, d))), L[a]),
        scale(tr(mul(L[b], K(L, c, d))), U[a]),
        scale(-tr(mul(L[a], K(L, c, d))), U[b])))


def curvature_trace(L, U, a, b):
    return (tr(mul(U[a], L[b])) - tr(mul(U[b], L[a]))) / 4


def quartic(L, U, a, b, c, d):
    V = [add(x, y) for x, y in zip(L, U)]
    return add(scale(F(1, 2), add(bracket(K(U, a, b), K(L, c, d)),
                                 bracket(K(U, c, d), K(L, a, b)))),
               T4(L, U, a, b, c, d), T4(L, U, c, d, a, b),
               scale(-curvature_trace(L, U, c, d), K(V, a, b)),
               scale(-curvature_trace(L, U, a, b), K(V, c, d)))


def quartic_check():
    L, U = [h, e, f, Z], [Z, Z, Z, h]
    values = [scale(sign(p), quartic(L, U, *p)) for p in PERMS]
    histogram = Counter(values)
    require(histogram == Counter({scale(F(-1, 8), h): 16, Z: 8}), "quartic histogram")
    require(scale(F(1, 24), add(*values)) == scale(F(-1, 12), h), "quartic average")


if __name__ == "__main__":
    cases = omega_checks()
    monomials = q2_check()
    quartic_check()
    print(json.dumps({"status": "PASS", "omega_basis_pairs": cases,
                      "permutations_per_pair": 24, "q2_formal_monomials": monomials,
                      "quartic_average": "-h/12", "source_evaluation": False}))
