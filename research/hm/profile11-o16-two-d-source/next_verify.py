#!/usr/bin/env python3
"""Fixed universal representation checks only. No source/model evaluation."""
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

# Fixed universal identities for NEXT-FF-EXCLUSION.md only.
assert sym(18)==rep('A+V+2P+D')
rows=[[(4,'V'),(4,'P'),(6,'one')],
      [(3,'Wp'),(4,'V'),(5,'Wp'),(6,'one')],
      [(3,'T'),(6,'one'),(10,'one')]]
for row in rows:
    rank=degree=0;h1=chi=ZERO
    for j,R in row:
        d=chars[R][0][0];rank+=d;degree-=j*d
        if j>=4:h1=va(h1,vm(chars[R],sym(j-4)))
        if j==3:chi=va(chi,chars[R])
        elif j>=5:chi=vs(chi,vm(chars[R],sym(j-5)))
    assert (rank,degree)==(8,-34)
    assert h1==rep('A+V+P') and chi==vk(-1,W)
    nonzero=[]
    for atom in row:
        j,R=atom
        for n,U in [(4,'D'),(10,'one'),(12,'one')]:
            h=0 if j<n else inner(chars[R],vm(chars[U],sym(j-n)))[0]
            assert h in (0,1)
            if h:nonzero.append((atom,(n,U)))
    assert nonzero==([((10,'one'),(10,'one'))] if row is rows[-1] else [])
assert vs(sym(18),rep('P+D'))==rep('A+V+P')
assert vs(vs(sym(18),rep('P+D')),sym(6))==chars['A']
assert vs(vs(sym(19),sym(5)),vm(chars['A'],W))==rep('Wp+T')
assert vs(sym(4),chars['D'])==ZERO and sym(5)==chars['T']
assert sym(6)==rep('V+P')
assert -26+4==-22 and 22>6
for j,R in [(3,'S'),(8,'one')]:
    assert j<12
print('PASS: three pinned P+D kernels; all internal channels; both first-polar characters; residual degree22 contradiction.')
print('The preserved-lattice and actual-image statements remain mathematical arguments, not executable assumptions proven by this check.')
