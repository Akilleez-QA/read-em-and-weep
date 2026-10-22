#!/usr/bin/env python3
"""Abstract equivariant splitting constraints; no actual map/rank evaluations.

The universal section/jet/saturation lemma is proved in the companion note.
"""
from pathlib import Path
from itertools import product
from functools import lru_cache
import runpy
import io
import contextlib

with contextlib.redirect_stdout(io.StringIO()):
    ring=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
va,vs,vm,inner,z=[ring[x] for x in ('vadd','vscale','vmul','inner','z')]
names=['one','W','Wp','A','V','P','S','D','T']
reps={name:ring[name] for name in names}
one,W,Wp,A,V,P,S,D,T=[reps[x] for x in names]
assert sum(int(r[0][0])**2 for r in reps.values())==120
for a in names:
    for b in names:
        assert inner(reps[a],reps[b])==z(int(a==b))

@lru_cache(None)
def sym(n):
    assert n>=0
    return tuple(ring['sym'](n,x) for x in W)

def effective(ch):
    cs=[inner(ch,r) for r in reps.values()]
    return all(b==0 and a>=0 and a.denominator==1 for a,b in cs)

M2=va(A,vs(2,V),vs(3,P),vs(4,D))
M3=va(vs(3,Wp),vs(3,S),vs(6,T))
M4=va(vs(2,V),vs(4,P),vs(3,D))
h1E1=va(vm(W,M4),vs(-1,M3))
chiE2=va(vm(W,M3),vs(-1,vm(A,M4)))
chiE3=va(vm(A,M3),vs(-1,vm(S,M4)))
chiDual3=va(vm(A,M3),vs(-1,vm(S,M2)))
assert h1E1==va(Wp,vs(3,T))
assert chiE2==vs(-1,V)
assert chiE3==va(Wp,vs(2,T))
assert chiDual3==va(T,vs(-2,W),vs(-1,S))
assert inner(chiDual3,T)==z(1)

# Every irreducible j>=3 block contributes a genuine subrepresentation of
# H1(E(1)); total dimension20 bounds j by22.  Central parity is mandatory.
allowed=[]
for j in range(3,23):
    for name,R in reps.items():
        if R[1][0]!=(-1)**j*R[0][0]:
            continue
        contribution=vm(R,sym(j-3))
        if effective(va(h1E1,vs(-1,contribution))):
            allowed.append((j,name,contribution))
assert [(j,name) for j,name,ch in allowed]==[
    (3,'Wp'),(3,'T'),(4,'V'),(4,'P'),(5,'Wp'),(8,'one'),(9,'W'),(10,'one')]
expected=[Wp,T,T,va(Wp,T),T,T,va(Wp,vs(2,T)),va(Wp,T)]
assert [ch for j,name,ch in allowed]==expected

# Parametrization, including the exact R2 representation from chi(E(2)).
profiles=[]
for a,d,g,h in product(range(2),repeat=4):
    for b,c,e,f in product(range(4),repeat=4):
        if a+d+g+h!=1 or b+c+d+e+f+2*g+h!=3 or c+g+h<1:
            continue
        coeff=(a,b,c,d,e,f,g,h)
        R2=va(vs(c+g+h-1,V),vs(d+e+g+h,P),vs(f+g,D))
        assert effective(R2)
        blocks=[(2,R2)]+[(j,vs(n,reps[name]))
                         for n,(j,name,ch) in zip(coeff,allowed) if n]
        rank=sum(int(R[0][0]) for j,R in blocks)
        degree=-sum(j*int(R[0][0]) for j,R in blocks)
        assert (rank,degree)==(17,-54)
        calcH1E1=va(*[vm(R,sym(j-3)) for j,R in blocks if j>=3])
        calcH1E2=va(*[vm(R,sym(j-4)) for j,R in blocks if j>=4])
        assert calcH1E1==h1E1
        assert va(R2,vs(-1,calcH1E2))==chiE2
        assert all(R[1][0]==(-1)**j*R[0][0] for j,R in blocks)
        profiles.append((coeff,R2,blocks))
assert len(profiles)==28
branch_counts={i:sum(c[i] for c,R2,blocks in profiles) for i in [0,3,6,7]}
assert branch_counts=={0:10,3:4,6:4,7:10}
section_free=[c for c,R2,blocks in profiles if R2[0]==z(0)]
assert section_free==[(1,2,1,0,0,0,0,0)]
assert sorted({int(R2[0][0]) for c,R2,blocks in profiles})==[0]+list(range(3,15))
assert sorted({j for c,R2,blocks in profiles for j,R in blocks if R[0]!=z(0)})==[2,3,4,5,8,9,10]

# Euler identities hold for every listed formal splitting, not only the two
# characters used to parametrize them.  Check a range straddling all degrees.
def chi_line(degree):
    if degree>=0:
        return list(sym(degree))
    if degree==-1:
        return vs(0,one)
    return vs(-1,sym(-degree-2))
for coeff,R2,blocks in profiles:
    for twist in range(0,12):
        from_blocks=va(*[vm(R,chi_line(twist-j)) for j,R in blocks])
        from_presentation=va(vm(M3,chi_line(twist-1)),vs(-1,vm(M4,chi_line(twist))))
        assert from_blocks==from_presentation

# Dimension endpoints of a generic rank-three plateau; the improved bounds
# use the universal section-persistence lemma proved in the companion note.
assert 17//3==5 and 13//3==4
assert 17-3*3==8 and 13-3*3==4
print('PASS: actual H1(E(1))=Wprime+3T6; chi(E(2))=-V; chi(E(3))=Wprime+2T6.')
print('PASS: chi(Q*(3))=T6-2W-S4, forcing actual T6 sections.')
print('PASS: exactly eight permissible irreducible negative blocks and28 formal splitting types.')
print('PASS: unique H0(E(2))=0 type is (Wprime+2T6)O(-3)+V O(-4).')
print('WITH THE PROVED SECTION-PERSISTENCE LEMMA: rank-three plateau k<=3,l<=3; l<=2 otherwise.')
print('NOT PROVED: realization of the28 types, rank-three exclusion, maximal rank, or smoothing closure.')
