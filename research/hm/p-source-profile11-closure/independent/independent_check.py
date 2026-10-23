from pathlib import Path
import json,hashlib,sys
from functools import lru_cache
from collections import Counter
ROOT=Path(__file__).parent
exec((ROOT/'character_base.py').read_text())
product=lru_cache(None)(product)
DIM={r:int(c[0][0]) for r,c in chars.items()}
# Independently authenticate exact fetched bytes against Git blobs. apply_patch may add one newline.
auth=[]
for m in json.loads((ROOT/'FETCH.json').read_text()):
 p=ROOT/'originals'/m['name']; raw=p.read_bytes()
 def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
 if blob(raw)!=m['git_blob'] and raw.endswith(b'\n') and blob(raw[:-1])==m['git_blob']:raw=raw[:-1];p.write_bytes(raw)
 need(blob(raw)==m['git_blob'])
 auth.append(dict(m,sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw)))
(ROOT/'AUTHENTICATION.json').write_text(json.dumps(auth,indent=2)+'\n')
rows=json.loads((ROOT/'originals/profile11-pairs.json').read_text());need(len(rows)==159)
P=[1,1,1,0,1,0,0,0]
E=[[-2,'P'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-5,'Wp']]
need(sum(DIM[r] for e,r in E)==17);need(sum(e*DIM[r] for e,r in E)==-54)
def h1(B,t):
 out=Counter()
 for e,r in B:out.update(product(r,-e-t-2))
 return out
def le(a,b):return all(a[r]<=b[r] for r in chars)
def deg(B):return sum(e*DIM[r] for e,r in B)
def shape(A):return sorted(map(tuple,A))
shapes=[shape([[-1,'Wp'],[4,'one']]),shape([[-1,'Wp'],[10,'one']]),shape([[-3,'Wp'],[16,'one']]),shape([[-5,'Wp'],[16,'one']])]
compatible=[];prior=[];new=[];remaining=[];records=[]
for i,row in enumerate(rows):
 A,B=row['A'],row['B'];need(deg(A)==row['a']);need(deg(B)==row['b'])
 need(row['defect']==-6-deg(A)-deg(B))
 passes=all(le(h1(A,u),h1(E,u)) and le(h0(B,u),h1(E,-u)) for u in range(-10,11))
 need(passes==(P in row['compatible_E_types']))
 if not passes:continue
 compatible.append(i)
 if not le(Counter(Wp=1,T=2),h0(A,3)):prior.append(i);continue
 if shape(A) in shapes:new.append(i);continue
 remaining.append(i)
 lambdas=sorted([e for e,r in B for _ in range(DIM[r])],reverse=True);need(len(lambdas)==3)
 caps=[];rankcaps=[]
 # Six possible nonincreasing positive rank sequences with terms at most two and sum ten.
 for twos in range(6):
  q=[2]*twos+[1]*(10-2*twos)
  rankcap=sum(sum(lambdas[:r])-2*(j+1)*r for j,r in enumerate(q))
  h1_=10-twos;h2_=twos
  cap=h1_*lambdas[0]-h1_*(h1_+1)+h2_*lambdas[1]-h2_*(h2_+1)
  need(cap==rankcap);caps.append(cap)
 ell=-54-deg(B);need(ell>max(caps))
 records.append(dict(index=i,A=A,B=B,defect=row['defect'],ordinary_B=lambdas,degree_L=ell,capacities_h1_10_to_5=caps,max_capacity=max(caps),gap=ell-max(caps)))
need(len(compatible)==35);need(len(prior)==16);need(len(new)==8);need(len(remaining)==11)
need(set(prior)|set(new)|set(remaining)==set(compatible))
need(sum(map(len,[prior,new,remaining]))==len(set(compatible)))
need(compatible==[42,43,53,62,63,64,65,66,67,73,74,76,86,87,88,89,96,102,103,109,110,111,116,130,132,134,141,142,143,144,145,148,149,150,151])
need(new==[86,87,88,89,96,109,116,134])
# Compare independent full records and source witnesses to frozen author's certificate.
PACK=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT.parent/'p-source-profile11-closure'
author=json.loads((PACK/'RESULT.json').read_text())
need(author['P_compatible_indices']==compatible)
need(author['partition']['cubic1140']==prior)
need(sorted(author['partition']['doublet1156']+author['partition']['flag1159'])==new)
need(author['partition']['dual_capacity']==remaining)
by={x['index']:x for x in author['records']}
for r in records:
 a=by[r['index']]
 need(a['ordinary_B_degrees']==r['ordinary_B'])
 need(a['degree_L']==r['degree_L'])
 need(a['capacities_for_h1_5_through_10']==r['capacities_h1_10_to_5'][::-1])
 need(a['capacity']==r['max_capacity']);need(a['contradiction_gap']==r['gap'])
for w in author['non_P_compatibility_witnesses']:
 x=rows[w['index']]; expected=[]
 for u in range(-10,11):
  for label,aa,bb in [('H1E-H1A',h1(E,u),h1(x['A'],u)),('H1Edual-H0B',h1(E,-u),h0(x['B'],u))]:
   negative={r:aa[r]-bb[r] for r in chars if aa[r]<bb[r]}
   if negative:expected.append(dict(twist=u,condition=label,negative=negative))
 need(expected==w['witnesses'])
# All author's immutable originals equal independently fetched byte identities.
for m in json.loads((PACK/'INPUTS.json').read_text()):
 candidates=[a for a in auth if a['ref']==m['ref'] and a['path']==m['path']]
 need(len(candidates)==1)
 a=candidates[0];need(a['sha256']==m['sha256'] and a['git_blob']==m['git_blob_sha1'] and a['bytes']==m['bytes'])
 need((PACK/m['file']).read_bytes()==(ROOT/'originals'/a['name']).read_bytes())
# Compare all multiplication characters to the separate authored McKay-ring implementation.
import importlib.util
spec=importlib.util.spec_from_file_location('production_characters',ROOT/'originals/characters.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
for r in chars:
 for n in range(41):need(product(r,n)==c.product(r,n))
print(json.dumps(dict(checks=checks,source_compatible=compatible,cubic_excluded=prior,new_shapes_excluded=new,capacity_excluded=remaining,capacity_records=records),indent=2))
