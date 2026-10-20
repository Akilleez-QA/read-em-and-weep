#!/usr/bin/env python3
"""Bounded producer controls in invented scalar/freeword algebra and mask metadata.

No production imports, model/source reads, actual matrices, physical curve
polynomials, physical q/r values, points, jets, residuals or detectors. The
formal letters below have no assigned geometric values. The mask computations
use only four-bit integers and their differences. Python standard library only.
"""
from fractions import Fraction as F


class Formal:
    """Commuting scalar jet labels together with ordered free-word jet labels."""
    def __init__(self, terms=None):
        self.terms = {k: F(v) for k, v in (terms or {}).items() if v}

    @staticmethod
    def lift(value):
        return value if isinstance(value, Formal) else Formal({((), ()): value})

    def __add__(self, other):
        out = self.terms.copy()
        for key, value in self.lift(other).terms.items():
            out[key] = out.get(key, F(0)) + value
        return Formal(out)

    __radd__ = __add__

    def __neg__(self):
        return Formal({key: -value for key, value in self.terms.items()})

    def __sub__(self, other):
        return self + (-self.lift(other))

    def __rsub__(self, other):
        return self.lift(other) - self

    def __mul__(self, other):
        out = {}
        for (s, w), coefficient in self.terms.items():
            for (t, z), value in self.lift(other).terms.items():
                key = (tuple(sorted(s + t)), w + z)
                out[key] = out.get(key, F(0)) + coefficient * value
        return Formal(out)

    __rmul__ = __mul__

    def derivative(self, direction):
        out = {}
        for (scalars, words), value in self.terms.items():
            for position, jet in enumerate(scalars):
                name, n0, n1 = jet
                changed = (name, n0 + (direction == 0), n1 + (direction == 1))
                key = (tuple(sorted(scalars[:position] + (changed,) + scalars[position+1:])), words)
                out[key] = out.get(key, F(0)) + value
            for position, jet in enumerate(words):
                name, n0, n1 = jet
                changed = (name, n0 + (direction == 0), n1 + (direction == 1))
                key = (scalars, words[:position] + (changed,) + words[position+1:])
                out[key] = out.get(key, F(0)) + value
        return Formal(out)


def scalar(name):
    return Formal({(((name, 0, 0),), ()): 1})


def word(name):
    return Formal({((), ((name, 0, 0),)): 1})


def mu(left, right):
    return F(1, 2) * (left.derivative(0)*right.derivative(1)
                      - left.derivative(1)*right.derivative(0))


passes = rejects = 0


def zero(name, expression):
    global passes
    if Formal.lift(expression).terms:
        raise RuntimeError(name + ': nonzero invented-symbol remainder')
    passes += 1
    print('PASS:', name)


def nonzero(name, expression):
    global rejects
    if not Formal.lift(expression).terms:
        raise RuntimeError(name + ': mutation was not rejected')
    rejects += 1
    print('REJECT:', name)


def condition(name, value):
    global passes
    if not value:
        raise RuntimeError(name)
    passes += 1
    print('PASS:', name)


# Independent invented additive edge labels on three adjacent edges.
a0, a1, z0, z1, c0, c1 = [scalar(n) for n in ('a0','a1','z0','z1','c0','c1')]
delta_e = z0*z1 - (a0+z0)*(a1+z1) + a0*a1
cross = a0*z1 + a1*z0
zero('same-edge scalar coboundary has the negative symmetric sign', delta_e+cross)
nonzero('reversed scalar coboundary sign', delta_e-cross)

for label, (a,b,c,d,e,f) in (
    ('01', (a0,a1,z0,z1,c0,c1)),
    ('10', (a1,a0,z1,z0,c1,c0))):
    zero('ordered scalar cup cocycle '+label,
         a*d + (a+c)*f - c*f - a*(d+f))

t = scalar('t')
coefficient = F(15, 4)
A, B = coefficient-t, -t
zero('explicit repair preserves the parameter difference', A-B-coefficient)
zero('explicit repair equals original plus its coboundary',
     A*a0*z1+B*a1*z0 - coefficient*a0*z1 - t*delta_e)
nonzero('wrong sign on repaired first scalar',
        A*a0*z1+B*a1*z0 - coefficient*a0*z1 + t*delta_e)

# Arbitrary scalar changes in a genuinely ordered free-row product.
X,Y = word('X'),word('Y')
e01,e12,e02 = scalar('e01'),scalar('e12'),scalar('e02')
delta = e12-e02+e01
first_change = (e12*Y)*X + Y*(e01*X) - e02*(Y*X)
zero('first-lift scalar repair has correct row order and composite edge',
     first_change-delta*(Y*X))
