#!/usr/bin/env python3
"""Universal characters and hypothetical degree checks only.

No actual coefficients, source matrices, maps, ranks, scans, or local models.
Frozen verifiers are read and run, never modified. The companion note proves
all derivative, saturation, evaluation, extension, and persistence arguments.
"""
from pathlib import Path
from itertools import combinations_with_replacement
import contextlib
import io
import runpy

here=Path(__file__).parent
with contextlib.chdir(here), contextlib.redirect_stdout(io.StringIO()):
    base=runpy.run_path(str(here/'verify_adjacent_rank_three_gauss.py'))
    runpy.run_path(str(here/'verify_adjacent_cubic_pairing_rank.py'))
    runpy.run_path(str(here/'verify_two_d5_backward_gauss_exclusion.py'))
va,vs,vm,hom,sym,dimension,effective,multiplicity,bundle_hom=[base[n] for n in
    ('va','vs','vm','hom','sym','dimension','effective','multiplicity','bundle_hom')]
reps=base['reps']
one,W,Wp,A,V,P,S,D,T=[reps[n] for n in ('one','W','Wp','A','V','P','S','D','T')]
zero=vs(0,one)
profiles=base['E_profiles']
duals=base['cubic_dual_profiles']

def dec(ch):
    return tuple(multiplicity(ch,reps[n]) for n in reps)

def sections(blocks,twist=0):
    return va(zero,*[vm(R,sym(d+twist)) for d,R in blocks if d+twist>=0])

def chi(blocks,twist=0):
    out=[]
    for d,R in blocks:
        e=d+twist
        if e>=0: out.append(vm(R,sym(e)))
        elif e<=-2: out.append(vs(-1,vm(R,sym(-e-2))))
    return va(zero,*out)

wanted={
 'X': (0,0,2,0,0,0,0,1),
 'Y': (0,0,1,0,1,0,0,1),
 'Z1':(0,0,1,0,0,1,0,1),
 'Z2':(0,0,1,0,0,0,1,0),
 'U1':(0,0,0,0,1,1,0,1),
 'U2':(0,0,0,0,1,0,1,0),
}
selected={name:next(p for p in profiles if p[0]==co) for name,co in wanted.items()}
assert len({p[0] for p in selected.values()})==6
expected_R={'X':va(vs(2,V),P),'Y':va(V,vs(2,P)),
 'Z1':va(V,P,D),'Z2':va(V,P,D),'U1':va(vs(2,P),D),'U2':va(vs(2,P),D)}
expected_high={
 'X':[(4,vs(2,V)),(10,one)],
 'Y':[(4,V),(5,Wp),(10,one)],
 'Z1':[(4,V),(8,one),(10,one)],
 'Z2':[(4,V),(9,W)],
 'U1':[(5,Wp),(8,one),(10,one)],
 'U2':[(5,Wp),(9,W)],
}
for name,(co,R,blocks) in selected.items():
    assert R==expected_R[name]
    assert blocks[1:]==expected_high[name]
    assert dimension(R)>=10>9
    assert sum(dimension(x) for j,x in blocks)==17
    assert sum(-j*dimension(x) for j,x in blocks)==-54
assert [17-3*i for i in (3,2,1)]==[8,11,14]
assert 2+2<5 and 1+3<5 and 0+4<5

# Rank-two B: the full image has a line kernel whose sections contain R-P.
line_options={}
for name,(_,R,_) in selected.items():
    residue=va(R,vs(-1,P))
    line_options[name]=[n for n in range(0,9,2)
                        if effective(va(sym(n),vs(-1,residue)))]
