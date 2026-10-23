"""Explicit spanning generators for the 162 Rq + 33 Rh traceless-W channels.

Only universal coefficient maps are built: no source solve, instance rank, or
independence assertion.  Matrices use W-major order, so the four 6x6 blocks
are indexed by (W output, W input), and each block uses Cartan4 + Spin2.
The deliberately redundant lists have 607 Rq and 71 Rh entries.
"""
from dataclasses import dataclass
from functools import lru_cache
from universal_complete_identity_w_coefficients import *

# Positive binary realizations; every B_j below is G-multiplicity-free.
CANONICAL_DEGREE = {'1': 0, 'V': 2, 'D5': 4, 'A': 6, 'P4': 6}
BINARY_TYPES = {0: ('1',), 2: ('V',), 4: ('D5',), 6: ('A', 'P4'),
                8: ('P4', 'D5'), 10: ('A', 'V', 'D5'),
                12: ('1', 'V', 'P4', 'D5')}
# These tensor-type exclusions are representation identities, not instance tests.
TARGET_TYPES = {'C_scalar': ('A',), 'S_scalar': ('A',),
                'C_V': ('P4', 'D5'), 'S_V': ('P4', 'D5'),
                'CS_V': ('P4', 'D5'), 'SC_V': ('P4', 'D5'),
                'C_D5': ('A', 'V', 'P4', 'D5'),
                'CS_D5': ('A', 'V', 'P4', 'D5'),
                'SC_D5': ('A', 'V', 'P4', 'D5'),
                'C_A': ('1', 'A', 'D5'), 'C_P4': ('V', 'P4', 'D5')}
FIRST_BLOCKS = {0: ('C_scalar', 'S_scalar'),
                2: ('C_V', 'S_V', 'CS_V', 'SC_V'),
                4: ('C_D5', 'CS_D5', 'SC_D5'), 6: ('C_A', 'C_P4')}


def project_six(f, p, kind):
    """G-project a positive sextic to A or P4, not a chosen coefficient."""
    if kind not in ('A', 'P4'):
        raise ValueError(kind)
    return dict(split_six(f, p))[kind]


def bridge_to_degree(f, g12, kind, p, target_degree):
    """The unique canonical common-G-component bridge into B_target_degree.

    Same-degree B6 uses its specified type projector.  Higher-degree bridges
    are fixed transvectants with the marked invariant, never sampled maps.
    """
    degree = CANONICAL_DEGREE[kind]
    if kind not in BINARY_TYPES.get(target_degree, ()):
        raise ValueError((kind, target_degree))
    if degree == target_degree:
        return project_six(f, p, kind) if degree == 6 else p
    if kind == '1' and target_degree == 12:
        return s.expand(g12*p)
    order = (12 + degree - target_degree)//2
    assert 12 + degree - target_degree == 2*order
    assert 0 <= order <= min(12, degree)
    return tv(g12, p, order)


@lru_cache(None)
def clebsch_monomial(k, r, index):
    """Sparse exact CG inclusion of S^(j-index) T^index in B_k tensor B6.

    Return {(first T degree, second T degree): rational coefficient}.
    j=k+6-2r.  This is Delta^r times the normalized (k-r,6-r)
    polarization, with Delta=X*Q-Y*Z.  Both binary variables are retained.
    """
    assert k in (0, 2, 4, 6) and 0 <= r <= min(k, 6)
    a, b = k-r, 6-r
    j = a+b
    assert 0 <= index <= j
    out = {}
    for t in range(max(0, a-(j-index)), min(a, index)+1):
        # Before multiplying by Delta^r the first T degree is t.
        c = s.Rational(comb(j-index, a-t)*comb(index, t), comb(j, a))
        for z in range(r+1):
            key = (t+z, index-t+r-z)
            out[key] = out.get(key, 0) + c*(-1)**z*comb(r, z)
    return {key: value for key, value in out.items() if value}


def clebsch_inclusion(p, k, r, variables=None):
    """Full two-variable CG tensor polynomial; useful for symbolic audits."""
    X, Y, Z, Q = variables or s.symbols('cg_X cg_Y cg_Z cg_Q')
    j = k+6-2*r
    cc = coeff(p, j)
    return s.expand(sum(cc[index]*value*X**(k-i)*Y**i*Z**(6-t)*Q**t
                        for index in range(j+1)
                        for (i, t), value in clebsch_monomial(k, r, index).items()))


def negative_w_matrix(f, p):
    """B6 -> A -> sl(W), in the original negative W monomial frame.

    The negative Casimir projection is applied before f^-1.  In particular
    this does not identify the inequivalent positive V with negative A.
    """
    R = op6(p)
    RA = (12*R-negative_casimir(f, R))/10
    return spin_from_rank_one(f.inv()*RA*f).applyfunc(s.factor)


