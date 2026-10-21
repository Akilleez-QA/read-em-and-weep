#!/usr/bin/env python3
"""Universal invariant degrees, root syzygy degrees and Chern checks only."""
from pathlib import Path
import runpy
r=runpy.run_path(str(Path(__file__).with_name('verify_pure_cross_block_couplings.py')))
assert [n for n in range(25) if r['inner'](r['one'],r['sy'](n))]==[0,12,20,24]
assert r['inner'](r['one'],r['vm'](r['sy'](4),r['sy'](4)))==1
assert [r['inner'](r['one'],r['vm'](r['sy'](12-k),r['sy'](6-k))) for k in range(7)]==[1,1,1,1,0,0,0]
# (a,k,vertical degree,p,q,kernel c1,kernel c2,image-hull c1,image-hull c2)
cases=[(18,2,0,4,17,-26,181,16,154),
       (18,6,12,0,1,-6,15,-4,16),
       (14,4,0,2,11,-18,83,8,72),
       (12,3,0,3,10,-18,81,8,58)]
def chern_root_push(u,v):
    # Symmetry permits nonnegative n in S_n(v), except S_-5 uses root duality.
    if u<v:u,v=v,u
    n=u-v
    assert n>=1
    return n-1+2*v,n*(n-1)//2+v*(n-1)+v*v
for a,k,v,p,q,nc1,nc2,hc1,hc2 in cases:
    assert (p,q)==(6-k,a+1-k-v)
    assert chern_root_push(-5-p,1-q)==(nc1,nc2)
    assert chern_root_push(p-5,q+1)==(hc1,hc2)
    d=-nc1
    ilen=2*p*q
    ic1=d-10
    ic2=55+d*d-10*d-nc2
    assert ic1==hc1 and ic2-hc2==ilen
    defect=2*(k-1)+v
    assert a+10-d==defect
    assert q+k+v==a+1 and p+k-6==0
    assert nc2-d*d//4 in (12,6,2,0)
    assert 2*defect+(2*d-10)==2*a+10
    assert p+q+5==d and 2+2*(p+q-1)==2*d-10
    print(f'PASS: a={a}, k={k}: kernel (c1,c2)=({nc1},{nc2}); image singularity length={ilen}; target divisor degree={defect}.')
# The only invariant quadratic on P(Sym^2 W) is the discriminant.
# Sym^2(Sym^2 W)=Sym^4 W + 1; Sym^4 W has no invariants.
assert r['inner'](r['one'],r['sy'](4))==0
print('PASS: invariant exclusions, saturated root-syzygy degrees, exact Chern and norm accounting.')
print('No actual coefficients, selected matrices, fiber ranks, or local-model experiment computed.')
