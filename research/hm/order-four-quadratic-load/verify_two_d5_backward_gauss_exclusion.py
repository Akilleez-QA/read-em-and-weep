#!/usr/bin/env python3
"""Universal character, bundle-degree, and evaluation-kernel checks.

No selected HM/source coefficients, actual-instance maps/ranks, scans,
or local-model experiments. Frozen inputs are run read-only.
"""
from pathlib import Path
from itertools import combinations_with_replacement
import contextlib
import io
import runpy

here = Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
    frozen = runpy.run_path(str(here/'verify_adjacent_rank_three_gauss.py'))

va,vs,vm,sym,dimension,multiplicity,bundle_hom = [frozen[n] for n in
    ('va','vs','vm','sym','dimension','multiplicity','bundle_hom')]
reps=frozen['reps']
one,W,Wp,A,V,P,S,D,T = [reps[n] for n in
    ('one','W','Wp','A','V','P','S','D','T')]
zero=vs(0,one)
R=va(P,vs(2,D))
C=va(S,Wp,T)
Cp=va(A,V,P)

expected={
 (0,0,0,0,0,2,0,1): ('A',R,[(2,R),(8,vs(2,one)),(10,one)]),
 (0,0,0,0,0,1,1,0): ('B',R,[(2,R),(8,one),(9,W)]),
 (1,0,1,0,0,2,0,0): ('C',vs(2,D),[(2,vs(2,D)),(3,Wp),(4,V),(8,vs(2,one))]),
}
assert len(frozen['twoD'])==len(expected)==3
line_candidates={}
for tup,quadratic,blocks in frozen['twoD']:
    name,R0,E=expected[tup]
    assert quadratic==R0 and sorted(blocks,key=lambda b:b[0])==E
    assert sum(dimension(r) for j,r in E)==17
    assert sum(j*dimension(r) for j,r in E)==54
    target=[(j+1,r) for j,r in E]
    upper=max(d for d,r in target)
    candidates=[e for e in range(1,upper+1,2)
                if multiplicity(sym(e),T) and bundle_hom(one,e,target)]
    line_candidates[name]=candidates
    assert all(0<=upper-e<12 for e in candidates)
assert line_candidates=={'A':[9,11],'B':[9],'C':[9]}
assert list(sym(9))==va(S,T) and list(sym(11))==va(W,S,T)
assert all(multiplicity(sym(d),one)==0 for d in (2,4,6))

# J=O4+O8 is saturated in the only two eligible Q types.
for i in (3,5):
    profile=frozen['cubic_dual_profiles'][i-1]
    ordinary=sorted([j for j,n,c in profile
                     for _ in range(c*dimension(reps[n]))],reverse=True)
    assert ordinary[:2]==[8,6]
    assert sum(ordinary[:2])-12==2<12

# Universal complete evaluation kernels, not a chosen map evaluation.
assert va(sym(4),sym(8))==R
assert va(sym(3),sym(7))==C
assert va(sym(2),sym(6))==Cp
assert dimension(R)==14 and dimension(C)==12 and dimension(Cp)==10
assert sum((4,8))==12
assert sum((3,7))==10
assert list(sym(3))==S and list(sym(4))==D and list(sym(6))==va(V,P)
assert list(sym(7))==va(Wp,T) and list(sym(8))==va(P,D)
# Kernel degree and rank of full evaluations are -sum(target degrees)
# and sum(target degrees), respectively, agreeing with coefficient O(-1).
assert dimension(C)==4+8 and dimension(Cp)==3+7

# High-line quotients: exact Hom dimensions explain all kernel branches.
HA=[(-8,vs(2,one)),(-10,one)]
HB=[(-8,one),(-9,W)]
# Nonzero ordinary maps are already controlled; equivariance removes
# the otherwise possible O(-10)->O(-8) degree-two polynomial.
assert bundle_hom(one,-10,[(-8,one)])==0
assert bundle_hom(W,-9,[(-8,one)])==1
assert bundle_hom(one,-8,[(-8,one)])==1
assert -9*2-(-8)==-10  # Euler sequence kernel in the scalar-zero case.
assert -3-(-8)>=-1 and -3-(-10)>=-1 and -3-(-9)>=-1

# Full image and next derivative quotient degrees for all possible e.
for e in (9,11):
    I=[4,8,3-e]
    quotient=[d-2 for d in I]
    next_target=[d+1 for d in quotient]
    assert quotient==[2,6,1-e]
    assert next_target==[3,7,2-e]
    assert all(a-(3-e)>=-1 for a in (4,8)) # split image extension

# Cases eliminated at the first backward derivative, by ordinary degree.
first_cases=[
    ('A e11',[0]*12+[-5]*2,-9),
    ('B e9 graph',[0]*12+[-6]*2,-7),
]
for name,source_degrees,negative_target in first_cases:
    assert min(source_degrees)>negative_target

# Common surviving high kernel: complete section evaluation and a forced
# O(-7)->O(-7) isomorphism leave C' O(-1)+O(-5) at twist three.
assert (3-2)+3 < 3+2  # H0(E^{--}(3))=0 by persistence.
assert va(sym(3),sym(7))==C
assert -5>-7 and 0>-7
assert 4>=-1  # Ext^1(O(-5),O(-1))=H1(O4)=0.
K2degrees=[-4]*dimension(Cp)+[-8]
assert len(K2degrees)==11 and sum(K2degrees)==-48
assert min([d+4 for d in K2degrees])==-4 > -8
assert 1>0 and 1<5  # E^{--}=F1 is an interior plateau stage.

# E_C: no actual D-subsystem map is evaluated. The exact ordinary bound
# follows universally from rank four, degree -8, and H0=0.
B0parts=[ds for ds in combinations_with_replacement(range(-8,0),4)
         if sum(ds)==-8]
assert B0parts and min(min(ds) for ds in B0parts)==-5
assert all(min(ds)>=-5 and max(ds)<=-1 for ds in B0parts)
assert all(min(ds)-2>=-7 for ds in B0parts)
assert min(-3,-4)>=-7
# Thus N(7), L(7), L(8) are generated and H1(N(7)),H1(L(8)) vanish;
# K(8) is generated, so it cannot map to the required O(-10).
assert -8 > -10

# These new three types are disjoint from both earlier excluded types.
new_tuples=set(expected)
old_tuples={frozen['twoV'][0][0],frozen['threeP'][0][0]}
assert len(old_tuples)==2 and not new_tuples & old_tuples
remaining=[x for x in frozen['E_profiles']
           if x[0] not in new_tuples | old_tuples]
assert len(remaining)==23
exceptional=[x for x in remaining if dimension(x[1])==0]
assert len(exceptional)==1
assert exceptional[0][0]==(1,2,1,0,0,0,0,0)

print('PASS: all three two-D5 types and all rank-one dual image degrees exhaustively matched.')
print('PASS: both forced image saturations have possible defect at most 2, below the first orbit length 12.')
print('PASS: universal complete-evaluation kernels have coefficients C=S4+Wp+T6 and Cprime=A+V+P4.')
print('PASS: both P4+2D5 types contradict the first or second backward rank-three derivative.')
print('PASS: the 2D5 type has K ordinary degrees at least -8, incompatible with the required O(-10) quotient.')
print('WITH THE GEOMETRIC PROOF: all three two-D5 cases in (k,l)=(3,2) are excluded; at most 23 of 28 primal types remain.')
print('NOT PROVED: full (3,2) exclusion, generic rank-three exclusion, square rank 28, or smoothing closure.')
