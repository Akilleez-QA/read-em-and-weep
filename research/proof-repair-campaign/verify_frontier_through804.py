#!/usr/bin/env python3
"""Extend, never overwrite, the historical 17-label planning snapshot."""
import argparse
from copy import deepcopy
import hashlib
import json
import verify_frontier as historical

ROOT=historical.ROOT
HISTORICAL_SHA256='3315d80f651911f87e8b12006263994cd591a4b5938e621fcf6bda111332b77c'
PINS_SHA256='4ce0d8673a1f57dc9395ef95bfb17fa13ebc0190357aa1fd31760b28e41c8652'
PROOF_SHA256={
 'pr802':'a18a6990f719592d71853692157161a9ca5fe6b7f2a78edacbfa060bb3513459',
 'pr803':'58752667d3b9cf603cc4a99b3ebce8b2f0e85af92ea8d5937cf3314d7d5edfa3',
 'pr804':'5f145e5fb7c6b791c9200d5c58d58618312443c80cc5ae30db1dbef132a41527',
}
CUTS=[
 {'source':'pr802','kind':'full_label','ids':['G3.11.16ee1aa30a9c','G3.11.db4688c30472']},
 {'source':'pr803','kind':'full_label','ids':['G3.11.cb71f599859d','G3.11.0fe2a757439f']},
 {'source':'pr804','kind':'full_label','ids':['G3.11.64d33b6d4139']},
]
require=historical.require

def load_inputs():
 base,prior,pins=historical.load_inputs()
 before=(ROOT/'frontier.json').read_bytes()
 require(hashlib.sha256(before).hexdigest()==HISTORICAL_SHA256,'Historical snapshot changed')
 snapshot=json.loads(before)
 require(snapshot==historical.build(base,prior,pins),'Historical replay mismatch')
 raw=(ROOT/'source-pins-through804.json').read_bytes()
 require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'New source pins changed')
 newpins=json.loads(raw)
 require(set(newpins)==set(PROOF_SHA256),'Wrong proof set')
 for key,pin in newpins.items():
  b=(ROOT/pin['local_file']).read_bytes()
  require(hashlib.sha256(b).hexdigest()==PROOF_SHA256[key],'Proof SHA256 mismatch: '+key)
  require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==pin['git_blob_sha1'],'Proof Git blob mismatch: '+key)
 return snapshot,newpins

def restrict(snapshot,cuts):
 """Exact relational restriction. Never construct a Cartesian product."""
 ids,ledger=historical.apply_label_cuts(snapshot['remaining_ids'],cuts)
 source={r['id']:r for r in snapshot['records']}
 require(len(source)==len(snapshot['records']) and set(source)==set(snapshot['remaining_ids']),'Historical record/ID mismatch')
 for i,r in source.items():
  require(r['profile']==historical.profile(i),'Record profile mismatch')
  pairs=historical.pair_set(r['baseline_pairs'])
  require(len(pairs)==r['baseline_pair_count'],'Record tuple count mismatch')
 records=[deepcopy(source[i]) for i in ids]
 for stage in ledger:
  stage['removed_baseline_pairs']=sum(source[i]['baseline_pair_count'] for i in stage['ids'])
 return ids,ledger,records

def build(snapshot,pins):
 require(snapshot['remaining_label_count']==17 and snapshot['remaining_profile_counts']=={'11':16,'12':0,'21':1},'Historical profile mismatch')
 ids,ledger,records=restrict(snapshot,CUTS)
 all_cuts=[{k:c[k] for k in ('source','kind','ids')} for c in snapshot['full_label_exclusion_ledger']]+CUTS
 original_ids=snapshot['remaining_ids']+[i for c in snapshot['full_label_exclusion_ledger'] for i in c['ids']]
 combined_ids,combined_ledger=historical.apply_label_cuts(original_ids,all_cuts)
 require(combined_ids==ids,'Cumulative cuts disagree')
 require(len(ids)==12 and historical.counts(ids)=={'11':11,'12':0,'21':1},'Current profile mismatch')
 tuples=sum(r['baseline_pair_count'] for r in records)
 removed=sum(s['removed_baseline_pairs'] for s in ledger)
 require((tuples,removed)==(1319,471),'Baseline tuple restriction mismatch')
 require(tuples+removed==snapshot['pair_accounting']['current17_baseline_relation']==1790,'Tuple partition mismatch')
 require([s['removed_baseline_pairs'] for s in ledger]==[441,18,12],'Per-stage tuple mismatch')
 return {
  'schema_version':1,'snapshot':'through804','scope':'New exact ledger extension of the historical PR805 seventeen-label snapshot using the pinned written full-label exclusions in PR802, PR803 and PR804.',
  'not_proof_completion':True,'geometric_constraints_fully_encoded':False,
  'historical_snapshot':{'file':'frontier.json','sha256':HISTORICAL_SHA256,'publication_commit':'d79b4ed8263076476296066def7f0c5be7752707','url':'https://github.com/Akilleez-QA/read-em-and-weep/blob/d79b4ed8263076476296066def7f0c5be7752707/research/proof-repair-campaign/frontier.json','labels':17,'baseline_pairs':1790},
  'remaining_label_count':len(ids),'remaining_ids':ids,'remaining_profile_counts':historical.counts(ids),
  'new_full_label_exclusion_ledger':ledger,'cumulative_full_label_exclusion_ledger':combined_ledger,
  'historical_source_edge_exclusion_ledger':snapshot['source_edge_exclusion_ledger'],
  'inherited_exclusions_not_recounted':snapshot['inherited_exclusions_not_recounted'],
  'pair_accounting':{'historical17_baseline_relation':1790,'new_removed_baseline_pairs':471,'current12_baseline_relation':tuples,'pr796_baseline_relation':1996,'total_post_pr796_full_label_pairs_removed':677},
  'pair_boundary':'Exactly the existing PR796 paired-witness relation restricted to the twelve surviving original IDs. No new source-edge geometry is claimed fully encoded, and no survivor is asserted realized.',
  'proof_boundary':'Public written geometric conclusions are input assumptions. This program checks exact finite accounting, not the mathematical validity of the proofs or any actual-instance rank. It does not duplicate proof review.',
  'source_pins':dict(snapshot['source_pins'],**pins),'new_proof_sha256':PROOF_SHA256,'new_source_pins_sha256':PINS_SHA256,
  'catalog_reference':snapshot['catalog_reference'],'records':records,
 }

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 result=build(*load_inputs());p=ROOT/'frontier-through804.json'
 if args.write:p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==result,'Through804 artifact differs from replay')
 print(json.dumps({'status':'PASS','labels':12,'profiles':result['remaining_profile_counts'],'baseline_pairs':1319,'frontier_sha256':hashlib.sha256(p.read_bytes()).hexdigest()},sort_keys=True))
if __name__=='__main__':main()
