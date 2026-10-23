#!/usr/bin/env python3
"""Fixed-minor response interface. Synthetic diagnostics only, never HM data."""
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sympy as S

CHECKS = 0
NEGATIVES = 0

def equal(A, B):
    return A.shape == B.shape and all(S.cancel(a-b) == 0 for a,b in zip(A,B))

def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise RuntimeError(message)

def indices(values, bound, name):
    values = tuple(values)
    if any(type(x) is not int or x < 0 or x >= bound for x in values):
        raise ValueError(name + ' contains invalid index')
    if len(set(values)) != len(values):
        raise ValueError(name + ' contains duplicate indices')
    return values

def certificate(D, L, I, J):
    """Over a field; symbolic nonconstant pivots mean localization, not global use."""
    D, L = S.Matrix(D), S.Matrix(L)
    if L.cols != D.cols:
        raise ValueError('extraction has wrong primitive domain')
    I, J = indices(I, D.rows, 'I'), indices(J, D.cols, 'J')
    if len(I) != len(J):
        raise ValueError('pivot is not square')
    r = len(I)
    if r:
        B = D.extract(I,J)
        delta = S.expand(B.det())
        if delta == 0:
            raise ValueError('singular pivot')
        adj = B.adjugate()
        N = S.zeros(D.cols,D.rows)
        for j0,j in enumerate(J):
            for i0,i in enumerate(I):
                N[j,i] = adj[j0,i0]
    else:
        delta, N = S.Integer(1), S.zeros(D.cols,D.rows)
    if not equal(delta*D, D*N*D):
        raise ValueError('rank residual failed')
    if not equal(delta*L, L*N*D):
        raise ValueError('descent residual failed')
    return delta,N

def response(D,L,I,J,s):
    D,L,s = S.Matrix(D),S.Matrix(L),S.Matrix(s)
    delta,N = certificate(D,L,I,J)
    if s.rows != D.rows:
        raise ValueError('source has wrong domain')
    if not equal(delta*s,D*N*s):
        raise ValueError('source is outside exact image')
    return (L*N*s/delta).applyfunc(S.cancel)

def reject(call, message):
    global NEGATIVES
    try:
        call()
    except ValueError:
        NEGATIVES += 1
    else:
        raise RuntimeError('negative control accepted: '+message)

