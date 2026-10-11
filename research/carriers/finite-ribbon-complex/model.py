#!/usr/bin/env python3
"""Global split complex for the Hamiltonian ribbon rank-two bundle.

All matrices are exact SymPy matrices over Q[s,t,x0,x1,x2,x3,k0,...,k4].
Run this file to verify chain maps and two local strong deformation retracts.
This module constructs the model; audit_atiyah.py evaluates the mixed Atiyah detector.
"""
import sympy as S

s,t,z,w = S.symbols('s t z w')
x0,x1,x2,x3 = x = S.symbols('x0 x1 x2 x3')
ks = S.symbols('k0:5')
X = S.Matrix([x0,x1]); Y = S.Matrix([x2,x3])


def expand(M):
    return M.applyfunc(S.expand)


def assert_zero(M, label=''):
    assert all(S.expand(e)==0 for e in M), label


def syzygy(n, base_s=s, base_t=t):
    """O(0)^(n-1) -> O(1)^n presenting O(n)."""
    M = S.zeros(n,n-1)
    for j in range(n-1):
        M[j,j] = base_t
        M[j+1,j] = -base_s
    return M


def shift(n, a, b):
    """n x (n-1), columns -b e_j + a e_(j+1)."""
    return syzygy(n, -a, -b)


def eval_row(n, bs=s, bt=t):
    return S.Matrix([[bs**(n-1-j)*bt**j for j in range(n)]])


def coeff_matrix(D, variable, n):
    return D.applyfunc(lambda q: S.expand(q).coeff(variable,n))


def nonnegative_z(D):
    def take(q):
        return S.Add(*[v for v in S.Add.make_args(S.expand(q))
                      if v.as_powers_dict().get(z,0)>=0])
    return D.applyfunc(take)


def build(k=0):
    """Return the G complex; its twist by O(-3,0) represents F.

    k is any polynomial in z of degree <=4. Use sum(ks[i]*z**i for i
    in range(5)) for the full formal five-parameter family.
    """
    a=z*X-Y
    hs=-X.applyfunc(lambda a:a**3)
    ht=-Y.applyfunc(lambda a:a**3)
    j=S.Matrix([-a[1],a[0]])
    D0=-z**2*S.diag(z*z*x0*x0+z*x0*x2+x2*x2,
                    z*z*x1*x1+z*x1*x3+x3*x3)
    Dk=expand(k*j*j.T)
    D=expand(D0+Dk)
    MQ=S.diag(syzygy(5),syzygy(5))
    MA=syzygy(4)
    T=S.Matrix.vstack(shift(5,x0,x2),shift(5,x1,x3))
    U=S.Matrix([[0,0,0,-x2**3],[0,0,0,-x3**3]])
    alpha=S.Matrix.vstack(T,U)
    H=S.Matrix.vstack(shift(4,x0,x2),shift(4,x1,x3))
    rho=S.zeros(2,8)
    for b in range(2):
        for q in range(4):
            rho[:,4*b+q]=s*coeff_matrix(D,z,4-q)[:,b]
    delta=S.Matrix.vstack(MQ,rho)
    b0=[]
    for a0,a1 in [(x0,x2),(x1,x3)]:
        b0 += [s*a0**3,s*a0*a0*a1,s*a0*a1*a1,s*a1**3,t*a1**3]
    betaQ=S.Matrix([b0])
    for b in range(2):
        for q in range(5):
            betaQ[0,5*b+q] -= s*(Y.T*coeff_matrix(Dk,z,5-q))[b]
    beta=S.Matrix.hstack(betaQ,(t*X-s*Y).T)
    d={-2:S.Matrix.vstack(MA,-H),
       -1:S.Matrix.hstack(alpha,delta),
        0:beta}
    terms_G={-2:[(0,-2)]*3,
             -1:[(1,-2)]*4+[(0,-1)]*8,
              0:[(1,-1)]*10+[(1,1)]*2,
              1:[(2,2)]}
    terms_F={i:[(p-3,q) for p,q in bds] for i,bds in terms_G.items()}
    return dict(d=d,terms_G=terms_G,terms_F=terms_F,D=D,Dk=Dk,
                alpha=alpha,delta=delta,beta=beta,H=H,MA=MA,MQ=MQ,
                a=a,hs=hs,ht=ht)


def kernel_inverse(n,chart):
    """Left inverse of syzygy on its image, polynomial on each chart."""
    K=S.zeros(n-1,n)
    if chart=='s':
        for j in range(n-1):
            for r in range(j+1,n): K[j,r]=-z**(r-j-1)
    elif chart=='t':
        for j in range(n-1):
            for r in range(j+1): K[j,r]=w**(j-r)
    else: raise ValueError(chart)
    return K


