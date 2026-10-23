"""Complete 18 harmonic + 3 trace coefficient maps for the new D5 legs.

The output is a symmetric 5-by-5 positive-linear coefficient tensor in the
negative quartic monomial labelling of quartic_adapted_legs().  This is a
coefficient-space construction, NOT a claim about middle-operator
independence or solvability of either C equation.  No C5 filter is applied.
All external coefficients and marking units remain free.
"""
from dataclasses import dataclass
from functools import lru_cache

from universal_minimal_traceless_w_target_routes import (
    s, comb, S, T, x, y, z, mon, coeff, tv, op4, quartic,
    marked_twelve, typed_outputs, project_six, bridge_to_degree,
    CANONICAL_DEGREE, BINARY_TYPES,
)
from universal_physical_mixed_leg_foundation import f as PHYSICAL_F


def polynomial(vector, degree):
    return s.expand(sum(c*m for c, m in zip(vector, mon(degree))))


def quartic_marking(f):
    """F4: negative quartics -> positive quartics, with literal inverse.

    It is induced by conjugating op4 through the actual cubic marking,
    not by identifying the inequivalent positive and negative binary SL2s.
    """
    return s.Matrix.hstack(*[
        coeff(quartic(f*op4(p)*f.inv()), 4) for p in mon(4)
    ]).applyfunc(s.factor)


@lru_cache(None)
def cg_monomial(m, n, r, index):
    """Exact CG inclusion B_(m+n-2r) -> B_m tensor B_n.

    Same Delta^r and normalized polarization convention as the existing
    clebsch_monomial(), generalized from its fixed second degree six.
    Dictionary indices are the T exponents in the two binary factors.
    """
    assert 0 <= r <= min(m, n)
    a, b = m-r, n-r
    degree = a+b
    assert 0 <= index <= degree
    out = {}
    for t in range(max(0, a-(degree-index)), min(a, index)+1):
        c = s.Rational(comb(degree-index, a-t)*comb(index, t),
                       comb(degree, a))
        for zz in range(r+1):
            key = (t+zz, index-t+r-zz)
            out[key] = out.get(key, 0)+c*(-1)**zz*comb(r, zz)
    return {key: value for key, value in out.items() if value}


@dataclass(frozen=True)
class LegTargetRoute:
    pair_degree: int
    outer_order: int
    degree: int
    kind: str

    @property
    def label(self):
        return ('pairB'+str(self.pair_degree)+'_outer'+str(self.outer_order)
                +'_B'+str(self.degree)+'_'+self.kind)


def leg_target_routes(kind=None):
    """All twelve typed target summands, three per A,V,P4,D5.

    Sym²(B4)=B8+B4+B0, followed by B2 tensor each summand.
    Different pair_degree/outer_order values are direct CG summands.
    """
    for n in (8, 4, 0):
        for r in range(min(2, n)+1):
            degree = 2+n-2*r
            for output_kind in BINARY_TYPES[degree]:
                if kind is None or kind == output_kind:
                    yield LegTargetRoute(n, r, degree, output_kind)


def positive_linear(p):
    """B2 -> physical positive-linear coefficients, without q0 division.

    The entire conic is (x,y,z)=(T²,-S²,ST), where this evaluates to p.
    """
    c = coeff(p, 2)
    return -y*c[0]+z*c[1]+x*c[2]


def target_tensor(p, route):
    """Nested exact CG inclusion into B2 tensor Sym²(B4).

    Matrices represent the FULL sum_i,j K_ij H_i tensor H_j.  Thus an
    off-diagonal coefficient occurs in both symmetric positions; there
    is no hidden factor-of-two convention.
    """
    n, r, degree = route.pair_degree, route.outer_order, route.degree
    assert degree == 2+n-2*r
    K = s.zeros(5)
    first = (-y, z, x)
    inner_order = (8-n)//2
    for index, c in enumerate(coeff(p, degree)):
        if c == 0:
            continue
        for (i, j), outer in cg_monomial(2, n, r, index).items():
            for (a, b), inner in cg_monomial(4, 4, inner_order, j).items():
                K[a, b] += c*outer*inner*first[i]
    return K.applyfunc(s.expand)


