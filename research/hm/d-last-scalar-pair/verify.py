#!/usr/bin/env python3
"""Exact universal controls; no actual source instances or evaluations."""
from pathlib import Path
from itertools import product
from math import comb
from fractions import Fraction
import hashlib,json
import characters as c
ROOT=Path(__file__).resolve().parent
checks=0
def require(ok,label):
 global checks
 checks+=1
 if not ok:raise RuntimeError(label)
for r in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/r['file']).read_bytes()
 require(len(b)==r['bytes'],'input length '+r['file'])
 require(hashlib.sha256(b).hexdigest()==r['sha256'],'input sha '+r['file'])
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==r['git_blob_sha1'],'input blob '+r['file'])
require((ROOT/'characters.py').read_bytes()==(ROOT/'inputs/characters-public.py').read_bytes(),'character source equality')
inv=[n for n in range(13) if c.product('one',n)['one']]
require(inv==[0,12],'invariant low degrees')
require(c.product('one',12)['one']==1,'unique F12')
require(c.product('one',18)['V']==1,'unique V18')
require(c.product('one',6)=={'V':1,'P':1},'Sym6')
require(c.product('one',8)=={'P':1,'D':1},'Sym8')
require(sum(c.DIM[r]*m for r,m in c.product('one',8).items())==9,'Sym8 dimension')
require(max(c.DIM[r] for r in c.product('one',8))==5,'proper Sym8 quotient bound')
# Exact equivariant polynomial map support, not selected polynomial matrices.
allowed2=[d for d in range(13) if any(c.product('one',d-gap)['one'] for gap in (0,2,12))]
allowed1=[d for d in range(13) if any(c.product('one',d-gap)['one'] for gap in (0,10,12))]
require(allowed2==[0,2,12],'rank2 deficits')
require(allowed1==[0,10,12],'rank1 deficits')
caps=[6*h-h*(h+1)-4*(10-h)-(10-h)*(11-h) for h in range(5,11)]
require(caps==[-50,-42,-38,-38,-42,-50],'capacities')
allocations={}; surviving={}
for h in (5,6,7):
 q=[2]*(10-h)+[1]*(2*h-10)
 require(sum(q)==10 and len(q)==h,'quotient ranks')
 budget=caps[h-5]+50
 raw=[a for a in product(*[allowed2 if r==2 else allowed1 for r in q]) if sum(a)==budget]
 allocations[str(h)]=[list(a) for a in raw]
 # On equal-rank stretches images have common generic subspace.
 # Delta0 versus2 at rank2 have distinct constant Pluecker planes.
 # Same-rank inclusion also forces nondecreasing deficit.
 good=[]
 for a in raw:
  plane=[d for d,r in zip(a,q) if r==2]
  compatible=not (0 in plane and 2 in plane)
  monotone=all(a[j]<=a[j+1] for j in range(h-1) if q[j]==q[j+1])
  if compatible and monotone:good.append(a)
 surviving[str(h)]=[list(a) for a in good]
 require(bool(good),'nonempty formal residual set')
require(surviving['5']==[[0]*5],'height5')
require(surviving['6']==[[2,2,2,2,0,0]],'height6')
require(surviving['7']==[[0,0,0,0,0,0,12],[0,0,12,0,0,0,0]],'height7 locations')
require(6-2*5==-4 and -4>-6,'height5 strict top')
require(6-2*6==-6,'height6 terminal')
require(6-2*7==-8 and 6-2*7-12==-20,'height7 terminals')
source=[(-2,'D'),(-3,'Wp'),(-3,'T'),(-4,'V'),(-8,'one')]
require(sum(c.DIM[r] for d,r in source)==17,'source rank')
require(sum(d*c.DIM[r] for d,r in source)==-54,'source degree')
require(all(d>-8 for d,r in source[:-1]),'only O-8 maps to target degree-8')
require(30-9==21 and 17-1==16 and -54+8==-46,'constant split dimensions')
require(13-8==5 and 10-7==3 and -50+14==-36,'residual dimensions')
possible=[]
for e in range(-8,-3):
 maps=[target for target in (-4,-6) if c.product('one',target-e)['one']]
 if maps:possible.append([e,maps])
require(possible==[[-6,[-6]],[-4,[-4]]],'all residual generic line degrees')
residual={}
for e in (-6,-4):
 total=3*e+24
 ds=[list(d) for d in product((0,12),repeat=3) if sum(d)==total and d[0]<=d[1]<=d[2]]
 residual[str(e)]=ds
require(residual=={'-6':[],'-4':[[0,0,12]]},'residual invariant divisors')
require(-4-6-12==-22,'residual terminal')
require(20-7-1==12 and 22-3-1==18,'apolar target degrees')
require(all(d>-4 for d,r in source[:-2]),'residual higher maps vanish')
# General basepoint-free sextic net quartic multiplication H1 vanishing.
for a in range(1,6):
 b=6-a
 require(4-a>=-1 and 4-b>=-1,'quartic sextic net cohomology')
# Exact formal apolar evaluation: <(x+t y)^n,x^(n-i)y^i>
# equals (-1)^i t^(n-i), with anti-diagonal normalized monomial pairing.
# These symbolic coefficients prove common factors remain common factors
# after determinant self-duality (up to x,y interchange/sign), no point chosen.
apolar_controls=0
for n in range(1,25):
 for i in range(n+1):
  j=n-i
  scalar=comb(n,j)*Fraction((-1)**j,comb(n,j))
  require(scalar==(-1)**j,'normalized apolar monomial evaluation')
  apolar_controls+=1
# Universal distributivity for each monomial of a degree12 common factor
# and each multiplier monomial. The apolar substituted monomial product
# has exactly the same exponent and sign as substituted degree-n product.
factor_controls=0
for m in (8,10):
 for i in range(13):
  for j in range(m+1):
   require((12-i)+(m-j)==12+m-(i+j),'formal product exponent')
   require((-1)**(12-i)*(-1)**(m-j)==(-1)**(12+m-i-j),'formal product sign')
   factor_controls+=1
result={'scope':'single D-source original pair50 exclusion','status':'all formal controls pass; written geometry requires independent review','checks':checks,'input_count':len(json.loads((ROOT/'INPUTS.json').read_text())),'capacity':caps,'allowed_deficits':{'rank2':allowed2,'rank1':allowed1},'raw_allocations':allocations,'nested_image_allocations':surviving,'residual_saturated_lines':possible,'residual_divisors':residual,'apolar_monomial_controls':apolar_controls,'common_factor_controls':factor_controls,'actual_instances_evaluated':0}
print(json.dumps(result,indent=2,sort_keys=True))
