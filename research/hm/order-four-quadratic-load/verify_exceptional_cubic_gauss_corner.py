#!/usr/bin/env python3
"""Universal exact character/degree checks for the cubic Gauss corner.

No selected coefficients, actual-instance maps, matrices, or rank tests.
The companion proof supplies all differentiation, jet, and saturation
arguments; this script reproduces their finite abstract arithmetic.
"""
from pathlib import Path
from functools import lru_cache
from itertools import combinations
import contextlib
import io
import runpy

with contextlib.redirect_stdout(io.StringIO()):
    ring = runpy.run_path(str(Path(__file__).with_name(
        'verify_negative_vertex_scalar.py')))
va, vs, vm, inner, z = [ring[x] for x in
                        ('vadd', 'vscale', 'vmul', 'inner', 'z')]
names = ['one', 'W', 'Wp', 'A', 'V', 'P', 'S', 'D', 'T']
reps = {name: ring[name] for name in names}
one, W, Wp, A, V, P, S, D, T = [reps[x] for x in names]
zero = vs(0, one)

def dimension(ch):
    assert ch[0][1] == 0 and ch[0][0].denominator == 1
    return int(ch[0][0])

def multiplicity(ch, R):
    a, b = inner(ch, R)
    assert b == 0 and a.denominator == 1
    return int(a)

def effective(ch):
    return all(multiplicity(ch, R) >= 0 for R in reps.values())

def hom(source, target):
    return multiplicity(vm(source, target), one)

@lru_cache(None)
def sym(n):
    assert n >= 0
    return tuple(ring['sym'](n, x) for x in W)

assert sum(dimension(R)**2 for R in reps.values()) == 120
for name, R in reps.items():
    for other, S0 in reps.items():
        assert multiplicity(R, S0) == int(name == other)
for n in range(55):
    assert dimension(sym(n)) == n+1 and effective(sym(n))

M2 = va(A, vs(2, V), vs(3, P), vs(4, D))
M3 = va(vs(3, Wp), vs(3, S), vs(6, T))
M4 = va(vs(2, V), vs(4, P), vs(3, D))
U = va(Wp, vs(2, T))
assert [dimension(x) for x in (M2, M3, M4, U)] == [41, 54, 37, 14]

# Positive dual identities for all j>=3 irreducible blocks. A block
# contributes j*dim(R) to dim(M3), so j<=54 exhausts every possibility.
blocks = []
for j in range(3, 55):
    for name, R in reps.items():
        if R[1][0] != (-1)**j * R[0][0]:
            continue
        c3, c2 = vm(R, sym(j-1)), vm(R, sym(j-2))
        if effective(va(M3, vs(-1, c3))) and effective(va(M2, vs(-1, c2))):
            vector = tuple(multiplicity(c3, reps[n]) for n in ('Wp','S','T'))
            vector += tuple(multiplicity(c2, reps[n]) for n in ('A','V','P','D'))
            # These seven coordinates are complete: no other constituent
            # can occur because both contributions are subrepresentations.
            assert c3 == va(*[vs(vector[i], reps[n])
                              for i,n in enumerate(('Wp','S','T'))])
            assert c2 == va(*[vs(vector[i+3], reps[n])
                              for i,n in enumerate(('A','V','P','D'))])
            blocks.append((j, name, vector, c3, c2))

assert [(j,n) for j,n,*_ in blocks] == [
    (3,'Wp'), (3,'T'), (4,'one'), (4,'V'), (4,'P'),
    (5,'W'), (5,'Wp'), (6,'one'), (6,'A'), (7,'W'), (7,'S'),
    (8,'one'), (8,'A'), (9,'W'), (10,'one'), (11,'Wp'),
    (16,'one'), (17,'W'), (18,'one'), (28,'one')]

