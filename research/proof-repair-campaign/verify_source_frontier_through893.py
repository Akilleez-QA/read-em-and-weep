#!/usr/bin/env python3
"""Two whole-source cuts; no promotion of the conditional PR885 alone."""
import argparse,hashlib,json
from copy import deepcopy
import verify_source_frontier_through888 as previous
ROOT=previous.ROOT;require=previous.require;accounting=previous.accounting
PREVIOUS_SHA256='aab12b513828d0de9087d5d314af3e9a68bfead828baff419e02202b4968d0e0'
PINS_SHA256='9868ab7458d40723a35e840095d2cc528d7a1b72a52a426d7cfaa55868a66c35'
RULES=[(892,127,'G3.11.cce6e3ba4eeb',[0,1,0,0,0,0,1,0],32),(893,125,'G3.11.ea6bced3bddf',[0,0,1,0,1,0,0,1],9)]
COVERAGE={'892':['original_maximal_profile11_not_only_initial_rank3','PR859_exact_gb_divisor12_exclusion','PR867_section2_only_fivekernel_classification','changed_Wminus11_internal_channels_all_zero','all_fivekernels_all_internal_images_saturated','nonconstant_C9_and_C12I_and_C8_excluded','C12II_negative_row_zero_by_actual_derivative_not_split_type','degree38_saturation_before_original_dual_endpoint','constantC7_to_actualC10_fulltop_exact_intersection','actual_Tchain_complete_U5_8','projected_Wplane_rank0_and_rank1_excluded','coherent_lattice_equals_line_firstpolar_before_saturation','fullspan_complete_degree10_identifies_saturated_U1_10','actual_nested_constant_annihilator_restrictions','constant_projection_commutes_osculation_rational_lifts','inner_ranknullity11plus5_outer_fullspan_line3','lowerbound19_contradicts_original_upper18','compatible_twistone_not_an_exclusion_no_splitfamily_inference'],
'893':['lowerPzero_complete_twoP_kernels_scalarV_internal0_or_full','lowerPnonzero_highonlyP','highP_onto_three_kernels_both_lowVkernel_cases_Hom_on_extensions','highP_divisor12_internalzero_impossible_gap','highP_divisor12_internalVfull_saturation_budget_below12','Vlow_nonzero_internal0_or_EulerWp_both_rawspans_saturated','Vlow_nonzero_M0_both_projection_cases','Vlow_nonzero_M1_all_three_channels_and_exact_extraEuler_block','actual_constantV_lowergraph_capture','constantP_highcapture_negative_tail_Hom_and_positive_degree_quotient','Vlow_zero_unique_degree18V_factors_D12','restricted_highq_nonzero_basepointfree_including_D12','q_nonzero_complete_five_positivekernels_internalzero','q_zero_factor_through_lowline_rawtwoO4_kernel_split','q_zero_saturation_budget_below12_actualV_projection_fullWp_linear_contradiction']}
MAXIMAL_PROFILE={'profile':'11','dual_rank':13,'first_gain':3,'next_gain_upper':2,'inner_constant_kernel_second_rank':11,'inner_projected_second_rank':5,'outer_projected_line_second_rank':3}
def validate_profile(row,original,scope=MAXIMAL_PROFILE):
 require(row['profile']==original['profile']==scope['profile']=='11' and scope==MAXIMAL_PROFILE,'Original maximal profile11 premise missing or broadened')
 require(scope['dual_rank']+scope['first_gain']+scope['next_gain_upper']==18 and scope['inner_constant_kernel_second_rank']+scope['inner_projected_second_rank']+scope['outer_projected_line_second_rank']==19,'Nested annihilator bounds mismatch')
