#!/usr/bin/env python3
"""Universal characters and hypothetical bundle arithmetic; no source instances."""
from pathlib import Path
import runpy, contextlib, io
here=Path(__file__).parent
with contextlib.chdir(here), contextlib.redirect_stdout(io.StringIO()):
    base=runpy.run_path(str(here/'verify_mixed_p4_d5_gauss_reduction.py'))
    single=runpy.run_path(str(here/'verify_single_d5_backward_gauss.py'))
for k in ('va','vs','vm','hom','sym','dimension','effective','multiplicity','bundle_hom','chi','sections','reps','rank','degree','shift','Es','wanted'):
    globals()[k]=base[k]
one,W,Wp,A,V,P,S,D,T=[reps[n] for n in ('one','W','Wp','A','V','P','S','D','T')]
# Every nonzero image summand receives T and has nonnegative degree.
def receives(d,R):
    return R[1][0]==-(-1)**d*R[0][0] and hom(T,vm(R,sym(d)))>0
assert not [(d,k) for d in range(2) for k,R in reps.items() if dimension(R)<=2 and receives(d,R)]
assert min(d for d in range(12) if receives(d,one))==5
# Lbar has degrees >=2, so quotient dual twist one has no sections.
# h0(A0)=7; chi(K2(4))=2m-9+delta forces m<=8.
assert (7+9)//2==8
assert 8-4==4<12
low_blocks=[(d,k) for d in range(2,5) for k,R in reps.items() if dimension(R)==2 and receives(d,R)]
assert low_blocks==[(2,'Wp'),(4,'W'),(4,'Wp')]
assert 2*5>8 # no pair of eligible lines
for E in Es.values():
    target=[(1-d,R) for d,R in E]
    assert bundle_hom(W,4,target)==0
    for ell in (2,4):
        AA=[(6,one),(1-ell,Wp)]
        m=2*ell
        assert degree(AA)==8-m
        assert dimension(sections(AA))==7
        assert 0<=7-(2*m-9)<12 # delta=0
        ch=va(chi(E,4),vs(-1,chi(AA,4)),vs(-1,chi(AA,2)))
        if ell==4:
            assert ch==va(vs(-1,A),vs(2,V),P)
            assert multiplicity(ch,V)==2>multiplicity(sections(AA),V)==1
        else:
            assert ch==base['frozen']['frozen']['ch4']
            assert va(chi(E,3),vs(-1,chi(AA,3)),vs(-1,chi(AA,1)))==base['frozen']['frozen']['ch3']
assert len(base['frozen']['frozen']['shapes'])==2 # frozen endpoint ran unchanged
# b=1: quotient of Htail onto O(n-2), n even, e-17<=n<=6.
expected={('X',11):[-6,4,6],('X',9):[-8,4,6],('Y',9):[-8,4,6],('Z',9):[4,6],('U',9):[4,6]}
positive=[]
for (name,e),ns in expected.items():
    E=Es[name]
    if e==11: tail=[(-3,T),(-8,one)]
    elif name in ('X','Y'): tail=[(-3,T),(-10,one)]
    elif name=='Z': tail=[(-4,V),(-4,P)]
    else: tail=[(-3,Wp),(-4,V),(-5,Wp)]
    found=[n for n in range(e-17,7,2) if sum(bundle_hom(R,d,[(n-2,one)]) for d,R in tail)>0]
    assert found==ns
    for n in found:
        lower=2*e-2*n-3
        upper=7+max(n-1,0)
        if lower>upper:
            assert n<0 or (e,n)==(11,4)
            continue
        assert n>0 and 0<=upper-lower<12 # forces delta=0
        assert min(6-(1-e),n-2-(1-e))>=-1 # extension splits
        AA=[(6,one),(n-2,one),(1-e,one)]
        assert degree(AA)==n+5-e
        degK2=-54-2*degree(AA)+6
        assert dimension(va(chi(E,4),vs(-1,chi(AA,4)),vs(-1,chi(AA,2))))==lower
        # Rank-three next derivative projects nontrivially onto O(-e-3).
        max_degree_with_low=-40-e-3
        if degK2>max_degree_with_low:
            assert (e,n) in ((9,4),(11,6))
            continue
        assert (e,n)==(9,6) and degK2==max_degree_with_low==-52
        required=va(chi(E,4),vs(-1,chi(AA,4)),vs(-1,chi(AA,2)))
        assert required==V
        U0=va(required,sym(6))
        assert U0==va(vs(2,V),P) and dimension(U0)==10
        assert sections(AA)==va(V,P,D)
        assert multiplicity(U0,V)>multiplicity(sections(AA),V)
        positive.append(name)
assert set(positive)==set(Es)
remaining=[p for p in single['new_remaining'] if p[0] not in wanted.values()]
assert len(single['new_remaining'])==9 and len(remaining)==5
print('PASS: four mixed P4+D5 octic-evaluation profiles excluded for b=1 and b=2.')
print('PASS: image saturation is derived from backward persistence, including both high lines.')
print('PASS: negative n cases use only the section bound, not an extension splitting.')
print('COMBINED: 5/28 formal types remain after the separately proved single-D5 exclusion.')
print('UNCHANGED: SF rank >=3, square rank >=27; no full plateau or smoothing closure.')
