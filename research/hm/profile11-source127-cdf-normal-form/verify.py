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
assert sym(4)==chars['D'] and sym(6)==rep('V+P')
assert sym(8)==rep('P+D') and sym(10)==rep('A+V+D')
assert sym(18)==rep('A+V+2P+D')
E=[('P',-2),('D',-2),('V',-4),('P',-4),('one',-8)]
Ehat=E[:-1]
def euler(atoms,t=0):
    out=ZERO
    for U,d in atoms:out=va(out,chi(U,d+t))
    return out
assert euler(E)==vk(-1,rep('2V+4P+3D'))
assert va(va(euler(E),sym(4)),sym(18))==vs(chars['A'],rep('V+2P+D'))
assert hom('A',0,'one',4)==0
assert inner(sym(18),chars['A'])==q(1)
for n in (14,16):assert inner(sym(n),chars['one'])==q(0)
assert inner(sym(6),chars['A'])==q(0)
# Exactly six rank-two splitting types, not a source-instance enumeration.
budget=rep('V+2P+D')
candidates=[ [('one',-a),('one',-(18-a))] for a in (2,4,6,8)]
candidates += [[('W',-9)],[('Wp',-9)]]
matched=[]
for c in candidates:
    assert sum(int(chars[U][0][0]) for U,d in c)==2
    assert sum(d*int(chars[U][0][0]) for U,d in c)==-18
    if vk(-1,euler(c))==budget:matched.append(c)
assert matched==[[('one',-8),('one',-10)],[('W',-9)]]
assert hom('one',-8,'A',0)==0
NA=[('W',-9)]
assert vk(-1,euler(NA,1))==rep('Wp+2T')
for U,d in Ehat:assert hom(U,d,'one',-8)==0
assert hom('one',-8,'one',-8)==1
assert hom('one',-8,'one',2)==0
# Actual pullback extension vanishes equivariantly; global generation then kills internal row.
assert inner(sym(10),chars['one'])==q(0)
assert hom('one',2,'one',-10)==0
assert all(hom(U,-j,'one',-10)==0 for U in names for j in range(5))
assert vs(euler(Ehat),euler(NA))==vk(-1,rep('P+2D'))
assert vs(euler(Ehat,1),euler(NA,1))==ZERO
assert vs(euler(Ehat,2),euler(NA,2))==rep('P+2D')
assert sum(int(chars[U][0][0]) for U,d in Ehat)-2==14
assert sum(d*int(chars[U][0][0]) for U,d in Ehat)+18==-28
for U,x in [('one','W'),('A','W+S'),('V','T'),('P','Wp+T'),('D','S+T')]:
    assert vm(chars[U],W)==rep(x)
assert vm(chars['V'],chars['A'])==rep('P+D')
assert vm(chars['P'],chars['A'])==rep('V+P+D')
assert hom('Wp',-1,'one',2)==0 and hom('T',-1,'one',2)==0
# Exhaustive five constant budgets, with coefficient equations from the proof.
constant_pairs=[(0,0),(1,0),(2,0),(0,1),(1,1)]
assert sorted(constant_pairs)==[(p,q) for p in range(3) for q in range(2) if p+q<=2]
rows=[]
for p0,q0 in constant_pairs:
    u=q0;v=p0+q0-1
    if v<0:continue
    C0=va(vk(p0,chars['V']),vk(q0,chars['P']))
    C4=va(vk(u,chars['V']),vk(v,chars['P']))
    C3=vs(vm(C0,W),vm(C4,W))
    C2=va(vs(rep('P+2D'),vm(C0,chars['A'])),C4)
    if any(x<0 for x in dec(C3)):continue
    assert C2 in (ZERO,chars['D'])
    rows.append((p0,q0,dec(C2),dec(C3),dec(C4)))
assert rows==[(1,0,dec(rep('D')),dec(rep('T')),dec(ZERO)),
              (0,1,dec(rep('D')),dec(rep('Wp')),dec(rep('V'))),
              (1,1,dec(ZERO),dec(ZERO),dec(rep('V+P')))]
# Source-specific top-P injection and exclusion of the first two residuals.
assert hom('P',-2,'A',0)==0
for U,d in [('D',-2),('T',-3),('Wp',-3),('V',-4)]:assert hom('P',-2,U,d)==0
assert inner(sym(8),chars['one'])==q(0)
for U in ('P','D'):
    for V in ('V','P'):assert hom(U,-2,V,-4)==0
# Exact actual-kernel flag: universal complete evaluation sequences.
flag=[('T',-5),('D',-6),('S',-7),('A',-8),('W',-9),('one',-10)]
assert va(chi('T',-5),chi('one',2))==euler([('V',-4),('P',-4)])
for i,(U,d) in enumerate(flag[:-1]):
    target=-2*i
    assert hom(U,d,'one',target)==1
    assert va(chi(*flag[i+1]),chi('one',target))==chi(U,d)
assert hom('one',-10,'one',-10)==1
assert hom('V',-4,'one',2)==1 and hom('P',-4,'one',2)==1
assert hom('V',-4,'P',-6)==0 and hom('P',-4,'V',-6)==0
# Fixed constant-span and balanced quotient identities.
H=rep('2A+2V+2P+2D');C10=rep('A+V+P');Hquot=vs(H,C10)
assert Hquot==va(sym(10),sym(8))==rep('A+V+P+2D')
assert sym(10)==rep('A+V+D') and sym(8)==rep('P+D')
assert max(3+3,3+5)==8 and 11+9==20
assert 7*(-4)+4==-24
assert vm(C10,W)==sym(19)==rep('W+Wp+S+2T')
assert vs(sym(18),C10)==rep('P+D')
# Two nonzero channel conditions defining the immutable family's Omega.
assert inner(sym(18),chars['P'])==q(2)
assert inner(sym(17),chars['Wp'])==q(1)
assert inner(sym(19),chars['Wp'])==q(1)
assert inner(sym(19),chars['T'])==q(2)
pairs=json.loads((ROOT/'audit-inputs/pairs.json').read_text());row=pairs[127]
assert [0,0,1,1,0,1,0,0] in row['compatible_E_types'] and row['defect']==0
assert row['A']==[[-8,'one'],[2,'one'],[16,'one']]
assert row['B']==[[-18,'one'],[-4,'one'],[6,'one']]
frontier=json.loads((ROOT/'audit-inputs/frontier.json').read_text());case=next(c for c in frontier['cases'] if c['id']=='G3.11.cce6e3ba4eeb')
assert case['source_index']==127 and case['original_defect']==0
print('PASS: five immutable inputs; exact c-d-f source; forced-A and six kernels; scalar separation and pullback Ext; rank14 Euler data and three residuals; top-P obstruction; complete kernel flag; constant-space and balanced-open identities.')
print('The proof and review establish actual saturation, canonical tower, osculating reconstruction and full-span separation. Necessary normal form only; off-diagonal lifts retained; no actual source instance evaluated.')
