"""Exact abstract Q4 quotient compression. No HM coefficients or dependencies.

Matrices act on column vectors. Empty matrices retain both dimensions.
Only integers, Fraction values and rational strings are accepted (not floats).
"""
from dataclasses import dataclass
from fractions import Fraction


def rational(x):
    if isinstance(x, bool) or not isinstance(x, (int, Fraction, str)):
        raise TypeError('Entries must be integers, Fractions, or rational strings')
    return Fraction(x)


@dataclass(frozen=True)
class Matrix:
    rows: int
    cols: int
    data: tuple

    def __post_init__(self):
        if self.rows < 0 or self.cols < 0 or len(self.data) != self.rows:
            raise ValueError('Invalid matrix shape')
        if any(len(row) != self.cols for row in self.data):
            raise ValueError('Ragged matrix')
        object.__setattr__(self, 'data', tuple(tuple(rational(x) for x in row)
                                             for row in self.data))

    @classmethod
    def of(cls, rows, ncols=None):
        rows = tuple(tuple(row) for row in rows)
        return cls(len(rows), len(rows[0]) if rows else (ncols or 0), rows)

    @classmethod
    def zero(cls, m, n):
        return cls(m, n, tuple((0,) * n for _ in range(m)))

    @classmethod
    def identity(cls, n):
        return cls(n, n, tuple(tuple(int(i == j) for j in range(n))
                              for i in range(n)))

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError('Incompatible matrix multiplication')
        return Matrix(self.rows, other.cols, tuple(
            tuple(sum((self.data[i][k] * other.data[k][j]
                       for k in range(self.cols)), Fraction(0))
                  for j in range(other.cols)) for i in range(self.rows)))

    def columns(self, indices):
        indices = tuple(indices)
        return Matrix(self.rows, len(indices), tuple(
            tuple(row[j] for j in indices) for row in self.data))

    def row_slice(self, start, stop):
        return Matrix(stop-start, self.cols, self.data[start:stop])


def hstack(*matrices):
    if not matrices or any(m.rows != matrices[0].rows for m in matrices):
        raise ValueError('hstack needs equally many rows')
    return Matrix(matrices[0].rows, sum(m.cols for m in matrices), tuple(
        tuple(x for m in matrices for x in m.data[i])
        for i in range(matrices[0].rows)))


def rref(a):
    data = [list(row) for row in a.data]
    pivots = []
    r = 0
    for j in range(a.cols):
        k = next((i for i in range(r, a.rows) if data[i][j]), None)
        if k is None:
            continue
        data[r], data[k] = data[k], data[r]
        scalar = data[r][j]
        data[r] = [x / scalar for x in data[r]]
        for i in range(a.rows):
            if i != r:
                scalar = data[i][j]
                data[i] = [x - scalar*y for x, y in zip(data[i], data[r])]
        pivots.append(j)
        r += 1
        if r == a.rows:
            break
    return Matrix(a.rows, a.cols, tuple(tuple(row) for row in data)), tuple(pivots)


def rank(a):
    return len(rref(a)[1])


def inverse(a):
    if a.rows != a.cols:
        raise ValueError('Inverse requires a square matrix')
    red, pivots = rref(hstack(a, Matrix.identity(a.rows)))
    if pivots[:a.rows] != tuple(range(a.rows)):
        raise ValueError('Singular matrix')
    return red.columns(range(a.cols, 2*a.cols))


@dataclass(frozen=True)
class Quotient:
    """Explicit X/im(generators): projection, section, relation certificates."""
    generators: Matrix
    basis_indices: tuple
    relation_basis: Matrix
    coordinates: Matrix
    projection: Matrix
    section: Matrix
    relation_coordinates: Matrix

    def verify(self):
        g, b, q, s = self.generators, self.relation_basis, self.projection, self.section
        # Identity is checked on the two coordinate blocks, avoiding addition.
        frame = hstack(b, s)
        coord = Matrix(g.rows, g.rows, self.relation_coordinates.data + q.data)
        return (b == g.columns(self.basis_indices)
                and b @ self.coordinates == g and rank(b) == b.cols
                and q @ g == Matrix.zero(q.rows, g.cols)
                and q @ s == Matrix.identity(q.rows)
                and frame @ coord == Matrix.identity(g.rows)
                and coord @ frame == Matrix.identity(g.rows))


def quotient(generators):
    """Return a deterministic basis of the quotient of the column-vector ambient."""
    indices = rref(generators)[1]
    b = generators.columns(indices)
    extended = hstack(b, Matrix.identity(generators.rows))
    chosen = rref(extended)[1]
    frame = extended.columns(chosen)
    inv = inverse(frame)
    relation = inv.row_slice(0, b.cols)
    q = inv.row_slice(b.cols, generators.rows)
    s = frame.columns(range(b.cols, generators.rows))
    result = Quotient(generators, indices, b, relation @ generators, q, s, relation)
    if not result.verify():
        raise ArithmeticError('Quotient certificate failed')
    return result