def validate_coverage(c):require(c==COVERAGE,'Incomplete divisor/kernel/scalar/saturation coverage')
def load_inputs():
 snapshot=previous.build(*previous.load_inputs());catalog=previous.load_inputs()[1]
 raw=(ROOT/'frontier-source-through888.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PREVIOUS_SHA256 and json.loads(raw)==snapshot,'Published890 predecessor changed')
 raw=(ROOT/'source-pins-source-through893.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'Manifest changed');pins=json.loads(raw)
 for p in pins.values():
  b=(ROOT/p['local_file']).read_bytes();require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==p['git_blob_sha1'],'Pinned proof/review changed')
 for pr in [892,893]:
  sha=hashlib.sha256((ROOT/pins[f'{pr}_PROOF']['local_file']).read_bytes()).hexdigest();require(sha in (ROOT/pins[f'{pr}_REVIEW']['local_file']).read_text(),'Proof/review binding mismatch')
 proof=(ROOT/pins['892_PROOF']['local_file']).read_text();review=(ROOT/pins['892_REVIEW']['local_file']).read_text()
 for pr in [859,867,885]:
  dep=json.loads((ROOT/'source-pins-source-through888.json').read_text())[f'{pr}_PROOF'];require(dep['commit'] in proof and hashlib.sha256((ROOT/dep['local_file']).read_bytes()).hexdigest() in review,'Missing exact892 prerequisite')
 dep=json.loads((ROOT/'source-pins-source-through888.json').read_text())['887_PROOF'];require(dep['commit'] in (ROOT/pins['893_PROOF']['local_file']).read_text(),'Missing highP universal classification')
 require(hashlib.sha256((ROOT/pins['original_actual']['local_file']).read_bytes()).hexdigest() in review,'Original maximal-profile input not authenticated')
 return snapshot,catalog,pins

def intersect(snapshot,catalog,rules=RULES):
 require(rules==RULES,'Only two exact complete source cuts permitted')
 rows=deepcopy(snapshot['records']);require(len(rows)==len(set(snapshot['remaining_ids']))==4 and {r['id'] for r in rows}==set(snapshot['remaining_ids']),'Stable IDs mismatch')
 originals=json.loads((ROOT/'inputs/original-one-one-pairs-db515250.json').read_text());frontier=json.loads((ROOT/'inputs/pr842-original_frontier.json').read_text())['cases'];ledger=[];seen=set()
 for pr,index,label,t,expected in rules:
  source=originals[index];matches=[r for r in frontier if r['id']==label];row=next(r for r in rows if r['id']==label)
  require(len(matches)==1 and matches[0]['source_index']==index and matches[0]['original_defect']==source['defect']==0 and t in source['compatible_E_types'],'Original source scope mismatch')
  if pr==892:validate_profile(row,matches[0])
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
 validate_coverage(COVERAGE);rows,ledger=intersect(snapshot,catalog)
 require(sum(r['remaining_source_pair_count'] for r in snapshot['records'])==310 and sum(r['remaining_source_pair_count'] for r in rows)==269 and all(r['remaining_source_pairs'] for r in rows),'Pair accounting mismatch')
 for item in ledger:item['proof_commit']=pins[f"{item['pr']}_PROOF"]['commit']
 return {'schema_version':1,'checkpoint':'source-through893-after-published890','previous_checkpoint':{'file':'frontier-source-through888.json','sha256':PREVIOUS_SHA256,'publication_pr':890,'publication_commit':'92fd2ba79aeece747622d3ded7cbdaf22e97eb26','necessary_pairs':310},'remaining_label_count':4,'remaining_ids':deepcopy(snapshot['remaining_ids']),'profile_counts':{'11':3,'12':0,'21':1},'new_full_label_exclusions':[],'pair_accounting':{'input_necessary_pairs':310,'additional_removed_pairs':41,'remaining_necessary_pairs':269},'new_source_edge_exclusion_ledger':ledger,'source_branch_coverage':COVERAGE,'source_pins':pins,'source_pins_sha256':PINS_SHA256,'records':rows,'boundary':deepcopy(snapshot['boundary']),'maximal_profile_premise':MAXIMAL_PROFILE,'scope_policy':'892 applies only to the original maximal profile11, not all splittings; no closure from a failed split family or compatible character. PR891 calibration is not a source cut.','deferred':'All later results, every remaining tuple and whole-label gate are outside this checkpoint.'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=build(*load_inputs());p=ROOT/'frontier-source-through893.json'
 if args.write:p.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==r,'Artifact differs from replay');print('PASS through893: 4 labels (3/0/1), 269 necessary pairs,41 additional pair cuts')
if __name__=='__main__':main()
