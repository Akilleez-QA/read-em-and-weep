#!/usr/bin/env python3
"""Integrate the six PR846 source edges after published PR849."""
import argparse, hashlib, json
from copy import deepcopy
import verify_frontier_through847 as previous
ROOT=previous.ROOT
require=previous.require
identify=previous.previous.identify
canonical=previous.previous.canonical
PREVIOUS_SHA256='6f59ac28b5a4cdfc34658dbd862e344dae2f1ed7ede053f2be0bc707c6595ee3'
PINS_SHA256='48b5c2ceafd8a6726c0fadbd720fbc1ebc05747812bd13e801689cb119ef966b'
LABELS={113:'G3.11.ad509d55173f',125:'G3.11.ea6bced3bddf',127:'G3.11.cce6e3ba4eeb'}
TUPLES={'ef':[0,0,0,0,1,1,0,1],'ce':[0,0,1,0,1,0,0,1],'be':[0,1,0,0,1,0,0,1],'ee':[0,0,0,0,2,0,0,1],'eg':[0,0,0,0,1,0,1,0]}
RULES=[(113,'ef','complementary_D'),(113,'ce','quadratic_gap'),(113,'be','zero_internal'),(125,'ee','forced_subblock'),(127,'ef','complementary_D'),(127,'eg','complementary_D')]
COVERAGE={'common':['strict_top_eight_or_eleven_sections','positive_divisor_at_least12_leaves_at_most7_sections','external_O16_saturated_original_defect0','both_exact_kernel_types'],
'complementary_D':['J_zero_positive_degree','J_Ominus8_nongenuine_linear_character','J_Wminus7_saturated_universal_multiplication','dependent_rows_rank4_into_rank3','independent_rows_full_linear_block_connection_contradiction'],
'zero_internal':['both_kernels_all_internal_Hom_zero','actual_first_span_positive_degree2'],
'quadratic_gap':['full_V_plus_2P_top','both_kernels_all_internal_Hom_zero','raw_quotient_O18','rank11_gap_requires22_or_at_most10'],
'forced_subblock':['three_P_section_multiplicity_isomorphism','kernel_of_lower_O4_projection_is_two_P','both_kernels_all_internal_Hom_zero','actual_first_span_positive_degree2']}
def decode(t):
 a,b,c,d,e,f,g,h=t
 require(c+g+h>=1,'Invalid source top')
 return [[-2,'V']]*(c+g+h-1)+[[-2,'P']]*(d+e+g+h)+[[-2,'D']]*(f+g)+[[-3,'Wp']]*a+[[-3,'T']]*b+[[-4,'V']]*c+[[-4,'P']]*d+[[-5,'Wp']]*e+[[-8,'one']]*f+[[-9,'W']]*g+[[-10,'one']]*h
