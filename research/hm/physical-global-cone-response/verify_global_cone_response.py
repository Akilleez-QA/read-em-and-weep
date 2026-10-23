#!/usr/bin/env python3
"""Exact bounded diagnostics for the global cone source-response interface.

Characters, formal free q-polynomial cochains, and immutable source integrity
only. No actual HM coefficients, points, matrices, source ranks, primitives or
response values. Acyclicity, geometric comparison and physical weight-four
vanishing are written source-backed inputs, not inferred by this script.
"""
from fractions import Fraction as F
from time import perf_counter


class Qphi:
    # a+b*phi with phi^2=phi+1.
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    @staticmethod
    def coerce(x):
        return x if isinstance(x, Qphi) else Qphi(x)

    def __add__(self, x):
        x = self.coerce(x)
        return Qphi(self.a+x.a, self.b+x.b)

    __radd__ = __add__

    def __neg__(self):
        return Qphi(-self.a, -self.b)

    def __sub__(self, x):
        return self+-self.coerce(x)

    def __rsub__(self, x):
        return self.coerce(x)+-self

    def __mul__(self, x):
        x = self.coerce(x)
        return Qphi(self.a*x.a+self.b*x.b,
                    self.a*x.b+self.b*x.a+self.b*x.b)

    __rmul__ = __mul__

    def __truediv__(self, x):
        # Only rational denominators are needed.
        return Qphi(self.a/F(x), self.b/F(x))

    def __pow__(self, n):
        out = Qphi(1)
        for _ in range(n):
            out = out*self
        return out

    def __eq__(self, x):
        x = self.coerce(x)
        return (self.a, self.b) == (x.a, x.b)


phi = Qphi(0, 1)
phibar = 1-phi
sizes = [1, 15, 20, 12, 12]
chars = {
    '1': [1, 1, 1, 1, 1],
    'A': [3, -1, 0, phi, phibar],
    'V': [3, -1, 0, phibar, phi],
    'P': [4, 0, 1, -1, -1],
    'D': [5, 1, -1, 0, 0],
}
chars = {k: [Qphi.coerce(v) for v in c] for k, c in chars.items()}


def add(*cs):
    return [sum((c[i] for c in cs), Qphi()) for i in range(5)]


def sub(c, d):
    return [x-y for x, y in zip(c, d)]


def tensor(c, d):
    return [x*y for x, y in zip(c, d)]


def times(n, c):
    return [n*x for x in c]


def inner(c, d):
    return sum((n*x*y for n, x, y in zip(sizes, c, d)), Qphi())/60


def binary_sym(n, two):
    if n == 0:
        return chars['1']
    prev, out = chars['1'], two
    for _ in range(1, n):
        prev, out = out, sub(tensor(two, out), prev)
    return out



checks = 0
negatives = 0


def eq(x, y, label):
    global checks
    if x != y:
        raise AssertionError(label)
    checks += 1


def ne(x, y, label):
    global negatives
    if x == y:
        raise AssertionError(label)
    negatives += 1


def rejects(fn, label):
    global negatives
    try:
        fn()
    except ValueError:
        negatives += 1
        return
    raise AssertionError(label)


# Free modules over Q[q]. Labels are universal generators, never HM data.
def atom(name, q=0):
    return {(q, name): F(1)}


def plus(*vectors):
    out = {}
    for v in vectors:
        for k, c in v.items():
            out[k] = out.get(k, F(0)) + c
    return {k: c for k, c in out.items() if c}


def scale(n, v):
    return {k: n*c for k, c in v.items() if n*c}


def qmul(v):
    return {(q+1, name): c for (q, name), c in v.items()}


def restrict(v):
    return {(q, name): c for (q, name), c in v.items() if q == 0}


def qdivide(v):
    if restrict(v):
        raise ValueError("not in the q-image")
    return {(q-1, name): c for (q, name), c in v.items()}


# The differential encodes a generic compatible pair and a generic lift change.
# This is a free sign/q-divisibility diagnostic, not a chosen actual primitive.
DERIVATIVES = {
    "E": plus(atom("S"), scale(-1, atom("W", 1))),
    "Y": atom("dY"),
    "S": {},
    "W": {},
    "dY": {},
}


def deriv(v):
    out = {}
    for (q, name), c in v.items():
        for (power, target), coeff in DERIVATIVES[name].items():
            key = (q+power, target)
            out[key] = out.get(key, F(0)) + c*coeff
    return {k: c for k, c in out.items() if c}


def cone_deriv(v):
    return restrict(deriv(v))


def source_integrity():
    import hashlib
    import json
    from pathlib import Path
    here = Path(__file__).resolve().parent
    manifest = json.loads((here/"SOURCE-MANIFEST.json").read_text())
    for spec in manifest["inputs"]:
        data = (here/"inputs"/(spec["name"]+".md")).read_bytes()
        eq(len(data), spec["bytes"], spec["name"]+" byte length")
        eq(hashlib.sha256(data).hexdigest(), spec["sha256"],
           spec["name"]+" sha256")
        blob = b"blob "+str(len(data)).encode()+b"\x00"+data
        eq(hashlib.sha1(blob).hexdigest(), spec["git_blob"],
           spec["name"]+" Git blob")


