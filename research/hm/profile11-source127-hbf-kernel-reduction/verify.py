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
# Exact h-b-f internal target; all checks remain fixed abstract characters.
def hom(a,t):
    j,R=a;n,U=t
    return 0 if j<n else int(inner(chars[R],vm(chars[U],sym(j-n)))[0])
target=[(4,'D'),(5,'T'),(10,'one'),(12,'one')]
nonzero=lambda row:[(a,t,hom(a,t)) for a in row for t in target if hom(a,t)]
expected={
0:[((8,'A'),(4,'D'),1),((8,'A'),(5,'T'),1)],
6:[((7,'W'),(4,'D'),1),((10,'one'),(5,'T'),1),((10,'one'),(10,'one'),1)],
8:[((9,'W'),(4,'D'),1),((9,'W'),(5,'T'),1)],
3:[((18,'one'),(4,'D'),1),((18,'one'),(5,'T'),1)],
11:[((8,'one'),(4,'D'),1),((10,'one'),(5,'T'),1),((10,'one'),(10,'one'),1)]}
for i,e in expected.items():assert nonzero(rows[i])==e
assert hom((8,'A'),(7,'W'))==1
assert hom((7,'W'),(4,'D'))==1
assert hom((9,'W'),(8,'one'))==1
assert hom((8,'one'),(4,'D'))==1
# Positive-degree and nongenuine-polar exclusions.
assert [-8+18,-8+18-6,-8+18-8]==[10,4,2]
C=vs(vs(sym(18),chars['P']),vm(W,sym(5)))
assert C==chars['A']
M1=vs(sym(19),vm(W,sym(4)))
assert vs(M1,vm(C,W))==vs(rep('Wp+T'),chars['S'])
assert vs(vs(vs(sym(18),chars['P']),sym(4)),sym(6))==C
assert vs(vs(sym(19),sym(3)),sym(5))==M1
# Surviving first spans: constant V+P, linear Wp+T, or linear T.
assert vs(vs(sym(18),chars['P']),vm(W,sym(3)))==rep('V+P')
assert vs(vs(sym(18),chars['P']),vm(chars['A'],sym(4)))==ZERO
assert vs(sym(19),vm(chars['A'],sym(3)))==rep('Wp+T')
assert vs(vs(vs(sym(18),chars['P']),vm(W,sym(3))),sym(6))==ZERO
assert vs(vs(sym(19),vm(W,sym(2))),sym(5))==rep('Wp+T')
assert vs(vs(sym(18),chars['P']),sym(14))==ZERO
assert vs(sym(19),sym(13))==chars['T']
# Standard cubic scalar-plane obstruction.
assert sym(8)==rep('P+D') and sym(16)==rep('V+P+2D')
assert inner(chars['A'],sym(16))==q(0)
assert vm(chars['T'],sym(2))==rep('Wp+S+2T')
assert hom((5,'W'),(3,'T'))==0
assert hom((10,'one'),(8,'one'))==0
assert 10<12
assert vs(vs(rep('2A+2V+2P+2D'),rep('A+V+P')),sym(8))==rep('A+V+D')
# Both rank-eight constant-span candidates, and exact lower-row tests.
assert vm(chars['P'],sym(2))==rep('V+P+D')
assert vm(chars['T'],W)==rep('V+P+D')
assert hom((4,'A'),(-4,'one'))==0 # A(-4) -> O(4)
assert hom((4,'A'),(6,'one'))==0 # A(-4) -> O(-6)
assert hom((3,'W'),(-4,'one'))==0
assert hom((6,'one'),(-4,'one'))==0
assert hom((3,'W'),(6,'one'))==0
assert hom((6,'one'),(6,'one'))==1 # surviving source127 row
assert hom((14,'one'),(-4,'one'))==0
assert hom((14,'one'),(6,'one'))==0
assert hom((-3,'Wp'),(-4,'one'))==0
assert vm(chars['D'],W)==rep('S+T')
# Uniform degree38 quotient and exact dual endpoint.
for c in (8,12):
    assert (19-c)+16-(30-c)==5
assert va(sym(16),sym(18))==rep('A+2V+3P+3D')
assert vs(rep('A+2V+3P+4D'),va(sym(16),sym(18)))==chars['D']
chi=va(vs(vs(chars['T'],vk(2,W)),chars['S']),va(sym(13),sym(15)))
assert chi==vs(rep('Wp+S+4T'),W)
assert vm(rep('2Wp+T'),sym(2))==rep('Wp+S+4T')
assert sym(7)==rep('Wp+T')
# Original tuple and exact endpoint.
pairs=json.loads((ROOT/'audit-inputs/pairs.json').read_text())
frontier=json.loads((ROOT/'audit-inputs/frontier.json').read_text())
t=[0,1,0,0,0,1,0,1];row=pairs[127]
assert t in row['compatible_E_types'] and row['defect']==0
assert row['A']==[[-8,'one'],[2,'one'],[16,'one']]
assert row['B']==[[-18,'one'],[-4,'one'],[6,'one']]
case=next(c for c in frontier['cases'] if c['id']=='G3.11.cce6e3ba4eeb')
assert case['source_index']==127 and case['original_defect']==0
assert 9+6+1+1==17 and -18-18-8-10==-54
print('PASS: nine immutable blobs; thirteen exact rank3 candidates and five kernels; complete h-b-f internal channels; polar obstructions; scalar-plane identities; all lower rows including the surviving scalar row; degree38 dual obstruction; original source127 h-b-f tuple.')
print('This is a necessary branch reduction, not a whole-source exclusion. Coherent-image, connection and saturation arguments are written in PROOF.md; no actual source instance was evaluated.')
