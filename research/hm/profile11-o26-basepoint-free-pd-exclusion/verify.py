#!/usr/bin/env python3
"""Bounded universal checks for the O26 delta-zero E6/E13 kernel budgets.

34 declared atoms, 25 declared supports, 84 declared atomic Hom dimensions.
No support enumerator, all-twist envelope, actual coefficients, selected points,
selected matrices, source-instance ranks, model experiments, or large computation.
Completeness is proved by the five-case human argument in PROOF.md.
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


B=rep('A+V+P+2D')
chi3=vk(-1,rep('W+S+T'))
budget=dec(B)
assert sym(28)==rep('A+V+2P+3D')
assert sym(29)==rep('W+Wp+2S+3T')
assert vm(W,rep('P+D'))==rep('Wp+S+2T')
assert vs(sym(28),rep('P+D'))==B
assert vs(vm(W,rep('P+D')),sym(29))==chi3

allowed=[
 (6,'one','A','W'), (8,'one','D','S'),
 (10,'one','V+P','T'), (12,'one','P+D','Wp+T'),
 (14,'one','A+V+D','S+T'), (18,'one','A+V+P+D','W+Wp+S+T'),
 (20,'one','V+P+2D','S+2T'),
 (4,'A','A','0'), (8,'A','A+V+P+D','W+S+T'),
 (4,'V','V','0'), (6,'V','P+D','T'), (8,'V','A+V+P+D','Wp+S+T'),
 (4,'P','P','0'), (6,'P','V+P+D','Wp+T'), (8,'P','A+V+P+2D','S+2T'),
 (4,'D','D','0'), (6,'D','A+V+P+D','S+T'),
 (7,'W','A+D','W+S'), (9,'W','V+P+D','S+T'), (13,'W','A+V+P+2D','Wp+S+2T'),
 (5,'Wp','P','Wp'), (7,'Wp','V+D','T'), (9,'Wp','A+P+D','S+T'),
 (13,'Wp','A+V+P+2D','W+S+2T'),
 (5,'S','A+D','S'), (5,'T','V+P+D','T'),
]
rejected=[
 (4,'one','one'), (16,'one','one+A+P+D'), (22,'one','A+V+2P+D'),
 (6,'A','one+A+D'), (5,'W','one+A'), (11,'W','V+2P+D'),
 (11,'Wp','one+A+V+P+D'), (7,'S','one+A+V+P+D'),
]
# These ranges are explicitly declared from the current bound, not imported.
declared_ranges={
 'one':(4,6,8,10,12,14,16,18,20,22),
 'A':(4,6,8), 'V':(4,6,8), 'P':(4,6,8), 'D':(4,6),
 'W':(5,7,9,11,13), 'Wp':(5,7,9,11,13), 'S':(5,7), 'T':(5,),
}
for R,indices in declared_ranges.items():
    dim=chars[R][0][0]
    # j<=23 follows from (j-3)*dim R<=20 and dim R>=1.
    bounded=tuple(j for j in range(4,24)
                  if (j-3)*dim<=20 and chars[R][1][0]==(-1)**j*dim)
    assert indices==bounded
eligible={(j,R) for R,indices in declared_ranges.items() for j in indices}
a={(j,R) for j,R,_,_ in allowed}; r={(j,R) for j,R,_ in rejected}
assert len(eligible)==34 and len(a)==26 and len(r)==8
assert not a&r and a|r==eligible
for j,R,b,t in allowed:
    actual=vm(chars[R],sym(j-4))
    assert actual==rep(b)
    assert all(0<=x<=y for x,y in zip(dec(actual),budget))
    assert (ZERO if j==4 else vm(chars[R],sym(j-5)))==rep(t)
for j,R,b in rejected:
    actual=vm(chars[R],sym(j-4))
    assert actual==rep(b)
    assert not all(0<=x<=y for x,y in zip(dec(actual),budget))
W_atoms={(j,R) for j,R,_,t in allowed if dec(rep(t))[names.index('W')]}
assert W_atoms=={(6,'one'),(7,'W'),(18,'one'),(8,'A'),(13,'Wp')}
for j,R,b,t in allowed:
    if (j,R) in W_atoms:
        assert dec(rep(b))[names.index('A')]==1
        assert dec(rep(t))[names.index('W')]==1
print('PASS: input character budgets and all 34 bounded atoms (26 allowed, 8 rejected).')
print('PASS: exactly the five declared W-contributing atoms, each consuming the unique A.')

# Exactly the nine residual blocks written in the human proof, not searched.
residuals=[
 ([(9,'W')],'S'),
 ([(10,'one'),(4,'D')],'0'),
 ([(10,'one'),(8,'one')],'S'),
 ([(12,'one'),(4,'V')],'Wp'),
 ([(6,'V'),(4,'V')],'0'),
 ([(6,'P')],'Wp'),
 ([(7,'Wp'),(4,'P')],'0'),
 ([(7,'Wp'),(5,'Wp')],'Wp'),
 ([(5,'T')],'0'),
]
for row,C in residuals:
    b,t=ZERO,ZERO
    for j,R in row:
        b=va(b,vm(chars[R],sym(j-4)))
        if j>=5: t=va(t,vm(chars[R],sym(j-5)))
    assert b==rep('V+P+D')
    assert vs(t,chars['T'])==rep(C)
print('PASS: all 9 declared residual blocks and their degree-minus-three coefficients.')

# All 25 supports are explicitly declared in the same order as PROOF.md.
supports=[
 [(3,'S'),(6,'one'),(8,'one'),(9,'W')],
 [(4,'D'),(6,'one'),(8,'one'),(10,'one')],
 [(3,'S'),(6,'one'),(8,'one'),(8,'one'),(10,'one')],
 [(3,'Wp'),(4,'V'),(6,'one'),(8,'one'),(12,'one')],
 [(4,'V'),(6,'one'),(6,'V'),(8,'one')],
 [(3,'Wp'),(6,'one'),(6,'P'),(8,'one')],
 [(4,'P'),(6,'one'),(7,'Wp'),(8,'one')],
 [(3,'Wp'),(5,'Wp'),(6,'one'),(7,'Wp'),(8,'one')],
 [(5,'T'),(6,'one'),(8,'one')],
 [(4,'D'),(6,'one'),(9,'W')],
 [(3,'T'),(6,'one'),(20,'one')],
 [(3,'S'),(7,'W'),(9,'W')],
 [(4,'D'),(7,'W'),(10,'one')],
 [(3,'S'),(7,'W'),(8,'one'),(10,'one')],
 [(3,'Wp'),(4,'V'),(7,'W'),(12,'one')],
 [(4,'V'),(6,'V'),(7,'W')],
 [(3,'Wp'),(6,'P'),(7,'W')],
 [(4,'P'),(7,'W'),(7,'Wp')],
 [(3,'Wp'),(5,'Wp'),(7,'W'),(7,'Wp')],
 [(5,'T'),(7,'W')],
 [(3,'Wp'),(4,'D'),(18,'one')],
 [(3,'Wp'),(3,'S'),(8,'one'),(18,'one')],
 [(4,'D'),(8,'A')],
 [(3,'S'),(8,'one'),(8,'A')],
 [(3,'T'),(13,'Wp')],
]
assert len(supports)==25 and len({tuple(sorted(row)) for row in supports})==25
for row in supports:
    h1,chi=ZERO,ZERO
    rank,degree=0,0
    for j,R in row:
        assert j>=3
        dim=chars[R][0][0]
        assert chars[R][1][0]==(-1)**j*dim
        rank+=dim; degree-=j*dim
        if j>=4: h1=va(h1,vm(chars[R],sym(j-4)))
        if j==3: chi=va(chi,chars[R])
        elif j>=5: chi=vs(chi,vm(chars[R],sym(j-5)))
    assert h1==B and chi==chi3 and rank==8 and degree==-44
print('PASS: all 25 declared supports satisfy both budgets, parity, rank 8, degree -44.')
print('Completeness is the five-case human proof, not a support-enumeration claim.')

# Exact, declared complete 21-by-4 atomic Hom table.
# Columns: T_5, 1_10, 1_12, W_11.
hom_rows=[
 (3,'T',(0,0,0,0)), (3,'Wp',(0,0,0,0)), (3,'S',(0,0,0,0)),
 (4,'D',(0,0,0,0)), (4,'V',(0,0,0,0)), (4,'P',(0,0,0,0)),
 (5,'Wp',(0,0,0,0)), (5,'T',(1,0,0,0)),
 (6,'one',(0,0,0,0)), (6,'V',(1,0,0,0)), (6,'P',(1,0,0,0)),
 (7,'W',(0,0,0,0)), (7,'Wp',(1,0,0,0)),
 (8,'one',(0,0,0,0)), (8,'A',(1,0,0,0)),
 (9,'W',(1,0,0,0)), (10,'one',(1,1,0,0)),
 (12,'one',(1,0,1,1)), (13,'Wp',(2,0,0,0)),
 (18,'one',(1,0,0,0)), (20,'one',(2,0,0,0)),
]
targets=[(5,'T'),(10,'one'),(12,'one'),(11,'W')]
assert len(hom_rows)==21
assert {(j,R) for j,R,_ in hom_rows}=={atom for row in supports for atom in row}
hom={}
for j,R,values in hom_rows:
    for (n,U),value in zip(targets,values):
        actual=q(0) if j<n else inner(chars[R],vm(chars[U],sym(j-n)))
        assert actual==q(value)
        hom[((j,R),(n,U))]=value
for i,row in enumerate(supports,1):
    toT=sum(hom[(a,(5,'T'))] for a in row)
    toQ6=sum(hom[(a,t)] for a in row for t in targets[:3])
    toQ13=sum(hom[(a,t)] for a in row for t in [targets[0],targets[3]])
    assert toT==1+(i in {11,25})
    assert toQ6==1+(i in {2,3,4,11,13,14,15,25})
    assert toQ13==1+(i in {4,11,15,25})
print('PASS: all 84 declared atomic Hom dimensions and all 25 aggregate dimensions for each target.')
print('No actual source map, derivative value, selected coefficient, point, matrix, or model was evaluated.')

# The twelve declared first-polar rows, not a splitting search.
polar_rows=[
 ('0',0,10,10,None,None),
 ('one',10,11,2,None,None),
 ('W',9,12,-4,'A+D','Wp+T-S'),
 ('V',6,13,-2,'A+V+D','Wp'),
 ('Wp',7,12,0,'A+P+D','0'),
 ('one',12,11,0,'A+V+D','0'),
 ('T',5,16,-8,'A+D','Wp+T'),
 ('A',8,13,-8,'D','Wp+T'),
 ('one',20,11,-8,'A','Wp+T'),
 ('P',6,14,-6,'A+D','T'),
 ('one',18,11,-6,'D','T'),
 ('Wp',13,12,-12,'0','Wp+S+T'),
]
for R,j,rk,dg,c_expected,l_expected in polar_rows:
    rj=0 if R=='0' else chars[R][0][0]
    dj=-j*rj
    assert (rk,dg)==(10+rj,10+dj+2*rj)
    h2=ZERO if R=='0' else vm(chars[R],sym(j-4))
    h3=ZERO if R=='0' else vm(chars[R],sym(j-5))
    c=vs(B,h2)
    lin=vs(vs(sym(29),h3),vm(W,c))
    assert c[0][0]+lin[0][0]==rk and -lin[0][0]==dg
    if c_expected is not None:
        expected=vs(rep('Wp+T'),rep('S')) if l_expected=='Wp+T-S' else rep(l_expected)
        assert c==rep(c_expected) and lin==expected
    else:
        assert dg>0
print('PASS: all 12 first-polar rank/degree/character rows, including the two-dimensional Hom channels.')

# Complete, explicitly listed quotient shapes from rank <=3, degree12, positivity and parity.
# Each item is (coefficient, positive degree); its complete evaluation kernel
# has coefficient coefficient tensor Sym^(degree-1) W at degree -1.
quotients=[
 [('one',12)],
 [('one',2),('one',10)], [('one',4),('one',8)], [('one',6),('one',6)],
 [('one',2),('one',2),('one',8)], [('one',2),('one',4),('one',6)],
 [('one',4),('one',4),('one',4)],
 [('A',4)], [('V',4)],
 [('W',1),('one',10)], [('Wp',1),('one',10)],
 [('W',3),('one',6)], [('Wp',3),('one',6)],
 [('W',5),('one',2)], [('Wp',5),('one',2)],
]
matching=[]
for i,row in enumerate(quotients):
    rank=sum(chars[R][0][0] for R,d in row)
    degree=sum(d*chars[R][0][0] for R,d in row)
    assert 1<=rank<=3 and degree==12
    coefficient=ZERO
    for R,d in row:
        assert chars[R][1][0]==(-1)**d*chars[R][0][0]
        coefficient=va(coefficient,vm(chars[R],sym(d-1)))
    if coefficient==rep('Wp+S+T'):
        matching.append(i)
assert matching==[2,8,10]
assert va(sym(2),sym(6))==rep('A+V+P')
assert vm(chars['V'],sym(4))==rep('A+V+P+D')
assert vm(chars['V'],sym(3))==rep('Wp+S+T')
assert vm(chars['V'],sym(2))==rep('P+D')
print('PASS: all 15 declared positive quotient shapes and exactly the three stated complete-evaluation alternatives.')

# All declared linear channels, and the three endpoint-negative vanishing tests.
linear={(R,U):inner(chars[R],vm(chars[U],W)) for R in ('P','D') for U in ('Wp','T')}
assert linear=={('P','Wp'):q(1),('P','T'):q(1),('D','Wp'):q(0),('D','T'):q(1)}
for target in (sym(3),sym(1),vm(W,sym(2))):
    assert inner(chars['Wp'],target)==q(0)
assert vm(chars['Wp'],sym(2))==chars['T']
assert vm(chars['V'],W)==chars['T']
assert inner(chars['T'],sym(1))==q(0) and inner(chars['T'],sym(3))==q(0)
assert inner(chars['Wp'],sym(7))==q(1)
assert all(inner(chars['Wp'],sym(n))==q(0) for n in (1,3,5))
print('PASS: universal polar channels, rank-one image obstructions, and endpoint-negative vanishing.')
print('PASS: the verifier only checks the finite declared universal data; geometric exactness is proved in PROOF.md.')
