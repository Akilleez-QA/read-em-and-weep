#!/usr/bin/env python3
"""Two second-defect-24 branches excluded by stabilizer fiber characters only."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json
ROOT=Path(__file__).resolve().parent

# Exact Q(sqrt(5)) character arithmetic, independently reproduced here.
def plus(a,b):return(a[0]+b[0],a[1]+b[1])
def times(a,b):return(a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(c,a):return(c*a[0],c*a[1])
def minus(a,b):return plus(a,scale(-1,b))
def total(xs):
 out=(F(0),F(0))
 for x in xs:out=plus(out,x)
 return out
z=lambda a,b=0:(F(a),F(b))
phi=z(F(1,2),F(1,2));phip=z(F(1,2),-F(1,2))
W=[z(2),z(-2),phi,scale(-1,phi),phip,scale(-1,phip),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
def symchar(n):
 a=[z(1)]*9
 if n==0:return a
 b=W
 for _ in range(2,n+1):a,b=b,[minus(times(w,v),u)for w,v,u in zip(W,b,a)]
 return b
chars={'one':[z(1)]*9,'W':W,'A':symchar(2),'S':symchar(3),'D':symchar(4),'T':symchar(5)}
chars['P']=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
chars['V']=[minus(a,b)for a,b in zip(symchar(6),chars['P'])]
chars['Wp']=[minus(times(w,p),t)for w,p,t in zip(W,chars['P'],chars['T'])]
names=('one','W','Wp','A','V','P','S','D','T')
def inner(a,b):return scale(F(1,120),total(scale(s,times(x,y))for s,x,y in zip(sizes,a,b)))
assert all(inner(chars[a],chars[b])==z(a==b)for a in names for b in names)
# Characters are real, hence the nine irreducibles are self-dual.
# W has trivial determinant: Lambda^2 W = 1 (the standard SL2 lift).
# The recurrence uses exactly that determinant-one linearization.
def mul(a,b):return [times(x,y)for x,y in zip(a,b)]
def sub(a,b):return [minus(x,y)for x,y in zip(a,b)]
def linear(terms):return [total(scale(c,chars[n][i])for c,n in terms)for i in range(9)]
def decompose(a):
 out=[inner(a,chars[n])for n in names]
 assert all(b==0 and x.denominator==1 for x,b in out)
 return tuple(int(x)for x,b in out)
M3=linear([(3,'Wp'),(3,'S'),(6,'T')])
M4=linear([(2,'V'),(4,'P'),(3,'D')])
PINNED={'rank-three-quotient-frontier-144.json': 'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad', 'two-one-rank-eleven-endpoint-splittings.json': '4704e794183cb1a2b0bf5069e3baedafeedc9ae186c40dea2917766100d23a16'}

assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
front=json.loads((ROOT/'rank-three-quotient-frontier-144.json').read_text())
pairs=json.loads((ROOT/'two-one-rank-eleven-endpoint-splittings.json').read_text())['pairs']
# Choose the C10 generator with W eigenvalues zeta,zeta^-1, zeta primitive10.
# Every irreducible determinant is trivial because the binary icosahedral group is perfect.
# At this generator Wprime has trace zeta^3+zeta^-3, hence weights3 and7.
assert chars['Wp'][2]==minus(times(times(phi,phi),phi),scale(3,phi))
assert chars['Wp'][2]==phip
weights={'one':(0,), 'Wp':(3,7)}
results=[]
for i,ID in [(2,'G3.21.d610e381ed75'),(10,'G3.21.d41783aef00b')]:
 row=next(c for c in front['cases']if c['id']==ID);p=pairs[i]
 assert row['profile']=='21' and row['source_index']==i and row['A']==p['A']
 assert row['status']=='not_excluded' and p['a']==10
 source_weights=sorted((e-2+w)%10 for e,n in p['A']for w in weights[n])
 assert source_weights==[0,0,4]
 opts=[a for a in p['alternatives']if a['s']==24]
 assert [a['torsion']for a in opts]==[[[24,6]],[[12,4],[12,6]]]
 tops=[]
 for alt in opts:
  # Each direct cyclic summand contributes its generator k, not its socle.
  top=sorted(k%10 for d,k in alt['torsion']);tops.append(top)
  assert 6 in top and 6 not in source_weights
 # Cyclic O(6)|2D12 has socle6-12=4, but generator weight6.
 assert (6-12)%10==4
 results.append(dict(id=ID,source_pair_index=i,excluded_second_defect=24,remaining_second_defects=[s for s in p['retained_second_defects']if s!=24],source_fiber_weights=source_weights,torsion_top_weights=tops))
out=dict(scope='Two positive-defect branches excluded by a stabilizer-fiber quotient obstruction; neither quotient pair excluded.',source_hashes=PINNED,stabilizer_order=10,O_one_fiber_weight=1,Wprime_weights=[3,7],cyclic_generator_weight=6,cyclic_socle_weight=4,cases=results)
(ROOT/'two-one-second-defect-twenty-four-image-exclusion.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: both A(-2) fibers have weights0,0,4; each allowed T24 top requires weight6.')
print('Two s=24 branches excluded; no quotient-case exclusion; no splitting enumeration.')