@dataclass(frozen=True)
class Compression:
    u: Matrix
    v: Matrix
    inclusion: Matrix
    residual_source: Quotient
    target: Quotient
    induced: Matrix
    compressed_cokernel: Quotient
    full_cokernel: Quotient
    forward: Matrix
    backward: Matrix

    @property
    def row_transform(self):
        d = self.target
        return Matrix(self.u.rows, self.u.rows,
                      d.relation_coordinates.data + d.projection.data)

    @property
    def full_augmented(self):
        return hstack(self.target.generators, self.u @ self.residual_source.section)

    @property
    def reduced_full_block(self):
        d = self.target
        top = hstack(d.coordinates, d.relation_coordinates
                     @ self.u @ self.residual_source.section)
        bottom = hstack(Matrix.zero(self.induced.rows, d.generators.cols), self.induced)
        return Matrix(self.u.rows, top.cols, top.data + bottom.data)

    @property
    def pivot_augmented(self):
        # Independent columns chosen from [v,uL], followed by uJ.
        return hstack(self.target.relation_basis,
                      self.u @ self.residual_source.section)

    @property
    def reduced_pivot_block(self):
        b = self.target.relation_basis.cols
        top = hstack(Matrix.identity(b), self.target.relation_coordinates
                     @ self.u @ self.residual_source.section)
        bottom = hstack(Matrix.zero(self.induced.rows, b), self.induced)
        return Matrix(self.u.rows, top.cols, top.data + bottom.data)

    @property
    def pivot_column_transform(self):
        b = self.target.relation_basis.cols
        h = self.target.relation_coordinates @ self.u @ self.residual_source.section
        negative = Matrix(h.rows, h.cols, tuple(tuple(-x for x in row) for row in h.data))
        top = hstack(Matrix.identity(b), negative)
        bottom = hstack(Matrix.zero(h.cols, b), Matrix.identity(h.cols))
        return Matrix(b+h.cols, b+h.cols, top.data + bottom.data)

    @property
    def diagonal_pivot_block(self):
        b = self.target.relation_basis.cols
        top = hstack(Matrix.identity(b), Matrix.zero(b, self.induced.cols))
        bottom = hstack(Matrix.zero(self.induced.rows, b), self.induced)
        return Matrix(self.u.rows, top.cols, top.data + bottom.data)

    @property
    def dimensions(self):
        return dict(residual_source=self.residual_source.projection.rows,
                    intermediate_target=self.target.projection.rows,
                    induced_rank=rank(self.induced),
                    paired_cokernel=self.full_cokernel.projection.rows,
                    cubic_kernel=self.v.cols-rank(self.v),
                    primary_increment=rank(self.target.generators)-rank(self.v))

    def verify(self):
        n, d = self.residual_source, self.target
        c, f = self.compressed_cokernel, self.full_cokernel
        return (all(x.verify() for x in (n, d, c, f))
                and self.row_transform @ self.full_augmented == self.reduced_full_block
                and self.row_transform @ self.pivot_augmented == self.reduced_pivot_block
                and self.row_transform @ self.pivot_augmented @ self.pivot_column_transform
                    == self.diagonal_pivot_block
                and n.generators == self.inclusion
                and d.generators == hstack(self.v, self.u @ self.inclusion)
                and f.generators == hstack(self.u, self.v)
                and c.generators == self.induced
                and d.projection @ self.u == self.induced @ n.projection
                and self.forward @ f.projection == c.projection @ d.projection
                and self.backward @ c.projection @ d.projection == f.projection
                and self.forward @ self.backward == Matrix.identity(c.projection.rows)
                and self.backward @ self.forward == Matrix.identity(f.projection.rows))


def compress(u, v, inclusion):
    """Compress K3--u-->K5<--v--K2 using injective L3-->K3.

    No rank or split-extension hypothesis. Chosen vector-space complements
    provide coordinates only; all entries of u and v remain in the calculation.
    """
    if u.rows != v.rows or inclusion.rows != u.cols:
        raise ValueError('Expected u:K3->K5, v:K2->K5, inclusion:L3->K3')
    if rank(inclusion) != inclusion.cols:
        raise ValueError('L3 inclusion must be injective')
    n = quotient(inclusion)
    d = quotient(hstack(v, u @ inclusion))
    induced = d.projection @ u @ n.section
    c = quotient(induced)
    f = quotient(hstack(u, v))
    forward = c.projection @ d.projection @ f.section
    backward = f.projection @ d.section @ c.section
    result = Compression(u, v, inclusion, n, d, induced, c, f, forward, backward)
    if not result.verify():
        raise ArithmeticError('Compression certificate failed')
    return result
