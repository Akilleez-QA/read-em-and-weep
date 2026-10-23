#!/usr/bin/env python3
"""Append complete source exclusions; preserve all earlier checkpoints."""
import argparse
from copy import deepcopy
import hashlib
import json
import verify_source_frontier_through823 as prior
ROOT=prior.ROOT
require=prior.require
PREVIOUS_SHA256='54068156ebad88ac4dce3b4c03ce7e7c3ad7e0ec1d5940c6ff001f8d48fcc47c'
PINS_SHA256='9b2301ac6e74da6f06bb9b5061665dcc536870f76700e790e5afa6d2dd309418'
SPLIT='G3.11.863639aa192e';BALANCED=prior.BALANCED
SOURCES={
 'ef':{'coefficients':[0,0,0,0,1,1,0,1],'blocks':[[-2,'P'],[-2,'P'],[-2,'D'],[-5,'Wp'],[-8,'one'],[-10,'one']]},
 'be':{'coefficients':[0,1,0,0,1,0,0,1],'blocks':[[-2,'P'],[-2,'P'],[-3,'T'],[-5,'Wp'],[-10,'one']]},
 'ce':{'coefficients':[0,0,1,0,1,0,0,1],'blocks':[[-2,'V'],[-2,'P'],[-2,'P'],[-4,'V'],[-5,'Wp'],[-10,'one']]},
 'cf':{'coefficients':[0,0,1,0,0,1,0,1],'blocks':[[-2,'V'],[-2,'P'],[-2,'D'],[-4,'V'],[-8,'one'],[-10,'one']]},
}
def rule(proof,label,source):return {'proof':proof,'label':label,'source':source,'kind':'source_edge','coverage':'complete_source'}
RULES=[rule('pr814',SPLIT,'ef'),rule('pr814',SPLIT,'be'),rule('pr814',BALANCED,'ef'),rule('pr814',BALANCED,'be'),rule('pr814',BALANCED,'ce'),rule('pr826',SPLIT,'ce'),rule('pr828',SPLIT,'cf'),rule('pr828',BALANCED,'cf')]
CORROBORATION={'proof':'pr828','label':SPLIT,'source':'ce','already_counted_by':'pr826','additional_removed_pair_count':0,'reason':'Independent proof of the identical full source exclusion; not a second deletion.'}

def load_inputs():
 s,c,oldpins=prior.load_inputs();snapshot=prior.build(s,c,oldpins)
 raw=(ROOT/'frontier-source-through823.json').read_bytes()
 require(hashlib.sha256(raw).hexdigest()==PREVIOUS_SHA256,'Through823 snapshot changed')
 require(json.loads(raw)==snapshot,'Through823 replay mismatch')
 raw=(ROOT/'source-pins-source-through828.json').read_bytes()
 require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'New pin manifest changed')
 pins=json.loads(raw)
 for key,p in pins.items():
  b=(ROOT/p['local_file']).read_bytes()
  require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==p['git_blob_sha1'],'Proof blob mismatch: '+key)
 pins['pr814']=oldpins['pr814-proof.md']
 return snapshot,c,pins

def intersect(snapshot,catalog,rules=RULES):
 require(len({e['id'] for e in catalog})==len(catalog),'Duplicate catalog ID')
 ids={name:prior.identify(catalog,d) for name,d in SOURCES.items()}
 rows={r['id']:r for r in snapshot['records']}
 require(len(rows)==len(snapshot['records']) and set(rows)==set(snapshot['remaining_ids']),'Stable ID mismatch')
 relations={}
 for label,r in rows.items():
  require(r['profile']==prior.prior.prior.historical.profile(label),'Profile mismatch')
  pairs={tuple(p) for p in r['remaining_source_pairs']}
  require(len(pairs)==len(r['remaining_source_pairs'])==r['remaining_source_pair_count'],'Duplicate pair or count mismatch')
  require(all(e in {x['id'] for x in catalog} for e,q in pairs),'Unknown source reference')
  relations[label]=pairs
 before=deepcopy(relations);ledger=[];seen=set()
 for r in rules:
  require(r['kind']=='source_edge' and r['coverage']=='complete_source','Conditional or wrong-kind cut')
  label=r['label'];require(label in relations,'Unknown stable ID');key=(label,prior.canonical(SOURCES[r['source']]['blocks']))
  require(key not in seen,'Double source exclusion');seen.add(key)
  eid=ids[r['source']];removed={p for p in relations[label] if p[0]==eid};relations[label]-=removed
  ledger.append(dict(r,source_definition=deepcopy(SOURCES[r['source']]),matched_local_E_id=eid,
    removed_pairs=sorted(map(list,removed)),actual_additional_pair_count=len(removed),already_absent_in_input=not bool(removed),label_count_delta=0))
 records=[]
 for label in sorted(rows):
  kept=relations[label];removed=before[label]-kept
  require(not kept&removed and kept|removed==before[label],'Partition mismatch')
  records.append({'id':label,'profile':rows[label]['profile'],'A':rows[label]['A'],'B':rows[label]['B'],
   'input_necessary_pair_count':len(before[label]),'removed_pair_count':len(removed),
   'remaining_source_pair_count':len(kept),'remaining_source_pairs':sorted(map(list,kept)),
   'removed_source_pairs':sorted(map(list,removed))})
 return records,ledger

