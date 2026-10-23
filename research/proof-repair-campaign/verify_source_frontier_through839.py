#!/usr/bin/env python3
"""Source relation checkpoint with explicit whole-label gate held closed."""
import argparse
from copy import deepcopy
import hashlib
import json
import verify_source_frontier_through834 as previous
from verify_source_frontier_through823 import identify, canonical
ROOT=previous.ROOT
require=previous.require
PREVIOUS_SHA256='735b1f248e1acb067fc4f63b57f23be92293140dc607a59e4d7c18af189a9da9'
PINS_SHA256='a978a79405b60c837cc4bc437ebab17dd525d72feb1090c6225d976ddf8de981'
SPLIT='G3.11.863639aa192e';BALANCED='G3.11.73682b4c817f'
SOURCES={
 'bb':{'coefficients':[0,2,0,0,0,0,0,1],'blocks':[[-2,'P'],[-3,'T'],[-3,'T'],[-10,'one']]},
 'bc':{'coefficients':[0,1,1,0,0,0,0,1],'blocks':[[-2,'V'],[-2,'P'],[-3,'T'],[-4,'V'],[-10,'one']]}}
COVERAGE={
 'split_bb':{'dependencies':['pr814_rank_one','pr821','pr836'],'cases':{'zero':'Strict-top injection excludes a zero top image','rank_one':'PR814 RANK-ONE-TOP-EXCLUSION','rank_two_nononto':'PR821 Section5 excludes split torsion','rank_two_onto':'PR836 excludes both constant-span alternatives'}},
 'balanced_bb':{'dependencies':['pr814_rank_one','pr819_cubic','pr836','pr838'],'cases':{'zero':'Strict-top injection excludes a zero top image','rank_one':'PR814 RANK-ONE-TOP-EXCLUSION','rank_two_nononto':'PR819 forces exactly defect12; PR838 excludes that branch','rank_two_onto':'PR836 excludes onto branch only'}},
 'balanced_bc':{'dependencies':['pr814','pr839'],'cases':{'zero':'Strict-top excludes zero, restated PR839 Section1','rank_one':'PR839 excludes with both lower-T channel cases and defective images retained','rank_two':'PR814 Section6 excludes, explicitly imported by PR839'}}}
RULES=[{'label':SPLIT,'source':'bb','coverage':'split_bb'},{'label':BALANCED,'source':'bb','coverage':'balanced_bb'},{'label':BALANCED,'source':'bc','coverage':'balanced_bc'}]
ORIGINAL={'file':'inputs/original-one-one-pairs-db515250.json','git_blob_sha1':'fe0afa410d89340d3082dc814277f89fbb582c19','commit':'db51525015bb7c5e825833d550d08dedf6f6ea96','url':'https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json','source_index':72}

def validate_coverage(coverage,pins):
 for key,c in coverage.items():
  require(set(c['dependencies'])<=set(pins),'Missing coverage dependency')
  expected={'zero','rank_one','rank_two'} if key=='balanced_bc' else {'zero','rank_one','rank_two_nononto','rank_two_onto'}
  require(set(c['cases'])==expected and all(c['cases'].values()),'Incomplete source branch coverage')

def load_inputs():
 s,c,p=previous.load_inputs();snapshot=previous.build(s,c,p)
 raw=(ROOT/'frontier-source-through834.json').read_bytes()
 require(hashlib.sha256(raw).hexdigest()==PREVIOUS_SHA256 and json.loads(raw)==snapshot,'Through834 changed or replay mismatch')
 raw=(ROOT/'source-pins-source-through839.json').read_bytes()
 require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'Source manifest changed')
 pins=json.loads(raw);old=json.loads((ROOT/'source-pins-source-through823.json').read_text())
 for key,file in [('pr814','pr814-proof.md'),('pr819_cubic','pr819-cubic.md'),('pr821','pr821-proof.md')]:pins[key]=old[file]
 for key,pin in pins.items():
  b=(ROOT/pin['local_file']).read_bytes()
  require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==pin['git_blob_sha1'],'Proof blob mismatch: '+key)
 b=(ROOT/ORIGINAL['file']).read_bytes()
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==ORIGINAL['git_blob_sha1'],'Original source catalog mismatch')
 original=json.loads(b)[72]
 require(original['defect']==0 and canonical(original['A'])==canonical([[5,'W'],[-10,'one']]) and canonical(original['B'])==canonical([[-7,'W'],[8,'one']]),'Original balanced tuple target mismatch')
 validate_coverage(COVERAGE,pins)
 return snapshot,c,pins,original

def intersect(snapshot,catalog,rules=RULES):
 ids={k:identify(catalog,s) for k,s in SOURCES.items()}
 rows={r['id']:r for r in snapshot['records']};require(set(rows)==set(snapshot['remaining_ids']) and len(rows)==len(snapshot['records']),'Stable ID mismatch')
 rel={}
 for label,r in rows.items():
  pairs={tuple(p) for p in r['remaining_source_pairs']}
  require(len(pairs)==len(r['remaining_source_pairs'])==r['remaining_source_pair_count'],'Duplicate pair or count mismatch')
  require(r['profile']==label.split('.')[1],'Profile mismatch');rel[label]=pairs
 before=deepcopy(rel);ledger=[];seen=set()
 for rule in rules:
  label=rule['label'];key=(label,canonical(SOURCES[rule['source']]['blocks']))
  require(key not in seen,'Double source exclusion');seen.add(key)
  eid=ids[rule['source']];cut={p for p in rel[label] if p[0]==eid};rel[label]-=cut
  ledger.append(dict(rule,kind='source_edge',source_definition=SOURCES[rule['source']],matched_local_E_id=eid,removed_pairs=sorted(map(list,cut)),actual_additional_pair_count=len(cut),already_absent_in_input=not bool(cut),adjudicated_label_count_delta=0))
 records=[]
 for label in sorted(rows):
  kept=rel[label];cut=before[label]-kept
  require(not kept&cut and kept|cut==before[label],'Pair partition mismatch')
  records.append({'id':label,'profile':rows[label]['profile'],'A':rows[label]['A'],'B':rows[label]['B'],'input_necessary_pair_count':len(before[label]),'removed_pair_count':len(cut),'remaining_source_pair_count':len(kept),'remaining_source_pairs':sorted(map(list,kept)),'removed_source_pairs':sorted(map(list,cut)),'relation_empty':not bool(kept)})
 return records,ledger

