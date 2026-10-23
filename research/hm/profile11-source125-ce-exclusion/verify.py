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

# Fixed characters used by this single reduction.
for n,r in [(6,'V+P'),(7,'Wp+T'),(8,'P+D'),(9,'S+T'),(10,'A+V+D'),(11,'W+S+T'),(12,'one+A+P+D'),(14,'A+V+P+D'),(18,'A+V+2P+D'),(19,'W+Wp+S+2T'),(20,'one+A+V+P+2D')]:
    assert sym(n)==rep(r)
for r,n,out in [('P',1,'Wp+T'),('V',1,'T'),('V',2,'P+D'),('Wp',1,'P'),('Wp',2,'T'),('Wp',3,'V+D'),('T',1,'V+P+D'),('A',4,'A+V+P+D')]:
    assert vm(chars[r],sym(n))==rep(out)

def chi(j,R,twist):
    d=twist-j
    return vm(chars[R],sym(d)) if d>=0 else (ZERO if d==-1 else vk(-1,vm(chars[R],sym(-d-2))))
def rowchi(row,twist):
    a=ZERO
    for j,R in row:a=va(a,chi(j,R,twist))
    return a
K2=[[(3,'Wp'),(4,'V'),(7,'W')],[(3,'Wp'),(4,'V'),(6,'one'),(8,'one')]]
for row in K2:
    assert sum(chars[R][0][0] for j,R in row)==7
    assert sum(j*chars[R][0][0] for j,R in row)==32
    assert rowchi(row,2)==vk(-1,rep('A+V+D'))
    assert rowchi(row,3)==vs(chars['Wp'],rep('W+S'))
assert vs(sym(19),vm(rep('A+D'),W))==vs(rep('Wp+T'),chars['S'])

checks=0
def table(atoms,targets,expected):
    global checks
    observed=set()
    for a in atoms:
        j,R=a
        for t in targets:
            k,U=t
            h=q(0) if j<k else inner(chars[R],vm(chars[U],sym(j-k)))
            checks+=1
            assert h in (q(0),q(1))
            if h==q(1): observed.add((a,t))
    assert observed==expected,(observed,expected)
for row in K2:
    table(row,[(4,'V'),(6,'V'),(7,'Wp'),(12,'one')],{((4,'V'),(4,'V'))})
# High-P kernels and both possible low kernels have no full-top internal channel.
KP=[[(8,'A')],[(7,'W'),(10,'one')],[(3,'Wp'),(18,'one')]]
for row in KP+ [[(3,'T')],[(2,'V'),(4,'V')]]:
    table(row,[(6,'V'),(7,'Wp'),(12,'one')],set())
for row in KP:
    assert sum(chars[R][0][0] for j,R in row)==3
    assert sum(j*chars[R][0][0] for j,R in row)==24
    assert rowchi(row,2)==vk(-1,rep('A+V+P+D'))
    assert rowchi(row,3)==vk(-1,rep('W+S+T'))
