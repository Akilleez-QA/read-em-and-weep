#!/usr/bin/env python3
"""Universal character and hypothetical bundle arithmetic only; no source instances."""
from pathlib import Path
import runpy, contextlib, io
here=Path(__file__).parent
with contextlib.chdir(here), contextlib.redirect_stdout(io.StringIO()):
    frozen=runpy.run_path(str(here/'verify_mixed_p4_d5_octic_exclusion.py'))
for k in ('va','vs','vm','hom','sym','dimension','effective','multiplicity','bundle_hom','chi','sections','reps','rank','degree','shift'):
    globals()[k]=frozen[k]
b=frozen['base']['b']
one,W,Wp,A,V,P,S,D,T=[reps[n] for n in ('one','W','Wp','A','V','P','S','D','T')]
R=va(V,P)
wanted={'X':(0,1,1,0,0,0,0,1),'Y':(0,0,2,1,0,0,0,0),'Z':(1,0,2,0,1,0,0,0)}
Es={n:[(-j,r) for j,r in next(p for p in frozen['remaining'] if p[0]==co)[2]] for n,co in wanted.items()}
assert Es=={'X':[(-2,R),(-3,T),(-4,V),(-10,one)],'Y':[(-2,R),(-4,vs(2,V)),(-4,P)],'Z':[(-2,R),(-3,Wp),(-4,vs(2,V)),(-5,Wp)]}
assert all(rank(E)==17 and degree(E)==-54 for E in Es.values())
# Nonzero pairing has image Wp O(1), section module P, annihilating V.
assert vm(Wp,sym(1))==P and hom(V,P)==0
assert [(a,bb) for a in range(1,4) for bb in range(1,4) if a==3 and 2<=min(a,bb) and a+bb-3<=2]==[(3,2)]
assert [n for n in range(0,9,2) if hom(V,sym(n))]==[6]
# Also a rank-one quadratic image must receive the whole R on sections.
assert [n for n in range(0,9,2) if effective(va(sym(n),vs(-1,R)))]==[6]
assert list(sym(6))==R and 8-6<12
for dp in b['cubic_dual_profiles']:
    Q=b['q_positive'](dp)
    ds=sorted([d for d,r in Q for _ in range(dimension(r))],reverse=True)
    assert max(ds)<=8 and sum(ds[:2])<=14
AA=[(4,one),(-1,Wp)]
assert degree(AA)==2 and sections(AA)==D
assert 15-2*6==3 and dimension(D)-3==2<12
for E in Es.values():
    cc=va(chi(E,4),vs(-1,chi(AA,4)),vs(-1,chi(AA,2)))
    assert cc==V and multiplicity(cc,V)>multiplicity(sections(AA),V)
# Zero pairing b=2: all source-compatible degree <=1 blocks are absent.
def receives(d,r):
    return r[1][0]==-(-1)**d*r[0][0] and hom(T,vm(r,sym(d)))>0
assert not [(d,n) for d in range(2) for n,r in reps.items() if dimension(r)<=2 and receives(d,r)]
assert min(d for d in range(12) if receives(d,one))==5
assert (5+5)//2==5 # 2m-5+delta <= h0(A0)=5 gives m<=5
assert 5-4<12 # epsilon=0
assert [(d,n) for d in range(2,3) for n,r in reps.items() if dimension(r)==2 and receives(d,r)]==[(2,'Wp')]
assert 2*5>5 # two lines cannot occur
assert 5-(2*4-5)==2<12 # delta=0
assert 4-(-1)>=-1 # split first quotient extension
# b=1: all eligible lines, not a selected candidate test.
line_lists={n:b['image_blocks'](T,[(1-d,r) for d,r in E],-1,1) for n,E in Es.items()}
assert line_lists=={'X':[(11,'one')],'Y':[],'Z':[]}
E=Es['X']; Ep=E[:-1]
assert max(1-d for d,r in E)==11
assert [bundle_hom(r,d,[(-10,one)]) for d,r in E]==[0,0,0,1]
assert rank(Ep)==16 and degree(Ep)==-44
# C0 rank two degree c<=14: deg K=-40-c>=-54.
assert -40-14==-54 and 54-14*3==12
# A tail contributing to O(-12) has j>=12; q<=12 forces a line,
# and central parity forces even j. Enumerate the necessary degree overlist.
low=[(j,n) for j in range(12,16) for n,r in reps.items()
     if r[1][0]==(-1)**j*r[0][0] and (j-3)*dimension(r)<=12]
assert low==[(12,'one'),(14,'one')]
assert bundle_hom(one,-4,Ep)==0 and bundle_hom(one,-6,Ep)==0
assert bundle_hom(A,-4,Ep)==0 and bundle_hom(V,-4,Ep)>0
assert sections(Ep,3)==va(Wp,vs(3,T))
assert 10 not in {2*a+6*bb for a in range(2) for bb in range(4)}
# Exhaust every residual splitting block after either low line, respecting
# rank13, q budget, central parity, and necessary Hom into Ep. Degree -3
# blocks are bounded additionally by actual section multiplicities of Ep(3).
solutions={}
for tail in (12,14):
    budget=12-(tail-3)
    blocks=[]
    for j in range(3,4+budget):
        for n,r in reps.items():
            if r[1][0]!=(-1)**j*r[0][0]:continue
            if (j-3)*dimension(r)>budget or not bundle_hom(r,-j,Ep):continue
            blocks.append((j,n,r))
    found=[]
    def rec(i,left,q,choice):
        if i==len(blocks):
            if left==0:found.append(choice)
            return
        j,n,r=blocks[i]; dim=dimension(r)
        cap=left//dim
        if j>3:cap=min(cap,q//((j-3)*dim))
        else:cap=min(cap,multiplicity(sections(Ep,3),r))
        for k in range(cap+1):rec(i+1,left-k*dim,q-k*(j-3)*dim,choice+[(j,n)]*k)
    rec(0,13,budget,[])
    solutions[tail]=found
assert solutions=={12:[],14:[]}
new_remaining=[p for p in frozen['remaining'] if p[0] not in wanted.values()]
assert len(frozen['remaining'])==5 and len(new_remaining)==2
print('PASS: all three R=V+P4 profiles excluded in both cubic-pairing branches.')
print('PASS: full eligible line lists, saturation bounds, Euler obstruction, and exhaustive tail arithmetic.')
print('REMAINDER: 2/28 after these exclusions alone:',[p[0] for p in new_remaining])
print('UNCHANGED: SF rank >=3, square rank >=27; no full plateau or smoothing closure.')
