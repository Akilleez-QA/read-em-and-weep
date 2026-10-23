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

# The unique high-D kernel and fixed completeness checks.
budget=dec(rep('A+V+2P'))
def fits(x): return all(0<=a<=b for a,b in zip(dec(x),budget))
assert [j for j in (4,6,8,10,12,14,16) if fits(sym(j-4))]==[6,10]
for R in ('A','V'):
    for j,k in ((4,14),(6,8)):
        assert not fits(va(vm(chars[R],sym(j-4)),sym(k-4)))
assert not fits(vk(2,sym(2))) and not fits(vk(2,sym(6)))
assert vm(chars['Wp'],W)==chars['P']
assert vm(chars['W'],W)!=chars['P']
K=[(5,'Wp'),(6,'one'),(10,'one')]
rank=degree=0; h=chi=ZERO
for j,R in K:
    dim=chars[R][0][0]; rank+=dim; degree-=j*dim
    h=va(h,vm(chars[R],sym(j-4)))
    chi=vs(chi,vm(chars[R],sym(j-5)))
assert (rank,degree)==(4,-26)
assert h==rep('A+V+2P') and chi==vk(-1,rep('W+Wp+T'))
assert vs(sym(18),chars['D'])==h
assert vs(vm(chars['D'],W),sym(19))==chi

def hom(atom,target):
    j,R=atom; k,U=target
    return q(0) if j<k else inner(chars[R],vm(chars[U],sym(j-k)))
targets=[(4,'P'),(5,'T'),(10,'one'),(12,'one')]
expected={((5,'Wp'),(4,'P')),((10,'one'),(4,'P')),
          ((10,'one'),(5,'T')),((10,'one'),(10,'one'))}
seen=set(); checks=0
for a in K:
    for t in targets:
        x=hom(a,t); assert x in (q(0),q(1)); checks+=1
        if x==q(1): seen.add((a,t))
assert seen==expected
assert hom((10,'one'),(5,'Wp'))==q(0)
assert hom((10,'one'),(3,'Wp'))==q(1)
assert hom((3,'Wp'),(2,'D'))==q(0)

# Three high-(P+D) kernels, used only in the lower-row-zero branch.
KPD=[[(4,'V'),(4,'P'),(6,'one')],
     [(3,'Wp'),(4,'V'),(5,'Wp'),(6,'one')],
     [(3,'T'),(6,'one'),(10,'one')]]
target2=[(5,'T'),(10,'one'),(12,'one')]
for i,row in enumerate(KPD):
    seen=set()
    for a in row:
        for t in target2:
            x=hom(a,t); assert x in (q(0),q(1)); checks+=1
            if x==q(1): seen.add((a,t))
    assert seen==(set() if i<2 else {((10,'one'),(5,'T')),((10,'one'),(10,'one'))})

# Saturated polar degrees and exact characters for high D.
assert [-10+18+d+2*r for r,d in [(0,0),(2,-10),(1,-10),(3,-20)]]==[8,2,0,-6]
base=rep('A+V+2P')
assert vs(base,sym(6))==rep('A+P')
assert vs(vs(base,sym(6)),chars['P'])==chars['A']
assert vs(sym(19),sym(5))==vm(rep('A+P'),W)
assert vs(vs(vs(sym(19),sym(5)),chars['Wp']),vm(chars['A'],W))==chars['T']

# Small P and cubic T kernels, and every claimed fixed character.
assert sym(6)==rep('V+P') and sym(7)==rep('Wp+T')
assert vm(chars['P'],W)==sym(7)
assert inner(chars['D'],sym(6))==q(0)
assert inner(chars['one'],sym(4))==q(0)
assert inner(chars['Wp'],sym(5))==q(0)
assert vm(chars['D'],W)==rep('S+T')
assert vm(chars['T'],W)==rep('V+P+D')
assert vs(vm(chars['T'],W),sym(8))==chars['V']
assert vs(sym(7),chars['T'])==chars['Wp']
assert all(hom(a,t)==q(0) for a in [(4,'V'),(5,'Wp')] for t in [(10,'one'),(12,'one')])
assert all(hom((4,'V'),t)==q(0) for t in [(5,'T'),(12,'one')])
assert va(chars['P'],sym(4))==rep('P+D')
assert 6!=18 and 6+8+10>18
assert 6!=8 and not 6<=3
assert 17-(5+2+1)==9 and -54-(-10-6-8)==-30 and -30>-90

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
assert [0,1,0,0,0,1,0,1] in source['compatible_E_types']
case=[x for x in data['rank-three-quotient-frontier-144.json']['cases'] if x['id']=='G3.11.ea6bced3bddf']
assert len(case)==1 and case[0]['source_index']==125
assert case[0]['A']==Aq and case[0]['B']==Bq and case[0]['original_defect']==0
print('PASS: high-D kernel, %d fixed internal Hom checks, polar and cubic-T identities, original source125 bf identity.'%checks)
print('No source/model evaluation, support search, all-twist envelope, or current frontier count was performed.')

