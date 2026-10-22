#!/usr/bin/env python3
"""Universal representation/bundle arithmetic only; no actual instance test.

No actual coefficients, matrices, map/rank evaluations, parameter scans,
model experiments, or positive-operator computation. The companion notes
prove all image, saturation, differentiation, and persistence claims.
"""
from pathlib import Path
import contextlib
import io
import runpy

here=Path(__file__).parent
with contextlib.chdir(here), contextlib.redirect_stdout(io.StringIO()):
    old=runpy.run_path(str(here/'verify_single_v_backward_evaluation.py'))
b=old['b']
va,vs,vm,hom,sym,dimension,effective,multiplicity,bundle_hom=[old[n] for n in
    ('va','vs','vm','hom','sym','dimension','effective','multiplicity','bundle_hom')]
reps=old['reps']
one,W,Wp,A,V,P,S,D,T=[reps[n] for n in ('one','W','Wp','A','V','P','S','D','T')]
zero=vs(0,one)
chi,sections=old['chi'],old['sections']

def rank(bs): return sum(dimension(R) for d,R in bs)
def degree(bs): return sum(d*dimension(R) for d,R in bs)
def dec(ch): return tuple(multiplicity(ch,R) for R in reps.values())
def shift(bs,t): return [(d+t,R) for d,R in bs]

excluded=set(old['excluded'])|{old['co']}
remaining=[p for p in old['old']['profiles'] if p[0] not in excluded]
assert len(excluded)==12 and len(remaining)==16
assert not [p for p in remaining if p[1]==vs(2,V)]
wanted={'X':(0,2,0,0,0,0,0,1),'Y':(0,1,1,1,0,0,0,0),
        'Z':(1,1,1,0,1,0,0,0)}
selected={n:next(p for p in remaining if p[0]==co) for n,co in wanted.items()}
assert len([p for p in remaining if p[1]==P])==3
E={n:[(-j,R) for j,R in p[2]] for n,p in selected.items()}
expected={
 'X':[(-2,P),(-3,vs(2,T)),(-10,one)],
 'Y':[(-2,P),(-3,T),(-4,V),(-4,P)],
 'Z':[(-2,P),(-3,Wp),(-3,T),(-4,V),(-5,Wp)]}
assert E==expected
for EE in E.values():
    assert rank(EE)==17 and degree(EE)==-54
assert vm(Wp,W)==P

# Full necessary psi image-block lists; rank3 irreducibles cannot project
# to Wp O2, and the only eligible rank2 block that can do so is Wp O2.
image_lists={}
for name,(_,_,blocks) in selected.items():
    target=[(j+1,R) for j,R in blocks]
    found=b['image_blocks'](T,target,-1,3)
    image_lists[name]=found
    assert [(d,n) for d,n in found if dimension(reps[n])==2 and
            bundle_hom(reps[n],d,[(2,Wp)])]==[(2,'Wp')]
    assert not [(d,n) for d,n in found if dimension(reps[n])==3 and
                bundle_hom(reps[n],d,[(2,Wp)])]
common=[(1,'V'),(2,'Wp'),(3,'V'),(4,'Wp'),(5,'V')]
assert image_lists=={'X':common+[(9,'A'),(10,'W'),(11,'one')],
                     'Y':common,'Z':common+[(6,'Wp')]}
assert hom(V,vm(Wp,W))==0
K_b3=[(-3,va(Wp,vs(2,T)))]
A_b3=[(-10,one),(-1,Wp)]
assert rank(K_b3)==14 and degree(K_b3)==-42
assert sections(K_b3,3)==va(Wp,vs(2,T))
assert sections(A_b3,1)==Wp
for t in range(-3,14):
    assert chi(E['X'],t)==va(chi(K_b3,t),chi(A_b3,t))

# If a=2 the high part maps onto O(n-2); its minimum degree bounds n.
line_options={}
for name,EE in E.items():
    H=EE[1:]
    lower=min(d for d,R in H)+2
    line_options[name]=[n for n in range(lower,9) if n%2==0 and
                       sum(bundle_hom(R,d,[(n-2,one)]) for d,R in H)]
assert line_options=={'X':[-8,4,6,8],'Y':[4,6,8],'Z':[4,6,8]}
# If a=3, ker B=Wp O(-1) maps nontrivially to O(n), n<=8.
assert [n for n in range(-1,9) if n%2==0 and
        bundle_hom(Wp,-1,[(n,one)])]==[6]
assert 6-1>=-1

# Uniform colength estimate. Positive invariant defects are at least12.
for n in (-8,4,6,8):
    An=[(n-2,one),(-1,Wp)]
    target_h0=dimension(sections(An))
    assert target_h0==max(n-1,0)
    allowed_delta=[d for d in range(0,100) if (d==0 or d>=12) and
                   15-2*n+d<=target_h0]
    assert allowed_delta==([] if n in (-8,4) else [0])
    assert -54-degree(An)-degree(shift(An,-2))==-40-2*n
