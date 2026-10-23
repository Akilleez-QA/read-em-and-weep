"""Explicit product-rule transport for q-middle full-U completions.

This constructs companions, not an equivalence with any other completion.
It never discards the divided arrow or its C,C anomaly.
"""
from universal_q_cubic_kernel_lift import *


def homogeneous_partner(coefficients,degree):
    """Euler partner of a homogeneous mixed leg of positive degree."""
    assert coefficients.shape==(12,1) and degree>0
    check_degree(coefficients,degree)
    Y=mixed(coefficients[:6,:],coefficients[6:,:])
    r=s.Matrix([[scalar_pairing(Y,B(s.eye(2)[:,j])) for j in range(2)]])
    Z=s.Matrix.vstack(*[J*r.diff(vi).T/degree for vi in positive])
    zleg=vww_leg(Z)
    for j in range(2):
        assert s.expand(scalar_pairing(zleg,A(s.eye(2)[:,j]))-r[j])==0
        assert not pair(zleg,B(s.eye(2)[:,j]))
        assert not pair(Y,A(s.eye(2)[:,j]))
    return dict(Y=Y,Z=Z,rB=r)


def coefficient_gradient_partner(scalar,row):
    """Six-vector p(J grad(scalar) row); the exterior p is not applied yet."""
    return s.Matrix.vstack(*[J*row.T*s.diff(scalar,vi) for vi in positive])


def q_linear_middle_completion(coefficient,qpolynomial=quadratic):
    """Return a full-U completion whose lower coefficient is q*coefficient.

    coefficient is symmetric12x12 and linear in x,y,z. All its derivatives
    are taken literally, including any dependence inherited from K(v).
    Pair degree-one B-column legs with degree-two q times constant legs.
    This chosen completion need not be the one induced by other generators.
    """
    assert coefficient.shape==(12,12)
    assert (coefficient-coefficient.T).applyfunc(s.expand)==s.zeros(12)
    check_degree(coefficient,1);check_degree([qpolynomial],2)
    Blegs=[homogeneous_partner(coefficient[:,j],1) for j in range(12)]
    Qlegs=[homogeneous_partner(qpolynomial*s.eye(12)[:,j],2) for j in range(12)]
    def action(eta,am,bm):
        kap=bm/am;out=[]
        for bb,qq in zip(Blegs,Qlegs):
            lb=adds(bb['Y'],sc(-kap,vww_leg(bb['Z'])))
            lq=adds(qq['Y'],sc(-kap,vww_leg(qq['Z'])))
            out.extend([sc(scalar_pairing(lq,eta)/2,lb),sc(scalar_pairing(lb,eta)/2,lq)])
        return adds(*out)
    return dict(Blegs=Blegs,Qlegs=Qlegs,action=action,coefficient=coefficient,q=qpolynomial)
