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

# Exactly the fixed character identities in the proof.
assert sym(18)==rep('A+V+2P+D')
assert sym(19)==rep('W+Wp+S+2T')
assert vm(chars['P'],W)==rep('Wp+T')
assert vm(chars['P'],sym(3))==rep('S+2T')
assert vm(chars['T'],sym(2))==rep('Wp+S+2T')
assert vm(chars['V'],W)==chars['T']
assert vm(chars['Wp'],W)==chars['P']
assert vm(chars['A'],W)==rep('W+S')

atoms=[(4,'A','A','0'),(4,'V','V','0'),(4,'D','D','0'),
       (5,'S','A+D','S'),(6,'one','A','W'),(7,'W','A+D','W+S'),
       (7,'Wp','V+D','T'),(8,'one','D','S'),(14,'one','A+V+D','S+T')]
budget=dec(rep('A+V+D'))
# The proof's complete dimension/parity eligibility list, not a support search.
eligible={'one':(4,6,8,10,12,14),'A':(4,6),'V':(4,6),'P':(4,),
          'D':(4,),'W':(5,7),'Wp':(5,7),'S':(5,),'T':()}
accepted={(j,R) for j,R,_,_ in atoms}
assert len(accepted)==9
for R,js in eligible.items():
    dim=chars[R][0][0]
    assert js==tuple(j for j in range(4,15)
                    if (j-3)*dim<=11 and chars[R][1][0]==(-1)**j*dim)
    for j in js:
        val=dec(vm(chars[R],sym(j-4)))
        assert all(0<=a<=b for a,b in zip(val,budget))==((j,R) in accepted)
for j,R,b,t in atoms:
    assert vm(chars[R],sym(j-4))==rep(b)
    assert (ZERO if j==4 else vm(chars[R],sym(j-5)))==rep(t)
assert {(j,R) for j,R,_,t in atoms if dec(rep(t))[names.index('W')]}=={(6,'one'),(7,'W')}

kernels={0:[[(3,'Wp'),(4,'V'),(7,'W')],[(3,'Wp'),(4,'V'),(6,'one'),(8,'one')]],
         1:[[(3,'Wp'),(3,'T'),(7,'W')],[(3,'Wp'),(3,'T'),(6,'one'),(8,'one')]]}
for m,rows in kernels.items():
    for row in rows:
        rank=degree=0; h1=chi=ZERO
        for j,R in row:
            dim=chars[R][0][0];rank+=dim;degree-=j*dim
            if j>=4:h1=va(h1,vm(chars[R],sym(j-4)))
            if j==3:chi=va(chi,chars[R])
            elif j>=5:chi=vs(chi,vm(chars[R],sym(j-5)))
        assert rank==7+3*m and degree==-32-6*m
        assert h1==rep('A+V+D' if m==0 else 'A+D')
        assert chi==vs(rep('Wp' if m==0 else 'Wp+T'),rep('W+S'))

# All atomic internal Hom checks are for the explicitly declared kernels/targets.
def hom(atom,target):
    j,R=atom;n,U=target
    return 0 if j<n else inner(chars[R],vm(chars[U],sym(j-n)))[0]
cases=[
 ('D-tail-h',0,[(4,'D'),(7,'Wp'),(10,'one'),(12,'one')],{((7,'W'),(4,'D')),((8,'one'),(4,'D'))}),
 ('D-tail-g',0,[(4,'D'),(7,'Wp'),(11,'W')],{((7,'W'),(4,'D')),((8,'one'),(4,'D'))}),
 ('be',0,[(5,'T'),(7,'Wp'),(12,'one')],set()),
 ('ce',1,[(6,'V'),(7,'Wp'),(12,'one')],set()),
 ('ee',0,[(4,'P'),(7,'Wp'),(12,'one')],set()),
]
checks=0
for name,m,targets,nonzero in cases:
    observed=set()
    for atom in set(a for row in kernels[m] for a in row):
        for target in targets:
            val=hom(atom,target);checks+=1
            assert val in (0,1)
            if val:observed.add((atom,target))
    assert observed==nonzero,(name,observed)

# Polar characters, derived additively from the exact derivative sequences.
chi_o8=vs(vs(sym(18),rep('2P')),sym(4))
chi1_o8=vs(sym(19),sym(3))
assert chi_o8==rep('A+V')
assert vs(chi1_o8,vm(chi_o8,W))==vs(rep('Wp+T'),chars['S'])
chi_w7=vs(vs(sym(18),rep('2P')),vm(W,sym(3)))
chi1_w7=vs(sym(19),vm(W,sym(2)))
assert chi_w7==chars['V']
assert vs(chi1_w7,vm(chi_w7,W))==rep('Wp+T')
assert inner(chars['P'],vm(chars['Wp'],W))==q(1)
assert inner(chars['P'],vm(chars['T'],W))==q(1)
assert inner(chars['W'],vm(chars['D'],sym(3)))==q(1)
assert inner(chars['one'],vm(chars['D'],sym(4)))==q(1)

# Exact membership and identities only, not recomputation of any envelope.
import json
from pathlib import Path
root=Path(__file__).resolve().parent
catalog=json.loads((root/'audit-inputs/one-one-endpoint-necessary-pairs.json').read_text())
labels=json.loads((root/'audit-inputs/rank-three-quotient-frontier-144.json').read_text())['cases']
expected={113:('G3.11.ad509d55173f',[[-10,'one'],[2,'one'],[16,'one']],[[-18,'one'],[-4,'one'],[8,'one']]),
          125:('G3.11.ea6bced3bddf',[[-10,'one'],[4,'one'],[16,'one']],[[-18,'one'],[-6,'one'],[8,'one']]),
          127:('G3.11.cce6e3ba4eeb',[[-8,'one'],[2,'one'],[16,'one']],[[-18,'one'],[-4,'one'],[6,'one']])}
targets={113:[(0,0,0,0,1,1,0,1),(0,0,1,0,1,0,0,1),(0,1,0,0,1,0,0,1)],
         125:[(0,0,0,0,2,0,0,1)],127:[(0,0,0,0,1,1,0,1),(0,0,0,0,1,0,1,0)]}
for ix,(label,Aq,Bq) in expected.items():
    original=catalog[ix]
    assert original['A']==Aq and original['B']==Bq and original['defect']==0
    stable=[r for r in labels if r['id']==label]
    assert len(stable)==1 and stable[0]['source_index']==ix
    assert stable[0]['A']==Aq and stable[0]['B']==Bq and stable[0]['original_defect']==0
    assert len(original['compatible_E_types'])==(13 if ix==127 else 10)
    assert all(list(t) in original['compatible_E_types'] for t in targets[ix])
print('PASS: nine declared kernel atoms; four exact kernels; %d fixed atomic Hom checks; polar characters; all six original source-edge identities.'%checks)
print('No source/model evaluation, support search, all-twist envelope, or current frontier count was performed.')
