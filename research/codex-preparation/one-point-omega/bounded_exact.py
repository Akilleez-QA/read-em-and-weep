"""Checked rational arithmetic and two independent mixed-derivative engines.

No model loading, physical entry point, subprocess or network exists here.
Derivative arrays describe a point germ, not a source-polynomial coefficient
store. Only distinct-coordinate derivatives are represented by Jet11.
"""

class Refusal(RuntimeError):
    pass


class Meter:
    def __init__(self, rational_ops=2_000_000, integer_ops=20_000_000, bits=4096):
        self.caps = dict(rational_ops=rational_ops, integer_ops=integer_ops, bits=bits)
        if any(type(n) is not int or n < 1 for n in self.caps.values()):
            raise ValueError('positive integer limits required')
        self.counts = dict(rational_ops=0, integer_ops=0, max_integer_bits=0)
        self.poisoned = False

    def fail(self, message):
        self.poisoned = True
        raise Refusal(message)

    def check(self):
        if self.poisoned:
            raise Refusal('arithmetic context already refused')

    def charge(self, key):
        self.check()
        if self.counts[key] >= self.caps[key]:
            self.fail(key + ' limit')
        self.counts[key] += 1

    def observe(self, n):
        self.check()
        if type(n) is not int:
            self.fail('exact integer required')
        b = n.bit_length()
        if b > self.caps['bits']:
            self.fail('integer height limit')
        self.counts['max_integer_bits'] = max(self.counts['max_integer_bits'], b)
        return n

    def integer(self, kind, a, b=None):
        self.observe(a)
        if b is not None:
            self.observe(b)
        self.charge('integer_ops')
        if kind == 'mul':
            upper = a.bit_length() + b.bit_length()
        elif kind == 'add':
            upper = max(a.bit_length(), b.bit_length()) + 1
        else:
            upper = a.bit_length()
        # Conservative refusal happens BEFORE allocating an oversized result.
        if upper > self.caps['bits']:
            self.fail('predicted intermediate integer height limit')
        if kind == 'mul':
            return self.observe(a * b)
        if kind == 'add':
            return self.observe(a + b)
        if kind == 'neg':
            return self.observe(-a)
        if kind == 'divmod':
            if b == 0:
                self.fail('integer division by zero')
            q, r = divmod(a, b)
            return self.observe(q), self.observe(r)
        self.fail('unknown integer operation')

    def gcd(self, a, b):
        if a < 0:
            a = self.integer('neg', a)
        while b:
            _, r = self.integer('divmod', a, b)
            a, b = b, r
        return a


class Rat:
    def __init__(self, meter, numerator, denominator=1):
        self.m = meter
        meter.charge('rational_ops')
        n, d = meter.observe(numerator), meter.observe(denominator)
        if d == 0:
            meter.fail('rational denominator zero')
        if d < 0:
            n, d = meter.integer('neg', n), meter.integer('neg', d)
        g = meter.gcd(n, d)
        self.n, r = meter.integer('divmod', n, g)
        self.d, s = meter.integer('divmod', d, g)
        if r or s:
            meter.fail('inexact rational normalization')

    def coerce(self, value):
        self.m.check()
        if isinstance(value, Rat):
            if value.m is not self.m:
                self.m.fail('foreign arithmetic context')
            return value
        return Rat(self.m, value)

    def __add__(self, other):
        b = self.coerce(other)
        p = self.m.integer('mul', self.n, b.d)
        q = self.m.integer('mul', b.n, self.d)
        return Rat(self.m, self.m.integer('add', p, q),
                   self.m.integer('mul', self.d, b.d))

    __radd__ = __add__

    def __neg__(self):
        self.m.check()
        return Rat(self.m, self.m.integer('neg', self.n), self.d)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        b = self.coerce(other)
        return Rat(self.m, self.m.integer('mul', self.n, b.n),
                   self.m.integer('mul', self.d, b.d))

    __rmul__ = __mul__

    def inv(self):
        self.m.check()
        return Rat(self.m, self.d, self.n)

    def __truediv__(self, other):
        return self * self.coerce(other).inv()

    def __eq__(self, other):
        return (isinstance(other, Rat) and self.m is other.m
                and self.n == other.n and self.d == other.d)

    def is_zero(self):
        self.m.check()
        return self.n == 0

    def text(self):
        self.m.check()
        return str(self.n) if self.d == 1 else str(self.n) + '/' + str(self.d)


def power(a, n):
    if type(n) is not int or not 0 <= n <= 64:
        a.m.fail('bounded nonnegative power required')
    out = scalar(a, 1)
    while n:
        if n & 1:
            out = out * a
        n //= 2
        if n:
            a = a * a
    return out


MASKS = (0, 1, 2, 4, 8, 3, 5, 6, 9, 10, 12)
INDEX = {mask: i for i, mask in enumerate(MASKS)}


