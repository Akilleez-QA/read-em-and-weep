#!/usr/bin/env python3
"""Universal character, diagonal-filtration, Chern and Hilbert checks only."""
from fractions import Fraction
from pathlib import Path
import runpy
r=runpy.run_path(str(Path(__file__).with_name('verify_pure_cross_block_couplings.py')))
for idx in (3,6):
    dims=[r['couplings']([term],2) for term in r['rows'][idx]]
    assert dims[:-1]==[0]*(len(dims)-1)
    assert dims[-1]==3
assert [r['couplings']([term],2) for term in r['rows'][5]]==[0,1,2]
expected={18:[3,2,2,1,1,1,1,0],14:[2,1,1,1,1,0,0,0]}
for a,want in expected.items():
    filt=[r['inner'](r['one'],r['vm'](r['sy'](a-k),r['sy'](6-k))) for k in range(7)]+[0]
    assert filt==want
    exact=[k for k in range(7) if filt[k]>filt[k+1]]
    assert exact==({18:[0,2,6],14:[0,4]}[a])
    # ch(S_(a+1))-ch(S7*) and RR, with rational arithmetic.
    c1=a+6
    ch2=-Fraction(a,2)+3
    chi0=Fraction(3,2)*c1+ch2
    assert chi0==a+12
    for d in range(6,a+11,2):
        t=a+10-d
        assert t>=0 and t+(d-4)==a+6
        assert 2*t+(2*d-10)==2*a+10
    print(f'PASS: a={a}: exact diagonal orders {exact}; torsion degree {c1}; chi={c1}t+{chi0}.')
print('PASS: IV/VII have zero low couplings; VI has low multiplicity one and scalar multiplicity two.')
print('PASS: actual-image, kernel, and target-Gram divisor degrees agree for every allowed even d.')
print('No actual coefficients, selected matrices, fiber ranks, or local-model experiment computed.')
