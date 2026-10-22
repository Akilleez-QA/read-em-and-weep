#!/usr/bin/env python3
"""Exact finite certificate for all iterated-section twists on26 surviving labels."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json
from functools import lru_cache
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
@lru_cache(None)
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
PINNED={'rank-three-quotient-frontier-144.json': 'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad', 'all-profile-iterated-section-envelope.json': '280654f6fa7c82483bee82cf31865e8a561facab82a8456d8666616778762cef'}

assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
rows=json.loads((ROOT/'rank-three-quotient-frontier-144.json').read_text())['cases']
prior=json.loads((ROOT/'all-profile-iterated-section-envelope.json').read_text());ids=set(prior['remaining_ids']);assert len(ids)==26
zero=(0,)*9
vadd=lambda *xs:tuple(map(sum,zip(*xs)))if xs else zero
vneg=lambda x:tuple(-v for v in x)
@lru_cache(None)
def block(n,e):
 if e==-1:return zero
 x=decompose(mul(chars[n],symchar(e if e>=0 else -e-2)))
 return x if e>=0 else vneg(x)
def chi(b,t):return vadd(*(block(n,e+t)for e,n in b))
def h0(b,t):return vadd(*(block(n,e+t)for e,n in b if e+t>=0))
M3b=tuple((-1,n)for c,n in [(3,'Wp'),(3,'S'),(6,'T')]for _ in range(c))
M4b=tuple((0,n)for c,n in [(2,'V'),(4,'P'),(3,'D')]for _ in range(c))
M2b=tuple((0,n)for c,n in [(1,'A'),(2,'V'),(3,'P'),(4,'D')]for _ in range(c))
dims=dict(zip(names,[1,2,2,3,3,4,4,5,6]));parity={n:int(chars[n][1][0]<0)for n in names}
# Reg_parity has dimension60 and multiplicity dim(rho) in its parity block.
reg={p:tuple(dims[n]if parity[n]==p else 0 for n in names)for p in [0,1]}
assert all(sum(v*dims[n]for v,n in zip(reg[p],names))==60 for p in [0,1])
# Check the exact root-of-unity identities on a full period.
for t in range(60):
 assert decompose(sub(symchar(t+60),symchar(t)))==reg[t%2]
 sum30=[total(symchar(t+2*k)[i]for k in range(30))for i in range(9)]
 assert decompose(sum30)==tuple(F(t+30,2)*v for v in reg[t%2])
records=[];failures=[]
for row in rows:
 if row['id']not in ids:continue
 for side,d,n,source in [('A',3,14,M4b),('B',2,10,M2b)]:
  J=tuple(tuple(x)for x in row[side]);deg=sum(e*dims[c]for e,c in J)
  assert sum(dims[c]for e,c in J)==3 and all(e%2==parity[c]for e,c in J)
  R=max(d,max(e for e,c in J)+2*d-2,-min(e for e,c in J),-(-(2*n-deg-90)//3))
  @lru_cache(None)
  def difference(t):
   target=vadd(*(h0(J,t-2*j)for j in range(1,t-d+2)))
   chiF=vadd(chi(M3b,t),vneg(chi(source,t)),vneg(chi(J,t)))
   return vadd(target,vneg(chiF))
  bad=[dict(twist=t,negative={c:v for c,v in zip(names,difference(t))if v<0})for t in range(d,R+60)if min(difference(t))<0]
  # Verify the derived recurrence at every residue-class anchor.
  for t in range(R,R+60):
   coefficient=F(3*t+deg+90-2*n,2)
   increment=tuple(coefficient*v for v in reg[t%2])
   assert coefficient>=0 and all(x.denominator==1 for x in increment)
   assert vadd(difference(t+60),vneg(difference(t)))==increment
  records.append(dict(id=row['id'],side=side,d=d,rank=n,degree_J=deg,eventual_threshold=R,last_checked_twist=R+59,failures=bad))
  failures.extend((row['id'],side,x)for x in bad)
assert not failures
out=dict(scope='No further exclusions: all26 labels satisfy this entire iterated-section-envelope family, not all necessary conditions.',source_hashes=PINNED,character_order=names,period=60,increment='((3r+degJ+90-2rankF)/2)*Reg_parity(r)',label_count=26,orientation_count=len(records),max_last_checked_twist=max(x['last_checked_twist']for x in records),records=records,remaining_ids=sorted(ids))
(ROOT/'iterated-section-envelope-all-twists.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: all26 labels satisfy every iterated-section twist; finite anchors plus genuine60-step increments. Max anchor:',out['max_last_checked_twist'])
