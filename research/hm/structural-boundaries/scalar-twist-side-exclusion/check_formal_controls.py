#!/usr/bin/env python3
"""Universal invented free-word and mask-metadata controls.

Only abstract noncommuting labels, commuting scalar jet labels, rational constants
and integer bit masks are used. No source/model files are read or imported; no
physical curve, actual matrix, polynomial, point, jet or residual is evaluated.
"""
from fractions import Fraction
import json


class Formal:
    """Sparse algebra: commuting scalar jets followed by an ordered free word."""
    frozen = frozenset(('ell', 'Aconst', 'Bconst'))

    def __init__(self, terms=None):
        self.terms = {key: Fraction(value) for key, value in (terms or {}).items() if value}

    @classmethod
    def coerce(cls, value):
        return value if isinstance(value, cls) else cls({((), ()): Fraction(value)})

    def __add__(self, other):
        result = self.terms.copy()
        for key, coefficient in self.coerce(other).terms.items():
            result[key] = result.get(key, Fraction(0)) + coefficient
        return Formal(result)

    __radd__ = __add__

    def __neg__(self):
        return Formal({key: -coefficient for key, coefficient in self.terms.items()})

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        result = {}
        for (scalar1, word1), coefficient1 in self.terms.items():
            for (scalar2, word2), coefficient2 in self.coerce(other).terms.items():
                key = (tuple(sorted(scalar1 + scalar2)), word1 + word2)
                result[key] = result.get(key, Fraction(0)) + coefficient1 * coefficient2
        return Formal(result)

    __rmul__ = __mul__

    def derive(self, direction):
        result = {}
        for (scalars, word), coefficient in self.terms.items():
            for index, jet in enumerate(scalars):
                name, order0, order1 = jet
                if name in self.frozen:
                    continue
                changed = (name, order0 + (direction == 0), order1 + (direction == 1))
                key = (tuple(sorted(scalars[:index] + (changed,) + scalars[index+1:])), word)
                result[key] = result.get(key, Fraction(0)) + coefficient
            for index, jet in enumerate(word):
                name, order0, order1 = jet
                changed = (name, order0 + (direction == 0), order1 + (direction == 1))
                key = (scalars, word[:index] + (changed,) + word[index+1:])
                result[key] = result.get(key, Fraction(0)) + coefficient
        return Formal(result)


def scalar(label):
    return Formal({(((label, 0, 0),), ()): 1})


def word(label):
    return Formal({((), ((label, 0, 0),)): 1})


def d0(value):
    return value.derive(0)


def d1(value):
    return value.derive(1)


def mu(left, right):
    return Fraction(1, 2) * (d0(left)*d1(right) - d1(left)*d0(right))


def nu(left, right):
    return Fraction(1, 8) * (d0(d0(left))*d1(d1(right))
                           - 2*d0(d1(left))*d0(d1(right))
                           + d1(d1(left))*d0(d0(right)))


passed, rejected = [], []


def equal(label, left, right=0):
    difference = left - right
    if difference.terms:
        raise RuntimeError(label + ': nonzero formal remainder (' + str(len(difference.terms)) + ' terms)')
    passed.append(label)


def unequal(label, left, right=0):
    if not (left - right).terms:
        raise RuntimeError(label + ': bad mutation was not rejected')
    rejected.append(label)


def series_product(left, right, star=True):
    coefficients = [Formal(), Formal(), Formal()]
    for i in range(3):
        for j in range(3-i):
            coefficients[i+j] += left[i]*right[j]
            if star and i+j+1 < 3:
                coefficients[i+j+1] += mu(left[i], right[j])
            if star and i+j+2 < 3:
                coefficients[i+j+2] += nu(left[i], right[j])
    return coefficients


# Free adjacent edges and arbitrary first scalar cocycle on a formal tetrahedron.
a, b, c = [word(label) for label in ('edge_a', 'edge_b', 'edge_c')]
u, v, w = [word(label) for label in ('lift_u', 'lift_v', 'lift_w')]
p, q, r = [scalar(label) for label in ('beta_p', 'beta_q', 'beta_r')]
ell = scalar('ell')
g = {(0, 1): a, (1, 2): b, (2, 3): c,
     (0, 2): b*a, (1, 3): c*b, (0, 3): c*b*a}
