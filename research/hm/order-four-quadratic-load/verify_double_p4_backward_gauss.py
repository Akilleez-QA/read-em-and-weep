#!/usr/bin/env python3
"""Universal representation and hypothetical bundle arithmetic only.
No source coefficients, instance matrices/ranks, scans, or model experiments.
"""
from pathlib import Path
import runpy, contextlib, io
here=Path(__file__).parent
with contextlib.chdir(here),contextlib.redirect_stdout(io.StringIO()):
    frozen=runpy.run_path(str(here/'verify_three_p4_backward_gauss.py'))
for key in ('b','old','va','vs','vm','hom','sym','dimension','effective','multiplicity','bundle_hom','chi','sections','reps','zero','rank','degree','shift','dec'):
    globals()[key]=frozen[key]
one,W,Wp,A,V,P,S,D,T=[reps[n] for n in ('one','W','Wp','A','V','P','S','D','T')]
wanted={'X':(0,1,0,0,1,0,0,1),'Y':(0,0,1,1,1,0,0,0),'Z':(1,0,1,0,2,0,0,0)}
selected={n:next(p for p in frozen['new_remaining'] if p[0]==co) for n,co in wanted.items()}
Es={n:[(-j,R) for j,R in p[2]] for n,p in selected.items()}
assert Es=={'X':[(-2,vs(2,P)),(-3,T),(-5,Wp),(-10,one)],
 'Y':[(-2,vs(2,P)),(-4,V),(-4,P),(-5,Wp)],
 'Z':[(-2,vs(2,P)),(-3,Wp),(-4,V),(-5,vs(2,Wp))]}
assert len(selected)==3
for E in Es.values():
 assert rank(E)==17 and degree(E)==-54
 for t in range(-5,16): assert chi(E,t)==chi(frozen['E']['X'],t)
# No line image can accommodate 2P sections. A nonzero pairing has t=2;
# a=2 would kill the extra P section, hence a=3,b=2.
assert all(multiplicity(sym(n),P)<2 for n in range(0,9,2))
assert [n for n in range(0,9,2) if multiplicity(sym(n),P)]==[6,8]
assert [(a,bb) for a in range(1,4) for bb in range(1,4)
        if a==3 and 2<=min(a,bb) and a+bb-3<=2]==[(3,2)]
for n in (6,8):
 An=[(n-2,one),(-1,Wp)]
 assert 15-2*n<=dimension(sections(An))
 assert dimension(sections(An))-(15-2*n)<12
 for E in Es.values():
  ch=va(chi(E,4),vs(-1,chi(An,4)),vs(-1,chi(An,2)))
  assert ch==(V if n==6 else frozen['ch4'])
  if n==8:
   assert va(chi(E,3),vs(-1,chi(An,3)),vs(-1,chi(An,1)))==frozen['ch3']
assert hom(V,D)==0
assert len(frozen['shapes'])==2 # exhaustive frozen endpoint contradiction
# Zero pairing forces a=2,b=1. Necessary rank-one psi lists are complete.
psi_lines={n:[(d,k) for d,k in b['image_blocks'](T,[(1-d,R) for d,R in E],-1,1)] for n,E in Es.items()}
assert psi_lines=={'X':[(11,'one')],'Y':[],'Z':[]}
# Rank-two quadratic image: enumerate all irreducible blocks then pairs of lines,
# requiring enough sections and total degree <=14. This is a necessary overlist.
from itertools import combinations_with_replacement
Jshapes=set()
for dp in b['cubic_dual_profiles']:
 Q=b['q_positive'](dp)
 ds=sorted([d for d,R in Q for _ in range(dimension(R))],reverse=True)
 assert ds[0]<=8 and sum(ds[:2])<=14
 blocks=b['image_blocks'](vs(2,P),Q,1,2)
 candidates=[[(d,k)] for d,k in blocks if dimension(reps[k])==2]
 lines=[(d,k) for d,k in blocks if dimension(reps[k])==1]
 candidates += [list(pair) for pair in combinations_with_replacement(lines,2)]
 for shape in candidates:
  bs=[(d,reps[k]) for d,k in shape]
  if degree(bs)<=14 and effective(va(sections(bs),vs(-2,P))):
   Jshapes.add(tuple(shape))
assert Jshapes=={((6,'one'),(6,'one')),((6,'one'),(8,'one')),((7,'W'),)}
for shape in Jshapes:
 C0=[(d,reps[k]) for d,k in shape]
 assert 0<=14-degree(C0)<12 # image saturated in Q and hence equal C0
 assert all(d+8>=-1 for d,R in C0) # split extension by O(-8)
 AA=shift(C0,-2)+[(-10,one)]
 assert degree(AA)==degree(C0)-14
# Exhaustive necessary K splitting list with rank14, q<=12, inclusion into E',
# H0(K(2))=0, and a nonzero Hom to O(-12).
Ep=Es['X'][:-1]
assert sections(Ep,3)==va(vs(2,Wp),vs(3,T))
assert bundle_hom(one,-4,Ep)==bundle_hom(one,-6,Ep)==0
kblocks=[]
for j in range(3,16):
 for name,R in reps.items():
  if R[1][0]!=(-1)**j*R[0][0] or (j-3)*dimension(R)>12:continue
  if not bundle_hom(R,-j,Ep):continue
  cap=14//dimension(R)
  if j==3:cap=min(cap,multiplicity(sections(Ep,3),R))
  kblocks.append((j,name,cap))
Kshapes=[]
def rec(i,r,q,chosen,has_low):
 if i==len(kblocks):
  if r==14 and has_low:Kshapes.append(chosen)
  return
 j,name,cap=kblocks[i];R=reps[name];d=dimension(R)
 cap=min(cap,(14-r)//d)
 if j>3:cap=min(cap,(12-q)//((j-3)*d))
 for count in range(cap+1):
  rec(i+1,r+count*d,q+count*(j-3)*d,chosen+[(-j,R)]*count,
      has_low or (count>0 and bundle_hom(R,-j,[(-12,one)])>0))
rec(0,0,0,[],False)
assert len(Kshapes)==1
for K in Kshapes:
 assert rank(K)==14 and degree(K)==-54
 assert chi(K,3)==Wp
 assert sum(1 for d,R in K if d==-12 and R==one)==1
 for shape in Jshapes:
  C0=[(d,reps[k]) for d,k in shape]
  AA=shift(C0,-2)+[(-10,one)]
  required=va(chi(Es['X'],3),vs(-1,chi(AA,3)))
  assert required==(va(T,vs(-1,Wp)) if degree(C0)==12 else va(T,vs(-1,S)))
  assert chi(K,3)!=required
new_remaining=[p for p in frozen['new_remaining'] if p[0] not in wanted.values()]
assert len(new_remaining)==10
print('PASS: all three 2P4 nonzero-pairing branches reach the frozen endpoint contradiction.')
print('PASS: zero pairing impossible for Y,Z; X has exactly three necessary quadratic-image shapes.')
print('PASS: exhaustive K degree/parity/Hom constraints leave one shape; it has incompatible Euler character.')
print('WITH THE COMPANION GEOMETRIC PROOF: at most 10/28 formal primal types remain.')
print('UNCHANGED: SF rank >=3 and square rank >=27; no entire adjacent-profile or smoothing theorem.')