def main():
    start = perf_counter()
    source_integrity()
    one, a, v, p, d = (chars[k] for k in ["1", "A", "V", "P", "D"])
    for name, c in chars.items():
        for other, e in chars.items():
            eq(inner(c, e), int(name == other), "character orthogonality")
    squares, cubes = [0, 0, 2, 4, 3], [0, 1, 0, 4, 3]
    sym3a = [(a[j]**3+3*a[j]*a[squares[j]]+2*a[cubes[j]])/6
             for j in range(5)]
    eq(sym3a, add(a, v, p), "Sym3 A")
    r = tensor(sym3a, d)
    eq(r, add(times(3, a), times(3, v), times(3, p), times(4, d)),
       "full polynomial coefficient module")
    eq(r[0], 50, "R dimension")
    m2 = add(a, times(2, v), times(3, p), times(4, d))
    m4 = add(times(2, v), times(4, p), times(3, d))
    kernel = add(a, d)
    image = add(times(2, v), times(3, p), times(3, d))
    eq(sub(m2, kernel), image, "actual q image character")
    eq(sub(m4, image), p, "actual cone H1 positive character")
    eq(sub(m2, m4), sub(kernel, p), "cone cohomology Euler check")
    eq(m2[0], 41, "positive ambient H1 at twist 2")
    eq(m4[0], 37, "positive ambient H1 at twist 4")
    eq(kernel[0], 8, "positive cone H0")
    eq(p[0], 4, "positive cone H1")
    eq(inner(r, kernel), 7, "compatible cohomology family torsor")
    eq(inner(r, p), 3, "cone obstruction family dimension")
    eq(inner(r, image), 27, "supplied W ambient compatibility sector")
    eq(inner(r, m4), 30, "full ambient target family dimension")
    eq(inner(r, m2), 34, "ambient candidate W cohomology family dimension")
    ne(p, times(0, one), "closed cone source not automatically exact")
    ne(m2[0], 0, "termwise acyclicity is not H1 B(2) vanishing")
    ne(inner(r, p), p[0], "family obstruction dimension not output dimension")
    ne(inner(r, image), 0, "cone quotient does not test supplied W defect")

    # Numerical inequalities in the cited termwise Bott premise only.
    # These do not replace Bott theory or its actual bundle identifications.
    for t in (2, 4):
        for partition in ((2, 2), (2, 1, 1), (1, 1, 1, 1)):
            eq(t+1 > max(partition), True, "End(K) Bott dominance")
        for degree in (t-1, t, t+1):
            eq(degree >= 0, True, "line term nonnegative twist")
    eq((4-2, 4, 2), (2, 4, 2), "q twist and recovered W twist")

    # Coefficientwise polynomial operations commute with restriction and d.
    for name in DERIVATIVES:
        x = atom(name)
        eq(deriv(deriv(x)), {}, "d squared zero")
        eq(deriv(qmul(x)), qmul(deriv(x)), "q-linear differential")
        eq(cone_deriv(restrict(x)), restrict(deriv(x)),
           "restriction commutes with d")
        eq(qdivide(qmul(x)), x, "unique inverse on q image")
    E, Y, S, W = (atom(name) for name in ("E", "Y", "S", "W"))
    eq(cone_deriv(restrict(E)), restrict(S), "cone primitive equation")
    numerator = plus(S, scale(-1, deriv(E)))
    eq(restrict(numerator), {}, "cone primitive forces q-divisibility")
    recovered = qdivide(numerator)
    eq(recovered, W, "recover W with correct sign")
    eq(deriv(recovered), {}, "recovered W closed")
    eq(deriv(E), plus(S, scale(-1, qmul(recovered))),
       "reconstructed ambient compatibility")
    changed_lift = plus(E, qmul(Y))
    changed_w = qdivide(plus(S, scale(-1, deriv(changed_lift))))
    eq(restrict(changed_lift), restrict(E), "lift difference vanishes on cone")
    eq(changed_w, plus(W, scale(-1, deriv(Y))), "W changes by minus dY")
    eq(deriv(changed_w), {}, "changed W remains closed")
    eq(restrict(plus(S, scale(-1, qmul(atom("dY"))))),
       restrict(S), "any qW change is invisible on the cone")
    ne(qdivide(plus(deriv(E), scale(-1, S))), W,
       "wrong recovery numerator sign rejected")
    ne(changed_w, plus(W, deriv(Y)), "wrong lift-change sign rejected")
    rejects(lambda: qdivide(S), "nondivisible numerator must be rejected")
    rejects(lambda: qdivide(plus(S, qmul(W))),
            "a nonzero constant term cannot be discarded before division")

    # Entire families use coefficient labels, not parameter values:
    # linearity of q-division is enough to preserve every polynomial degree.
    mixed = plus(scale(F(2, 3), E), scale(F(-5, 7), qmul(Y)))
    eq(restrict(deriv(mixed)), cone_deriv(restrict(mixed)),
       "linear coefficient families commute with restriction")
    eq(qdivide(qmul(mixed)), mixed, "coefficientwise lift has no denominator in parameters")
    elapsed = perf_counter()-start
    if elapsed >= 10:
        raise RuntimeError("bounded diagnostic exceeded ten-second guard")
    print(f"PASS: {checks} exact integrity/character/q-cochain checks; "
          f"{negatives} negative controls.")
    print("No actual HM evaluation; geometry and physical matching remain written inputs.")


if __name__ == "__main__":
    main()
