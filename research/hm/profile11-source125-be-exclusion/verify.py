#!/usr/bin/env python3
"""Fixed universal character identities and one original source identity only."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import hashlib
import json

def q(a, b=0): return (Q(a), Q(b))
def plus(x, y): return (x[0]+y[0], x[1]+y[1])
def times(x, y): return (x[0]*y[0]+5*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def scale(k, x): return (k*x[0], k*x[1])
def total(xs):
    out = q(0)
    for x in xs: out = plus(out, x)
    return out
ZERO = (q(0),)*9
def va(x,y): return tuple(plus(a,b) for a,b in zip(x,y))
def vk(k,x): return tuple(scale(k,a) for a in x)
def vm(x,y): return tuple(times(a,b) for a,b in zip(x,y))
def vs(x,y): return va(x,vk(-1,y))
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
chars = {'one':sym(0),'W':W,'A':sym(2),'S':sym(3),'D':sym(4),'T':sym(5)}
chars['P'] = tuple(map(q,(4,4,-1,-1,-1,-1,1,1,0)))
chars['V'] = vs(sym(6),chars['P'])
chars['Wp'] = vs(vm(W,chars['P']),chars['T'])
names = ('one','W','Wp','A','V','P','S','D','T')
def inner(x,y): return scale(Q(1,120),total(scale(k,times(a,b)) for k,a,b in zip(sizes,x,y)))
assert all(inner(chars[a],chars[b]) == q(a==b) for a in names for b in names)
def rep(s):
    out = ZERO
    if s == '0': return out
    for term in s.split('+'):
        k = int(term[0]) if term[0].isdigit() else 1
        name = term[1:] if term[0].isdigit() else term
        out = va(out,vk(k,chars[name]))
    return out
def dec(x):
    out = [inner(x,chars[n]) for n in names]
    assert all(b==0 and a.denominator==1 for a,b in out)
    return tuple(int(a) for a,b in out)

# Fixed universal identities for the be proof; no model/source evaluations.
def hom(a,t):
    j,R=a; k,U=t
    return q(0) if j<k else inner(chars[R],vm(chars[U],sym(j-k)))
checks=0
def check_table(atoms,targets,expected):
    global checks
    seen=set()
    for a in atoms:
        for t in targets:
            x=hom(a,t); checks+=1
            assert x in (q(0),q(1))
            if x==q(1): seen.add((a,t))
    assert seen==expected,(seen,expected)

def h1_twist2(K):
    out=ZERO
    for j,R in K:
        if j>=4: out=va(out,vm(chars[R],sym(j-4)))
    return out

def chi_twist3(K):
    out=ZERO
    for j,R in K:
        if j==3: out=va(out,chars[R])
        elif j>=5: out=vs(out,vm(chars[R],sym(j-5)))
    return out

# Complete high-P rank-three alternatives, as justified in the prose.
budget=rep('A+V+P+D'); target=vk(-1,rep('W+S+T'))
assert vs(sym(18),chars['P'])==budget
assert vs(vm(chars['P'],W),sym(19))==target
for R in ('A','V'): assert h1_twist2([(8,R)])==budget
assert chi_twist3([(8,'A')])==target
assert chi_twist3([(8,'V')])==vk(-1,rep('Wp+S+T'))
rank_two=[[(j,R),(24-2*j,'one')] for j in (3,5,7,9) for R in ('W','Wp')]
fit=[K for K in rank_two if h1_twist2(K)==budget]
assert fit==[[(3,'W'),(18,'one')],[(3,'Wp'),(18,'one')],
             [(5,'Wp'),(14,'one')],[(7,'W'),(10,'one')],[(9,'W'),(6,'one')]]
assert [K for K in fit if chi_twist3(K)==target]==[
    [(3,'Wp'),(18,'one')],[(7,'W'),(10,'one')],[(9,'W'),(6,'one')]]
triples=[[(j,'one') for j in ds] for ds in ((6,6,12),(6,8,10),(8,8,8))]
assert [K for K in triples if h1_twist2(K)==budget]==[triples[1]]
assert chi_twist3(triples[1])==target
assert hom((6,'one'),(2,'P'))==q(0)

KA=[(8,'A')]; KW=[(7,'W'),(10,'one')]; KU=[(3,'Wp'),(18,'one')]
for K in (KA,KW,KU):
    assert sum(chars[R][0][0] for _,R in K)==3
    assert sum(-j*chars[R][0][0] for j,R in K)==-24
    assert h1_twist2(K)==budget and chi_twist3(K)==target

# Lower-row-zero kernels and divisor kernel have no internal channel.
for K in ([(3,'Wp'),(4,'V'),(7,'W')],
          [(3,'Wp'),(4,'V'),(6,'one'),(8,'one')]):
    check_table(K,[(5,'T'),(7,'Wp'),(12,'one')],set())
check_table([(4,'V')],[(4,'P'),(5,'T'),(7,'Wp'),(12,'one')],set())
assert -16+18==2 and 6>3 and 8-6==2<12

# The five Ext groups of the full positive kernel vanish.
for R,d in [('A',2),('W',1),('one',4),('one',12)]:
    assert inner(sym(0),vm(vm(chars['V'],chars[R]),sym(d)))==q(0)
# The Wp(-3) extension vanishes by ordinary H1(O(1))=0.
assert vm(chars['A'],chars['V'])==rep('P+D')
assert sym(12)==rep('one+A+P+D')

# Full-top internal channels, and the corresponding high-only channels.
for K,a in ((KA,(8,'A')),(KW,(10,'one')),(KU,(18,'one'))):
    check_table(K+[(4,'V')],[(5,'T'),(7,'Wp'),(12,'one')],{(a,(5,'T'))})
    check_table(K,[(4,'P'),(5,'T'),(7,'Wp'),(12,'one')],
                {(a,(4,'P')),(a,(5,'T'))})

# First-span character and degree identities.
base=vs(va(sym(6),sym(18)),vk(2,chars['P']))
assert base==rep('A+2V+P+D')
assert vm(chars['A'],sym(4))==rep('A+V+P+D')
assert sym(14)==rep('A+V+P+D')
assert vs(base,vm(chars['A'],sym(4)))==chars['V']
assert vs(base,sym(14))==chars['V']
assert vs(vs(va(sym(7),sym(19)),vm(chars['A'],sym(3))),vm(chars['V'],W))==rep('2Wp+T')
assert vs(vs(va(sym(7),sym(19)),sym(13)),vm(chars['V'],W))==rep('Wp+T')
assert -16+24-24+6==-10 and 8+2+3==13
assert -16+24-18+2==-8 and 8+2+1==11
assert -8+18-10+2==2
assert vs(vs(sym(18),chars['P']),vm(chars['A'],sym(4)))==ZERO
assert vs(vs(sym(18),chars['P']),sym(14))==ZERO
assert vs(sym(19),vm(chars['A'],sym(3)))==rep('Wp+T')
assert vs(sym(19),sym(13))==chars['T']

# Universal Euler/multiplication and graph capture identities.
assert vm(chars['Wp'],W)==chars['P']
assert vm(chars['Wp'],sym(2))==chars['T']
assert vm(chars['V'],W)==chars['T']
check_table([(2,'P')],[(1,'Wp'),(1,'T')],{((2,'P'),(1,'Wp')),((2,'P'),(1,'T'))})
check_table([(1,'Wp')],[(0,'V')],set())
assert inner(chars['Wp'],sym(5))==q(0)
assert inner(chars['Wp'],sym(17))==q(1)
assert inner(chars['P'],sym(2))==q(0)
assert inner(chars['T'],sym(1))==q(0)

# Second constant projection and final residual.
check_table([(18,'one')],[(4,'P'),(5,'T'),(7,'Wp'),(12,'one')],
    {((18,'one'),(4,'P')),((18,'one'),(5,'T'))})
check_table([(16,'one')],[(2,'P'),(3,'T'),(5,'Wp'),(10,'one')],
    {((16,'one'),(2,'P')),((16,'one'),(3,'T'))})
assert -2+18-18+2==0
assert 4+6-1==9 and -8-18+16==-10
assert 9+2+1==12 and -10-10-10==-30
assert 12-8==4 and -30>-40

# Exact original source identity and immutable Git blob pins.
root=Path(__file__).resolve().parent/'audit-inputs'
pins={'one-one-endpoint-necessary-pairs.json':'fe0afa410d89340d3082dc814277f89fbb582c19',
      'rank-three-quotient-frontier-144.json':'8b5971092f9ef762584912609fd5e9301c4e271d'}
data={}
for name,sha in pins.items():
    b=(root/name).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha
    data[name]=json.loads(b)
source=data['one-one-endpoint-necessary-pairs.json'][125]
Aq=[[-10,'one'],[4,'one'],[16,'one']]
Bq=[[-18,'one'],[-6,'one'],[8,'one']]
assert source['A']==Aq and source['B']==Bq and source['defect']==0
assert [0,1,0,0,1,0,0,1] in source['compatible_E_types']
case=[x for x in data['rank-three-quotient-frontier-144.json']['cases'] if x['id']=='G3.11.ea6bced3bddf']
assert len(case)==1 and case[0]['source_index']==125
assert case[0]['A']==Aq and case[0]['B']==Bq and case[0]['original_defect']==0
print('PASS: %d fixed Hom checks, high-P kernels, Ext/polar/Euler identities, original source125 be identity.'%checks)
print('No source/model evaluation, support search, all-twist envelope, or current frontier count was performed.')

