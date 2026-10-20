"""Independent invented-word and abstract-mask controls.

Only formal words, scalar-jet labels, and rational coefficients occur here.
No source/model files, primitive entries, actual matrices, physical
polynomials, points, jets, residuals, or source programs are read/run.
"""

from fractions import Fraction as Q


def add(*items):
    out = {}
    for item in items:
        for key, value in item.items():
            out[key] = out.get(key, Q(0)) + value
            if not out[key]:
                del out[key]
    return out


def scale(c, item):
    return {key: Q(c) * value for key, value in item.items() if c * value}


def word(*letters):
    return {tuple(letters): Q(1)}


def product(left, right):
    out = {}
    for a, ac in left.items():
        for b, bc in right.items():
            out = add(out, {a + b: ac * bc})
    return out


def derivative(axis, item):
    out = {}
    for letters, coefficient in item.items():
        for k, letter in enumerate(letters):
            differentiated = letters[:k] + (letter + "_d" + str(axis),) + letters[k + 1:]
            out = add(out, {differentiated: coefficient})
    return out


def scalar_mu(scalars, matrix_word):
    """mu(scalar, word) with central formal scalar-jet labels."""
    out = {}
    for scalar, coefficient in scalars.items():
        for axis, other, sign in ((0, 1, 1), (1, 0, -1)):
            for letters, wc in derivative(other, matrix_word).items():
                out = add(out, {((scalar, axis), letters): coefficient * wc * Q(sign, 2)})
    return out


def surround(left, item, right):
    out = {}
    for l, lc in left.items():
        for (jet, letters), coefficient in item.items():
            for r, rc in right.items():
                out = add(out, {(jet, l + letters + r): lc * coefficient * rc})
    return out


def require(label, condition):
    if not condition:
        raise RuntimeError(label)
    print("PASS:", label)


unit = word()
A, B, C = word("A"), word("B"), word("C")
BA, CB, CBA = product(B, A), product(C, B), product(C, product(B, A))
x, y, z = {"x": Q(1)}, {"y": Q(1)}, {"z": Q(1)}
t = {"y": Q(1), "z": Q(1), "x": Q(-1)}  # x+t=y+z

# Multiplying the normalized Cech identity by the total transition eliminates
# all inverses.  This computes its four ordered terms independently.
delta_N = add(
    surround(unit, scalar_mu(y, CB), A),
    scale(-1, scalar_mu(t, CBA)),
    scalar_mu(z, CBA),
    scale(-1, surround(C, scalar_mu(x, BA), unit)),
)
F = scale(-1, surround(unit, scalar_mu(x, C), BA))
G = surround(CB, scalar_mu(y, A), unit)
require("scalar placement coboundary is -F-G", delta_N == scale(-1, add(F, G)))
require("ordinary associator is F-G and lambda coefficient is F+G",
        add(F, scale(-1, G), scale(-1, delta_N)) == scale(2, F))
require("left scalar star gives 2F", add(F, scale(-1, G), scale(-1, delta_N)) == scale(2, F))
require("right scalar star gives -2G", add(F, scale(-1, G), delta_N) == scale(-2, G))
require("sign-reversed lambda coefficient is detected", delta_N != add(F, G))
require("mixed-sector doubling is detected", delta_N != scale(-2, add(F, G)))
require("endpoint word-order reversal is detected",
        F != scale(-1, surround(BA, scalar_mu(x, C), unit)))

# Keep every second edge independent.  These are invented word symbols.
X, Y, Z, P, Qedge, R = (word(s) for s in ("X", "Y", "Z", "P", "Q", "R"))
d_ijk = add(product(Y, A), product(B, X), scale(-1, P))
d_jkl = add(product(Z, B), product(C, Y), scale(-1, Qedge))
d_ikl = add(product(Z, BA), product(C, P), scale(-1, R))
d_ijl = add(product(Qedge, A), product(CB, X), scale(-1, R))
boundary = add(product(C, d_ijk), scale(-1, product(d_jkl, A)), d_ikl, scale(-1, d_ijl))
require("all six independent second edges cancel", boundary == {})


# Abstract binary labels only; coefficients are ordered pairs for independent
# formal parameters alpha and beta.  This does not evaluate a geometric model.
def bits(mask):
    return mask & 1, (mask >> 1) & 1


def edge(i, j):
    a, b = bits(i), bits(j)
    return b[0] - a[0], b[1] - a[1]


def cup(i, j, k):
    u, v = edge(i, j), edge(j, k)
    return Q(u[0] * v[1]), Q(u[1] * v[0])


def vscale(c, vector):
    return tuple(c * x for x in vector)


def fg(i, j, k, l):
    u, v = edge(i, j), edge(k, l)
    return vscale(Q(v[0] - v[1], 2), cup(i, j, k)), vscale(Q(u[1] - u[0], 2), cup(j, k, l))


expected = {
    (0, 1, 3, 5): ((Q(1, 2), Q(0)), (Q(0), Q(0))),
    (0, 2, 3, 6): ((Q(0), Q(-1, 2)), (Q(0), Q(0))),
    (0, 1, 2, 3): ((Q(1, 2), Q(0)), (Q(0), Q(-1, 2))),
    (0, 2, 5, 7): ((Q(0), Q(-1, 2)), (Q(1, 2), Q(0))),
}
for labels, wanted in expected.items():
    require("abstract mask coefficients " + str(labels), fg(*labels) == wanted)
    i, j, k, l = labels
    sums = tuple(cup(i, j, k)[n] + cup(i, k, l)[n] - cup(j, k, l)[n] - cup(i, j, l)[n] for n in (0, 1))
    require("ordered cup cocycle " + str(labels), sums == (Q(0), Q(0)))

require("swapping ordered cup slots changes the primary witness", fg(0, 1, 2, 3)[0] != (Q(0), Q(1, 2)))
print("All independent formal controls passed.")
