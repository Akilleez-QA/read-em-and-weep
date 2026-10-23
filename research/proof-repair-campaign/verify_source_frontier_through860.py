#!/usr/bin/env python3
"""One complete source cut, preserving all five registered labels."""
import argparse, hashlib, json
from copy import deepcopy
import verify_source_frontier_through854 as previous
ROOT=previous.ROOT
require=previous.require
accounting=previous.accounting
LABEL='G3.11.ea6bced3bddf'
TUPLE=[0,0,0,0,1,1,0,1]
PREVIOUS_SHA256='c56375860d238bab5d171f4798025e09f4943406b899dc2aed7c78fef05945d4'
PINS_SHA256='f8fb4df0f81ccccfe1225186d5d1f7f5a8acd5a82763b3b899b291d419c490fc'
COVERAGE={'high_subsystem':['lower_P_row_kernel_including_entire_row_zero','saturated_P_plus_D_subblock','nine_sections_exclude_any_positive_divisor','all_three_exact_kernels'],
'internal_images':['zero','P_Ominus4_scalar_saturated','Wp_Ominus5_tautological_saturated','Ominus10_all_covariant_scalar_graph_combinations_saturated'],
'nonzero_images':['first_polars_actual_constant_and_linear_parts','D_to_T_nonzero_constant_A_rank_obstruction','D_to_T_nonzero_AplusV_O8_factors_through_saturated_O16','P_projection_nonzero_A_channel_zero_rankV_too_small','T_only_full_linear_summand','WpplusT_a_zero','WpplusT_b_zero','WpplusT_a_b_nonzero_Euler_kernel_degree7_onto','full_linear_summand_actual_connection_contradiction'],
'zero_image':['actual_constant_ten_space','exact_intersection_and_saturated_constant_projection','residual_P_to_O4_basepoint_free','exact_V_Ominus4_kernel_internal_zero','quadratic_rank4_gap_b6_neither8_nor_at_most3']}
def validate_coverage(c):require(c==COVERAGE,'Incomplete whole-source internal-image coverage')
def load_inputs():
 s,c,p=previous.load_inputs();snapshot=previous.build(s,c,p)
 raw=(ROOT/'frontier-source-through854.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PREVIOUS_SHA256 and json.loads(raw)==snapshot,'Published857 predecessor changed')
 raw=(ROOT/'source-pins-source-through860.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'Manifest changed');pins=json.loads(raw)
 for pin in pins.values():
  b=(ROOT/pin['local_file']).read_bytes();require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==pin['git_blob_sha1'],'Pinned proof changed')
 b=(ROOT/pins['proof']['local_file']).read_bytes();sha=hashlib.sha256(b).hexdigest();require(sha=='f73132ccbdaf1e4db28197a6ea1a180a0216a46295c105f16623aed08e9e3bff' and sha in (ROOT/pins['review']['local_file']).read_text(),'Review binding mismatch')
 original=json.loads((ROOT/'inputs/original-one-one-pairs-db515250.json').read_text())[125];frontier=json.loads((ROOT/'inputs/pr842-original_frontier.json').read_text())['cases'];matches=[r for r in frontier if r['id']==LABEL]
 require(len(matches)==1 and matches[0]['source_index']==125 and matches[0]['original_defect']==original['defect']==0 and TUPLE in original['compatible_E_types'],'Original source identity mismatch')
 row=next(r for r in snapshot['records'] if r['id']==LABEL)
 for key in ['A','B']:require(accounting.canonical(row[key])==accounting.canonical(original[key])==accounting.canonical(matches[0][key]),'Original A/B mismatch')
 return snapshot,c,pins

def intersect(snapshot,catalog,rules=(LABEL,)):
 require(tuple(rules)==(LABEL,),'Only one exact label/source edge allowed; duplicate or widened cut')
 records=deepcopy(snapshot['records']);ids=[r['id'] for r in records];require(len(ids)==len(set(ids))==5 and set(ids)==set(snapshot['remaining_ids']),'Stable IDs mismatch')
 definition={'coefficients':TUPLE,'blocks':accounting.decode(TUPLE)};eid=accounting.identify(catalog,definition)
 target=next(r for r in records if r['id']==LABEL);before={tuple(p) for p in target['remaining_source_pairs']};require(len(before)==len(target['remaining_source_pairs'])==target['remaining_source_pair_count'],'Duplicate pair/count mismatch')
 cut={p for p in before if p[0]==eid};kept=before-cut;require(kept|cut==before and not kept&cut,'Pair partition mismatch')
 target.update(input_necessary_pair_count=len(before),removed_pair_count=len(cut),remaining_source_pair_count=len(kept),remaining_source_pairs=sorted(map(list,kept)),removed_source_pairs=sorted(map(list,cut)),relation_empty=not kept)
 ledger=[{'kind':'source_edge','label':LABEL,'original_source_index':125,'source_name':'ef','source_definition':definition,'proof_commit':'cdf1d9ae5e477ef5f541d92888059ceedb4fd9b4','matched_local_E_id':eid,'removed_pairs':sorted(map(list,cut)),'actual_additional_pair_count':len(cut),'already_absent':not bool(cut),'adjudicated_label_count_delta':0}]
 return records,ledger

def build(snapshot,catalog,pins):
 validate_coverage(COVERAGE);records,ledger=intersect(snapshot,catalog)
 require(ledger[0]['actual_additional_pair_count']==9,'Exact source cut mismatch');require(sum(r['remaining_source_pair_count'] for r in records)==501 and all(r['remaining_source_pairs'] for r in records),'Remaining relation mismatch')
 return {'schema_version':1,'checkpoint':'source-through860-after-published857','previous_checkpoint':{'file':'frontier-source-through854.json','sha256':PREVIOUS_SHA256,'publication_pr':857,'publication_commit':'17c102303f6fa130b68eb91e8e17c0208d486b09','necessary_pairs':510},'remaining_label_count':5,'remaining_ids':deepcopy(snapshot['remaining_ids']),'profile_counts':{'11':4,'12':0,'21':1},'new_full_label_exclusions':[],'pair_accounting':{'input_necessary_pairs':510,'additional_removed_pairs':9,'remaining_necessary_pairs':501},'new_source_edge_exclusion_ledger':ledger,'source_branch_coverage':COVERAGE,'source_pins':pins,'source_pins_sha256':PINS_SHA256,'records':records,'deferred':deepcopy(snapshot['deferred'])+[{'pr':858,'commit':'d3b3134e23d0aa4c4b58fd1457f040856d2d0655','kind':'abstract_residual_templates_not_HM_realization','action':'No deletion or realization inference.'},{'pr':859,'commit':'6129e92a26572779003f3295227f688b77ed881c','kind':'conditional_degree12_highP_branch_restrictions','action':'Not promoted to a whole-source cut.'}],'boundary':deepcopy(snapshot['boundary'])}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();result=build(*load_inputs());p=ROOT/'frontier-source-through860.json'
 if a.write:p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==result,'Artifact differs from replay')
 print(json.dumps({'status':'PASS','labels':5,'necessary_pairs':501,'new_pair_cuts':9,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()},sort_keys=True))
if __name__=='__main__':main()