for EE in E.values():
    A6=[(4,one),(-1,Wp)]
    assert va(chi(EE,4),vs(-1,chi(A6,4)),
              vs(-1,chi(A6,2)))==V
    assert sections(A6)==D and hom(V,D)==0

A8=[(6,one),(-1,Wp)]
C8=shift(A8,-2)
ch3=vs(-1,va(Wp,S,T))
ch4=va(vs(-1,A),V,P,vs(-1,D))
for EE in E.values():
    assert va(chi(EE,3),vs(-1,chi(A8,3)),vs(-1,chi(C8,3)))==ch3
    assert va(chi(EE,4),vs(-1,chi(A8,4)),vs(-1,chi(C8,4)))==ch4

# Exhaustive equivariant K2 classification from H0(K2(3))=0 and the two
# characters. All j>=5 satisfy (j-4)*dim R<=12, so j<=16.
target=vs(-1,ch3)
blocks=[]
for j in range(5,17):
    for name,R in reps.items():
        if R[1][0]!=(-1)**j*R[0][0] or (j-4)*dimension(R)>12: continue
        contribution=vm(R,sym(j-5))
        if effective(va(target,vs(-1,contribution))):
            blocks.append((j,name,contribution))
assert [(j,n) for j,n,c in blocks]==[
 (5,'Wp'),(5,'S'),(5,'T'),(6,'V'),(6,'P'),(6,'D'),(7,'Wp'),
 (8,'one'),(8,'V'),(9,'W'),(9,'Wp'),(10,'one'),(12,'one'),(14,'one')]
shapes=[]
def recurse(i,left,chosen):
    if i==len(blocks):
        if dimension(left): return
        h14=va(zero,*[vm(R,sym(j-6)) for j,R in chosen if j>=6])
        U=va(ch4,h14)
        if effective(U): shapes.append([(-4,U)]+[(-j,R) for j,R in chosen])
        return
    j,name,c=blocks[i]
    cap=min(multiplicity(left,R)//multiplicity(c,R)
            for R in reps.values() if multiplicity(c,R))
    for count in range(cap+1):
        recurse(i+1,va(left,vs(-count,c)),chosen+[(j,reps[name])]*count)
recurse(0,target,[])
assert shapes==[
 [(-4,va(V,P)),(-5,Wp),(-9,W)],
 [(-4,va(V,P)),(-5,Wp),(-8,one),(-10,one)]]
for K2 in shapes:
    assert rank(K2)==11 and degree(K2)==-56
    assert sections(K2,3)==zero
    assert chi(K2,3)==ch3 and chi(K2,4)==ch4
    for EE in E.values():
        for t in range(-3,15):
            assert chi(K2,t)==va(chi(EE,t),vs(-1,chi(A8,t)),vs(-1,chi(C8,t)))

# Frozen endpoint proof: complete evaluation and vanishing tail maps.
assert list(sym(6))==va(V,P) and list(sym(5))==T
for tail in [[(-9,W)],[(-8,one),(-10,one)]]:
    for d,R in tail:
        assert bundle_hom(R,d+4,[(-1,Wp)])==0
        assert bundle_hom(R,d,[(-7,Wp)])==0
    F0=[(-5,T)]+tail
    assert rank(F0)==8 and degree(F0)==-48
    assert sections(F0,5)==T
    assert bundle_hom(T,-5,[(-7,Wp)])==0
assert [s for s in range(5,31) if 8*s<=48 and s<=5]==[5]
weight=13*(48-8*5)
generators=(96,160,240,60,100,150)
reachable={0}
for k in range(weight+1):
    if k in reachable:
        reachable.update(k+g for g in generators if k+g<=weight)
assert weight==104 and weight not in reachable

# Close the other branch as part of this combined universal verifier.
with contextlib.chdir(here), contextlib.redirect_stdout(io.StringIO()):
    zero_pairing=runpy.run_path(str(here/'verify_p4_zero_pairing.py'))
assert zero_pairing['wanted']==wanted
new_remaining=[p for p in remaining if p[0] not in wanted.values()]
assert len(new_remaining)==13
print('The13 remaining formal primal tuples after both new branches:')
for co,R,blocks in new_remaining:
    print(str(co)+' R='+old['name'](R))
print('PASS: selected exactly the three new R=P4 tuples among the16 frozen survivors.')
print('PASS: b=3 excluded; b=2 forces A_n=O(n-2)+Wp O(-1), n=-8,4,6,8.')
print('PASS: backward degree/persistence forces n=8 and zero second-image defect.')
print('PASS: exhaustive positive character recursion gives exactly two K2 shapes.')
print('PASS: both shapes violate the frozen rank-one endpoint104 semigroup condition.')
print('PASS: the complete zero-pairing companion verifier also passes for these same three types.')
print('WITH BOTH GEOMETRIC PROOFS: at most13/28 formal primal types remain.')
print('NOT PROVED: full adjacent-profile exclusion, SF rank>=4, square rank28, or smoothing closure.')
