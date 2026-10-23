"""Exact 44 harmonic + 8 trace maps for the ABSTRACT q-orthogonal quotient.

Only coefficient tensors are constructed. No actual source is selected, no
operator independence or source solvability is asserted, and no q quotient
is silently discarded. The unchanged DD block is imported from the frozen
18+3 constructor. See COMPLETE-44-HARMONIC-Q-ORTHOGONAL-LEG-COEFFICIENTS.md.
"""
from dataclasses import dataclass
from universal_new_d5_leg_coefficients import (
    s, S, T, x, y, z, mon, coeff, tv, polynomial, cg_monomial,
    positive_linear, NewD5LegCoefficientBuilder, PHYSICAL_F,
    CANONICAL_DEGREE, project_six, bridge_to_degree,
)
from universal_q_leg_equivariant_labeling import quotient_section_matrix, to_raw_coefficient
from universal_complete_identity_w_coefficients import (
    op2, op4, op6, quadratic, quartic, sextic, casimir, typed_outputs,
)


def apolar_metric(degree):
    """Normalized apolar bilinear form tv(p,q,degree)/(degree!)²."""
    return s.Matrix(degree+1, degree+1,
                    lambda i,j: (-1)**i/s.binomial(degree,i)
                    if i+j == degree else 0)


J2 = apolar_metric(2)
# The quotient Y_i C(zeta)/q0=zeta_i labels A* in S²,ST,T² order.
# A primal negative B2 vector c therefore has dual-leg coefficients J2*c.


@dataclass(frozen=True)
class QLegTargetRoute:
    sector: str
    pair_kind: str
    outer_order: int
    degree: int
    kind: str

    @property
    def pair_degree(self):
        return CANONICAL_DEGREE[self.pair_kind]

    @property
    def label(self):
        return (self.sector+'_pair'+self.pair_kind+'_outer'
                +str(self.outer_order)+'_B'+str(self.degree)+'_'+self.kind)


# One nonzero inclusion for each simple type in V tensor pair_kind.
# The exact adjoint left inverses and sum-to-identity certificates are
# checked by verify_q_orthogonal_leg_coefficients.py, without any rank test.
PAIR_OUTER_CHOICES = {
    '1': ((0, 2, 'V'),),
    'V': ((0, 4, 'D5'), (1, 2, 'V'), (2, 0, '1')),
    'D5': ((0, 6, 'A'), (0, 6, 'P4'), (1, 4, 'D5'), (2, 2, 'V')),
    'A': ((0, 8, 'P4'), (0, 8, 'D5')),
    'P4': ((0, 8, 'P4'), (0, 8, 'D5'), (1, 6, 'A')),
}


def q_leg_target_routes(sector=None, kind=None):
    """The five AA and twelve AD simple target inclusions; DD is frozen."""
    for sec, pairs in (('AA', ('1','D5')), ('AD', ('A','V','P4','D5'))):
        if sector is not None and sec != sector:
            continue
        for pair in pairs:
            for r, degree, outkind in PAIR_OUTER_CHOICES[pair]:
                if kind is None or outkind == kind:
                    yield QLegTargetRoute(sec, pair, r, degree, outkind)


def typed_projection(f, kind, p):
    return project_six(f,p,kind) if kind in ('A','P4') else p


def outer_binary_tensor(f, g12, p, route):
    """Coefficients in positive B2 tensor canonical pair-type B_n.

    The first axis is positive S²,ST,T². The second is the canonical
    positive binary frame, with the required A/P4 projection applied.
    No negative/positive binary SL2 identification is made.
    """
    n = route.pair_degree
    q = bridge_to_degree(f,g12,route.kind,p,route.degree)
    out = s.zeros(3,n+1)
    pair_basis = [coeff(typed_projection(f,route.pair_kind,b),n) for b in mon(n)]
    for index,c in enumerate(coeff(q,route.degree)):
        if c == 0:
            continue
        for (i,j),v in cg_monomial(2,n,route.outer_order,index).items():
            for k,w in enumerate(pair_basis[j]):
                if w != 0:
                    out[i,k] += c*v*w
    return out.applyfunc(s.factor)


