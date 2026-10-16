"""Generic exact four-axis elliptic field. No model data or admission policy."""
from dataclasses import dataclass, field
from fractions import Fraction
from types import MappingProxyType

ZERO = (0, 0, 0, 0)

class LimitExceeded(RuntimeError):
    pass

class NotLaurentPolynomial(ValueError):
    pass

class UnsupportedInverse(ValueError):
    pass


def _integer(value):
    if type(value) is not int:
        raise TypeError("exact integer required")
    return value


def _exponent(value, signed=False):
    value = tuple(value)
    if len(value) != 4:
        raise ValueError("four exponents required")
    for n in value:
        _integer(n)
        if not signed and n < 0:
            raise ValueError("polynomial exponents must be nonnegative")
    return value


def _axis(i):
    if type(i) is not int or not 0 <= i < 4:
        raise ValueError("axis must be 0..3")
    return i


@dataclass(frozen=True, slots=True)
class Limits:
    products: int = 1_000_000
    storage_events: int = 1_000_000
    bit_height: int = 4096
    steps: int = 2_000_000

    def __post_init__(self):
        for n in (self.products, self.storage_events, self.bit_height, self.steps):
            if type(n) is not int or n < 0:
                raise ValueError("limits must be nonnegative integers")


class Execution:
    """One aggregate meter; share this object throughout a caller execution.

    Caps are algorithmic hooks, not estimates of memory or physical admission.
    Failed executions are permanently poisoned, including preexisting objects.
    """
    __slots__ = ('_limits', '_counts', '_failed')

    def __init__(self, limits=None):
        self._limits = limits if limits is not None else Limits()
        if not isinstance(self._limits, Limits):
            raise TypeError("Limits required")
        self._counts = dict(products=0, storage_events=0, bit_height=0,
                            steps=0, basis_products=0)
        self._failed = False

    @property
    def limits(self):
        return self._limits

    @property
    def counts(self):
        return MappingProxyType(dict(self._counts))

    def check(self):
        if self._failed:
            raise LimitExceeded("execution is closed after budget exhaustion")

    def tick(self, key='steps', n=1):
        self.check()
        self._counts[key] += n
        if key != 'basis_products' and self._counts[key] > getattr(self._limits, key):
            self._failed = True
            raise LimitExceeded(key)

    def observe(self, q):
        self.check()
        h = max(abs(q.numerator).bit_length(), q.denominator.bit_length())
        self._counts['bit_height'] = max(self._counts['bit_height'], h)
        if h > self._limits.bit_height:
            self._failed = True
            raise LimitExceeded('bit_height')
        return q

    def q(self, value):
        self.tick()
        if type(value) not in (int, Fraction):
            raise TypeError("only int and Fraction coefficients accepted")
        return self.observe(Fraction(value))

    def add(self, a, b):
        self.tick()
        return self.observe(a + b)

    def mul(self, a, b):
        self.tick()
        self.tick('products')
        return self.observe(a * b)

    def div(self, a, b):
        self.tick()
        self.tick('products')
        return self.observe(a / b)

    def poly(self, terms=()):
        return Poly(self, terms)

    def constant(self, q):
        return self.poly(((ZERO, q),))

    def xpoly(self, i):
        e = list(ZERO)
        e[_axis(i)] = 1
        return self.poly(((tuple(e), 1),))

    def rational(self, numerator, denominator=None):
        self.check()
        if any(isinstance(p, Poly) and p.ex is not self for p in (numerator, denominator)):
            raise ValueError("polynomial inputs must share receiving Execution")
        if not isinstance(numerator, Poly):
            numerator = self.constant(numerator)
        if denominator is None:
            denominator = self.constant(1)
        elif not isinstance(denominator, Poly):
            denominator = self.constant(denominator)
        return Rational(numerator, denominator)

    def element(self, terms=()):
        return Element(self, terms)

    def scalar(self, q):
        if not isinstance(q, Rational):
            q = self.rational(q)
        return self.element(((0, q),))

    def x(self, i):
        return self.scalar(self.rational(self.xpoly(i)))

    def y(self, i):
        return self.element(((1 << _axis(i), self.rational(1)),))

    def curve(self, i):
        x = self.xpoly(i)
        return x * x * x - x


def _same(a, b):
    a.ex.check()
    b.ex.check()
    if a.ex is not b.ex:
        raise ValueError("objects must share one Execution")


