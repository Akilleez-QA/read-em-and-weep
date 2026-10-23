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

# Only fixed universal characters and immutable source identities are checked.
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
entries=json.loads((ROOT/'audit-inputs/manifest.json').read_text());assert len(entries)==7
for e in entries:
    b=(ROOT/'audit-inputs'/e['name']).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob']

def hom(U,degree,V,target_degree):
    n=target_degree-degree
    return 0 if n<0 else inner(chars[U],vm(chars[V],sym(n)))[0]
kernels=[[("A",-8)],[("W",-7),("one",-10)],[("W",-9),("one",-6)],[("Wp",-3),("one",-18)],[("one",-6),("one",-8),("one",-10)]]
expected=[[("A",-8,"D",-4),("A",-8,"T",-5)],[("W",-7,"D",-4),("one",-10,"T",-5)],[("W",-9,"D",-4),("W",-9,"T",-5)],[("one",-18,"D",-4),("one",-18,"T",-5)],[("one",-8,"D",-4),("one",-10,"T",-5)]]
for kernel,want in zip(kernels,expected):
    got=[]
    for U,d in kernel:
        for V,e in [("D",-4),("T",-5),("W",-11)]:
            m=hom(U,d,V,e)
            assert m in (0,1)
            if m:got.append((U,d,V,e))
    assert got==want
    assert sum(int(chars[U][0][0]) for U,d in kernel)==3
    assert sum(d*int(chars[U][0][0]) for U,d in kernel)==-24
    h12=ZERO;chi3=ZERO
    for U,d in kernel:
        h12=va(h12,vm(chars[U],sym(-d-4))) if d<=-4 else h12
        if d+3>=0:chi3=va(chi3,vm(chars[U],sym(d+3)))
        elif d+3<=-2:chi3=vs(chi3,vm(chars[U],sym(-d-5)))
    assert h12==rep('A+V+P+D')
    assert chi3==vk(-1,rep('W+S+T'))
# Euler/polar identities and endpoint-specific disappearances.
assert vm(chars['P'],W)==rep('Wp+T')
assert vm(chars['P'],sym(2))==rep('V+P+D')
assert vm(chars['T'],W)==rep('V+P+D')
assert vm(chars['T'],sym(2))==rep('Wp+S+2T')
assert vm(chars['D'],W)==rep('S+T')
assert hom('one',-8,'D',-2)==0
assert hom('one',-8,'W',-9)==0
assert hom('T',-3,'one',-8)==0
assert hom('W',-5,'T',-3)==0
assert hom('W',-5,'W',-9)==0
for n in (8,10,18): assert inner(sym(n),chars['one'])==q(0)
assert hom('A',-4,'one',4)==0
assert hom('W',-3,'one',4)==0
assert hom('one',-6,'one',4)==0
assert hom('one',-14,'one',4)==0 and hom('one',-14,'one',-6)==0
assert sym(7)==rep('Wp+T')
assert inner(chars['D'],sym(2))==q(0) and inner(chars['T'],sym(1))==q(0)
assert inner(chars['A'],sym(16))==q(0)
assert [(e,int(hom('W',-9,'one',e))) for e in range(-9,1) if hom('W',-9,'one',e)]==[(-8,1)]
assert sym(8)==rep('P+D') and sym(10)==rep('A+V+D')
assert vs(rep('2A+2V+2P+2D'),rep('A+V+P'))==rep('A+V+P+2D')
assert vs(rep('A+V+P+2D'),sym(8))==sym(10)
# Exact character test intentionally does not exclude the final branch.
M2=rep('A+2V+3P+4D');M3=rep('3Wp+3S+6T')
assert va(va(rep('P+D'),vm(chars['A'],sym(4))),sym(16))==M2
assert vk(-1,va(vm(chars['A'],sym(3)),sym(15)))==vk(-1,rep('W+2S+3T'))
assert vs(M3,vm(M2,W))==vk(-1,rep('W+2S+3T'))
assert 11+5==16 and 16+3==19 and 13+3+2==18 and 19>18
# Exact original tuple and complete universe, not a realizability computation.
pairs=json.loads((ROOT/'audit-inputs/pairs.json').read_text());row=pairs[127]
assert [0,1,0,0,0,0,1,0] in row['compatible_E_types'] and len(row['compatible_E_types'])==13 and row['defect']==0
assert row['A']==[[-8,'one'],[2,'one'],[16,'one']]
assert row['B']==[[-18,'one'],[-4,'one'],[6,'one']]
frontier=json.loads((ROOT/'audit-inputs/frontier.json').read_text())
case=next(c for c in frontier['cases'] if c['id']=='G3.11.cce6e3ba4eeb')
assert case['source_index']==127 and case['original_defect']==0
print('PASS: seven immutable blobs; exact g-b source identity; five high-P kernel characters; every changed internal channel and endpoint vanishing; projected Euler-plane character tests; twist-one compatibility; nested constant-projection rank bounds.')
print('Coherent images, saturation, actual dual sequences and independent osculating directions are proved in PROOF.md. No selected source/model data or actual ranks were evaluated.')
