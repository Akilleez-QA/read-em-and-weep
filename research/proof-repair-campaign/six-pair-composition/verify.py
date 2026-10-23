#!/usr/bin/env python3
"""Exact composition of pinned necessary-pair certificates, not an instance proof."""
import json, hashlib, argparse
from pathlib import Path
from collections import Counter
from copy import deepcopy
ROOT=Path(__file__).resolve().parent
S='G3.21.d610e381ed75'; C='G3.11.cce6e3ba4eeb'; U='G3.11.8ae96830fd21'
def require(p,m):
 if not p: raise ValueError(m)
def canon(b): return tuple(sorted(Counter(map(tuple,b)).items()))
def load():
 pins=json.loads((ROOT/'pins.json').read_text()); out=[]
 for n in ['before','source2','cdf','catalog']:
  b=(ROOT/'inputs'/f'{n}.json').read_bytes(); require(hashlib.sha256(b).hexdigest()==pins[n]['sha256'],'input hash '+n); out.append(json.loads(b))
 return out
def pairs(rows):
 require(len({r['id'] for r in rows})==len(rows),'duplicate label')
 ans=set()
 for r in rows:
  ps=r['remaining_source_pairs'];require(all(len(p)==2 and all(type(v)is int for v in p) for p in ps),'invalid ids')
  require(len(set(map(tuple,ps)))==len(ps),'duplicate pair')
  require(r['remaining_source_pair_count']==len(ps),'row count')
  ans.update((r['id'],*p) for p in ps)
 return ans
def match(cat,eb,qb,coeff):
 es=[e['id'] for e in cat['E_catalog'] if canon(e['blocks'])==canon(eb) and e['coefficients']==coeff]
 qs=[i for i,q in enumerate(cat['Q_catalog']) if canon(q)==canon(qb)]
 require(len(es)==len(qs)==1,'nonunique semantic match');return es[0],qs[0]
def compose(before,source,cdf,cat):
 b=pairs(before['records']);a=pairs(source['records'])
 require({x[0] for x in b}=={S,C,U} and len(b)==114,'wrong predecessor')
 require(source['source2']['id']==S and cdf['label']==C,'wrong scope')
 require(source['source2']['E_tuple']==[0,1,0,0,0,0,1,0] and cdf['source_tuple']==[0,0,1,1,0,1,0,0],'wrong source tuple')
 require(canon(source['source2']['E_blocks'])==canon([[-9,'W'],[-3,'T'],[-2,'P'],[-2,'D']]),'wrong source2 E')
 require(canon(source['source2']['Qstar_blocks'])==canon([[-2,'P'],[-2,'D'],[-6,'A'],[-18,'one']]),'wrong source2 quotient')
 require(canon(cdf['source_blocks'])==canon([[-2,'P'],[-2,'D'],[-4,'V'],[-4,'P'],[-8,'one']]),'wrong cdf E')
 require(canon(cdf['quotient_dual_blocks'])==canon([[-18,'one'],[-7,'S'],[-1,'Wp'],[-1,'T']]),'wrong cdf quotient')
 sp=match(cat,source['source2']['E_blocks'],source['source2']['Qstar_blocks'],source['source2']['E_tuple'])
 cp=match(cat,cdf['source_blocks'],cdf['quotient_dual_blocks'],cdf['source_tuple'])
 require(source['source2']['matched_pair']==list(sp),'source2 semantic ID')
 require((cdf['E_catalog_id'],cdf['Q_catalog_id'])==cp,'cdf semantic ID')
 cut1=b-a;require(a<=b and len(a)==37 and len(cut1)==77 and {x[0] for x in cut1}=={S},'source2 cut')
 require({x for x in a if x[0]==S}=={(S,*sp)},'source2 survivor')
 for old in before['records']:
  new=next(r for r in source['records'] if r['id']==old['id'])
  require(old['A']==new['A'] and old['B']==new['B'] and old['profile']==new['profile'],'identity drift')
  if old['id']!=S:require(old==new,'unrelated source2 row changed')
 require(cdf['input_pair_count']==32 and cdf['removed_pair_count']==31 and cdf['label_count_delta']==0,'cdf counts')
 require(cdf['kept_pairs']==[list(cp)],'cdf survivor')
 raw=cdf['removed_pairs'];require(len(raw)==len(set(map(tuple,raw)))==31,'duplicate cdf cut')
 cut2={(C,*p) for p in raw};keep={(C,*cp)}
 require(not cut1&cut2 and cut2<=a,'overlap or missing cut')
 require({p for p in a if p[0]==C}==cut2|keep and not cut2&keep,'cdf exact partition')
 final=a-cut2
 require(len(final)==6 and b==cut1|cut2|final and not cut1&final and not cut2&final,'disjoint accounting')
 require({x for x in final if x[0]==U}=={x for x in b if x[0]==U},'source126 changed')
 require({x[0] for x in final}=={S,C,U},'label cut')
 rows=[]
 for r in source['records']:
  ps=sorted([e,q] for lab,e,q in final if lab==r['id'])
  rows.append({'id':r['id'],'profile':r['profile'],'A':r['A'],'B':r['B'],'remaining_source_pairs':ps,'remaining_source_pair_count':len(ps)})
 require({r['id']:r['remaining_source_pair_count'] for r in rows}=={U:4,C:1,S:1},'4+1+1')
 return {'kind':'composed_necessary_pair_ledger','pair_accounting':{'before':114,'source2_removed':77,'cdf_removed':31,'after':6},'remaining_label_count':3,'profile_counts':{'11':2,'12':0,'21':1},'records':rows,'disjoint_cut_ledger':{'source2':sorted(map(list,cut1)),'cdf':sorted(map(list,cut2))},'actual_instance_evaluated':False,'complete_proof':False,'source2_cut_is_overdue_structural_integration':True}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();result=compose(*load());out=ROOT/'frontier.json'
 if a.write:out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 require(json.loads(out.read_text())==result,'result replay mismatch');print('PASS: disjoint 114=77+31+6; six=4+1+1; three labels retained; semantic matching')