@dataclass(frozen=True, slots=True, init=False, eq=False)
class Poly:
    ex: Execution = field(repr=False)
    terms: tuple

    def __init__(self, ex, terms=()):
        ex.check()
        data = {}
        source = terms.items() if hasattr(terms, 'items') else terms
        for e, q in source:
            ex.tick()
            e, q = _exponent(e), ex.q(q)
            for power in e:
                ex.observe(Fraction(power))
            q = ex.add(data.get(e, Fraction(0)), q)
            ex.tick('storage_events')
            if q:
                data[e] = q
            else:
                data.pop(e, None)
        ex.tick('storage_events', len(data) + 1)
        object.__setattr__(self, 'ex', ex)
        object.__setattr__(self, 'terms', tuple(sorted(data.items())))

    def is_zero(self):
        self.ex.check()
        return not self.terms

    def __eq__(self, other):
        if not isinstance(other, Poly):
            return NotImplemented
        _same(self, other)
        return self.terms == other.terms

    def __add__(self, other):
        _same(self, other)
        return Poly(self.ex, (*self.terms, *other.terms))

    def __neg__(self):
        return self.scale(-1)

    def __sub__(self, other):
        return self + (-other)

    def scale(self, q):
        q = self.ex.q(q)
        return Poly(self.ex, ((e, self.ex.mul(c, q)) for e, c in self.terms))

    def __mul__(self, other):
        _same(self, other)
        def terms():
            for e, a in self.terms:
                for f, b in other.terms:
                    self.ex.tick()
                    yield tuple(u + v for u, v in zip(e, f)), self.ex.mul(a, b)
        return Poly(self.ex, terms())

    def partial(self, i):
        i = _axis(i)
        def terms():
            for e, q in self.terms:
                self.ex.tick()
                if e[i]:
                    f = list(e)
                    f[i] -= 1
                    yield tuple(f), self.ex.mul(q, self.ex.q(e[i]))
        return Poly(self.ex, terms())

    def divide(self, divisor):
        """Exact single-divisor lexicographic polynomial long division, Q[x]."""
        _same(self, divisor)
        if divisor.is_zero():
            raise ZeroDivisionError("zero polynomial divisor")
        work, quotient, remainder = self, self.ex.poly(), self.ex.poly()
        de, dc = divisor.terms[-1]
        while not work.is_zero():
            self.ex.tick()
            e, c = work.terms[-1]
            if all(a >= b for a, b in zip(e, de)):
                t = self.ex.poly(((tuple(a-b for a, b in zip(e, de)),
                                   self.ex.div(c, dc)),))
                quotient = quotient + t
                work = work - t * divisor
            else:
                t = self.ex.poly(((e, c),))
                remainder = remainder + t
                work = work - t
        return quotient, remainder


@dataclass(frozen=True, slots=True, init=False, eq=False)
class Rational:
    numerator: Poly
    denominator: Poly

    @property
    def ex(self):
        return self.numerator.ex

    def __init__(self, numerator, denominator):
        _same(numerator, denominator)
        if denominator.is_zero():
            raise ZeroDivisionError("zero rational denominator")
        ex = numerator.ex
        # Canonical zero; normalize constant denominators and denominator lead.
        if numerator.is_zero():
            denominator = ex.constant(1)
        elif len(denominator.terms) == 1 and denominator.terms[0][0] == ZERO:
            numerator = numerator.scale(ex.div(Fraction(1), denominator.terms[0][1]))
            denominator = ex.constant(1)
        elif denominator.terms[-1][1] != 1:
            s = ex.div(Fraction(1), denominator.terms[-1][1])
            numerator, denominator = numerator.scale(s), denominator.scale(s)
        ex.tick('storage_events')
        object.__setattr__(self, 'numerator', numerator)
        object.__setattr__(self, 'denominator', denominator)

    def is_zero(self):
        return self.numerator.is_zero()

    def __eq__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        _same(self, other)
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __add__(self, other):
        _same(self, other)
        if self.is_zero():
            return other
        if other.is_zero():
            return self
        if self.denominator == other.denominator:
            return Rational(self.numerator + other.numerator, self.denominator)
        return Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __neg__(self):
        return Rational(-self.numerator, self.denominator)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        _same(self, other)
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def inverse(self):
        return Rational(self.denominator, self.numerator)

    def __truediv__(self, other):
        _same(self, other)
        return self * other.inverse()

    def partial(self, i):
        i = _axis(i)
        return Rational(self.numerator.partial(i) * self.denominator -
                        self.numerator * self.denominator.partial(i),
                        self.denominator * self.denominator)

    def laurent_coefficient(self, exponent):
        """Return a coefficient only after proving this rational is Laurent.

        Extract x^d from denominator, divide numerator by the residual full
        polynomial, reject any remainder, then read coefficient at exponent+d.
        """
        self.ex.check()
        exponent = _exponent(exponent, signed=True)
        d = tuple(min(e[i] for e, _ in self.denominator.terms) for i in range(4))
        residual = self.ex.poly((tuple(e[i]-d[i] for i in range(4)), c)
                                for e, c in self.denominator.terms)
        quotient, remainder = self.numerator.divide(residual)
        if not remainder.is_zero():
            raise NotLaurentPolynomial("nonzero polynomial division remainder")
        target = tuple(exponent[i]+d[i] for i in range(4))
        # No support shortcut precedes divisibility certification.
        for e, c in quotient.terms:
            self.ex.tick()
            if e == target:
                return c
        return Fraction(0)


