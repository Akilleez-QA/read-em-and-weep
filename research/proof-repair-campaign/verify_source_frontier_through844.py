#!/usr/bin/env python3
"""Source-edge-only integration; split whole-label gate deliberately closed."""
import argparse, hashlib, json
from copy import deepcopy
import verify_frontier_through842 as previous
ROOT=previous.ROOT
require=previous.require
canonical=previous.previous.canonical
identify=previous.previous.identify
SPLIT='G3.11.863639aa192e'
PREVIOUS_SHA256='5d7a507067f54d1372ccee7aa4eee870878a33b74a2b277980d3c04270071f44'
PINS_SHA256='6a668f243b4a26c21a4c0c02422a74730440ca4b936eed42be0f1780553db241'
SOURCES={'bf':{'coefficients':[0,1,0,0,0,1,0,1],'blocks':[[-2,'P'],[-2,'D'],[-3,'T'],[-8,'one'],[-10,'one']]},'bc':{'coefficients':[0,1,1,0,0,0,0,1],'blocks':[[-2,'V'],[-2,'P'],[-3,'T'],[-4,'V'],[-10,'one']]}}
COVERAGE={
'bf':{'rank_zero':'strict-top','rank_two_defect':'nine sections force delta<=7, hence delta0','rank_two_internal_zero':'PR814 Section5','rank_two_internal_nonzero':'PR830 Sections1-4; all nonzero combinations','rank_one':'PR844 BF interface Sections1-4 plus BF corollary actual-connection transfer and split descent','complementary_channels':'T quintic / V sextic / Wp septic; all-zero case contradicted'},
'bc':{'rank_zero':'strict-top','rank_two':'PR814 Section6','rank_one_top':'complete direct O(4) sextic','lower_T_zero':'BC Section2 full split quotient','lower_T_nonzero_both_top_rows':'BC Section4 full split quotient','lower_T_nonzero_only_O2':'BC Section4.1 P nonzero or scalar zero/nonzero f12, raw defect retained','lower_T_nonzero_only_O4':'BC Section4.2 sextic rows nonzero or both zero; Ext degree minus1 retained','transfer':'BC Section5 exact actual-connection interface'},
'descent':{'initial_rank_one':'Section2.1 excluded','initial_rank_two_defect':'Section2.2 delta12 excluded, not saturated away','K3_types':'all four I/II/III/IV retained','K4_types':'all four a/b/c/d retained, including split-specific d','terminal_b':'Section6 raw O(-8)+O(-18); next target O(-10)+O(-20)','terminal_d':'Section7 scalar zero/nonzero f12 both excluded','geometry':'same saturated actual kernels and constant connection; raw quotient factorization; derivative rank at most2'}}
def validate_coverage(c):require(c==COVERAGE,'Incomplete source branch coverage')
def load_inputs():
 s,c,o,p,t=previous.load_inputs();snapshot=previous.build(s,c,o,p,t)
 raw=(ROOT/'frontier-through842.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PREVIOUS_SHA256 and json.loads(raw)==snapshot,'Through842 changed')
 raw=(ROOT/'source-pins-source-through844.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'Manifest changed');pins=json.loads(raw)
 for k,pin in pins.items():
  b=(ROOT/pin['local_file']).read_bytes();require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==pin['git_blob_sha1'],'Proof blob mismatch: '+k)
 review=(ROOT/pins['SPLIT-DESCENT-BUNDLE-REVIEW.md']['local_file']).read_text()
 for name in ['SPLIT-BACKWARD-DESCENT.md','SPLIT-BC-SOURCE-EXCLUSION.md','SPLIT-BF-SOURCE-COROLLARY.md','SPLIT-BF-BACKWARD-INTERFACE.md','SPLIT-BF-INTERFACE-REVIEW.md']:
  require(hashlib.sha256((ROOT/pins[name]['local_file']).read_bytes()).hexdigest() in review,'Review does not bind companion: '+name)
 require(hashlib.sha256((ROOT/'inputs/pr830-proof.md').read_bytes()).hexdigest()=='d762e23c6b402bf8bfd62160e310ecacf601a910d47f6a3e278cd8a3806657f6','PR830 mismatch')
 original=json.loads((ROOT/'inputs/original-one-one-pairs-db515250.json').read_text())[69]
 frontier=json.loads((ROOT/'inputs/pr842-original_frontier.json').read_text());matches=[r for r in frontier['cases'] if r['id']==SPLIT]
 require(len(matches)==1 and matches[0]['source_index']==69 and matches[0]['original_defect']==original['defect']==0,'Original split identity mismatch')
 row=next(r for r in snapshot['records'] if r['id']==SPLIT)
 for key in ['A','B']:require(canonical(row[key])==canonical(original[key])==canonical(matches[0][key]),'Original split quotient mismatch')
 for source in SOURCES.values():require(source['coefficients'] in original['compatible_E_types'] and canonical(previous.decode(source['coefficients']))==canonical(source['blocks']),'Original source tuple/block mismatch')
 return snapshot,c,pins

def intersect(snapshot,catalog,rules=('bf','bc')):
 require(len(rules)==len(set(rules)),'Double source exclusion')
 records=deepcopy(snapshot['records']);ids=[r['id'] for r in records]
 require(len(set(ids))==len(ids)==8 and set(ids)==set(snapshot['remaining_ids']),'Stable ID mismatch')
 target=next(r for r in records if r['id']==SPLIT)
 pairs={tuple(p) for p in target['remaining_source_pairs']};require(len(pairs)==target['remaining_source_pair_count']==len(target['remaining_source_pairs']),'Duplicate pair or count mismatch')
 before=set(pairs);ledger=[]
 for name in rules:
  eid=identify(catalog,SOURCES[name]);cut={p for p in pairs if p[0]==eid};pairs-=cut
  ledger.append({'kind':'source_edge','label':SPLIT,'source':name,'source_definition':SOURCES[name],'matched_local_E_id':eid,'removed_pairs':sorted(map(list,cut)),'actual_additional_pair_count':len(cut),'adjudicated_label_count_delta':0})
 target.update(input_necessary_pair_count=len(before),removed_pair_count=len(before-pairs),remaining_source_pair_count=len(pairs),remaining_source_pairs=sorted(map(list,pairs)),removed_source_pairs=sorted(map(list,before-pairs)),relation_empty=not pairs)
 require(before==pairs|{tuple(p) for r in ledger for p in r['removed_pairs']},'Pair partition mismatch')
 return records,ledger

def build(snapshot,catalog,pins):
 validate_coverage(COVERAGE);records,ledger=intersect(snapshot,catalog)
 require([r['actual_additional_pair_count'] for r in ledger]==[19,19],'Expected exact additional cuts')
 require(sum(r['remaining_source_pair_count'] for r in records)==721,'Pair count mismatch')
 empty=sorted(r['id'] for r in records if not r['remaining_source_pairs']);require(empty==[SPLIT],'Unexpected empty relation')
 return {'schema_version':1,'checkpoint':'source-strata-through844-label-gated','previous_checkpoint':{'file':'frontier-through842.json','sha256':PREVIOUS_SHA256,'publication_pr':843,'publication_commit':'b23fdc1a66fde80d1bbf74f4fdee7ddefb7af772','necessary_pairs':759},'registered_label_count':8,'registered_ids':deepcopy(snapshot['remaining_ids']),'registered_profile_counts':{'11':7,'12':0,'21':1},'nonempty_relation_label_count':7,'nonempty_relation_ids':sorted(r['id'] for r in records if r['remaining_source_pairs']),'empty_relation_ids':empty,'new_adjudicated_full_label_exclusions':[],'whole_label_gate':{'label':SPLIT,'status':'held_closed','immutable_full_exhaustion_publication_verified':False,'full_exhaustion_publication':None,'reason':'Await immutable complete original ten-source exhaustion and independently check its full coverage before any registered-label decrement.'},'pair_accounting':{'input_necessary_pairs':759,'bf_removed':19,'bc_removed':19,'additional_removed_pairs':38,'remaining_necessary_pairs':721},'new_source_edge_exclusion_ledger':ledger,'source_branch_coverage':COVERAGE,'source_pins':pins,'source_pins_sha256':PINS_SHA256,'records':records,'deferred':[{'pr':845,'kind':'necessary_forms_not_exclusion','action':'No source edge or label deletion; length20 modification forms remain necessary conditions only.'}],'boundary':snapshot['boundary'],'scope':'Finite accounting conditional on immutable written source theorems; neither an entire split-label exclusion nor a realization claim.'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();result=build(*load_inputs());p=ROOT/'frontier-source-through844.json'
 if a.write:p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==result,'Artifact differs from replay')
 print(json.dumps({'status':'PASS','registered_labels':8,'nonempty_relation_labels':7,'necessary_pairs':721,'new_pair_cuts':38,'whole_label_gate':'held_closed','sha256':hashlib.sha256(p.read_bytes()).hexdigest()},sort_keys=True))
if __name__=='__main__':main()