class Jet11:
    """Value, four first derivatives and six DISTINCT mixed derivatives.

    Exact algebra Q[epsilon]/(epsilon_i^2, degree>=3). Coefficients of distinct
    monomials ARE derivatives, with no missing factorial. No diagonal second
    derivative or higher derivative is requested or claimed.
    """
    def __init__(self, meter, values):
        meter.check()
        if len(values) != 11 or any(not isinstance(v, Rat) or v.m is not meter for v in values):
            meter.fail('Jet11 context/shape')
        self.m, self.v = meter, tuple(values)

    @classmethod
    def constant(cls, meter, value):
        r = value if isinstance(value, Rat) else Rat(meter, value)
        return cls(meter, [r] + [Rat(meter, 0) for _ in range(10)])

    @classmethod
    def coordinate(cls, meter, value, axis):
        out = list(cls.constant(meter, value).v)
        out[INDEX[1 << axis]] = Rat(meter, 1)
        return cls(meter, out)

    def coerce(self, value):
        if isinstance(value, Jet11):
            if value.m is not self.m:
                self.m.fail('foreign jet context')
            return value
        return Jet11.constant(self.m, value)

    def __add__(self, other):
        b = self.coerce(other)
        return Jet11(self.m, [a + b for a, b in zip(self.v, b.v)])

    __radd__ = __add__

    def __neg__(self):
        return Jet11(self.m, [-v for v in self.v])

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __mul__(self, other):
        b = self.coerce(other)
        out = [Rat(self.m, 0) for _ in MASKS]
        for i, a in enumerate(MASKS):
            for j, c in enumerate(MASKS):
                if not a & c and (a | c) in INDEX:
                    k = INDEX[a | c]
                    out[k] = out[k] + self.v[i] * b.v[j]
        return Jet11(self.m, out)

    __rmul__ = __mul__

    def inv(self):
        r = self.v[0].inv()
        u = self * Jet11.constant(self.m, r) - 1
        return (Jet11.constant(self.m, 1) - u + u * u) * Jet11.constant(self.m, r)

    def __truediv__(self, other):
        return self * self.coerce(other).inv()

    def coefficient(self, *axes):
        mask = sum(1 << i for i in axes)
        if len(set(axes)) != len(axes) or mask not in INDEX:
            self.m.fail('only distinct derivatives of order<=2')
        return self.v[INDEX[mask]]

    def __eq__(self, other):
        return isinstance(other, Jet11) and self.m is other.m and self.v == other.v


class Mixed4:
    """Independent explicit (value, d_u, d_v, d_u d_v) product/quotient rules."""
    def __init__(self, meter, values):
        meter.check()
        if len(values) != 4 or any(not isinstance(v, Rat) or v.m is not meter for v in values):
            meter.fail('Mixed4 context/shape')
        self.m, self.v = meter, tuple(values)

    @classmethod
    def constant(cls, meter, value):
        r = value if isinstance(value, Rat) else Rat(meter, value)
        return cls(meter, [r] + [Rat(meter, 0) for _ in range(3)])

    @classmethod
    def coordinate(cls, meter, value, axis, pair):
        v = list(cls.constant(meter, value).v)
        if axis in pair:
            v[1 + pair.index(axis)] = Rat(meter, 1)
        return cls(meter, v)

    def coerce(self, value):
        if isinstance(value, Mixed4):
            if value.m is not self.m:
                self.m.fail('foreign mixed context')
            return value
        return Mixed4.constant(self.m, value)

    def __add__(self, other):
        b = self.coerce(other)
        return Mixed4(self.m, [a + b for a, b in zip(self.v, b.v)])

    __radd__ = __add__

    def __neg__(self):
        return Mixed4(self.m, [-v for v in self.v])

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __mul__(self, other):
        a, b, c, d = self.v
        e, f, g, h = self.coerce(other).v
        return Mixed4(self.m, (a*e, b*e+a*f, c*e+a*g, d*e+b*g+c*f+a*h))

    __rmul__ = __mul__

    def inv(self):
        a, b, c, d = self.v
        r = a.inv()
        return Mixed4(self.m, (r, -b*r*r, -c*r*r, 2*b*c*r*r*r-d*r*r))

    def __truediv__(self, other):
        return self * self.coerce(other).inv()

    def unit_sqrt(self):
        # Independently derived derivatives of f^2=s at f(point)=1.
        a, b, c, d = self.v
        if a != Rat(self.m, 1):
            self.m.fail('unit square-root germ required')
        half, quarter = Rat(self.m, 1, 2), Rat(self.m, 1, 4)
        return Mixed4(self.m, (a, b*half, c*half, d*half-b*c*quarter))

    def __eq__(self, other):
        return isinstance(other, Mixed4) and self.m is other.m and self.v == other.v


def scalar(sample, n):
    return Rat(sample.m, n) if isinstance(sample, Rat) else type(sample).constant(sample.m, n)


def madd(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError('matrix addition shape')
    return [[x + y for x, y in zip(r, s)] for r, s in zip(a, b)]


def mscale(a, q):
    return [[v * q for v in row] for row in a]


def msub(a, b):
    return madd(a, mscale(b, scalar(b[0][0], -1)))


def mmul(a, b):
    if len(a[0]) != len(b):
        raise ValueError('ordered matrix multiplication shape')
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), scalar(a[0][0], 0))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(r) for r in zip(*a)]


def det2(a):
    if len(a) != 2 or any(len(r) != 2 for r in a):
        raise ValueError('2x2 matrix required')
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def inverse2(a):
    r = det2(a).inv()
    return mscale([[a[1][1], -a[0][1]], [-a[1][0], a[0][0]]], r)


def commutator(a, b):
    return msub(mmul(a, b), mmul(b, a))


def entries(a, component=None):
    return [[v if component is None else v.v[component] for v in row] for row in a]


def equal_matrix(a, b):
    return len(a) == len(b) and all(len(r) == len(s) and all(x == y for x, y in zip(r, s)) for r, s in zip(a, b))
