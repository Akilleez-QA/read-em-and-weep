#!/usr/bin/env python3
"""Exact d1 on line-bundle cohomology of Hom(L_F,L_F)(twist).

Negative homogeneous monomials are Cech H^top representatives. This computes
only E1 -> E2. Higher differentials are not silently discarded.
"""
from functools import lru_cache
from collections import defaultdict
import sympy as S
import model as M

@lru_cache(None)
def compositions(total,n):
    if n==1:return ((total,),) if total>=0 else ()
    if total<0:return ()
    return tuple((r,)+p for r in range(total+1) for p in compositions(total-r,n-1))

@lru_cache(None)
def monomials(a,b,q):
    if a>=0:A=compositions(a,2); qa=0
    elif a<=-2:A=tuple(tuple(-v-1 for v in p) for p in compositions(-a-2,2));qa=1
    else:return ()
    if b>=0:B=compositions(b,4);qb=0
    elif b<=-4:B=tuple(tuple(-v-1 for v in p) for p in compositions(-b-4,4));qb=3
    else:return ()
    if qa+qb!=q:return ()
    return tuple(x+y for x in A for y in B)


def basis(data,p,q,twist):
    out=[]; terms=data['terms_F']
    for i,src in sorted(terms.items()):
        j=i+p
        if j not in terms:continue
        for c,(sa,sb) in enumerate(src):
            for r,(da,db) in enumerate(terms[j]):
                for exps in monomials(da-sa+twist[0],db-sb+twist[1],q):
                    out.append((i,c,j,r,exps))
    return out


def polynomial_terms(data):
    ds={}
    for p,D in data['d'].items():
        ent={}
        for r in range(D.rows):
            for c in range(D.cols):
                if D[r,c]!=0:
                    ent[r,c]=S.Poly(S.expand(D[r,c]),M.s,M.t,*M.x).terms()
        ds[p]=ent
    return ds


def differential(data,p,q,twist,ds=None):
    dom=basis(data,p,q,twist); cod=basis(data,p+1,q,twist)
    target={v:i for i,v in enumerate(cod)}
    if ds is None:ds=polynomial_terms(data)
    entries=defaultdict(lambda:0)
    for col,(i,c,j,r,exps) in enumerate(dom):
        if j in ds:
            for (nr,nc),terms in ds[j].items():
                if nc!=r:continue
                for powers,coeff in terms:
                    lab=(i,c,j+1,nr,tuple(a+b for a,b in zip(exps,powers)))
                    if lab in target:entries[target[lab],col]+=coeff
        if i-1 in ds:
            for (nr,nc),terms in ds[i-1].items():
                if nr!=c:continue
                for powers,coeff in terms:
                    lab=(i-1,nc,j,r,tuple(a+b for a,b in zip(exps,powers)))
                    if lab in target:entries[target[lab],col]+=(-1 if p % 2 == 0 else 1)*coeff
    return S.SparseMatrix(len(cod),len(dom),dict(entries))


def row(data,q,twist):
    ds=polynomial_terms(data)
    dims={p:len(basis(data,p,q,twist)) for p in range(-3,4)}
    mats={p:differential(data,p,q,twist,ds) for p in range(-3,3)}
    return dims,mats

if __name__=='__main__':
    import argparse
    pa=argparse.ArgumentParser();pa.add_argument('--q',type=int,default=4)
    pa.add_argument('--twist',type=int,nargs=2,default=[-2,-1]); args=pa.parse_args()
    data=M.build();dims,mats=row(data,args.q,tuple(args.twist))
    ranks={p:A.rank() for p,A in mats.items() if A.rows and A.cols}
    for p in range(-3,2):
        assert mats[p+1]*mats[p]==S.zeros(mats[p+1].rows,mats[p].cols)
    print('Twist',args.twist,'q',args.q)
    print('E1 dimensions:',dims)
    print('d1 exact rational ranks:',ranks)
    print('E2 dimensions:',{p:dim-ranks.get(p,0)-ranks.get(p-1,0) for p,dim in dims.items()})
    print('These are E2 dimensions only. Higher differentials must be checked.')
