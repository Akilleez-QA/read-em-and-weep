#!/usr/bin/env python3
"""Universal characters and hypothetical degrees only: no instance evaluations.

Companion: P4-ZERO-PAIRING-EXCLUDED-BY-BACKWARD-PERSISTENCE.md.
Reads frozen verifiers without changing them. No actual HM/source coefficients,
actual maps/matrices/ranks, parameter scans, local models, or positive operators.
"""
from pathlib import Path
from functools import lru_cache
import contextlib
import io
import runpy

here=Path(__file__).parent
with contextlib.chdir(here), contextlib.redirect_stdout(io.StringIO()):
    previous=runpy.run_path(str(here/'verify_single_v_backward_evaluation.py'))
base=previous['b']; old=previous['old']
va,vs,vm,hom,sym,dimension,effective,multiplicity,bundle_hom,chi,sections=[previous[n] for n in
 ('va','vs','vm','hom','sym','dimension','effective','multiplicity','bundle_hom','chi','sections')]
reps=previous['reps']
one,W,Wp,A,V,P,S,D,T=[reps[n] for n in ('one','W','Wp','A','V','P','S','D','T')]
zero=vs(0,one)
def rank(bs): return sum(dimension(R) for d,R in bs)
def degree(bs): return sum(d*dimension(R) for d,R in bs)
def decomposition(ch):return tuple(multiplicity(ch,R) for R in reps.values())
def pretty(ch):return '+'.join(str(multiplicity(ch,R))+n for n,R in reps.items() if multiplicity(ch,R)) or '0'

wanted={
 'X':(0,2,0,0,0,0,0,1),
 'Y':(0,1,1,1,0,0,0,0),
 'Z':(1,1,1,0,1,0,0,0),
}
Es={label:[(-j,R) for j,R in next(p for p in old['profiles'] if p[0]==co)[2]]
    for label,co in wanted.items()}
assert Es=={
 'X':[(-2,P),(-3,vs(2,T)),(-10,one)],
 'Y':[(-2,P),(-3,T),(-4,V),(-4,P)],
 'Z':[(-2,P),(-3,Wp),(-3,T),(-4,V),(-5,Wp)],
}
assert all(rank(E)==17 and degree(E)==-54 for E in Es.values())
assert 2+2<5 and 1+3<5 and 0+4<5

# Enumerate all necessary globally generated image blocks of rank <=2.
psi_lists={}
for label,E in Es.items():
    target=[(1-d,R) for d,R in E]
    psi_lists[label]=base['image_blocks'](T,target,-1,2)
assert psi_lists=={
 'X':[(2,'Wp'),(4,'Wp'),(10,'W'),(11,'one')],
 'Y':[(2,'Wp'),(4,'Wp')],
 'Z':[(2,'Wp'),(4,'Wp'),(6,'Wp')],
}
max_rank2={}
for label,E in Es.items():
    ds=sorted([1-d for d,R in E for _ in range(dimension(R))],reverse=True)
    max_rank2[label]=sum(ds[:2])
assert max_rank2=={'X':15,'Y':10,'Z':12}
assert 2*10>15 and 2*11>15  # W O(10), or two eligible line blocks.
for label,es in [('X',(2,4)),('Y',(2,4)),('Z',(2,4,6))]:
    for e in es: assert 0<=max_rank2[label]-2*e<12
assert max(1-d for d,R in Es['X'])-11==0

line_phi=set()
for dp in old['duals']:
    Q=base['q_positive'](dp)
    ds=sorted([d for d,R in Q for _ in range(dimension(R))],reverse=True)
    assert ds[0]<=8 and sum(ds[:2])<=14
    line_phi.update(e for e,n in base['image_blocks'](P,Q,1,2) if n=='one')
assert line_phi=={6,8}
assert [e for e in range(0,9,2) if hom(P,sym(e))]==[6,8]
for n in (6,8):
    assert 0<=8-n<12
    for e in (2,4,6):assert n+e-3>=-1

# Uniform torsion bound: no unproved saturation of the second image.
bounds={(n,e):3*n-4*e-8 for n in (6,8) for e in (2,4,6)}
assert bounds=={(6,2):2,(6,4):-6,(6,6):-14,(8,2):8,(8,4):0,(8,6):-8}
assert all(upper<12 for upper in bounds.values())
expected_ch4={(6,2):V,(8,4):va(vs(-1,A),vs(2,V),P),
              (8,2):va(vs(-1,A),V,P,vs(-1,D))}
for E in Es.values():
    for n,e in expected_ch4:
        quotient=[(n-2,one),(1-e,Wp)]
        quotient2=[(d-2,R) for d,R in quotient]
        assert degree(quotient)==n-2*e
        assert dimension(sections(quotient))==n-1
        assert -54-degree(quotient)-degree(quotient2)+11*5==7-2*n+4*e
        cc=va(chi(E,4),vs(-1,chi(quotient,4)),vs(-1,chi(quotient2,4)))
        assert cc==expected_ch4[n,e]
        target=sections(quotient)
        if (n,e)==(6,2):
            assert target==D and multiplicity(cc,V)==1>multiplicity(target,V)==0
        elif (n,e)==(8,4):
            assert target==va(V,P) and multiplicity(cc,V)==2>multiplicity(target,V)==1
        else:
            cc3=va(chi(E,3),vs(-1,chi(quotient,3)),vs(-1,chi(quotient2,3)))
            assert cc3==vs(-1,va(Wp,S,T))
            assert -54-degree(quotient)-degree(quotient2)==-56