beta = {(0, 1, 2): p, (1, 2, 3): q, (0, 2, 3): r, (0, 1, 3): p+r-q}
chi = {triple: scalar('chi_' + ''.join(map(str, triple))) for triple in beta}
U = {(0, 1): u, (1, 2): v, (2, 3): w}
U[0, 2] = v*a+b*u+mu(b, a)-p*g[0, 2]
U[1, 3] = w*b+c*v+mu(c, b)-q*g[1, 3]
U[0, 3] = w*g[0, 2]+c*U[0, 2]+mu(c, g[0, 2])-r*g[0, 3]
W = {edge: word('second_' + ''.join(map(str, edge))) for edge in g}

for i, j, k in beta:
    equal('first-lift route ' + str((i, j, k)),
          U[j, k]*g[i, j]+g[j, k]*U[i, j]+mu(g[j, k], g[i, j]),
          U[i, k]+beta[i, j, k]*g[i, k])


def B(cochain):
    return c*cochain[0, 1, 2]-cochain[1, 2, 3]*a+cochain[0, 2, 3]-cochain[0, 1, 3]


def ordinary_defect(triple):
    i, j, k = triple
    return (W[j, k]*g[i, j]+g[j, k]*W[i, j]-W[i, k]
            +U[j, k]*U[i, j]+mu(U[j, k], g[i, j])+mu(g[j, k], U[i, j])
            +nu(g[j, k], g[i, j])-beta[triple]*U[i, k]-chi[triple]*g[i, k])


E = {triple: mu(beta[triple], g[triple[0], triple[2]]) for triple in beta}
D0 = {triple: ordinary_defect(triple) for triple in beta}
Dl = {triple: D0[triple]-ell*E[triple] for triple in beta}
Fraw = mu(c, p)*g[0, 2]
Graw = g[1, 3]*mu(q, a)
K = chi[0, 1, 2]+chi[0, 2, 3]-chi[1, 2, 3]-chi[0, 1, 3]+p*r-q*(p+r-q)
Al = (1+ell)*Fraw+(ell-1)*Graw

equal('correction boundary B(E)=Fraw+Graw', B(E), Fraw+Graw)
equal('ordinary full defect associator with all second edges', B(D0)+K*g[0, 3]+Fraw-Graw)
equal('symbolic constant-lambda full defect associator', B(Dl)+K*g[0, 3]+Al)
equal('scalar-slot skew symmetry', mu(p, a), -mu(a, p))
equal('scalar-slot ordered product rule', mu(p, b*a), mu(p, b)*a+b*mu(p, a))
equal('left scalar endpoint error', mu(c, p*g[0, 2])-p*mu(c, g[0, 2]), Fraw)
equal('right scalar endpoint error', mu(q*g[1, 3], a)-q*mu(g[1, 3], a), Graw)

T = {edge: [g[edge], U[edge], W[edge]] for edge in g}
left_association = series_product(T[2, 3], series_product(T[1, 2], T[0, 1]))
right_association = series_product(series_product(T[2, 3], T[1, 2]), T[0, 1])
for degree in range(3):
    equal('direct ambient-star associativity degree ' + str(degree), left_association[degree], right_association[degree])

h = [Formal.coerce(1), p, chi[0, 1, 2]]
ordinary = series_product(h, T[0, 2], star=False)
left_star = series_product(h, T[0, 2])
right_star = series_product(T[0, 2], h)
for degree in (0, 1):
    equal('left-star placement lower degree ' + str(degree), left_star[degree], ordinary[degree])
    equal('right-star placement lower degree ' + str(degree), right_star[degree], ordinary[degree])
equal('left-star placement lambda=+1', left_star[2]-ordinary[2], E[0, 1, 2])
equal('right-star placement lambda=-1', right_star[2]-ordinary[2], -E[0, 1, 2])