assert line_options=={'X':[],'Y':[6],'Z1':[],'Z2':[],'U1':[8],'U2':[8]}
assert vm(Wp,W)==P
assert list(sym(4))==D
assert list(sym(5))==T
assert list(sym(6))==va(V,P)
assert list(sym(7))==va(Wp,T)
assert list(sym(8))==va(P,D)
for name,n in [('Y',6),('U1',8),('U2',8)]:
    R=selected[name][1]
    assert va(P,sym(n))==R
    # Complete evaluation of I=Wp O1+On and of Wp O+O(n-1).
    first_kernel=va(Wp,sym(n-1))
    assert sections([(0,Wp),(n-1,one)])==first_kernel
    assert all(j>=4 for j,x in expected_high[name])
    assert n-1>=-1  # H1(O(n-1))=0, splitting the full image extension.
assert not effective(va(D,vs(-1,va(D,V))))

# U endpoint calculation. Every tail component has zero map to Wp O(-1)
# in beta_K2(4), and then zero map to Wp O(-7) in beta_F0.
for tail in [[(-8,one),(-10,one)],[(-9,W)]]:
    for d,R in tail:
        assert bundle_hom(R,d+4,[(-1,Wp)])==0
        assert bundle_hom(R,d,[(-7,Wp)])==0
    F0=[(-5,T)]+tail
    assert sum(dimension(R) for d,R in F0)==8
    assert sum(d*dimension(R) for d,R in F0)==-48
    assert sections(F0,5)==T
    assert bundle_hom(T,-5,[(-7,Wp)])==0
assert hom(one,vm(Wp,W))==0
assert hom(one,vm(Wp,sym(3)))==0
assert hom(W,vm(Wp,sym(2)))==0
assert [s for s in range(5,31) if 8*s<=48]==[5,6]
assert [s for s in range(5,7) if s<=5]==[5]
weight=13*(48-8*5)
generators=(12*8,20*8,30*8,12*5,20*5,30*5)
reachable={0}
for k in range(weight+1):
    if k in reachable:
        reachable.update(k+g for g in generators if k+g<=weight)
assert weight==104 and weight not in reachable

# Enumerate only hypothetical rank-two image shapes into the five Q types.
# Individual Hom existence and repeated-line Hom dimensions are necessary,
# not sufficient, for an injection; using them gives a safe overlist.
shape_blocks={
 'W5':[(5,W)], 'W7':[(7,W)],
 '44':[(4,one),(4,one)], '46':[(4,one),(6,one)],
 '48':[(4,one),(8,one)], '66':[(6,one),(6,one)],
 '68':[(6,one),(8,one)], '88':[(8,one),(8,one)],
}
actual_shape_lists={}
for name,(_,R,_) in selected.items():
    options=set()
    for dp in duals:
        Q=base['q_positive'](dp)
        available=base['image_blocks'](R,Q,+1,2)
        for e,rn in available:
            if dimension(reps[rn])!=2: continue
            if effective(va(vm(reps[rn],sym(e)),vs(-1,R))):
                assert rn=='W' and e in (5,7)
                options.add(f'W{e}')
        lines=[e for e,rn in available if rn=='one']
        for e,f in combinations_with_replacement(lines,2):
            if e==f and bundle_hom(one,e,Q)<2: continue
            if effective(va(sym(e),sym(f),vs(-1,R))):
                options.add(f'{e}{f}')
    actual_shape_lists[name]=options
expected_shapes={
 'X':{'66'}, 'Y':{'W7','66','68'},
 'Z1':{'W5','46','W7','68'}, 'Z2':{'W5','46','W7','68'},
 'U1':{'W7','68'}, 'U2':{'W7','68'},
}
assert actual_shape_lists==expected_shapes
for dp in duals:
    Q=base['q_positive'](dp)
    degrees=sorted([d for d,R in Q for _ in range(dimension(R))],reverse=True)
    assert degrees[0]<=8 and sum(degrees[:2])<=14
    assert bundle_hom(one,8,Q)<=1
for options in expected_shapes.values():
    for shape in options:
        J=shape_blocks[shape]
        j=sum(d*dimension(R) for d,R in J)
        assert j in (10,12,14) and 0<=14-j<12
        assert all(d>=4 for d,R in J)

