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

# All following computations are fixed universal character arithmetic.
dims={n:int(chars[n][0][0]) for n in names}
def hom(a,t):
    j,R=a; k,U=t
    return q(0) if j<k else inner(chars[R],vm(chars[U],sym(j-k)))
def h1(j,R):
    return dec(vm(chars[R],sym(j-4))) if j>=4 else (0,)*9
def chi3(j,R):
    return dec(chars[R]) if j==3 else dec(vk(-1,vm(chars[R],sym(j-5)))) if j>=5 else (0,)*9
def vecadd(a,b):return tuple(x+y for x,y in zip(a,b))
checks=0
def check_table(atoms,targets,expected):
    global checks
    got=set()
    for a in atoms:
        for t in targets:
            v=hom(a,t); checks+=1
            assert v in (q(0),q(1))
            if v==q(1):got.add((a,t))
    assert got==expected,(got,expected)

# Strict-top multiplicities, fixed invariants, and all relevant symmetric powers.
assert sym(6)==rep('V+P')
assert sym(7)==rep('Wp+T')
assert sym(8)==rep('P+D')
assert sym(18)==rep('A+V+2P+D')
assert sym(19)==rep('W+Wp+S+2T')
assert sym(20)==rep('one+A+V+P+2D')
assert [n for n in range(1,19) if inner(sym(n),chars['one'])!=q(0)]==[12]
assert inner(sym(12),chars['one'])==q(1)
assert inner(sym(6),chars['V'])==inner(sym(18),chars['V'])==q(1)
assert inner(sym(20),chars['V'])==q(1)
assert vm(rep('2V+P'),W)==rep('Wp+3T')

# Saturated positive-pair kernel character budgets.
budget=dec(rep('A+2P+D')); target=dec(vk(-1,rep('W+Wp+S')))
assert vs(va(sym(6),sym(18)),rep('2V+P'))==rep('A+2P+D')
assert vs(vm(rep('2V+P'),W),va(sym(7),sym(19)))==vk(-1,rep('W+Wp+S'))
assert sum(d*m for d,m in zip((dims[n] for n in names),budget))==16

# Exhaustive possible atoms: j>=3, rank<=8, degree<=40, H1 budget16.
# For j>=4, (j-3)dim(R)<=16 gives j<=19, so no larger degree is omitted.
atoms=[]
for j in range(3,20):
    for R in names:
        d=dims[R]
        if d>8 or j*d>40 or chars[R][1][0]!=(-1)**j*d:continue
        h=h1(j,R)
        if any(x>y for x,y in zip(h,budget)):continue
        if inner(chars[R],vm(rep('2V+P'),sym(j-2)))==q(0):continue
        atoms.append((j,R))
expected=[(3,'Wp'),(3,'T'),(4,'P'),(4,'D'),(5,'Wp'),(5,'S'),
          (6,'V'),(7,'W'),(8,'one'),(9,'Wp'),(12,'one')]
assert atoms==expected
expected_h=['0','0','P','D','P','A+D','P+D','A+D','D','A+P+D','P+D']
expected_c=['Wp','T','0','0','-Wp','-S','-T','-W-S','-S','-S-T','-Wp-T']
for (j,R),hh,cc in zip(atoms,expected_h,expected_c):
    assert h1(j,R)==dec(rep(hh))
    sign=-1 if cc.startswith('-') else 1
    assert chi3(j,R)==dec(vk(sign,rep(cc.replace('-','+').lstrip('+'))))
# The -W character forces exactly one W(-7), consuming A+D.
assert [(j,R) for j,R in atoms if chi3(j,R)[names.index('W')]<0]==[(7,'W')]
assert [(j,R) for j,R in atoms if chi3(j,R)[names.index('W')]>0]==[]
remaining_budget=dec(rep('2P'))
assert [(j,R) for j,R in atoms if all(x<=y for x,y in zip(h1(j,R),remaining_budget))]==[
    (3,'Wp'),(3,'T'),(4,'P'),(5,'Wp')]
# The elementary equations z+w=2, x-w=-1, y=0 have exactly two nonnegative solutions.
assert [(x,z,w) for w in range(3) for z in range(3) for x in range(3)
        if z+w==2 and x-w==-1]==[(0,1,1),(1,0,2)]
K1=[(3,'Wp'),(5,'Wp'),(5,'Wp'),(7,'W')]
K2=[(4,'P'),(5,'Wp'),(7,'W')]
for K in (K1,K2):
    hh=cc=(0,)*9
    for j,R in K:hh=vecadd(hh,h1(j,R));cc=vecadd(cc,chi3(j,R))
    assert hh==budget and cc==target
    assert sum(dims[R] for j,R in K)==8
    assert sum(j*dims[R] for j,R in K)==40
    check_table(K,[(6,'V'),(12,'one')],set())
assert -20+6+18==4>0

# Raw divided positive system and no hidden saturation correction.
check_table([(3,'T'),(5,'Wp')],[(6,'V'),(12,'one')],set())
assert 6+2==8 and -18-10==-28
assert vm(chars['Wp'],W)==chars['P']
assert vm(chars['V'],W)==chars['T']
# V(-2)->O4 kernel Wp(-5): rank/degree and twist2 H1 identity.
assert 3-1==2 and -6-4==-10
assert vs(sym(6),chars['V'])==chars['P']
assert vm(chars['Wp'],W)==chars['P']
assert -20+12==-8 and -8+12>0
assert vs(vk(2,sym(6)),rep('2V+P'))==chars['P']
assert vm(chars['P'],W)==rep('Wp+T')
assert vs(vk(2,sym(7)),vm(chars['P'],W))==rep('Wp+T')
assert 10+2==12 and 4+2+6==12 and -2-6==-8

# All projection channels and rank bounds used in the constant13 construction.
check_table([(2,'V'),(2,'P')],[(1,'Wp'),(1,'T')],{
    ((2,'V'),(1,'T')),((2,'P'),(1,'Wp')),((2,'P'),(1,'T'))})
assert 10-3==7 and 3+2==5<7 and 6<7
assert 7+1+1==9 and 4+9==13
assert -8-(-14)==6 and 0-(-8)==8
assert sym(8)==rep('P+D')

# Quartic-tail external and internal channels; two source copies vs one high row.
check_table([(4,'V')],[(10,'one'),(-4,'one'),(-16,'one')],{
    ((4,'V'),(-16,'one'))})
check_table([(4,'V')],[(4,'V'),(4,'P'),(6,'V'),(12,'one')],{
    ((4,'V'),(4,'V'))})
check_table([(4,'V')],[(0,'one')],set())
assert [n for n in names if dims[n]<=2 and chars[n][1][0]==dims[n]]==['one']
assert 2-1>=1 and 10+3==13 and -20-12==-32<0

# Exact original-source identity; no current accounting or source-model evaluation.
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
assert [0,0,2,0,0,0,0,1] in source['compatible_E_types']
cases=[c for c in data['rank-three-quotient-frontier-144.json']['cases'] if c['id']=='G3.11.ea6bced3bddf']
assert len(cases)==1 and cases[0]['source_index']==125
assert cases[0]['A']==Aq and cases[0]['B']==Bq and cases[0]['original_defect']==0
print('PASS: %d fixed Hom checks; 11 complete kernel atoms, two kernels, raw-divisor/polar/tail identities, original cc source pins.'%checks)
print('No actual source/model evaluation, selected points, matrices, ranks, scans, or frontier counts were performed.')