def local_model(data,chart):
    """Return local original monad, comparison q, inverse i, homotopy H.

    q i = identity, identity - i q = d H + H d.
    Every entry is polynomial in z (s chart) or w (t chart).
    """
    if chart=='s':
        sub={s:1,t:z}
        va=eval_row(4,1,z); vq=eval_row(5,1,z)
        a=data['a']; h=data['hs']
        rA=S.eye(4)[:,0]; rQ=S.eye(5)[:,0]
        Rs=[nonnegative_z(data['D']*z**(j-5)) for j in range(5)]
        R=S.Matrix.hstack(*[Rs[j][:,b] for b in range(2) for j in range(5)])
    elif chart=='t':
        sub={s:w,t:1}
        va=eval_row(4,w,1); vq=eval_row(5,w,1)
        a=X-w*Y; h=data['ht']
        rA=S.eye(4)[:,3]; rQ=S.eye(5)[:,4]
        Rt=[]
        for j in range(5):
            f=expand(data['D']*z**(j-5))
            Rt.append(expand((nonnegative_z(f)-f).subs(z,1/w)))
        R=S.Matrix.hstack(*[Rt[j][:,b] for b in range(2) for j in range(5)])
    else: raise ValueError(chart)
    d={n:expand(M.subs(sub)) for n,M in data['d'].items()}
    VQ=S.diag(vq,vq); RQ=S.diag(rQ,rQ)
    monad={-1:S.Matrix.vstack(a,h),0:S.Matrix.hstack(-h.T,a.T)}
    phi=S.Matrix.vstack(S.Matrix.hstack(VQ,S.zeros(2)),
                        S.Matrix.hstack(R,S.eye(2)))
    q={-2:S.zeros(0,3),-1:S.Matrix.hstack(va,S.zeros(1,8)),
       0:phi,1:S.eye(1)}
    sigma0=S.Matrix.vstack(S.Matrix.hstack(RQ,S.zeros(10,2)),
                           S.Matrix.hstack(-R*RQ,S.eye(2)))
    KA=kernel_inverse(4,chart)
    KQ=S.diag(kernel_inverse(5,chart),kernel_inverse(5,chart))
    T=data['alpha'][:10,:]
    kappa=expand(KQ*(T*rA-RQ*a))
    i={-2:S.zeros(3,0),-1:S.Matrix.vstack(rA,-kappa),0:sigma0,1:S.eye(1)}
    homotopy={-1:S.Matrix.hstack(KA*(S.eye(4)-rA*va),S.zeros(3,8)),
               0:S.Matrix.vstack(S.zeros(4,12),
                   S.Matrix.hstack(KQ*(S.eye(10)-RQ*VQ),S.zeros(8,2))),
               1:S.zeros(12,1)}
    return dict(d=d,monad=monad,q=q,i=i,H=homotopy,R=R,phi=phi,
                VQ=VQ,VA=va,KQ=KQ,KA=KA)


def verify_degrees(data):
    for n,D in data['d'].items():
        for r in range(D.rows):
            for c in range(D.cols):
                if D[r,c]==0: continue
                dst=data['terms_G'][n+1][r]
                src=data['terms_G'][n][c]
                target=(dst[0]-src[0],dst[1]-src[1])
                for powers,coeff in S.Poly(S.expand(D[r,c]),s,t,*x).terms():
                    assert (sum(powers[:2]),sum(powers[2:]))==target,(n,r,c,target)


def verify(data,verbose=True):
    d=data['d']
    assert_zero(d[-1]*d[-2],'d-1 d-2')
    assert_zero(d[0]*d[-1],'d0 d-1')
    verify_degrees(data)
    if verbose: print('PASS: global differentials compose to zero and have every required bidegree.')
    locals_={}
    for chart in ['s','t']:
        loc=local_model(data,chart); locals_[chart]=loc
        d=loc['d']; a=loc['monad']; q=loc['q']; i=loc['i']; H=loc['H']
        assert_zero(q[-1]*d[-2],'q chain at -2')
        assert_zero(q[0]*d[-1]-a[-1]*q[-1],'q chain at -1')
        assert_zero(q[1]*d[0]-a[0]*q[0],'q chain at 0')
        assert_zero(d[-1]*i[-1]-i[0]*a[-1],'i chain at -1')
        assert_zero(d[0]*i[0]-i[1]*a[0],'i chain at 0')
        for n in [-1,0,1]:
            assert_zero(q[n]*i[n]-S.eye(q[n].rows),'q i')
        assert_zero(H[-1]*d[-2]-S.eye(3),'contraction -2')
        assert_zero(d[-2]*H[-1]+H[0]*d[-1]-(S.eye(12)-i[-1]*q[-1]),'contraction -1')
        assert_zero(d[-1]*H[0]+H[1]*d[0]-(S.eye(12)-i[0]*q[0]),'contraction 0')
        assert_zero(d[0]*H[1]-(S.eye(1)-i[1]*q[1]),'contraction 1')
        assert_zero(q[-2]*H[-1],'q H -1')
        assert_zero(q[-1]*H[0],'q H 0')
        assert_zero(H[-1]*i[-1],'H i -1')
        assert_zero(H[0]*i[0],'H i 0')
        assert_zero(H[-1]*H[0],'H squared')
        if verbose: print(f'PASS: {chart}-chart comparison, inverse, and strong deformation retract.')
    # Global compatibility of comparison q. Line frames transform by z^p.
    data_s=locals_['s']; data_t=locals_['t']
    TB=S.Matrix.vstack(S.Matrix.hstack(z**5*S.eye(2),S.zeros(2)),
                       S.Matrix.hstack(data['D'],z*S.eye(2)))
    original_transition={-1:S.Matrix([[z**4]]),0:TB,1:S.Matrix([[z**2]])}
    for n in [-1,0,1]:
        TL=S.diag(*[z**p for p,q in data['terms_G'][n]])
        assert_zero(data_s['q'][n]*TL-original_transition[n]*data_t['q'][n].subs(w,1/z),
                    'global comparison transition')
    if verbose: print('PASS: comparison maps glue globally to the original ribbon monad.')
    return locals_


if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser(); p.add_argument('--all-parameters',action='store_true')
    args=p.parse_args()
    k=sum(ks[i]*z**i for i in range(5)) if args.all_parameters else 0
    model=build(k)
    verify(model)
    print('Ranks:',{n:len(tw) for n,tw in model['terms_F'].items()})
    print('F terms:',model['terms_F'])
    print('Run audit_atiyah.py for the exact mixed Atiyah nonvanishing certificate.')
