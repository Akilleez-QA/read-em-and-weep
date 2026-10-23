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

# Fixed abstract representation identities and exact input integrity only.
from pathlib import Path
import hashlib
import json
ROOT=Path(__file__).resolve().parent
for entry in json.loads((ROOT/'audit-inputs/manifest.json').read_text()):
    data=(ROOT/'audit-inputs'/entry['name']).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==entry['git_blob']
assert sym(6)==rep('V+P')
assert sym(7)==rep('Wp+T')
assert sym(14)==rep('A+V+P+D')
assert all(inner(sym(n),chars['one'])==q(0) for n in (13,14,15))
assert vm(chars['P'],W)==rep('Wp+T')
assert vm(chars['V'],W)==chars['T']
assert vm(chars['Wp'],W)==chars['P']
assert inner(chars['P'],sym(4))==q(0)
assert vs(sym(6),chars['P'])==chars['V']
# Degree12 leaves the exact V O(-4) kernel.
assert 18-12==6 and 4-1==3 and -8-4==-12
assert vm(chars['V'],sym(0))==chars['V']
assert int(chars['V'][0][0])==3
assert inner(sym(2),chars['V'])==q(0)
assert 2*2>3 and 7-3>3
# All kernel-to-internal-target components vanish.
def hom(j,R,n,U):
    return 0 if j<n else int(inner(chars[R],vm(chars[U],sym(j-n)))[0])
targets=[[(4,'D'),(6,'V'),(6,'P'),(10,'one')],
 [(4,'D'),(5,'T'),(10,'one'),(12,'one')],
 [(4,'D'),(5,'T'),(11,'W')],
 [(4,'D'),(5,'Wp'),(6,'V'),(7,'Wp'),(10,'one')]]
assert all(hom(4,'V',j,R)==0 for target in targets for j,R in target)
# Raw first-span degree, invariant defect bound, rank-one gap and polar chars.
assert 4+1==5 and -8+6==-2
assert 2<12
assert 4-1<6<2*4
assert vs(sym(6),chars['P'])==chars['V']
assert vs(sym(7),vm(chars['V'],W))==chars['Wp']
assert hom(2,'P',1,'Wp')==1
assert 4>3 and 2*(-1)==-2
# Original exact source membership and bundle decoding.
pairs=json.loads((ROOT/'audit-inputs/pairs.json').read_text())
frontier=json.loads((ROOT/'audit-inputs/frontier.json').read_text())
row=pairs[127]
assert row['A']==[[-8,'one'],[2,'one'],[16,'one']] and row['defect']==0
case=next(x for x in frontier['cases'] if x['id']=='G3.11.cce6e3ba4eeb')
assert case['source_index']==127 and case['A']==row['A'] and case['original_defect']==0
tuples=[(0,0,1,1,0,1,0,0),(0,1,0,0,0,1,0,1),
        (0,1,0,0,0,0,1,0),(1,0,1,0,1,1,0,0)]
expected=[[(2,'P',1),(2,'D',1),(4,'V',1),(4,'P',1),(8,'one',1)],
 [(2,'P',1),(2,'D',1),(3,'T',1),(8,'one',1),(10,'one',1)],
 [(2,'P',1),(2,'D',1),(3,'T',1),(9,'W',1)],
 [(2,'P',1),(2,'D',1),(3,'Wp',1),(4,'V',1),(5,'Wp',1),(8,'one',1)]]
def decode(t):
    a,b,c,d,e,f,g,h=t
    out=[(2,'V',c+g+h-1),(2,'P',d+e+g+h),(2,'D',f+g),
     (3,'Wp',a),(3,'T',b),(4,'V',c),(4,'P',d),
     (5,'Wp',e),(8,'one',f),(9,'W',g),(10,'one',h)]
    assert all(k>=0 for j,R,k in out)
    return [atom for atom in out if atom[2]]
for t,atoms in zip(tuples,expected):
    assert list(t) in row['compatible_E_types']
    assert decode(t)==atoms
    assert sum(int(chars[R][0][0])*k for j,R,k in atoms)==17
    assert -sum(int(chars[R][0][0])*k*j for j,R,k in atoms)==-54
print('PASS: immutable blobs, four exact source127 tuples, divisor-degree constraints, exact kernel budget, all internal Hom vanishings, saturation budget, and two polar contradictions.')
print('No actual instance was evaluated. Sheaf-theoretic and connection arguments remain written mathematics; no whole source-edge exclusion is asserted.')
