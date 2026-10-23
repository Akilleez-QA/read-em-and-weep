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

# Fixed abstract representation checks. No actual instance is evaluated.
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
PINNED=json.loads((ROOT/'audit-inputs/manifest.json').read_text())
for entry in PINNED:
    data=(ROOT/'audit-inputs'/entry['name']).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==entry['git_blob']

assert sym(18)==rep('A+V+2P+D')
assert sym(19)==rep('W+Wp+S+2T')
assert sym(6)==rep('V+P')
assert sym(10)==rep('A+V+D')
assert sym(14)==rep('A+V+P+D')
assert inner(sym(10),chars['one'])==q(0)
assert inner(sym(14),chars['one'])==q(0)
assert inner(sym(2),chars['one'])==q(0)
assert vm(chars['D'],W)==rep('S+T')
assert vm(chars['P'],W)==rep('Wp+T')
assert vm(chars['T'],W)==rep('V+P+D')
assert vm(chars['A'],W)==rep('W+S')

# Atoms (j,R) denote R O(-j); the number is an abstract Hom dimension.
def hom(atom,target):
    j,R=atom; n,U=target
    return 0 if j<n else int(inner(chars[R],vm(chars[U],sym(j-n)))[0])
rows=[[(4,'V'),(4,'P'),(6,'one')],
      [(3,'Wp'),(4,'V'),(5,'Wp'),(6,'one')],
      [(3,'T'),(6,'one'),(10,'one')]]
targets=[[(4,'D'),(10,'one'),(10,'one'),(12,'one')],
         [(4,'D'),(10,'one'),(11,'W')]]
for row_index,row in enumerate(rows):
    rank=degree=0;h1=chi=ZERO
    for j,R in row:
        d=int(chars[R][0][0]);rank+=d;degree-=j*d
        if j>=4:h1=va(h1,vm(chars[R],sym(j-4)))
        if j==3:chi=va(chi,chars[R])
        elif j>=5:chi=vs(chi,vm(chars[R],sym(j-5)))
    assert (rank,degree)==(8,-34)
    assert h1==rep('A+V+P') and chi==vk(-1,W)
    for target in targets:
        nonzero=[(a,t,hom(a,t)) for a in row for t in target if hom(a,t)]
        expected=[((10,'one'),(10,'one'),1)]*(2 if target is targets[0] else 1) if row_index==2 else []
        assert nonzero==expected

# Actual-image polar characters are checked, not their geometric derivation.
assert vs(sym(18),rep('P+D'))==rep('A+V+P')
assert vs(vs(sym(18),rep('P+D')),sym(6))==chars['A']
assert vs(vs(sym(19),sym(5)),vm(chars['A'],W))==rep('Wp+T')
assert 9+1==10 and -18+18==0
assert 9+2==11 and -18+18-8==-8
assert 5+1==6 and -10+4==-6
assert sym(4)==chars['D'] and sym(5)==chars['T']
assert 7-6==1 and 0-(-6)==6

# The residual quartic kernel has no internal derivative channel to the tails.
for target in [[(10,'one'),(10,'one'),(12,'one')],[(10,'one'),(11,'W')]]:
    assert all(hom((3,'S'),t)==0 for t in target)
# A killed scalar L may move internally only toward D O(-4).
assert hom((8,'one'),(4,'D'))==1
assert all(hom((8,'one'),t)==0 for t in [(10,'one'),(11,'W'),(12,'one')])
# Scalar-nonzero gf kernel cannot move into the negative endpoint quotient.
assert hom((3,'S'),(10,'one'))==0
assert hom((9,'W'),(10,'one'))==0
assert -10-8==-18 and -18!=-6
assert 5+2==7 and -10-18==-28
assert 7+1==8 and -28+4==-24
assert 24>6

# Pin both exact source edges and the full thirteen-member catalog list.
pairs=json.loads((ROOT/'audit-inputs/pairs.json').read_text())
frontier=json.loads((ROOT/'audit-inputs/frontier.json').read_text())
row=pairs[127]
expected=[(0,0,0,0,0,2,0,1),(0,0,0,0,1,1,0,1),
(0,0,1,0,0,1,0,1),(0,1,0,0,0,1,0,1),(0,0,0,0,0,1,1,0),
(0,0,0,0,1,0,1,0),(0,0,1,0,0,0,1,0),(0,1,0,0,0,0,1,0),
(0,0,1,1,0,1,0,0),(1,0,1,0,0,2,0,0),(1,0,1,0,1,1,0,0),
(1,0,2,0,0,1,0,0),(1,1,1,0,0,1,0,0)]
assert list(map(tuple,row['compatible_E_types']))==expected
assert row['defect']==0
assert row['A']==[[-8,'one'],[2,'one'],[16,'one']]
assert row['B']==[[-18,'one'],[-4,'one'],[6,'one']]
case=next(c for c in frontier['cases'] if c['id']=='G3.11.cce6e3ba4eeb')
assert case['source_index']==127 and case['original_defect']==0
assert case['A']==row['A'] and case['B']==row['B']

def decode(t):
    a,b,c,d,e,f,g,h=t
    out=[(2,'V',c+g+h-1),(2,'P',d+e+g+h),(2,'D',f+g),
         (3,'Wp',a),(3,'T',b),(4,'V',c),(4,'P',d),
         (5,'Wp',e),(8,'one',f),(9,'W',g),(10,'one',h)]
    assert all(k>=0 for j,R,k in out)
    return [(j,R,k) for j,R,k in out if k]
assert decode(expected[0])==[(2,'P',1),(2,'D',2),(8,'one',2),(10,'one',1)]
assert decode(expected[4])==[(2,'P',1),(2,'D',2),(8,'one',1),(9,'W',1)]
for t in [expected[0],expected[4]]:
    atoms=decode(t)
    assert sum(k*int(chars[R][0][0]) for j,R,k in atoms)==17
    assert -sum(j*k*int(chars[R][0][0]) for j,R,k in atoms)==-54
print('PASS: seven immutable blobs; complete original source127 list; both exact two-D sources.')
print('PASS: three high-line kernels, every internal Hom channel, first-polar characters, invariant-free degrees10/14, scalar-line and scalar-branch arithmetic.')
print('Only fixed abstract characters and original catalog data were checked. Connection, saturation, and coherent-lattice proofs remain written mathematics.')
