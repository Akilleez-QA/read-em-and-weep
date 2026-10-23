#!/usr/bin/env python3
"""One whole-label gate discharge; no repeated source-pair cuts."""
import argparse, hashlib, json, re
from copy import deepcopy
import verify_source_frontier_through844 as previous
ROOT=previous.ROOT
require=previous.require
SPLIT=previous.SPLIT
COMMIT='6529c3d4e513bb1958ba57b20262e06d35000f77'
PREVIOUS_SHA256='914da79fc3b871448477fd9283643b8e1bc30ae9b45c5cbf5c31c3d75125c5ee'
PINS_SHA256='ecbe2e5004bcebd42a2d8ceeaff25d8ff2fc1619bc7f26bd536119b86ad0b4b9'
BRANCHES={'ff':['strict_top_D_multiplicity'],'ee':['strict_top_P_multiplicity'],'cc':['strict_top_V_multiplicity'],
'ef':['zero_top_impossible','two_P_rows_force_onto','pr814_zero_internal_polar'],
'be':['zero_top_impossible','two_P_rows_force_onto','pr814_zero_internal_polar'],
'ce':['zero_top_impossible','two_P_rows_force_onto','pr814_actual_constant_D','pr826_degree22_determinant_no_invariant'],
'cf':['zero_top_impossible','V_and_D_rows_force_onto','pr814_actual_constant_P','pr828_horizontal_projected_lattice'],
'bf':list(previous.COVERAGE['bf'].keys())+['actual_connection_transfer','split_descent_all_four_types_and_both_terminal_defects'],
'bc':list(previous.COVERAGE['bc'].keys())+['split_descent_all_four_types_and_both_terminal_defects'],
'bb':['zero_top_impossible','rank_one_O4_pr814','rank_one_O6_pr814','rank_two_delta_only0_or12','delta12_Wp_minus1_has_zero_O4_row_pr821','onto_nine_dimensional_span_pr836','onto_twelve_dimensional_P_conic_pr836']}
def validate_branches(c):require(c==BRANCHES,'Incomplete original-source branch coverage')
def load_inputs():
 s,c,p=previous.load_inputs();snapshot=previous.build(s,c,p)
 raw=(ROOT/'frontier-source-through844.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PREVIOUS_SHA256 and json.loads(raw)==snapshot,'Through844 changed')
 raw=(ROOT/'source-pins-through847.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'Manifest changed');pins=json.loads(raw)
 for key,pin in pins.items():
  b=(ROOT/pin['local_file']).read_bytes();require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==pin['git_blob_sha1'],'Pinned proof/review changed')
 proof=(ROOT/pins['proof']['local_file']).read_text();review=(ROOT/pins['review']['local_file']).read_text();sha=hashlib.sha256(proof.encode()).hexdigest()
 require(sha=='8a36d8f64036a690648fd7cc14d8c5ea73406ecf2d106bea4db7638c80b21d9e' and sha in review,'Review does not bind proof')
 original=json.loads((ROOT/'inputs/original-one-one-pairs-db515250.json').read_text())[69]
 return snapshot,c,original,pins,proof

def exhaustion(original,catalog,proof,branches=BRANCHES):
 validate_branches(branches)
 parsed=[(n,[int(v) for v in t.split(',')]) for n,t in re.findall(r'^\d+\. (\w+) = \(([0-9,]+)\)',proof,re.M)]
 require(len(parsed)==10 and [t for n,t in parsed]==original['compatible_E_types'],'Exact ordered original ten tuples mismatch')
 require(len({tuple(t) for n,t in parsed})==10 and {n for n,t in parsed}==set(BRANCHES),'Duplicate tuple/source')
 out=[]
 for n,t in parsed:
  blocks=previous.previous.decode(t);eid=previous.identify(catalog,{'coefficients':t,'blocks':blocks});dims=previous.previous.DIMS
  require(sum(dims[r] for d,r in blocks)==17 and sum(d*dims[r] for d,r in blocks)==-54,'Universal source arithmetic mismatch')
  out.append({'source_name':n,'multiplicity_tuple':t,'source_blocks':blocks,'matched_local_E_id':eid,'branch_coverage':branches[n],'new_pair_cuts':0})
 return out

def build(snapshot,catalog,original,pins,proof):
 coverage=exhaustion(original,catalog,proof)
 require(snapshot['whole_label_gate']['status']=='held_closed' and snapshot['whole_label_gate']['label']==SPLIT,'Wrong predecessor gate')
 ids=snapshot['registered_ids'];require(len(ids)==len(set(ids))==8 and SPLIT in ids,'Duplicate/missing label')
 records=snapshot['records'];require(len(records)==8 and {r['id'] for r in records}==set(ids),'Stable record mismatch')
 removed=next(r for r in records if r['id']==SPLIT);require(removed['remaining_source_pairs']==[] and removed['remaining_source_pair_count']==0,'Label operation must not repeat source cuts')
 kept=deepcopy([r for r in records if r['id']!=SPLIT]);counts={p:sum(r['profile']==p for r in kept) for p in ['11','12','21']}
 require(counts=={'11':6,'12':0,'21':1} and sum(r['remaining_source_pair_count'] for r in kept)==721,'Accounting mismatch')
 return {'schema_version':1,'checkpoint':'whole-label-through847','previous_checkpoint':{'file':'frontier-source-through844.json','sha256':PREVIOUS_SHA256,'registered_labels':8,'necessary_pairs':721,'gate':'held_closed'},'remaining_label_count':7,'remaining_ids':sorted(set(ids)-{SPLIT}),'profile_counts':counts,'new_full_label_exclusion_ledger':[{'id':SPLIT,'kind':'whole_label','proof_commit':COMMIT,'original_source_index':69,'original_defect':0,'complete_original_tuple_count':10,'actual_additional_pair_count':0}],'new_source_edge_exclusions':[],'pair_accounting':{'input_necessary_pairs':721,'additional_removed_pairs':0,'remaining_necessary_pairs':721},'whole_label_gate':{'status':'discharged_by_pinned_written_exhaustion','original_ten_tuple_catalog_independently_verified':True,'immutable_full_exhaustion_publication_verified':True,'publication_commit':COMMIT},'original_ten_tuple_exhaustion':coverage,'split_descent_branch_coverage':deepcopy(previous.COVERAGE),'source_pins':pins,'source_pins_sha256':PINS_SHA256,'records':kept,'deferred':deepcopy(snapshot['deferred'])+[{'pr':846,'commit':'1644b5221fe6f8c23f30401fd6f2dc64230c0f5f','kind':'source_exclusions_not_integrated','action':'Deferred to a separate bounded source checkpoint; no O16 edges deleted here.'}],'boundary':deepcopy(snapshot['boundary'])}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();result=build(*load_inputs());p=ROOT/'frontier-through847.json'
 if a.write:p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==result,'Artifact differs from replay')
 print(json.dumps({'status':'PASS','labels':7,'profiles':result['profile_counts'],'necessary_pairs':721,'additional_pair_cuts':0,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()},sort_keys=True))
if __name__=='__main__':main()
