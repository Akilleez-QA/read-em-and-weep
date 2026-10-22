#!/usr/bin/env python3
"""Universal character/degree verifier; no instance coefficients or maps."""
from pathlib import Path
from itertools import combinations_with_replacement
import contextlib,io,runpy
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
 r=runpy.run_path(str(ROOT/'verify_exceptional_cubic_gauss_corner.py'))
 p=runpy.run_path(str(ROOT/'verify_equivariant_splitting_gauss_persistence.py'))
for key in ('va','vs','vm','sym','reps','M3','M4','zero','dimension','multiplicity','effective','hom','T','one','U'):
 globals()[key]=r[key]
V,A,P,S=[reps[n] for n in ('V','A','P','S')]
profiles=[blocks for coeff,R2,blocks in p['profiles']]
assert len(profiles)==28
# A direct summand of psi's globally generated image must have a T6
# section constituent and a nonzero equivariant map to E*(1).
eligible=[]
for e in range(12):
 for n,R in reps.items():
  if dimension(R)>3 or R[1][0]!=(-1)**(e+1)*R[0][0]:continue
  if not hom(T,vm(R,sym(e))):continue
  if any(sum(hom(R,vm(C,sym(j+1-e))) for j,C in blocks if j+1>=e)
         for blocks in profiles): eligible.append((e,n))
assert eligible==[(1,'V'),(2,'Wp'),(3,'V'),(4,'Wp'),(5,'V'),
 (6,'Wp'),(7,'A'),(8,'W'),(9,'one'),(9,'A'),(10,'W'),(11,'one')]
# Deliberately allow even mixed blocks not co-occurring in a primal type:
# this is a necessary overlist, never an existence assertion.
images=[]
for count in range(1,4):
 for J in combinations_with_replacement(eligible,count):
  if sum(dimension(reps[n]) for e,n in J)==3: images.append(J)
def h0dual(J,twist):
 return sum(dimension(reps[n])*(twist-e+1) for e,n in J if e<=twist)
survivors=[]
for J in images:
 degree=sum(e*dimension(reps[n]) for e,n in J)
 assert h0dual(J,0)==0
 if degree-1<=h0dual(J,2):survivors.append(J)
assert survivors==[((1,'V'),)]
# Saturation: D-1<=h0(V O(1))=6, and D-3 is an invariant divisor.
assert [d for d in range(3,8) if d-3 in {12*a+20*b+30*c for a in range(2) for b in range(2) for c in range(2)}]==[3]
assert vm(V,sym(1))==T
assert va(U,vs(-1,vm(V,sym(3))))==va(T,vs(-1,S))
assert va(U,vs(-1,vm(V,sym(3))),vs(-1,vm(V,sym(1))))==vs(-1,S)
chiK24=va(vm(M3,sym(3)),vs(-1,vm(M4,sym(4))),
           vs(-1,vm(V,sym(4))),vs(-1,vm(V,sym(2))))
assert chiK24==va(vs(-1,A),vs(2,V),P)
# H1(K2(3))=S, with all ordinary degrees <=-4.
negative=[]
for j in range(5,9):
 for n,R in reps.items():
  if R[1][0]==(-1)**j*R[0][0] and effective(va(S,vs(-1,vm(R,sym(j-5))))):
   negative.append((j,n))
assert negative==[(5,'S'),(8,'one')]
assert not effective(chiK24)
assert va(chiK24,A)==va(vs(2,V),P)
# K2=(2V+P) O(-4)+O(-8); only the two V constant maps hit V O(-4).
assert hom(P,V)==0 and hom(one,vm(V,sym(4)))==0
assert hom(V,V)==1
# F0=(V+P) O(-4)+O(-8) cannot differentiate into V O(-6).
assert hom(one,vm(V,sym(2)))==0
assert (2*3+4+1, -(2*3+4)*4-8)==(11,-48)
assert (3+4+1,-(3+4)*4-8)==(8,-36)
print('PASS: (3,1) dual cubic derivative rank three is excluded.')
print('Necessary remaining image ranks: 1 or 2; rank-one images O(9), O(11).')
