#!/usr/bin/env python3
"""Two whole-source cuts; no promotion of the conditional PR885 alone."""
import argparse,hashlib,json
from copy import deepcopy
import verify_frontier_through884 as previous
ROOT=previous.ROOT;require=previous.require;accounting=previous.accounting
PREVIOUS_SHA256='333285c517af01365b6e77f48ac43dc6685cb2bf7a03f0df5d9731fb41d47254'
PINS_SHA256='ca65815e6eb34cbf894d4271c8fc5d18344b517fb5420bfe453f3106837f2b87'
RULES=[(887,125,'G3.11.ea6bced3bddf',[0,1,0,0,1,0,0,1],9),(888,127,'G3.11.cce6e3ba4eeb',[0,1,0,0,0,1,0,1],32)]
COVERAGE={'887':['lower_P_row_zero_both_twoP_kernels_internalzero','lower_P_row_nonzero_highonly_F','highP_divisor12_internalzero_gap_requires_impossible_delta2','three_highP_kernels_A8_W7plusO10_Wp3plusO18','all_fullpositive_kernel_extensions_split','all_internal_channels_zero_or_saturated_A8_O10_O18_graphs','zeroimage_positive_degree_and_Wkernel_positive_degree','A_and_U_polar_spans_constantV','both_projection_multiplicity_cases_and_highonly_direction_not_kerb','actual_constantV_captures_lower_positive_graph','second_constantP_captures_highline','negative_only_residual_constants_removed_rank_at_least4_degree_minus30'],
'888':['PR859_exact_hbf_divisor12_excluded_only','PR867_section2_universal_fivekernels_only','PR885_all_fivekernels_and_all_internal_images','PR885_lowDzero_and_constant_span_scalarplane_obstruction','PR885_C9_impossible_C12caseI_and_C8_degree38_obstruction','PR885_C12caseII_scalarzero_degree38_obstruction','PR885_scalar_nonzero_remaining_optional_Tzero_or_nonzero','PR888_actual_negative_row_kernel_Y0_before_highrow_kernel_X','positive_rank2quotient_all_five_splittings_WpO7_forced','rank3_U0_split_without_assuming_saturation','fullspan_defect_delta0_or12','delta12_original_Sym7_endpoint_dimension10_gt8','delta0_exact_dual_H1_VplusPplusD_and_chi_twist1_minusW','all_twelve_H1atoms_Wfree_at_twist1_degree_minus1_retained']}
def validate_coverage(c):require(c==COVERAGE,'Incomplete divisor/kernel/scalar/saturation coverage')
def load_inputs():
 snapshot=previous.build(*previous.load_inputs());catalog=previous.load_inputs()[1]
 raw=(ROOT/'frontier-through884.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PREVIOUS_SHA256 and json.loads(raw)==snapshot,'Published886 predecessor changed')
 raw=(ROOT/'source-pins-source-through888.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'Manifest changed');pins=json.loads(raw)
 for p in pins.values():
  b=(ROOT/p['local_file']).read_bytes();require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==p['git_blob_sha1'],'Pinned proof/review changed')
 for pr in [885,887,888]:
  sha=hashlib.sha256((ROOT/pins[f'{pr}_PROOF']['local_file']).read_bytes()).hexdigest();require(sha in (ROOT/pins[f'{pr}_REVIEW']['local_file']).read_text(),'Proof/review binding mismatch')
 dependency=pins['885_PROOF'];proof=(ROOT/pins['888_PROOF']['local_file']).read_text();require(dependency['url'] in proof and hashlib.sha256((ROOT/dependency['local_file']).read_bytes()).hexdigest() in proof,'Missing exact885 dependency')
 for pr in [859,867]:require(pins[f'{pr}_PROOF']['commit'] in (ROOT/dependency['local_file']).read_text(),'Missing divisor/classification dependency')
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
 validate_coverage(COVERAGE);rows,ledger=intersect(snapshot,catalog)
 require(sum(r['remaining_source_pair_count'] for r in snapshot['records'])==351 and sum(r['remaining_source_pair_count'] for r in rows)==310 and all(r['remaining_source_pairs'] for r in rows),'Pair accounting mismatch')
 for item in ledger:item['proof_commit']=pins[f"{item['pr']}_PROOF"]['commit']
 return {'schema_version':1,'checkpoint':'source-through888-after-published886','previous_checkpoint':{'file':'frontier-through884.json','sha256':PREVIOUS_SHA256,'publication_pr':886,'publication_commit':'192a2349475498aa3ea08863bd665a85573ccb20','necessary_pairs':351},'remaining_label_count':4,'remaining_ids':deepcopy(snapshot['remaining_ids']),'profile_counts':{'11':3,'12':0,'21':1},'new_full_label_exclusions':[],'pair_accounting':{'input_necessary_pairs':351,'additional_removed_pairs':41,'remaining_necessary_pairs':310},'new_source_edge_exclusion_ledger':ledger,'source_branch_coverage':COVERAGE,'source_pins':pins,'source_pins_sha256':PINS_SHA256,'records':rows,'boundary':deepcopy(snapshot['boundary']),'conditional_dependency_policy':'PR885 alone deletes no pair; only PR888 completes its scalar-nonzero branch. PR867 only supplies universal section2 classification. PR859 alone is not a whole-edge cut.','deferred':'All later results, every remaining tuple and whole-label gate are outside this checkpoint.'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=build(*load_inputs());p=ROOT/'frontier-source-through888.json'
 if args.write:p.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==r,'Artifact differs from replay');print('PASS through888: 4 labels (3/0/1), 310 necessary pairs,41 additional pair cuts')
if __name__=='__main__':main()
