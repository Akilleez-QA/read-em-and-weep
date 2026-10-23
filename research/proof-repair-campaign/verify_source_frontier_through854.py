#!/usr/bin/env python3
"""Three whole source edges; PR848 conditional branch is not an extra cut."""
import argparse, hashlib, json
from copy import deepcopy
import verify_frontier_through850 as previous
import verify_source_frontier_pr846 as accounting
ROOT=previous.ROOT
require=previous.require
PREVIOUS_SHA256='9dd0642fa5a74b86f0b57682d63b65b13ae0c3ce21a4629b4a3a7a2790d8f844'
PINS_SHA256='185e0dc608dad823306695be14922575656f89334079ee7b485c1a24b1636915'
LABELS={113:'G3.11.ad509d55173f',127:'G3.11.cce6e3ba4eeb'}
TUPLES={'ff':[0,0,0,0,0,2,0,1],'fg':[0,0,0,0,0,1,1,0]}
RULES=[(113,'ff','pr848'),(127,'ff','pr854'),(127,'fg','pr854')]
COVERAGE={'common':['strict_top_D_multiplicity_kernel','nine_high_line_sections_exclude_positive_divisor','all_three_PR802_kernels','internal_zero_or_saturated_Ominus10','nonzero_internal_PR802_all_three_channels','zero_internal_actual_constant_projection_saturated','residual_D_complete_quartic','actual_M_Tminus1_and_C1_quotient_O6'],
'113_ff':['negative_Ominus10_scalar_forced_nonzero','endpoint_kernel_extension_splits','no_internal_Ominus12','actual_G_degree_minus22','preserved_lattice_rank8_or9','onto_O6_to_O22_impossible'],
'127_ff':['kernel_line_of_two_scalar_row_even_if_row_zero','positive_external_zero_Sym10','full_external_derivative_zero','internal_only_Dminus4','D0_plus_L_direct_summand','scalar_line_obstruction'],
'127_fg':['scalar_zero_Euler_nonzero','scalar_zero_positive_external_zero','scalar_zero_internal_only_Dminus4','Euler_kernel_Ominus10_channel_retained_not_assumed_zero','D0_plus_L_direct_summand','scalar_zero_scalar_line_obstruction','scalar_nonzero_actual_graph','scalar_nonzero_kernel_extension_splits','scalar_nonzero_no_internal_Ominus10','scalar_nonzero_G_degree_minus24','scalar_nonzero_onto_O6_to_O24_impossible'],
'scalar_line_obstruction':['actual_image_sheaf_preserved_under_constant_projection','nonzero_image_lattice_degree_minus8_contradiction','L_in_C1','Sym14_no_invariants_forces_L_in_M','D0_plus_L_saturated_via_direct_summand','equal_rank_implies_equality_only_using_saturation','degree_minus18_not_minus6']}
def validate_coverage(c):require(c==COVERAGE,'Incomplete whole-source branch coverage')
def load_inputs():
 s,c,p,o=previous.load_inputs();snapshot=previous.build(s,c,p,o)
 raw=(ROOT/'frontier-through850.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PREVIOUS_SHA256 and json.loads(raw)==snapshot,'Published855 predecessor changed')
 raw=(ROOT/'source-pins-source-through854.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'Manifest changed');pins=json.loads(raw)
 for key,pin in pins.items():
  b=(ROOT/pin['local_file']).read_bytes();require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==pin['git_blob_sha1'],'Pinned file mismatch')
 for pr,sha in [(848,'70a85a7fc501598cfd81d8ee91a4c3244cb195a463a05eaf2a3a43ff93f17ca4'),(854,'1f2c7ffb18c9a4e74b1f398c0edc5da87f08a6cd3d94acb0eea53b3836501218')]:
  b=(ROOT/pins['pr'+str(pr)+'_proof']['local_file']).read_bytes();review=(ROOT/pins['pr'+str(pr)+'_review']['local_file']).read_text();require(hashlib.sha256(b).hexdigest()==sha and sha in review,'Review binding mismatch')
 original=json.loads((ROOT/'inputs/original-one-one-pairs-db515250.json').read_text());frontier=json.loads((ROOT/'inputs/pr842-original_frontier.json').read_text())['cases']
 for ix,label in LABELS.items():
  matches=[r for r in frontier if r['id']==label];require(len(matches)==1 and matches[0]['source_index']==ix and matches[0]['original_defect']==original[ix]['defect']==0,'Original identity mismatch')
  row=next(r for r in snapshot['records'] if r['id']==label)
  for key in ['A','B']:require(accounting.canonical(row[key])==accounting.canonical(original[ix][key])==accounting.canonical(matches[0][key]),'Original A/B mismatch')
 for ix,name,pr in RULES:require(TUPLES[name] in original[ix]['compatible_E_types'],'Original tuple absent')
 return snapshot,c,pins

def intersect(snapshot,catalog,rules=RULES):
 records=deepcopy(snapshot['records']);ids=[r['id'] for r in records];require(len(ids)==len(set(ids))==5 and set(ids)==set(snapshot['remaining_ids']),'Stable IDs mismatch')
 rel={r['id']:{tuple(p) for p in r['remaining_source_pairs']} for r in records}
 for r in records:require(len(rel[r['id']])==len(r['remaining_source_pairs'])==r['remaining_source_pair_count'],'Duplicate pair/count mismatch')
 before=deepcopy(rel);seen=set();ledger=[]
 for ix,name,pr in rules:
  label=LABELS[ix];definition={'coefficients':TUPLES[name],'blocks':accounting.decode(TUPLES[name])};key=(label,accounting.canonical(definition['blocks']));require(key not in seen,'Double source cut');seen.add(key)
  eid=accounting.identify(catalog,definition);cut={p for p in rel[label] if p[0]==eid};rel[label]-=cut
  ledger.append({'kind':'source_edge','label':label,'original_source_index':ix,'source_name':name,'source_definition':definition,'proof':pr,'matched_local_E_id':eid,'removed_pairs':sorted(map(list,cut)),'actual_additional_pair_count':len(cut),'already_absent':not bool(cut),'adjudicated_label_count_delta':0})
 for r in records:
  label=r['id']
  if label in LABELS.values():
   kept=rel[label];cut=before[label]-kept;require(kept|cut==before[label] and not kept&cut,'Pair partition mismatch');r.update(input_necessary_pair_count=len(before[label]),removed_pair_count=len(cut),remaining_source_pair_count=len(kept),remaining_source_pairs=sorted(map(list,kept)),removed_source_pairs=sorted(map(list,cut)),relation_empty=not kept)
 return records,ledger

def build(snapshot,catalog,pins):
 validate_coverage(COVERAGE);records,ledger=intersect(snapshot,catalog)
 require([r['actual_additional_pair_count'] for r in ledger]==[17,32,32],'Exact cuts mismatch');require(all(r['remaining_source_pairs'] for r in records),'Unexpected empty relation')
 require(sum(r['remaining_source_pair_count'] for r in records)==510,'Pair count mismatch')
 return {'schema_version':1,'checkpoint':'source-through854-after-published855','previous_checkpoint':{'file':'frontier-through850.json','sha256':PREVIOUS_SHA256,'publication_pr':855,'publication_commit':'4f1ed662a7124379900d1bb39942a5cd4537066a','necessary_pairs':591},'remaining_label_count':5,'remaining_ids':deepcopy(snapshot['remaining_ids']),'profile_counts':{'11':4,'12':0,'21':1},'new_full_label_exclusions':[],'pair_accounting':{'input_necessary_pairs':591,'additional_removed_pairs':81,'remaining_necessary_pairs':510},'new_source_edge_exclusion_ledger':ledger,'source_branch_coverage':COVERAGE,'prior_conditional_scope':{'pr':848,'index127_fg':'Scalar-nonzero branch only; never counted as a full edge. PR854 now supplies complete scalar-zero/nonzero coverage and independently covers ff.','additional_cuts_from_old_conditional_branch':0},'source_pins':pins,'source_pins_sha256':PINS_SHA256,'records':records,'deferred':[{'pr':856,'kind':'non_exclusion_fixed_window_decomposition','action':'Deferred; no source edge or label removed by a decomposition.'}],'boundary':deepcopy(snapshot['boundary'])}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();result=build(*load_inputs());p=ROOT/'frontier-source-through854.json'
 if a.write:p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==result,'Artifact differs from replay')
 print(json.dumps({'status':'PASS','labels':5,'necessary_pairs':510,'new_pair_cuts':81,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()},sort_keys=True))
if __name__=='__main__':main()
