#!/usr/bin/env python3
"""Independent tuple-exponent rational arithmetic; never evaluates source DAGs."""
from fractions import Fraction
from itertools import product
from math import comb

SHAPE=(6,37,22)

def mul(a,b,shape=SHAPE):
    out={}
    for x,c in a.items():
        for y,d in b.items():
            k=tuple(i+j for i,j in zip(x,y))
            if all(i<bound for i,bound in zip(k,shape)):
                out[k]=out.get(k,0)+c*d
    return {k:c for k,c in out.items() if c}

def power(a,e,shape=SHAPE):
    assert type(e) is int and e>=0
    out={(0,)*len(shape):1}
    while e:
        if e&1: out=mul(out,a,shape)
        e//=2
        if e:a=mul(a,a,shape)
    return out

def kernels():
    shape=(6,22)
    # Invert G by finite geometric series in the nilpotent ideal (T,z).
    h={(0,1):1,(1,0):1,(1,1):3,(1,2):1,(2,1):1,(2,2):1}
    current={(0,0):1};inv=dict(current)
    for n in range(1,27):
        current=mul(current,h,shape)
        for k,c in current.items(): inv[k]=inv.get(k,0)+(-1)**n*c
    assert not mul(current,h,shape)
    inv={k:c for k,c in inv.items() if c}
    g={(0,0):1,**h}
    assert mul(g,inv,shape)=={(0,0):1}
    answer=power(inv,70,shape)
    assert mul(power(g,70,shape),answer,shape)=={(0,0):1}
    return [[answer.get((t,z),0) for z in range(22)] for t in range(6)]

def select(poly,m=(2,2,2,0),roles=(0,1,2,3)):
    assert sorted(roles)==list(range(4)) and len(m)==4 and all(x in (0,1,2) for x in m)
    i,j,k,l=roles;assert m[i]==2
    d,L,S=3+m[j],21-m[l],sum(m)
    assert 30+S<SHAPE[1]
    K=kernels();rows=[];total=Fraction(0)
    sign=(-1)**sum(roles[a]>roles[b] for a in range(4) for b in range(a+1,4))
    for r in range(d+1):
        for ell in range(L+1):
            ex=[0]*4
            ex[i],ex[j],ex[k],ex[l]=272,212-r,159-S+r-ell,48+ell
            assert sum(ex)==691-S
            c=Fraction(poly.get((r,30+S,ell),0));weight=K[d-r][L-ell]
            total+=weight*c
            rows.append({'sourceExponents':ex,'quotientSlot':[r,30+S,ell], 'kernelWeight':weight,'coefficient':[str(c.numerator),str(c.denominator)], 'weightedContribution':[str((c*weight).numerator),str((c*weight).denominator)]})
    return sign,total,rows
