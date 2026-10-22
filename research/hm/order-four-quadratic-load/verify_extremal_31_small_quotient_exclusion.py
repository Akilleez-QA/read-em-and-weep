#!/usr/bin/env python3
"""Exact abstract character certificate; no actual maps or rank experiments."""
from pathlib import Path
import runpy, contextlib, io
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
    d=runpy.run_path(str(ROOT/'verify_extremal_31_five_quotient_section_envelopes.py'))
for key in ('va','vs','vm','sym','reps','effective','euler','sections','vec','profiles'):
    globals()[key]=d[key]
mu=d['mu']; zero=vs(0,reps['one'])
sub=lambda a,b:va(a,vs(-1,b))
survivors={tuple(x['coefficients']) for x in d['certificate'][0]['survivors']}
assert len(survivors)==4
chi3=reps['Wp']
chi4=va(reps['V'],vs(2,reps['P']),reps['D'])
A03=vs(2,reps['T'])
B=va(reps['Wp'],reps['W'],reps['S'])
patterns=[]
for coeff,R,blocks in profiles:
    if tuple(coeff) not in survivors:continue
    E3=va(*[vm(C,sections(3-j)) for j,C in blocks])
    lo=vec(sub(E3,A03)); hi=tuple(min(a,b) for a,b in zip(vec(E3),vec(B)))
    assert lo==hi
    X=sub(E3,A03); H1=sub(X,chi3)
    assert H1 in (zero,reps['S'])
    Echi4=va(*[vm(C,euler(4-j)) for j,C in blocks])
    assert sub(Echi4,va(sym(6),vm(reps['Wp'],sym(3))))==chi4
    patterns.append((coeff,vec(X)))
# K has rank 14, degree -54, and all degrees <=-3. Thus j<=15.
odd={'W','Wp','S','T'}
tails=[]
for j in range(5,16):
    for name,C in reps.items():
        if (j%2==1)!=(name in odd):continue
        if effective(sub(reps['S'],vm(C,sym(j-5)))):
            tails.append((j,name))
assert tails==[(5,'S'),(8,'one')]
# Top degree -3 coefficient X. H1 at twist 4 determines degree -4.
X=va(reps['Wp'],reps['S'])
wrong=sub(chi4,vm(X,reps['W']))
assert not effective(wrong)
right=va(wrong,reps['A'])
assert right==va(reps['V'],reps['P'])
base=sub(chi4,vm(reps['Wp'],reps['W']))
assert base==va(reps['V'],reps['P'],reps['D'])
assert list(sym(2))==reps['A'] and list(sym(3))==reps['S'] and list(sym(4))==reps['D']
# Hom(source coefficient O(-j),target coefficient O(-t)).
def hom(C,j,D,t):return mu(vm(C,vm(D,sections(j-t))),reps['one'])
# The high blocks have no map to O, except D O(-4) or S O(-3).
assert hom(reps['Wp'],3,reps['one'],0)==0
for C,j in [(reps['V'],4),(reps['P'],4),(reps['one'],8)]:
    assert hom(C,j,reps['one'],0)==0
assert hom(reps['D'],4,reps['one'],0)==1
assert hom(reps['S'],3,reps['one'],0)==1
# Standard evaluation kernels Sym^(m-1) W O(-m-1).
assert vm(reps['D'],sym(1))==va(sym(5),sym(3))
assert vm(reps['S'],sym(1))==va(sym(4),sym(2))
kernels=[[(va(reps['V'],reps['P']),4),(reps['S'],5)],
         [(va(reps['A'],reps['V'],reps['P']),4),(reps['one'],8)]]
for K2 in kernels:
    assert all(hom(C,j,reps['Wp'],5)==0 for C,j in K2)
print('PASS: four survivors force exactly two K splittings.')
print('PASS: both actual derivative kernels have Hom_G(K2,Wprime O(-5))=0.')
print('CONCLUSION with the companion sheaf proof: (n,e)=(4,2) is excluded.')
print('Other quotient cases remain; SF >= 3 and square rank >= 27 unchanged.')
