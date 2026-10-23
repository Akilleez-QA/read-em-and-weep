#!/usr/bin/env python3
"""Fixed universal character identities and one original source identity only."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import hashlib
import json

def q(a, b=0): return (Q(a), Q(b))
def plus(x, y): return (x[0]+y[0], x[1]+y[1])
def times(x, y): return (x[0]*y[0]+5*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def scale(k, x): return (k*x[0], k*x[1])
def total(xs):
    out = q(0)
    for x in xs: out = plus(out, x)
    return out
ZERO = (q(0),)*9
def va(x,y): return tuple(plus(a,b) for a,b in zip(x,y))
def vk(k,x): return tuple(scale(k,a) for a in x)
def vm(x,y): return tuple(times(a,b) for a,b in zip(x,y))
def vs(x,y): return va(x,vk(-1,y))
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
chars = {'one':sym(0),'W':W,'A':sym(2),'S':sym(3),'D':sym(4),'T':sym(5)}
chars['P'] = tuple(map(q,(4,4,-1,-1,-1,-1,1,1,0)))
chars['V'] = vs(sym(6),chars['P'])
chars['Wp'] = vs(vm(W,chars['P']),chars['T'])
names = ('one','W','Wp','A','V','P','S','D','T')
def inner(x,y): return scale(Q(1,120),total(scale(k,times(a,b)) for k,a,b in zip(sizes,x,y)))
assert all(inner(chars[a],chars[b]) == q(a==b) for a in names for b in names)
def rep(s):
    out = ZERO
    if s == '0': return out
    for term in s.split('+'):
        k = int(term[0]) if term[0].isdigit() else 1
        name = term[1:] if term[0].isdigit() else term
        out = va(out,vk(k,chars[name]))
    return out
def dec(x):
    out = [inner(x,chars[n]) for n in names]
    assert all(b==0 and a.denominator==1 for a,b in out)
    return tuple(int(a) for a,b in out)

# Fixed character identities used by the proof.
for n,s in [(6,'V+P'),(7,'Wp+T'),(8,'P+D'),(18,'A+V+2P+D'),(19,'W+Wp+S+2T')]:
    assert sym(n)==rep(s)
for R,n,s in [('P',1,'Wp+T'),('P',2,'V+P+D'),('P',3,'S+2T'),
              ('D',1,'S+T'),('T',1,'V+P+D'),('A',2,'one+A+D'),('V',2,'P+D')]:
    assert vm(chars[R],sym(n))==rep(s)

# The declared six atoms and their complete dimension/parity eligibility list.
atoms=[(4,'A','A','0'),(4,'V','V','0'),(4,'P','P','0'),
       (5,'Wp','P','Wp'),(6,'one','A','W'),(10,'one','V+P','T')]
eligible={'one':(4,6,8,10,12),'W':(5,7),'Wp':(5,7),'A':(4,6),
          'V':(4,6),'P':(4,),'S':(5,),'D':(4,),'T':()}
budget=dec(rep('A+V+P'))
accepted={(j,R) for j,R,_,_ in atoms}
for R,js in eligible.items():
    dim=chars[R][0][0]
    assert js==tuple(j for j in range(4,14)
                    if (j-3)*dim<=10 and chars[R][1][0]==(-1)**j*dim)
    for j in js:
        h=dec(vm(chars[R],sym(j-4)))
        assert all(0<=a<=b for a,b in zip(h,budget))==((j,R) in accepted)
for j,R,h,t in atoms:
    assert vm(chars[R],sym(j-4))==rep(h)
    assert (ZERO if j==4 else vm(chars[R],sym(j-5)))==rep(t)
assert [(j,R) for j,R,_,t in atoms if dec(rep(t))[names.index('W')]]==[(6,'one')]

kernels=[[(4,'V'),(4,'P'),(6,'one')],
         [(3,'Wp'),(4,'V'),(5,'Wp'),(6,'one')],
         [(3,'T'),(6,'one'),(10,'one')]]
for row in kernels:
    rank=degree=0; h=chi=ZERO
    for j,R in row:
        dim=chars[R][0][0]; rank+=dim; degree-=j*dim
        if j>=4: h=va(h,vm(chars[R],sym(j-4)))
        if j==3: chi=va(chi,chars[R])
        elif j>=5: chi=vs(chi,vm(chars[R],sym(j-5)))
    assert (rank,degree)==(8,-34)
    assert h==rep('A+V+P') and chi==vk(-1,W)

targets=[(4,'P'),(7,'Wp'),(10,'one'),(12,'one')]
expected=[{((4,'P'),(4,'P'))},{((5,'Wp'),(4,'P'))},
          {((10,'one'),(4,'P')),((10,'one'),(10,'one'))}]
checks=0
for row,ex in zip(kernels,expected):
    observed=set()
    for j,R in row:
        for t,U in targets:
            h=q(0) if j<t else inner(chars[R],vm(chars[U],sym(j-t)))
            assert h in (q(0),q(1)); checks+=1
            if h==q(1): observed.add(((j,R),(t,U)))
    assert observed==ex

# Exact first-polar characters for the three nonzero images.
for j,R,C,L in [(4,'P','A+V','Wp+T'),(5,'Wp','A+V','T'),(10,'one','A','Wp+T')]:
    c=vs(rep('A+V+P'),vm(chars[R],sym(j-4)))
    chi1=sym(19) if j==4 else vs(sym(19),vm(chars[R],sym(j-5)))
    assert c==rep(C) and vs(chi1,vm(c,W))==rep(L)
assert inner(chars['one'],sym(8))==q(0)
assert inner(chars['Wp'],sym(5))==q(0)
assert inner(chars['P'],vm(chars['A'],sym(2)))==q(0)
assert inner(chars['P'],vm(chars['V'],sym(2)))==q(1)
assert vs(sym(6),chars['P'])==chars['V']
assert vs(vm(chars['P'],W),sym(7))==ZERO
assert 6!=2*4 and not 6<=4-1

# Exact immutable original source and stable-label identities, not a new frontier.
root=Path(__file__).resolve().parent/'audit-inputs'
pins={'one-one-endpoint-necessary-pairs.json':'fe0afa410d89340d3082dc814277f89fbb582c19',
      'rank-three-quotient-frontier-144.json':'8b5971092f9ef762584912609fd5e9301c4e271d'}
data={}
for name,sha in pins.items():
    b=(root/name).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha
    data[name]=json.loads(b)
source=data['one-one-endpoint-necessary-pairs.json'][125]
Aq=[[-10,'one'],[4,'one'],[16,'one']]
Bq=[[-18,'one'],[-6,'one'],[8,'one']]
assert source['A']==Aq and source['B']==Bq and source['defect']==0
assert [0,0,0,0,1,1,0,1] in source['compatible_E_types']
case=[x for x in data['rank-three-quotient-frontier-144.json']['cases'] if x['id']=='G3.11.ea6bced3bddf']
assert len(case)==1 and case[0]['source_index']==125
assert case[0]['A']==Aq and case[0]['B']==Bq and case[0]['original_defect']==0
print('PASS: six kernel atoms, three kernels, %d fixed internal Hom checks, polar and Euler-channel identities, original source125 ef identity.'%checks)
print('No source/model evaluation, support search, all-twist envelope, or current frontier count was performed.')
