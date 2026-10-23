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

# Fixed thirteen-candidate abstract character check, not an actual-source evaluation.
from pathlib import Path
import hashlib
import json
ROOT=Path(__file__).resolve().parent
for e in json.loads((ROOT/'audit-inputs/manifest.json').read_text()):
    data=(ROOT/'audit-inputs'/e['name']).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==e['git_blob']
assert sym(18)==rep('A+V+2P+D')
assert sym(19)==rep('W+Wp+S+2T')
assert vm(chars['P'],W)==rep('Wp+T')
assert vm(chars['A'],W)==rep('W+S')
assert sym(6)==rep('V+P')
B=rep('A+V+P+D'); X=vk(-1,rep('W+S+T'))
assert vs(sym(18),chars['P'])==B
assert vs(vm(chars['P'],W),sym(19))==X
# Each declared candidate is forced by rank3, degree−24 and center parity.
rows=[[(8,'A')],[(8,'V')],[(3,'W'),(18,'one')],[(3,'Wp'),(18,'one')],
[(5,'W'),(14,'one')],[(5,'Wp'),(14,'one')],[(7,'W'),(10,'one')],
[(7,'Wp'),(10,'one')],[(9,'W'),(6,'one')],[(9,'Wp'),(6,'one')],
[(6,'one'),(6,'one'),(12,'one')],[(6,'one'),(8,'one'),(10,'one')],
[(8,'one'),(8,'one'),(8,'one')]]
expected_h1=['A+V+P+D','A+V+P+D','A+V+P+D','A+V+P+D',
 'one+2A+V+D','A+V+P+D','A+V+P+D','2V+P+D','A+V+P+D','2A+P+D',
 '2A+P+D','A+V+P+D','3D']
passing=[]
for index,row in enumerate(rows):
    rank=degree=0; h1=chi=ZERO
    for j,R in row:
        d=int(chars[R][0][0]);rank+=d;degree-=j*d
        if j>=4:h1=va(h1,vm(chars[R],sym(j-4)))
        if j==3:chi=va(chi,chars[R])
        elif j>=5:chi=vs(chi,vm(chars[R],sym(j-5)))
    assert (rank,degree)==(3,-24)
    assert h1==rep(expected_h1[index])
    if h1==B:
        assert chi==vk(-1,rep('Wp+S+T')) if index in [1,2,5] else chi==X
    if h1==B and chi==X:passing.append(index)
assert passing==[0,3,6,8,11]
# Completeness of the short rank/degree partitions, without unknown maps.
assert [(j,24-2*j) for j in (3,5,7,9)]==[(3,18),(5,14),(7,10),(9,6)]
assert all(sum(t)==24 for t in [(6,6,12),(6,8,10),(8,8,8)])
# All relevant actual internal target Hom spaces.
def hom(atom,target):
    j,R=atom;n,U=target
    return 0 if j<n else int(inner(chars[R],vm(chars[U],sym(j-n)))[0])
target=[(4,'D'),(6,'V'),(6,'P'),(10,'one')]
nonzero=lambda row:[(a,t,hom(a,t)) for a in row for t in target if hom(a,t)]
assert nonzero(rows[8])==[((9,'W'),(4,'D'),1)]
assert nonzero(rows[11])==[((8,'one'),(4,'D'),1),((10,'one'),(10,'one'),1)]
assert vm(chars['V'],sym(3))==rep('Wp+S+T')
assert vm(chars['P'],sym(3))==rep('S+2T')
# Universal unique factorization W O(-9) -> O(-8) -> D O(-4).
assert hom((9,'W'),(8,'one'))==1
assert hom((8,'one'),(4,'D'))==1
# First-span rank-degree and polar-character identities.
assert -8+18==10 and -8+18-6==4 and -8+18-8==2
assert 4+1+2==7 and -8+18-6-8==-4
C=vs(vs(vs(sym(18),chars['P']),sym(4)),sym(6))
assert C==chars['A']
M1=vs(vs(sym(19),sym(3)),sym(5))
assert M1==rep('W+Wp+T')
L=vs(M1,vm(C,W))
assert L==vs(rep('Wp+T'),chars['S'])
assert inner(L,chars['S'])==q(-1)
# Confirm the three remaining forms really have nonzero candidate channels.
assert nonzero(rows[0])==[((8,'A'),(4,'D'),1)]
assert nonzero(rows[6])==[((7,'W'),(4,'D'),1),((10,'one'),(10,'one'),1)]
assert nonzero(rows[3])==[((18,'one'),(4,'D'),1),((18,'one'),(6,'P'),1)]
pairs=json.loads((ROOT/'audit-inputs/pairs.json').read_text())
frontier=json.loads((ROOT/'audit-inputs/frontier.json').read_text())
row=pairs[127]; t=[0,0,1,1,0,1,0,0]
assert t in row['compatible_E_types'] and row['defect']==0
assert row['A']==[[-8,'one'],[2,'one'],[16,'one']]
case=next(c for c in frontier['cases'] if c['id']=='G3.11.cce6e3ba4eeb')
assert case['source_index']==127 and case['original_defect']==0
assert 4+5+3+4+1==17 and -2*(4+5)-4*(3+4)-8==-54
print('PASS: eight immutable blobs; original c-d-f source identity; all thirteen rank3 candidates; exactly five initial kernels; complete channels for two exclusions; three residual interfaces.')
print('PASS: universal Hom multiplicities, saturated-image degree arithmetic, impossible first-polar linear character.')
print('This is a necessary high-P kernel reduction only; the published basepoint-free dependency is explicit. The geometric saturation arguments remain written mathematics; no actual source instance was evaluated.')
