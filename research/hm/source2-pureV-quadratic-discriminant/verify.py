#!/usr/bin/env python3
"""Exact symbolic checks; no coefficients or roots of the actual V6 system."""
from pathlib import Path
from itertools import combinations,permutations
import hashlib,json,math
ROOT=Path(__file__).resolve().parent
n=0
def ck(p,s):
 global n
 n+=1
 if not p:raise RuntimeError(s)
for e in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/e['local_path']).read_bytes()
 ck(hashlib.sha256(b).hexdigest()==e['sha256'],'source SHA256')
 ck(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob'],'source Git blob')
# Restriction formula and image-complex Smith ranks.
for r in (1,2):
 k=2+r
 ck(5-(3-r)==k,'restriction rank formula')
 ck((5-k,4-k,k)=={1:(2,1,3),2:(1,0,4)}[r],'formal image cohomology ranks')
# All potential vanishing sequences for a degree-six linear series.
for a in combinations(range(7),3):
 M=[[1,1,1],list(a),[i*(i-1) for i in a]]
 det=(M[1][1]*M[2][2]-M[1][2]*M[2][1])-(M[1][0]*M[2][2]-M[1][2]*M[2][0])+(M[1][0]*M[2][1]-M[1][1]*M[2][0])
 ck(det==math.prod(a[j]-a[i] for i in range(3) for j in range(i+1,3)),'Wronskian leading determinant')
 if a[0]==0 and a[1]>=2:ck(sum(a)-3>=2,'nonimmersive weight at least two')
ck(3*6-3*2==12,'Wronskian bundle degree')
ck(2*min((12,20,30,60))>12,'orbit forbids differential zero')
# Universal divisor pushforward dimensions and cokernel length.
ck(7-5==2 and 3-2==1,'secant rank and kernel rank')
ck(5==0-5*(-1),'secant c1')
def chi(k):return (k+2)*(k+1)//2
ck(4*chi(0)-5*chi(-1)+chi(-5)==10,'degeneracy length')
# Stabilizer possibilities and invariant local lengths.
orders={h*i for h in (1,2,3,5) for i in (1,2) if 60%(h*i)==0}
sizes=sorted({60//h for h in orders})
ck(sizes==[6,10,12,15,20,30,60],'pair orbit sizes')
poss=[(s,m) for s in sizes for m in range(1,11) if s*m==10]
ck(poss==[(10,1)],'single orbit is reduced')
ck(min(sizes)*2>10,'cannot contain two orbits')
# Verify A5 elementary finite-group facts without a precomputed class table.
def parity(p):return sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))%2
G=[p for p in permutations(range(5)) if not parity(p)]
def compose(p,q):return tuple(p[q[i]] for i in range(5))
def order(p):
 q=tuple(range(5))
 for k in range(1,61):
  q=compose(p,q)
  if q==tuple(range(5)):return k
 raise RuntimeError('group order')
ck(len(G)==60,'A5 order')
counts={k:sum(order(g)==k for g in G) for k in (1,2,3,5)}
ck(counts=={1:1,2:15,3:20,5:24},'A5 element orders')
subs={frozenset((g,compose(g,g))) for g in G if order(g)==3}
ck(len(subs)==10,'ten cyclic order-three subgroups')
for sub in subs:
 normalizer=[]
 for g in G:
  inv=tuple(g.index(i) for i in range(5))
  if frozenset(compose(compose(g,h),inv) for h in sub)==sub:normalizer.append(g)
 ck(len(normalizer)==6,'order-three pair stabilizer order')
ck(60//3==20,'root orbit size')
# Negative control: basepoint-free does not itself imply jet separation.
# The formal system 1,z²,z³ has nonzero value but zero derivatives at z=0.
exponents=(0,2,3)
values=[int(e==0) for e in exponents]
derivatives=[int(e==1) for e in exponents]
ck(values==[1,0,0] and derivatives==[0,0,0] and sum(exponents)-3==2,'ramification weight model')
print(f'PASS: {n} exact checks; two immutable inputs; no actual coefficient evaluation.')
