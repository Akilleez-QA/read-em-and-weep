#!/usr/bin/env python3
"""Symbolic bundle arithmetic and exact targeted catalogue certificate; no instance evaluation."""
import json, hashlib
from pathlib import Path
from copy import deepcopy
from collections import Counter
ROOT=Path(__file__).resolve().parent
LABEL='G3.11.cce6e3ba4eeb'
TUPLE=[0,0,1,1,0,1,0,0]
E=[[-2,'P'],[-2,'D'],[-4,'V'],[-4,'P'],[-8,'one']]
Q=[[-18,'one'],[-7,'S'],[-1,'Wp'],[-1,'T']]
DIMS={'one':1,'W':2,'Wp':2,'S':4,'V':3,'P':4,'D':5,'T':6}
A=[[-8,'one'],[2,'one'],[16,'one']];B=[[-18,'one'],[-4,'one'],[6,'one']]
def require(p,m):
 if not p:raise ValueError(m)
def canon(x):return Counter(map(tuple,x))
def gitsha(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def load():
 pins=json.loads((ROOT/'input-pins.json').read_text());out={}
 for k,p in pins.items():
  b=(ROOT/p['file']).read_bytes();require(gitsha(b)==p['git_blob'],'Input tampered: '+k)
  out[k]=b.decode() if k=='proof' else json.loads(b)
 return out
def ids(catalog,dual):
 es=[x['id'] for x in catalog['E_catalog'] if x['coefficients']==TUPLE and canon(x['blocks'])==canon(E)]
 qs=[i for i,x in enumerate(dual['profiles']) if canon(x)==canon(Q)]
 require(es==[14] and qs==[148],'Missing or nonunique exact bundle identity')
 require(catalog['Q_catalog']==dual['profiles'],'Q catalogues disagree')
 return es[0],qs[0]
def fragment(snapshot,catalog,dual,original,label=LABEL,source_tuple=TUPLE):
 require(label==LABEL and source_tuple==TUPLE,'Wrong target scope')
 require(original[127]['defect']==0 and source_tuple in original[127]['compatible_E_types'],'Original source mismatch')
 require(canon(original[127]['A'])==canon(A) and canon(original[127]['B'])==canon(B),'Original endpoints mismatch')
 eid,qid=ids(catalog,dual)
 rows=snapshot['records'];require(len({r['id'] for r in rows})==len(rows),'Duplicate labels')
 candidates=[r for r in rows if r['id']==label];require(len(candidates)==1,'Target label missing')
 row=candidates[0];require(canon(row['A'])==canon(A) and canon(row['B'])==canon(B),'Target endpoints mismatch')
 pairs=row['remaining_source_pairs'];require(all(len(p)==2 and all(type(v)is int for v in p) for p in pairs),'Invalid pair IDs')
 old=set(map(tuple,pairs));require(len(old)==len(pairs)==32 and {e for e,q in old}=={eid},'Expected exact unique cdf row')
 keep={(eid,qid)};require(keep<=old,'Forced quotient missing')
 cut=old-keep;require(len(cut)==31 and not cut&keep and old==cut|keep,'Incorrect exact partition')
 # Filter keyed by label AND original source pair; never remove a Q id globally.
 allbefore={(r['id'],*p) for r in rows for p in r['remaining_source_pairs']}
 removed={(label,*p) for p in cut};after=allbefore-removed
 require({p for p in allbefore if p[0]!=label}=={p for p in after if p[0]!=label},'Other label changed')
 require({p[0] for p in allbefore}=={p[0] for p in after},'Label removed')
 return {'kind':'necessary_quotient_specialization','label':label,'original_source_index':127,'source_tuple':TUPLE,'source_blocks':E,'quotient_dual_blocks':Q,'E_catalog_id':eid,'Q_catalog_id':qid,'input_pair_count':32,'kept_pairs':sorted(map(list,keep)),'removed_pairs':sorted(map(list,cut)),'removed_pair_count':31,'label_count_delta':0,'requires_normal_form_commit':'1528ff8ea56b21e03f7501a962bdaa6728a75904','scope':'Only this label and exact c-d-f source; abstract bundle splitting, not horizontal splitting or actual realization.'}
def main():
 x=load();checks=0;negatives=0
 def check(p,m):
  nonlocal checks
  require(p,m);checks+=1
 def reject(f):
  nonlocal negatives
  try:f()
  except ValueError:negatives+=1;return
  raise ValueError('Negative control accepted')
 # Apolar annihilator index sets for every symbolic universal subspace through n=18.
 for n in range(1,19):
  for k in range(n):
   original=set(range(k+1));ann={j for j in range(n+1) if n-j not in original}
   check(ann==set(range(n-k)),'Apolar orientation')
   check((k+1)+(n-k)==n+1 and (k+1)*(k-n)+(n-k)*(k+1)==0,'Universal rank/degree')
 h1=lambda d:max(-d-1,0)
 check(4*h1(18-7)+8*h1(18-1)==0,'Correct Ext orientation')
 check(4*h1(7-18)+8*h1(1-18)==168,'Reverse Ext must not vanish')
 check(sum(DIMS[r] for d,r in Q)==13,'Q rank')
 check(sum(d*DIMS[r] for d,r in Q)==-54,'Q degree')
 check(sum(DIMS[r]*max(-d,0) for d,r in Q)==54,'h0 Q(-1)')
 check(sum(DIMS[r]*max(-d-1,0) for d,r in Q)==41,'h0 Q(-2)')
 check(sum(DIMS[r] for d,r in E)==17 and sum(d*DIMS[r] for d,r in E)==-54,'E rank/degree')
 result=fragment(x['frontier'],x['catalog'],x['dual'],x['original']);checks+=1
 for wrong in ['G3.21.d610e381ed75','G3.11.8ae96830fd21']:
  reject(lambda:fragment(x['frontier'],x['catalog'],x['dual'],x['original'],label=wrong))
 reject(lambda:fragment(x['frontier'],x['catalog'],x['dual'],x['original'],source_tuple=[1,1,1,0,0,1,0,0]))
 for mutation in ['duplicate','endpoint','missing148','boolid']:
  s=deepcopy(x['frontier']);r=next(t for t in s['records'] if t['id']==LABEL)
  if mutation=='duplicate':r['remaining_source_pairs'].append(r['remaining_source_pairs'][0])
  if mutation=='endpoint':r['A'][0][0]=-6
  if mutation=='missing148':r['remaining_source_pairs']=[p for p in r['remaining_source_pairs'] if p!=[14,148]]
  if mutation=='boolid':r['remaining_source_pairs'][0][0]=True
  reject(lambda:fragment(s,x['catalog'],x['dual'],x['original']))
 bad=deepcopy(x['dual']);bad['profiles'].append(Q);reject(lambda:ids(x['catalog'],bad))
 bad=deepcopy(x['catalog']);bad['E_catalog'].append(dict(bad['E_catalog'][14]));reject(lambda:ids(bad,x['dual']))
 bad=deepcopy(x['catalog']);bad['Q_catalog'][148][0][0]=1;reject(lambda:ids(bad,x['dual']))
 # An already-authenticated checkpoint may have changed only source2; targeted result is unchanged.
 s=deepcopy(x['frontier']);r=next(t for t in s['records'] if t['id']=='G3.21.d610e381ed75');r['remaining_source_pairs']=[[13,21]]
 check(fragment(s,x['catalog'],x['dual'],x['original'])==result,'Independent source2 composition')
 (ROOT/'targeted-filter.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print(f'PASS {checks} symbolic/identity checks; {negatives} negative controls; cdf32=1+31; no label cut')
if __name__=='__main__':main()