# Exhaustive positive-character recursion for K2 with all degrees <=-4.
# H1(K2(3))=Wp+S+T has dimension12; every j>=5 block contributes
# (j-4)*dim(R), giving j<=16. No map evaluation is involved.
target1=va(Wp,S,T)
assert dimension(target1)==12
ch4=expected_ch4[8,2]
blocks=[]
for j in range(5,17):
    for name,R in reps.items():
        if R[1][0]!=(-1)**j*R[0][0]:continue
        if (j-4)*dimension(R)>12:continue
        contribution=vm(R,sym(j-5))
        if effective(va(target1,vs(-1,contribution))):
            blocks.append((j,name,R,contribution))
assert [(j,n) for j,n,R,c in blocks]==[
 (5,'Wp'),(5,'S'),(5,'T'),(6,'V'),(6,'P'),(6,'D'),(7,'Wp'),
 (8,'one'),(8,'V'),(9,'W'),(9,'Wp'),(10,'one'),(12,'one'),(14,'one')]
answers=[]
def recurse(i,left,tail):
    if i==len(blocks):
        if dimension(left):return
        h14=va(zero,*[vm(R,sym(j-6)) for j,R in tail if j>=6])
        U=va(ch4,h14)
        if not effective(U):return
        K2=[(-4,U)]+[(-j,R) for j,R in tail]
        if rank(K2)!=11:return
        assert degree(K2)==-56
        assert sections(K2,3)==zero and chi(K2,3)==vs(-1,target1)
        assert chi(K2,4)==ch4
        answers.append(K2)
        return
    j,name,R,c=blocks[i]
    cap=min(multiplicity(left,r)//multiplicity(c,r) for r in reps.values() if multiplicity(c,r))
    for k in range(cap+1):recurse(i+1,va(left,vs(-k,c)),tail+[(j,R)]*k)
recurse(0,target1,[])
expected_shapes=[
 [(-4,va(V,P)),(-5,Wp),(-9,W)],
 [(-4,va(V,P)),(-5,Wp),(-8,one),(-10,one)],
]
assert answers==expected_shapes

# Endpoint: the exact same universally verified rank-one semigroup obstruction.
for K2 in answers:
    tail=K2[2:]
    assert sections(K2,4)==va(V,P)==list(sym(6))
    assert list(sym(5))==T
    for d,R in tail:
        assert bundle_hom(R,d+4,[(-1,Wp)])==0
        assert bundle_hom(R,d,[(-7,Wp)])==0
    assert bundle_hom(T,-5,[(-7,Wp)])==0
    F0=[(-5,T)]+tail
    assert rank(F0)==8 and degree(F0)==-48 and sections(F0,5)==T
assert [s for s in range(5,7) if 8*s<=48 and s<=5]==[5]
weight=13*(48-8*5)
generators=(96,160,240,60,100,150)
reachable={0}
for n in range(weight+1):
    if n in reachable:reachable.update(n+g for g in generators if n+g<=weight)
assert weight==104 and weight not in reachable

# X, b=1: K embeds in Eprime, rank14, degree >=-54, degrees <=-3.
Eprime=[(-2,P),(-3,vs(2,T))]
assert rank(Eprime)==16 and degree(Eprime)==-44
assert sections(Eprime,3)==va(Wp,vs(3,T))
assert bundle_hom(one,-4,Eprime)==bundle_hom(one,-6,Eprime)==0
assert 2*12+12*3>54 # Any rank>=2 block at degree<=-12 violates the degree budget.
assert [j for j in range(12,16) if j%2==0 and j-3<=12]==[12,14]
assert 12-(14-3)==1 and 12-(12-3)==3
assert 2*(5-3)==4>3 # An odd degree-five block has dimension at least two.
assert [r for r in range(4) if (13-r)%2==0]==[1,3]
assert [2*a+6*b for a in range(2) for b in range(4)].count(10)==0
assert -40-14==-54 and -(-54)-42==12
# The line O(-10) is the only source of the quotient O(-10).
assert all(bundle_hom(R,d,[(-10,one)])==0 for d,R in Eprime)
assert bundle_hom(one,-10,[(-10,one)])==1

print('PASS: all three exact single-P4 primal types and all zero-pairing image lists.')
print('PASS: first-image saturation and uniform second-image bound exclude all but n=8,e=2.')
print('PASS: positive-character recursion gives exactly the two endpoint K2 shapes:')
for K2 in answers:print('  '+' + '.join(pretty(R)+' O('+str(d)+')' for d,R in K2))
print('PASS: endpoint complete evaluation, Hom vanishings, and 104 semigroup obstruction.')
print('PASS: the sole rank-one cubic-image branch violates its necessary negative quotient.')
print('WITH THE GEOMETRIC PROOF: zero pairing is impossible for all three single-P4 types.')
print('NOT PROVED HERE: nonzero-pairing exclusion, full adjacent-profile exclusion, SF rank>=4, or square rank28.')