# Rank-one psi: abstract source character and target Hom filters.
line_psi={}
for name,(_,R,blocks) in selected.items():
    target=[(j+1,x) for j,x in blocks]
    upper=max(d for d,x in target)
    opts=[e for e in range(1,upper+1,2)
          if multiplicity(sym(e),T) and bundle_hom(one,e,target)]
    line_psi[name]=opts
    assert all(0<=upper-e<=2<12 for e in opts)
assert line_psi=={'X':[11],'Y':[11],'Z1':[9,11],
                 'Z2':[9],'U1':[9,11],'U2':[9]}

# Ordinary N0 degree bound follows from H0(N0)=0 and sum degrees=-j.
for name,(_,R,_) in selected.items():
    for shape in expected_shapes[name]:
        J=shape_blocks[shape]
        j=sum(d*dimension(x) for d,x in J)
        r=dimension(R)-2
        lower_N=-j+(r-1)-2
        assert lower_N==dimension(R)-j-5
        assert lower_N>=-8
        if name.startswith(('U','Z')):
            assert lower_N>=-7
        # All e=11 high tails have degree >=-8, hence K has no O(-12) map.
        if 11 in line_psi[name]:
            high=[(jj,x) for jj,x in expected_high[name] if jj!=10]
            assert max(jj for jj,x in high)<=8
assert -8>-12

# e=9 high kernels, including the unique W evaluation.
assert hom(W,W)==1 and hom(one,one)==1
assert vm(W,W)==va(one,A)
assert bundle_hom(V,-4,[(-8,one)])==0
assert bundle_hom(Wp,-5,[(-8,one)])==0
# [W O(-9)] = [O(-8)] + [O(-10)] in equivariant K-theory.
for t in range(0,13):
    assert chi([(-9,W)],t)==chi([(-8,one),(-10,one)],t)
assert -7>-10 and -7+10>=-1

# Sharp e=9 bottleneck: K2 rank11, degrees <=-4, one <=-12.
max_degree_K2=-12-10*4
assert max_degree_K2==-52
for j in (10,14):
    admissible_deltas=[delta for delta in range(100)
                       if -24-2*j+delta<=-52]
    assert admissible_deltas==([] if j==10 else [0])
assert -24-2*14==-52
assert 10*(-4)+(-12)==-52

# Exact K-theory character in the forced delta=0, j=14 branch.
for name in ('Z1','Z2','U1','U2'):
    E=[(-j,R) for j,R in selected[name][2]]
    for shape in ('W7','68'):
        J=shape_blocks[shape]
        quotient1=[(d-2,R) for d,R in J]+[(-8,one)]
        quotient2=[(d-4,R) for d,R in J]+[(-10,one)]
        chiK2=va(chi(E,4),vs(-1,chi(quotient1,4)),vs(-1,chi(quotient2,4)))
        assert chiK2==V
        U=va(chiK2,sym(6))
        assert U==va(vs(2,V),P) and dimension(U)==10
        target=sections(J,-2)
        assert target==va(V,P,D)
        assert multiplicity(U,V)==2>multiplicity(target,V)==1

# New types are disjoint from both frozen earlier groups.
old=[]
for co,R,blocks in profiles:
    if R in (vs(2,V),vs(3,P),vs(2,D),va(P,vs(2,D))): old.append(co)
assert len(old)==5 and not set(old).intersection(wanted.values())
assert len(profiles)-len(old)-len(selected)==17

print('PASS: six exact large-R primal types, disjoint from the five frozen exclusions.')
print('PASS: rank-two pairing leaves only n=6 or8; backward evaluations and endpoint degree semigroup exclude both.')
print('PASS: zero-pairing image shapes, e=9/11 line degrees, and saturation defects are exhaustively filtered.')
print('PASS: e=11 violates the negative quotient; e=9 forces K2=(2V+P)O(-4)+O(-12), violating final persistence.')
print('WITH THE PROVED GEOMETRIC LEMMAS: at most17/28 formal primal types remain for (3,2).')
print('NOT PROVED: full adjacent-profile exclusion, generic SF rank>=4, square rank28, or a smoothing conclusion.')
