"""Constructive lower-middle correction: T C divisible by q -> exact C kernel.

No full-U completion, divided arrow, or higher-weight term is removed.
All transformations use the checked physical constant C-pairing split.
"""
from universal_graded_c_orthogonal_module import *

positive=s.Matrix([x,y,z])
quadratic=x*y+z*z


def check_degree(entries,degree):
    for entry in entries:
        p=s.Poly(s.expand(entry),x,y,z)
        assert all(sum(mon)==degree or coeff==0 for mon,coeff in p.terms()),(degree,entry)


def exact_quotient(entries,polynomial):
    out=[]
    for entry in entries:
        quotient,remainder=s.div(s.Poly(s.expand(entry),x,y,z),s.Poly(polynomial,x,y,z))
        assert remainder.is_zero,('non-divisible lower-C coefficient',entry)
        out.append(quotient.as_expr())
    return out


def symmetric_linear_inverse(residual):
    """For every free quadratic vector r, B=B^t and B*v=r."""
    J=residual.jacobian(positive)
    F=(positive.T*residual)[0]
    return J+J.T-s.hessian(F,positive)/2


def skew_linear_inverse(residual):
    """For quadratic r with v*r=0, B=-B^t and B*v=r."""
    assert s.expand((positive.T*residual)[0])==0
    J=residual.jacobian(positive)
    return (J-J.T)/3


def q_cubic_lift(T,qpolynomial=quadratic,known_defect=None):
    """T=T_exact+q B, with T_exact C=0 and B symmetric positive-linear.

    T is a symmetric physical twelve-by-twelve cubic coefficient matrix.
    qpolynomial is a degree-two scalar polynomial (may include the actual
    invariant-frame unit). known_defect is only a speed aid and is checked
    against the literal full physical pairing before any construction.
    """
    assert T.shape==(12,12)
    assert (T-T.T).applyfunc(s.expand)==s.zeros(12)
    check_degree(T,3);check_degree([qpolynomial],2)
    m=graded_module();row=s.diag(positive.T,positive.T,positive.T)
    E=row*m['D']
    if known_defect is None:
        entries=exact_quotient(T*E.T,qpolynomial)
        defect=s.Matrix(12,3,entries)
    else:defect=known_defect
    assert (T*E.T-qpolynomial*defect).applyfunc(s.expand)==s.zeros(12,3)
    check_degree(defect,2)
    basis=m['C'].row_join(m['R'])
    inverse=m['Zeta'].col_join(m['D'])
    assert (inverse*basis-s.eye(12)).applyfunc(s.expand)==s.zeros(12)
    rho=inverse*defect
    B=s.zeros(12)
    # The C-C block is freely left zero. Mixed C/(A tensor V) blocks use
    # scalar Euler inversion; symmetry fixes the transpose block.
    for c in range(3):
        for b in range(3):
            for i in range(3):
                value=s.diff(rho[c,b],positive[i])/2
                B[c,3+3*b+i]=B[3+3*b+i,c]=value
    # Off-diagonal A blocks are not themselves V-symmetric. Decompose
    # using the transpose A block, retaining its alternating sector.
    for a in range(3):
        for b in range(a,3):
            rab=rho[3+3*a:6+3*a,b]
            rba=rho[3+3*b:6+3*b,a]
            rp=(rab+rba)/2;rm=(rab-rba)/2
            block=symmetric_linear_inverse(rp)+skew_linear_inverse(rm)
            B[3+3*a:6+3*a,3+3*b:6+3*b]=block
            B[3+3*b:6+3*b,3+3*a:6+3*a]=block.T
    correction=(basis*B*basis.T).applyfunc(s.expand)
    exact=(T-qpolynomial*correction).applyfunc(s.expand)
    assert (correction-correction.T).applyfunc(s.expand)==s.zeros(12)
    assert (exact*E.T).applyfunc(s.expand)==s.zeros(12,3)
    check_degree(correction,1);check_degree(exact,3)
    return dict(exact=exact,correction=correction,defect=defect,
                split_correction=B,pairing=E,q=qpolynomial)


def standard_q_orthogonal_legs():
    """Three q-pairing legs and the five exact legs, no completion asserted."""
    m=graded_module();grad=s.Matrix([y/2,x/2,z])
    QQ=m['R']*s.diag(grad,grad,grad)
    all_legs=QQ.row_join(m['Y'])
    row=s.diag(positive.T,positive.T,positive.T)*m['D']
    assert (row*all_legs-quadratic*s.eye(3).row_join(s.zeros(3,5))).applyfunc(s.expand)==s.zeros(3,8)
    return all_legs


def reconstruct_q_leg(y,degree):
    """Exact all-degree q-orthogonal leg generation with source coefficients."""
    m=graded_module();row=s.diag(positive.T,positive.T,positive.T)*m['D']
    rho=s.Matrix(3,y.cols,exact_quotient(row*y,quadratic))
    QQ=standard_q_orthogonal_legs()[:,:3]
    result=reconstruct_leg(y-QQ*rho,degree)
    result['A_new']=rho
    assert (m['C']*result['C']+m['Acoeff']*result['A']+m['Y']*result['D5']+QQ*rho-y).applyfunc(s.expand)==s.zeros(*y.shape)
    return result
