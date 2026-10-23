"""Complete 55 harmonic + 10 trace maps for the prescribed arbitrary-qB family.

The intrinsic target is V tensor Sym^2(A* tensor V*) = V tensor Sym^2(M9).
Cauchy and binary CG inclusions construct it without an equivariant physical
section.  Both negative A and positive V indices are retained.  The regular
physical section is optional, and its changes are full C-source boundaries.
No actual source coefficient, source-column system, or feasibility solve occurs.
"""
from dataclasses import dataclass
from functools import lru_cache

from universal_q_orthogonal_leg_coefficients import (
    s,S,T,x,y,z,mon,coeff,polynomial,cg_monomial,apolar_metric,J2,
    QOrthogonalLegCoefficientBuilder,QLegTargetRoute,PAIR_OUTER_CHOICES,
    outer_binary_tensor,typed_projection,CANONICAL_DEGREE,bridge_to_degree,
    PHYSICAL_F,
)


# A positive binary p=c0 S^2+c1 ST+c2 T^2 is -c0*y+c1*z+c2*x.
# D's positive index is the coefficient of (x,y,z), not a binary index.
POSITIVE_COVECTOR = s.Matrix([[0,0,1],[-1,0,0],[0,1,0]])
QUOTIENT_FRAME = s.kronecker_product(J2,POSITIVE_COVECTOR)


@lru_cache(None)
def cg_matrix(m,n,r):
    degree=m+n-2*r
    out=s.zeros((m+1)*(n+1),degree+1)
    for k in range(degree+1):
        for (i,j),v in cg_monomial(m,n,r,k).items():
            out[i*(n+1)+j,k]=v
    return out


def unflatten(v,rows,cols):
    return s.Matrix(rows,cols,list(v))


@dataclass(frozen=True)
class MiddlePairRoute:
    sector: str
    pair_order: int
    kind: str

    @property
    def label(self):
        return self.sector+'_cg'+str(self.pair_order)+'_'+self.kind


def middle_pair_routes(kind=None):
    """Twelve simple pair copies, with all repeated copies distinguished."""
    specs=[('SS00',0,'1'),('SS04',0,'D5'),('SS40',0,'D5'),
           ('SS44',0,'P4'),('SS44',0,'D5'),
           ('SS44',1,'A'),('SS44',1,'P4'),
           ('SS44',2,'D5'),('SS44',3,'V'),('SS44',4,'1'),
           ('AA22',0,'P4'),('AA22',0,'D5')]
    for sec,r,k in specs:
        if kind is None or k==kind:
            yield MiddlePairRoute(sec,r,k)


@dataclass(frozen=True)
class MiddleTargetRoute:
    pair: MiddlePairRoute
    outer_order: int
    degree: int
    kind: str

    @property
    def pair_kind(self):return self.pair.kind
    @property
    def pair_degree(self):return CANONICAL_DEGREE[self.pair.kind]
    @property
    def label(self):
        return self.pair.label+'_outer'+str(self.outer_order)+'_B'+str(self.degree)+'_'+self.kind


def middle_target_routes(kind=None):
    """36 simple target copies, character 1+8A+8V+9P4+10D5."""
    for pair in middle_pair_routes():
        for r,d,k in PAIR_OUTER_CHOICES[pair.kind]:
            if kind is None or k==kind:
                yield MiddleTargetRoute(pair,r,d,k)


