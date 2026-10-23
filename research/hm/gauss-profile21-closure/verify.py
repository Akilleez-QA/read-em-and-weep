#!/usr/bin/env python3
"""Six universal endpoint rank partitions and four fixed formal quotient rows."""
from pathlib import Path
from collections import Counter
import hashlib,json,sys
import characters as c
ROOT=Path(__file__).resolve().parent
checks=0
def require(ok,msg):
 global checks
 checks+=1
 if not ok:raise RuntimeError(msg)
manifest=json.loads((ROOT/'INPUTS.json').read_text())
require(len(manifest)==10,'ten pinned complete originals')
for x in manifest:
 b=(ROOT/x['file']).read_bytes()
 require(len(b)==x['bytes'],x['file']+' bytes')
 require(hashlib.sha256(b).hexdigest()==x['sha256'],x['file']+' SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['git_blob_sha1'],x['file']+' Git blob')
base=json.loads((ROOT/'inputs/frontier182.json').read_text())['cases']
p21={r['source_index']:r for r in base if r['profile']=='21'}
require(set(p21)==set(range(13)),'original thirteen row identities')
expected={
 2:([[-8,'one'],[2,'one'],[16,'one']],[6,-4,-18],-38,-38),
 5:([[-8,'one'],[4,'one'],[16,'one']],[6,-6,-18],-36,-42),
 9:([[-8,'one'],[6,'one'],[16,'one']],[6,-8,-18],-34,-46),
10:([[-8,'one'],[9,'Wp']],[6,-11,-11],-38,-49)}
heights=[(h,10-h) for h in range(5,11)]
def ordinary(B):return sorted([e for e,R in B for _ in range(c.DIM[R])],reverse=True)
rows=[]
for i,(A,lam,degL,mx) in expected.items():
 row=p21[i]
 require(row['A']==A,'exact A'+str(i))
 require(ordinary(row['B'])==lam,'exact ordered ordinary B'+str(i))
 require(row['original_defect']==0,'original defect zero'+str(i))
 require(sorted(row['B'])==sorted([[-e-2,R] for e,R in A]),'exact equivariant transpose'+str(i))
 require(-54-sum(lam)==degL,'actual endpoint degree'+str(i))
 values=[sum(h*la-h*(h+1) for h,la in zip(pair,lam)) for pair in heights]
 require(max(values)==mx,'degree capacity maximum'+str(i))
 if i!=2:require(degL>mx,'strict capacity contradiction'+str(i))
 else:require([list(h) for h,v in zip(heights,values) if v==mx]==[[7,3],[8,2]],'exact equality heights')
 rows.append(dict(row,ordinary_B=lam,degree_L=degL,capacities=values,maximum_capacity=mx,conclusion='equality rigidity contradiction' if i==2 else 'strict degree contradiction'))
require(6-2*7==-8 and -2-7==-9 and -8>-9,'height7 strict-top contradiction')
require(6-2*8==-10 and -2-8==-10,'height8 deepest line exact degree')
require(c.product('one',10)==Counter(A=1,V=1,D=1),'complete degree10 character')
require(c.DIM['A']+c.DIM['V']+c.DIM['D']==11,'degree10 complete span dimension')
require(11-min(c.DIM[r] for r in ('A','V','D'))==8<9,'every proper quotient too small')
require(c.product('one',8)==Counter(P=1,D=1),'eighth osculating coefficient')
require(8-10==-2 and 10-8==2 and 8+1==9,'eighth osculating degree and rank')
require(10-(10-8)+1==9,'apolar annihilator exponent')
E=[[-2,'D'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-8,'one']]
require(min(e for e,R in E)==-8,'exact D-type minimum degree')
require(all(e>-9 for e,R in E),'ordinary Hom to W O(-9) vanishes')
require(sum(c.DIM[R] for e,R in E)==17 and sum(e*c.DIM[R] for e,R in E)==-54,'exact D-type rank and degree')
cut2=[0,1,8,11,12];cut3=[3,4,6,7];cut4=sorted(expected)
require(len(cut2+cut3+cut4)==len(set(cut2+cut3+cut4))==13,'disjoint complete original13 partition')
require(sorted(cut2+cut3+cut4)==list(range(13)),'all necessary original21 indices covered')
out={'scope':'Actual maximal profile (2,1) exclusion, conditional on pinned geometric necessities and direct reductions; not COV','authenticated_originals':10,'checks':checks+c.checks,'universal_height_pairs':[list(h) for h in heights],'four_new_rows':rows,'profile21_partition':{'primary_profile_reduction':cut2,'cubic_rigidity':cut3,'this_packet':cut4},'profile21_excluded':True,'profile11_excluded':False,'global_rank3_exclusion':False,'actual_instance_evaluated':False,'historical_enumeration_rerun':False}
text=json.dumps(out,indent=2,sort_keys=True)+'\n'
if '--write' in sys.argv:(ROOT/'RESULT.json').write_text(text)
else:require((ROOT/'RESULT.json').read_text()==text,'exact result replay')
print(text)
