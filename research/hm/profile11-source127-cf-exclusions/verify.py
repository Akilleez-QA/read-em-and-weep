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

# Fixed abstract characters and original catalog checks only.
from pathlib import Path
import json
import hashlib
ROOT=Path(__file__).resolve().parent
for e in json.loads((ROOT/'audit-inputs/manifest.json').read_text()):
    data=(ROOT/'audit-inputs'/e['name']).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==e['git_blob']
def hom(atom,target):
    j,R=atom; n,U=target
    return 0 if j<n else int(inner(chars[R],vm(chars[U],sym(j-n)))[0])
def budget(row):
    rank=degree=0;h1=chi=ZERO
    for j,R in row:
        d=int(chars[R][0][0]);rank+=d;degree-=j*d
        if j>=4:h1=va(h1,vm(chars[R],sym(j-4)))
        if j==3:chi=va(chi,chars[R])
        elif j>=5:chi=vs(chi,vm(chars[R],sym(j-5)))
    return rank,degree,h1,chi
assert sym(6)==rep('V+P') and sym(7)==rep('Wp+T')
assert sym(8)==rep('P+D')
assert sym(18)==rep('A+V+2P+D')
assert sym(19)==rep('W+Wp+S+2T')
assert inner(sym(8),chars['one'])==q(0)
# Entire-top hypothetical kernel and all changed tail targets.
tails=[[(10,'one'),(12,'one')],[(11,'W')]]
fulltop=[[(3,'T'),(4,'P'),(6,'one')],[(3,'Wp'),(3,'T'),(5,'Wp'),(6,'one')]]
for row in fulltop:
    rank,deg,h1,chi=budget(row)
    assert rank==11 and deg==-40 and h1==rep('A+P') and chi==vs(chars['T'],W)
    for tail in tails:assert all(hom(a,t)==0 for a in row for t in [(6,'V')]+tail)
assert 11<18<24
# The four high-F kernels from immutable PR861, rechecked in both sources.
rows=[[(4,'P'),(7,'W')],[(3,'Wp'),(5,'Wp'),(7,'W')],
      [(4,'P'),(6,'one'),(8,'one')],[(3,'Wp'),(5,'Wp'),(6,'one'),(8,'one')]]
for i,row in enumerate(rows):
    rank,deg,h1,chi=budget(row)
    assert (rank,deg)==(6,-30) and h1==rep('A+P+D') and chi==vk(-1,rep('W+S'))
    for tail in tails:
        target=[(4,'D'),(6,'V')]+tail
        actual=[(a,t,hom(a,t)) for a in row for t in target if hom(a,t)]
        expected=[((7,'W'),(4,'D'),1)] if i<2 else [((8,'one'),(4,'D'),1)]
        assert actual==expected
F=rep('V+P')
C8=vs(vs(sym(18),F),sym(4))
L8=vs(vs(sym(19),sym(3)),vm(C8,W))
assert C8==rep('A+P') and L8==vs(chars['T'],chars['S'])
C7=vs(vs(sym(18),F),vm(W,sym(3)))
L7=vs(vs(sym(19),vm(W,sym(2))),vm(C7,W))
assert C7==chars['P'] and L7==chars['T']
assert -14+18==4
assert vm(chars['T'],W)==rep('V+P+D')
assert vm(chars['Wp'],sym(2))==chars['T']
assert vm(chars['Wp'],sym(3))==rep('V+D')
assert [n for n in range(7) if inner(sym(n),W)==q(1)]==[1]
assert inner(sym(5),chars['Wp'])==q(0)
assert hom((-3,'Wp'),(-4,'one'))==0  # Wp O(3) -> O(4)
assert hom((-3,'Wp'),(6,'one'))==0   # Wp O(3) -> O(-6)
assert -18>-22
# Divisor branch, exact intersections, and all O(-4) residual Hom spaces.
for tail in tails:assert all(hom((3,'T'),t)==0 for t in [(4,'D'),(6,'V')]+tail)
assert -14+6==-8 and 8<12
for residual in [[(2,'D'),(4,'V'),(8,'one'),(10,'one')],[(2,'D'),(4,'V'),(9,'W')]]:
    assert all(hom((4,'one'),t)==0 for t in residual)
