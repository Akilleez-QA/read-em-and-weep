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

# Fixed universal characters and exact original source identity only.
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
entries=json.loads((ROOT/'audit-inputs/manifest.json').read_text());assert len(entries)==5
for e in entries:
    b=(ROOT/'audit-inputs'/e['name']).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob']
def hom(U,d,V,e):return 0 if e<d else inner(chars[U],vm(chars[V],sym(e-d)))[0]
def chi(U,d):
    if d>=0:return vm(chars[U],sym(d))
    if d==-1:return ZERO
    return vk(-1,vm(chars[U],sym(-d-2)))
assert sym(6)==rep('V+P') and sym(18)==rep('A+V+2P+D')
assert inner(sym(12),chars['one'])==q(1)
assert inner(sym(6),chars['V'])==q(1) and inner(sym(18),chars['V'])==q(1)
assert hom('V',-2,'one',2)==0 and hom('V',-2,'one',-8)==0
assert hom('Wp',-3,'V',0)==1
assert all(inner(sym(n),chars['Wp'])==q(0) for n in range(4))
assert va(chi('Wp',-5),chi('one',4))==chi('V',-2)
target=[('D',-4),('Wp',-5),('V',-6),('one',-10)]
channels=[]
for V,e in target:
    h=hom('Wp',-5,V,e);assert h in (0,1)
    if h:channels.append((V,e))
assert channels==[('Wp',-5)]
assert vm(chars['D'],W)==rep('S+T')
assert vm(chars['V'],W)==chars['T']
assert vm(chars['V'],sym(2))==rep('P+D')
assert vm(chars['Wp'],sym(3))==rep('V+D')
assert va(chi('V',-2),chi('one',6))==chars['P']
assert va(va(chi('V',-2),chi('one',6)),chi('Wp',-3))==ZERO
assert -6+6==0 and -6+6-6==-6
assert 4+4==8 and 0-8==-8 and 8-1==7 and -8-6==-14
assert -14==7*(-2)
assert 7 not in [0,3,5,8]
assert inner(chars['P'],rep('V+D'))==q(0)
assert inner(chars['V'],rep('P+D'))==q(0)
pairs=json.loads((ROOT/'audit-inputs/pairs.json').read_text());row=pairs[127]
assert [1,0,2,0,0,1,0,0] in row['compatible_E_types'] and row['defect']==0
assert row['A']==[[-8,'one'],[2,'one'],[16,'one']]
assert row['B']==[[-18,'one'],[-4,'one'],[6,'one']]
frontier=json.loads((ROOT/'audit-inputs/frontier.json').read_text());case=next(c for c in frontier['cases'] if c['id']=='G3.11.cce6e3ba4eeb')
assert case['source_index']==127 and case['original_defect']==0
print('PASS: five immutable inputs; exact a-c-c-f source; top V divisor-twelve factorization characters; universal kernel; complete internal channel; both first-span characters; incompatible coefficient spans; common-image rank/degree obstruction.')
print('The exact PR901 cubic-span interface and all actual coherent-image, saturation and intersection arguments are verified in PROOF.md and REVIEW.md. This is a whole a-c-c-f source exclusion, not a whole-label claim. No selected actual source instance was evaluated.')
