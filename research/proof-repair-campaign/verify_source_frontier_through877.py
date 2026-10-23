#!/usr/bin/env python3
"""Finite source-edge reconciliation; written proofs remain explicit premises."""
import argparse,hashlib,json
from copy import deepcopy
import verify_source_frontier_through860 as previous
ROOT=previous.ROOT;require=previous.require;accounting=previous.accounting
PREVIOUS_SHA256='8c9703f6f91bd92cf96053f498d7caab9c248d9a9339ea5a2666b3ee3ac7f77c'
PINS_SHA256='981d6b5f1f8a69130715b399a343826667b868368d5ec2a8e4012964484df39b'
LABELS={113:'G3.11.ad509d55173f',125:'G3.11.ea6bced3bddf',127:'G3.11.cce6e3ba4eeb'}
TUPLES={'cf':[0,0,1,0,0,1,0,1],'cg':[0,0,1,0,0,0,1,0],'bc':[0,1,1,0,0,0,0,1],'bf':[0,1,0,0,0,1,0,1],'bb':[0,2,0,0,0,0,0,1]}
RULES=[(868,113,'cf',17),(870,127,'cf',32),(870,127,'cg',32),(874,113,'bc',17),(875,125,'bf',9),(877,113,'bb',17)]
LATER=[(881,113,'bf',17),(882,125,'cf',9)]
COVERAGE={
'868':['PR861_sections2_to5_exclude_divisor0','PR861_sections6_to7_actual_C9_exact_intersections','divisor12_derivative_comparison_and_stabilizer_characters_2_vs_8_6','double_D12_defect_24_to29_hence24','both_degree38_extensions','original_Sym9_dual_endpoint_no_stronger_vanishing'],
'870':['both_cf_and_cg_full_source_tails_checked','low_D_row_zero_rank12_gap','divisor0_four_kernels_all_internal_images_0_W7_O8','actual_Pconstant_Tlinear_channels_and_rank2_forcing','divisor12_exact_intersections_changed_tails','double_D12_characters_2_vs_6_6','both_extensions_original_Sym7_dual_endpoint'],
'874':['divisor0_four_kernels_internal_zero_degree4','divisor12_raw_defect_at_most8_hence0','changed_bc_tail_exact_intersection_Hom_vanishing','double_D12_exact24','both_extensions_original_Sym9_dual_endpoint'],
'875':['cubic_T_auxiliary_all_one_two_three_increments','lower_P_row_zero_J0_and_all_linear_channels','lower_P_nonzero_canonical_Wp3_capture','high_D_no_divisor12','all_internal_images_0_Wp5_O10_Wp5plusO10_saturated','constant_AplusP_scalar_Tnonzero_Ponly','linear_AplusT_equaldegree24_positivepair_capture','negative_residual_scalar_T_Wp_only_cases'],
'877':['high_P_divisors_0_or12_complete','divisor12_internal_zero_actual_Euler_horizontal','divisor0_all_five_kernels','all_0_A8_O10_W9_O18_internal_images_saturated','A8_C9_rank8_degree_bound','A8_C12_both_extension_classes_no_injection','O18_Tlinear_actual_cubic_C8','C8_not_in_Eplus_all_degree3_channels_zero','degree38_quotient_fullspan_defect_at_most5_hence0','both_extensions_original_dual_endpoint'],
'881':['high_P_divisors_0_or12_complete','divisor12_changed_D_internal_zero_Euler_horizontal','kernelI_images_0_W7_A8','kernelII_images_0_W7_O10_W7plusO10','kernelIII_images_0_O8_W9','kernelIV_images_0_O18','kernelV_images_0_O8_O10_O8plusO10','constant_VplusP_negative_horizontal_O8_Sym10_AplusVplusD','both_rank8_linear_C9_top_dimensions6_7_impossible','both_rank8_linear_C12_degree38_exact_quotient','Tlinear_C8_changed_degree2_3_Hom_checked','uniform_fullspan_defect_at_most5_hence0','both_extensions_original_dual_endpoint'],
'882':['Vtop_auxiliary_exact_projection_negative_tails','complete_Sym6_auxiliary_trapped_V_coherent_image_all_ranks','lower_P_row_zero_all_J0_V4_O10_cases','lower_P_nonzero_canonical_Wp3','high_D_basepointfree_unique_kernel','all_internal_images_0_Wp5_O10_Wp5plusO10_saturated','constant_AplusP_scalar_VandP_Vonly_Ponly','linear_AplusT_equaldegree24_capture','negative_residual_scalar_Vnonzero_Wponly']}
def validate_coverage(coverage,prs):
 require(coverage=={str(pr):COVERAGE[str(pr)] for pr in sorted(set(prs))},'Incomplete source/divisor coverage')
def pins_load():
 raw=(ROOT/'source-pins-source-through882.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'Manifest changed');pins=json.loads(raw)
 for p in pins.values():
  b=(ROOT/p['local_file']).read_bytes();require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==p['git_blob_sha1'],'Pinned source changed')
 for pr in [868,870,874,875,877,881,882]:
  sha=hashlib.sha256((ROOT/pins[f'pr{pr}_proof']['local_file']).read_bytes()).hexdigest()
  require(sha in (ROOT/pins[f'pr{pr}_review']['local_file']).read_text(),'Exact proof/review binding mismatch')
 require(hashlib.sha256((ROOT/pins['pr861_proof']['local_file']).read_bytes()).hexdigest() in (ROOT/pins['pr868_review']['local_file']).read_text(),'Missing divisor0 dependency binding')
 return pins

