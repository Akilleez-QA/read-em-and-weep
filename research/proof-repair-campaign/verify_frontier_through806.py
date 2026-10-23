#!/usr/bin/env python3
"""Append PR806 cuts to the immutable through804 checkpoint, without rescanning."""
import argparse
from copy import deepcopy
import hashlib
import json
import verify_frontier_through804 as prior

ROOT=prior.ROOT
require=prior.require
PRIOR_SHA256='2a927b6606ec43d2b6f39a5992e4f8bc38829f09cd03842d6afcf29c60e83bca'
PINS_SHA256='50157b0d9992d3db00cec3d33a67a41c56800fd55cbb3bd2416973f76d5e103a'
PROOF_SHA256='a377136f70014ca0d7913e3a652e5bf8bd1a06a316a622fdf9911f434ce1bf0e'
CUTS=[{'source':'pr806','kind':'full_label','ids':['G3.11.1e318198128e','G3.11.6795493ae8cd','G3.11.a5d4e292b34e']}]

def load_inputs():
 snapshot=prior.build(*prior.load_inputs())
 raw=(ROOT/'frontier-through804.json').read_bytes()
 require(hashlib.sha256(raw).hexdigest()==PRIOR_SHA256,'Through804 checkpoint changed')
 require(json.loads(raw)==snapshot,'Through804 replay mismatch')
 raw=(ROOT/'source-pins-through806.json').read_bytes()
 require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'PR806 source pin changed')
 pins=json.loads(raw);require(set(pins)=={'pr806'},'Unexpected proof set');pin=pins['pr806']
 proof=(ROOT/pin['local_file']).read_bytes()
 require(hashlib.sha256(proof).hexdigest()==PROOF_SHA256,'PR806 proof hash mismatch')
 require(hashlib.sha1(b'blob '+str(len(proof)).encode()+b'\0'+proof).hexdigest()==pin['git_blob_sha1'],'PR806 Git blob mismatch')
 return snapshot,pins

def build(snapshot,pins):
 require(snapshot['remaining_label_count']==12 and snapshot['remaining_profile_counts']=={'11':11,'12':0,'21':1},'Wrong checkpoint profile')
 ids,ledger,records=prior.restrict(snapshot,CUTS)
 all_cuts=[{k:c[k] for k in ('source','kind','ids')} for c in snapshot['cumulative_full_label_exclusion_ledger']]+CUTS
 original=snapshot['remaining_ids']+[i for c in snapshot['cumulative_full_label_exclusion_ledger'] for i in c['ids']]
 cumulative_ids,cumulative=prior.historical.apply_label_cuts(original,all_cuts)
 require(cumulative_ids==ids,'Cumulative ledger mismatch')
 require(len(ids)==9 and prior.historical.counts(ids)=={'11':8,'12':0,'21':1},'Current profile mismatch')
 tuples=sum(r['baseline_pair_count'] for r in records)
 require(tuples==1004 and ledger[0]['removed_baseline_pairs']==315,'Tuple restriction mismatch')
 require(tuples+315==snapshot['pair_accounting']['current12_baseline_relation']==1319,'Tuple partition mismatch')
 return {
  'schema_version':1,'snapshot':'through806','scope':'Append-only extension through the three full-label exclusions of pinned PR806; no newer publications are included.',
  'not_proof_completion':True,'geometric_constraints_fully_encoded':False,
  'historical_snapshot':deepcopy(snapshot['historical_snapshot']),
  'previous_checkpoint':{'file':'frontier-through804.json','sha256':PRIOR_SHA256,'labels':12,'baseline_pairs':1319},
  'remaining_label_count':9,'remaining_ids':ids,'remaining_profile_counts':prior.historical.counts(ids),
  'new_full_label_exclusion_ledger':ledger,'cumulative_full_label_exclusion_ledger':cumulative,
  'historical_source_edge_exclusion_ledger':deepcopy(snapshot['historical_source_edge_exclusion_ledger']),
  'inherited_exclusions_not_recounted':snapshot['inherited_exclusions_not_recounted'],
  'pair_accounting':{'historical17_baseline_relation':1790,'through804_baseline_relation':1319,'new_removed_baseline_pairs':315,'current9_baseline_relation':1004,'pr796_baseline_relation':1996,'total_post_pr796_full_label_pairs_removed':992},
  'pair_boundary':snapshot['pair_boundary'].replace('twelve','nine'),
  'proof_boundary':snapshot['proof_boundary'],
  'source_pins':dict(snapshot['source_pins'],**pins),'new_proof_sha256':{'pr806':PROOF_SHA256},'new_source_pins_sha256':PINS_SHA256,
  'catalog_reference':snapshot['catalog_reference'],'records':records,
 }

def main():
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args()
 result=build(*load_inputs());p=ROOT/'frontier-through806.json'
 if args.write:p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==result,'Through806 artifact differs from replay')
 print(json.dumps({'status':'PASS','labels':9,'profiles':result['remaining_profile_counts'],'baseline_pairs':1004,'frontier_sha256':hashlib.sha256(p.read_bytes()).hexdigest()},sort_keys=True))
if __name__=='__main__':main()
