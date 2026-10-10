#!/usr/bin/env python3
"""Exact Cech contraction and homological transfer for the split ribbon model.

Uses the standard coordinate covers of P1 and P3. Each Laurent monomial has
its finite simplex Cech complex, contracted by a vertex outside its negative
support. Only the finite monomials reached by the requested transfer occur.
"""
from collections import defaultdict
from functools import lru_cache
import itertools
import sympy as S
import model as M
import spectral_d1 as C


def clean(out):return {k:S.expand(v) for k,v in out.items() if v!=0}

def add(*cochains):
    out=defaultdict(lambda:0)
    for cochain in cochains:
        for k,v in cochain.items():out[k]+=v
    return clean(out)


def scale(c,x):return {k:c*v for k,v in x.items() if c*v!=0}

def negmask(exps):return sum(1<<i for i,a in enumerate(exps) if a<0)

def degree(mask):return mask.bit_count()-1


def incl_factor(exps):
    n=len(exps);neg=negmask(exps)
    if neg==0:return tuple(1<<i for i in range(n))
    if neg==(1<<n)-1:return ((1<<n)-1,)
    return ()


def proj_factor(exps,mask):
    n=len(exps);neg=negmask(exps)
    return (neg==0 and mask==1) or (neg==(1<<n)-1 and mask==neg)


def h_factor(exps,mask):
    n=len(exps);neg=negmask(exps)
    if neg==(1<<n)-1:return ()
    r=next(i for i in range(n) if not (neg>>i)&1)
    if not (mask>>r)&1:return ()
    J=mask^(1<<r)
    if not J:return ()
    sign=-1 if (mask&((1<<r)-1)).bit_count()%2 else 1
    return ((J,sign),)


def include(v,basis):
    out=defaultdict(lambda:0)
    for idx,value in enumerate(v):
        if not value:continue
        i,c,j,r,exps=basis[idx]
        for ma in incl_factor(exps[:2]):
            for mb in incl_factor(exps[2:]):out[(i,c,j,r,exps,ma,mb)]+=value
    return clean(out)


def project(cochain,basis):
    idx={v:i for i,v in enumerate(basis)};out=S.zeros(len(basis),1)
    for (i,c,j,r,exps,ma,mb),v in cochain.items():
        if proj_factor(exps[:2],ma) and proj_factor(exps[2:],mb):
            out[idx[i,c,j,r,exps]]+=v
    return out


def contract(cochain):
    out=defaultdict(lambda:0)
    for (i,c,j,r,e,ma,mb),v in cochain.items():
        for na,sgn in h_factor(e[:2],ma):out[i,c,j,r,e,na,mb]+=sgn*v
        if proj_factor(e[:2],ma):
            sgnbase=-1 if degree(ma)%2 else 1
            for na in incl_factor(e[:2]):
                for nb,sgn in h_factor(e[2:],mb):out[i,c,j,r,e,na,nb]+=sgnbase*sgn*v
    return clean(out)


def vertical(cochain):
    out=defaultdict(lambda:0)
    for (i,c,j,r,e,ma,mb),v in cochain.items():
        for a in range(2):
            if not ma>>a&1:
                na=ma|(1<<a);sgn=-1 if (ma&((1<<a)-1)).bit_count()%2 else 1
                out[i,c,j,r,e,na,mb]+=sgn*v
        for b in range(4):
            if not mb>>b&1:
                nb=mb|(1<<b); parity=degree(ma)+(mb&((1<<b)-1)).bit_count()
                out[i,c,j,r,e,ma,nb]+=(-1 if parity%2 else 1)*v
    return clean(out)


def horizontal(data,cochain,ds=None):
    """Total-complex perturbation (-1)^q d_Hom."""
    if ds is None:ds=C.polynomial_terms(data)
    out=defaultdict(lambda:0)
    for (i,c,j,r,exps,ma,mb),v in cochain.items():
        p=j-i;q=degree(ma)+degree(mb);sgn=(-1 if q%2 else 1)
        if j in ds:
            for (nr,nc),terms in ds[j].items():
                if nc!=r:continue
                for powers,coeff in terms:
                    e=tuple(a+b for a,b in zip(exps,powers))
                    out[i,c,j+1,nr,e,ma,mb]+=sgn*v*coeff
        if i-1 in ds:
            for (nr,nc),terms in ds[i-1].items():
                if nr!=c:continue
                for powers,coeff in terms:
                    e=tuple(a+b for a,b in zip(exps,powers))
                    out[i-1,nc,j,r,e,ma,mb]+=sgn*(-1 if p%2==0 else 1)*v*coeff
    return clean(out)


def transfer_column(data,p,q,twist,v,length,verbose=False,check_zigzag=True):
    """Coefficient p b (-h b)^(length-1) i(v), with exact Cech checks."""
    B=C.basis(data,p,q,twist);out_basis=C.basis(data,p+length,q-length+1,twist)
    y=include(v,B);ds=C.polynomial_terms(data)
    if check_zigzag: assert not vertical(y), 'Initial representative must be Cech closed.'
    for step in range(length):
        y=horizontal(data,y,ds)
        if verbose:print('horizontal',step+1,'terms',len(y),flush=True)
        if step<length-1:
            next_y=scale(-1,contract(y))
            if check_zigzag:
                assert not add(vertical(next_y),y), 'Nonzero intermediate cohomology: this simple zigzag needs a correction.'
            y=next_y
            if verbose:print('contract','terms',len(y),flush=True)
    if check_zigzag: assert not vertical(y), 'Final representative must be Cech closed.'
    return project(y,out_basis),y


def verify_contraction():
    samples=[tuple(-1 if mask>>i&1 else 0 for i in range(2)) for mask in range(4)]
    bsamples=[tuple(-1 if mask>>i&1 else 0 for i in range(4)) for mask in range(16)]
    count=0
    for ea,eb in itertools.product(samples,bsamples):
        e=ea+eb;na=negmask(ea);nb=negmask(eb)
        for ma in range(1,4):
            if ma&na!=na:continue
            for mb in range(1,16):
                if mb&nb!=nb:continue
                basis_elem=(0,0,0,0,e,ma,mb);v={basis_elem:S.Integer(1)}
                ip={}
                if proj_factor(ea,ma) and proj_factor(eb,mb):
                    ip={(0,0,0,0,e,a,b):S.Integer(1) for a in incl_factor(ea) for b in incl_factor(eb)}
                assert not add(vertical(contract(v)),contract(vertical(v)),scale(-1,v),ip),basis_elem
                assert not contract(contract(v)),basis_elem
                assert not vertical(vertical(v)),basis_elem
                assert not contract(ip),basis_elem
                ph=sum(value for (*_,ee,aa,bb),value in contract(v).items()
                       if proj_factor(ee[:2],aa) and proj_factor(ee[2:],bb))
                assert ph==0,basis_elem
                count+=1
    return count


if __name__=='__main__':
    print('PASS: Cech contraction identities on',verify_contraction(),'monomial Cech basis vectors covering all negative supports.')
