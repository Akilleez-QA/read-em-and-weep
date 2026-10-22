#!/usr/bin/env python3
"""Universal character bookkeeping for the (1,3) rank-one exclusion.
No selected actual coefficient, point, map, instance matrix or rank test.
"""
from pathlib import Path
from itertools import combinations_with_replacement
import contextlib
import io
import runpy
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
    r=runpy.run_path(str(ROOT/'verify_extremal_13_cubic_image_reduction.py'))
for key in ('va','vs','vm','sym','reps','zero','dimension','multiplicity',
            'effective','hom','T','one','U','W','S','cohom','deg'):
    globals()[key]=r[key]
# The predecessor exhausts all parity-compatible individual blocks in
# both actual positive budgets, with the exhaustive bound j<=54.
assert max(j for j,n in r['qblocks'])==28
section_lines=[e for e in range(13,30,2)
               if effective(va(sym(e),vs(-1,U)))]
assert section_lines==[17,19,23,25,27,29]
lines=[e for e in section_lines if r['line_targets'](e)]
assert lines==[17,19,29]
assert r['line_targets'](17)==[(16,'one'),(17,'W'),(28,'one')]
assert r['line_targets'](19)==[(18,'one')]
assert r['line_targets'](29)==[(28,'one')]
divisors={12*a+20*b+30*c for a in range(3) for b in range(2)
          for c in range(2)}
assert [(e,f) for e in lines for f in lines if f>=e and f-e in divisors
        ]==[(17,17),(17,29),(19,19),(29,29)]
# Full saturated image slopes >=-1; one slope >=17 contributes no
# sections to either dual twist. The other two contribute at most six.
assert max(max(3-b,0)+max(1-b,0) for b in range(-1,30))==6
assert 17+2*6==29
assert 29-min(lines)+1==13
assert min(lines)-13>=-1  # H1(O(f-b))=0; extension splits.
# All possible irreducible complement blocks. An ordinary degree is
# bounded by 13 from deg B<=12 and its other degree >=-1.
eligible=[]
for b in range(-1,14):
    for n,R in reps.items():
        if dimension(R)>2 or R[1][0]!=(-1)**(b+1)*R[0][0]:
            continue
        if hom(reps['V'],vm(R,sym(b+1))):
            eligible.append((b,n))
candidates=[]
for f in lines:
    for count in (1,2):
        for B in combinations_with_replacement(eligible,count):
            if sum(dimension(reps[n]) for b,n in B)!=2:
                continue
            SS=((f,'one'),)+B
            if deg(SS)>29:
                continue
            Kchi=va(T,vs(-2,W),vs(-1,S),
                    vs(-1,cohom(SS,4,True,True)))
            envelope=va(cohom(SS,2,True),cohom(SS,0,True))
            gap=va(envelope,vs(-1,Kchi))
            assert dimension(Kchi)==deg(SS)-17
            assert not effective(gap)
            candidates.append((f,B,deg(SS),multiplicity(gap,T)))
assert candidates==[
    (17,((2,'Wp'),),21,-1),
    (17,((4,'W'),),25,-2),
    (17,((6,'W'),),29,-2),
    (17,((6,'Wp'),),29,-2),
    (17,((5,'one'),(5,'one')),27,-2),
    (19,((2,'Wp'),),23,-1),
    (19,((4,'W'),),27,-2),
    (19,((5,'one'),(5,'one')),29,-2),
]
print('PASS: rank-one cubic image in (1,3) is excluded.')
print('All eight full-saturation complements violate the dual T6 section budget.')
print('J is never identified with the full actual derivative image I.')
print('Rank-two cubic image and unresolved global bounds remain open.')
