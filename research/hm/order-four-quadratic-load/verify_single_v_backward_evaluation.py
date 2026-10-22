#!/usr/bin/env python3
"""Universal representation/bundle arithmetic only, not an instance test.

Runs earlier frozen verifiers without modifying them. No actual HM/source
coefficients, actual maps/matrices/ranks, parameter scans, or local models.
The companion note proves all image, extension, and differentiation claims.
"""
from pathlib import Path
from itertools import combinations_with_replacement
import contextlib
import io
import runpy

here=Path(__file__).parent
with contextlib.chdir(here), contextlib.redirect_stdout(io.StringIO()):
    old=runpy.run_path(str(here/'verify_six_large_quadratic_gauss_exclusions.py'))
b=old['base']
va,vs,vm,hom,sym,dimension,effective,multiplicity,bundle_hom=[old[n] for n in
    ('va','vs','vm','hom','sym','dimension','effective','multiplicity','bundle_hom')]
reps=old['reps']
one,W,Wp,A,V,P,S,D,T=[reps[n] for n in ('one','W','Wp','A','V','P','S','D','T')]
zero=vs(0,one)
chi,sections=old['chi'],old['sections']

def name(ch):
    return '+'.join((str(multiplicity(ch,r)) if multiplicity(ch,r)>1 else '')+n
                    for n,r in reps.items() if multiplicity(ch,r)) or '0'

def rank(bs): return sum(dimension(R) for d,R in bs)
def degree(bs): return sum(d*dimension(R) for d,R in bs)

def ext1(source,target):
    # Ext^1_G(R O(d),S O(e))=Hom_G(R,S tensor H^1(O(e-d))).
    return sum(hom(R,vm(S0,sym(d-e-2)))
               for d,R in source for e,S0 in target if d-e>=2)

excluded=set(old['old'])|set(old['wanted'].values())
remaining=[p for p in old['profiles'] if p[0] not in excluded]
assert len(excluded)==11 and len(remaining)==17
selected=[p for p in remaining if p[1]==V]
assert len(selected)==1
co,R,blocks=selected[0]
assert co==(1,1,2,0,0,0,0,0)
E=[(-j,x) for j,x in blocks]
assert E==[(-2,V),(-3,Wp),(-3,T),(-4,vs(2,V))]
assert rank(E)==17 and degree(E)==-54
assert 2+2<5 and 1+3<5 and 0+4<5
assert hom(V,P)==0  # B cannot have the remaining Wp O(1) image.

# Every individual globally generated image block is checked abstractly.
target=[(j+1,x) for j,x in blocks]
psi_blocks=b['image_blocks'](T,target,-1,3)
assert psi_blocks==[(1,'V'),(2,'Wp'),(3,'V'),(4,'Wp'),(5,'V')]
assert not [x for x in psi_blocks if dimension(reps[x[1]])==1]
assert [x for x in psi_blocks if dimension(reps[x[1]])==2]==[(2,'Wp'),(4,'Wp')]
assert hom(T,sym(1))==hom(T,sym(3))==0 and hom(T,sym(5))==1
assert bundle_hom(one,5,target)==0
line_phi=set()
for dp in old['duals']:
    Q=b['q_positive'](dp)
    assert max(d for d,x in Q)<=8
    line_phi.update(e for e,n in b['image_blocks'](V,Q,1,2) if n=='one')
assert line_phi=={6}
assert [e for e in range(0,9,2) if hom(V,sym(e))]==[6]
assert 0<=8-6<12
for e in (2,4):
    assert 0<=2*5-2*e<12
    assert 3+e>=-1  # splitting the full first image extension.

# Canonical V-subsystem kernel N0: all rank-two splitting possibilities.
assert vm(V,sym(3))==va(Wp,S,T)
assert hom(W,vm(V,sym(3)))==0
assert hom(Wp,vm(V,sym(3)))==1
assert [(d,e) for d,e in combinations_with_replacement(range(-6,0),2)
        if d+e==-6 and d%2==e%2==0]==[(-4,-2)]
assert bundle_hom(one,-2,[(0,V)])==0
assert ext1([(-3,T),(-4,vs(2,V))],[(-5,Wp)])==0

# Complete evaluation is checked in equivariant K-theory, universally.
def eval_sequence(R,d,twist):
    assert d>=1
    src=[(twist,vm(R,sym(d)))]
    ker=[(twist-1,vm(R,sym(d-1)))]
    tgt=[(twist+d,R)]
    for t in range(-3,13):
        assert chi(src,t)==va(chi(ker,t),chi(tgt,t))

eval_sequence(one,1,-4)
eval_sequence(Wp,1,-4)
eval_sequence(Wp,1,-1)
eval_sequence(Wp,2,-3)
eval_sequence(one,5,0)
assert vm(Wp,W)==P
assert vm(Wp,sym(2))==T
assert vm(Wp,sym(3))==va(V,D)

