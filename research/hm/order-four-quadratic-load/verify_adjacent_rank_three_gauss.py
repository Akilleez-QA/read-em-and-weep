#!/usr/bin/env python3
"""Exact universal character/degree checks for adjacent Gauss profiles.

No actual coefficients, actual-instance map evaluations, matrices, or rank tests.
The companion proof establishes the jet, derivative, and saturation lemmas.
Earlier frozen verifiers are read and run, never modified.
"""
from pathlib import Path
from functools import lru_cache
from itertools import combinations_with_replacement
from collections import Counter
import contextlib
import io
import runpy

here = Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
    base = runpy.run_path(str(here/'verify_exceptional_cubic_gauss_corner.py'))
    primal = runpy.run_path(str(here/'verify_equivariant_splitting_gauss_persistence.py'))

va,vs,vm,hom,sym,dimension,effective,multiplicity = [base[n] for n in
    ('va','vs','vm','hom','sym','dimension','effective','multiplicity')]
reps = base['reps']
one,W,Wp,A,V,P,S,D5,T = [reps[n] for n in
                       ('one','W','Wp','A','V','P','S','D','T')]
M2,M3,U = [base[n] for n in ('M2','M3','U')]
zero = vs(0,one)
cubic_dual_profiles = base['profiles']
E_profiles = primal['profiles']

def bundle_hom(R,e,target):
    """Hom_G(R O(e), direct sum of target coefficient/degree blocks)."""
    return sum(hom(R,vm(S0,sym(d-e))) for d,S0 in target if d>=e)

def image_blocks(source,target,center,max_rank):
    """Necessary direct summands of a globally generated image bundle."""
    result=[]
    for e in range(max(d for d,R in target)+1):
        for name,R in reps.items():
            if dimension(R)>max_rank:
                continue
            if R[1][0] != center*(-1)**e*R[0][0]:
                continue
            if hom(source,vm(R,sym(e))) and bundle_hom(R,e,target):
                result.append((e,name))
    return result

# Universal image-degree gap. If degree I=11, all ordinary degrees are
# >=-1 and h0(I(-1)) is at most13, against h0(E^-(4))=14.
degree11 = [ds for ds in combinations_with_replacement(range(-1,14),3)
            if sum(ds)==11]
assert degree11
assert max(sum(max(d,0) for d in ds) for ds in degree11)==13 < 14
assert -45-11 == -56 and -56+3*14 == -14
assert [n for n in range(11,14) if n%2 and n!=11] == [13]
assert (2-2)+4 < 2+3  # F0 is allowed in section persistence.

# Positive dual-character enumeration for j>=2. Every block is bounded
# by j*dim(R)<=54; all nine irreducibles and central parity are checked.
blocks=[]
for j in range(2,55):
    for name,R in reps.items():
        if R[1][0] != (-1)**j*R[0][0]:
            continue
        c3,c2=vm(R,sym(j-1)),vm(R,sym(j-2))
        if effective(va(M3,vs(-1,c3))) and effective(va(M2,vs(-1,c2))):
            vector=tuple(multiplicity(c3,reps[n]) for n in ('Wp','S','T'))
            vector+=tuple(multiplicity(c2,reps[n]) for n in ('A','V','P','D'))
            assert c3==va(*[vs(vector[i],reps[n])
                            for i,n in enumerate(('Wp','S','T'))])
            assert c2==va(*[vs(vector[i+3],reps[n])
                            for i,n in enumerate(('A','V','P','D'))])
            blocks.append((j,name,vector))
assert [(j,n) for j,n,v in blocks] == [(2,'V'),(2,'P'),(2,'D')]+[
    (j,n) for j,n,*_ in base['blocks']]
assert len(blocks)==23

