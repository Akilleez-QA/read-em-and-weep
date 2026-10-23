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

# Bounded universal identities only; no source-instance evaluation.
assert sym(4)==chars['D']
assert sym(6)==rep('V+P')
assert sym(7)==rep('Wp+T')
assert sym(8)==rep('P+D')
assert sym(18)==rep('A+V+2P+D')
assert sym(19)==rep('W+Wp+S+2T')
assert vm(chars['T'],W)==rep('V+P+D')
assert vm(chars['Wp'],sym(2))==chars['T']
assert vm(chars['Wp'],sym(3))==rep('V+D')
assert vm(chars['P'],W)==rep('Wp+T')
assert vm(chars['V'],W)==chars['T']
assert vm(chars['A'],W)==rep('W+S')

atoms=[(4,'A','A','0'),(4,'P','P','0'),(4,'D','D','0'),
 (5,'Wp','P','Wp'),(5,'S','A+D','S'),(6,'one','A','W'),
 (6,'V','P+D','T'),(7,'W','A+D','W+S'),(8,'one','D','S'),
 (9,'Wp','A+P+D','S+T'),(12,'one','P+D','Wp+T')]
budget=dec(rep('A+P+D'))
eligible={'one':(4,6,8,10,12,14),'A':(4,6),'V':(4,6),
 'P':(4,6),'D':(4,),'W':(5,7,9),'Wp':(5,7,9),'S':(5,),'T':(5,)}
accepted={(j,R) for j,R,_,_ in atoms}
for R,js in eligible.items():
 dim=chars[R][0][0]
 assert js==tuple(j for j in range(4,16) if (j-3)*dim<=12 and chars[R][1][0]==(-1)**j*dim)
 for j in js:
  val=dec(vm(chars[R],sym(j-4)))
  assert all(0<=a<=b for a,b in zip(val,budget))==((j,R) in accepted),(j,R,val)
for j,R,b,t in atoms:
 assert vm(chars[R],sym(j-4))==rep(b)
 assert (ZERO if j==4 else vm(chars[R],sym(j-5)))==rep(t)
assert {(j,R) for j,R,_,t in atoms if dec(rep(t))[names.index('W')]}=={(6,'one'),(7,'W')}
kernels=[[(4,'P'),(7,'W')],[(3,'Wp'),(5,'Wp'),(7,'W')],
 [(4,'P'),(6,'one'),(8,'one')],[(3,'Wp'),(5,'Wp'),(6,'one'),(8,'one')]]
for row in kernels:
 rank=degree=0;h1=chi=ZERO
 for j,R in row:
  dim=chars[R][0][0];rank+=dim;degree-=j*dim
  if j>=4:h1=va(h1,vm(chars[R],sym(j-4)))
  if j==3:chi=va(chi,chars[R])
  elif j>=5:chi=vs(chi,vm(chars[R],sym(j-5)))
 assert (rank,degree)==(6,-30)
 assert h1==rep('A+P+D')
 assert chi==vk(-1,rep('W+S'))
def hom(atom,target):
 j,R=atom;n,U=target
 return 0 if j<n else inner(chars[R],vm(chars[U],sym(j-n)))[0]
nonzero=set()
for a in set(a for row in kernels for a in row):
 for b in [(4,'D'),(6,'V'),(10,'one'),(12,'one')]:
  h=hom(a,b)
  assert h in (0,1)
  if h:nonzero.add((a,b))
assert nonzero=={((7,'W'),(4,'D')),((8,'one'),(4,'D'))}
C=vs(vs(sym(18),rep('V+P')),sym(4))
L=vs(vs(sym(19),sym(3)),vm(C,W))
assert C==rep('A+P') and L==vs(chars['T'],chars['S'])
C=vs(vs(sym(18),rep('V+P')),vm(W,sym(3)))
L=vs(vs(sym(19),vm(W,sym(2))),vm(C,W))
assert C==chars['P'] and L==chars['T']
assert inner(sym(8),chars['one'])==q(0)
assert [n for n in range(7) if inner(sym(n),W)!=q(0)]==[1]
assert inner(sym(5),chars['Wp'])==q(0)
assert inner(sym(1),chars['Wp'])==q(0)
assert inner(chars['Wp'],vm(W,sym(6)))==q(1)
for target in [(2,'D'),(4,'V'),(8,'one'),(10,'one')]:
 assert hom((4,'one'),target)==0
# Original exact source membership, not a frontier recomputation.
import json
p=__import__('pathlib').Path(__file__).resolve().parent/'audit-inputs'
c=json.loads((p/'one-one-endpoint-necessary-pairs.json').read_text())[113]
l=json.loads((p/'rank-three-quotient-frontier-144.json').read_text())['cases']
assert c['A']==[[-10,'one'],[2,'one'],[16,'one']] and c['defect']==0
assert [0,0,1,0,0,1,0,1] in c['compatible_E_types'] and len(c['compatible_E_types'])==10
assert [r['source_index'] for r in l if r['id']=='G3.11.ad509d55173f']==[113]
print('PASS: 11 declared support atoms; four exact kernels; internal Hom support; both polar characters; rank-one-channel obstruction; original cf membership.')
print('No selected actual source evaluation, search, scan, envelope, or frontier count.')
