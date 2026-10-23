#!/usr/bin/env python3
"""One exact accf source-edge cut; coherent images and label gates preserved."""
import argparse,hashlib,json
from copy import deepcopy
import verify_source_frontier_through906 as previous
ROOT=previous.ROOT;require=previous.require;accounting=previous.accounting
PREVIOUS_SHA256='3c73a17a05a4d83ff98b802759f8f54228ec50ebe5adb338dab97d3ca06665d8'
PINS_SHA256='e825a08cc425cbff7c6fa09ca58cd5364820eb50d8b0f73e37a5698017238b56'
RULES=[(907,127,'G3.11.cce6e3ba4eeb',[1,0,2,0,0,1,0,0],32)]
COVERAGE={'901':['original_zero_defect_actual_quotient','Wp_cubic_high_exact_f12_factor_degree7_onto_kernelO10','kernel_internal_V_and_scalar_channels_all_combinations','raw_first_span_images_not_saturated_external_lemma','zero_internal_CV_coherent_projection_same_f12_lattice','universal_V_to_P_and_D_saturated_injections','V_only_internal_branch_actual_high_capture_ranktwo_degree_minus6_contradiction','nonzero_scalar_negative_row_retained_optional_V','D_only_span_degree14_scalar_Homzero_contradiction','accf_only_full_VplusD_span_Pminus2_actual_image_f12O6'],
'907':['topV_high_exact_f12_factor_degree6_onto','kernel_Wpminus5_universal_saturated_injection','internal_target_D4_Wp5_twoV6_O10_only_original_Wp_row','internal_zero_raw_constantP_actual_image_f12O6','internal_nonzero_raw_Tminus1_saturation_defect_atmost6','exact_intersection_preimage_Bplus_originalR_not_unrelated_isomorphic_copy','nonzero_internal_span_PplusD_cannot_contain_full_VplusD','constantP_disjoint_from_actual_VplusD_span','sum_Pconstant_plus_Pminus2_rank8_degree_minus8','both_onto_same_coherent_f12O6_in_L_at_divisor_not_generic_equality','invariant_degree12_space_dimension_one_no_division_or_saturation','intersection_kernel_rank7_degree_minus14','all_degrees_atmost_minus2_force_pure_top','multiplicityfree_VplusD_subrepresentation_dimensions_0_3_5_8_not7']}
CHANNEL_BOUNDARY={'raw_high_image_degree_before_twist':4,'raw_high_image_degree_after_twist':6,'saturated_high_line_degree_after_twist':18,'f12_divisor_degree_retained':12,'replace_coherent_image_by_saturation':False,'optional_cubic_internal_V_row_allowed':True,'topV_internal_Wp_row_nonzero_considered':True,'original_R_intersection_identified':True,'PR901_alone_whole_source_cut':False}
def validate_channels(c):require(c==CHANNEL_BOUNDARY,'Changed-target allowed channels incorrectly discarded')
def validate_coverage(c):require(c==COVERAGE,'Incomplete divisor/kernel/scalar/saturation coverage')
def load_inputs():
 snapshot=previous.build(*previous.load_inputs());catalog=previous.load_inputs()[1]
 raw=(ROOT/'frontier-source-through906.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PREVIOUS_SHA256 and json.loads(raw)==snapshot,'Through906 predecessor changed')
 raw=(ROOT/'source-pins-source-through907.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'Manifest changed');pins=json.loads(raw)
 for p in pins.values():
  b=(ROOT/p['local_file']).read_bytes();require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==p['git_blob_sha1'],'Pinned proof/review changed')
 for pr in [901,907]:
  sha=hashlib.sha256((ROOT/pins[f'{pr}_PROOF']['local_file']).read_bytes()).hexdigest();require(sha in (ROOT/pins[f'{pr}_REVIEW']['local_file']).read_text(),'Proof/review binding mismatch')
 for pr in [901,907]:
  require('db51525015bb7c5e825833d550d08dedf6f6ea96' in (ROOT/pins[f'{pr}_PROOF']['local_file']).read_text(),'Missing original source pin')
 proof=(ROOT/pins['907_PROOF']['local_file']).read_text();review=(ROOT/pins['907_REVIEW']['local_file']).read_text()
 dep=pins['901_PROOF'];require(dep['commit'] in proof and dep['commit'] in review and dep['git_blob_sha1']=='8734e450297032410ac5625efeddd3cea34fd654' and dep['git_blob_sha1'] in proof and dep['git_blob_sha1'] in review,'Missing exact901 prerequisite')
 return snapshot,catalog,pins

def intersect(snapshot,catalog,rules=RULES):
 require(rules==RULES,'Only one exact complete source cuts permitted')
 rows=deepcopy(snapshot['records']);require(len(rows)==len(set(snapshot['remaining_ids']))==4 and {r['id'] for r in rows}==set(snapshot['remaining_ids']),'Stable IDs mismatch')
 originals=json.loads((ROOT/'inputs/original-one-one-pairs-db515250.json').read_text());frontier=json.loads((ROOT/'inputs/pr842-original_frontier.json').read_text())['cases'];ledger=[];seen=set()
 for pr,index,label,t,expected in rules:
  source=originals[index];matches=[r for r in frontier if r['id']==label];row=next(r for r in rows if r['id']==label)
  require(len(matches)==1 and matches[0]['source_index']==index and matches[0]['original_defect']==source['defect']==0 and t in source['compatible_E_types'],'Original source scope mismatch')
  for key in ['A','B']:require(accounting.canonical(source[key])==accounting.canonical(matches[0][key])==accounting.canonical(row[key]),'Exact original endpoint mismatch')
  definition={'coefficients':t,'blocks':accounting.decode(t)};e=accounting.identify(catalog,definition);require((label,e) not in seen,'Double cut');seen.add((label,e))
  before={tuple(p) for p in row['remaining_source_pairs']};require(len(before)==len(row['remaining_source_pairs'])==row['remaining_source_pair_count'],'Duplicate pairs or count mismatch')
  cut={p for p in before if p[0]==e};kept=before-cut;require(len(cut)==expected and cut.isdisjoint(kept) and cut|kept==before,'Exact cut mismatch')
  row.update(remaining_source_pairs=sorted(map(list,kept)),remaining_source_pair_count=len(kept))
  ledger.append({'kind':'source_edge','pr':pr,'original_source_index':index,'label':label,'source_definition':definition,'matched_local_E_id':e,'removed_pairs':sorted(map(list,cut)),'actual_additional_pair_count':len(cut),'adjudicated_label_count_delta':0})
 for row in rows:
  old=next(r for r in snapshot['records'] if r['id']==row['id']);a={tuple(p) for p in old['remaining_source_pairs']};b={tuple(p) for p in row['remaining_source_pairs']};row.update(input_necessary_pair_count=len(a),removed_pair_count=len(a-b),removed_source_pairs=sorted(map(list,a-b)),relation_empty=not b)
 return rows,ledger

def build(snapshot,catalog,pins):
 validate_coverage(COVERAGE);validate_channels(CHANNEL_BOUNDARY);rows,ledger=intersect(snapshot,catalog)
 require(sum(r['remaining_source_pair_count'] for r in snapshot['records'])==178 and sum(r['remaining_source_pair_count'] for r in rows)==146 and [r['id'] for r in rows if not r['remaining_source_pairs']]==['G3.11.ea6bced3bddf'],'Pair accounting mismatch')
 for item in ledger:item['proof_commit']=pins[f"{item['pr']}_PROOF"]['commit']
 return {'schema_version':1,'checkpoint':'source-through907-after-published910','previous_checkpoint':{'file':'frontier-source-through906.json','sha256':PREVIOUS_SHA256,'publication_pr':910,'publication_commit':'988037951c759459fbed3e87c1bed4210125450d','publication_tree':'e88028eb247b6089f8bb65b499e8c7996b5aeb54','necessary_pairs':178},'remaining_label_count':4,'remaining_ids':deepcopy(snapshot['remaining_ids']),'profile_counts':{'11':3,'12':0,'21':1},'new_full_label_exclusions':[],'pair_accounting':{'input_necessary_pairs':178,'additional_removed_pairs':32,'remaining_necessary_pairs':146},'new_source_edge_exclusion_ledger':ledger,'source_branch_coverage':COVERAGE,'source_pins':pins,'source_pins_sha256':PINS_SHA256,'records':rows,'boundary':deepcopy(snapshot['boundary']),'changed_channel_boundary':CHANNEL_BOUNDARY,'whole_label_gate':{'label':'G3.11.ea6bced3bddf','status':'held_pending_separate_original_ten_tuple_exhaustion','additional_pair_cuts_on_future_label_closure':0},'scope_policy':'907 combines exact901 accf reduction with both topV internal branches and the identical coherent f12 image.901 alone makes no source cut. Source cuts only; no realization or formal-proof claim.','deferred':'All later results, every remaining tuple and whole-label gate are outside this checkpoint.'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=build(*load_inputs());p=ROOT/'frontier-source-through907.json'
 if args.write:p.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==r,'Artifact differs from replay');print('PASS through907: 4 registered labels (3/0/1), 146 necessary pairs, 32 additional pair cuts; source125 label gate HELD')
if __name__=='__main__':main()
