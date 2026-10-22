#!/usr/bin/env python3
"""Universal representation and hypothetical bundle arithmetic only.
No actual source coefficients, selected points, instance matrices/ranks or scans.
Frozen predecessors are executed unchanged.
"""
from pathlib import Path
from itertools import combinations_with_replacement
import runpy, contextlib, io
here=Path(__file__).parent
with contextlib.chdir(here), contextlib.redirect_stdout(io.StringIO()):
    frozen=runpy.run_path(str(here/'verify_mixed_p4_d5_octic_exclusion.py'))
    runpy.run_path(str(here/'verify_adjacent_cubic_pairing_rank.py'))
b=frozen['base']['b']
for key in ('va','vs','vm','hom','sym','dimension','effective','multiplicity','bundle_hom','chi','sections','reps','rank','degree','shift'):
    globals()[key]=frozen[key]
one,W,Wp,V,P,D,T=[reps[n] for n in ('one','W','Wp','V','P','D','T')]
profile=(1,0,2,0,0,1,0,0)
selected=next(p for p in frozen['remaining'] if p[0]==profile)
R=va(V,D)
E=[(-j,RR) for j,RR in selected[2]]
assert E==[(-2,R),(-3,Wp),(-4,vs(2,V)),(-8,one)]
assert rank(E)==17 and degree(E)==-54
assert hom(R,P)==0 # only remaining nonzero B image has section module P
assert not [n for n in range(0,9,2) if effective(va(sym(n),vs(-1,R)))]
assert [(a,bb) for a in range(2,4) for bb in range(1,4) if a+bb<=3]==[(2,1)]
Qs=[b['q_positive'](dp) for dp in b['cubic_dual_profiles']]
assert len(Qs)==5
Jshapes=set(); per_Q=[]
for Q in Qs:
    ds=sorted([d for d,RR in Q for _ in range(dimension(RR))],reverse=True)
    assert ds[0]<=8 and sum(ds[:2])<=14
    assert bundle_hom(Wp,7,Q)==0
    blocks=b['image_blocks'](R,Q,1,2)
    candidates=[[(d,k)] for d,k in blocks if dimension(reps[k])==2]
    lines=[(d,k) for d,k in blocks if dimension(reps[k])==1]
    candidates += [list(pair) for pair in combinations_with_replacement(lines,2)]
    shapes=set()
    for shape in candidates:
        J=[(d,reps[k]) for d,k in shape]
        if degree(J)<=14 and effective(va(sections(J),vs(-1,R))):shapes.add(tuple(shape))
    per_Q.append(shapes);Jshapes.update(shapes)
J5=((5,'W'),);J46=((4,'one'),(6,'one'));J7=((7,'W'),);J68=((6,'one'),(8,'one'))
assert per_Q==[{J5,J46},{J5,J46,J7},{J5,J46,J7,J68},{J5,J46,J7},{J5,J46,J7,J68}]
assert Jshapes=={J5,J46,J7,J68}
assert hom(Wp,W)==0 and hom(Wp,vm(one,sym(1)))==0
assert b['image_blocks'](T,[(1-d,RR) for d,RR in E],-1,1)==[(9,'one')]
assert max(1-d for d,RR in E)==9 # cubic image saturated
Htail=E[1:-1]
assert min(d for d,RR in Htail)>=-4
for shape in Jshapes:
    J=[(d,reps[k]) for d,k in shape];j=degree(J)
    assert j in (10,14) and 0<=14-j<12 # J saturated
    assert all(d+6>=-1 for d,RR in J) # extension by O(-8) splits
    assert dimension(R)-2==6
    # N0 has rank6, degree -j, no sections. Each irreducible
    # R0 O(-q) consumes (q-1)dim R0 of excess j-6.
    # q<=j-5 follows even before applying parity.
    eligible=[]
    for q in range(1,j-4):
        for name,R0 in reps.items():
            if R0[1][0]!=(-1)**q*R0[0][0]:continue
            if dimension(R0)<=6 and (q-1)*dimension(R0)<=j-6:
                eligible.append((q,name))
    max_q=max(q for q,name in eligible)
    assert max_q==({10:4,14:8}[j])
    assert -max_q-2>=-10
    # N(10), Htail(10) generated and H1(N(10))=0.
    assert 10-max_q-2>=0 and min(d+10 for d,RR in Htail)>=0
    AA=shift(J,-2)+[(-8,one)]
    assert degree(AA)==j-12
    assert degree(E)-degree(AA)==-42-j
    # K(10) generated; required projection to O(-10) splits.
    # Image C+O(-10), C subset J(-4), deg C=j-8-delta.
    degK2_without_delta=-24-2*j
    assert (-42-j)-(j-18)==degK2_without_delta
    # K2 rank11, each degree<=-4, one degree<=-12.
    bound=-4*10-12
    assert bound==-52
    if j==10:
        assert degK2_without_delta>bound
        continue
    assert degK2_without_delta==bound # forces delta=0 and equality splitting
    C=shift(AA,-2)
    ch=va(chi(E,4),vs(-1,chi(AA,4)),vs(-1,chi(C,4)))
    assert ch==V
    U0=va(ch,sym(6))
    assert U0==va(vs(2,V),P) and dimension(U0)==10
    assert sections(AA)==va(V,P,D)
    assert multiplicity(U0,V)==2>multiplicity(sections(AA),V)==1
remaining=[p for p in frozen['remaining'] if p[0]!=profile]
assert len(frozen['remaining'])==5 and len(remaining)==4
print('PASS: V+D5 profile (1,0,2,0,0,1,0,0) excluded by backward Gauss persistence.')
print('PASS: five Q types, all image shapes, parity kernel bound, saturation and final V multiplicity.')
print('COMBINED with frozen predecessors: at most 4/28 formal types remain.')
print('UNCHANGED: SF rank >=3, square rank >=27; no full plateau or smoothing closure.')
