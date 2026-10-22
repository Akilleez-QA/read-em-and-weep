#!/usr/bin/env python3
"""Exact abstract-character tests; no actual source/map/point evaluations."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
import hashlib,json
ROOT=Path(__file__).resolve().parent
FILES=['rank-three-quotient-frontier-144.json','maximal-profile-degree-envelope-refinement.json','NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md','ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md']
# Frozen input hashes are set below, not inferred at verification time.
PINNED={'rank-three-quotient-frontier-144.json': 'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad', 'maximal-profile-degree-envelope-refinement.json': '002cee319e88fb83039efca5d2816bdb93f578ba9a5a60d6fd44725edf5de94d', 'NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md': '53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08', 'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md': 'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256'}

def z(a,b=0):return(F(a),F(b))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def mul(a,b):return(a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(k,a):return(k*a[0],k*a[1])
def neg(a):return scale(-1,a)
def sub(a,b):return add(a,neg(b))
def total(xs):
 out=z(0)
 for a in xs:out=add(out,a)
 return out
phi=z(F(1,2),F(1,2));phip=z(F(1,2),-F(1,2))
W=(z(2),z(-2),phi,neg(phi),phip,neg(phip),z(1),z(-1),z(0))
sizes=(1,1,12,12,12,12,20,20,30)
ZERO=(z(0),)*9
@lru_cache(None)
def sym(n):
 assert n>=0
 a=(z(1),)*9
 if n==0:return a
 b=W
 for _ in range(2,n+1):a,b=b,tuple(sub(mul(w,v),u)for w,v,u in zip(W,b,a))
 return b

def va(a,b):return tuple(add(x,y)for x,y in zip(a,b))
def vs(a,b):return tuple(sub(x,y)for x,y in zip(a,b))
def vm(a,b):return tuple(mul(x,y)for x,y in zip(a,b))
def vk(k,a):return tuple(scale(k,x)for x in a)
chars={'one':sym(0),'W':W,'A':sym(2),'S':sym(3),'D':sym(4),'T':sym(5)}
chars['P']=tuple(map(z,(4,4,-1,-1,-1,-1,1,1,0)))
chars['V']=vs(sym(6),chars['P']);chars['Wp']=vs(vm(W,chars['P']),chars['T'])
names=('one','W','Wp','A','V','P','S','D','T')
def inner(a,b):return scale(F(1,120),total(scale(k,mul(x,y))for k,x,y in zip(sizes,a,b)))
assert all(inner(chars[a],chars[b])==z(a==b)for a in names for b in names)
def linear(terms):
 out=ZERO
 for k,n in terms:out=va(out,vk(k,chars[n]))
 return out
M3=linear(((3,'Wp'),(3,'S'),(6,'T')))
M4=linear(((2,'V'),(4,'P'),(3,'D')))
M2=linear(((1,'A'),(2,'V'),(3,'P'),(4,'D')))
@lru_cache(None)
def line_chi(e):return sym(e)if e>=0 else ZERO if e==-1 else vk(-1,sym(-e-2))
@lru_cache(None)
def bundle_chi(bs,r):
 out=ZERO
 for e,R in bs:out=va(out,vm(chars[R],line_chi(e+r)))
 return out
@lru_cache(None)
def bundle_h0(bs,r):
 out=ZERO
 for e,R in bs:
  if e+r>=0:out=va(out,vm(chars[R],sym(e+r)))
 return out

def decompose(a):
 out=[inner(a,chars[n])for n in names]
 assert all(b==0 and x.denominator==1 for x,b in out)
 return tuple(int(x)for x,b in out)
assert PINNED and all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
rows=json.loads((ROOT/FILES[0]).read_text())['cases']
prior=json.loads((ROOT/FILES[1]).read_text());keep=set(prior['remaining_ids'])
assert len(rows)==182 and len(keep)==37 and keep<=set(r['id']for r in rows)
new=[]
for row in rows:
 if row['id']not in keep:continue
 witnesses=[]
 for orient,key,d,C in [('primal','A',3,M4),('dual','B',2,M2)]:
  bs=tuple(map(tuple,row[key]))
  for r in range(d,12):
   chi_source=vs(vm(M3,line_chi(r-1)),vm(C,line_chi(r)))
   chi_kernel=vs(chi_source,bundle_chi(bs,r))
   target=ZERO
   for j in range(1,r-d+2):target=va(target,bundle_h0(bs,r-2*j))
   gap=decompose(vs(target,chi_kernel))
   negative={n:v for n,v in zip(names,gap)if v<0}
   if negative:
    witnesses.append({'orientation':orient,'twist':r,'negative_multiplicities':negative,'target_character':decompose(target),'kernel_euler_character':decompose(chi_kernel),'full_gap':gap})
    break
 if witnesses:new.append({'id':row['id'],'profile':row['profile'],'witnesses':witnesses})
cut={r['id']for r in new};remaining=sorted(keep-cut)
assert len(cut)==11 and Counter(r['profile']for r in new)=={'11':9,'21':2}
assert len(remaining)==26
counts=dict(Counter(r['profile']for r in rows if r['id']in remaining));assert counts=={'11':20,'12':4,'21':2}
historical=sorted(r['id']for r in rows if r['id']not in keep)
assert len(historical)+len(cut)+len(remaining)==182
out={'scope':'Finite iterated-section character tests exclude11 necessary labels; no exhaustive all-twist or realization claim.','source_hashes':PINNED,'input_count':37,'remaining_count':26,'remaining_by_profile':counts,'tested_twists':{'primal':[3,11],'dual':[2,11]},'character_order':names,'new_exclusions':new,'prior_excluded_ids':historical,'remaining_ids':remaining}
(ROOT/'all-profile-iterated-section-envelope.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:11 new exclusions;37->26; profiles20/4/2; all182 IDs preserved.')