# Divisor-P and two-positive-row N interfaces.
table([(4,'V')],[(4,'V'),(4,'P'),(6,'V'),(7,'Wp'),(12,'one')],{((4,'V'),(4,'V'))})
table([(5,'Wp'),(4,'V')],[(4,'P'),(6,'V'),(7,'Wp'),(12,'one')],{((5,'Wp'),(4,'P'))})
assert vs(vk(2,sym(7)),vm(rep('V+P'),W))==chars['Wp']
assert vs(vs(vk(2,sym(7)),chars['Wp']),vm(chars['V'],W))==rep('Wp+T')
table([(3,'Wp')],[(-6,'one')],set()) # Wp(-3) -> O(6): degree9.
assert inner(chars['Wp'],sym(9))==q(0)
assert inner(chars['V'],vm(chars['V'],sym(2)))==q(0)
assert inner(chars['Wp'],sym(5))==q(0)
# Second linear-block constant projection.
table([(18,'one')],[(4,'V'),(4,'P'),(6,'V'),(7,'Wp'),(12,'one')],{((18,'one'),(4,'V')),((18,'one'),(4,'P'))})
table([(16,'one')],[(2,'V'),(2,'P'),(4,'V'),(5,'Wp'),(10,'one')],{((16,'one'),(2,'V')),((16,'one'),(2,'P'))})
# Fixed representation vanishings in the second projection and q alternative.
for n,r in [(4,'V'),(8,'V'),(0,'V'),(12,'V'),(11,'Wp'),(6,'one')]: assert inner(chars[r],sym(n))==q(0)
# The final full-top positive kernel, fixed support and negative-W shortcut.
KF=[[(7,'W'),(4,'V'),(4,'P')],[(7,'W'),(4,'V'),(5,'Wp'),(3,'Wp')],[(7,'W'),(10,'one'),(3,'T')],[(8,'A'),(3,'T')],[(18,'one'),(3,'Wp'),(3,'T')]]
for row in KF:
    assert sum(chars[R][0][0] for j,R in row)==9
    assert sum(j*chars[R][0][0] for j,R in row)==42
    assert rowchi(row,2)==vk(-1,rep('A+V+P+D'))
    assert rowchi(row,3)==vk(-1,rep('W+S'))
    table(row,[(6,'V'),(7,'Wp'),(12,'one')],set())
atoms=[(4,x) for x in ('A','V','P','D')]+[(5,x) for x in ('Wp','S','T')]+[(6,x) for x in ('one','V','P','D')]+[(7,x) for x in ('W','Wp')]+[(8,x) for x in ('one','A','V')]+[(9,x) for x in ('W','Wp')]+[(j,'one') for j in (10,12,14,18)]
budget=dec(rep('A+V+P+D'))
for j,R in atoms:
    h=dec(vk(-1,chi(j,R,2)))
    assert all(0<=a<=b for a,b in zip(h,budget))
negativeW=[(j,R) for j,R in atoms if inner(chi(j,R,3),W)==q(-1)]
assert negativeW==[(6,'one'),(7,'W'),(8,'A'),(18,'one')]
for j,R in negativeW: assert inner(vk(-1,chi(j,R,2)),chars['A'])==q(1)
assert inner(chars['V'],sym(4))==inner(chars['P'],sym(4))==q(0)
assert vs(vk(2,sym(7)),vm(chars['V'],W))==rep('2Wp+T')
assert [n for n in range(1,21) if inner(chars['one'],sym(n))!=q(0)]==[12,20]
# Degrees/ranks whose contradictions are used.
assert -22+6+18==2 and -14+16==2
assert -8+12>0 and -2+12>0
# Pinned original catalog identity, using the cf immutable audit copies.
root=Path(__file__).resolve().parent/'audit-inputs'
pins={'one-one-endpoint-necessary-pairs.json':'fe0afa410d89340d3082dc814277f89fbb582c19', 'rank-three-quotient-frontier-144.json':'8b5971092f9ef762584912609fd5e9301c4e271d'}
data={}
for name,sha in pins.items():
    b=(root/name).read_bytes(); assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha
    data[name]=json.loads(b)
source=data['one-one-endpoint-necessary-pairs.json'][125]
assert source['A']==[[-10,'one'],[4,'one'],[16,'one']]
assert source['B']==[[-18,'one'],[-6,'one'],[8,'one']]
assert source['defect']==0 and [0,0,1,0,1,0,0,1] in source['compatible_E_types']
case=[x for x in data['rank-three-quotient-frontier-144.json']['cases'] if x['id']=='G3.11.ea6bced3bddf']
assert len(case)==1 and case[0]['source_index']==125 and case[0]['original_defect']==0
print('PASS:',checks,'fixed Hom spaces, kernel/polar identities, and pinned source125 ce identity.')
print('No selected actual source evaluation, source scan, parameter, point, matrix, or instance rank was used.')
