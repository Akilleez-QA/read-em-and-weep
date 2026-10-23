#!/usr/bin/env python3
"""Three exact source-edge cuts; source125 whole-label gate remains held."""
import argparse,hashlib,json
from copy import deepcopy
import verify_source_frontier_through897 as previous
ROOT=previous.ROOT;require=previous.require;accounting=previous.accounting
PREVIOUS_SHA256='c2f649ab814ab83ef90d29b384f26ead2851fc8748351a0633dc145fe32d9ccf'
PINS_SHA256='bf4db87cf3725ce78ff779c3c6a73460129aa6d2c144431af63895ec80a82800'
RULES=[(905,127,'G3.11.cce6e3ba4eeb',[1,0,1,0,0,2,0,0],32),(906,125,'G3.11.ea6bced3bddf',[0,2,0,0,0,0,0,1],9),(906,125,'G3.11.ea6bced3bddf',[0,1,1,0,0,0,0,1],9)]
COVERAGE={'905':['original_zero_defect_actual_saturated_quotient_not_abstract_split','strict_top_twoD_rows_independent_high_only_D','divisor_bound14_only12_D_absent_Sym6','six_atom_kernel_budget_complete_unique_O6_Wp5_O10','internal_target_D4_Wp5_V6_twoO10','all_four_images_zero_Wp5_scalarO10_both','scalar_multiplicity_line_arbitrary_not_fixed_coordinate','images_saturated_first_spans_degrees8_2_0_minus6','constant_seven_actual_high_capture_Wp3_internal_external_zero','linear_first_span_actual_constantA_high_capture_divisor_bound16','actual_quotient_Tminus1_saturated_in_projected_source','D_tautological_injection_coefficient_kernel_contains_D','T_constant_span_VplusP','Wp3_into_constantA_Homzero_but_linear_channel_retained','Wp3_constant_span_intersection_is_V','actual_derivatives_stay_Tminus1_contradicts_constantV'],
'906':['actual_positive_preimage_chi_forces_constantA','high_A_onto_divisor12_impossible','ranktwo_kernel_W9_Wp9_all_four_scalar_pairs','scalar_8_10_character_compatible_but_A_Sym8_Homzero','actual_constant_projection_K_to_scalarO10_zero','original_scalarO10_retained_all_quotients','actual_R_constants_C0_P_or_VplusP','mandatory_Wp_linear_top_contradiction','twist2_D_multiplicity_one_forces_C0_P','linear_T_top_complete_degree5_kernelD_internalzero','constant_VplusP_projection_negative_only_rank5_degree_minus30_contradiction','bb_actual_split_P2_T3','bc_quartic_nonzero_Serre_dual_coefficient_injection_not_character_guess','bc_quartic_nonzero_actual_split_P2_T3','bc_quartic_zero_preserves_actual_V4_summand','bc_quartic_zero_actual_split_VplusP2_V4','residual_P_kernelV4_internalzero_including_scalar_target12','quadratic_rank4_gap_excludes_increment6','complete_Sym6_kernelT3_first_linear_second_constantC9','quartic_tail_externalzero_internal_topV_retained','coherent_projected_image_connection_preserved_lattice_argument','tail_ranks1_2_Homzero_rank3_degree_contradiction_rank10_in_C9']}
CHANNEL_BOUNDARY={'acff_scalar_multiplicity_line_arbitrary':True,'acff_Wp3_into_Tminus1_allowed':True,'bc_quartic_nonzero_allowed':True,'bc_quartic_zero_allowed':True,'scalar_Ominus10_retained':True,'whole_source_Hom_vanishing_claim':False,'partial_PR901_used':False}
def validate_channels(c):require(c==CHANNEL_BOUNDARY,'Changed-target allowed channels incorrectly discarded')
def validate_coverage(c):require(c==COVERAGE,'Incomplete divisor/kernel/scalar/saturation coverage')
def load_inputs():
 snapshot=previous.build(*previous.load_inputs());catalog=previous.load_inputs()[1]
 raw=(ROOT/'frontier-source-through897.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PREVIOUS_SHA256 and json.loads(raw)==snapshot,'Published899 predecessor changed')
 raw=(ROOT/'source-pins-source-through906.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'Manifest changed');pins=json.loads(raw)
 for p in pins.values():
  b=(ROOT/p['local_file']).read_bytes();require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==p['git_blob_sha1'],'Pinned proof/review changed')
 for pr in [905,906]:
  sha=hashlib.sha256((ROOT/pins[f'{pr}_PROOF']['local_file']).read_bytes()).hexdigest();require(sha in (ROOT/pins[f'{pr}_REVIEW']['local_file']).read_text(),'Proof/review binding mismatch')
 for pr in [905,906]:
  require('db51525015bb7c5e825833d550d08dedf6f6ea96' in (ROOT/pins[f'{pr}_PROOF']['local_file']).read_text(),'Missing original source pin')
 review=(ROOT/pins['906_REVIEW']['local_file']).read_text()
 for pr in [875,882]:require(hashlib.sha256((ROOT/f'inputs/pr{pr}_proof.md').read_bytes()).hexdigest() in review,'Missing exact universal dependency binding')
 require(pins['original_strict_top']['git_blob_sha1']=='d7506dae49b4be43230450c4132bd5db91f137ef','Original strict-top pin mismatch')
 return snapshot,catalog,pins

def intersect(snapshot,catalog,rules=RULES):
 require(rules==RULES,'Only three exact complete source cuts permitted')
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
 require(sum(r['remaining_source_pair_count'] for r in snapshot['records'])==228 and sum(r['remaining_source_pair_count'] for r in rows)==178 and [r['id'] for r in rows if not r['remaining_source_pairs']]==['G3.11.ea6bced3bddf'],'Pair accounting mismatch')
 for item in ledger:item['proof_commit']=pins[f"{item['pr']}_PROOF"]['commit']
 return {'schema_version':1,'checkpoint':'source-through906-after-published899','previous_checkpoint':{'file':'frontier-source-through897.json','sha256':PREVIOUS_SHA256,'publication_pr':899,'publication_commit':'3cde13b41962d494da61131bc84fbf8b82442b9d','necessary_pairs':228},'remaining_label_count':4,'remaining_ids':deepcopy(snapshot['remaining_ids']),'profile_counts':{'11':3,'12':0,'21':1},'new_full_label_exclusions':[],'pair_accounting':{'input_necessary_pairs':228,'additional_removed_pairs':50,'remaining_necessary_pairs':178},'new_source_edge_exclusion_ledger':ledger,'source_branch_coverage':COVERAGE,'source_pins':pins,'source_pins_sha256':PINS_SHA256,'records':rows,'boundary':deepcopy(snapshot['boundary']),'changed_channel_boundary':CHANNEL_BOUNDARY,'whole_label_gate':{'label':'G3.11.ea6bced3bddf','status':'held_pending_separate_original_ten_tuple_exhaustion','additional_pair_cuts_on_future_label_closure':0},'scope_policy':'905 uses original inputs, not partial901.906 retains scalar tail and covers both quartic components. Source cuts only; no realization or formal-proof claim.','deferred':'All later results, every remaining tuple and whole-label gate are outside this checkpoint.'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=build(*load_inputs());p=ROOT/'frontier-source-through906.json'
 if args.write:p.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==r,'Artifact differs from replay');print('PASS through906: 4 registered labels (3/0/1), 178 necessary pairs, 50 additional pair cuts; source125 label gate HELD')
if __name__=='__main__':main()
