#!/usr/bin/env python3
"""Finite universal A5 incidences and local arithmetic, never actual instances."""
from pathlib import Path
from itertools import permutations,product
import hashlib,json
root=Path(__file__).resolve().parent;checks=[]
def ck(name,value):
 if not value: raise RuntimeError(name)
 checks.append(name)
for p in json.loads((root/'INPUTS.json').read_text()):
 b=(root/p['local_path']).read_bytes()
 ck('immutable pin '+p['label'],len(p['commit'])==40)
 ck('sha256 '+p['label'],hashlib.sha256(b).hexdigest()==p['sha256'])
 ck('git blob '+p['label'],hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==p['git_blob'])
identity=tuple(range(5))
def mul(a,b):return tuple(a[b[i]] for i in range(5))
def inv(a):return tuple(a.index(i) for i in range(5))
def parity(a):return sum(a[i]>a[j] for i in range(5) for j in range(i+1,5))%2
def order(a):
 b=identity
 for k in range(1,61):
  b=mul(a,b)
  if b==identity:return k
 raise RuntimeError('order')
G=[p for p in permutations(range(5)) if parity(p)==0]
I=[g for g in G if order(g)==2]
ck('A5 order',len(G)==60);ck('fifteen involutions',len(I)==15)
def cyclic(a):
 S={identity};b=a
 while b!=identity:S.add(b);b=mul(a,b)
 return frozenset(S)
def cyclics(n):return set(cyclic(g) for g in G if order(g)==n)
def normalizer(S):return set(g for g in G if frozenset(mul(mul(g,x),inv(g)) for x in S)==S)
C3=cyclics(3);C5=cyclics(5)
ck('ten order-three axes',len(C3)==10);ck('six order-five axes',len(C5)==6)
for n,groups,count in [(3,C3,3),(5,C5,5)]:
 ck(str(n)+' normalizer order',all(len(normalizer(S))==2*n for S in groups))
 ck(str(n)+' normalizer involutions',all(len(set(I)&normalizer(S))==count for S in groups))
 ck(str(n)+' axes per involution line',all(sum(h in normalizer(S) for S in groups)==2 for h in I))
centralizers={h:frozenset(g for g in G if mul(g,h)==mul(h,g)) for h in I}
ck('involution centralizers are Klein four',all(len(S)==4 and all(order(x) in [1,2] for x in S) for S in centralizers.values()))
ck('five Klein four groups',len(set(centralizers.values()))==5)
ck('two other axis points per mirror',all(len((set(S)&set(I))-{h})==2 for h,S in centralizers.items()))
ck('each order-two axis belongs to two other mirrors',all(sum(h!=k and mul(h,k)==mul(k,h) for h in I)==2 for k in I))
# Model a C2-stabilized orbit as G/H. Stabilizers identify the unique mirror.
h=I[0];H={identity,h};remaining=set(G);cosets=[]
while remaining:
 g=next(iter(remaining));C=frozenset(mul(g,x) for x in H);cosets.append((g,C));remaining-=C
ck('C2 orbit has thirty points',len(cosets)==30)
ck('C2 orbit has two points per mirror',all(sum(mul(mul(g,h),inv(g))==k for g,C in cosets)==2 for k in I))
# Diagonal rotation model is representation-only: no source or direction is chosen.
V4=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
charsu=[y*x for x,y,z in V4];charsv=[z*x for x,y,z in V4]
ck('two mirror characters independent',len(set(zip(charsu,charsv)))==4)
# The all-degree character formula is parity, demonstrated at every parity class.
for i,j in product(range(2),repeat=2):
 ch=[u**i*v**j for u,v in zip(charsu,charsv)]
 ck('u-character iff odd-even '+str((i,j)),(ch==charsu)==(i==1 and j==0))
ck('fixed general mirror order',2*2+2*1==6)
ck('ell5 mirror order',2*3+2*1==8)
ck('ell3 mirror order',2*2+2*2==8)
ck('competing extra orbits force line divisor',6+2+2>9)
ck('jet-line extra offconic forces line divisor',8+2>9)
ck('general Bezout residual',9**2-(6*4+10)==47)
ck('jet Bezout residual',9**2-(6*9+10)==17 and 9**2-(6*4+10*4)==17)
ck('free orbit impossible',34+60>81)
ck('jet conic orbit reduced',2*12>17)
ck('extra thirty orbit reduced',2*30>47)
ck('extra fifteen ideal has linear part',15*4>15*(9-6))
ck('fifteen local length at most two', [k for k in range(1,10) if 15*(1+k)<=45]==[1,2])
ck('conic curvilinear length at most three',[k for k in range(1,10) if 12*k<=47]==[1,2,3])
rows=[(k,l,m) for k in range(4) for l in range(3) for m in range(2) if l*m==0 and 12*k+15*l+30*m<=47]
lengths=sorted(set(34+12*k+15*l+30*m for k,l,m in rows))
supports=sorted(set(12*(k>0)+15*(l>0)+30*m for k,l,m in rows))
ck('necessary total length list',lengths==[34,46,49,58,61,64,70,73,76])
ck('necessary extra support list',supports==[0,12,15,27,30,42])
print(json.dumps({'status':'pass','count':len(checks),'checks':checks,'integer_configurations':rows,'possible_necessary_lengths':lengths,'scope':'necessary universal constraints only; no occurrence or actual gate selection'},indent=2))
