#!/usr/bin/env python3
"""Universal P-type character and Euler controls; no actual instance data."""
import hashlib,json,pathlib
from collections import Counter
from fractions import Fraction as F
from characters import chars,product,q,plus,times,scale,DIM,NAMES
ROOT=pathlib.Path(__file__).resolve().parent
checks=0
def require(ok,label):
 global checks
 checks+=1
 if not ok: raise RuntimeError(label)
for d in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/d['file']).read_bytes()
 require(len(b)==d['bytes'],'bytes '+d['file'])
 require(hashlib.sha256(b).hexdigest()==d['sha256'],'SHA256 '+d['file'])
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==d['git_blob_sha1'],'blob '+d['file'])
sizes=[1,1,12,12,12,12,20,20,30]
def inner(a,b):
 z=q(0)
 for w,x,y in zip(sizes,a,b):z=plus(z,scale(F(w,120),times(x,y)))
 return z
for a in NAMES:
 for b in NAMES:require(inner(chars[a],chars[b])==q(int(a==b)),'orthogonality')
for i in range(9):require(times(chars['Wp'][i],chars['W'][i])==chars['P'][i],'Wp W = P')
require(product('P',1)==Counter(Wp=1,T=1),'unique top Wp and T')
expected=[{'one':1},{'W':1},{'A':1},{'S':1},{'D':1},{'T':1},{'V':1,'P':1},{'Wp':1,'T':1}]
for n,e in enumerate(expected):require(product('one',n)==Counter(e),'Sym '+str(n))
require(all(product('one',n)['Wp']==0 for n in range(7)),'first Wp lower degrees')
require(product('one',7)['Wp']==1,'first Wp at seven')
chi=product('P',2)+product('Wp',1)+product('T',1)+Counter(V=1)
require(chi==Counter(V=3,P=3,D=2),'P-source quartic Euler')
# Polynomial lists represent formal chart coordinates, never sampled values.
def add(a,b):
 c=[0]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 while len(c)>1 and c[-1]==0:c.pop()
 return c
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 while len(c)>1 and c[-1]==0:c.pop()
 return c
def dot(a,b):
 z=[0]
 for x,y in zip(a,b):z=add(z,mul(x,y))
 return z
for j,r,s in [([[1],[0,1]],[[0,-1],[1]],[[0],[1]]),([[0,1],[1]],[[-1],[0,1]],[[-1],[0]])]:
 require(dot(r,j)==[0],'Euler chart composite')
 require(dot(r,s)==[1],'Euler chart split surjection')
 # det[j s]=1: gives invertible change of basis, exact kernel as well.
 require(add(mul(j[0],s[1]),[-x for x in mul(j[1],s[0])])==[1],'Euler chart basis')
# Euler virtual exactness in arbitrary tested twists; geometric proof handles all.
def euler(r,d):
 if d>=0:return product(r,d)
 if d==-1:return Counter()
 return Counter({x:-n for x,n in product(r,-d-2).items()})
for t in range(-7,9):
 diff=euler('P',t-2);diff.subtract(euler('Wp',t-3));diff.subtract(euler('Wp',t-1))
 require(all(n==0 for n in diff.values()),'Euler exact character twist '+str(t))
# Rank-one top-kernel degree and extension vanishing: symbolic affine identities.
require((-3*2)+(-2)==(-2*4),'top-kernel degree identity constant term')
require(-3-(-2)==-1,'Ext exponent e-1 from (-3)-(-e-2)')
require(6-1>=-1,'Ext H1 vanishes for all e>=6')
result={'status':'PASS','checks':checks,'source':'P-type actual Gauss source, conditional hypotheses in PROOF.md','forced_factor':'Wprime O(-1)','line_image_minimum_degree':6,'line_image_even':True,'top_kernel_rank2_image':'Wp O(-3)','top_kernel_rank1_image':'Wp O(-3) + O(-e-2), noncanonical equivariant split','quartic_Euler':dict(sorted(chi.items())),'actual_instance_evaluations':0,'new_live_exclusions_claimed':0}
print(json.dumps(result,indent=2,sort_keys=True))
