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
entries=json.loads((ROOT/'audit-inputs/manifest.json').read_text());assert len(entries)==8
for e in entries:
    b=(ROOT/'audit-inputs'/e['name']).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob']

def hom(U,degree,V,target_degree):
    n=target_degree-degree
    return 0 if n<0 else inner(chars[U],vm(chars[V],sym(n)))[0]
kernels=[[("A",-8)],[("W",-7),("one",-10)],[("W",-9),("one",-6)],[("Wp",-3),("one",-18)],[("one",-6),("one",-8),("one",-10)]]
expected=[[("A",-8,"D",-4)],[("W",-7,"D",-4),("one",-10,"one",-10)],[("W",-9,"D",-4)],[("one",-18,"D",-4),("one",-18,"Wp",-5)],[("one",-8,"D",-4),("one",-10,"one",-10)]]
for kernel,want in zip(kernels,expected):
    got=[]
    for U,d in kernel:
        for V,e in [("D",-4),("Wp",-5),("V",-6),("Wp",-7),("one",-10)]:
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

assert hashlib.sha256((ROOT/'audit-inputs/PR888.md').read_bytes()).hexdigest()=='1740dd7bb504cb49c726952373f74700e3396b7a8a94a1f89e7e3f6121775e38'
# Constant first span: every complementary W(-5) channel is absent.
for V,e in [('Wp',-3),('V',-4),('Wp',-5),('one',-8)]:assert hom('W',-5,V,e)==0
assert hom('W',-5,'D',-2)==1
# After actual constant projection, the top Wp(-3) is horizontal.
assert hom('Wp',-3,'one',2)==0 and hom('Wp',-3,'one',-8)==0
for V,e in [('V',-6),('Wp',-7),('one',-10)]:assert hom('Wp',-3,V,e)==0
# Rank-six temporary containment: O(-4) cannot inject in any residual row.
for V,e in [('D',-2),('Wp',-3),('V',-4),('Wp',-5),('one',-8)]:assert hom('one',-4,V,e)==0
assert hom('Wp',-3,'Wp',-3)==1 # the allowed new row is retained
assert hom('one',-18,'Wp',-5)==1
assert inner(chars['Wp'],sym(1))==q(0) and inner(chars['D'],sym(2))==q(0)
# Fixed polar and lower-row characters.
assert vm(chars['P'],W)==rep('Wp+T')
assert vm(chars['P'],sym(2))==rep('V+P+D')
assert vm(chars['T'],W)==rep('V+P+D')
assert vm(chars['A'],W)==rep('W+S')
assert sym(19)==rep('W+Wp+S+2T')
assert rep('Wp+T')!=rep('S')
for n in (8,10,18):assert inner(sym(n),chars['one'])==q(0)
assert hom('W',-3,'one',4)==0 and hom('one',-6,'one',4)==0
assert hom('one',-14,'one',4)==0 and hom('one',-14,'one',-6)==0
assert sym(7)==rep('Wp+T')
C=rep('V+P+D')
assert vm(W,W)==rep('one+A')
Vchi=va(C,vm(W,W));assert Vchi==rep('one+A+V+P+D')
positive_rank2=[vm(W,sym(7)),vm(chars['Wp'],sym(7)),va(sym(2),sym(12)),va(sym(4),sym(10)),va(sym(6),sym(8))]
expected=['V+2P+D','one+A+V+P+D','one+2A+P+D','A+V+2D','V+2P+D']
assert all(x==rep(y) for x,y in zip(positive_rank2,expected))
assert [i for i,x in enumerate(positive_rank2) if x==Vchi]==[1]
assert -20+6==-14 and -14-18==-32 and 18+2*7==32
assert 8+22-18==12
assert -54+32+12==-10 # defect12 gives rank10 pure O(-1)
assert 10>8 and sym(7)==rep('Wp+T')
M2=rep('A+2V+3P+4D');M3=rep('3Wp+3S+6T')
assert sym(16)==rep('V+P+2D')
assert vm(chars['Wp'],sym(5))==rep('A+P+D')
assert vs(M2,va(sym(16),vm(chars['Wp'],sym(5))))==C
Q1=vs(M3,vm(M2,W));U1=vk(-1,va(sym(15),vm(chars['Wp'],sym(4))))
assert Q1==vk(-1,rep('W+2S+3T'))
assert U1==vk(-1,rep('2S+3T'))
assert vs(Q1,U1)==vk(-1,W)
# Exhaustive small H1-budget atoms: (j-1)dim coefficient<=12 and center parity.
B=dec(C);allowed=[]
for j in range(2,14):
    for name in names:
        U=chars[name];d=int(U[0][0])
        if (j-1)*d>12 or U[1]!=q((-1)**j*d):continue
        h1=dec(vm(U,sym(j-2)))
        if all(0<=a<=b for a,b in zip(h1,B)):
            allowed.append((j,name))
expected_atoms=[(2,'V'),(2,'P'),(2,'D'),(3,'Wp'),(3,'T'),(4,'V'),(4,'P'),(5,'Wp'),(6,'one'),(7,'W'),(8,'one'),(10,'one')]
assert allowed==expected_atoms
expected_h1_twist1=['0','0','0','Wp','T','T','Wp+T','T','S','S+T','T','Wp+T']
for (j,name),expected in zip(allowed,expected_h1_twist1):
    h=ZERO if j==2 else vm(chars[name],sym(j-3))
    assert h==rep(expected)
    assert inner(h,W)==q(0)
pairs=json.loads((ROOT/'audit-inputs/pairs.json').read_text());row=pairs[127]
assert [1,0,1,0,1,1,0,0] in row['compatible_E_types'] and len(row['compatible_E_types'])==13 and row['defect']==0
assert row['A']==[[-8,'one'],[2,'one'],[16,'one']]
assert row['B']==[[-18,'one'],[-4,'one'],[6,'one']]
frontier=json.loads((ROOT/'audit-inputs/frontier.json').read_text())
case=next(c for c in frontier['cases'] if c['id']=='G3.11.cce6e3ba4eeb')
assert case['source_index']==127 and case['original_defect']==0
print('PASS: eight immutable blobs and exact PR888 hash; a-c-e-f source identity; all five kernels and every changed internal channel; horizontal Wp block; retained Wp(-3) channel and forbidden O(-4) injection; scalar-row saturation and complete twist-one support obstruction.')
print('Actual maps, intersections, saturation and dependency interfaces are proved in PROOF.md. No selected actual source data, point, parameter, derivative, matrix or instance rank was evaluated.')
