"""q-orthogonal mixed-leg quotient and explicit all-scale source interface.

Universal formal coefficient identities only. Frozen dependencies are read-only.
No source solution, selected actual coefficients, rank, or model is evaluated.
"""
from universal_degree_one_c_orthogonal_module import *
from universal_orthogonal_leg_source_map_extension import extend_C_source,theta,q,C_action

@lru_cache(None)
def q_orthogonal_legs():
    """D5 followed by three lifts with Y_i*C=q e_i, all in literal M9."""
    module=build_module();D,Mu,C,Zeta=cartan_pair_split()
    out=[]
    for leg in quartic_adapted_legs():
        out.append(dict(Y=leg['Y'],Z=leg['Z'],rC=leg['C'],R0=s.zeros(1,3),removed=s.zeros(3,1)))
    for target in range(3):
        rhs=[s.Rational(1,1)/theta if j//6==target and j%6 in (1,5) else 0 for j in range(18)]
        vector=module['right_inverse'].subs(dict(zip(module['rhs'],rhs)), simultaneous=True)
        raw=module['blocks'](vector)
        cc=s.Matrix.vstack(*(Pstd.inv()*extract*b for b in raw))
        removed=(Zeta*cc).applyfunc(s.factor);projected=cc-C*removed
        yy=[(spin*(cliff*raw[r])+Cinc*projected[4*r:4*r+4,:]).applyfunc(s.factor) for r in range(2)]
        yf=mixed(*yy)
        rb=s.Matrix([[scalar_pairing(yf,B(s.eye(2)[:,j])) for j in range(2)]])
        zz=s.Matrix.vstack(*[J*rb.diff(vi).T for vi in (x,y,z)]).applyfunc(s.factor)
        zf=vww_leg(zz)
        rc=s.Matrix([[scalar_pairing(zf,C_column(sp)[0]) for sp in mon(2)]])
        rr=s.eye(3)[target,:]
        for j,sp in enumerate(mon(2)):
            assert s.expand(scalar_pairing(yf,C_column(sp)[0])-q*rr[j])==0
        out.append(dict(Y=yy,Z=zz,rC=rc,R0=rr,removed=removed,raw=raw))
    return out


def q_completed_family_interface(coefficient):
    """All residuals and actual quotient, for a symmetric positive-linear K.

    Tnew=kAt/kappa L K L*, L=Y-kappa Z. Before source correction:
      C1=kAt cm/kappa q Y K R0,
      C3=kAt cm(-Y K rC-q Z K R0),
      C5=kAt cm kappa p(GZ K rC).
    The explicit q-valued left cochain is kAt cm/kappa L K R0;
    it is NOT asserted separately closed as a monad cochain.
    """
    assert coefficient.shape==(8,8)
    assert (coefficient-coefficient.T).applyfunc(s.expand)==s.zeros(8)
    legs=q_orthogonal_legs()
    Ys=[s.Matrix.hstack(*(leg['Y'][r] for leg in legs)) for r in range(2)]
    GZ=s.Matrix.hstack(*(leg['Z'] for leg in legs))
    RC=s.Matrix.vstack(*(leg['rC'] for leg in legs))
    R0=s.Matrix.vstack(*(leg['R0'] for leg in legs))
    tr=coefficient*RC;tr0=coefficient*R0
    D3=[sc(-1,mixed(*(yy*tr[:,j] for yy in Ys))) for j in range(3)]
    G5=GZ*tr
    quotient_Y=[mixed(*(yy*tr0[:,j] for yy in Ys)) for j in range(3)]
    quotient_Z=GZ*tr0
    return dict(D3=D3,G5=G5,quotient_Y=quotient_Y,quotient_Z=quotient_Z,
                leg_Y=Ys,leg_Z=GZ,RC=RC,R0=R0,coefficient=coefficient)


def extend_q_C_source(coefficient):
    """Construct additive candidates and all errors; never solve them.

    The actual new normalized divided left arrow (C columns) is
      Vnorm - kappa^-1 quotient_Y + p(quotient_Z).
    Multiply by kAt cm and add the OLD divided arrow, once. Source end
      kAt [[0,(cm/am)Pc],[0,-y]]
    is exactly the existing extension, with its fixed negative-dual end.
    """
    out=q_completed_family_interface(coefficient)
    out['source_extension']=extend_C_source(out['D3'],out['G5'])
    return out


def restore_q_companion(record,am,bm,cm,kAt):
    """Restore the entire additive five-source end and divided arrow.

    Input is extend_q_C_source(K). Output is unconditional candidate data,
    not a claim of vanishing errors or closure. The right arrow is the
    FIXED negative determinant dual: right(eta)_i=b(left_i,eta)/det.
    Add these source/arrow increments to the frozen old ones exactly once.
    divided_right_pairing retains raw four-form values off-image; the scalar
    divided_right action is valid only after exterior-closure errors vanish.
    """
    kap=bm/am;ex=record['source_extension']
    source=s.zeros(5)
    source[:2,2:]=kAt*cm/am*ex['Pc']
    source[2:,2:]=-kAt*ex['y']
    divided=[[{},{}],[{},{}]]
    for j in range(3):
        extra=adds(sc(-1/kap,record['quotient_Y'][j]),vww_leg(record['quotient_Z'][:,j]))
        divided.append(sc(kAt*cm,adds(ex['high'][j]['Vnorm'],extra)))
    def right_pairing(eta):
        return [pair(v,eta) for v in divided]
    def right(eta):
        assert all(not contract(coords,ff) for v in divided for ff in v), 'Scalar right arrow requires vanishing exterior-closure errors.'
        return s.Matrix([[scalar_pairing(v,eta) for v in divided]])
    return dict(source_left=source,source_right=-source.T,
                divided_left=divided,divided_right=right,divided_right_pairing=right_pairing,
                source_errors=ex)


def q_completed_middle_action(record,eta,am,bm,kAt):
    """Actual skew middle kAt*(am/bm)*L K L* on any closed eta.

    record is q_completed_family_interface(K) or extend_q_C_source(K).
    No source/error vanishing assumption is used by this middle action.
    """
    kap=bm/am
    legs=[adds(mixed(record['leg_Y'][0][:,i],record['leg_Y'][1][:,i]),
               sc(-kap,vww_leg(record['leg_Z'][:,i]))) for i in range(8)]
    rhs=s.Matrix([scalar_pairing(leg,eta) for leg in legs])
    weights=record['coefficient']*rhs
    return adds(*(sc(kAt/kap*weights[i],leg) for i,leg in enumerate(legs)))