@dataclass(frozen=True, slots=True, init=False, eq=False)
class Element:
    ex: Execution = field(repr=False)
    terms: tuple

    def __init__(self, ex, terms=()):
        ex.check()
        data = {}
        source = terms.items() if hasattr(terms, 'items') else terms
        for mask, coefficient in source:
            ex.tick()
            if type(mask) is not int or not 0 <= mask < 16:
                raise ValueError("basis mask must be 0..15")
            if not isinstance(coefficient, Rational) or coefficient.ex is not ex:
                raise ValueError("rational coefficient must share Execution")
            coefficient = data[mask] + coefficient if mask in data else coefficient
            ex.tick('storage_events')
            if coefficient.is_zero():
                data.pop(mask, None)
            else:
                data[mask] = coefficient
        ex.tick('storage_events', len(data) + 1)
        object.__setattr__(self, 'ex', ex)
        object.__setattr__(self, 'terms', tuple(sorted(data.items())))

    def is_zero(self):
        self.ex.check()
        return not self.terms

    def __eq__(self, other):
        if not isinstance(other, Element):
            return NotImplemented
        _same(self, other)
        return (self - other).is_zero()

    def __add__(self, other):
        _same(self, other)
        return Element(self.ex, (*self.terms, *other.terms))

    def __neg__(self):
        return Element(self.ex, ((m, -c) for m, c in self.terms))

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        _same(self, other)
        def terms():
            for a, c in self.terms:
                for b, d in other.terms:
                    self.ex.tick()
                    self.ex.tick('basis_products')
                    q = c * d
                    for i in range(4):
                        if a & b & (1 << i):
                            q = q * self.ex.rational(self.ex.curve(i))
                    yield a ^ b, q
        return Element(self.ex, terms())

    def inverse(self):
        self.ex.check()
        if not self.terms:
            raise ZeroDivisionError("zero field element")
        if len(self.terms) != 1:
            raise UnsupportedInverse("general nonmonomial y inverse is not implemented")
        mask, c = self.terms[0]
        denominator = c
        for i in range(4):
            if mask & (1 << i):
                denominator = denominator * self.ex.rational(self.ex.curve(i))
        return Element(self.ex, ((mask, denominator.inverse()),))

    def __truediv__(self, other):
        _same(self, other)
        return self * other.inverse()

    def V(self, i):
        """Invariant derivation, including differentiation of the y moving frame."""
        i = _axis(i)
        self.ex.check()
        pieces = []
        for mask, c in self.terms:
            self.ex.tick()
            # y_i * partial_i(c) * y^mask, reduced by the same basis product.
            term = Element(self.ex, ((mask, c.partial(i)),)) * self.ex.y(i)
            pieces.extend(term.terms)
            if mask & (1 << i):
                x = self.ex.xpoly(i)
                dy = (x * x).scale(3) - self.ex.constant(1)
                dy = dy.scale(Fraction(1, 2))
                pieces.append((mask ^ (1 << i), c * self.ex.rational(dy)))
            self.ex.tick('storage_events', len(term.terms) + bool(mask & (1 << i)))
        return Element(self.ex, pieces)

    def jet(self, axes):
        """Apply V in the supplied order; counts are shared with all other work."""
        self.ex.check()
        result = self
        for i in axes:
            self.ex.tick()
            result = result.V(i)
        return result

    def rational_x(self):
        self.ex.check()
        if not self.terms:
            return self.ex.rational(0)
        if len(self.terms) != 1 or self.terms[0][0] != 0:
            raise ValueError("element has nonzero y-basis components")
        return self.terms[0][1]

    def laurent_coefficient(self, exponent):
        return self.rational_x().laurent_coefficient(exponent)