@lru_cache(None)
def solve(i, remaining):
    if i == len(blocks):
        return ((),) if not any(remaining) else ()
    vector = blocks[i][2]
    cap = min(x//y for x,y in zip(remaining,vector) if y)
    answers = []
    for count in range(cap+1):
        rest = tuple(x-count*y for x,y in zip(remaining,vector))
        answers.extend((count,)+suffix for suffix in solve(i+1,rest))
    return tuple(answers)

solutions = solve(0, (3,3,6,1,2,3,4))
assert len(solutions) == 5
profiles = []
for counts in solutions:
    profile = tuple((j,n,count) for (j,n,*_),count in zip(blocks,counts) if count)
    profiles.append(profile)
assert profiles == [
    ((3,'T',1),(4,'V',1),(6,'one',1),(6,'A',1)),
    ((3,'T',1),(4,'V',1),(5,'W',1),(7,'W',1)),
    ((3,'T',1),(4,'V',1),(5,'W',1),(6,'one',1),(8,'one',1)),
    ((3,'T',1),(4,'one',1),(4,'V',1),(6,'one',1),(7,'W',1)),
    ((3,'T',1),(4,'one',1),(4,'V',1),(6,'one',2),(8,'one',1))]
for profile in profiles:
    assert sum(c*dimension(reps[n]) for j,n,c in profile) == 13
    assert sum(c*j*dimension(reps[n]) for j,n,c in profile) == 54
    assert va(*[vs(c,vm(reps[n],sym(j-1))) for j,n,c in profile]) == M3
    assert va(*[vs(c,vm(reps[n],sym(j-2))) for j,n,c in profile]) == M2
    assert va(*[vs(c,reps[n]) for j,n,c in profile if j==3]) == T
    assert max(j for j,n,c in profile) <= 8

# Exhaust every rank<=3 irreducible direct summand of an equivariant
# globally generated image J inside T O(4). Its degrees are 0..4 and
# its central character is odd. Each block must pass both Hom tests.
j_candidates = []
for e in range(5):
    for name,R in reps.items():
        if dimension(R)>3 or R[1][0] != (-1)**(e+1)*R[0][0]:
            continue
        if hom(U,vm(R,sym(e))) and hom(R,vm(T,sym(4-e))):
            j_candidates.append((e,name))
assert j_candidates == [(0,'Wp'),(1,'V'),(2,'Wp'),(3,'V')]
assert all(dimension(reps[n]) >= 2 for e,n in j_candidates)
assert all(4*dimension(reps[n])-e*dimension(reps[n]) < 12
           for e,n in j_candidates)
assert all(dimension(vm(reps[n],sym(e))) < 14 for e,n in j_candidates)

# Orbit-semigroup bounds, independently generated with nonnegative
# coefficients. Only 0 and12 occur at or below12.
semigroup = {12*a+20*b+30*c for a in range(6)
             for b in range(4) for c in range(3)}
assert sorted(x for x in semigroup if x<=12) == [0,12]

# Rank-one psi image test: degrees odd<=5, global sections contain T,
# and an inclusion into E*(1)=U O4+V O5 would be required.
line_psi = [e for e in (1,3,5) if multiplicity(sym(e),T)]
assert line_psi == [5]
assert hom(one,V) == 0  # O5 -> V O5; O5 -> U O4 is already zero.

# Abstract rank possibilities. Rank1 B is forbidden; rank(B)=rank(phi)
# contradicts global-section injectivity since each possible J has h0<14.
rank_profiles = [(a,b,t) for a in (2,3) for b in (2,3) for t in (2,3)
                 if a+b-3<=t<=min(a,b) and a>t]
assert rank_profiles == [(3,2,2)]

# Wp O0 would leave12 sections in a line with at most10 sections.
assert dimension(va(U,vs(-1,Wp))) == 12 > 9+1
assert vm(Wp,sym(2)) == T
K0 = va(U,vs(-1,T))
assert K0 == va(Wp,T) and dimension(K0) == 8
line_phi = [e for e in (1,3,5,7,9)
            if effective(va(sym(e),vs(-1,K0)))]
assert line_phi == [7]
assert list(sym(7)) == va(Wp,T)
assert list(sym(9)) == va(S,T)
assert va(sym(7),vm(Wp,sym(2))) == U
assert 9-7 < 12  # No equivariant torsion between the two kernel lines.

# Saturation of I=O7+Wp O2 in each Q(1). No actual inclusion is tested.
degree_I = 7+2*2
assert degree_I == 11
degree_profiles = [sorted([j+1 for j,n,c in profile
                          for _ in range(c*dimension(reps[n]))],reverse=True)
                   for profile in profiles]
top_sums = [sum(ds[:3]) for ds in degree_profiles]
assert top_sums == [21,22,22,23,23]
defects = [sorted(t for t in semigroup if t<=bound-degree_I) for bound in top_sums]
assert defects == [[0],[0],[0],[0,12],[0,12]]
assert degree_profiles[3][:4] == [8,8,7,5]
assert degree_profiles[4][:4] == [9,7,7,5]
for ds in degree_profiles[3:]:
    # At maximum degree23 there is a unique top exterior-power line.
    assert sum(1 for inds in combinations(range(13),3)
               if sum(ds[i] for i in inds)==23) == 1
    # Its rank-three bundle has no map to T O4, contradicting B!=0.
    assert min(ds[:3]) > 4

# Full kernel splitting forced after saturation. Check all shifts and
# the exact coefficient representation from twist4 cohomology.
rank_E, degree_E, rank_I = 17,-54,3
degree_quotient = degree_I-3*rank_I
rank_backward = rank_E-rank_I
degree_backward = degree_E-degree_quotient
assert degree_quotient == 2
assert (rank_backward,degree_backward) == (14,-56)
assert degree_backward+3*rank_backward == -rank_backward
sections_E4 = va(vm(U,W),V)
sections_I1 = va(sym(8),vm(Wp,sym(3)))
R_backward = va(sections_E4,vs(-1,sections_I1))
assert R_backward == va(vs(2,V),vs(2,P))
next_target = va(sym(6),vm(Wp,W))
assert next_target == va(V,vs(2,P))
assert va(R_backward,vs(-1,next_target)) == V
assert (dimension(R_backward),dimension(next_target)) == (14,11)

# Section-persistence indices: E--=F_(k-2), four derivatives end at
# F_(k+2), still interior to m=k+l when k=l=3.
k=l=3
m=k+l
assert k-2 == 1 and (k-2)+4 == k+2 == 5 < m

print('PASS: positive dual identities give20 individual blocks and exactly five formal cubic types.')
print('PASS: k=3 forces H0(Q*(3))=T6 and all dual degrees j<=8.')
print('PASS: quartic images are Wprime O, Wprime O2, V O1, V O3; rank1 is impossible.')
print('PASS: corner ranks are (3,2,2), quartic image Wprime O2, and im(phi)=O7+Wprime O2.')
print('PASS: every possible positive saturation defect contradicts the nonzero quartic projection.')
print('PASS: E^-=(2V+2P4)O(-4); next derivative forces V in H0(E^{--}(4)).')
print('WITH THE PROVED JET/SATURATION LEMMAS: generic-rank-three corner (k,l)=(3,3) is excluded.')
print('NOT PROVED: exclusion of all rank-three profiles, square rank28, maximal rank, or smoothing closure.')
