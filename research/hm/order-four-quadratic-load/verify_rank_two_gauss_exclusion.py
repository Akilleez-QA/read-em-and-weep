#!/usr/bin/env python3
"""Universal flag integers and exact abstract characters, never actual map tests.

The geometric saturated-flag, diagonal-contact, and projection lemmas are proved
in RANK-TWO-GAUSS-EXCLUSION-BY-ENDPOINT-FLAGS.md.  This program checks their finite
integer/representation consequences only.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from pathlib import Path
import contextlib
import io
import runpy


@lru_cache(None)
def semigroup(cap):
    if cap < 0:
        return ()
    values={0}
    for t in range(cap+1):
        if t in values:
            values.update(t+g for g in (12,20,30) if t+g<=cap)
    return tuple(sorted(values))


def catalog(n,r,Dmax):
    """All possible (D,h), retaining every invariant orbit-degree choice.

    Collapse only by weighted degree R and initial-degree numerator T.
    These two integers determine D and h, so no such pair is lost.
    """
    s=n-r
    cap=n*(Dmax-r*s)
    if cap<0:
        return {}
    weights=[s*j if j<r else r*(n-j) for j in range(1,n)]
    choices=semigroup(cap//min(weights))
    states={(0,0)}
    for j,w in enumerate(weights,1):
        nxt=set()
        for R,T in states:
            for delta in choices:
                if R+w*delta>cap:
                    break
                nxt.add((R+w*delta,T+(n-j)*delta))
        states=nxt
    result=defaultdict(set)
    for R,T in states:
        if R%n or T%n:
            continue
        D=r*s+R//n
        h=n-1+T//n
        if D%2 or h%2:
            continue
        result[D].add(h)
    return dict(result)


def full_flags(n,r,D):
    """All vectors, without the (R,T) collapse used for degree-only tables."""
    s=n-r
    budget=n*(D-r*s)
    weights=[s*j if j<r else r*(n-j) for j in range(1,n)]
    choices=semigroup(budget//min(weights))
    def recurse(j,left,ds):
        if j==n:
            if left:
                return
            T=sum((n-jj)*d for jj,d in enumerate(ds,1))
            if T%n:
                return
            h=n-1+T//n
            if h%2:
                return
            a=[-h]
            for d in ds:
                a.append(a[-1]+2+d)
            assert sum(a)==0 and -sum(a[:r])==D
            assert all(x%2==0 for x in a)
            yield tuple(ds),tuple(a)
            return
        w=weights[j-1]
        for d in choices:
            if w*d>left:
                break
            yield from recurse(j+1,left-w*d,ds+[d])
    yield from recurse(1,budget,[])


# Diagonal contact and minimal complementary span dimensions.
for k,l in [(1,1),(1,2),(2,1)]:
    m=k+l; p=17-2*k; q=13-2*l
    assert p+q+m-1==29-m
    assert p+m+q+m==30
assert 29-2==27 and 29-3==26
assert 2*60+36>150  # Nonorthogonal (1,2).
assert 52+2*48<=150<52+2*50
assert 15*(46-44)==30<48
assert 60 not in {48*a+80*b+120*c+132*d+220*e+330*f
                  for a,b,c,d,e,f in product(range(2),repeat=6)}
assert 14<26  # Remaining nonorthogonal (2,1) upper line degree.

# Exhaustive full-integrality lists for nonorthogonal (1,1).
expected={
    (18,15,70):[54,60,66], (19,15,70):[60],
    (14,11,58):[42,48,54], (15,11,58):[44,52,56],
    (16,11,58):[],
}
cat={key:catalog(*key) for key in expected}
for key,degrees in expected.items():
    assert sorted(cat[key])==degrees,(key,cat[key])
assert cat[15,11,58][44]=={14}
nonorth=[]
for n in [18,19]:
    for nn in [14,15,16]:
        for A,hs in cat[n,15,70].items():
            for B,hhs in cat[nn,11,58].items():
                delta=104-A-B
                if delta in semigroup(104):
                    nonorth.append((n,nn,A,B,delta))
                    assert (A,B,delta)==(60,44,0)
                    assert max(hhs)<27
assert nonorth==[(18,15,60,44,0),(19,15,60,44,0)]

# Orthogonal projection: 54=D_C+D_B+tau, tau in the orbit semigroup.
assert 54-2*16-12==10<12
assert 54-2*16-11==11<12
assert 54-2*15-24==0
assert 12*(14-12)==24 and (-(14-1))%2==1
# The unramified upper flag in the last case has odd initial degree.

pair_lists={}
for k,l in [(1,1),(1,2)]:
    r,n=17-k,17-k+l
    rr,nn=13-l,13+k-l
    lo=max(2*r,r*(n-r))
    up=rr*(nn-rr)
    C={D:hs for D,hs in catalog(n,r,54-up).items() if D>=lo}
    B={D:hs for D,hs in catalog(nn,rr,54-lo).items() if D>=up}
    pair_lists[k,l]=[(D,DD) for D in sorted(C) for DD in sorted(B)
                     if 54-D-DD in semigroup(54)]
    assert all(D+DD==54 for D,DD in pair_lists[k,l])
assert pair_lists[1,1]==[(32,22),(34,20),(36,18),(38,16),(42,12)]
assert pair_lists[1,2]==[(38,16),(42,12)]

# Exact character ring, using only the existing universal abstract verifier.
with contextlib.redirect_stdout(io.StringIO()):
    ring=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
va,vs,vm,inner,z=[ring[x] for x in ('vadd','vscale','vmul','inner','z')]
W,Wp,A,V,P,D,S,T=[ring[x] for x in ('W','Wp','A','V','P','D','S','T')]
one=ring['one']
reps=[one,W,Wp,A,V,P,S,D,T]
base=[A,V,P,D]

@lru_cache(None)
def sym(n):
    assert n>=0
    return tuple(ring['sym'](n,x) for x in W)


def effective(chi):
    coeff=[inner(chi,r) for r in reps]
    return all(b==0 and a>=0 and a.denominator==1 for a,b in coeff)


def module(coeff):
    return va(*[vs(c,r) for c,r in zip(coeff,base)])


H=va(*[vs(2,r) for r in base])
M3=va(vs(3,Wp),vs(3,S),vs(6,T))
M4=va(vs(2,V),vs(4,P),vs(3,D))
actual_h1=va(vm(W,M4),vs(-1,M3))
assert actual_h1==va(Wp,vs(3,T))
assert H==va(vm(W,M3),vs(-1,va(A,vs(2,V),vs(3,P),vs(4,D))),vs(-1,M4))

# Dimension-17 possible submodules and both injection conditions.
u17=[c for c in product(range(3),repeat=4)
     if sum(a*b for a,b in zip(c,(3,3,4,5)))==17]
assert u17==[(0,1,1,2),(1,0,1,2),(1,2,2,0),(2,1,2,0),(2,2,0,1)]
expected_injections={
    (32,22):([2],[1,3,4]), (34,20):([1],[3,4]),
    (36,18):([1,3],[5]), (38,16):([1,2],[4]),
    (42,12):([1,2,3,4,5],[]),
}
for DC,DB in pair_lists[1,1]:
    lower=[];upper=[]
    for i,c in enumerate(u17,1):
        U=module(c);Z=va(H,vs(-1,U))
        if effective(va(sym(DC+1),vs(-1,vm(W,U)))):
            lower.append(i)
        if effective(va(sym(DB),vs(-1,Z))):
            upper.append(i)
    assert (lower,upper)==expected_injections[DC,DB]
    assert not set(lower)&set(upper)

# Dimension-18 module, upper injection, and final actual cohomology mismatch.
u18=[c for c in product(range(3),repeat=4)
     if sum(a*b for a,b in zip(c,(3,3,4,5)))==18]
assert u18==[(0,0,2,2),(1,2,1,1),(2,1,1,1)]
assert list(sym(12))==va(one,A,P,D)
assert list(sym(16))==va(V,P,vs(2,D))
forced={}
for DC,DB in pair_lists[1,2]:
    allowed=[c for c in u18
             if effective(va(sym(DB),vs(-1,va(H,vs(-1,module(c))))))]
    assert len(allowed)==1
    forced[DC]=module(allowed[0])
assert forced[38]==va(vs(2,A),V,P,D)
assert forced[42]==va(A,vs(2,V),P,D)
assert max(18*(d-32) for d in [38,42])==180<16*12
predicted={}
for DC,DB in pair_lists[1,2]:
    # The last adjacent rank-one derivative is unramified.
    a17,a18=DC//2-1,DC//2+1
    assert a17+a18==DC and a18-a17==2
    RC1=va(sym(a17+1),sym(a18+1))
    C1=va(RC1,vs(-1,vm(W,forced[DC])))
    predicted[DC]=va(C1,sym(DB-3))
    assert predicted[DC]!=actual_h1
assert predicted[38]==va(W,Wp,S,vs(2,T))
assert predicted[42]==va(W,vs(3,S),T)

# Optional independent full-vector/character refinement.
def euler_line(a):
    if a>=0:
        return list(sym(a))
    if a<=-2:
        return vs(-1,sym(-a-2))
    return vs(0,one)

f38=list(full_flags(18,16,38))
f42=list(full_flags(18,16,42))
assert len(f38)==2 and len(f42)==11
assert {tuple((j,d) for j,d in enumerate(ds,1) if d) for ds,aa in f38}=={
    ((1,54),),((1,30),(2,12))}
chars38=[va(*[euler_line(a) for a in aa]) for ds,aa in f38]
assert all(ch in [va(one,A,P,vs(2,D)),va(one,V,P,vs(2,D))] for ch in chars38)
matching42=[(ds,aa) for ds,aa in f42
            if va(*[euler_line(a) for a in aa])==forced[42]]
assert len(matching42)==1
assert matching42[0][0]==(30,12,12)+(0,)*14
assert matching42[0][1]==(-66,-34,-20,-6,-4,-2,0,2,4,6,8,10,12,14,16,18,20,22)

print('PASS: full even-integer flag arithmetic excludes every nonorthogonal endpoint case.')
print('PASS: invariant projection torsion vanishes in the remaining short profiles.')
print('PASS: orthogonal (2,1) violates complete-flag parity.')
print('PASS: every orthogonal (1,1) pair violates necessary representation embeddings.')
print('PASS: both orthogonal (1,2) pairs contradict actual H1(E(1))=Wprime+3T6.')
print('PASS: independent complete-vector character refinement (2 and 11 vectors).')
print('CONCLUSION WITH THE PROVED GEOMETRIC LEMMAS: generic SF rank >=3; positive-square rank >=27.')
print('NOT PROVED: maximal SF rank 13, square surjectivity, smoothing closure, or a new generic section count.')
