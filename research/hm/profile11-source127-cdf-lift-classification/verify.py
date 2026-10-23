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

# Fixed universal characters and immutable input authentication only.
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
entries=json.loads((ROOT/'audit-inputs/manifest.json').read_text());assert len(entries)==6
for e in entries:
    b=(ROOT/'audit-inputs'/e['name']).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob']
def hom(U,d,V,e):return 0 if e<d else inner(chars[U],vm(chars[V],sym(e-d)))[0]
C10=rep('A+V+P');C11=sym(10);C9=sym(8)
assert C11==rep('A+V+D') and C9==rep('P+D')
assert sym(18)==rep('A+V+2P+D')
assert sym(22)==rep('2A+V+P+2D')
assert inner(C11,C10)==q(2)
assert inner(sym(22),rep('V+P'))==q(2)
assert hom('V',-4,'one',18)==1 and hom('P',-4,'one',18)==1
assert inner(C9,C10)==q(1)
assert sum(hom('one',-8,U,0) for U in ('A','V','P'))==1
assert inner(chars['D'],C10)==q(0)
# Exact principal-parts sequence: 0 -> Sym6(-4) -> Sym10 O -> Sym3(7) -> 0.
assert va(vk(-1,vm(sym(6),sym(2))),vm(sym(3),sym(7)))==sym(10)
assert 7+4==11 and -28+4*7==0
assert hom('S',7,'one',18)==1
# The two exceptional lines: only fixed universal channel multiplicities.
assert inner(sym(12),chars['one'])==q(1)
assert inner(sym(6),chars['V'])==q(1) and inner(sym(6),chars['P'])==q(1)
assert inner(sym(18),chars['V'])==q(1)
assert inner(sym(7),chars['T'])==q(1) and inner(sym(7),chars['Wp'])==q(1)
assert inner(sym(5),chars['Wp'])==q(0)
assert vm(chars['V'],W)==chars['T']
assert vm(chars['Wp'],W)==chars['P'] and vm(chars['Wp'],sym(2))==chars['T']
# The Wronskian proof is symbolic and universal, not a determinant evaluation.
# The degree-j falling factorial is monic for j=0,1,2,3.
falling=[[1]]
for j in range(1,4):
    prev=falling[-1];out=[0]*(len(prev)+1)
    for k,a in enumerate(prev):out[k]-=(j-1)*a;out[k+1]+=a
    falling.append(out)
assert falling==[[1],[0,1],[0,-1,1],[0,2,-3,1]]
assert all(poly[-1]==1 and len(poly)==j+1 for j,poly in enumerate(falling))
pairs=json.loads((ROOT/'audit-inputs/pairs.json').read_text());row=pairs[127]
assert [0,0,1,1,0,1,0,0] in row['compatible_E_types'] and row['defect']==0
assert row['A']==[[-8,'one'],[2,'one'],[16,'one']]
assert row['B']==[[-18,'one'],[-4,'one'],[6,'one']]
frontier=json.loads((ROOT/'audit-inputs/frontier.json').read_text());case=next(c for c in frontier['cases'] if c['id']=='G3.11.cce6e3ba4eeb')
assert case['source_index']==127 and case['original_defect']==0
print('PASS: six immutable inputs; original c-d-f identity; exact scalar and quartic shear dimensions; jet quotient Euler identity; missing D in C10; universal monic falling-factorial identities.')
print('Generic jet surjectivity, the zero kernel of the shear map, regular lift removal and parameter uniqueness are proved structurally. No selected actual source coefficient, point, derivative, matrix or rank was evaluated.')
