#!/usr/bin/env python3
"""Exact abstract vector-space interface certificate, NOT HM coefficients.

Constructs tau:Q^6->P plus R, Psi:P plus R->T, dim(P,R,T)=(20,10,2).
Checks all raw rank pairs (rank projection_P tau, rank Psi|R) in 0..6 x 0..2.
The genuine generic HM generation theorem forces the second rank to be 2;
its seven surviving models still realize every first rank at interface level.
No model is asserted to arise from an HM module, Hilbert--Burch curve, or bundle.
Uses only Python standard library and rational Gaussian elimination.
"""
from fractions import Fraction as Q


def zeros(m,n): return [[Q(0) for _ in range(n)] for _ in range(m)]
def rank(a):
    a=[list(map(Q,row)) for row in a]
    if not a: return 0
    m,n=len(a),len(a[0]); k=0
    for j in range(n):
        p=next((i for i in range(k,m) if a[i][j]),None)
        if p is None: continue
        a[k],a[p]=a[p],a[k]
        z=a[k][j]; a[k]=[x/z for x in a[k]]
        for i in range(m):
            if i!=k and a[i][j]:
                z=a[i][j]; a[i]=[x-z*y for x,y in zip(a[i],a[k])]
        k+=1
        if k==m: break
    return k

def product(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def concat(a,b): return [x+y for x,y in zip(a,b)]

for s in range(7):
    for r in range(3):
        tau=zeros(30,6); psi=zeros(2,30)
        # s visible directions and 6-s directions invisible under projection to P.
        for j in range(s): tau[j][j]=1
        for j in range(s,6): tau[20+r+j-s][j]=1
        # R gives r output directions. P provides the 2-r missing directions.
        for j in range(r): psi[j][20+j]=1
        for j in range(2-r): psi[r+j][s+j]=1
        mu=tau[:20]; ell=[row[20:] for row in psi]
        assert rank(tau)==6 and rank(psi)==2
        assert rank(mu)==s and rank(ell)==r
        assert all(x==0 for row in product(psi,tau) for x in row)
        assert 30-rank(tau)==24
        assert 30-rank(psi)-rank(tau)==22
        incR=zeros(30,10)
        for j in range(10): incR[20+j][j]=1
        rank_R_to_cokertau=rank(concat(tau,incR))-rank(tau)
        assert 10-rank_R_to_cokertau==6-s
        assert 24-rank_R_to_cokertau==20-s
        if r==2:
            # ker ell has eight coordinate basis vectors in R. Its image in
            # ker Psi / im tau is the hyperplane-extendable part of W.
            incKerEll=zeros(30,8)
            for j in range(8): incKerEll[22+j][j]=1
            image_dim=rank(concat(tau,incKerEll))-rank(tau)
            assert image_dim==2+s==8-(6-s)
            assert 22-image_dim==20-s==14+(6-s)
        print(f'PASS rank(mu)={s}, rank(ell)={r}; tau=6, Psi=2, W=22')
print('PASS: all 21 raw interfaces; all 7 interfaces with generic HM rank(ell)=2.')
print('LIMIT: interface freedom only; no geometric or graded-module realizability claim.')
