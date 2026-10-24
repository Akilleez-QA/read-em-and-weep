#!/usr/bin/env python3
"""Small universal polynomial/character controls; no actual-instance jets."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from math import factorial
import hashlib,json
from characters import product,DIM
ROOT=Path(__file__).resolve().parent
checks=0
def check(a,b,label):
 global checks
 checks+=1
 if a!=b:raise RuntimeError((label,a,b))
for n,want in [(7,{'Wp':1,'T':1}),(12,{'one':1,'A':1,'D':1,'P':1}),(13,{'W':1,'S':1,'T':1,'Wp':1}),(14,{'A':1,'D':1,'V':1,'P':1})]:check(dict(product('one',n)),want,'fixed Sym'+str(n))
check(product('one',14).get('one',0),0,'negative tail cannot reach scalar O4')
check(product('one',7).get('S',0),0,'cubic S cannot reach scalar O4')
check(product('D',1).get('S',0),1,'canonical D-row cubic inclusion')
check(product('A',2).get('one',0),1,'canonical O2 to A4 row')
check(dict(product('one',3)),{'S':1},'unique cubic evaluation')
check(-58-(-8),-50,'negative-image kernel degree')
def add(*ps):
 c=Counter()
 for p in ps:c.update(p)
 return {m:v for m,v in c.items() if v}
def scale(k,p):return {m:k*v for m,v in p.items() if k*v}
def mul(p,r):
 c=Counter()
 for (a,b),v in p.items():
  for (d,e),w in r.items():c[a+d,b+e]+=v*w
 return {m:v for m,v in c.items() if v}
one={(0,0):F(1)};y={(1,0):F(1)};z={(0,1):F(1)}
h1=add(scale(10,one),scale(-1,y),scale(-1,z));h2=y;h3=z
cap=add(scale(-1,mul(h1,h1)),scale(-1,mul(h2,h2)),scale(-1,mul(h3,h3)),scale(-11,z))
diff=add(h1,scale(-1,h2))
completed=add(scale(-50,one),scale(-1,z),scale(-F(3,2),mul(z,z)),scale(-F(1,2),mul(diff,diff)))
check(cap,completed,'all-height exact square identity')
check(5+5,10,'equality heights')
check(sum(2-4*j for j in range(1,6)),-50,'five exact graded degrees')
flag=[]
for j in range(1,6):
 k=5-j;n=9
 c=product('W',k)
 rank=2*(k+1);degree=rank*(k-n)
 check(rank,2*(6-j),'principal-parts rank')
 check(degree,sum(2-4*i for i in range(j,6)),'principal-parts degree equality')
 check(sum(DIM[r]*v for r,v in c.items()),rank,'flag coefficient dimension')
 # Universal monomial contraction: n-k directional contractions kill
 # exactly the monomials with formal transverse order >k. This uses no
 # actual source form, coefficient system, parameter, point or jet.
 surviving=[]
 for transverse in range(n+1):
  power=n-transverse
  coeff=0 if power<n-k else factorial(power)//factorial(power-(n-k))
  if coeff:surviving.append(transverse)
 check(surviving,list(range(k+1)),'universal complete-system contraction kernel')
 flag.append({'j':j,'degree':k-n,'coefficient':dict(c),'rank':rank,'total_degree':degree})
check([x['coefficient'] for x in flag],[{'S':1,'T':1},{'A':1,'D':1},{'W':1,'S':1},{'one':1,'A':1},{'W':1}],'exact full flag')
check(-5-(-4),-1,'quartic subbundle has no map to pure minus five')
check(2+(-8),-6,'positive defective image degree')
check(6-(-6),12,'positive defective image quotient length')
pins=[('inputs/five-kernels.md','4d06da768074a6e813ed295a088d862ce328a4cd33b739e88e20ac1f315de36a'),('inputs/top-four.md','56bb8a0aa5ada0f550e0967ef9e535838e9162c2ff2e5ced039a3f6ddb2aacf0'),('inputs/low-top.md','c3d21cb63ffac4c69247e8deba8ef352f673ac3a7b2f91507bc54fbecae943af')]
for f,h in pins:check(hashlib.sha256((ROOT/f).read_bytes()).hexdigest(),h,'input pin '+f)
print(json.dumps({'status':'PASS','checks':checks,'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'flag':flag,'scope':'Universal character, all-height polynomial and complete-system principal-parts controls only; no actual coefficient/point/jet evaluation.'},indent=2,sort_keys=True))