@lru_cache(None)
def solve(i,remaining):
    if i==len(blocks):
        return ((),) if not any(remaining) else ()
    vector=blocks[i][2]
    cap=min(x//y for x,y in zip(remaining,vector) if y)
    answers=[]
    for count in range(cap+1):
        rest=tuple(x-count*y for x,y in zip(remaining,vector))
        answers.extend((count,)+suffix for suffix in solve(i+1,rest))
    return tuple(answers)

profiles=[tuple((j,n,c) for (j,n,v),c in zip(blocks,counts) if c)
          for counts in solve(0,(3,3,6,1,2,3,4))]
assert len(profiles)==37

def quadratic(profile):
    return va(zero,*[vs(c,reps[n]) for j,n,c in profile if j==2])

def q_positive(profile,twist=0):
    return [(j+twist,vs(c,reps[n])) for j,n,c in profile]

quad_counts=Counter()
for profile in profiles:
    assert sum(c*dimension(reps[n]) for j,n,c in profile)==13
    assert sum(c*j*dimension(reps[n]) for j,n,c in profile)==54
    assert va(*[vs(c,vm(reps[n],sym(j-1))) for j,n,c in profile])==M3
    assert va(*[vs(c,vm(reps[n],sym(j-2))) for j,n,c in profile])==M2
    R2=quadratic(profile)
    quad_counts[tuple(multiplicity(R2,R) for R in (V,P,D5))]+=1
assert quad_counts=={
    (0,0,0):5, (0,0,1):7, (0,1,0):8, (0,1,1):6,
    (0,2,0):3, (1,0,0):5, (1,1,0):3}
assert [p for p in profiles if dimension(quadratic(p))==0]==cubic_dual_profiles

# Quadratic dual derivative: rank3 is excluded geometrically by deg S0<0.
# Its only rank<=2 image blocks are Wp O1 and Wp O3; no line survives.
Estar=[(3,U),(4,V)]
quadratic_images=image_blocks(va(V,P,D5),Estar,+1,2)
assert quadratic_images==[(1,'Wp'),(3,'Wp')]
assert vm(Wp,W)==P and vm(Wp,sym(3))==va(V,D5)
assert all(4*2-e*2<12 for e,n in quadratic_images)
permitted=[]
for profile in profiles:
    R2=quadratic(profile)
    if not dimension(R2):
        continue
    for e,n in quadratic_images:
        if effective(va(vm(reps[n],sym(e)),vs(-1,R2))):
            permitted.append((profile,e))
assert Counter(tuple(multiplicity(quadratic(p),R) for R in (V,P,D5))
               for p,e in permitted)=={(0,1,0):8,(1,0,0):5,(0,0,1):7}

# Full image I projects onto Wp O(3-e), with line kernel O(n).
# Degree I>=13 and injection H0(E3)=U impose the exact finite filters.
survivors=[]
for profile,e in permitted:
    q=3-e
    Q1=q_positive(profile,1)
    upper=max(d for d,R in Q1)
    for n in range(13-2*q,upper+1):
        if n%2!=1:
            continue
        h0I=va(sym(n),vm(Wp,sym(q)))
        if effective(va(h0I,vs(-1,U))) and bundle_hom(one,n,Q1):
            survivors.append((profile,e,n))
assert survivors==[
    (((2,'P',1),(3,'T',1),(5,'W',1),(18,'one',1)),1,19),
    (((2,'P',1),(3,'T',1),(4,'one',1),(6,'one',1),(18,'one',1)),1,19)]
assert [n for n in range(9,20,2)
        if effective(va(sym(n),vs(-1,va(Wp,T))))]==[13,17,19]
assert multiplicity(sym(2),one)==multiplicity(sym(6),one)==0

# Saturation in the two high types: O19 is their unique highest line;
# the projected Wp O2 is saturated by the dual evaluation lemma.
for profile,e,n in survivors:
    Q1=q_positive(profile,1)
    assert bundle_hom(one,19,Q1)==1
    assert sum(dimension(R) for d,R in Q1 if d==19)==1
    assert max(d for d,R in Q1 if d<19)<=7
degree_I=19+2*2
degree_S0=9-degree_I
degree_dual_quotient=degree_S0-2*3
degree_dual_backward=-54-degree_dual_quotient
assert (degree_I,degree_S0,degree_dual_quotient,degree_dual_backward)==(23,-14,-20,-34)
assert 10+degree_dual_backward+3*10==6 > dimension(Wp)==2
assert (3-2)+3 < 3+2  # Dual second-backward-stage persistence.

# Zero-quadratic branch: nonzero cubic derivative has no rank-one image;
# rank3 is excluded by deg S0(1)=12-D<0. Both rank2 blocks saturate.
cubic_images=image_blocks(T,[(4,U),(5,V)],-1,3)
assert cubic_images==[(1,'V'),(2,'Wp'),(3,'V'),(4,'Wp'),(5,'V')]
cubic_rank2=[(e,n) for e,n in cubic_images if dimension(reps[n])==2]
assert cubic_rank2==[(2,'Wp'),(4,'Wp')]
assert all(5*2-e*2<12 for e,n in cubic_rank2)
assert all(max(d for d,R in q_positive(p,1))<=9 for p in cubic_dual_profiles)
assert list(sym(9))==va(S,T)
assert not effective(va(sym(9),vm(Wp,sym(2)),vs(-1,U)))

# Once the cubic derivative vanishes, T lies in H0(S0(-1)). Every
# rank-one block of S0 mapping into E* has even degree<=-2. The only
# rank-two block of degree<=3 contributing T in that twist is Wp O3.
assert all(bundle_hom(one,e,Estar)==0 for e in (0,2,4))
rank2_S0=[]
for e in (1,3):
    for name in ('W','Wp'):
        R=reps[name]
        if multiplicity(vm(R,sym(e-1)),T) and bundle_hom(R,e,Estar):
            rank2_S0.append((e,name))
assert rank2_S0==[(3,'Wp')]
assert bundle_hom(W,3,Estar)==0
assert bundle_hom(Wp,3,Estar)==1
assert vm(Wp,sym(2))==T
assert 13>9  # Forced O(D) summand of I cannot inject into Q(1).

# Separate (3,2) cubic-pairing lemma.
pairing_images=image_blocks(va(V,P,D5),[(3,T)],+1,3)
assert pairing_images==[(0,'V'),(1,'Wp'),(2,'V')]
assert [vm(reps[n],sym(e)) for e,n in pairing_images]==[V,P,va(P,D5)]
assert all(3*dimension(reps[n])-e*dimension(reps[n])<12
           for e,n in pairing_images)
line_sections=[sym(e) for e in (0,2,4,6,8)]
assert all(multiplicity(ch,R)<=1 for ch in line_sections for R in (V,P,D5))
rank2_irreducible=[vm(reps[n],sym(e)) for n in ('W','Wp') for e in (1,3,5,7)]
assert all(multiplicity(ch,P)<=2 and multiplicity(ch,D5)<=1
           for ch in rank2_irreducible)

twoV=[x for x in E_profiles if x[1]==vs(2,V)]
threeP=[x for x in E_profiles if x[1]==vs(3,P)]
assert len(twoV)==len(threeP)==1
assert twoV[0][0]==(1,0,3,0,0,0,0,0)
assert threeP[0][0]==(0,0,0,0,2,0,0,1)
assert sorted(twoV[0][2],key=lambda x:x[0])==[(2,vs(2,V)),(3,Wp),(4,vs(3,V))]
assert sorted(threeP[0][2],key=lambda x:x[0])==[(2,vs(3,P)),(5,vs(2,Wp)),(10,one)]
assert bundle_hom(one,5,[(3,vs(2,V)),(4,Wp),(5,vs(3,V))])==0
assert len(E_profiles)-len(twoV)-len(threeP)==26

# Conditional two-D5 restriction: abstract Hom spaces only, not map tests.
twoD=[x for x in E_profiles if x[1] in (vs(2,D5),va(P,vs(2,D5)))]
assert len(twoD)==3
assert [e for e in (0,2,4,6,8) if multiplicity(sym(e),D5)]==[4,8]
hom4=[]
hom8=[]
line_pairs=[]
for i,profile in enumerate(cubic_dual_profiles,1):
    residual=[(j,vs(c,reps[n])) for j,n,c in profile if (j,n)!=(3,'T')]
    h4,h8=bundle_hom(one,4,residual),bundle_hom(one,8,residual)
    hom4.append(h4)
    hom8.append(h8)
    available={4:h4,8:h8}
    for pair in combinations_with_replacement((4,8),2):
        if all(pair.count(e)<=available[e] for e in set(pair)):
            line_pairs.append((i,pair))
assert hom4==[1,1,1,1,1]
assert hom8==[0,0,1,0,1]
assert line_pairs==[(3,(4,8)),(5,(4,8))]

print('PASS: universal image-degree gap D>=13 for l=3, k>=2.')
print('PASS: 23 eligible dual blocks give exactly 37 formal types under j>=2.')
print('PASS: nonzero quadratic sections leave only two high-line types; both violate dual persistence.')
print('PASS: all five zero-quadratic types force an impossible O(D), D>=13, inside Q(1).')
print('WITH THE PROVED GEOMETRIC LEMMAS: (k,l)=(2,3) is excluded; l=3 forces k=1.')
print('PASS: (3,2) excludes primal quadratic types 2V and 3P4, leaving at most 26 formal types.')
print('PASS: its two-D5 cases force image O4+O8 and dual type 3 or5.')
print('NOT PROVED: full (3,2) exclusion, generic rank-three exclusion, square rank28, or smoothing closure.')
