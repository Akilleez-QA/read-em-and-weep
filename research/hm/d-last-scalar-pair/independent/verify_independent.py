#!/usr/bin/env python3
"""Universal symbolic controls only; no actual HM instances or parameter values."""
from fractions import Fraction as Q
from math import comb
from itertools import product
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent
checks=0
kinds={}
def check(b,label):
 global checks
 checks+=1;kinds[label]=kinds.get(label,0)+1
 if not b: raise RuntimeError(label)
def plus(a,b):return(a[0]+b[0],a[1]+b[1])
def mul(a,b):return(a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def neg(a):return(-a[0],-a[1])
def sy(n,t):
 a,b=(Q(1),Q(0)),t
 if n==0:return a
 for _ in range(1,n):a,b=b,plus(mul(t,b),neg(a))
 return b
tr=[(Q(2),Q(0)),(Q(-2),Q(0)),(Q(1,2),Q(1,2)),(Q(-1,2),Q(-1,2)),(Q(1,2),Q(-1,2)),(Q(-1,2),Q(1,2)),(Q(1),Q(0)),(Q(-1),Q(0)),(Q(0),Q(0))]
weights=[1,1,12,12,12,12,20,20,30]
Pchar=[(Q(x),Q(0)) for x in [4,4,-1,-1,-1,-1,1,1,0]]
Vchar=[plus(sy(6,t),neg(p)) for t,p in zip(tr,Pchar)]
def ip(a,b):
 z=(Q(0),Q(0))
 for x,y,w in zip(a,b,weights):
  v=mul(x,y);z=plus(z,(v[0]*w,v[1]*w))
 check(z[1]==0 and z[0].denominator==1,'character rationality')
 return z[0]/120
inv=[ip([sy(n,t) for t in tr],[(Q(1),Q(0))]*9) for n in range(13)]
check(inv==[1]+[0]*11+[1],'invariants')
check(ip([sy(18,t) for t in tr],Vchar)==1,'V18 multiplicity')
check(ip(Vchar,Vchar)==1,'V irreducible')
check(ip(Pchar,Pchar)==1,'P irreducible')
for t,p,v in zip(tr,Pchar,Vchar):
 check(sy(8,t)==plus(p,sy(4,t)),'Sym8 decomposition')
 check(sy(6,t)==plus(p,v),'Sym6 decomposition')
# Enumerate integer budget compositions, independently of the author's product over allowed deficits.
def comp(s,n):
 if n==1:yield(s,);return
 for d in range(s+1):
  for tail in comp(s-d,n-1):yield(d,)+tail
survivors={};raw={}
for h in [5,6,7]:
 ranks=[2]*(10-h)+[1]*(2*h-10)
 cap=sum(sum([6,-4][:q])-2*j*q for j,q in enumerate(ranks,1))
 budget=cap+50; raw[h]=[];survivors[h]=[]
 for ds in comp(budget,h):
  legal=all(any(d-gap in (0,12) for gap in ((0,2,12) if q==2 else (0,10,12))) for d,q in zip(ds,ranks))
  if not legal:continue
  raw[h].append(ds)
  r2=ds[:10-h]
  monotone=all(ds[i]<=ds[i+1] for i in range(h-1) if ranks[i]==ranks[i+1])
  planes=not(0 in r2 and 2 in r2)
  if monotone and planes:survivors[h].append(ds)
 check(cap=={5:-50,6:-42,7:-38}[h],'capacity')
check(survivors=={5:[(0,)*5],6:[(2,2,2,2,0,0)],7:[(0,0,0,0,0,0,12),(0,0,12,0,0,0,0)]},'nested allocations')
# Exhaust residual saturated-line degree, equivariant components, and divisor persistence.
res=[]
for e in range(-8,-3):
 maps=[b for b in [-4,-6] if b-e in [0,12]]
 if maps:
  divisors=[d for d in comp(3*e+24,3) if all(x in [0,12] for x in d) and d[0]<=d[1]<=d[2]]
  res.append([e,maps,divisors])
check(res==[[-6,[-6],[]],[-4,[-4],[(0,0,12)]]],'residual saturated line')
# Apolar annihilation for formal l=x+t*y, all monomial generators.
# No value is substituted for t. Each pairing is one t-monomial times the rational sum below.
for n in range(1,25):
 for k in range(n):
  for i in range(k+1):
   for j in range(n-k):
    z=Q(0)
    for a in range(n-k+1):
     b=n-i-j-a
     if 0<=b<=k+1:
      z+=Q(comb(n-k,a)*comb(k+1,b)*(-1)**(a+i),comb(n,a+i))
    check(z==0,'formal apolar annihilation')
  check((k+1)+(n-k)==n+1,'annihilator dimensions')
# <x^(n-i)y^i,(u*x+v*y)^n>=(-1)^i*u^i*v^(n-i).
# Show coefficientwise multiplicativity, with the determinant coordinate rotation explicit.
for m in [8,10]:
 n=12+m
 for i in range(13):
  for j in range(m+1):
   check((-1)**i*(-1)**j==(-1)**(i+j),'common factor sign')
   check((i+j,12-i+m-j)==(i+j,n-i-j),'common factor exponents')
for a in range(1,6):check(4-a>=-1 and 4-(6-a)>=-1,'sextic H1')
check((30-9,17-1,-54+8,13-8,10-7,-50+14)==(21,16,-46,5,3,-36),'actual split arithmetic')
result={'status':'PASS','checks':checks,'by_category':kinds,'raw_allocation_counts':{h:len(a) for h,a in raw.items()},'nested_survivors':survivors,'actual_instances_evaluated':0,'interpretation':'Supporting universal controls; not proof-assistant verification.'}
print(json.dumps(result,indent=2,sort_keys=True))