def coverage_report(original,catalog,records):
 tuples={tuple(t) for t in original['compatible_E_types']}
 expected={(0,b,c,0,e,f,0,1) for b in range(3) for c in range(3) for e in range(3) for f in range(3) if b+c+e+f==2}
 require(tuples==expected and len(tuples)==10,'Original ten-tuple coverage mismatch')
 catalog_by_tuple={tuple(e['coefficients']):e for e in catalog}
 historical=json.loads((ROOT/'inputs/pr796-same-source-witness-intersection.json').read_text())
 old=next(r for r in historical['records'] if r['id']==BALANCED)
 oldpairs=old['remaining_source_pairs'];current=next(r for r in records if r['id']==BALANCED)['remaining_source_pairs']
 out=[]
 for t in sorted(tuples):
  require(t in catalog_by_tuple,'Original tuple missing in source catalog')
  e=catalog_by_tuple[t];n=sum(x==e['id'] for x,q in oldpairs);m=sum(x==e['id'] for x,q in current)
  out.append({'source_multiplicity_tuple':list(t),'source_blocks':e['blocks'],'historical_pr796_pair_count':n,'current_pair_count':m,'relation_status':'already_absent_from_historical_relation' if n==0 else 'removed_by_pinned_source_checkpoint_chain','mathematical_exhaustion_certified_here':False})
 require(sum(r['historical_pr796_pair_count'] for r in out)==112 and sum(r['current_pair_count'] for r in out)==0,'Balanced tuple partition mismatch')
 require(sum(r['historical_pr796_pair_count']==0 for r in out)==3,'Earlier absent tuple count mismatch')
 return out

def build(snapshot,catalog,pins,original):
 validate_coverage(COVERAGE,pins);records,ledger=intersect(snapshot,catalog)
 require([r['actual_additional_pair_count'] for r in ledger]==[19,16,16],'Source-edge accounting mismatch')
 require(sum(r['remaining_source_pair_count'] for r in records)==759,'Tuple total mismatch')
 empty=sorted(r['id'] for r in records if r['relation_empty']);require(empty==[BALANCED],'Unexpected empty relation')
 registered=deepcopy(snapshot['remaining_ids']);require(len(registered)==9,'Registered label count changed')
 report=coverage_report(original,catalog,records)
 return {'schema_version':1,'checkpoint':'source-strata-through839-label-gated','not_proof_completion':True,'geometric_constraints_fully_encoded':False,
 'scope':'Source-edge checkpoint only. An empty recorded necessary relation is not promoted to a whole-label theorem in this artifact.',
 'previous_checkpoint':{'file':'frontier-source-through834.json','sha256':PREVIOUS_SHA256,'publication_commit':'cf17981333f34548226d87c7146a78167d44ac04','necessary_pairs':810},
 'registered_label_count':9,'registered_ids':registered,'registered_profile_counts':{'11':8,'12':0,'21':1},
 'nonempty_relation_label_count':8,'nonempty_relation_ids':sorted(r['id'] for r in records if not r['relation_empty']),
 'empty_relation_ids':empty,'new_adjudicated_full_label_exclusions':[],
 'whole_label_gate':{'status':'held_closed','original_ten_tuple_catalog_independently_verified':True,'immutable_full_exhaustion_publication_verified':False,'full_exhaustion_publication':None,'reason':'Await a separately published immutable full-exhaustion theorem and check its coverage before any registered label decrement. Earlier absence of three tuples in a numerical necessary relation is not a substitute for that theorem.'},
 'pair_accounting':{'input_necessary_pairs':810,'split_bb_removed':19,'balanced_bb_removed':16,'balanced_bc_removed':16,'additional_removed_pairs':51,'remaining_necessary_pairs':759},
 'new_source_edge_exclusion_ledger':ledger,'source_branch_coverage':COVERAGE,
 'original_balanced_source_catalog':ORIGINAL,'balanced_ten_tuple_relation_coverage':report,
 'split_residual':{'label':SPLIT,'source_names':['bf','bc'],'remaining_necessary_pairs':38,'rank_branch_restrictions_not_promoted_to_source_cuts':True},
 'source_definitions':SOURCES,'source_pins':pins,'new_source_pins_sha256':PINS_SHA256,'catalog_reference':snapshot['catalog_reference'],'matching_rule':snapshot['matching_rule'],
 'proof_boundary':snapshot['proof_boundary'],'records':records}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args()
 result=build(*load_inputs());p=ROOT/'frontier-source-through839.json'
 if a.write:p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==result,'Artifact differs from replay')
 print(json.dumps({'status':'PASS','registered_labels':9,'nonempty_relation_labels':8,'remaining_necessary_pairs':759,'whole_label_gate':'held_closed','sha256':hashlib.sha256(p.read_bytes()).hexdigest()},sort_keys=True))
if __name__=='__main__':main()
