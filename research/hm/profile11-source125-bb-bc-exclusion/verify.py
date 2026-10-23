#!/usr/bin/env python3
"""Fixed universal character identities and one original source identity only."""
if not __debug__:
    raise SystemExit("Run without -O: this verifier requires its assertion checks to be enabled.")

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

# Fixed universal identities only. No selected source map or coefficient is constructed.
def chi(j,R,t):
    d=t-j
    return vm(chars[R],sym(d)) if d>=0 else (ZERO if d==-1 else vk(-1,vm(chars[R],sym(-d-2))))
def rowchi(row,t):
    out=ZERO
    for j,R in row:out=va(out,chi(j,R,t))
    return out
def rd(row):
    return (sum(int(chars[R][0][0]) for j,R in row),-sum(j*int(chars[R][0][0]) for j,R in row))
def h1(row,t):
    out=ZERO
    for j,R in row:
        if t-j<=-2:out=va(out,vm(chars[R],sym(j-t-2)))
    return out
hom_checks=0
def hom(j,R,k,U,expected):
    global hom_checks
    got=q(0) if j<k else inner(chars[R],vm(chars[U],sym(j-k)))
    hom_checks+=1
    assert got==q(expected),(j,R,k,U,got,expected)

for n,r in [(6,'V+P'),(7,'Wp+T'),(8,'P+D'),(10,'A+V+D'),(12,'one+A+P+D'),(14,'A+V+P+D'),(18,'A+V+2P+D')]:
    assert sym(n)==rep(r)
for r,n,out in [('V',1,'T'),('P',1,'Wp+T'),('D',1,'S+T'),('V',2,'P+D'),('P',2,'V+P+D'),('P',3,'S+2T'),('W',5,'D+V+P'),('W',6,'Wp+2T'),('W',7,'V+2P+D'),('Wp',7,'one+A+V+P+D')]:
    assert vm(chars[r],sym(n))==rep(out)

BB=[(2,'P'),(3,'T'),(3,'T')]
BC=[(2,'V'),(2,'P'),(3,'T'),(4,'V')]
K=[(9,'W')]
for F in (BB,BC):
    assert rd(F)==(16,-44) and rd(F+[(10,'one')])==(17,-54)
    assert rowchi(F+[(10,'one')],0)==vk(-1,rep('2V+4P+3D'))
    assert va(rowchi(F+[(10,'one')],0),va(sym(6),sym(18)))==vs(chars['A'],rep('P+2D'))
    assert h1(F,1)==vk(2,chars['T'])
    assert vs(rowchi(F,0),rowchi(K,0))==vk(-1,rep('V+P+D'))
    assert vs(rowchi(F,1),rowchi(K,1))==chars['Wp']
    assert vs(rowchi(F,3),rowchi(K,3))==rep('Wp+S+4T')
    for j,R in F:
        hom(j,R,10,'one',0)
    assert (16-2,-44+18)==(14,-26)
assert (17+2,-54+6+18)==(19,-30)

# Forced high-A map and complete rank-two kernel alternatives.
hom(0,'A',-6,'one',0)
hom(0,'A',-18,'one',1)
hom(8,'one',0,'A',0)
hom(9,'W',10,'one',0)
assert h1(K,0)==vs(sym(18),chars['A'])
assert h1([(9,'Wp')],0)!=h1(K,0)
scalar_pairs=[[(a,'one'),(18-a,'one')] for a in (2,4,6,8)]
assert [row for row in scalar_pairs if h1(row,0)==h1(K,0)]==[[(8,'one'),(10,'one')]]
assert [d for d in range(1,19) if inner(chars['one'],sym(d))!=q(0)]==[12]
assert inner(chars['A'],sym(6))==q(0)