def first_coefficient_basis(f, k, block):
    """Images of the monomial basis of B_k in one chosen End(C+U) block."""
    assert block in FIRST_BLOCKS[k]
    kind = {0: '1', 2: 'V', 4: 'D5'}.get(k)
    out = []
    for p in mon(k):
        if k == 6:
            kind = block[2:]
            p = project_six(f, p, kind)
        out.append(dict(coefficient_embeddings(kind, p))[block])
    return out


@dataclass(frozen=True)
class TargetRoute:
    kind: str
    first_degree: int
    order: int
    clebsch_degree: int
    block: str

    @property
    def label(self):
        return self.block+'_B'+str(self.clebsch_degree)+'_cg'+str(self.order)


def target_routes(kind):
    """All output routes, including any routes killed by a final projector."""
    for k in (0, 2, 4, 6):
        for r in range(min(k, 6)+1):
            j = k+6-2*r
            if kind in BINARY_TYPES[j]:
                for block in FIRST_BLOCKS[k]:
                    if kind in TARGET_TYPES[block]:
                        yield TargetRoute(kind, k, r, j, block)


def typed_source_polynomials(f, H0):
    """Canonical typed source maps, exactly as for the identity-W generator."""
    g12 = marked_twelve(f)
    qh = quartic(H0)
    rq, rh = [], []
    for name, kind, p, degree in negative_inputs(f):
        rh.append((name, kind, p))
        for order in range(min(4, degree)+1):
            product = tv(qh, p, order)
            outdegree = 4+degree-2*order
            for outkind, q in typed_outputs(f, g12, product, outdegree):
                rq.append((name+'_tv'+str(order)+'_'+outkind, outkind, q))
    assert len(rq) == 38 and len(rh) == 5
    return rq, rh


class TracelessWBuilder:
    """Reusable coefficient builder; output map matrices are cached lazily.

    The template for a route is linear on its canonical B_d.  Supplying a
    typed source polynomial then only substitutes its complete coefficients.
    No numerical marking or source coefficient is selected.
    """
    def __init__(self, f):
        self.f = f
        self.g12 = marked_twelve(f)
        self.w_basis = [negative_w_matrix(f, p) for p in mon(6)]
        self.first_basis = {}
        self.route_templates = {}

    def tensor_image(self, p, route):
        k, r, j = route.first_degree, route.order, route.clebsch_degree
        key = (k, route.block)
        if key not in self.first_basis:
            self.first_basis[key] = first_coefficient_basis(self.f, k, route.block)
        first = self.first_basis[key]
        terms = {}
        for index, c in enumerate(coeff(p, j)):
            if c == 0:
                continue
            for (i, t), value in clebsch_monomial(k, r, index).items():
                tensor = s.kronecker_product(self.w_basis[t], first[i])
                for row in range(12):
                    for col in range(12):
                        if tensor[row, col] != 0:
                            key0 = (row, col)
                            terms[key0] = terms.get(key0, 0)+c*value*tensor[row, col]
        return s.Matrix(12, 12, lambda i, j: s.factor(terms.get((i, j), 0)))

    def template(self, route):
        if route not in self.route_templates:
            degree = CANONICAL_DEGREE[route.kind]
            templates = []
            for p in mon(degree):
                q = bridge_to_degree(self.f, self.g12, route.kind, p,
                                     route.clebsch_degree)
                templates.append(self.tensor_image(q, route))
            self.route_templates[route] = templates
        return self.route_templates[route]

    def apply(self, p, route, expand=True):
        templates = self.template(route)
        cc = coeff(p, CANONICAL_DEGREE[route.kind])
        M = sum((c*T0 for c, T0 in zip(cc, templates) if c != 0), s.zeros(12))
        return M.applyfunc(s.expand) if expand else M

    def iter_coefficients(self, f, H0, expand=True):
        """Yield (Rq_or_Rh, label, 12x12 coefficient), without forcing a list."""
        assert f == self.f
        rq, rh = typed_source_polynomials(f, H0)
        for category, source in [('Rq', rq), ('Rh', rh)]:
            for name, kind, p in source:
                for route in target_routes(kind):
                    yield category, name+'_'+route.label, self.apply(p, route, expand)


def build_complete_traceless_w_coefficients(f, H0, expand=True):
    """Return 607 Rq and 71 Rh generators spanning dimensions162 and33.

    Their 12x12 coefficient matrices are W-major.  They are not asserted
    independent and are not unrestricted middle cochains or source solutions.
    """
    builder = TracelessWBuilder(f)
    rq, rh = [], []
    for category, label, M in builder.iter_coefficients(f, H0, expand):
        (rq if category == 'Rq' else rh).append((label, M))
    assert len(rq) == 607 and len(rh) == 71
    return rq, rh
