"""Exact complete C residual of arbitrary q times a symmetric-linear middle.

No source equations are solved. The canonical q quotient is full-U balanced
but its C,C cochain anomaly is retained explicitly.
"""
from universal_q_middle_completion_transport import *


def vww_zero_WW_to_mixed(G,degree):
    """Literal Koszul transport p(G)=mixed(d0,d1), assuming v.G=0."""
    assert G.shape==(6,1)
    check_degree(G,degree)
    h=s.zeros(6,1)
    for a in range(2):
        g=s.Matrix([G[2*i+a] for i in range(3)])
        assert s.expand((positive.T*g)[0])==0
        curl=s.Matrix([s.diff(g[2],y)-s.diff(g[1],z),
                       s.diff(g[0],z)-s.diff(g[2],x),
                       s.diff(g[1],x)-s.diff(g[0],y)])
        for i in range(3):h[2*i+a]=-curl[i]/(degree+1)
    converted=s.Matrix.vstack(-w*h,u*h)
    eqvec(vww_leg(G),mixed(converted[:6,:],converted[6:,:]))
    return converted


def q_middle_C_interface(coefficient,qpolynomial=quadratic,completed=None):
    """For kAt/kappa times the paired completion, return the exact interface.

    C residual = kAt cm [q/kappa*N1 - q*p(ZN) + D3 + kappa*p(G5)].
    N1-kappa*p(ZN) annihilates both complete U columns. D3 has no WW part.
    The C,C anomaly is stored; no independently closed cochain is asserted.
    The additive actual divided arrow is Vnorm-kappa^-1*N1+p(ZN),
    multiplied by kAt cm, exactly once.
    """
    out=q_linear_middle_completion(coefficient,qpolynomial) if completed is None else completed
    assert out['coefficient']==coefficient and out['q']==qpolynomial
    ZB=s.Matrix.hstack(*(bb['Z'] for bb in out['Blegs']))
    ZQ=s.Matrix.hstack(*(qq['Z'] for qq in out['Qlegs']))
    const=[mixed(s.eye(12)[:6,j],s.eye(12)[6:,j]) for j in range(12)]
    Ccols=[C_column(sp)[0] for sp in mon(2)]
    E=s.Matrix([[scalar_pairing(gg,cc) for gg in const] for cc in Ccols])
    RC_B=s.Matrix([[scalar_pairing(vww_leg(ZB[:,i]),cc) for cc in Ccols] for i in range(12)])
    RC_Q=s.Matrix([[scalar_pairing(vww_leg(ZQ[:,i]),cc) for cc in Ccols] for i in range(12)])
    N1=(coefficient*E.T).applyfunc(s.expand)
    ZN=s.Matrix.hstack(*(homogeneous_partner(N1[:,j],2)['Z'] for j in range(3)))
    D3mixed=-(coefficient*RC_Q+qpolynomial*RC_B)/2
    D3vww=(-(ZQ*N1+qpolynomial*ZB*E.T)/2+qpolynomial*ZN).applyfunc(s.expand)
    converted=s.Matrix.hstack(*(vww_zero_WW_to_mixed(D3vww[:,j],3) for j in range(3)))
    D3coeff=(D3mixed+converted).applyfunc(s.expand)
    G5=((ZB*RC_Q+ZQ*RC_B)/2).applyfunc(s.expand)
    D3=[mixed(D3coeff[:6,j],D3coeff[6:,j]) for j in range(3)]
    quotient_Y=[mixed(N1[:6,j],N1[6:,j]) for j in range(3)]
    ZNC=s.Matrix([[scalar_pairing(vww_leg(ZN[:,i]),cc) for cc in Ccols] for i in range(3)])
    # Remainder D3+kappa*G5 has C,C antisymmetry q*(ZNC-ZNC^t).
    # The qN part has the opposite anomaly. Neither is silently deleted.
    out.update(D3=D3,D3coeff=D3coeff,G5=G5,quotient_Y=quotient_Y,
               quotient_Y_coeff=N1,quotient_Z=ZN,D3_mixed_raw=D3mixed,
               D3_vww_raw=D3vww,E=E,RC_B=RC_B,RC_Q=RC_Q,ZB=ZB,ZQ=ZQ,
               quotient_Z_C=ZNC,C_C_anomaly_factor=ZNC-ZNC.T)
    return out


def extend_q_middle_C_source(coefficient):
    """Unconditional source candidates/errors, not a source-equation solve."""
    from universal_orthogonal_leg_source_map_extension import extend_C_source,q
    out=q_middle_C_interface(coefficient,q)
    out['source_extension']=extend_C_source(out['D3'],out['G5'])
    return out


def restore_q_middle_companion(record,am,bm,cm,kAt):
    """Restore full source/divided data using the identical checked interface.

    Input must be extend_q_middle_C_source output, with the actual q0.
    Keeps all source errors and the fixed negative determinant-dual arrow.
    """
    from universal_q_orthogonal_leg_completion import restore_q_companion
    return restore_q_companion(record,am,bm,cm,kAt)
