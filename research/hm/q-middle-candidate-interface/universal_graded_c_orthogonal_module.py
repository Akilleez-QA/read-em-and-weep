"""All-degree C-orthogonal mixed legs, with literal physical source shifts.

No physical coefficient, source value, point, or marking is specialized.
All finite inversions are checked Laurent-unit identities. The polynomial
variables stay free; no rank or actual-instance experiment is used.
"""
from functools import lru_cache
from itertools import combinations
from universal_degree_one_c_orthogonal_module import *
from universal_degree_one_c_orthogonal_module import _eliminate,_backsolve,_coefficient_rows

positive_variables=(x,y,z)
positive_pairs=((0,1),(0,2),(1,2))
KOSZUL2=s.Matrix([[-y,-z,0],[x,0,-z],[0,x,y]])
KOSZUL3=s.Matrix([z,-y,x])

def potential(q,degree):
    """Koszul contracting homotopy on A-valued positive homogeneous one-forms.

    For row_v q=0, KOSZUL2*potential(q,d)=q, blockwise.
    Coefficients may be matrices and stay wholly formal.
    """
    assert q.rows==9 and degree>=0
    return s.Matrix.vstack(*[(q[3*a+j,:].diff(positive_variables[i])-q[3*a+i,:].diff(positive_variables[j]))/(degree+1)
                             for a in range(3) for i,j in positive_pairs])


def relation_potential(h,degree):
    """Koszul homotopy on homogeneous two-forms; kernel δ2 equals image δ3."""
    assert h.rows==9 and degree>=0
    return s.Matrix.vstack(*[(h[3*a+2,:].diff(x)-h[3*a+1,:].diff(y)+h[3*a,:].diff(z))/(degree+2)
                             for a in range(3)])


@lru_cache(None)
def graded_module():
    t=s.Matrix(s.symbols('graded_free_leg0:12'))
    yy=mixed(t[:6,:],t[6:,:])
    D=s.Matrix([[s.diff(scalar_pairing(yy,C_column(sp)[0]),vi,tt) for tt in t]
                for sp in mon(2) for vi in positive_variables])
    rhs=s.symbols('graded_pairing_rhs0:9')
    pivots=_eliminate(_coefficient_rows(D*t,t),rhs)
    Rraw=_backsolve(pivots,12).jacobian(rhs)
    _,_,_,Zeta=cartan_pair_split()
    C=s.Matrix.hstack(*[s.Matrix.vstack(*C_column(sp)[1]) for sp in mon(2)])
    Zeta=Zeta*s.diag(Pstd.inv()*extract,Pstd.inv()*extract)
    R=((s.eye(12)-C*Zeta)*Rraw).applyfunc(s.factor)
    zero=lambda M: M.applyfunc(s.expand)==s.zeros(*M.shape)
    assert zero(D*C) and zero(Zeta*C-s.eye(3))
    assert zero(D*R-s.eye(9)) and zero(Zeta*R)
    assert zero(R*D+C*Zeta-s.eye(12))
    Acoeff=s.Matrix.hstack(*[s.Matrix.vstack(*[
        s.kronecker_product(s.Matrix(positive_variables),s.eye(2)[:,a]) if rr==r else s.zeros(6,1)
        for rr in range(2)]) for r in range(2) for a in range(2)])
    old=build_module()
    Y=s.Matrix.hstack(*[s.Matrix.vstack(*yy) for yy in old['normalized']])
    P=potential(D*Acoeff,1).row_join(potential(D*Y,1))
    determinant=s.factor(P.det())
    assert determinant==2*FB**4*FC**3*FD**2/9
    Pinv=P.inv().applyfunc(s.factor)
    d2=s.diag(KOSZUL2,KOSZUL2,KOSZUL2)
    d3=s.diag(KOSZUL3,KOSZUL3,KOSZUL3)
    full_relation=(Pinv*d3).applyfunc(s.factor)
    H,Rel=full_relation[:4,:],full_relation[4:,:]
    Cshift=(Zeta*Acoeff*H).applyfunc(s.factor)
    assert zero(R*d2*P-(s.eye(12)-C*Zeta)*Acoeff.row_join(Y))
    assert zero(Y*Rel+Acoeff*H-C*Cshift)
    ZG=s.Matrix.hstack(*old['partners'])
    sigma=-s.Matrix([[sum((u,w)[r]*H[2*r+a,j] for r in range(2)) for j in range(3)] for a in range(2)])
    Wcoeff=(ZG*Rel+s.Matrix.vstack(*[Mi*sigma for Mi in Ms])).applyfunc(s.factor)
    WC=s.Matrix.hstack(*[s.Matrix([scalar_pairing(vww_leg(Wcoeff[:,j]),C_column(sp)[0]) for sp in mon(2)]) for j in range(3)])
    return dict(D=D,C=C,Zeta=Zeta,R=R,pivots=pivots,d2=d2,d3=d3,
                Acoeff=Acoeff,Y=Y,ZG=ZG,P=P,Pinv=Pinv,detP=determinant,
                relation=Rel,relation_A=H,relation_C=Cshift,
                relation_sigma=sigma,relation_W=Wcoeff,relation_WC=WC)