class QOrthogonalLegCoefficientBuilder(NewD5LegCoefficientBuilder):
    """Abstract split quotient tensors in slots D5[0:5],A*[5:8].

    The raw three q-lifts need NOT define this equivariant splitting. Their
    exact D5-mixing transport must be supplied before physical use.
    """
    def __init__(self, f=PHYSICAL_F):
        super().__init__(f)
        self.q_templates = {}
        self.pair_templates = {}

    def harmonic_sources(self,a,hpoly):
        """All seven typed harmonic maps, including the formerly absent scalar."""
        out = super().harmonic_sources(a,hpoly)
        qa = polynomial(self.F4*coeff(s.expand(a*a),4),4)
        out.append(('a2h_tv4_1','1',tv(qa,hpoly,4)))
        return out

    def canonical_to_negative_pair(self,kind,p):
        """Invert the physical cubic conjugation on each typed pair summand."""
        if kind == '1':
            return p
        p = typed_projection(self.f,kind,p)
        if kind == 'A':
            return quadratic(self.f.inv()*op6(p)*self.f)
        if kind == 'D5':
            return quartic(self.f.inv()*op4(p)*self.f)
        if kind == 'V':
            return sextic(self.f.inv()*op2(p)*self.f)
        if kind == 'P4':
            return sextic(self.f.inv()*op6(p)*self.f)
        raise ValueError(kind)

    def pair_embedding(self,sector,kind,p):
        """Canonical type -> literal symmetric8x8 leg tensor (no V factor).

        AA uses negative B2 tensor B2 and J2 on BOTH dual A indices.
        AD uses negative B2 tensor B4 and J2 on the A index. The convention
        is a tensor d + d tensor a, with no implicit half in either block.
        """
        if sector == 'AA':
            if kind not in ('1','D5'):
                raise ValueError((sector,kind))
            degree = 0 if kind == '1' else 4
            neg = self.canonical_to_negative_pair(kind,p)
            pair = s.zeros(3)
            for index,c in enumerate(coeff(neg,degree)):
                for (i,j),v in cg_monomial(2,2,(4-degree)//2,index).items():
                    pair[i,j] += c*v
            out = s.zeros(8)
            out[5:,5:] = J2*pair*J2.T
            return out.applyfunc(s.factor)
        if sector == 'AD':
            if kind not in ('A','V','P4','D5'):
                raise ValueError((sector,kind))
            degree = {'A':2,'D5':4,'V':6,'P4':6}[kind]
            neg = self.canonical_to_negative_pair(kind,p)
            pair = s.zeros(3,5)
            for index,c in enumerate(coeff(neg,degree)):
                for (i,j),v in cg_monomial(2,4,(6-degree)//2,index).items():
                    pair[i,j] += c*v
            pair = J2*pair
            out = s.zeros(8)
            out[5:,:5] = pair
            out[:5,5:] = pair.T
            return out.applyfunc(s.factor)
        raise ValueError(sector)

    def q_template(self,route):
        if route not in self.q_templates:
            n = route.pair_degree
            pairkey = (route.sector,route.pair_kind)
            if pairkey not in self.pair_templates:
                self.pair_templates[pairkey] = [
                    self.pair_embedding(route.sector,route.pair_kind,p)
                    for p in mon(n)]
            pairs = self.pair_templates[pairkey]
            out = []
            for p in mon(CANONICAL_DEGREE[route.kind]):
                tensor = outer_binary_tensor(self.f,self.g12,p,route)
                K = s.zeros(8)
                for i in range(3):
                    for j in range(n+1):
                        if tensor[i,j] != 0:
                            K += (-y,z,x)[i]*tensor[i,j]*pairs[j]
                out.append(K.applyfunc(s.factor))
            self.q_templates[route] = out
        return self.q_templates[route]

    def q_apply(self,p,route,expand=True):
        K = sum((c*Q for c,Q in zip(coeff(p,CANONICAL_DEGREE[route.kind]),
                                    self.q_template(route)) if c != 0),s.zeros(8))
        return K.applyfunc(s.expand) if expand else K

    def iter_coefficients(self,a,hpoly,expand=True):
        """Yield (harmonic_or_trace,label,K), exact counts AA7+AD19+DD18 /1+4+3."""
        for category,sources in (
                ('harmonic',self.harmonic_sources(a,hpoly)),
                ('trace',[self.trace_source(a,hpoly)])):
            for name,kind,p in sources:
                for route in q_leg_target_routes(kind=kind):
                    yield category,name+'__'+route.label,self.q_apply(p,route,expand)
        # Calling the frozen method directly preserves its exact DD18+3.
        old = NewD5LegCoefficientBuilder(self.f)
        for category,label,K5 in old.iter_coefficients(a,hpoly,expand):
            K = s.zeros(8)
            K[:5,:5] = K5
            yield category,'DD__'+label,K


    def iter_raw_coefficients(self,a,hpoly,theta,expand=True):
        """Use the verified equivariant quotient section, preserving every raw term.

        Equivariance is modulo source shifts, not of polynomial representatives.
        The formal theta is exactly the unit in q0=(xy+z²)/theta.
        """
        for category,label,K in self.iter_coefficients(a,hpoly,expand):
            yield category,label,to_raw_coefficient(K,theta)


def build_q_orthogonal_leg_coefficients(a,hpoly,f=PHYSICAL_F,expand=True):
    out = {'harmonic':[],'trace':[]}
    for category,label,K in QOrthogonalLegCoefficientBuilder(f).iter_coefficients(a,hpoly,expand):
        out[category].append((label,K))
    assert len(out['harmonic']) == 44 and len(out['trace']) == 8
    return out['harmonic'],out['trace']


def build_raw_q_orthogonal_leg_coefficients(a,hpoly,theta,f=PHYSICAL_F,expand=True):
    """Return all44+8 in the literal raw8 frame, using the VERIFIED D5 mixing.

    The actual source interface uses PHYSICAL_F. An alternate f is meaningful
    only with all physical marking/leg conventions consistently transported.
    """
    out = {'harmonic':[],'trace':[]}
    for category,label,K in QOrthogonalLegCoefficientBuilder(f).iter_raw_coefficients(a,hpoly,theta,expand):
        out[category].append((label,K))
    assert len(out['harmonic']) == 44 and len(out['trace']) == 8
    return out['harmonic'],out['trace']


def transport_to_raw_legs(K, section_transport):
    """Apply a separately VERIFIED split-to-raw section matrix B.

    Canonical legs L_can=L_raw B imply K_raw=B K B^T. No identity section
    is assumed. This function checks algebraic size only, not equivariance.
    """
    if K.shape != (8,8) or section_transport.shape != (8,8):
        raise ValueError('Expected an 8x8 coefficient and verified 8x8 section transport.')
    if (K-K.T).applyfunc(s.expand) != s.zeros(8):
        raise ValueError('Coefficient tensor must be symmetric.')
    return (section_transport*K*section_transport.T).applyfunc(s.expand)


def full_q_c_residual_interface(K, section_transport):
    """Use a supplied verified section transport, retaining ALL raw residuals.

    q0=(xy+z²)/theta lives in the actual leg/source constructor. Coefficient
    maps never divide by q0. The abstract split tensor is NOT automatically
    a raw-leg coefficient: a nontrivial D5/A mixing may be required.
    """
    from universal_q_orthogonal_leg_completion import extend_q_C_source
    return extend_q_C_source(transport_to_raw_legs(K,section_transport))


def verified_q_c_residual_interface(K):
    """Canonical PHYSICAL_F split tensor -> verified raw quotient -> all sources.

    This uses the exact theta from the actual constructor, never a normalization.
    It makes no claim that a basis tensor solves the resulting source errors.
    """
    from universal_q_orthogonal_leg_completion import theta, extend_q_C_source
    return extend_q_C_source(to_raw_coefficient(K,theta))