def validate_coverage(c):require(c==COVERAGE,'Incomplete whole-source coverage')
def load_inputs():
 s,c,o,p,t=previous.load_inputs();snapshot=previous.build(s,c,o,p,t)
 raw=(ROOT/'frontier-through847.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PREVIOUS_SHA256 and json.loads(raw)==snapshot,'Predecessor changed')
 raw=(ROOT/'source-pins-source-pr846.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'Manifest changed');pins=json.loads(raw)
 for k,pin in pins.items():
  b=(ROOT/pin['local_file']).read_bytes();require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==pin['git_blob_sha1'],'Proof blob mismatch')
 proof=(ROOT/pins['proof']['local_file']).read_bytes();review=(ROOT/pins['review']['local_file']).read_text();sha=hashlib.sha256(proof).hexdigest();require(sha=='e1c5bdad0cfe1f989ba1d325d35cd80d69dafc961da7710691a173c235b0af9a' and sha in review,'Review binding mismatch')
 original=json.loads((ROOT/'inputs/original-one-one-pairs-db515250.json').read_text());frontier=json.loads((ROOT/'inputs/pr842-original_frontier.json').read_text())['cases']
 for ix,label in LABELS.items():
  matches=[r for r in frontier if r['id']==label];require(len(matches)==1 and matches[0]['source_index']==ix and matches[0]['original_defect']==original[ix]['defect']==0,'Original label identity mismatch')
  row=next(r for r in snapshot['records'] if r['id']==label)
  for key in ['A','B']:require(canonical(row[key])==canonical(original[ix][key])==canonical(matches[0][key]),'Original quotient mismatch')
 for ix,name,case in RULES:require(TUPLES[name] in original[ix]['compatible_E_types'],'Source not in original list')
 return snapshot,c,pins

def intersect(snapshot,catalog,rules=RULES):
 records=deepcopy(snapshot['records']);ids=[r['id'] for r in records];require(len(ids)==len(set(ids))==7 and set(ids)==set(snapshot['remaining_ids']),'Stable IDs mismatch')
 rows={r['id']:r for r in records};rel={r['id']:{tuple(p) for p in r['remaining_source_pairs']} for r in records}
 for r in records:require(len(rel[r['id']])==len(r['remaining_source_pairs'])==r['remaining_source_pair_count'],'Duplicate pair/count mismatch')
 before=deepcopy(rel);ledger=[];seen=set()
 for ix,name,case in rules:
  label=LABELS[ix];definition={'coefficients':TUPLES[name],'blocks':decode(TUPLES[name])};key=(label,canonical(definition['blocks']));require(key not in seen,'Double source cut');seen.add(key)
  eid=identify(catalog,definition);cut={p for p in rel[label] if p[0]==eid};rel[label]-=cut
  ledger.append({'kind':'source_edge','label':label,'original_source_index':ix,'source_name':name,'source_definition':definition,'coverage':case,'matched_local_E_id':eid,'removed_pairs':sorted(map(list,cut)),'actual_additional_pair_count':len(cut),'already_absent':not bool(cut),'adjudicated_label_count_delta':0})
 for label in LABELS.values():
  r=rows[label];kept=rel[label];cut=before[label]-kept;require(kept|cut==before[label] and not kept&cut,'Pair partition mismatch');r.update(input_necessary_pair_count=len(before[label]),removed_pair_count=len(cut),remaining_source_pair_count=len(kept),remaining_source_pairs=sorted(map(list,kept)),removed_source_pairs=sorted(map(list,cut)),relation_empty=not kept)
 return records,ledger

def build(snapshot,catalog,pins):
 validate_coverage(COVERAGE);records,ledger=intersect(snapshot,catalog)
 cuts=[r['actual_additional_pair_count'] for r in ledger]
 require(cuts==[17,17,17,9,32,32],'Exact six-edge accounting mismatch')
 require(all(r['remaining_source_pairs'] for r in records),'Unexpected empty relation: label adjudication required separately')
 require(sum(r['remaining_source_pair_count'] for r in records)==597,'Pair total mismatch')
 return {'schema_version':1,'checkpoint':'source-pr846-after-published849','previous_checkpoint':{'file':'frontier-through847.json','sha256':PREVIOUS_SHA256,'publication_pr':849,'publication_commit':'8d279e1816025b4c2103e4ebbd698cd94ac419f7','necessary_pairs':721},'remaining_label_count':7,'remaining_ids':deepcopy(snapshot['remaining_ids']),'profile_counts':{'11':6,'12':0,'21':1},'new_full_label_exclusions':[],'pair_accounting':{'input_necessary_pairs':721,'additional_removed_pairs':124,'remaining_necessary_pairs':597},'new_source_edge_exclusion_ledger':ledger,'source_branch_coverage':COVERAGE,'source_pins':pins,'source_pins_sha256':PINS_SHA256,'records':records,'deferred':[r for r in snapshot['deferred'] if r['pr']!=846],'later_results':'Not integrated; this checkpoint contains exactly the six PR846 source edges.','boundary':deepcopy(snapshot['boundary']),'scope':'Necessary-source relation accounting conditional on pinned written geometric proofs; no label cut or realization assertion.'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();result=build(*load_inputs());p=ROOT/'frontier-source-pr846.json'
 if a.write:p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==result,'Artifact differs from replay')
 print(json.dumps({'status':'PASS','labels':7,'necessary_pairs':597,'new_pair_cuts':124,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()},sort_keys=True))
if __name__=='__main__':main()
