#!/usr/bin/env python3
"""Two whole-source cuts; no promotion of the conditional PR885 alone."""
import argparse,hashlib,json
from copy import deepcopy
import verify_source_frontier_through893 as previous
ROOT=previous.ROOT;require=previous.require;accounting=previous.accounting
PREVIOUS_SHA256='9f9a2604435b69d66c78da914260a82d8497ed127b55ada874102329dc5d83a0'
PINS_SHA256='4f4029d47b4996474a698cfd5f6cc60cdefbb6a4fc91ecd1f4996ec7db3c72d9'
RULES=[(895,125,'G3.11.ea6bced3bddf',[0,0,2,0,0,0,0,1],9),(897,127,'G3.11.cce6e3ba4eeb',[1,0,1,0,1,1,0,0],32)]
COVERAGE={'895':['strict_top_target_has_twoV_not_direct_exclusion','saturated_fullpositive_pair_complete_elevenatoms_two_kernels','both_kernels_internalzero_positive_degree4','twoV_rows_diagonalized_highP_nondivisible_forces_forbidden_onto_pair','raw_twoO4_highP_zero_or_divisible_retained','raw_kernel_T3_Wp5_internalzero_saturation_budget_below12','actual_constantP_projection_rank7_three_nonzero_channels','actual_projected_quadratic_secondspan_C9_lifts_constantC13','twoV4_tail_highrow_multiplicity1_forces_zeroexternal_summand','internal_derivative_only_top_actual_constant_projection','preserved_coherent_lattice_saturation_proved','tail_image_ranks1_2_trivial_Homzero_rank3_degree_contradiction','FplusJ_saturated_rank13_degree_minus32_vs_constantC13'],
'897':['PR859_exact_acef_divisor12_exclusion','PR867_section2_universal_fivekernels_not_cdf_cuts','changed_full_target_D4_Wp5_V6_Wp7_O10','kernelIV_degree13_Wp_covariant_retained_not_T','all_fivekernel_internal_images_zero_nonzero_and_saturated_combinations','constantC7_actualprojection_then_constantA_negative_Wp3_horizontal','rank8_C9_topdimension_obstruction','rank8_C12_actualcoefficient_map_intersections_and_Y','scalarzero_degree38_shareddefect_atmost5_before_dual','scalarnonzero_PR888_full_interface_reconstructed_not_whole_theorem_transfer','negative_row_kernel_before_highrow_kernel','positive_rank2_allfive_splittings_WpO7','shareddefect0_or12_and_delta12_original_endpoint','delta0_exactcohomology_twelve_Wfree_atoms_degree_minus1_retained','rank6_C8_allowed_Wpminus3_injection_not_Homzero','rank3_degree_minus10_forces_minus3_minus3_minus4','obligatory_scalar_Ominus4_companion_has_zero_map_all_target_blocks','C8_lowerrows_zero_degree38_obstruction']}
CHANNEL_BOUNDARY={'cc_strict_top_excludes':False,'cc_top_V_multiplicity':2,'cc_target_V_multiplicity':2,'acef_Wp_minus3_self_channel_allowed':True,'acef_kernelIV_Wp_degree13_covariant_allowed':True,'acef_companion_obstruction':'mandatory scalar O(-4), not whole-source Hom vanishing'}
def validate_channels(c):require(c==CHANNEL_BOUNDARY,'Changed-target allowed channels incorrectly discarded')
def validate_coverage(c):require(c==COVERAGE,'Incomplete divisor/kernel/scalar/saturation coverage')
def load_inputs():
 snapshot=previous.build(*previous.load_inputs());catalog=previous.load_inputs()[1]
 raw=(ROOT/'frontier-source-through893.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PREVIOUS_SHA256 and json.loads(raw)==snapshot,'Published898 predecessor changed')
 raw=(ROOT/'source-pins-source-through897.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'Manifest changed');pins=json.loads(raw)
 for p in pins.values():
  b=(ROOT/p['local_file']).read_bytes();require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==p['git_blob_sha1'],'Pinned proof/review changed')
 for pr in [895,897]:
  sha=hashlib.sha256((ROOT/pins[f'{pr}_PROOF']['local_file']).read_bytes()).hexdigest();require(sha in (ROOT/pins[f'{pr}_REVIEW']['local_file']).read_text(),'Proof/review binding mismatch')
 proof=(ROOT/pins['897_PROOF']['local_file']).read_text();review=(ROOT/pins['897_REVIEW']['local_file']).read_text()
 for pr in [859,867,885,888]:
  dep=json.loads((ROOT/'source-pins-source-through888.json').read_text())[f'{pr}_PROOF'];require(dep['commit'] in proof and hashlib.sha256((ROOT/dep['local_file']).read_bytes()).hexdigest() in review,'Missing exact897 prerequisite')
 require(hashlib.sha256((ROOT/'inputs/pr888_proof.md').read_bytes()).hexdigest() in proof,'Scalar-row interface not exact-version bound')
 for pr in [875,882]:
  dep=json.loads((ROOT/'source-pins-source-through882.json').read_text())[f'pr{pr}_proof'];require(dep['commit'] in (ROOT/pins['895_PROOF']['local_file']).read_text(),'Missing universal895 interface dependency')
 return snapshot,catalog,pins

def intersect(snapshot,catalog,rules=RULES):
 require(rules==RULES,'Only two exact complete source cuts permitted')
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
 require(sum(r['remaining_source_pair_count'] for r in snapshot['records'])==269 and sum(r['remaining_source_pair_count'] for r in rows)==228 and all(r['remaining_source_pairs'] for r in rows),'Pair accounting mismatch')
 for item in ledger:item['proof_commit']=pins[f"{item['pr']}_PROOF"]['commit']
 return {'schema_version':1,'checkpoint':'source-through897-after-published898','previous_checkpoint':{'file':'frontier-source-through893.json','sha256':PREVIOUS_SHA256,'publication_pr':898,'publication_commit':'5d2345090aecc2240555fb6f39a1f2ea813dcd62','necessary_pairs':269},'remaining_label_count':4,'remaining_ids':deepcopy(snapshot['remaining_ids']),'profile_counts':{'11':3,'12':0,'21':1},'new_full_label_exclusions':[],'pair_accounting':{'input_necessary_pairs':269,'additional_removed_pairs':41,'remaining_necessary_pairs':228},'new_source_edge_exclusion_ledger':ledger,'source_branch_coverage':COVERAGE,'source_pins':pins,'source_pins_sha256':PINS_SHA256,'records':rows,'boundary':deepcopy(snapshot['boundary']),'changed_channel_boundary':CHANNEL_BOUNDARY,'scope_policy':'895 uses raw-divisor/polar/trapped-tail proof, not strict-top alone.897 reconstructs both scalar-row interfaces and retains allowed Wp channels.','deferred':'All later results, every remaining tuple and whole-label gate are outside this checkpoint.'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=build(*load_inputs());p=ROOT/'frontier-source-through897.json'
 if args.write:p.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==r,'Artifact differs from replay');print('PASS through897: 4 labels (3/0/1), 228 necessary pairs,41 additional pair cuts')
if __name__=='__main__':main()
