#!/usr/bin/env python3
"""Only the universal character identities used by the tail-rank proof.
No source coefficients, points, matrices, derivatives, ranks, or enumeration.
"""
#!/usr/bin/env python3
"""Universal binary-icosahedral characters in exact Q(sqrt(5)) arithmetic.

Character definitions only. No source-specific budget, atoms, support table,
source instances, source coefficients, models, points, or geometric evaluation.
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

M2=rep('A+2V+3P+4D'); M3=rep('3Wp+3S+6T'); M4=rep('2V+4P+3D')
assert vs(vs(vm(M3,W),M2),M4)==rep('2A+2V+2P+2D')
assert sym(10)==rep('A+V+D')
Hbar=rep('A+V+2P+D')
for text,expected in [('A+P','V+P+D'),('A+D','V+2P'),('P+D','A+V+P'),('V+P','A+P+D')]:
    C1=rep(text); B=vs(Hbar,C1)
    assert B==rep(expected)
    assert 7<=C1[0][0]<=9 and B[0][0]>=10
    assert dec(B)[names.index('P')]>=1
assert inner(chars['P'],sym(10))==q(0)
print('PASS: ambient character, all four possible constant quotients, their P constituents, and the degree-ten obstruction.')
print('The rank-drop exclusion is proved by exact fibers and exterior-square degree, not computed on a source instance.')
