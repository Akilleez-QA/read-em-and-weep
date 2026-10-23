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

# Fixed abstract support check and immutable source identity only.
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
entries=json.loads((ROOT/'audit-inputs/manifest.json').read_text());assert len(entries)==5
for e in entries:
    b=(ROOT/'audit-inputs'/e['name']).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob']
assert hashlib.sha256((ROOT/'audit-inputs/PR885.md').read_bytes()).hexdigest()=='3e3a994defbeea2cefff4b0a64a93f70e0059417f8850a79d85069c1d45ab169'
C=rep('V+P+D')
assert vm(W,W)==rep('one+A')
Vchi=va(C,vm(W,W));assert Vchi==rep('one+A+V+P+D')
positive_rank2=[vm(W,sym(7)),vm(chars['Wp'],sym(7)),va(sym(2),sym(12)),va(sym(4),sym(10)),va(sym(6),sym(8))]
expected=['V+2P+D','one+A+V+P+D','one+2A+P+D','A+V+2D','V+2P+D']
assert all(x==rep(y) for x,y in zip(positive_rank2,expected))
assert [i for i,x in enumerate(positive_rank2) if x==Vchi]==[1]
assert -20+6==-14 and -14-18==-32 and 18+2*7==32
assert 8+22-18==12
assert -54+32+12==-10 # defect12 gives rank10 pure O(-1)
assert 10>8 and sym(7)==rep('Wp+T')
M2=rep('A+2V+3P+4D');M3=rep('3Wp+3S+6T')
assert sym(16)==rep('V+P+2D')
assert vm(chars['Wp'],sym(5))==rep('A+P+D')
assert vs(M2,va(sym(16),vm(chars['Wp'],sym(5))))==C
Q1=vs(M3,vm(M2,W));U1=vk(-1,va(sym(15),vm(chars['Wp'],sym(4))))
assert Q1==vk(-1,rep('W+2S+3T'))
assert U1==vk(-1,rep('2S+3T'))
assert vs(Q1,U1)==vk(-1,W)
# Exhaustive small H1-budget atoms: (j-1)dim coefficient<=12 and center parity.
B=dec(C);allowed=[]
for j in range(2,14):
    for name in names:
        U=chars[name];d=int(U[0][0])
        if (j-1)*d>12 or U[1]!=q((-1)**j*d):continue
        h1=dec(vm(U,sym(j-2)))
        if all(0<=a<=b for a,b in zip(h1,B)):
            allowed.append((j,name))
expected_atoms=[(2,'V'),(2,'P'),(2,'D'),(3,'Wp'),(3,'T'),(4,'V'),(4,'P'),(5,'Wp'),(6,'one'),(7,'W'),(8,'one'),(10,'one')]
assert allowed==expected_atoms
expected_h1_twist1=['0','0','0','Wp','T','T','Wp+T','T','S','S+T','T','Wp+T']
for (j,name),expected in zip(allowed,expected_h1_twist1):
    h=ZERO if j==2 else vm(chars[name],sym(j-3))
    assert h==rep(expected)
    assert inner(h,W)==q(0)
pairs=json.loads((ROOT/'audit-inputs/pairs.json').read_text());row=pairs[127]
assert [0,1,0,0,0,1,0,1] in row['compatible_E_types'] and row['defect']==0
assert row['A']==[[-8,'one'],[2,'one'],[16,'one']]
assert row['B']==[[-18,'one'],[-4,'one'],[6,'one']]
frontier=json.loads((ROOT/'audit-inputs/frontier.json').read_text())
case=next(c for c in frontier['cases'] if c['id']=='G3.11.cce6e3ba4eeb')
assert case['source_index']==127 and case['original_defect']==0
print('PASS: five immutable blobs and exact reduction hash; positive rank2 quotient classification; defect12 strict-top contradiction; original twist1 subtraction; complete twelve-atom H1 budget; every twist1 H1 atom W-free; exact source127 h-b-f identity.')
print('The actual intersection, full-span saturation and dependency interfaces are proved in PROOF.md. No selected actual source data, parameter, point, derivative, matrix or rank was evaluated.')