class QMiddleQuotientCoefficientBuilder(QOrthogonalLegCoefficientBuilder):
    def __init__(self,f=PHYSICAL_F):
        super().__init__(f)
        self.middle_pairs={}
        self.middle_templates={}

    def cauchy_pair(self,p,route):
        """Canonical type -> symmetric9x9 in negative B2 tensor positive B2.

        Tensor rows and columns are (negative A index, positive V index).
        SS and AA mean symmetric/symmetric and alternating/alternating,
        respectively. The entire ordered-entry matrix is returned, no half.
        """
        p=typed_projection(self.f,route.kind,p)
        sec=route.sector
        if sec=='SS00':
            n,m=0,0;H=s.Matrix([[p]])
        elif sec=='SS04':
            n,m=0,4;H=coeff(p,4).T
        elif sec=='SS40':
            n,m=4,0;H=self.F4inv*coeff(p,4)
        elif sec=='SS44':
            n,m=4,4;d=8-2*route.pair_order
            q=bridge_to_degree(self.f,self.g12,route.kind,p,d)
            H=self.F4inv*unflatten(cg_matrix(4,4,route.pair_order)*coeff(q,d),5,5)
        elif sec=='AA22':
            n,m=2,2
            # V_positive tensor A_canonical -> A_negative tensor V_positive.
            rr=QLegTargetRoute('AD','A',0,8,route.kind)
            VA=outer_binary_tensor(self.f,self.g12,p,rr)
            Aback=s.Matrix.hstack(*[coeff(self.canonical_to_negative_pair('A',q),2) for q in mon(6)])
            H=Aback*VA.T
        else:raise ValueError(sec)
        # H's two indices are the pair labels; split each into two legs.
        tensor=cg_matrix(2,2,(4-n)//2)*H*cg_matrix(2,2,(4-m)//2).T
        K=s.Matrix(9,9,lambda a,b:tensor[3*(a//3)+(b//3),3*(a%3)+(b%3)])
        return K.applyfunc(s.factor)

    def pair_templates_for(self,route):
        if route not in self.middle_pairs:
            self.middle_pairs[route]=[self.cauchy_pair(p,route) for p in mon(CANONICAL_DEGREE[route.kind])]
        return self.middle_pairs[route]

    def middle_template(self,route):
        if route not in self.middle_templates:
            pairs=self.pair_templates_for(route.pair)
            out=[]
            for p in mon(CANONICAL_DEGREE[route.kind]):
                tensor=outer_binary_tensor(self.f,self.g12,p,route)
                K=s.zeros(9)
                for i in range(3):
                    for j in range(route.pair_degree+1):
                        if tensor[i,j]!=0:
                            K+=(-y,z,x)[i]*tensor[i,j]*pairs[j]
                out.append(K.applyfunc(s.factor))
            self.middle_templates[route]=out
        return self.middle_templates[route]

    def middle_apply(self,p,route,frame='intrinsic',expand=True):
        K=sum((c*Q for c,Q in zip(coeff(p,CANONICAL_DEGREE[route.kind]),self.middle_template(route)) if c!=0),s.zeros(9))
        if frame=='quotient':K=QUOTIENT_FRAME*K*QUOTIENT_FRAME.T
        elif frame=='physical':K=physical_representative(QUOTIENT_FRAME*K*QUOTIENT_FRAME.T)
        elif frame!='intrinsic':raise ValueError(frame)
        return K.applyfunc(s.expand) if expand else K

    def iter_coefficients(self,a,hpoly,frame='physical',expand=True):
        """65 exact maps; trace means bookkeeping, not added trace freedom."""
        for category,sources in (('harmonic',self.harmonic_sources(a,hpoly)),('trace',[self.trace_source(a,hpoly)])):
            for name,kind,p in sources:
                for route in middle_target_routes(kind):
                    yield category,name+'__'+route.label,self.middle_apply(p,route,frame,expand)


def physical_representative(K):
    """A regular symmetric12x12 section of a D-coordinate quotient tensor.

    The section R is NOT asserted equivariant. Only the quotient maps are;
    the explicit full-source correction below handles every section change.
    """
    from universal_graded_c_orthogonal_module import graded_module
    R=graded_module()['R']
    return (R*K*R.T).applyfunc(s.factor)


def section_change_coefficients(K,X):
    """R'=R+C X; return every C-factor term with exact halves.

    B'-B=C L^t+L C^t, L=R K X^t+(1/2)C X K X^t.
    X is arbitrary3x9; no equivariance or special entries are imposed.
    """
    from universal_graded_c_orthogonal_module import graded_module
    assert K.shape==(9,9) and X.shape==(3,9)
    assert (K-K.T).applyfunc(s.expand)==s.zeros(9)
    m=graded_module();R,C=m['R'],m['C']
    L=R*K*X.T+C*X*K*X.T/2
    return dict(section=R+C*X,C=C,L=L,
                difference=C*L.T+L*C.T)


def project_physical_coefficient(B):
    """Project a regular symmetric12x12 B, retaining every removed C factor.

    B-P B P^t=C L^t+L C^t with P=R D, M=Zeta B,
    N=Zeta B Zeta^t, and L=B Zeta^t-C N/2.
    """
    from universal_graded_c_orthogonal_module import graded_module
    assert B.shape==(12,12)
    assert (B-B.T).applyfunc(s.expand)==s.zeros(12)
    m=graded_module();D,R,C,Zeta=(m[k] for k in ('D','R','C','Zeta'))
    M=Zeta*B;N=M*Zeta.T;L=B*Zeta.T-C*N/2
    return dict(quotient=D*B*D.T,representative=R*D*B*D.T*R.T,
                C=C,M=M,N=N,L=L,difference=C*L.T+L*C.T)


def completed_C_factor_boundary(c,l,qpolynomial,cm):
    """Full source-boundary data for B=c*l^t+l*c^t, with l positive-linear.

    Returns H=q*l-kappa*p(ZH) with F_q(B)=S(c,H), UNHALVED S.
    If alpha_C=cm*c, the homotopy is e_C*[H,-]/cm and its dual
    H*e_C^t/cm. BOTH source ends are P=h alpha and Pd=beta hd=-P*.
    Caller supplies only the C-source label; no source columns are generated.
    """
    from universal_q_middle_completion_transport import homogeneous_partner
    from universal_graded_c_orthogonal_module import graded_module
    assert c.shape==(12,1) and l.shape==(12,1)
    module=graded_module()
    assert (module['D']*c).applyfunc(s.expand)==s.zeros(9,1)
    assert all(s.diff(v,t)==0 for v in c for t in (x,y,z))
    p1=homogeneous_partner(l,1)
    qparts=[homogeneous_partner(qpolynomial*s.eye(12)[:,j],2)['Z'] for j in range(12)]
    ZH=(sum((l[j]*qparts[j] for j in range(12)),s.zeros(6,1))+qpolynomial*p1['Z'])/2
    return dict(C=c,Hmixed=qpolynomial*l,Hpartner=ZH,
                source_label=module['Zeta']*c/cm,
                source_homotopy_scale=1/cm,
                endpoint_rule='P=h*alpha; Pd=beta*hd=-P^t',
                middle_rule='alpha*h+hd*beta=S(c,H)')


def projected_completion_boundary(B,qpolynomial,cm):
    """Full representative-change boundary for arbitrary physical B.

    The three returned partners are literal differentiated polynomial legs.
    If Q_j=L2(q e_j) and H_i=L1(M^t_i), their full exterior values are
    l_i=(Q M^t_i+q H_i-q(C N)_i)/2. In particular Q M^t is NOT L3(q M^t).
    Endpoint homotopies retain 1/cm and both prescribed dual source blocks.
    """
    data=project_physical_coefficient(B)
    data['boundaries']=[completed_C_factor_boundary(data['C'][:,i],data['L'][:,i],qpolynomial,cm) for i in range(3)]
    return data


def build_q_middle_quotient_coefficients(a,hpoly,f=PHYSICAL_F,frame='physical',expand=True):
    out={'harmonic':[],'trace':[]}
    for cat,label,K in QMiddleQuotientCoefficientBuilder(f).iter_coefficients(a,hpoly,frame,expand):
        out[cat].append((label,K))
    assert len(out['harmonic'])==55 and len(out['trace'])==10
    return out['harmonic'],out['trace']
