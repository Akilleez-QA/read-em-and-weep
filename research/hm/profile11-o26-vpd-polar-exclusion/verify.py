#!/usr/bin/env python3
"""Exact checks of declared universal identities and twelve stated supports.

No support enumerator, source instance, source coefficient, point, derivative,
matrix, geometric rank evaluation, model, numerical envelope, or large search.
Completeness of the supports is the human two-case proof in PROOF.md.
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


def require(condition, label):
    if not condition:
        raise AssertionError(label)

def equal(actual, expected, label):
    require(actual == rep(expected), label)

dimensions = {n: int(chars[n][0][0]) for n in names}
parity = {n: (1 if n in ('W', 'Wp', 'S', 'T') else 0) for n in names}
B = rep('A+P+2D')

equal(sym(28), 'A+V+2P+3D', 'Sym28')
equal(vm(rep('V+P+D'), W), 'Wp+S+3T', 'top tensor W')
equal(sym(29), 'W+Wp+2S+3T', 'Sym29')
equal(vs(sym(28), rep('V+P+D')), 'A+P+2D', 'H1 budget')
require(vs(vm(rep('V+P+D'), W), sym(29)) == vk(-1, rep('W+S')), 'Euler budget')

# Every atom permitted by parity and (j-3)*dim U <= 17 is declared below.
# Tuples are (U, j, b, t, admissible); these are identities, not supports.
ATOMS = [
    ('one',4,'one','0',False),
    ('one',6,'A','W',True),
    ('one',8,'D','S',True),
    ('one',10,'V+P','T',False),
    ('one',12,'P+D','Wp+T',True),
    ('one',14,'A+V+D','S+T',False),
    ('one',16,'one+A+P+D','W+S+T',False),
    ('one',18,'A+V+P+D','W+Wp+S+T',False),
    ('one',20,'V+P+2D','S+2T',False),
    ('A',4,'A','0',True),
    ('A',6,'one+A+D','W+S',False),
    ('A',8,'A+V+P+D','W+S+T',False),
    ('V',4,'V','0',False),
    ('V',6,'P+D','T',True),
    ('V',8,'A+V+P+D','Wp+S+T',False),
    ('P',4,'P','0',True),
    ('P',6,'V+P+D','Wp+T',False),
    ('D',4,'D','0',True),
    ('D',6,'A+V+P+D','S+T',False),
    ('W',5,'one+A','W',False),
    ('W',7,'A+D','W+S',True),
    ('W',9,'V+P+D','S+T',False),
    ('W',11,'V+2P+D','Wp+2T',False),
    ('Wp',5,'P','Wp',True),
    ('Wp',7,'V+D','T',False),
    ('Wp',9,'A+P+D','S+T',True),
    ('Wp',11,'one+A+V+P+D','W+Wp+S+T',False),
    ('S',5,'A+D','S',True),
    ('S',7,'one+A+V+P+D','W+S+T',False),
    ('T',5,'V+P+D','T',False),
]
declared = {(u,j) for u,j,*_ in ATOMS}
bounded = {(u,j) for u in names for j in range(4,21)
           if j % 2 == parity[u] and (j-3)*dimensions[u] <= 17}
require(len(ATOMS) == len(declared) == 30 and declared == bounded,
        'complete 30-atom dimension/parity boundary')
good = set()
for u,j,b,t,admissible in ATOMS:
    actual_b = vm(chars[u], sym(j-4))
    actual_t = vm(chars[u], sym(j-5)) if j>=5 else ZERO
    equal(actual_b,b,f'b({u},{j})')
    equal(actual_t,t,f't({u},{j})')
    is_good = all(0 <= x <= y for x,y in zip(dec(actual_b),dec(B)))
    require(is_good == admissible, f'admissibility({u},{j})')
    if admissible:
        good.add((u,j))
require(len(good)==11, 'eleven admissible atoms')

# Each tuple is (representation, j, multiplicity). All supports are explicit.
SUPPORTS = [
    [('P',4,1),('D',4,1),('one',6,1),('one',8,1)],
    [('S',3,1),('P',4,1),('one',6,1),('one',8,2)],
    [('Wp',3,1),('D',4,1),('Wp',5,1),('one',6,1),('one',8,1)],
    [('Wp',3,1),('S',3,1),('Wp',5,1),('one',6,1),('one',8,2)],
    [('Wp',3,1),('T',3,1),('one',6,1),('one',8,1),('one',12,1)],
    [('T',3,1),('V',6,1),('one',6,1),('one',8,1)],
    [('P',4,1),('D',4,1),('W',7,1)],
    [('S',3,1),('P',4,1),('W',7,1),('one',8,1)],
    [('Wp',3,1),('D',4,1),('Wp',5,1),('W',7,1)],
    [('Wp',3,1),('S',3,1),('Wp',5,1),('W',7,1),('one',8,1)],
    [('Wp',3,1),('T',3,1),('W',7,1),('one',12,1)],
    [('T',3,1),('V',6,1),('W',7,1)],
]
for i, support in enumerate(SUPPORTS,1):
    h1, chi = ZERO, ZERO
    rank = degree = 0
    for u,j,m in support:
        require(j>=3 and m>0 and j%2==parity[u], f'K{i} H0/parity')
        rank += m*dimensions[u]
        degree -= j*m*dimensions[u]
        if j==3:
            chi=va(chi,vk(m,chars[u]))
        else:
            require((u,j) in good, f'K{i} admissible atom')
            h1=va(h1,vk(m,vm(chars[u],sym(j-4))))
            if j>=5:
                chi=vs(chi,vk(m,vm(chars[u],sym(j-5))))
    require(h1==B and chi==vk(-1,rep('W+S')), f'K{i} budgets')
    require((rank,degree)==(11,-50), f'K{i} rank/degree')

equal(sym(6),'V+P','Sym6 Hom identity')
equal(vm(chars['V'],W),'T','V tensor W')
equal(vm(W,W),'one+A','W tensor W')

def hom_dimension(u,j,r,k):
    if j<k:
        return 0
    return dec(vm(chars[r],sym(j-k)))[names.index(u)]

TARGETS = {'Q3':[('V',6),('one',10),('one',12)],
           'Q12':[('V',6),('W',11)]}
EXPECTED_ATOMIC = {
    'Q3': {('V',6,'V',6):1, ('one',12,'V',6):1, ('one',12,'one',12):1},
    'Q12': {('V',6,'V',6):1, ('one',12,'V',6):1, ('one',12,'W',11):1},
}
source_atoms = {(u,j) for support in SUPPORTS for u,j,m in support}
require(len(source_atoms)==11,'eleven source atom types')
for target_name, target in TARGETS.items():
    actual_atomic = {}
    for u,j in source_atoms:
        for r,k in target:
            dim=hom_dimension(u,j,r,k)
            require(dim>=0,'nonnegative Hom multiplicity')
            if dim:
                actual_atomic[(u,j,r,k)]=dim
    require(actual_atomic==EXPECTED_ATOMIC[target_name],
            f'{target_name} complete atomic Hom list')
    for i,support in enumerate(SUPPORTS,1):
        hom_total=sum(m*hom_dimension(u,j,r,k) for u,j,m in support for r,k in target)
        expected=2 if i in (5,11) else 1 if i in (6,12) else 0
        require(hom_total==expected,f'K{i} -> {target_name} dimension')

print('PASS: exact source cohomology identities; all 30 declared bounded atoms;')
print('11 admissible atoms; 12 declared supports with rank 11 and degree -50;')
print('complete atomic Hom lists and all 24 support/target Hom dimensions.')
print('Support completeness is proved by the two-case argument, not enumerated.')

# The two actual first-polar character alternatives and universal polar channels.
for source, j, expected_linear in [("V",6,"Wp+T"),("one",12,"T")]:
    c=vs(B,vm(chars[source],sym(j-4)))
    linear=vs(vs(sym(29),vm(chars[source],sym(j-5))),vm(W,c))
    equal(c,"A+D","constant coefficient")
    equal(linear,expected_linear,"linear coefficient")
equal(vm(chars["V"],chars["A"]),"P+D","no V-to-A quadratic channel")
equal(vm(chars["P"],chars["A"]),"V+P+D","no P-to-A quadratic channel")
equal(vm(chars["D"],chars["A"]),"A+V+P+D","D quadratic channels")
equal(sym(8),"P+D","Sym8 contraction source")
equal(sym(7),"Wp+T","Sym7 contraction target")
require([(u,v,hom_dimension(u,2,v,1)) for u in ("V","P","D") for v in ("Wp","T")] == [("V","Wp",0),("V","T",1),("P","Wp",1),("P","T",1),("D","Wp",0),("D","T",1)],"all six linear polar channels")
print("PASS: both first-polar splittings and all universal quadratic/linear channels.")
