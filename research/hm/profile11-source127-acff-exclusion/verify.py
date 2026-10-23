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
entries=json.loads((ROOT/'audit-inputs/manifest.json').read_text());assert len(entries)==4
for e in entries:
    b=(ROOT/'audit-inputs'/e['name']).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob']
def hom(U,d,V,e):return 0 if e<d else inner(chars[U],vm(chars[V],sym(e-d)))[0]
def chi(U,d):
    if d>=0:return vm(chars[U],sym(d))
    if d==-1:return ZERO
    return vk(-1,vm(chars[U],sym(-d-2)))
assert sym(18)==rep('A+V+2P+D') and sym(19)==rep('W+Wp+S+2T')
assert sym(6)==rep('V+P') and sym(4)==chars['D']
for n in (14,16):assert inner(sym(n),chars['one'])==q(0)
assert inner(sym(6),chars['D'])==q(0) and inner(sym(6),chars['A'])==q(0)
assert inner(va(sym(4),sym(18)),chars['D'])==q(2)
budget=rep('A+V+2P');atoms=[]
for j in range(4,18):
    for U in names:
        d=int(chars[U][0][0])
        if d>4 or (j-3)*d>14 or chars[U][1]!=q((-1)**j*d):continue
        h=dec(vm(chars[U],sym(j-4)))
        if all(0<=x<=y for x,y in zip(h,dec(budget))):atoms.append((U,j))
assert atoms==[('A',4),('V',4),('P',4),('Wp',5),('one',6),('one',10)]
assert [dec(ZERO if j==4 else vm(chars[U],sym(j-5))) for U,j in atoms]==[dec(rep(x)) for x in ['0','0','0','Wp','W','T']]
kernel=[('one',-6),('Wp',-5),('one',-10)]
h12=ZERO;c3=ZERO;c1=ZERO
for U,d in kernel:
    h12=va(h12,vm(chars[U],sym(-d-4)))
    c3=va(c3,chi(U,d+3));c1=va(c1,chi(U,d+1))
assert h12==budget and c3==vk(-1,rep('W+Wp+T'))
assert c1==vk(-1,sym(17))==vk(-1,rep('Wp+S+2T'))
assert sum(int(chars[U][0][0]) for U,d in kernel)==4
assert sum(d*int(chars[U][0][0]) for U,d in kernel)==-26
target=[('D',-4),('Wp',-5),('V',-6),('one',-10)]
channels=[]
for U,d in kernel:
    for V,e in target:
        h=hom(U,d,V,e);assert h in (0,1)
        if h:channels.append((U,d,V,e))
assert channels==[('Wp',-5,'Wp',-5),('one',-10,'one',-10)]
# Quadratic first-polar Euler characters for both surviving images.
M0=va(va(chi('D',-2),chi('one',-8)),sym(18))
M1=va(M0,chi('Wp',-3));M11=va(va(va(chi('D',-1),chi('one',-7)),chi('Wp',-2)),sym(19))
assert M0==rep('A+P') and M1==chars['A']
assert M11==rep('W+S+T') and vs(M11,vm(chars['A'],W))==chars['T']
assert -10+18==8 and -10-6+18==2 and -10-8+18==0 and -10-6-8+18==-6
# All changed projection and trapped-linear channels.
assert hom('A',0,'one',4)==0 and hom('A',0,'one',-6)==0
assert hom('Wp',-3,'one',2)==0 and hom('Wp',-3,'one',-8)==0
assert hom('Wp',-3,'A',0)==0
for U,d in [('D',-4),('V',-6),('one',-10)]:assert hom('Wp',-3,U,d)==0
assert hom('D',-2,'T',-1)==1
assert vm(chars['T'],W)==rep('V+P+D')
assert vm(chars['Wp'],sym(3))==rep('V+D')
assert vm(chars['A'],sym(3))==rep('W+S+T')
pairs=json.loads((ROOT/'audit-inputs/pairs.json').read_text());row=pairs[127]
assert [1,0,1,0,0,2,0,0] in row['compatible_E_types'] and row['defect']==0
assert row['A']==[[-8,'one'],[2,'one'],[16,'one']]
assert row['B']==[[-18,'one'],[-4,'one'],[6,'one']]
frontier=json.loads((ROOT/'audit-inputs/frontier.json').read_text());case=next(c for c in frontier['cases'] if c['id']=='G3.11.cce6e3ba4eeb')
assert case['source_index']==127 and case['original_defect']==0
print('PASS: four immutable original blobs; exact a-c-f-f identity; strict-top D multiplicities; exhaustive six-atom high-D kernel budget; unique kernel at twists1/2/3; all internal channels; both first-polar characters; constant-A basepoint-free tests; trapped Wp linear-span identities.')
print('Actual images, saturation, projections and connection arguments are proved in PROOF.md. No selected actual source data, parameter, point, derivative, matrix or instance rank was evaluated.')
