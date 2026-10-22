#!/usr/bin/env python3
"""Universal abstract character checks, not coefficient or map experiments."""
from pathlib import Path
import contextlib, io, runpy
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
    base=runpy.run_path(str(ROOT/'verify_extremal_31_five_quotient_section_envelopes.py'))
for key in ('va','vs','vm','sym','reps','effective','euler','sections','vec','mu','U'):
    globals()[key]=base[key]
zero=vs(0,reps['one'])
sub=lambda a,b:va(a,vs(-1,b))
one,W,Wp,S,D,T=[reps[k] for k in ('one','W','Wp','S','D','T')]
chi=va(U,vs(-1,sym(7)),vs(-1,Wp))
assert chi==sub(T,Wp)
assert va(sym(5),sym(3))==va(T,S)
assert list(sym(4))==D and list(sym(5))==T
assert vm(D,W)==va(T,S)
assert list(sym(7))==va(Wp,T)
assert mu(sym(10),one)==0
assert vm(Wp,W)==reps['P']
assert len(base['certificate'][3]['survivors'])==10
# Euler positivity and the envelope give exactly these X values.
for X in (T,va(T,S)):
    assert effective(sub(X,chi))
    assert sub(X,chi) in (Wp,va(Wp,S))
# All K degrees <=-2; rank 14 and degree -52 bound j <=26.
odd={'W','Wp','S','T'}
for H1,expected in [(Wp,[(5,'Wp')]),(va(Wp,S),[(5,'Wp'),(5,'S'),(8,'one')])]:
    possible=[]
    for j in range(5,27):
        for name,C in reps.items():
            if (j%2==1)!=(name in odd):continue
            if effective(sub(H1,vm(C,sym(j-5)))):
                possible.append((j,name))
    assert possible==expected,(possible,expected)
# Contributions are Wp, S, S: exact H1 therefore forces Wp(-5)
# and either no optional tail, S(-5), or one(-8).
def hom(C,j,D,t):
    return mu(vm(C,vm(D,sections(j-t))),one)
assert hom(Wp,5,Wp,5)==1
assert hom(S,5,Wp,5)==0
assert hom(one,8,Wp,5)==0
assert hom(S,5,one,-2)==0
assert hom(one,8,one,-2)==0
assert hom(D,2,one,-2)==1
assert hom(T,3,one,-2)==1
assert hom(S,3,one,-2)==0
# Evaluation-kernel characters for m=4 and m=5.
assert vm(D,W)==va(sym(5),sym(3))
assert vm(T,W)==va(sym(6),sym(4))
# Twist exponents of Hom(source,evaluation kernel), for source degree -j.
# d=1: kernel S(-3), j=3,4; d=0: kernel D(-4), j=3,4.
# H1(O(q))=0 for q>=-1, hence every remaining map lifts.
for kernel_degree in (3,4):
    for j in (3,4):
        assert j-kernel_degree>=-1
# Every possible actual K2 summand has zero Hom into Wp(-7).
for name,C in reps.items():
    for j in (3,4):assert hom(C,j,Wp,7)==0
assert hom(S,5,Wp,7)==0
assert hom(one,8,Wp,7)==0
print('PASS: the (6,4) envelope forces the universal three-tail overlist.')
print('PASS: all evaluation lifts are justified by H1(O(q))=0, q>=-1.')
print('PASS: every resulting actual K2 has Hom_G(K2,Wprime O(-7))=0.')
print('CONCLUSION with the companion sheaf proof: (n,e)=(6,4) is excluded.')
print('SF >= 3 and positive-square rank >= 27 remain unchanged.')