nonzero('omitted composite-edge first-lift change',
        (e12*Y)*X + Y*(e01*X) - delta*(Y*X))
nonzero('reversed row product in scalar first-lift repair',
        first_change-delta*(X*Y))

# These verify the two ordered scalar-slot product rules used in the anomaly.
Z, P = word('Z'), scalar('P')
zero('left scalar-slot Leibniz error', mu(Z,P*(Y*X))-P*mu(Z,Y*X)-mu(Z,P)*(Y*X))
zero('right scalar-slot Leibniz error', mu(P*(Z*Y),X)-P*mu(Z*Y,X)-(Z*Y)*mu(P,X))
nonzero('reversed first scalar-slot error word order',
        mu(Z,P*(Y*X))-P*mu(Z,Y*X)-(Y*X)*mu(Z,P))


def bits(mask):
    return tuple((mask >> direction) & 1 for direction in range(4))


def difference(left, right):
    return tuple(y-x for x,y in zip(bits(left),bits(right)))


def cup_coefficients(masks, i,j,k):
    left, right = difference(masks[i],masks[j]), difference(masks[j],masks[k])
    # Coefficients of A and B; no scalar functions are instantiated.
    return left[0]*right[1], left[1]*right[0]


def anomaly_coefficients(masks):
    """Normalized coefficients of A,B after the proved support cancellation.

    Both formal bilinear scalars have b=kappa*R0*R1. The first endpoint
    contributes kappa012*(d23[0]-d23[1])/2, and the negative second
    endpoint contributes kappa123*(d01[0]-d01[1])/2. R2 is supported in
    direction 2, so its exponent never enters directions 0 or 1.
    """
    d23,d01 = difference(masks[2],masks[3]),difference(masks[0],masks[1])
    k012,k123 = cup_coefficients(masks,0,1,2),cup_coefficients(masks,1,2,3)
    return tuple(F(k012[n]*(d23[0]-d23[1])+k123[n]*(d01[0]-d01[1]),2) for n in range(2))


QA, QB = (0,1,3,5),(0,2,3,6)
for label,masks,expected_cups,expected_current in (
    ('A',QA,((1,0),(0,0)),(0,-1,1,0)),
    ('B',QB,((0,1),(0,0)),(-1,0,1,0))):
    condition(label+' witness has four distinct increasing legal masks', tuple(sorted(set(masks))) == masks)
    condition(label+' witness varies exactly bits 0,1,2',
              tuple(len({bits(mask)[d] for mask in masks}) for d in range(4)) == (2,2,2,1))
    condition(label+' witness isolates its cup and kills the second endpoint',
              (cup_coefficients(masks,0,1,2),cup_coefficients(masks,1,2,3)) == expected_cups)
    condition(label+' witness has the required supported logarithmic current',
              difference(masks[2],masks[3]) == expected_current)

alpha,beta = scalar('alpha'),scalar('beta')
def coefficient_expression(pair):
    return pair[0]*alpha+pair[1]*beta

new_A,new_B = anomaly_coefficients(QA),anomaly_coefficients(QB)
zero('first fresh anomaly is positive alpha over two', coefficient_expression(new_A)-F(1,2)*alpha)
zero('second fresh anomaly is negative beta over two', coefficient_expression(new_B)+F(1,2)*beta)
nonzero('reversed first fresh anomaly sign', coefficient_expression(new_A)+F(1,2)*alpha)
nonzero('reversed second fresh anomaly sign', coefficient_expression(new_B)-F(1,2)*beta)
nonzero('doubled repeated-pair coefficient', coefficient_expression(new_A)-alpha)

old=anomaly_coefficients((0,1,2,3))
zero('old increasing square sees only alpha plus beta',coefficient_expression(old)-F(1,2)*(alpha+beta))
condition('antisymmetric repair cancels the old square',old[0]*F(15,8)+old[1]*F(-15,8)==0)
condition('antisymmetric repair survives on both fresh witnesses',
          [pair[0]*F(15,8)+pair[1]*F(-15,8) for pair in (new_A,new_B)] == [F(15,16),F(15,16)])
condition('two fresh witnesses separately detect the two coefficients',
          new_A[0]*new_B[1]-new_A[1]*new_B[0] == F(-1,4))

print('All bounded producer controls passed:',passes,'checks;',rejects,'mutations rejected.')