# Actual quotient cohomology and constant-space restrictions.
assert h1(K,0)==rep('V+2P+D')
assert h1(K,1)==rep('Wp+2T')
assert h1(K,2)==rep('D+V+P')
assert h1(BB,2)==ZERO and rowchi(BB,2)==chars['P']
assert h1(BC,2)==chars['V'] and va(rowchi(BC,2),h1(BC,2))==rep('V+P')
assert inner(vm(rep('V+P'),sym(2)),chars['D'])==q(2)
for h0 in (rep('V+2P+D'),rep('2V+2P+D')):
    assert inner(h0,chars['D'])==q(1)
assert vs(rep('V+2P+D'),vm(chars['P'],sym(2)))==chars['P']
assert vs(rep('2V+2P+D'),vm(chars['P'],sym(2)))==rep('V+P')
assert vs(rep('Wp+S+4T'),vm(chars['P'],sym(3)))==rep('Wp+2T')
assert vs(rep('Wp+2T'),vm(chars['P'],W))==chars['T']

# Top Wp and T actual derivative channels used after removing all constants.
hom(1,'Wp',-4,'one',0)
hom(1,'Wp',10,'one',0)
# Internal targets of the same or lower source degrees, represented by the largest degree.
for R in names:
    hom(1,'Wp',3,R,0)
    hom(2,'D',4,R,0)
hom(2,'D',12,'one',0)
hom(1,'T',-4,'one',1)
assert rd([(1,'T')])==(6,-6)
assert va(rowchi([(1,'T')],0),sym(6))==rep('V+P')
assert (10-6+1,-26+6-10)==(5,-30)
assert -30 > -10*5

# Nonzero quartic component and both final actual splitting deductions.
hom(9,'W',4,'V',1)
assert inner(chars['V'],vm(W,sym(5)))==q(1)
assert (14-4,-26)==(10,-26)
assert (10-4,-26+8)==(6,-18)
assert -18==-3*6
assert (7,-14)==rd([(2,'V'),(2,'P')])
assert (10,-26)==rd([(2,'P'),(3,'T')])
assert rowchi([(2,'P'),(3,'T')],3)==rep('Wp+2T')
# Residual rank-four increment6 obstruction.
hom(2,'P',-4,'one',1)
hom(4,'V',5,'T',0)
hom(4,'V',12,'one',0)
assert 6>4-1 and 6!=2*4
# Published complete-Sym6 internal and coherent-tail obstructions.
hom(3,'T',6,'V',0)
hom(3,'T',12,'one',0)
hom(4,'V',-4,'one',0)
hom(4,'V',10,'one',0)
hom(4,'V',0,'one',0)
assert 7+3>9

# Exact original source identities only, with immutable Git-blob verification.
root=Path(__file__).resolve().parent/'audit-inputs'
pins={'one-one-endpoint-necessary-pairs.json':'fe0afa410d89340d3082dc814277f89fbb582c19',
      'rank-three-quotient-frontier-144.json':'8b5971092f9ef762584912609fd5e9301c4e271d'}
data={}
for name,pin in pins.items():
    raw=(root/name).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==pin
    data[name]=json.loads(raw)
source=data['one-one-endpoint-necessary-pairs.json'][125]
Aq=[[-10,'one'],[4,'one'],[16,'one']]
Bq=[[-18,'one'],[-6,'one'],[8,'one']]
assert source['A']==Aq and source['B']==Bq and source['defect']==0
assert [0,2,0,0,0,0,0,1] in source['compatible_E_types']
assert [0,1,1,0,0,0,0,1] in source['compatible_E_types']
cases=[c for c in data['rank-three-quotient-frontier-144.json']['cases'] if c['id']=='G3.11.ea6bced3bddf']
assert len(cases)==1
case=cases[0]
assert case['source_index']==125 and case['original_defect']==0 and case['A']==Aq and case['B']==Bq
print(f'PASS: {hom_checks} fixed Hom checks, exact kernel/cohomology identities, and pinned source125 bb/bc identities.')
print('Two source exclusions only; no whole-label coverage or current frontier count is certified by this verifier.')
print('No selected actual source, coefficient, parameter, point, derivative, matrix, instance rank, scan, or large computation.')
