"""Frozen-list source-conditioned V/Z closure. No candidate regeneration."""
import hashlib,json
from pathlib import Path
from collections import Counter
import characters as c
ROOT=Path(__file__).resolve().parent
checks=0
def require(ok,message):
 global checks
 checks+=1
 if not ok: raise RuntimeError(message)
def h1(blocks,t):
 out=Counter()
 for e,r in blocks:out.update(c.product(r,-e-t-2))
 return out
def chi(blocks,t):
 out=c.h0(blocks,t);out.subtract(h1(blocks,t));return out
def signed(x):return {r:x[r] for r in c.NAMES if x[r]}
def negative(x):return {r:x[r] for r in c.NAMES if x[r]<0}
def degree(blocks):return sum(e*c.DIM[r] for e,r in blocks)
def ordinary(blocks):return sorted([e for e,r in blocks for _ in range(c.DIM[r])],reverse=True)
for item in json.loads((ROOT/'INPUTS.json').read_text()):
 data=(ROOT/item['file']).read_bytes()
 require(len(data)==item['bytes'],'input byte length '+item['file'])
 require(hashlib.sha256(data).hexdigest()==item['sha256'],'input sha256 '+item['file'])
 require(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==item['git_blob_sha1'],'input git blob '+item['file'])
rows=json.loads((ROOT/'inputs/profile11-pairs.json').read_text());require(len(rows)==159,'frozen count')
sources={'V':{'tuple':[1,1,2,0,0,0,0,0],'blocks':[[-2,'V'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-4,'V']]},'Z':{'tuple':[1,2,1,0,0,0,0,0],'blocks':[[-3,'Wp'],[-3,'T'],[-3,'T'],[-4,'V']]}}
expected_cubic=[42,43,53,62,63,64,65,66,67,73,74,76,102,103,110,111]
expected_quartic=[86,87,88,89,96,116,134]
expected_capacity=[130,132,141,142,143,144,145,148,149,150,151]
expected_compatible=sorted(expected_cubic+expected_quartic+expected_capacity)
result={}
for label,s in sources.items():
 E=s['blocks'];require(len(ordinary(E))==17 and degree(E)==-54,'source rank degree')
 require(signed(c.h0(E,3))=={'T':2,'Wp':1},'source cubic character')
 require(signed(chi(E,4))=={'D':2,'V':3,'P':3},'source quartic Euler')
 compatible=[];excluded=[];part={'cubic':[],'quartic':[],'capacity':[]};cert=[]
 for i,row in enumerate(rows):
  A,B=row['A'],row['B'];fail=[]
  require(degree(A)==row['a'] and degree(B)==row['b'],'record degree')
  require(len(ordinary(A))==len(ordinary(B))==3,'record rank')
  for u in range(-10,11):
   lhs=h1(A,u);rhs=h1(E,u); delta=rhs.copy();delta.subtract(lhs)
   neg=negative(delta)
   if neg:fail.append({'twist':u,'condition':'H1(A)<=H1(E)','negative':neg})
   lhs=c.h0(B,u);rhs=h1(E,-u);delta=rhs.copy();delta.subtract(lhs)
   neg=negative(delta)
   if neg:fail.append({'twist':u,'condition':'H0(B)<=H1(E(-u))','negative':neg})
  ok=not fail;require(ok==(s['tuple'] in row['compatible_E_types']),f'{label} stored compatibility {i}')
  if not ok:excluded.append({'index':i,'first_failure':fail[0]});continue
  compatible.append(i)
  cub=c.h0(A,3);cub.subtract(Counter(Wp=1,T=2))
  env=c.h0(A,2);env.update(chi(A,4));env.subtract(chi(E,4))
  witness={'index':i,'A':A,'B':B,'a':row['a'],'b':row['b'],'defect':row['defect'],'cubic_residual':signed(cub),'quartic_envelope':signed(env)}
  if negative(cub):stage='cubic';witness['negative']=negative(cub)
  elif negative(env):stage='quartic';witness['negative']=negative(env)
  else:
   stage='capacity';lam=ordinary(B);heights=[]
   for h1_ in range(5,11):
    h2=10-h1_; cap=h1_*lam[0]-h1_*(h1_+1)+h2*lam[1]-h2*(h2+1)
    heights.append({'heights':[h1_,h2],'cap':cap})
   cap=max(x['cap'] for x in heights); degL=-54-row['b']
   require(lam[0]<=-1,'negative top B');require(cap<=-70,'uniform capacity');require(degL>cap,'capacity contradiction')
   witness.update(ordinary_B=lam,all_height_capacities=heights,exact_cap=cap,actual_degree_L=degL,gap=degL-cap)
  witness['stage']=stage;part[stage].append(i);cert.append(witness)
 require(compatible==expected_compatible,label+' exact compatible list')
 require(part['cubic']==expected_cubic,label+' cubic partition')
 require(part['quartic']==expected_quartic,label+' quartic partition')
 require(part['capacity']==expected_capacity,label+' capacity partition')
 require(sum(map(len,part.values()))==34,label+' complete disjoint coverage')
 result[label]={'source_tuple':s['tuple'],'source_blocks':E,'compatible_indices':compatible,'partition':part,'certificates':cert,'incompatible_records':excluded,'survivors':[]}
# Independent combinatorial description of every nonincreasing rank sequence.
seqs=[]
def ranks(prefix,total,previous):
 if total==10:seqs.append(prefix);return
 for q in range(1,previous+1):
  if total+q<=10:ranks(prefix+[q],total+q,q)
ranks([],0,2)
require(len(seqs)==6,'six rank partitions')
require(sorted((sum(q>=1 for q in s),sum(q>=2 for q in s)) for s in seqs)==[(h,10-h) for h in range(5,11)],'rank/height completeness')
for s in seqs:
 require(sum(j*q for j,q in enumerate(s,1))>=30,'weighted rank lower bound')
 for row in result['V']['certificates']:
  if row['stage']!='capacity':continue
  lam=row['ordinary_B']; bound=sum(sum(lam[:q])-2*j*q for j,q in enumerate(s,1))
  h=(len(s),sum(q==2 for q in s));other=next(x['cap'] for x in row['all_height_capacities'] if x['heights']==list(h))
  require(bound==other,'direct rank/height capacity agreement')
output={'scope':'Exclusion of V and Z actual sources only in maximal profile (1,1), conditional on pinned necessity and actual-geometry inputs; no global repair.','sources':result,'rank_sequences':seqs,'checks':checks,'character_controls':c.checks}
print(json.dumps(output,indent=2,sort_keys=True))