def main():
    root=Path(__file__).parent
    for name,digest in [
        ('cone908.md','aafd5ee2b8a0a1d0876886b4db361c05d2a34cc41ab59e44ecec54580061cfcc'),
        ('matching914.md','d5805f030eab27138adc250b98700749419e246cc7b1f5652a4c73647861a29e')]:
        require(hashlib.sha256((root/'inputs'/name).read_bytes()).hexdigest()==digest,'input pin '+name)

    # Polynomial rank-two universal block family. No actual HM coefficient.
    b00,b01,b10,b11,x0,x1,y0,y1,w0,w1,z = S.symbols('b00 b01 b10 b11 x0 x1 y0 y1 w0 w1 z')
    B=S.Matrix([[b00,b01],[b10,b11]])
    X=S.Matrix([x0,x1]); Y=S.Matrix([[y0,y1]])
    D=B.row_join(B*X).col_join((Y*B).row_join(Y*B*X))
    L=S.Matrix([[w0,w1]])*B.row_join(B*X)
    delta,N=certificate(D,L,(0,1),(0,1))
    require(equal(delta*D,D*N*D),'universal rank residual')
    require(equal(delta*L,L*N*D),'universal descent residual')
    require(equal(D*N*D,delta*D),'universal generalized inverse')
    require(equal((D*N)*(D*N),delta*D*N),'universal projector numerator')
    aa,hh=S.symbols('a h')
    u=S.Matrix([aa**3*hh,aa**2*hh,hh])
    source=D*u
    require(equal(response(D,L,(0,1),(0,1),source),L*u),'universal source response')
    require(equal((delta*S.eye(3)-D*N).extract((0,1),(0,1,2)),S.zeros(2,3)),'pivot residual rows zero')

    # Fixed rank-two D, chart-function extraction, entire homogeneous cubic-a/linear-h source.
    D=S.Matrix([[1,2,3,0],[0,1,1,1],[1,3,4,1]])
    L=S.Matrix([[1,z,2],[z*z,-1,0]])*D
    a0,a1,a2=S.symbols('a0 a1 a2')
    u=S.Matrix([a0**3*hh,a0**2*a1*hh,a0*a1*a2*hh,a2**3*hh])
    require(all(S.Poly(v,a0,a1,a2).homogeneous_order()==3 for v in u),'genuine homogeneous cubic-a family')
    s=D*u
    rows=[]
    for I in combinations(range(3),2):
        for J in combinations(range(4),2):
            if D.extract(I,J).det()==0:
                continue
            d,N=certificate(D,L,I,J)
            require(equal(response(D,L,I,J,s),L*u),'fixed full-family response')
            require(equal(D*N*D,d*D),'fixed rank identity')
            require(equal(L*N*D,d*L),'fixed descent identity')
            require(equal(D*N*s,d*s),'fixed membership identity')
            require(equal(D*N*D*N,d*D*N),'fixed projection identity')
            require(equal((d*S.eye(3)-D*N).extract(I,range(3)),S.zeros(2,3)),'fixed pivot residual zero')
            rows.append(L*N/d)
    for R in rows:
        require(equal((R-rows[0])*D,S.zeros(2,4)),'pivot difference kills image')
    require(all(not x.has(aa,hh,a0,a1,a2) for R in rows for x in R),'no source parameter denominator')

    # Nonphysical descent passes: authentication cannot be inferred from M1/M2.
    require(equal(response(D,S.zeros(1,4),(0,1),(0,1),s),S.zeros(1,1)), 'zero row passes algebra only')

    # Two extensions disagree off the exact image although certified on image.
    E=S.ones(2,2); H=S.Matrix([[1,1]]); outside=S.Matrix([1,0])
    d0,N0=certificate(E,H,(0,),(0,)); d1,N1=certificate(E,H,(1,),(0,))
    require(not equal(H*N0/d0,H*N1/d1),'whole row equality must not be inferred')
    require(equal((H*N0/d0-H*N1/d1)*E,S.zeros(1,2)),'extension agreement on exact image')
    require(not equal(H*N0*outside/d0,H*N1*outside/d1),'off-image value is pivot-dependent')
    reject(lambda:response(E,H,(0,),(0,),outside),'off-image source')

    # Zero rank is a separate valid branch.
    Z=S.zeros(2,3); ZL=S.zeros(1,3)
    require(equal(response(Z,ZL,(),(),S.zeros(2,1)),S.zeros(1,1)),'rank-zero response')
    reject(lambda:certificate(E,H,(),()),'zero pivot for nonzero differential')
    reject(lambda:certificate(Z,S.ones(1,3),(),()),'zero differential nonzero extraction')
    reject(lambda:response(Z,ZL,(),(),S.ones(2,1)),'zero differential nonzero source')

    reject(lambda:certificate(D,L,(0,0),(0,1)),'duplicate row indices')
    reject(lambda:certificate(D,L,(0,1),(1,1)),'duplicate column indices')
    reject(lambda:certificate(D,L,(0,3),(0,1)),'out-of-range row')
    reject(lambda:certificate(D,L,(0,1),(0,-1)),'negative column index')
    reject(lambda:certificate(D,L,(0,True),(0,1)),'boolean index')
    reject(lambda:certificate(D,L,(0,),(0,1)),'nonsquare pivot')
    reject(lambda:certificate(E,H,(0,1),(0,1)),'singular pivot')
    reject(lambda:certificate(S.eye(2),H,(0,),(0,)),'nonmaximal minor')
    reject(lambda:certificate(E,S.Matrix([[1,0]]),(0,),(0,)),'extraction fails kernel descent')
    reject(lambda:certificate(E,S.ones(1,3),(0,),(0,)),'wrong extraction dimension')
    reject(lambda:response(E,H,(0,),(0,),S.zeros(3,1)),'wrong source dimension')

    # A selected-block-only check is insufficient: pivot identity passes,
    # while the full rank residual rejects the second independent column.
    F=S.eye(2)
    require(F[0,0]==1,'pivot block itself nonzero')
    reject(lambda:certificate(F,H,(0,),(0,)),'omitted nonpivot column')

    # Nonunit-ring warning: t e=1 is soluble in k(t), not k[t].
    t=S.symbols('t')
    V=S.Matrix([[t]]); VL=S.Matrix([[1]])
    d,N=certificate(V,VL,(0,),(0,))
    require(equal(d*S.ones(1,1),V*N*S.ones(1,1)),'localized membership identity')
    q=response(V,VL,(0,),(0,),S.ones(1,1))[0]
    require(S.cancel(q)==1/t and S.denom(q)==t,'localized response has genuine denominator')
    reject(lambda:certificate(V.subs(t,0),VL,(0,),(0,)),'rank-changing specialization')

    print(json.dumps({'status':'PASS','checks':CHECKS,'negative_controls':NEGATIVES,
        'scope':'synthetic and universal polynomial interfaces only; no actual HM instance'},sort_keys=True))

if __name__=='__main__':
    main()
