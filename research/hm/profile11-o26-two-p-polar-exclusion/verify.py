#!/usr/bin/env python3
"""Exact universal checks for the O26 delta-zero U6/U13 kernel budget.

29 declared bounded atoms, 6 declared supports, 36 distinct atomic Hom channels.
No support enumerator, geometric model, source coefficients, source matrices,
point evaluation, source-instance ranks, scan, or old numerical envelope.
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


B=rep('A+V+2D')
chi3=vs(chars['Wp'],rep('W+S'))
budget=dec(B)
allowed=[
 (6,'one','A','W'),(8,'one','D','S'),(14,'one','A+V+D','S+T'),
 (4,'A','A','0'),(4,'V','V','0'),(4,'D','D','0'),
 (7,'W','A+D','W+S'),(7,'Wp','V+D','T'),(5,'S','A+D','S'),
]
rejected=[
 (4,'one','one'),(10,'one','V+P'),(12,'one','P+D'),
 (16,'one','one+A+P+D'),(18,'one','A+V+P+D'),
 (6,'A','one+A+D'),(8,'A','A+V+P+D'),
 (6,'V','P+D'),(8,'V','A+V+P+D'),
 (4,'P','P'),(6,'P','V+P+D'),(6,'D','A+V+P+D'),
 (5,'W','one+A'),(9,'W','V+P+D'),(11,'W','V+2P+D'),
 (5,'Wp','P'),(9,'Wp','A+P+D'),(11,'Wp','one+A+V+P+D'),
 (7,'S','one+A+V+P+D'),(5,'T','V+P+D'),
]
# Completeness of the 29-atom degree bound is checked only over m<=19,
# the universal maximum from (m-3)*dim(R)<=16. This is not a support search.
eligible={(m,R) for R in names for m in range(4,20)
          if chars[R][1][0]==((-1)**m)*chars[R][0][0]
          and (m-3)*chars[R][0][0]<=16}
assert len(eligible)==29
assert {(m,R) for m,R,_,_ in allowed}.isdisjoint({(m,R) for m,R,_ in rejected})
assert {(m,R) for m,R,_,_ in allowed}|{(m,R) for m,R,_ in rejected}==eligible
assert len(allowed)==9 and len(rejected)==20
for m,R,b,t in allowed:
    actual=vm(chars[R],sym(m-4))
    assert actual==rep(b)
    assert all(0<=x<=y for x,y in zip(dec(actual),budget))
    assert (ZERO if m==4 else vm(chars[R],sym(m-5)))==rep(t)
for m,R,b in rejected:
    actual=vm(chars[R],sym(m-4))
    assert actual==rep(b)
    assert not all(0<=x<=y for x,y in zip(dec(actual),budget))
assert {(m,R) for m,R,_,t in allowed if dec(rep(t))[names.index('W')]}=={(6,'one'),(7,'W')}
print('PASS: all 29 bounded atoms; exactly 9 admissible and 20 rejected.')

supports=[
 [(3,'Wp'),(4,'V'),(4,'D'),(6,'one'),(8,'one')],
 [(3,'Wp'),(3,'S'),(4,'V'),(6,'one'),(8,'one'),(8,'one')],
 [(3,'Wp'),(3,'T'),(6,'one'),(7,'Wp'),(8,'one')],
 [(3,'Wp'),(4,'V'),(4,'D'),(7,'W')],
 [(3,'Wp'),(3,'S'),(4,'V'),(7,'W'),(8,'one')],
 [(3,'Wp'),(3,'T'),(7,'W'),(7,'Wp')],
]
assert len({tuple(sorted(row)) for row in supports})==6
for row in supports:
    h1,chi=ZERO,ZERO
    rank,degree=0,0
    for m,R in row:
        assert m>=3
        dim=chars[R][0][0]
        assert chars[R][1][0]==((-1)**m)*dim
        rank+=dim; degree-=m*dim
        if m>=4: h1=va(h1,vm(chars[R],sym(m-4)))
        if m==3: chi=va(chi,chars[R])
        elif m>=5: chi=vs(chi,vm(chars[R],sym(m-5)))
    assert h1==B and chi==chi3
    assert rank==12 and degree==-52
print('PASS: all 6 declared supports satisfy the exact identities, rank 12, degree -52.')
print('Completeness is the two-case human budget proof in PROOF.md, not an enumeration claim.')

sources={source for row in supports for source in row}
targets={(7,'Wp'),(10,'one'),(12,'one'),(11,'W')}
assert len(sources)==9 and len(targets)==4
nonzero={((7,'Wp'),(7,'Wp')):1}
for m,R in sources:
    for n,U in targets:
        value=q(0) if m<n else inner(chars[R],vm(chars[U],sym(m-n)))
        assert value==q(nonzero.get(((m,R),(n,U)),0))
for target in [[(7,'Wp'),(10,'one'),(12,'one')],[(7,'Wp'),(11,'W')]]:
    dimensions=[sum(nonzero.get((source,t),0) for source in row for t in target) for row in supports]
    assert dimensions==[0,0,1,0,0,1]
print('PASS: all 36 distinct atomic Hom channels; only Wp_7 -> Wp_7 is nonzero.')
print('PASS: for both U6 and U13, the 6 Hom dimensions are [0,0,1,0,0,1].')

# The first-polar characters and the three one-dimensional linear channels.
assert vs(sym(28),rep("2P+D"))==B
assert vs(vm(rep("2P+D"),W),sym(29))==chi3
c=vs(B,vm(chars["Wp"],sym(3)))
ell=vs(vs(sym(29),vm(chars["Wp"],sym(2))),vm(c,W))
assert c==rep("A+D") and ell==rep("Wp+T")
assert sym(8)==rep("P+D") and sym(7)==rep("Wp+T")
assert vm(chars["P"],W)==rep("Wp+T")
assert vm(chars["D"],W)==rep("S+T")
assert [(U,V,inner(chars[U],vm(chars[V],W))) for U in ("P","D") for V in ("Wp","T")] == [("P","Wp",q(1)),("P","T",q(1)),("D","Wp",q(0)),("D","T",q(1))]
print("PASS: first-polar constant/linear characters and all three contraction channels.")