unequal('wrong correction-boundary sign', B(E), -Fraw-Graw)
unequal('wrong lambda-defect sign', B({t: D0[t]+ell*E[t] for t in beta})+K*g[0, 3]+Al)
unequal('wrong G coefficient lambda+1', B(Dl)+K*g[0, 3]+(1+ell)*Fraw+(ell+1)*Graw)
unequal('wrong F coefficient 1-lambda', B(Dl)+K*g[0, 3]+(1-ell)*Fraw+(ell-1)*Graw)
unequal('mixed-sector factor two', B(Dl)+K*g[0, 3]+2*Al)
unequal('omitted scalar K', B(Dl)+Al)
unequal('reversed F word order', B(Dl)+K*g[0, 3]+(1+ell)*g[0, 2]*mu(c, p)+(ell-1)*Graw)
unequal('left-star mislabeled lambda=-1', left_star[2]-ordinary[2], -E[0, 1, 2])
unequal('right-star mislabeled lambda=+1', right_star[2]-ordinary[2], E[0, 1, 2])

# Pure mask metadata: suppress a common nonzero formal symbol R; no r, x, y,
# geometric function, actual transition, or physical coefficient is constructed.
Aconst, Bconst = scalar('Aconst'), scalar('Bconst')


def edge_delta(mask1, mask2, coordinate):
    return ((mask2 >> coordinate) & 1) - ((mask1 >> coordinate) & 1)


def beta_coefficient(masks, i, j, k):
    return (Aconst*edge_delta(masks[i], masks[j], 0)*edge_delta(masks[j], masks[k], 1)
            +Bconst*edge_delta(masks[i], masks[j], 1)*edge_delta(masks[j], masks[k], 0))


def endpoint_coefficients(masks):
    first = Fraction(1, 2)*beta_coefficient(masks, 0, 1, 2)*(edge_delta(masks[2], masks[3], 0)-edge_delta(masks[2], masks[3], 1))
    second = Fraction(1, 2)*beta_coefficient(masks, 1, 2, 3)*(edge_delta(masks[0], masks[1], 1)-edge_delta(masks[0], masks[1], 0))
    return first, second


mask_rows = [
    ('QA', (0, 1, 3, 5), Fraction(1, 2)*Aconst, Formal()),
    ('QB', (0, 2, 3, 6), -Fraction(1, 2)*Bconst, Formal()),
    ('Q1', (0, 1, 2, 3), Fraction(1, 2)*Aconst, -Fraction(1, 2)*Bconst),
    ('Q2', (0, 2, 5, 7), -Fraction(1, 2)*Bconst, Fraction(1, 2)*Aconst),
]
for name, masks, expectedF, expectedG in mask_rows:
    if not all(masks[i] < masks[i+1] for i in range(3)):
        raise RuntimeError(name + ': masks not strictly increasing')
    passed.append(name + ' strictly increasing mask metadata')
    actualF, actualG = endpoint_coefficients(masks)
    equal(name + ' F coefficient', actualF, expectedF)
    equal(name + ' G coefficient', actualG, expectedG)
    equal(name + ' scalar cocycle', beta_coefficient(masks, 0, 1, 2)+beta_coefficient(masks, 0, 2, 3),
          beta_coefficient(masks, 1, 2, 3)+beta_coefficient(masks, 0, 1, 3))

F1, G1 = endpoint_coefficients((0, 1, 2, 3))
F2, G2 = endpoint_coefficients((0, 2, 5, 7))
equal('joint lambda=-1 Q1 leaves B', -2*G1, Bconst)
equal('joint lambda=-1 Q2 leaves minus A', -2*G2, -Aconst)
unequal('Q1 G sign reversed', G1, Fraction(1, 2)*Bconst)
unequal('Q2 G sign reversed', G2, -Fraction(1, 2)*Aconst)
unequal('Q2 endpoints interchanged', F2, G2)

print(json.dumps({'scope': 'invented formal free words and integer mask metadata only',
                  'passed_count': len(passed), 'rejected_mutation_count': len(rejected),
                  'passed': passed, 'rejected_mutations': rejected}, indent=2, sort_keys=True))