def build(snapshot,catalog,pins):
 records,ledger=intersect(snapshot,catalog)
 ids=sorted(r['id'] for r in records if r['remaining_source_pair_count'])
 require(ids==snapshot['remaining_ids'] and len(ids)==9,'Unexpected empty relation; do not infer whole-label geometry')
 require([r['actual_additional_pair_count'] for r in ledger]==[19,19,16,16,16,19,19,16],'Per-source accounting mismatch')
 total=sum(r['remaining_source_pair_count'] for r in records)
 require(total==840 and sum(r['removed_pair_count'] for r in records)==140,'Tuple accounting mismatch')
 profiles=prior.prior.prior.historical.counts(ids);require(profiles=={'11':8,'12':0,'21':1},'Profile accounting mismatch')
 by_label={r['id']:r for r in records};require(by_label[SPLIT]['remaining_source_pair_count']==57 and by_label[BALANCED]['remaining_source_pair_count']==32,'Low-positive subtotal mismatch')
 catalog_by_id={e['id']:e for e in catalog}
 expected_low={SPLIT:{(0,1,0,0,0,1,0,1),(0,1,1,0,0,0,0,1),(0,2,0,0,0,0,0,1)},BALANCED:{(0,1,1,0,0,0,0,1),(0,2,0,0,0,0,0,1)}}
 for label,expected in expected_low.items():
  actual={tuple(catalog_by_id[e]['coefficients']) for e,q in by_label[label]['remaining_source_pairs']}
  require(actual==expected,'Remaining low-positive source types mismatch')
 # Keep still-unencoded conditional results. Remove superseded cf/ce and deferred complete-cut entries.
 unencoded=[deepcopy(x) for x in snapshot['unencoded_or_deferred_results'] if x['scope'] not in ('cf and split-ce sources','Other complete ef/be exclusions in both low-positive labels and balanced ce')]
 return {'schema_version':1,'checkpoint':'source-strata-through828','not_proof_completion':True,'geometric_constraints_fully_encoded':False,
  'scope':'Append the complete PR814 ef/be and balanced-ce source cuts, PR826 split-ce cut, and PR828 cf cuts. Deduplicate PR828 split-ce corroboration. No broader conditional cuts.',
  'previous_checkpoint':{'file':'frontier-source-through823.json','sha256':PREVIOUS_SHA256,'labels':9,'necessary_pairs':980},
  'remaining_label_count':9,'remaining_ids':ids,'remaining_profile_counts':profiles,'new_full_label_exclusions':[],
  'new_source_edge_exclusion_ledger':ledger,'overlapping_proof_claims_not_recounted':[CORROBORATION],
  'previous_source_edge_exclusion_ledger':snapshot['new_source_edge_exclusion_ledger'],
  'pair_accounting':{'input_necessary_pairs':980,'pr814_additional_removed_pairs':86,'pr826_additional_removed_pairs':19,'pr828_additional_removed_pairs':35,'additional_removed_pairs':140,'remaining_necessary_pairs':840,'historical_through806_pairs':1004,'cumulative_source_pair_cuts':164},
  'low_positive_remaining':{SPLIT:{'source_names':['bf','bc','bb'],'pair_count':57},BALANCED:{'source_names':['bc','bb'],'pair_count':32}},
  'source_definitions':SOURCES,'source_pins':pins,'new_source_pins_sha256':PINS_SHA256,
  'unencoded_or_deferred_results':unencoded,
  'catalog_reference':snapshot['catalog_reference'],'matching_rule':snapshot['matching_rule'],
  'proof_boundary':'Pinned public written source exclusions are input assumptions, not re-proved by finite accounting. Retained pairs are necessary formal witnesses, not realizations. No whole-label theorem, actual-instance evaluation or consumed experiment is inferred or executed.',
  'records':records}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 result=build(*load_inputs());p=ROOT/'frontier-source-through828.json'
 if args.write:p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==result,'Artifact differs from replay')
 print(json.dumps({'status':'PASS','labels':9,'profiles':result['remaining_profile_counts'],'remaining_necessary_pairs':840,'additional_cuts':140,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()},sort_keys=True))
if __name__=='__main__':main()
