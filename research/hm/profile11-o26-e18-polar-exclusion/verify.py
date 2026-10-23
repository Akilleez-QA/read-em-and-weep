#!/usr/bin/env python3
"""Bounded exact checks: 31 atoms, 17 declared splittings, 60 Hom channels.

No source instances, source matrices, points, geometric rank evaluations,
splitting enumerator, all-twist scan, network access, or external files.
"""
from fractions import Fraction as Q
from functools import lru_cache

# Exact Q(sqrt(5)) arithmetic: (a,b) denotes a+b*sqrt(5).
def q(a, b=0): return (Q(a), Q(b))
def plus(x, y): return (x[0]+y[0], x[1]+y[1])
def times(x, y): return (x[0]*y[0]+5*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def scale(k, x): return (k*x[0], k*x[1])
def total(xs):
    out = q(0)
    for x in xs: out = plus(out, x)
    return out
ZERO = (q(0),)*9
def va(x, y): return tuple(plus(a,b) for a,b in zip(x,y))
def vk(k, x): return tuple(scale(k,a) for a in x)
def vm(x, y): return tuple(times(a,b) for a,b in zip(x,y))
def vs(x, y): return va(x,vk(-1,y))
phi, phip = q(Q(1,2),Q(1,2)), q(Q(1,2),-Q(1,2))
W = (q(2),q(-2),phi,scale(-1,phi),phip,scale(-1,phip),q(1),q(-1),q(0))
sizes = (1,1,12,12,12,12,20,20,30)
@lru_cache(None)
def sym(n):
    assert n >= 0
    a = (q(1),)*9
    if n == 0: return a
    b = W
    for _ in range(2,n+1): a,b = b,vs(vm(W,b),a)
    return b
chars = {"one":sym(0),"W":W,"A":sym(2),"S":sym(3),"D":sym(4),"T":sym(5)}
chars["P"] = tuple(map(q,(4,4,-1,-1,-1,-1,1,1,0)))
chars["V"] = vs(sym(6),chars["P"])
chars["Wp"] = vs(vm(W,chars["P"]),chars["T"])
names = ("one","W","Wp","A","V","P","S","D","T")
def inner(x,y): return scale(Q(1,120),total(scale(k,times(a,b)) for k,a,b in zip(sizes,x,y)))
assert all(inner(chars[a],chars[b]) == q(a==b) for a in names for b in names)
def rep(text):
    out = ZERO
    if text == "0": return out
    for term in text.split("+"):
        k = int(term[0]) if term[0].isdigit() else 1
        name = term[1:] if term[0].isdigit() else term
        out = va(out,vk(k,chars[name]))
    return out
def dec(x):
    out = [inner(x,chars[n]) for n in names]
    assert all(b==0 and a.denominator==1 for a,b in out)
    return tuple(int(a) for a,b in out)
B, C = rep("A+V+2P+D"), rep("W+Wp+T")
budget = dec(B)

# The complete eligible-atom table is declared, not searched.
allowed = [
 (2,"A","A","0"),(2,"V","V","0"),(2,"P","P","0"),(2,"D","D","0"),
 (3,"Wp","P","Wp"),(3,"S","A+D","S"),(3,"T","V+P+D","T"),
 (4,"one","A","W"),(4,"V","P+D","T"),(4,"P","V+P+D","Wp+T"),
 (4,"D","A+V+P+D","S+T"),(5,"W","A+D","W+S"),(5,"Wp","V+D","T"),
 (6,"one","D","S"),(6,"A","A+V+P+D","W+S+T"),
 (6,"V","A+V+P+D","Wp+S+T"),(7,"W","V+P+D","S+T"),
 (7,"Wp","A+P+D","S+T"),(8,"one","V+P","T"),
 (9,"W","V+2P+D","Wp+2T"),(10,"one","P+D","Wp+T"),
 (12,"one","A+V+D","S+T"),(16,"one","A+V+P+D","W+Wp+S+T"),
 (20,"one","A+V+2P+D","Wp+S+2T")]
rejected = [
 (2,"one","one"),(14,"one","one+A+P+D"),(18,"one","V+P+2D"),
 (4,"A","one+A+D"),(3,"W","one+A"),
 (9,"Wp","one+A+V+P+D"),(5,"S","one+A+V+P+D")]
eligible = {(a,"one") for a in range(2,21,2)}
eligible |= {(a,R) for R in ("A","V") for a in (2,4,6)}
eligible |= {(a,R) for R in ("P","D") for a in (2,4)}
eligible |= {(a,R) for R in ("W","Wp") for a in (3,5,7,9)}
eligible |= {(a,"S") for a in (3,5)} | {(3,"T")}
assert len(eligible)==31
assert {(a,R) for a,R,_,_ in allowed}.isdisjoint({(a,R) for a,R,_ in rejected})
assert {(a,R) for a,R,_,_ in allowed} | {(a,R) for a,R,_ in rejected} == eligible
for a,R,b,t in allowed:
    actual = vm(chars[R],sym(a-2))
    assert actual == rep(b)
    assert all(0<=x<=y for x,y in zip(dec(actual),budget))
    assert (ZERO if a==2 else vm(chars[R],sym(a-3))) == rep(t)
for a,R,b in rejected:
    actual = vm(chars[R],sym(a-2))
    assert actual == rep(b)
    assert not all(0<=x<=y for x,y in zip(dec(actual),budget))
assert {(a,R) for a,R,_,t in allowed if dec(rep(t))[names.index("W")]} == {
    (4,"one"),(5,"W"),(6,"A"),(16,"one")}

# Each pair (m,R) means R tensor O(-m) in K0, not L.
candidates = [
 [(6,"one"),(4,"D"),(10,"one"),(5,"Wp")],
 [(6,"one"),(5,"T"),(5,"Wp")],
 [(6,"one"),(6,"V"),(4,"V"),(5,"Wp")],
 [(6,"one"),(6,"P"),(4,"P")],
 [(6,"one"),(6,"P"),(5,"Wp"),(3,"Wp")],
 [(6,"one"),(7,"Wp"),(4,"P"),(5,"Wp")],
 [(6,"one"),(7,"Wp"),(5,"Wp"),(5,"Wp"),(3,"Wp")],
 [(6,"one"),(8,"one"),(10,"one"),(5,"Wp"),(3,"S")],
 [(6,"one"),(9,"W"),(5,"Wp"),(3,"S")],
 [(6,"one"),(11,"W"),(3,"T")],
 [(6,"one"),(12,"one"),(4,"V"),(4,"P")],
 [(6,"one"),(12,"one"),(4,"V"),(5,"Wp"),(3,"Wp")],
 [(6,"one"),(12,"one"),(10,"one"),(3,"T")],
 [(7,"W"),(10,"one"),(5,"Wp"),(3,"S")],
 [(8,"A"),(5,"Wp"),(3,"S")],
 [(18,"one"),(4,"P"),(3,"S")],
 [(18,"one"),(5,"Wp"),(3,"Wp"),(3,"S")]]
assert len({tuple(sorted(row)) for row in candidates}) == 17
for row in candidates:
    h1, chi3 = ZERO, ZERO
    rank, degree = 0, 0
    for m,R in row:
        assert m >= 3  # H0(K0(2)) is zero.
        dim = chars[R][0][0]
        rank += dim
        degree -= m*dim
        if m >= 4: h1 = va(h1,vm(chars[R],sym(m-4)))
        if m == 3: chi3 = va(chi3,chars[R])
        elif m >= 5: chi3 = vs(chi3,vm(chars[R],sym(m-5)))
    assert rank == 9 and degree == -46
    assert h1 == B and chi3 == vk(-1,C)
print("PASS: 31 bounded atom identities; 24 admissible and 7 rejected; all 17 declared supports satisfy the exact input identities.")
print("Completeness is the four-case budget proof in PROOF.md Section 3, not an enumeration claim.")

# Global equivariant Hom channels to Q = Wp_5 + V_6 + 2*one_10.
# Each asserted multiplicity below is PER target copy.
targets = [(5,"Wp",1),(6,"V",1),(10,"one",2)]
sources = {source for row in candidates for source in row}
assert len(sources) == 20
nonzero_channels = {
 ((5,"Wp"),(5,"Wp")): 1,
 ((6,"P"),(5,"Wp")): 1,
 ((6,"V"),(6,"V")): 1,
 ((10,"one"),(10,"one")): 1,
 ((11,"W"),(5,"Wp")): 1,
 ((11,"W"),(6,"V")): 1,
 ((11,"W"),(10,"one")): 1,
 ((12,"one"),(5,"Wp")): 1,
 ((12,"one"),(6,"V")): 1,
 ((18,"one"),(5,"Wp")): 1,
}
for m,R in sources:
    for n,U,_ in targets:
        value = q(0) if m<n else inner(chars[R],vm(chars[U],sym(m-n)))
        assert value == q(nonzero_channels.get(((m,R),(n,U)),0))
hom_dimensions = [sum(copies*nonzero_channels.get((source,(n,U)),0)
                      for source in row for n,U,copies in targets)
                  for row in candidates]
assert hom_dimensions == [3,1,2,1,2,1,2,3,1,4,2,3,4,3,1,1,2]
print("PASS: all 60 atomic Hom channels and all 17 total Hom dimensions; 10 atomic channels are nonzero, each one-dimensional per target copy.")

# First-polar characters for exactly the eleven declared image types.
image_rows = [
 ([], "A+V+2P+D", "-Wp-T", 11, 8),
 ([(5,"Wp")], "A+V+P+D", "-Wp", 13, 2),
 ([(6,"V")], "A+V+P", "S", 14, -4),
 ([(10,"one")], "A+P+D", "0", 12, 0),
 ([(12,"one")], "A+V+P", "S-Wp", 12, -2),
 ([(18,"one")], "P", "S+T-Wp", 12, -8),
 ([(5,"Wp"),(6,"V")], "A+V", "S+T", 16, -10),
 ([(5,"Wp"),(10,"one")], "A+D", "T", 14, -6),
 ([(5,"Wp"),(12,"one")], "A+V", "S+T-Wp", 14, -8),
 ([(10,"one"),(12,"one")], "A", "S+T", 13, -10),
 ([(11,"W")], "A", "S+T", 13, -10)]
def signed_rep(text):
    out=ZERO
    for term in text.replace("-","+-").split("+"):
        if term: out=va(out,vk(-1,rep(term[1:])) if term.startswith("-") else rep(term))
    return out
for parts,ct,lt,r,d in image_rows:
    c=vs(sym(28),rep("2D")); h3=ZERO
    for m,R in parts:
        c=vs(c,vm(chars[R],sym(m-4)))
        h3=va(h3,vm(chars[R],sym(m-5)))
    ell=vs(vs(sym(29),h3),vm(W,c))
    assert c==rep(ct) and ell==signed_rep(lt)
    assert r==11+sum(chars[R][0][0] for m,R in parts)
    assert d==8+sum((2-m)*chars[R][0][0] for m,R in parts)
assert [inner(sym(n),chars["one"])[0] for n in range(0,29,2)] == [1,0,0,0,0,0,1,0,0,0,1,0,1,0,0]
assert sym(6)==rep("V+P")
assert inner(vm(chars["D"],sym(2)),chars["A"])==q(1)
assert inner(vm(chars["D"],sym(2)),chars["D"])==q(1)
assert inner(vm(chars["D"],W),chars["S"])==q(1)
assert inner(vm(chars["D"],W),chars["T"])==q(1)
print("PASS: all eleven first-polar characters, ranks and degrees; low invariant degrees and the two D channels.")
