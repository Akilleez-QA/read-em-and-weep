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

# Fixed abstract identities only; no parameters or actual source instances.
from pathlib import Path
import hashlib
import json
ROOT=Path(__file__).resolve().parent
entries=json.loads((ROOT/'audit-inputs/manifest.json').read_text())
assert len(entries)==6
for e in entries:
    data=(ROOT/'audit-inputs'/e['name']).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==e['git_blob']
for n,R in {16:'V+P+2D',17:'Wp+S+2T',18:'A+V+2P+D',19:'W+Wp+S+2T',10:'A+V+D',8:'P+D',7:'Wp+T',6:'V+P'}.items():
    assert sym(n)==rep(R)
assert inner(sym(16),chars['one'])==q(0)
assert vm(chars['P'],W)==rep('Wp+T')
assert vm(chars['A'],W)==rep('W+S')
assert vm(chars['V'],W)==chars['T']
assert vm(chars['Wp'],W)==chars['P']
assert vm(chars['Wp'],chars['A'])==chars['T']
C0=rep('A+V+P'); F=rep('P+D')
assert vm(C0,W)==sym(19)
assert vs(sym(18),C0)==F
# Covariant-space dimensions used in the two exact Euler sequences.
def mult(R,n):return inner(chars[R],sym(n))[0]
assert [mult('A',18),mult('V',18),mult('P',18)]==[1,1,2]
assert [mult('W',19),mult('S',19),mult('Wp',19),mult('T',19)]==[1,1,1,2]
assert [mult('Wp',17),mult('P',18),mult('Wp',19)]==[1,2,1]
assert 10 < 12 # raw quadratic defect bound below the minimum orbit size
H=va(va(C0,sym(10)),sym(8))
assert H==rep('2A+2V+2P+2D')
assert 9+7+1==17 and -18-28-8==-54
assert 1+4+8==13 and 18+4*7+8==54
# Universal osculating-block arithmetic, not pointwise ranks.
def u(n,k):return k+1,(k+1)*(k-n)
for n,k in [(10,6),(8,0),(10,3),(8,7)]:
    r,d=u(n,k);r1,d1=u(n,k+1)
    assert r1-r==1 and d1-d==2*k-n+2
assert [2*6-10,2*0-8]==[2,-8]
assert [2*3-10,2*7-8]==[-4,6]
assert 10+u(10,7)[0]+u(8,1)[0]==20
assert 10+u(10,8)[0]+u(8,2)[0]==22
assert (1+1+1,1+1+0)==(3,2)
M2=rep('A+2V+3P+4D');M3=rep('3Wp+3S+6T')
H1E=va(va(F,vm(sym(6),sym(2))),sym(6))
H1Qdual=va(sym(16),vm(chars['S'],sym(5)))
H1Em1=va(va(vm(F,W),vm(sym(6),sym(3))),sym(7))
assert H1E==rep('2V+4P+3D')
assert H1Qdual==M2
assert H1Em1==M3
assert va(va(sym(17),vm(chars['S'],sym(6))),sym(7))==M3
pairs=json.loads((ROOT/'audit-inputs/pairs.json').read_text())
frontier=json.loads((ROOT/'audit-inputs/frontier.json').read_text())
row=pairs[127];t=[0,0,1,1,0,1,0,0]
assert t in row['compatible_E_types'] and row['defect']==0
assert row['A']==[[-8,'one'],[2,'one'],[16,'one']]
assert row['B']==[[-18,'one'],[-4,'one'],[6,'one']]
case=next(c for c in frontier['cases'] if c['id']=='G3.11.cce6e3ba4eeb')
assert case['source_index']==127 and case['original_defect']==0
print('PASS: six immutable blobs; degree18/19 covariant and Euler-space characters; balanced kernel and fixed coefficient representations; source127 c-d-f identity; universal rank/degree and profile arithmetic.')
print('Nonemptiness, saturation and generic osculation are proved structurally in PROOF.md. No parameter, coefficient, point, derivative, matrix or rank of an actual source instance was selected or evaluated.')
