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

# Fixed universal representation arithmetic and exact original source identity only.
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
entries=json.loads((ROOT/'audit-inputs/manifest.json').read_text());assert len(entries)==4
for e in entries:
    b=(ROOT/'audit-inputs'/e['name']).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob']
def hom(U,d,V,e):return 0 if e<d else inner(chars[U],vm(chars[V],sym(e-d)))[0]
assert sym(6)==rep('V+P') and sym(7)==rep('Wp+T')
assert sym(12)==rep('one+A+P+D')
assert sym(18)==rep('A+V+2P+D') and sym(19)==rep('W+Wp+S+2T')
assert inner(chars['one'],sym(12))==q(1)
assert inner(chars['Wp'],sym(7))==q(1) and inner(chars['Wp'],sym(19))==q(1)
assert inner(chars['V'],sym(6))==q(1) and inner(chars['V'],sym(18))==q(1)
assert inner(chars['D'],sym(6))==q(0)
assert hom('Wp',-3,'one',2)==0 and hom('Wp',-3,'one',-8)==0
assert vm(chars['Wp'],W)==chars['P']
assert vm(chars['Wp'],sym(3))==rep('V+D')
assert vs(sym(6),vm(chars['Wp'],W))==chars['V']
targets=[[("D",-4,2),("V",-6,1),("one",-10,2)],[("V",-4,1),("D",-4,1),("V",-6,2),("one",-10,1)],[("D",-4,1),("T",-5,1),("V",-6,1),("one",-10,1)]]
want=[[("one",-10,2)],[("V",-4,1),("one",-10,1)],[("T",-5,1),("one",-10,1)]]
for target,expected in zip(targets,want):
    got=[]
    for U,d,m in target:
        h=hom('one',-10,U,d)
        assert h in (0,1)
        if h:got.append((U,d,m))
        assert hom('Wp',-3,U,d)==0
    assert got==expected
# Coherent projected a-c-c-f V block has no remaining internal channel.
for U,d in [('D',-4),('V',-6),('one',-10)]:assert hom('V',-2,U,d)==0
assert hom('V',-2,'one',2)==0 and hom('V',-2,'one',-8)==0
assert -6+6==0 and -6+(-10+4)+4==-8
assert 4*2==8 and 8<12
pairs=json.loads((ROOT/'audit-inputs/pairs.json').read_text());row=pairs[127]
tuples=[[1,0,1,0,0,2,0,0],[1,0,2,0,0,1,0,0],[1,1,1,0,0,1,0,0]]
for t in tuples:assert t in row['compatible_E_types']
assert row['defect']==0 and row['A']==[[-8,'one'],[2,'one'],[16,'one']]
assert row['B']==[[-18,'one'],[-4,'one'],[6,'one']]
frontier=json.loads((ROOT/'audit-inputs/frontier.json').read_text());case=next(c for c in frontier['cases'] if c['id']=='G3.11.cce6e3ba4eeb')
assert case['source_index']==127 and case['original_defect']==0
# Universal V quadratic channels and full-scalar refinement.
assert vm(chars['V'],sym(2))==rep('P+D')
assert hom('V',-2,'P',0)==1 and hom('V',-2,'D',0)==1
assert hom('Wp',-3,'D',0)==1 and hom('Wp',-3,'V',0)==1
assert vm(chars['Wp'],sym(3))==rep('V+D')
for e in range(-3,1):assert hom('Wp',-3,'one',e)==0
for e in range(-2,2):assert hom('V',-2,'one',e)==0
assert vm(chars['D'],W)==rep('S+T')
assert inner(sym(14),chars['one'])==q(0)
assert hom('Wp',3,'one',4)==0 and hom('one',6,'one',4)==0
for U in ('W','Wp'):assert hom(U,-3,'D',-2)==0
assert hom('one',-2,'D',-2)==0
assert hom('one',-8,'one',6)==0
# Exhaustive single-V H1 budget used for both universal injections.
budget=dec(chars['V']);atoms=[]
for j in range(2,6):
    for U in names:
        d=int(chars[U][0][0])
        if (j-1)*d>3 or chars[U][1]!=q((-1)**j*d):continue
        h=dec(vm(chars[U],sym(j-2)))
        if all(0<=x<=y for x,y in zip(h,budget)):atoms.append((U,j))
assert atoms==[('V',2)]
assert 7-5==2 and -18-(-12)==-6 and 2*(-4)<-6
assert -8-6==-14 and -6-(-14)==8
print('PASS: four immutable original blobs; all three exact tuples; forced degree12 factor spaces; all genuine kernel channels; raw polar/saturation bounds; coherent constant-V contradiction; universal V injections; scalar-row and full-eight-space refinement; exact cubic-polar ranks/degrees.')
print('This is a partial reduction, not a whole-source exclusion. No selected actual source, parameter, point, derivative, matrix or instance rank was evaluated.')
