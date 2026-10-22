"""Explicit 18+5 supported N_W coefficient channels, with full c companion.
No independent-operator, source-quotient or obstruction-value assertion.
"""
from universal_complete_identity_w_coefficients import *
from universal_supported_w_action_assembly import positive_wedge_matrix

B6=(Kinc*Pstd).row_join(spin)
B6inv=B6.inv()

def physical_six_coefficient(K_balanced):
    """Transport Cartan4+Spin2 coefficient to physical positive two-forms."""
    return B6*K_balanced*B6inv

def n_w_coefficients(f,H0):
    """Return balanced Cartan4+Spin2 coefficients, not physical matrices."""
    d=k*S*S-2*h*S*T-l*T*T
    Delta=h*h+k*l
    qD=quartic(f*op4(d*d)*f.inv())
    qH=quartic(H0)
    g12=marked_twelve(f)
    rq=[('DeltaH_'+label,M) for label,M in coefficient_embeddings('D5',Delta*qH)]
    rh=[('Delta_'+label,M) for label,M in coefficient_embeddings('1',Delta)]
    rh += [('D5_'+label,M) for label,M in coefficient_embeddings('D5',qD)]
    for order in range(5):
        product=tv(qH,qD,order)
        for kind,p0 in typed_outputs(f,g12,product,8-2*order):
            for label,M in coefficient_embeddings(kind,p0):
                rq.append(('H_D5_tv'+str(order)+'_'+label,M))
    assert len(rq)==18 and len(rh)==5
    return rq,rh

def n_w_closed_action(K,polar,F):
    """Exact full supported K tensor N_W action on a closed two-form.
    K uses PHYSICAL six-space coordinates. F carries the rank-two source
    spinor factor. Output is entirely VW. Balanced coefficients must use
    n_w_balanced_closed_action instead.
    """
    E=positive_wedge_matrix(polar)
    Q=K*E+E*up*adj6(K)*low
    vv=putp(getp(F))
    iv=[contract([x,y,z,0,0],g) for g in vv]
    z0=s.Matrix([iv[a].get((i,),0) for i in range(3) for a in range(2)])
    mixed=[wedge(contract([x,y,z,0,0],g),{(3,):-w,(4,):u}) for g in putp(Q*z0)]
    return sc(-2,mixed)

def n_w_balanced_closed_action(K_balanced,polar,F):
    """Evaluate a generated balanced coefficient with its full frame transport."""
    return n_w_closed_action(physical_six_coefficient(K_balanced),polar,F)