def load_inputs():
 s,c,p=previous.load_inputs();snapshot=previous.build(s,c,p)
 raw=(ROOT/'frontier-source-through860.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PREVIOUS_SHA256 and json.loads(raw)==snapshot,'Published863 predecessor changed')
 return snapshot,c,pins_load()

def intersect(snapshot,catalog,rules,allowed):
 require(rules==allowed,'Duplicate, omitted, conditional or broadened source cut')
 records=deepcopy(snapshot['records']);ids=[r['id'] for r in records]
 require(len(set(ids))==len(ids)==5 and set(ids)==set(snapshot['remaining_ids']),'Stable IDs changed')
 original=json.loads((ROOT/'inputs/original-one-one-pairs-db515250.json').read_text());frontier=json.loads((ROOT/'inputs/pr842-original_frontier.json').read_text())['cases']
 ledger=[];seen=set()
 for pr,index,name,expected in rules:
  label=LABELS[index];row=next(r for r in records if r['id']==label);source=original[index];match=[r for r in frontier if r['id']==label]
  require(len(match)==1 and match[0]['source_index']==index and match[0]['original_defect']==source['defect']==0,'Original source scope changed')
  for key in ['A','B']:require(accounting.canonical(row[key])==accounting.canonical(source[key])==accounting.canonical(match[0][key]),'Original quotient identity mismatch')
  t=TUPLES[name];require(t in source['compatible_E_types'],'Tuple absent from original source list')
  definition={'coefficients':t,'blocks':accounting.decode(t)};eid=accounting.identify(catalog,definition)
  require((label,eid) not in seen,'Double source exclusion');seen.add((label,eid))
  before={tuple(p) for p in row['remaining_source_pairs']};require(len(before)==len(row['remaining_source_pairs'])==row['remaining_source_pair_count'],'Duplicate pair/count mismatch')
  cut={p for p in before if p[0]==eid};kept=before-cut
  require(len(cut)==expected and cut.isdisjoint(kept) and cut|kept==before,'Exact additional cut mismatch')
  row.update(remaining_source_pairs=sorted(map(list,kept)),remaining_source_pair_count=len(kept),relation_empty=not kept)
  ledger.append({'kind':'source_edge','pr':pr,'label':label,'original_source_index':index,'source_name':name,'source_definition':definition,'matched_local_E_id':eid,'removed_pairs':sorted(map(list,cut)),'actual_additional_pair_count':len(cut),'adjudicated_label_count_delta':0})
 for row in records:
  old=next(r for r in snapshot['records'] if r['id']==row['id']);a={tuple(p) for p in old['remaining_source_pairs']};b={tuple(p) for p in row['remaining_source_pairs']}
  row.update(input_necessary_pair_count=len(a),removed_pair_count=len(a-b),removed_source_pairs=sorted(map(list,a-b)),relation_empty=not b)
 return records,ledger

def make(snapshot,catalog,pins,rules,checkpoint,previous_file,previous_sha,input_count,remaining_count):
 coverage={str(pr):COVERAGE[str(pr)] for pr in sorted({r[0] for r in rules})};validate_coverage(coverage,[r[0] for r in rules])
 records,ledger=intersect(snapshot,catalog,rules,rules)
 require(sum(r['remaining_source_pair_count'] for r in snapshot['records'])==input_count,'Input total changed')
 require(sum(r['remaining_source_pair_count'] for r in records)==remaining_count and sum(r['actual_additional_pair_count'] for r in ledger)==input_count-remaining_count,'Accounting mismatch')
 for entry in ledger:entry['proof_commit']=pins[f"pr{entry['pr']}_proof"]['commit']
 return {'schema_version':1,'checkpoint':checkpoint,'previous_checkpoint':{'file':previous_file,'sha256':previous_sha,'necessary_pairs':input_count},'remaining_label_count':5,'remaining_ids':deepcopy(snapshot['remaining_ids']),'profile_counts':{'11':4,'12':0,'21':1},'nonempty_relation_label_count':sum(bool(r['remaining_source_pairs']) for r in records),'new_full_label_exclusions':[],'whole_label_gate':{'G3.11.ad509d55173f':'closed_pending_separate_immutable_original_ten_tuple_exhaustion'},'pair_accounting':{'input_necessary_pairs':input_count,'additional_removed_pairs':input_count-remaining_count,'remaining_necessary_pairs':remaining_count},'new_source_edge_exclusion_ledger':ledger,'source_branch_coverage':coverage,'source_pins':pins,'source_pins_sha256':PINS_SHA256,'records':records,'boundary':{'necessary_relation_not_realizability':True,'no_actual_instance_computation':True,'not_Lean_certified':True,'PR869':'Nonempty abstract degree28 family; no HM realization or exclusion.','PR876':'Nonempty abstract source127 cdf family; no HM realization or exclusion.','all_other_results':'Deferred; no inference from abstracts or conditional branches.'}}
def build(snapshot,catalog,pins):return make(snapshot,catalog,pins,RULES,'source-through877','frontier-source-through860.json',PREVIOUS_SHA256,501,377)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();result=build(*load_inputs());p=ROOT/'frontier-source-through877.json'
 if args.write:p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==result,'Artifact differs from replay');print('PASS through877: 5 registered labels, 377 necessary pairs, 124 new pair cuts')
if __name__=='__main__':main()