H=[(-3,Wp),(-3,T),(-4,vs(2,V))]
assert bundle_hom(Wp,-3,[(-1,Wp)])==0
assert bundle_hom(T,-3,[(-1,Wp)])==1
assert bundle_hom(V,-4,[(-1,Wp)])==1
assert bundle_hom(T,-3,[(-3,Wp)])==0
assert bundle_hom(V,-4,[(-3,Wp)])==0
assert 3*(-4)-2*(-1)==-10  # line kernel when alpha=0.

H_nonzero=[(-3,Wp),(-4,va(P,vs(2,V)))]
H_zero=[(-3,va(Wp,T)),(-4,V),(-10,one)]
assert ext1(H_nonzero,[(-5,Wp)])==1
assert ext1(H_zero,[(-5,Wp)])==1
assert ext1([(-3,Wp)],[(-5,Wp)])==1
for HH in (H_nonzero,H_zero):
    for t in range(-3,13):
        assert chi(HH,t)==va(chi(H,t),vs(-1,chi([(-1,Wp)],t)))

Kshapes={
 'A':[(-3,Wp),(-4,va(P,vs(2,V))),(-5,Wp)],
 'B':[(-4,va(vs(2,P),vs(2,V)))],
 'C':[(-3,va(Wp,T)),(-4,V),(-5,Wp),(-10,one)],
 'D':[(-3,T),(-4,va(P,V)),(-10,one)],
}
A2=[(4,one),(-1,Wp)]
for n,K in Kshapes.items():
    assert rank(K)==14 and degree(K)==-56
    for t in range(-3,13):
        assert chi(K,t)==va(chi(E,t),vs(-1,chi(A2,t)))
assert sections(Kshapes['A'],3)==Wp
assert sections(Kshapes['B'],3)==zero
assert sections(Kshapes['C'],3)==va(Wp,T)
assert sections(Kshapes['D'],3)==T
assert sections([(5,one),(0,Wp)])==va(T,Wp)
assert hom(Wp,T)==hom(T,Wp)==0
assert bundle_hom(V,-1,[(0,Wp)])==0
assert bundle_hom(P,-1,[(0,Wp)])==1
L0=[(-1,va(P,vs(2,V))),(-2,Wp)]
assert rank(L0)==12 and degree(L0)==-14
assert min(d for d,x in L0)==-2
assert 5-min(d for d,x in L0)==7<12
# All invariant effective divisor lengths <=7 vanish.
assert [12*a+20*c+30*d for a in range(1) for c in range(1)
        for d in range(1) if 12*a+20*c+30*d<=7]==[0]

# e=4 kernel and complete evaluation. Degree rules isolate its Wp block.
K4=[(-3,T),(-4,vs(2,V)),(-5,Wp)]
A4=[(4,one),(-3,Wp)]
assert rank(K4)==14 and degree(K4)==-52
assert sections(K4,3)==T
assert bundle_hom(T,0,[(-2,Wp)])==0
assert bundle_hom(V,-1,[(-2,Wp)])==0
assert bundle_hom(Wp,-2,[(-2,Wp)])==1
for t in range(-3,13):
    assert chi(K4,t)==va(chi(E,t),vs(-1,chi(A4,t)))

# Once beta_K is surjective, its two quotient bundles fix chi(K2(4)).
for e,Ae,expected in [(2,A2,V),(4,A4,va(D,vs(2,V)))]:
    q2=[(d-2,x) for d,x in Ae]
    K2chi=va(chi(E,4),vs(-1,chi(Ae,4)),vs(-1,chi(q2,4)))
    assert K2chi==expected
    final_target=sections(q2,2)
    assert final_target==D
    assert multiplicity(K2chi,V)>multiplicity(final_target,V)==0

print('The 17 formal types remaining before the new exclusion:')
for coeff,R,bs in remaining:
    print(str(coeff)+'  R='+name(R)+'  E='+
          ' + '.join(name(x)+' O(-'+str(j)+')' for j,x in bs if dimension(x)))
print('PASS: the unique R=V type is disjoint from all eleven frozen exclusions.')
print('PASS: B=0 forces phi image O(6) and psi image Wprime O(2) or O(4), all saturated.')
print('PASS: canonical V-evaluation kernel, exhaustive four K shapes, and complete evaluation identities.')
print('PASS: both second quotients force a V constituent in H0(K2(4)), absent from the final target D5.')
assert len(remaining)-len(selected)==16
print('WITH THE GEOMETRIC PROOF: at most16/28 formal primal types remain for (3,2).')
print('NOT PROVED: full adjacent-profile exclusion, generic SF rank>=4, square rank28, or smoothing closure.')
