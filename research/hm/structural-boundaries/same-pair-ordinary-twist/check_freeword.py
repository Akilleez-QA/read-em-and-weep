#!/usr/bin/env python3
"""Independent one-parameter associator control in an invented free jet algebra.

No imports from any production/source/model module. No matrices, physical curve,
physical polynomial, owner, point, residual or detector are constructed/evaluated.
Words are formal noncommuting labels; scalar jet labels commute. Only the
universal ordered Leibniz identities in the review are checked.
"""
from fractions import Fraction as F

class WordSum:
    def __init__(self, terms=None):
        self.terms = {k: F(v) for k, v in (terms or {}).items() if v}
    @staticmethod
    def lift(x):
        return x if isinstance(x, WordSum) else WordSum({((), ()): F(x)})
    def __add__(self, other):
        other = self.lift(other)
        out = self.terms.copy()
        for key, value in other.terms.items():
            out[key] = out.get(key, F(0)) + value
        return WordSum(out)
    __radd__ = __add__
    def __neg__(self):
        return WordSum({k: -v for k, v in self.terms.items()})
    def __sub__(self, other):
        return self + (-self.lift(other))
    def __rsub__(self, other):
        return self.lift(other) - self
    def __mul__(self, other):
        other = self.lift(other)
        out = {}
        for (s, w), c in self.terms.items():
            for (t, z), d in other.terms.items():
                key = (tuple(sorted(s + t)), w + z)
                out[key] = out.get(key, F(0)) + c * d
        return WordSum(out)
    __rmul__ = __mul__
    def derivative(self, direction):
        out = {}
        for (s, w), c in self.terms.items():
            for position, jet in enumerate(s):
                name, da, db = jet
                dj = (name, da + (direction == 0), db + (direction == 1))
                key = (tuple(sorted(s[:position] + (dj,) + s[position + 1:])), w)
                out[key] = out.get(key, F(0)) + c
            for position, jet in enumerate(w):
                name, da, db = jet
                dj = (name, da + (direction == 0), db + (direction == 1))
                key = (s, w[:position] + (dj,) + w[position + 1:])
                out[key] = out.get(key, F(0)) + c
        return WordSum(out)


def scalar(name):
    return WordSum({(((name, 0, 0),), ()): 1})


def word(name):
    return WordSum({((), ((name, 0, 0),)): 1})


def da(x):
    return x.derivative(0)


def db(x):
    return x.derivative(1)


def mu(x, y):
    return F(1, 2) * (da(x) * db(y) - db(x) * da(y))


def nu(x, y):
    return F(1, 8) * (da(da(x)) * db(db(y))
                      - 2 * da(db(x)) * da(db(y))
                      + db(db(x)) * da(da(y)))


def require_zero(name, expression):
    if expression.terms:
        raise RuntimeError(name + ': nonzero remainder of ' + str(len(expression.terms)) + ' formal terms')
    print('PASS:', name)


def require_nonzero(name, expression):
    if not expression.terms:
        raise RuntimeError(name + ': bad mutation was accepted')
    print('REJECT:', name, '(' + str(len(expression.terms)) + ' formal terms)')


# Three free adjacent zeroth-order edges; composite edges use the row order.
a, b, c = [word(name) for name in ('a', 'b', 'c')]
u, v, w = [word(name) for name in ('u', 'v', 'w')]
g = {(0, 1): a, (1, 2): b, (2, 3): c,
     (0, 2): b*a, (1, 3): c*b, (0, 3): c*b*a}

# Three arbitrary scalar first coefficients and the sole scalar cocycle relation.
p, q, r = [scalar(name) for name in ('p', 'q', 'r')]
beta = {(0, 1, 2): p, (1, 2, 3): q,
        (0, 2, 3): r, (0, 1, 3): p+r-q}
chi = {t: scalar('h2_' + ''.join(map(str, t))) for t in beta}

# Arbitrary valid first lifts, recursively determined on composite edges.
U = {(0, 1): u, (1, 2): v, (2, 3): w}
U[0, 2] = v*a + b*u + mu(b, a) - p*g[0, 2]
U[1, 3] = w*b + c*v + mu(c, b) - q*g[1, 3]
U[0, 3] = w*g[0, 2] + c*U[0, 2] + mu(c, g[0, 2]) - r*g[0, 3]

for i, j, k in beta:
    require_zero('first-lift route ' + str((i, j, k)),
                 U[j, k]*g[i, j] + g[j, k]*U[i, j]
                 + mu(g[j, k], g[i, j]) - U[i, k] - beta[i, j, k]*g[i, k])

# An arbitrary second correcting edge is retained independently on every edge.
W = {edge: word('W_' + ''.join(map(str, edge))) for edge in g}


def defect(triple, second_coefficient=nu, include_gerbe_first=True):
    i, j, k = triple
    result = (W[j, k]*g[i, j] + g[j, k]*W[i, j] - W[i, k]
              + U[j, k]*U[i, j]
              + mu(U[j, k], g[i, j]) + mu(g[j, k], U[i, j])
              + second_coefficient(g[j, k], g[i, j])
              - chi[triple]*g[i, k])
    if include_gerbe_first:
        result -= beta[triple]*U[i, k]
    return result


def boundary_unscaled(D):
    return c*D[0, 1, 2] - D[1, 2, 3]*a + D[0, 2, 3] - D[0, 1, 3]


D = {t: defect(t) for t in beta}
S = chi[0, 1, 2] + chi[0, 2, 3] - chi[1, 2, 3] - chi[0, 1, 3] + p*r - q*(p+r-q)
A = mu(c, p)*g[0, 2] - g[1, 3]*mu(q, a)
identity = boundary_unscaled(D) + S*g[0, 3] + A
require_zero('full epsilon-squared associator, arbitrary h2/U/W', identity)

# The first coefficient is an ordered biderivation in scalar slots.
require_zero('left scalar product-rule error', mu(c, p*g[0, 2]) - p*mu(c, g[0, 2]) - mu(c, p)*g[0, 2])
require_zero('right scalar product-rule error', mu(q*g[1, 3], a) - q*mu(g[1, 3], a) - g[1, 3]*mu(q, a))

# Direct epsilon-squared associativity of the free Moyal coefficient.
require_zero('independent one-parameter Moyal associativity',
             nu(c, b)*a + mu(mu(c, b), a) + nu(c*b, a)
             - c*nu(b, a) - mu(c, mu(b, a)) - nu(c, b*a))

# Negative controls preserve all other formal data.
require_nonzero('reversed anomaly sign', boundary_unscaled(D) + S*g[0, 3] - A)
require_nonzero('mixed-sector factor 2 imported into same-pair anomaly', boundary_unscaled(D) + S*g[0, 3] + 2*A)
D_bad_nu = {t: defect(t, second_coefficient=lambda x, y: 2*nu(x, y)) for t in beta}
require_nonzero('wrong second-coefficient normalization 1/4', boundary_unscaled(D_bad_nu) + S*g[0, 3] + A)
D_bad_gerbe = {t: defect(t, include_gerbe_first=False) for t in beta}
require_nonzero('omitted minus beta U term', boundary_unscaled(D_bad_gerbe) + S*g[0, 3] + A)
A_bad_order = g[0, 2]*mu(c, p) - g[1, 3]*mu(q, a)
require_nonzero('reversed first anomaly word order', boundary_unscaled(D) + S*g[0, 3] + A_bad_order)
require_nonzero('omitted ordinary scalar associator', boundary_unscaled(D) + A)
print('All independent invented-freeword controls passed.')
