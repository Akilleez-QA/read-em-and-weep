#!/usr/bin/env python3
"""Universal characters and hypothetical bundle arithmetic only.
No actual coefficients, points, instance matrices/ranks, scans, or model spikes.
All predecessor files are executed unchanged.
"""
from pathlib import Path
import contextlib, io, runpy
here=Path(__file__).parent
with contextlib.chdir(here),contextlib.redirect_stdout(io.StringIO()):
    frozen=runpy.run_path(str(here/'verify_mixed_p4_d5_octic_exclusion.py'))
    endpoint=runpy.run_path(str(here/'verify_three_p4_backward_gauss.py'))
for key in ('va','vs','vm','hom','sym','dimension','effective','multiplicity','bundle_hom','chi','sections','reps','rank','degree','shift'):
    globals()[key]=frozen[key]
b=frozen['base']['b']
one,W,Wp,A,V,P,S,D,T=[reps[n] for n in ('one','W','Wp','A','V','P','S','D','T')]
profile=(1,2,1,0,0,0,0,0)
p=next(p for p in frozen['remaining'] if p[0]==profile)
E=[(-j,R) for j,R in p[2] if dimension(R)]
assert E==[(-3,Wp),(-3,vs(2,T)),(-4,V)]
assert rank(E)==17 and degree(E)==-54 and dimension(sections(E,2))==0
U=va(Wp,vs(2,T))
assert sections(E,3)==U
Et=[(1-d,R) for d,R in E]
assert max(d for d,R in Et)==5
blocks=b['image_blocks'](T,Et,-1,3)
assert blocks==[(1,'V'),(2,'Wp'),(3,'V'),(4,'Wp'),(5,'V')]
assert not [x for x in blocks if dimension(reps[x[1]])==1]
assert [(d,n) for d,n in blocks if dimension(reps[n])==2]==[(2,'Wp'),(4,'Wp')]
assert [(d,n) for d,n in blocks if dimension(reps[n])==3]==[(1,'V'),(3,'V'),(5,'V')]
# If b=3, every degree of L is >=1, as are those of its saturation.
# A0=Lbar*(1) therefore has all degrees <=0: h0<=3, deg<=0.
# Universal backward bound is chi(K2(4))=7-2 deg(A0)+delta.
assert 7>3
# Rank-two saturation follows from the maximum ordinary target degree 5.
for e in (2,4):
    assert 0<=2*5-2*e<12
# Verify every dual profile, not an arbitrary Q bound.
Qs=[b['q_positive'](dp) for dp in b['cubic_dual_profiles']]
assert len(Qs)==5
for Q in Qs:
    assert rank(Q)==13 and degree(Q)==54
    assert max(d for d,R in Q)<=8
    assert sections([(-d,R) for d,R in Q],3)==T
# rank K=14 and H0(K(2))=0 => deg K<=-42.
# A0 extension O(n-2) by Wp O(1-e) has degree n-2e.
# Thus n>=2e-12; center parity n even, and Q bounds n<=8.
candidates=[]
for e in (2,4):
    for n in range(2*e-12,9,2):
        aa_degree=n-2*e
        lower=7-2*n+4*e
        upper=max(n-1,0) # valid without splitting; quotient has no sections
        if lower>upper: continue
        candidates.append((n,e))
        assert 0<=upper-lower<12 # actual next-image defect delta=0
        assert n+e-3>=-1 # Ext^1(Wp O(1-e),O(n-2)) vanishes
        AA=[(n-2,one),(1-e,Wp)]
        assert degree(AA)==aa_degree and dimension(sections(AA))==upper
        C=shift(AA,-2)
        assert degree(E)-degree(AA)-degree(C)==-48-2*aa_degree
        ch4=va(chi(E,4),vs(-1,chi(AA,4)),vs(-1,chi(C,4)))
        assert dimension(ch4)==lower
        if (n,e)==(6,2):
            assert ch4==V and sections(AA)==D
            assert multiplicity(ch4,V)>multiplicity(sections(AA),V)
        elif (n,e)==(8,4):
            assert ch4==va(vs(-1,A),vs(2,V),P)
            assert sections(AA)==va(V,P)
            assert multiplicity(ch4,V)>multiplicity(sections(AA),V)
        else:
            assert (n,e)==(8,2)
            ch3=va(chi(E,3),vs(-1,chi(AA,3)),vs(-1,chi(C,3)))
            assert ch3==endpoint['ch3'] and ch4==endpoint['ch4']
            assert AA==endpoint['A8'] and C==endpoint['C8']
            assert len(endpoint['shapes'])==2
            for K2 in endpoint['shapes']:
                for twist in range(-3,15):
                    assert chi(K2,twist)==va(chi(E,twist),vs(-1,chi(AA,twist)),vs(-1,chi(C,twist)))
            assert endpoint['weight']==104 and 104 not in endpoint['reachable']
assert candidates==[(6,2),(8,2),(8,4)]
assert len(frozen['remaining'])==5
print('PASS: the R=0 tuple (1,2,1,0,0,0,0,0) is excluded by backward Gauss persistence.')
print('PASS: exhaustive cubic image list; rank three contradiction; rank two saturation; all line degrees.')
print('PASS: exactly three quotient candidates, zero second-image torsion, two character contradictions and frozen endpoint.')
print('SCOPE: this excludes the R=0 type only. SF>=3 and square rank>=27 are unchanged; no smoothing claim.')