assert hom((-7,'W'),(-18,'one'))==1
assert hom((-7,'W'),(-4,'one'))==0 and hom((-7,'W'),(6,'one'))==0
# Uniform stabilizer exponents; not an actual point evaluation.
assert (-8)%10==2 and (-(-6))%10==6 and (-4)%10==6
assert 2!=6
# Exact defect/span/rank/degree budgets.
assert 17-7==10 and -54-(-14)==-40 and 30-9==21
assert 10+40-21==29 and 29-24<12
assert -40+24==-16 and 14+24==38 and 38-18==20
assert 13-2==11 and -54+38==-16
# Actual dual characters and both possible Sigma extensions.
M2=rep('A+2V+3P+4D');M3=rep('3Wp+3S+6T')
assert vs(vm(M3,sym(2)),vm(M2,sym(3)))==vs(chars['T'],rep('2W+S'))
assert sym(13)==rep('W+Wp+S+T') and sym(15)==rep('S+2T')
assert sym(16)==rep('V+P+2D')
assert vm(W,sym(17))==va(sym(16),sym(18))
assert vm(W,sym(14))==va(sym(13),sym(15))
assert vs(M2,va(sym(16),sym(18)))==chars['D']
chiR=va(vs(chars['T'],rep('2W+S')),va(sym(13),sym(15)))
assert chiR==vs(rep('Wp+S+4T'),W)
assert vs(chiR,vm(chars['D'],W))==vs(rep('Wp+3T'),W)
assert vm(rep('2Wp+T'),chars['A'])==rep('Wp+S+4T')
for R,out in [('W','W+S'),('Wp','T'),('S','W+S+T'),('T','Wp+S+2T')]:
    assert vm(chars[R],chars['A'])==rep(out)
# Complete fixed parity/dimension atom list for H1(R)=D.
eligible={'one':(2,4,6),'W':(3,),'Wp':(3,),'A':(2,),
 'V':(2,),'P':(2,),'S':(),'D':(2,),'T':()}
accepted={(2,'D'),(6,'one')}; D_budget=dec(chars['D'])
for R,js in eligible.items():
    dim=chars[R][0][0]
    assert js==tuple(j for j in range(2,8) if (j-1)*dim<=5 and chars[R][1][0]==(-1)**j*dim)
    for j in js:
        v=dec(vm(chars[R],sym(j-2)))
        assert all(0<=a<=b for a,b in zip(v,D_budget))==((j,R) in accepted)
assert inner(rep('2Wp+T'),chars['Wp'])==q(2)
assert inner(sym(7),chars['Wp'])==q(1)
# Exact source127 labels/tuples and decoder; no new frontier count.
pairs=json.loads((ROOT/'audit-inputs/pairs.json').read_text()); row=pairs[127]
frontier=json.loads((ROOT/'audit-inputs/frontier.json').read_text())
assert row['A']==[[-8,'one'],[2,'one'],[16,'one']] and row['defect']==0
assert row['B']==[[-18,'one'],[-4,'one'],[6,'one']]
case=next(c for c in frontier['cases'] if c['id']=='G3.11.cce6e3ba4eeb')
assert case['source_index']==127 and case['original_defect']==0
source_tuples=[(0,0,1,0,0,1,0,1),(0,0,1,0,0,0,1,0)]
def decode(t):
    a,b,c,d,e,f,g,h=t
    out=[(2,'V',c+g+h-1),(2,'P',d+e+g+h),(2,'D',f+g),
         (3,'Wp',a),(3,'T',b),(4,'V',c),(4,'P',d),
         (5,'Wp',e),(8,'one',f),(9,'W',g),(10,'one',h)]
    assert all(k>=0 for j,R,k in out)
    return [atom for atom in out if atom[2]]
expected=[[(2,'V',1),(2,'P',1),(2,'D',1),(4,'V',1),(8,'one',1),(10,'one',1)],
          [(2,'V',1),(2,'P',1),(2,'D',1),(4,'V',1),(9,'W',1)]]
for t,want in zip(source_tuples,expected):
    assert list(t) in row['compatible_E_types'] and decode(t)==want
    assert sum(k*int(chars[R][0][0]) for j,R,k in want)==17
    assert -sum(j*k*int(chars[R][0][0]) for j,R,k in want)==-54
print('PASS: eight immutable blobs; both exact source127 cf-family edges; every changed internal/quotient Hom interface; basepoint-free polar characters and exact intersections.')
print('PASS: stabilizer exponents; exact double-divisor degree budget; dual H1 and Euler characters; complete support alternatives; forced two Wp copies versus one.')
print('No actual HM/source instance was evaluated. Connection, torsion, saturation, and span arguments remain written mathematics; no whole-label or global conclusion is asserted.')
