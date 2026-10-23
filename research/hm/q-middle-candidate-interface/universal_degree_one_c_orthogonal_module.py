"""Universal degree-one C-orthogonal module by exact coefficient identities.

This is the explicitly authorized small 18-equation/36-coefficient problem,
not an actual-instance matrix/rank scan. No source or marking is evaluated.
All elimination pivots are Laurent units, and the right inverse is checked.
"""
from universal_c_orthogonal_mixed_leg import *
from functools import lru_cache


def _unit(c):
    num,den=s.fraction(s.factor(c))
    return (len(s.Poly(num,FB,FC,FD).terms())==1 and
            len(s.Poly(den,FB,FC,FD).terms())==1)


def _coefficient_rows(forms,unknown):
    rows=[]
    for e in forms:
        rows.append({j:s.factor(s.diff(e,t)) for j,t in enumerate(unknown) if s.diff(e,t)!=0})
    return rows


def _eliminate(rows,rhs=None):
    """Checked triangular coefficient substitution; never calls rank()."""
    pivots=[]
    for i,original in enumerate(rows):
        row=dict(original);right=(rhs[i] if rhs is not None else 0)
        for p,pv,pr,_ in pivots:
            if p in row:
                fac=row[p]
                right=s.cancel(right-fac*pr)
                for j,c in pv.items():
                    nv=s.cancel(row.get(j,0)-fac*c)
                    if nv:row[j]=nv
                    elif j in row:del row[j]
        if not row:
            assert s.expand(right)==0
            continue
        choices=[j for j,c in row.items() if _unit(c)]
        assert choices,('a nonunit denominator would be required',row)
        p=min(choices);pivot=row[p]
        row={j:s.cancel(c/pivot) for j,c in row.items()}
        pivots.append((p,row,s.cancel(right/pivot),pivot))
    return pivots


def _backsolve(pivots,n,freevals=None):
    out=[s.Integer(0)]*n
    for j,value in (freevals or {}).items():out[j]=value
    for p,row,right,_ in reversed(pivots):
        out[p]=s.cancel(right-sum(c*out[j] for j,c in row.items() if j!=p))
    return s.Matrix(out)


