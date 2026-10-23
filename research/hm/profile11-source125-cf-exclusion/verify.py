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

# All checks below are fixed identities arising in this single proof.
def hom(atom,target):
    j,R=atom; k,U=target
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
    assert seen==expected, (seen,expected)

# Reusable kernels and exact polar identities.
assert sym(4)==chars['D'] and sym(6)==rep('V+P')
assert sym(7)==rep('Wp+T') and sym(8)==rep('P+D')
assert vm(chars['Wp'],W)==chars['P']
assert vm(chars['V'],W)==chars['T']
assert vm(chars['P'],W)==rep('Wp+T')
assert vm(chars['D'],W)==rep('S+T')
assert vm(chars['T'],W)==rep('D+V+P')
assert inner(chars['V'],sym(4))==q(0)
assert inner(chars['V'],sym(8))==q(0)
assert inner(chars['Wp'],sym(5))==q(0)
assert inner(chars['one'],sym(2))==q(0)
assert inner(chars['one'],sym(4))==q(0)
assert inner(chars['Wp'],vm(chars['D'],W))==q(0)
assert sym(18)==rep('A+V+2P+D')
assert vs(sym(18),rep('P+D'))==rep('A+V+P')
assert vs(vs(sym(18),rep('P+D')),sym(6))==chars['A']
assert vs(vs(sym(19),sym(5)),vm(chars['A'],W))==rep('Wp+T')
assert vs(vm(rep('V+P'),W),sym(7))==chars['T']
assert vs(vm(chars['V'],W),sym(7))==vk(-1,chars['Wp'])
assert vs(sym(6),chars['V'])==chars['P']

# High-(P+D) and lower-P-zero kernel interfaces.
KPD=[[(4,'V'),(4,'P'),(6,'one')],
     [(3,'Wp'),(4,'V'),(5,'Wp'),(6,'one')],
     [(3,'T'),(6,'one'),(10,'one')]]
targets=[(4,'V'),(6,'V'),(10,'one'),(12,'one')]
for i,K in enumerate(KPD):
    expected={((4,'V'),(4,'V'))} if i<2 else {
        ((10,'one'),(4,'V')),((10,'one'),(10,'one'))}
    check_table(K,targets,expected)
for K in KPD[:2]:
    check_table(K,[(6,'V'),(10,'one'),(12,'one')],set())
check_table([(2,'V'),(5,'Wp')],[(6,'V'),(10,'one'),(12,'one')],set())

# High-D kernel, its internal image, and polar degrees.
KD=[(5,'Wp'),(6,'one'),(10,'one')]
rank=degree=0; h=ZERO
for j,R in KD:
    rank+=chars[R][0][0]; degree-=j*chars[R][0][0]
    h=va(h,vm(chars[R],sym(j-4)))
assert (rank,degree)==(4,-26) and h==rep('A+V+2P')
check_table(KD,[(4,'V'),(4,'P'),(6,'V'),(10,'one'),(12,'one')],{
    ((5,'Wp'),(4,'P')),((10,'one'),(4,'V')),
    ((10,'one'),(4,'P')),((10,'one'),(10,'one'))})
check_table([(10,'one')],[(5,'Wp'),(3,'Wp')],{((10,'one'),(3,'Wp'))})
assert [-10+18+d+2*r for r,d in [(0,0),(2,-10),(1,-10),(3,-20)]]==[8,2,0,-6]
assert vs(h,sym(6))==rep('A+P')
assert vs(vs(h,sym(6)),chars['P'])==chars['A']
assert vs(vs(vs(sym(19),sym(5)),chars['Wp']),vm(chars['A'],W))==chars['T']

# Small obstruction kernels, trapped-tail internal map, and quotient line channels.
check_table([(5,'Wp')],[(6,'V'),(10,'one'),(12,'one')],set())
check_table([(3,'T')],[(6,'V'),(12,'one')],set())
check_table([(4,'V')],[(4,'V'),(4,'P'),(12,'one')],{((4,'V'),(4,'V'))})
check_table([(2,'D')],[(6,'V'),(10,'one'),(12,'one')],set())
check_table([(8,'one')],[(2,'V'),(2,'P'),(4,'V'),(8,'one'),(10,'one')],{
    ((8,'one'),(2,'V')),((8,'one'),(2,'P')),((8,'one'),(8,'one'))})
check_table([(8,'one')],[(2,'V'),(1,'Wp'),(4,'V'),(8,'one'),(10,'one')],{
    ((8,'one'),(2,'V')),((8,'one'),(1,'Wp')),((8,'one'),(8,'one'))})
assert vs(sym(6),rep('V+P'))==ZERO
assert vs(sym(5),ZERO)==chars['T']
assert 18!=24 and not 18<=11
assert -24+6+18==0
assert 7+3>9 and -4*3==-12
assert 17-(5+2+1)==9 and -54-(-10-6-8)==-30 and -30>-90
assert -2*3-(-8)==2
assert -2*3-2-(-8)==0

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
assert [0,0,1,0,0,1,0,1] in source['compatible_E_types']
case=[x for x in data['rank-three-quotient-frontier-144.json']['cases'] if x['id']=='G3.11.ea6bced3bddf']
assert len(case)==1 and case[0]['source_index']==125
assert case[0]['A']==Aq and case[0]['B']==Bq and case[0]['original_defect']==0
print('PASS: %d fixed internal Hom checks, polar and trapped-tail identities, original source125 cf identity.'%checks)
print('No source/model evaluation, support search, all-twist envelope, or current frontier count was performed.')

