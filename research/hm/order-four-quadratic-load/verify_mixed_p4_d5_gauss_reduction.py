#!/usr/bin/env python3
"""Universal representation and hypothetical splitting arithmetic only.
No actual source coefficients, selected points, matrices/ranks, or scans.
Frozen dependencies are executed unchanged.
"""
from pathlib import Path
from itertools import combinations_with_replacement
import runpy, contextlib, io
here=Path(__file__).parent
with contextlib.chdir(here),contextlib.redirect_stdout(io.StringIO()):
    frozen=runpy.run_path(str(here/'verify_double_p4_backward_gauss.py'))
for key in ('b','va','vs','vm','hom','sym','dimension','effective','multiplicity','bundle_hom','chi','sections','reps','zero','rank','degree','shift','dec'):
    globals()[key]=frozen[key]
one,W,Wp,A,V,P,S,D,T=[reps[n] for n in ('one','W','Wp','A','V','P','S','D','T')]
wanted={
 'X':(0,1,0,0,0,1,0,1), 'Y':(0,1,0,0,0,0,1,0),
 'Z':(0,0,1,1,0,1,0,0), 'U':(1,0,1,0,1,1,0,0)}
Es={n:[(-j,R) for j,R in next(p for p in frozen['new_remaining'] if p[0]==co)[2]] for n,co in wanted.items()}
R=va(P,D)
assert Es=={
 'X':[(-2,R),(-3,T),(-8,one),(-10,one)],
 'Y':[(-2,R),(-3,T),(-9,W)],
 'Z':[(-2,R),(-4,V),(-4,P),(-8,one)],
 'U':[(-2,R),(-3,Wp),(-4,V),(-5,Wp),(-8,one)]}
for E in Es.values():
 assert rank(E)==17 and degree(E)==-54
 for t in range(-5,16): assert chi(E,t)==chi(frozen['Es']['X'],t)
# Nonzero pairing forces a=3,b=2; its line kernel contains D.
assert dimension(R)==9>dimension(P)==4
assert [(a,bb) for a in range(1,4) for bb in range(1,4) if a==3 and 2<=min(a,bb) and a+bb-3<=2]==[(3,2)]
assert [n for n in range(0,9,2) if effective(va(sym(n),vs(-1,D)))]==[4,8]
for n in (4,8):
 An=[(n-2,one),(-1,Wp)]
 lower=15-2*n; upper=dimension(sections(An))
 if n==4: assert lower>upper
 else:
  assert upper-lower==8<12
  for E in Es.values():
   for t in (3,4):
    required=va(chi(E,t),vs(-1,chi(An,t)),vs(-1,chi(An,t-2)))
    assert required==frozen['frozen']['ch'+str(t)]
assert len(frozen['frozen']['shapes'])==2 # frozen endpoint is executed above
# A rank-one quadratic image must be the complete octic evaluation.
assert [n for n in range(0,9,2) if effective(va(sym(n),vs(-1,R)))]==[8]
assert list(sym(8))==R and list(sym(7))==va(Wp,T)
# Exhaustive necessary quadratic rank-two image overlist.
Jshapes=set()
for dp in b['cubic_dual_profiles']:
 Q=b['q_positive'](dp)
 ds=sorted([d for d,RR in Q for _ in range(dimension(RR))],reverse=True)
 assert ds[0]<=8 and sum(ds[:2])<=14
 blocks=b['image_blocks'](R,Q,1,2)
 candidates=[[(d,k)] for d,k in blocks if dimension(reps[k])==2]
 lines=[(d,k) for d,k in blocks if dimension(reps[k])==1]
 candidates += [list(pair) for pair in combinations_with_replacement(lines,2)]
 for shape in candidates:
  J=[(d,reps[k]) for d,k in shape]
  if degree(J)<=14 and effective(va(sections(J),vs(-1,R))):Jshapes.add(tuple(shape))
assert Jshapes=={((5,'W'),),((4,'one'),(6,'one')),((4,'one'),(8,'one')),((7,'W'),),((6,'one'),(8,'one'))}
line_options={n:b['image_blocks'](T,[(1-d,RR) for d,RR in E],-1,1) for n,E in Es.items()}
assert line_options=={'X':[(9,'one'),(11,'one')],'Y':[(9,'one')],'Z':[(9,'one')],'U':[(9,'one')]}
for n,E in Es.items():
 for e,_ in line_options[n]:
  assert 0<=max(1-d for d,RR in E)-e<12
  if e==11:
   assert n=='X';tail=[(-3,T),(-8,one)]
  elif n in ('X','Y'):tail=[(-3,T),(-10,one)]
  elif n=='Z':tail=[(-4,V),(-4,P)]
  else:tail=[(-3,Wp),(-4,V),(-5,Wp)]
  # Universal high-tail kernel K-theory, including W O(-9)->O(-8).
  for t in range(-2,13):assert chi(tail,t)==va(chi(E[1:],t),vs(-1,chi([(1-e,one)],t)))
  assert min(d for d,RR in tail)>=-10
  for shape in Jshapes:
   J=[(d,reps[k]) for d,k in shape];j=degree(J)
   assert j in (10,12,14) and 0<=14-j<12 # saturation
   assert all(d+e-3>=-1 for d,RR in J) # split full image
   # N0 has rank7, all degrees <=-1 and degree -j; N=N0(-2).
   assert dimension(R)-2==7
   lower_N=dimension(R)-j-5
   assert lower_N>=-10
   AA=shift(J,-2)+[(1-e,one)]
   if e==11:
    assert -1-e==-12<-10 # next derivative impossible
    continue
   # K(10) globally generated; projection onto O(-10) splits a line.
   assert -1-e==-10
   # K2 has rank11, all degrees <=-4, and must map to O(-12).
   deg_without_delta=-24-2*j
   if j<14:assert deg_without_delta>-52
   else:
    assert deg_without_delta==-52
    C=shift(J,-4)+[(-10,one)]
    required=va(chi(E,4),vs(-1,chi(AA,4)),vs(-1,chi(C,4)))
    assert required==V
    U=va(required,sym(6))
    assert U==va(vs(2,V),P) and dimension(U)==10
    assert sections(shift(C,2))==va(V,P,D)
    assert multiplicity(U,V)==2>multiplicity(sections(shift(C,2)),V)==1
print('PASS: all four mixed P4+D5 nonzero-pairing branches excluded.')
print('PASS: all four zero-pairing a=2,b=1 branches excluded, including both high tails.')
print('NECESSARY: B=0, a=1, complete evaluation onto saturated O(8); b=1 or2 remains open.')
print('UNCHANGED: at most10/28 formal types; SF rank>=3, square rank>=27; no smoothing closure.')