class NewD5LegCoefficientBuilder:
    """Lazy complete coefficient-space basis, at the actual free marking."""
    def __init__(self, f=PHYSICAL_F):
        self.f = f
        self.F4 = quartic_marking(f)
        self.F4inv = self.F4.inv().applyfunc(s.factor)
        self.g12 = marked_twelve(f)
        self.templates = {}

    def harmonic_sources(self, a, hpoly):
        """Six typed maps from harmonic quadratic-a tensor linear-h.

        a is a negative binary quadratic; hpoly is a positive quartic.
        The scalar order-four source is omitted because the target has
        no scalar component. Repeated P4/D5 sources have distinct CG order.
        """
        qa = polynomial(self.F4*coeff(s.expand(a*a), 4), 4)
        out = []
        for order in range(4):
            degree = 8-2*order
            for kind, p in typed_outputs(self.f, self.g12,
                                         tv(qa, hpoly, order), degree):
                out.append(('a2h_tv'+str(order)+'_'+kind, kind, p))
        assert len(out) == 6
        return out

    def trace_source(self, a, hpoly):
        """For a=k S²-2d S T-l T², the trace factor is d²+kl."""
        return ('a_trace_h_D5', 'D5', s.expand(-tv(a, a, 2)*hpoly/8))

    def template(self, route):
        if route not in self.templates:
            degree = CANONICAL_DEGREE[route.kind]
            out = []
            for p in mon(degree):
                q = bridge_to_degree(self.f, self.g12, route.kind, p,
                                     route.degree)
                KP = target_tensor(q, route)
                # Convert BOTH positive quartic vector factors back to
                # the negative quartic labels of the actual source legs.
                out.append((self.F4inv*KP*self.F4inv.T).applyfunc(s.factor))
            self.templates[route] = out
        return self.templates[route]

    def apply(self, p, route, expand=True):
        cc = coeff(p, CANONICAL_DEGREE[route.kind])
        K = sum((c*Q for c, Q in zip(cc, self.template(route)) if c != 0),
                s.zeros(5))
        return K.applyfunc(s.expand) if expand else K

    def iter_coefficients(self, a, hpoly, expand=True):
        """Yield (harmonic_or_trace, label, symmetric5x5 coefficient)."""
        for category, sources in (
            ('harmonic', self.harmonic_sources(a, hpoly)),
            ('trace', [self.trace_source(a, hpoly)]),
        ):
            for name, kind, p in sources:
                for route in leg_target_routes(kind):
                    yield category, name+'__'+route.label, self.apply(p, route, expand)


def build_new_d5_leg_coefficients(a, hpoly, f=PHYSICAL_F, expand=True):
    """Return lists of 18 harmonic and 3 trace (label, K) coefficient maps."""
    builder = NewD5LegCoefficientBuilder(f)
    out = {'harmonic': [], 'trace': []}
    for category, label, K in builder.iter_coefficients(a, hpoly, expand):
        out[category].append((label, K))
    assert len(out['harmonic']) == 18 and len(out['trace']) == 3
    return out['harmonic'], out['trace']


def full_c_residual_interface(K):
    """Retain the ENTIRE C3/C5 errors; never impose standalone C5 zero.

    The imported frozen interface uses the same actual marking as PHYSICAL_F.
    Its Y/G outputs multiply -cm*kappa / cm*kappa², respectively, for the
    raw T=L K L*. The clean normalization (am/bm)T instead has factors
    -cm / cm*kappa. Use the unfiltered residuals in a JOINT source solve.
    """
    from universal_degree_one_c_orthogonal_module import completed_family_interface
    return completed_family_interface(K)
