#!/usr/bin/env python3
"""Universal hypothetical bundle arithmetic. No actual coefficients or map tests."""
from pathlib import Path
import contextlib,io,runpy
from itertools import combinations_with_replacement
here=Path(__file__).parent
with contextlib.chdir(here),contextlib.redirect_stdout(io.StringIO()):
    frozen=runpy.run_path(str(here/'verify_double_p4_backward_gauss.py'))
for key in ('b','va','vs','vm','hom','sym','dimension','effective','multiplicity','bundle_hom','chi','sections','reps','zero','rank','degree','shift','dec'):
    globals()[key]=frozen[key]
one,W,Wp,A,V,P,S,D,T=[reps[n] for n in ('one','W','Wp','A','V','P','S','D','T')]
co=(1,1,1,0,0,1,0,0)
p=next(p for p in frozen['new_remaining'] if p[0]==co)
E=[(-j,R) for j,R in p[2]]
assert E==[(-2,D),(-3,Wp),(-3,T),(-4,V),(-8,one)]
assert rank(E)==17 and degree(E)==-54
assert hom(D,vm(Wp,W))==0 # B=0
assert [(a,bb) for a in range(1,4) for bb in range(1,4) if a+bb<=3]==[(1,1),(1,2),(2,1)]
Qs=[b['q_positive'](dp) for dp in b['cubic_dual_profiles']]
for Q in Qs:
    ds=sorted([d for d,R in Q for _ in range(dimension(R))],reverse=True)
    assert ds[0]<=8 and sum(ds[:2])<=14
Et=[(1-d,R) for d,R in E]
ds=sorted([d for d,R in Et for _ in range(dimension(R))],reverse=True)
assert ds[:2]==[9,5]
psi=b['image_blocks'](T,Et,-1,2)
assert psi==[(2,'Wp'),(4,'Wp'),(8,'W'),(9,'one')]
assert 2*8>14 and 2*9>14
# b=2: the only images are Wp O(e), e=2,4. Both are saturated.
for e in (2,4):assert 0<=14-2*e<12
phi_lines=set()
for Q in Qs:
    phi_lines.update((d,n) for d,n in b['image_blocks'](D,Q,1,1))
assert phi_lines=={(4,'one'),(8,'one')}
for n in (4,8):assert 0<=8-n<12
for n in (4,8):
 for e in (2,4):
    AA=[(n-2,one),(1-e,Wp)]
    assert degree(AA)==n-2*e
    assert dimension(sections(AA))==n-1
    assert 7-2*n+4*e==degree(E)-2*degree(AA)+6+55
    bound=3*n-4*e-8
    assert bound=={(4,2):-4,(4,4):-12,(8,2):8,(8,4):0}[(n,e)]
    if bound<0:continue
    assert bound<12
    ch4=va(chi(E,4),vs(-1,chi(AA,4)),vs(-1,chi(AA,2)))
    if e==4:
        assert ch4==va(vs(-1,A),vs(2,V),P)
        assert multiplicity(ch4,V)==2 and multiplicity(sections(AA),V)==1
    else:
        assert ch4==frozen['frozen']['ch4']
        assert va(chi(E,3),vs(-1,chi(AA,3)),vs(-1,chi(AA,1)))==frozen['frozen']['ch3']
        assert len(frozen['frozen']['shapes'])==2
# b=1: unique saturated cubic line O(9), cancel E's O(-8).
assert [(d,n) for d,n in psi if dimension(reps[n])==1]==[(9,'one')]
Ep=E[:-1]
assert all(bundle_hom(R,d,[(-8,one)])==0 for d,R in Ep)
assert sections(Ep,3)==va(S,Wp,vs(2,T))
# Exhaust all necessary K blocks: rank14, degrees <=-3, excess q<=14,
# inclusion in Ep, degree-3 section multiplicity, nonzero Hom to O(-10).
kblocks=[]
for j in range(3,18):
 for name,R in reps.items():
    dim=dimension(R)
    if R[1][0]!=(-1)**j*R[0][0] or (j-3)*dim>14:continue
    if not bundle_hom(R,-j,Ep):continue
    cap=14//dim
    if j==3:cap=min(cap,multiplicity(sections(Ep,3),R))
    kblocks.append((j,name,cap))
