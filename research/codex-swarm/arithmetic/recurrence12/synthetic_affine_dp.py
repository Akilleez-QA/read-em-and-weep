"""Synthetic integer/support control only. No import path from physical plans.
Sparse affine-index convolution with a bounded total-degree index. Integer
weights represent toy multiplicities, never coefficients of the physical source.
"""
from math import comb


def bounded_affine_convolution(*, synthetic, total, bounds, affine_columns,
                               offsets, kernels):
    """D[i+1,r+n,alpha+c_i*n+offset_i+beta] +=
       D[i,r,alpha] * binom(total-r,n) * kernels[i][n][beta].
    All per-slot n values are explicit synthetic data. Affine output indices may
    be signed; n is always nonnegative. None of the physical DAGs is accepted.
    """
    if synthetic is not True:raise ValueError('synthetic control only')
    if type(total) is not int or not 0<=total<=8:raise ValueError('synthetic total bound')
    d=len(bounds)
    if not 1<=d<=4 or not len(affine_columns)==len(offsets)==len(kernels)==d:raise ValueError('slot count')
    width=len(affine_columns[0])
    if not 1<=width<=4:raise ValueError('synthetic index width')
    def vector(a):
        if type(a) is not tuple or len(a)!=width or any(type(v) is not int or abs(v)>32 for v in a):raise ValueError('bounded integer vector')
    for i,(lo,hi) in enumerate(bounds):
        if any(type(v) is not int for v in (lo,hi)) or not 0<=lo<=hi<=total:raise ValueError('synthetic n range')
        vector(affine_columns[i]);vector(offsets[i])
        if type(kernels[i]) is not dict or set(kernels[i])!=set(range(lo,hi+1)):raise ValueError('complete toy kernels required')
        for support in kernels[i].values():
            if type(support) is not dict or len(support)>16:raise ValueError('tiny explicit support required')
            for beta,c in support.items():
                vector(beta)
                if type(c) is not int or abs(c)>64:raise ValueError('toy integer multiplicity')
    states={(0,(0,)*width):1}
    for i,(lo,hi) in enumerate(bounds):
        nxt={}
        for (r,alpha),coefficient in states.items():
            for n in range(lo,min(hi,total-r)+1):
                for beta,c in kernels[i][n].items():
                    target=tuple(a+b+n*v+off for a,b,v,off in zip(alpha,beta,affine_columns[i],offsets[i]))
                    key=(r+n,target)
                    nxt[key]=nxt.get(key,0)+coefficient*comb(total-r,n)*c
        states={k:v for k,v in nxt.items() if v}
    return {alpha:c for (r,alpha),c in states.items() if r==total}
