"""Linear C-source extension for a full-U-zero, C1-zero new middle.

The frozen supported216 map is not edited or invoked on the new middle.
Input D3 is its normalized complete weight-three C output; G5 is its
normalized VWW primitive at weight five. Every off-image error is retained.
"""
from universal_physical_mixed_leg_foundation import *
from universal_regular_negative_ell_inverse import regular_cubic_ell_split_degree

theta=s.symbols('mixed_theta',nonzero=True)
q=(x*y+z*z)/theta

def expand_matrix(m):return m.applyfunc(s.expand)
def lap(p):return s.expand(theta*(4*s.diff(p,x,y)+s.diff(p,z,2)))
def delta(p):return s.expand(S*s.diff(p,u)+T*s.diff(p,w))
def C_action(v):return adds(*(sc(v[j],C_column(mon(2)[j])[0]) for j in range(3)))
def get_mixed(F,wi):return s.Matrix([F[a].get((i,wi),0) for i in range(3) for a in range(2)])
def binary_cartan(v):return poly(f.inv()*Pstd.inv()*extract*v,3)
def primitive_from_principal(v):
    return adds(*[[contract(coords,wedge(ff,{(3+r,):1})) for ff in putp(v.diff(ww)/3)]
                  for r,ww in enumerate((u,w))])

def extend_C_source(D3,G5):
    """Return additive candidates/errors, not a source-feasibility decision.

    For middle kAt*kappa^-1 L K L*, actual new C output is
    kAt*cm*(D3+kappa*p(G5)). Output source increment is
    kAt*[[0,(cm/am)Pc],[0,-y]], with its negative-dual right endpoint.
    Existing old H/Pc/LC and rawC/R/y errors combine linearly with this
    result. Old P,K,Qmat,Paa and every old U error are unchanged.
    """
    assert len(D3)==3 and G5.shape==(6,3)
    Pc=expand_matrix(cliff*low*G5/3)
    LC=expand_matrix(extract*low*G5)
    assert expand_matrix(G5-s.Matrix.vstack(*Ms)*Pc-up*Kinc*LC)==s.zeros(6,3)
    low_residual=[];records=[];ys=[]
    jform={(3,):-w,(4,):u}
    for j in range(3):
        assert all(not contract(coords,ff) and (3,4) not in ff for ff in D3[j])
        L5=adds(vww_leg(G5[:,j]),sc(-1,B(Pc[:,j])))
        low_residual.append(L5)
        R=adds(D3[j],sc(-1,A(Pc[:,j])))
        E=getp(R);eb=binary_cartan(E)
        sigma=s.expand(eb.subs({S:u,T:w},simultaneous=True))
        rq=lap(sigma)/6;sigma_h=s.expand(sigma-q*rq)
        assert lap(sigma_h)==0
        E0=expand_matrix(Cinc*f*coeff(delta(delta(delta(rq)))/120,3))
        ypoly,polar=regular_cubic_ell_split_degree(binary_cartan(E-q*E0),u,w,S,T,3)
        ycol=coeff(ypoly,2);ys.append(ycol)
        R1=adds(R,C_action(ycol))
        V0=primitive_from_principal(E0)
        Hhigh=adds(R1,sc(-q,V0))
        Lhigh=expand_matrix((get_mixed(Hhigh,4).diff(u)-get_mixed(Hhigh,3).diff(w))/3)
        Lwedge=[wedge({(i,):Lhigh[2*i+a] for i in range(3)},jform) for a in range(2)]
        full_error=adds(Hhigh,sc(-1,Lwedge))
        expected=spin*cliff*E+Cinc*f*coeff(delta(delta(delta(sigma_h)))/120,3)
        assert expand_matrix(getp(Hhigh)-expected)==s.zeros(6,1)
        Lquot=Lhigh.applyfunc(lambda e:lap(e)/10)
        Lharm=expand_matrix(Lhigh-q*Lquot)
        assert Lharm.applyfunc(lap)==s.zeros(6,1)
        qform=[wedge({(i,):Lquot[2*i+a] for i in range(3)},jform) for a in range(2)]
        hform=[wedge({(i,):Lharm[2*i+a] for i in range(3)},jform) for a in range(2)]
        Vnorm=sc(-1,adds(V0,qform))
        eqvec(adds(R1,sc(q,Vnorm)),adds(full_error,hform))
        records.append(dict(R=R,R1=R1,E=E,high_spin=cliff*E,sigma=sigma,
            rq=rq,sigma_harmonic=sigma_h,E0=E0,y=ycol,ell_polar=polar,
            V0=V0,Hhigh=Hhigh,Lhigh=Lhigh,Lquot=Lquot,Lharm=Lharm,
            high_full_remainder=full_error,Vnorm=Vnorm))
    return dict(H=G5,Pc=Pc,LC=LC,y=s.Matrix.hstack(*ys),
                low_literal=low_residual,high=records,D3=D3)
