"""Exact equivariant quotient-label adapter for the raw q-orthogonal legs.

No polynomial splitting is asserted equivariant. The correction is literal;
its labels are equivariant modulo the proved A/C source submodule.
"""
import sympy as s


def quotient_section_matrix(theta):
    """Columns: five unchanged D5 legs, then corrected dual-A legs.

    raw-leg matrix times this matrix gives the corrected representatives.
    Both source tensor indices must be transported for a middle coefficient.
    """
    P=s.eye(8)
    P[3,5]=1/(12*theta)
    P[2,6]=-1/(4*theta)
    P[1,7]=1/(4*theta)
    return P


def to_raw_coefficient(K,theta):
    if K.shape!=(8,8) or K!=K.T:
        raise ValueError('Expected a symmetric 8-by-8 coefficient tensor')
    P=quotient_section_matrix(theta)
    return (P*K*P.T).applyfunc(s.expand)


def corrected_leg_records(raw_legs,theta):
    if len(raw_legs)!=8:
        raise ValueError('Expected D5-then-dual-A raw legs')
    P=quotient_section_matrix(theta)
    out=[]
    for j in range(8):
        record={}
        for field in ('Z','rC','R0'):
            record[field]=sum((P[i,j]*raw_legs[i][field] for i in range(8)),
                              s.zeros(*raw_legs[0][field].shape)).applyfunc(s.factor)
        record['Y']=[sum((P[i,j]*raw_legs[i]['Y'][r] for i in range(8)),
                         s.zeros(*raw_legs[0]['Y'][r].shape)).applyfunc(s.factor)
                     for r in range(2)]
        out.append(record)
    return out
