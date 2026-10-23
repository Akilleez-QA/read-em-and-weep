#!/usr/bin/env python3
"""Compose a reviewed quotient restriction; does not prove its geometric premise."""
import json,hashlib,argparse
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parent
LABEL='G3.11.8ae96830fd21'
E=[[-2,'P'],[-2,'D'],[-2,'D'],[-8,'one'],[-9,'W']]
Q=[
 [[-1,'Wp'],[-2,'P'],[-2,'D'],[-6,'one'],[-28,'one']],
 [[-1,'Wp'],[-1,'T'],[-4,'V'],[-6,'one'],[-28,'one']],
 [[-1,'Wp'],[-1,'Wp'],[-2,'D'],[-3,'Wp'],[-6,'one'],[-28,'one']],
 [[-1,'Wp'],[-1,'Wp'],[-1,'T'],[-6,'one'],[-10,'one'],[-28,'one']]]
def req(ok,msg):
 if not ok:raise ValueError(msg)
def canon(x):return tuple(sorted(Counter(map(tuple,x)).items()))
def load():
 pins=json.loads((ROOT/'pins.json').read_text());out=[]
 for name in ['six','restriction','catalog']:
  b=(ROOT/'inputs'/f'{name}.json').read_bytes();req(hashlib.sha256(b).hexdigest()==pins[name]['sha256'],'hash '+name);out.append(json.loads(b))
 return out
def compose(s,r,c):
 req(r['stable_label']==LABEL and r['labels_removed']==0,'scope')
 es=[e['id'] for e in c['E_catalog'] if canon(e['blocks'])==canon(E) and e['coefficients']==[0,0,0,0,0,1,1,0]];req(len(es)==1,'semantic E ambiguity');eid=es[0]
 qs=[]
 for blocks in Q:
  ids=[i for i,q in enumerate(c['Q_catalog']) if canon(q)==canon(blocks)];req(len(ids)==1,'semantic Q ambiguity');qs.append(ids[0])
 expected={(eid,q) for q in qs};keep={(eid,q) for q in qs[:2]};cut=expected-keep
 for key,values in [('starting_pairs',expected),('retained_pairs',keep),('removed_pairs',cut)]:
  raw=r[key];req(all(len(p)==2 and all(type(i)is int for i in p) for p in raw),'invalid pair');req(len(raw)==len(set(map(tuple,raw))) and set(map(tuple,raw))==values,key)
 req(r['template_assignment']==dict(zip(['I','II','III'],[qs[0],qs[0],qs[1]])),'template assignment')
 rows=s['records'];req(len(rows)==3 and len({x['id'] for x in rows})==3,'labels')
 before=set()
 for row in rows:
  ps=row['remaining_source_pairs'];req(all(len(p)==2 and all(type(i)is int for i in p) for p in ps),'pair type');req(len(ps)==row['remaining_source_pair_count']==len(set(map(tuple,ps))),'duplicate/count')
  before.update((row['id'],*p) for p in ps)
 req(len(before)==6 and s['remaining_label_count']==3 and s['profile_counts']=={'11':2,'12':0,'21':1},'six checkpoint')
 req({row['id']:row['profile'] for row in rows}=={LABEL:'11','G3.11.cce6e3ba4eeb':'11','G3.21.d610e381ed75':'21'},'stable identities')
 req({(e,q) for label,e,q in before if label==LABEL}==expected,'target predecessor')
 removed={(LABEL,*p) for p in cut};after=before-removed
 req(len(removed)==2 and len(after)==4 and before==after|removed and not after&removed,'6=2+4')
 req({p for p in after if p[0]!=LABEL}=={p for p in before if p[0]!=LABEL},'unrelated changed')
 req({p[0] for p in before}=={p[0] for p in after},'label exclusion')
 out=[]
 for row in rows:
  new=dict(row);new['remaining_source_pairs']=sorted([e,q] for label,e,q in after if label==row['id']);new['remaining_source_pair_count']=len(new['remaining_source_pairs']);out.append(new)
 req(sorted(x['remaining_source_pair_count'] for x in out)==[1,1,2],'2+1+1')
 return {'kind':'composed_necessary_pair_ledger','pair_accounting':{'before':6,'removed':2,'after':4},'remaining_label_count':3,'profile_counts':s['profile_counts'],'records':out,'removed_pairs':sorted(map(list,removed)),'actual_instance_evaluated':False,'complete_proof':False,'historical_six_preserved':True,'restriction_kind':'new_source126_quotient_deduction'}
if __name__=='__main__':
 pub=json.loads((ROOT/'publication.json').read_text());req(pub['independent_review']=='PASS' and len(pub['theorem_commit'])==40,'theorem publication/review pending')
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();result=compose(*load());path=ROOT/'frontier.json'
 if a.write:path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 req(json.loads(path.read_text())==result,'replay mismatch');print('PASS:6=2+4;4=2+1+1;three labels;unrelated pairs preserved')