@lru_cache(None)
def build_module():
    unknown=s.symbols('orthogonal_coefficient0:36');rhs=s.symbols('orthogonal_rhs0:18')
    B6=spin.row_join(Cinc);V=(x,y,z)
    def blocks(vector):
        return [B6*s.Matrix([sum(vector[18*r+3*j+k]*V[k] for k in range(3)) for j in range(6)]) for r in range(2)]
    def equations(vector):
        yy=mixed(*blocks(vector));out=[]
        for sp in mon(2):
            val=scalar_pairing(yy,C_column(sp)[0])
            out.extend([s.Poly(val,x,y,z).coeff_monomial(mm) for mm in (x*x,x*y,x*z,y*y,y*z,z*z)])
        return s.Matrix(out)
    eqs=equations(unknown);rows=_coefficient_rows(eqs,unknown)
    pivots=_eliminate(rows,list(rhs))
    assert len(pivots)==18 # each independent RHS was solved, not guessed
    right_inverse_value=_backsolve(pivots,36)
    assert (equations(right_inverse_value)-s.Matrix(rhs)).applyfunc(s.expand)==s.zeros(18,1)
    homogeneous=[(p,row,0,unit) for p,row,_,unit in pivots]
    free=[j for j in range(36) if j not in [p for p,_,_,_ in pivots]]
    kernel=[_backsolve(homogeneous,36,{j:1}) for j in free]
    for kk in kernel:assert equations(kk)==s.zeros(18,1)
    # Literal reconstruction holds for every free coefficient vector.
    free_symbols=s.symbols('orthogonal_free0:18')
    arbitrary=_backsolve(homogeneous,36,dict(zip(free,free_symbols)))
    assert (arbitrary-s.Matrix.hstack(*kernel)*s.Matrix(free_symbols)).applyfunc(s.expand)==s.zeros(36,1)

    def coefficient_vector(physical_blocks):
        entries=[]
        for block in physical_blocks:
            balanced=(B6.inv()*block).applyfunc(s.expand)
            entries.extend([s.diff(balanced[j],V[k]) for j in range(6) for k in range(3)])
        return s.Matrix(entries)
    known=[]
    for col in range(3):
        _,cs=C_column(mon(2)[col])
        for vi in V:known.append(coefficient_vector([vi*b for b in cs]))
    for r in range(2):
        for a in range(2):
            known.append(coefficient_vector([s.kronecker_product(s.Matrix(V),s.eye(2)[:,a]) if t==r else s.zeros(6,1) for t in range(2)]))
    for kk in known:assert equations(kk)==s.zeros(18,1)
    # Work only in exact homogeneous free coordinates; no actual-instance
    # matrix is formed. Unit triangular identities give an explicit quotient.
    known_rows=[{i:s.factor(kk[j]) for i,j in enumerate(free) if kk[j]!=0} for kk in known]
    old_pivots=_eliminate(known_rows)
    assert len(old_pivots)==13
    new_coordinates=[i for i in range(18) if i not in [p for p,_,_,_ in old_pivots]]
    new_raw=[kernel[i] for i in new_coordinates]
    D,Mu,C,Zeta=cartan_pair_split()
    normalized=[];removed=[];partners=[];pairing_B=[];pairing_C=[]
    for kk in new_raw:
        raw=blocks(kk)
        cc=s.Matrix.vstack(*(Pstd.inv()*extract*b for b in raw))
        zz=(Zeta*cc).applyfunc(s.factor);removed.append(zz)
        projected=cc-C*zz
        yy=[spin*(cliff*raw[r])+Cinc*projected[4*r:4*r+4,:] for r in range(2)]
        yy=[b.applyfunc(s.factor) for b in yy];normalized.append(yy)
        yf=mixed(*yy)
        assert all(not pair(yf,C_column(sp)[0]) for sp in mon(2))
        rr=s.Matrix([[scalar_pairing(yf,B(s.eye(2)[:,j])) for j in range(2)]])
        gg=s.Matrix.vstack(*[J*rr.diff(vi).T for vi in V]).applyfunc(s.factor)
        zf=vww_leg(gg)
        for j in range(2):assert s.expand(scalar_pairing(zf,A(s.eye(2)[:,j]))-rr[j])==0
        assert all(not pair(zf,B(s.eye(2)[:,j])) for j in range(2))
        partners.append(gg);pairing_B.append(rr)
        pairing_C.append(s.Matrix([[scalar_pairing(zf,C_column(sp)[0]) for sp in mon(2)]]))
    return dict(unknown=unknown,rhs=rhs,pivots=pivots,free=free,kernel=kernel,
                right_inverse=right_inverse_value,blocks=blocks,equations=equations,
                old_pivots=old_pivots,new_coordinates=new_coordinates,new_raw=new_raw,
                normalized=normalized,removed=removed,partners=partners,
                pairing_B=pairing_B,pairing_C=pairing_C)


def quartic_adapted_legs():
    """Five representatives labelled by S^4,S^3T,S^2T^2,ST^3,T^4.

    The quotient labelling is equivariant; this chosen polynomial splitting
    is not asserted canonical. Each r_C is the full transvectant (H,z)_2.
    """
    m=build_module()
    labels=[(1,-18*FC/FD**2),(3,-18/FD),(2,2/FC),(0,-6/FB),(4,-12*FD/(FB*FC))]
    return [dict(Y=[(mult*b).applyfunc(s.factor) for b in m['normalized'][i]],
                 Z=(mult*m['partners'][i]).applyfunc(s.factor),
                 C=(mult*m['pairing_C'][i]).applyfunc(s.factor)) for i,mult in labels]


def completed_family_interface(coefficient):
    """Exact raw C3/C5 coefficient interface; no solve or specialization.

    coefficient is an arbitrary symmetric 5-by-5 positive-linear matrix.
    For T=sum K_ij L_i L_j*, raw C3=-kappa mixed(Yblocks K RC),
    raw C5=kappa^2 p(GZ K RC). Actual C residuals multiply cm.
    """
    assert coefficient.shape==(5,5)
    assert (coefficient-coefficient.T).applyfunc(s.expand)==s.zeros(5)
    legs=quartic_adapted_legs()
    Ys=[s.Matrix.hstack(*(leg['Y'][r] for leg in legs)) for r in range(2)]
    GZ=s.Matrix.hstack(*(leg['Z'] for leg in legs))
    RC=s.Matrix.vstack(*(leg['C'] for leg in legs))
    transport=coefficient*RC
    G=GZ*transport
    return dict(Y=[yy*transport for yy in Ys],G=G,RC=RC,
                C5_cartan=extract*low*G,C5_source=cliff*low*G/3,
                coefficient=coefficient,leg_Y=Ys,leg_Z=GZ)