def reconstruct_leg(y,degree):
    """Constructively decompose ANY homogeneous C-orthogonal mixed leg.

    Returns y=C*c+Acoeff*a+Y*b. All source coefficients are retained.
    This includes arbitrary polynomial coefficients, not just degree one.
    """
    m=graded_module();q=m['D']*y
    vv=s.Matrix([positive_variables])
    assert all((vv*q[3*j:3*j+3,:]).applyfunc(s.expand)==s.zeros(1,y.cols) for j in range(3))
    h=potential(q,degree)
    assert (m['d2']*h-q).applyfunc(s.expand)==s.zeros(*q.shape)
    parts=m['Pinv']*h
    a,b=parts[:4,:],parts[4:,:]
    c=m['Zeta']*y-m['Zeta']*m['Acoeff']*a
    assert (m['C']*c+m['Acoeff']*a+m['Y']*b-y).applyfunc(s.expand)==s.zeros(*y.shape)
    return dict(C=c,A=a,D5=b,koszul=h)


def fitting_certificate():
    """Ten checked exterior-cube identities generate exactly (x,y,z)^3.

    This is a universal polynomial ideal certificate, not a point test or
    an evaluated rank calculation.
    """
    m=graded_module();Rel=m['relation']
    I=list(combinations(range(5),3))
    minors=[s.factor(Rel[list(rows),:].det()) for rows in I]
    scales=[2*FB*FC*FD,2*FB**2*FD**2/(3*FC),2*FB**2*FC*FD**2/3,
            FB*FC*FD/3,FB*FC*FD/9,-FB*FC*FD/9,-2*FB*FC*FD,
            2*FB*FC*FD/3,2*FB**2*FC*FD**2/3,FB*FC*FD/9]
    n=[s.expand(a*b) for a,b in zip(scales,minors)]
    expected=[x*x*z,x*y*y-y*z*z,FB*FD*x**3+3*FC**2*y*y*z,x*y*z-z**3,
              y*z*z,x*x*y-x*z*z,x*z*z,x*y*z,FB*FD*x*x*z+3*FC**2*y**3,y*y*z]
    assert all(s.expand(a-b)==0 for a,b in zip(n,expected))
    reconstruction=[(n[2]-3*FC**2*n[9])/(FB*FD),n[5]+n[6],n[0],n[1]+n[4],n[7],n[6],
                    (n[8]-FB*FD*n[0])/(3*FC**2),n[9],n[4],n[7]-n[3]]
    cubics=[x**3,x*x*y,x*x*z,x*y*y,x*y*z,x*z*z,y**3,y*y*z,y*z*z,z**3]
    assert all(s.expand(a-b)==0 for a,b in zip(reconstruction,cubics))
    return dict(indices=I,minors=minors,scales=scales,normalized=n,
                reconstruction=reconstruction,cubics=cubics)