Ks=[]
def recurse(i,r,q,chosen,low):
 if i==len(kblocks):
    if r==14 and low:Ks.append(chosen)
    return
 j,name,cap=kblocks[i];R=reps[name];dim=dimension(R)
 cap=min(cap,(14-r)//dim)
 if j>3:cap=min(cap,(14-q)//((j-3)*dim))
 for count in range(cap+1):
    recurse(i+1,r+count*dim,q+count*(j-3)*dim,chosen+[(-j,R)]*count,
      low or(count>0 and bundle_hom(R,-j,[(-10,one)])>0))
recurse(0,0,0,[],False)
assert len(Ks)==20
# C0 need NOT be globally generated. Enumerate all rank2 splittings with
# nonnegative total degree <=14 and maximum ordinary degree <=8.
# Hence all ordinary degrees are >=-8. Require only Hom to Q and D sections.
pairs={}
for Q in Qs:
 blocks=[(d,n) for d in range(-8,9) for n,R in reps.items()
         if dimension(R)<=2 and R[1][0]==(-1)**d*R[0][0] and bundle_hom(R,d,Q)]
 shapes=[[(d,n)] for d,n in blocks if dimension(reps[n])==2]
 lines=[(d,n) for d,n in blocks if dimension(reps[n])==1]
 shapes += [list(pair) for pair in combinations_with_replacement(lines,2)]
 for shape in shapes:
    C0=[(d,reps[n]) for d,n in shape]
    if not 0<=degree(C0)<=14 or multiplicity(sections(C0),D)<1:continue
    for K in Ks:
        if degree(C0)!=-degree(K)-42:continue
        if not all(chi(K,t)==va(chi(Ep,t),vs(-1,chi(C0,t-2))) for t in range(5)):continue
        key=(tuple((d,dec(R)) for d,R in K),tuple(shape))
        pairs[key]=(K,C0)
assert len(pairs)==10
# Match the complete table, not merely its size.
def kkey(K):return tuple(sorted((d,dec(R)) for d,R in K))
K10=[(-3,S),(-3,T),(-4,V),(-10,one)]
K12a=[(-3,Wp),(-3,T),(-4,D),(-10,one)]
K12b=[(-3,Wp),(-3,S),(-3,T),(-8,one),(-10,one)]
K14a=[(-3,T),(-4,V),(-4,P),(-10,one)]
K14b=[(-3,T),(-3,T),(-10,one),(-10,one)]
K14c=[(-3,Wp),(-3,T),(-4,V),(-5,Wp),(-10,one)]
expected=set()
for sh,ks in [(((5,'W'),),[K10]),(((4,'one'),(6,'one')),[K10]),
              (((4,'one'),(8,'one')),[K12a,K12b]),
              (((7,'W'),),[K14a,K14b,K14c]),
              (((6,'one'),(8,'one')),[K14a,K14b,K14c])]:
    for K in ks:expected.add((kkey(K),sh))
assert {(kkey(K),key[1]) for key,(K,C0) in pairs.items()}==expected
for K,C0 in pairs.values():
    c=degree(C0)
    assert c in (10,12,14)
    assert all(d>=4 for d,R in C0) # split E/K extension
    assert any(d==-10 and R==one for d,R in K)
    assert all(d==-10 and R==one or d>=-8 for d,R in K)
    assert all(not bundle_hom(R,d,[(-10,one)]) for d,R in K if d>=-8)
    # beta_K is scalar-surjective onto O(-10), so its image splits.
    # deg K2=-24-2c+delta; rank11 and a map to O(-12) imply <=-52.
    assert -24-2*c>=-52
    if c<14:
        assert -24-2*c>-52
        continue
    AA=shift(C0,-2)+[(-8,one)]
    CC=shift(C0,-4)+[(-10,one)]
    assert va(chi(E,4),vs(-1,chi(AA,4)),vs(-1,chi(CC,4)))==V
    assert list(sym(6))==va(V,P)
    U=va(V,sym(6))
    assert U==va(vs(2,V),P)
    target=sections(C0,-2)
    assert target==va(V,P,D)
    assert multiplicity(U,V)==2 and multiplicity(target,V)==1
new_remaining=[p for p in frozen['new_remaining'] if p[0]!=co]
assert len(new_remaining)==9
print('PASS: single D5 pairing vanishes; both possible cubic-image ranks are excluded.')
print('PASS: b=2 has four necessary quotient cases, each contradictory.')
print('PASS: b=1 exhaustive necessary splitting arithmetic gives ten pairs; all contradict backward persistence.')
print('WITH THE COMPANION GEOMETRIC PROOF: at most 9/28 formal primal types remain.')
print('UNCHANGED: SF rank >=3, square rank >=27; no full adjacent-profile or smoothing theorem.')
