#!/usr/bin/env python3
"""Two-label exclusion with exact original 4/8-source coverage."""
import argparse, hashlib, json
from copy import deepcopy
import verify_source_frontier_pr846 as previous
import verify_source_frontier_through834 as o26
ROOT=previous.ROOT
require=previous.require
PREVIOUS_SHA256='d51a2df425026dba304e3a0c9ce2f4f14b173500d3bceeaedb09c932fc06991d'
PINS_SHA256='e5b3f19ab91096a21cf21b87fec0a0508ff5eb9e725d2d468f587468f989fb24'
COMMIT='eed466e78efb572db42ebbe76bd0176cd47efe3a'
LABELS={112:o26.D,115:o26.W}
LISTS={112:['E0','U6','E3','E6'],115:['E0','U6','E3','E6','E10','U13','E12','E13']}
COVERAGE={
'112:E0':{'0':'PR817 Section7','12':'PR813','20':'PR813 top mismatch'},
'112:U6':{'0':'PR829','12':'PR829','20':'PR829'},
'112:E3':{'0':'PR834','12':'PR813','20':'PR813'},
'112:E6':{'0':'PR840 entire basepoint-free partition','12':'PR813','20':'PR850 with PR825 and PR845'},
'115:E0':{'all':'PR817 Section7 negative W-tail rank mismatch'},
'115:U6':{'0':'PR829','12':'PR829','20':'PR829'},
'115:E3':{'0':'PR834','12':'PR813','20':'PR813'},
'115:E6':{'all':'PR813 and PR840 Section1 negative W-tail rank mismatch'},
'115:E10':{'0':'PR817 Section7','12':'PR813','20':'PR813 top mismatch'},
'115:U13':{'0':'PR829','12':'PR829','20':'PR829'},
'115:E12':{'0':'PR834','12':'PR813','20':'PR813'},
'115:E13':{'0':'PR840 entire basepoint-free partition','12':'PR813','20':'PR850 with PR825 and PR845'}}
TAIL_SCOPE=['actual_E_spans_H','PR825_exact_sheaf_intersections_not_projection_saturation','PR845_all_six_templates','cubic_saturation_defect0_or12_retained','D12_disjoint_from_reduced_D20','constant_span_C1_dimension7_to9_at_most_one_P','tail_full_span_B_dimension_at_least10_contains_P','rank_zero_impossible','E13_rank_one_all_d_ge9_impossible','E6_rank_one_only_d10_missing_P','fiber_kernel_nonzero_L_component_on_every_D20_point','det_tail_Ominus18','wedge_vanishes_on_reduced_degree20_divisor','no_nonzero_Ominus18_to_Ominus20']
def validate_coverage(c,tail):require(c==COVERAGE and tail==TAIL_SCOPE,'Incomplete source/divisor/tail coverage')
def load_inputs():
 s,c,p=previous.load_inputs();snapshot=previous.build(s,c,p)
 raw=(ROOT/'frontier-source-pr846.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PREVIOUS_SHA256 and json.loads(raw)==snapshot,'Published851 predecessor changed')
 raw=(ROOT/'source-pins-through850.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'Manifest changed');pins=json.loads(raw)
 for k,pin in pins.items():
  b=(ROOT/pin['local_file']).read_bytes();require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==pin['git_blob_sha1'],'Pinned proof changed: '+k)
 proof=(ROOT/pins['proof']['local_file']).read_bytes();review=(ROOT/pins['review']['local_file']).read_text();sha=hashlib.sha256(proof).hexdigest();require(sha=='f2874bb3a6b90ef7742ac9f8014ddf532667745c63e8c630dfab70301fda4264' and sha in review,'Review binding mismatch')
 originals=json.loads((ROOT/'inputs/original-one-one-pairs-db515250.json').read_text());frontier=json.loads((ROOT/'inputs/pr842-original_frontier.json').read_text())['cases']
 for ix,label in LABELS.items():
  matches=[r for r in frontier if r['id']==label];require(len(matches)==1 and matches[0]['source_index']==ix and matches[0]['original_defect']==originals[ix]['defect']==0 and matches[0]['profile']=='11','Original label identity mismatch')
  row=next(r for r in snapshot['records'] if r['id']==label)
  for key in ['A','B']:require(previous.canonical(row[key])==previous.canonical(originals[ix][key])==previous.canonical(matches[0][key]),'Original A/B mismatch')
 return snapshot,c,pins,originals

def coverage_report(originals,catalog,coverage=COVERAGE,tail=TAIL_SCOPE):
 validate_coverage(coverage,tail);out=[]
 for ix,names in LISTS.items():
  tuples=[o26.SOURCES[n]['coefficients'] for n in names]
  require(tuples==originals[ix]['compatible_E_types'] and len({tuple(t) for t in tuples})==len(tuples),'Exact original complete source list mismatch')
  for name in names:
   definition=deepcopy(o26.SOURCES[name]);require(previous.canonical(previous.decode(definition['coefficients']))==previous.canonical(definition['blocks']),'Source full decoding mismatch')
   eid=previous.identify(catalog,definition)
   out.append({'label':LABELS[ix],'original_source_index':ix,'source_name':name,'source_definition':definition,'matched_local_E_id':eid,'case_coverage':coverage[str(ix)+':'+name]})
 return out

def build(snapshot,catalog,pins,originals):
 report=coverage_report(originals,catalog)
 ids=snapshot['remaining_ids'];require(len(set(ids))==len(ids)==7,'Duplicate IDs');rows=snapshot['records'];require(len(rows)==7 and {r['id'] for r in rows}==set(ids),'Stable records mismatch')
 ledger=[]
 for ix,label in LABELS.items():
  row=next(r for r in rows if r['id']==label);pairs=row['remaining_source_pairs'];require(len({tuple(p) for p in pairs})==len(pairs)==row['remaining_source_pair_count']==3,'Exact remaining pair count mismatch')
  source='E6' if ix==112 else 'E13';eid=previous.identify(catalog,o26.SOURCES[source]);require(all(e==eid for e,q in pairs),'Unexpected residual source')
  ledger.append({'kind':'whole_label','id':label,'original_source_index':ix,'original_defect':0,'proof_commit':COMMIT,'complete_original_source_count':len(LISTS[ix]),'removed_pairs':deepcopy(pairs),'actual_additional_pair_count':3})
 kept=deepcopy([r for r in rows if r['id'] not in LABELS.values()]);counts={p:sum(r['profile']==p for r in kept) for p in ['11','12','21']}
 require(counts=={'11':4,'12':0,'21':1} and sum(r['remaining_source_pair_count'] for r in kept)==591,'Accounting mismatch')
 return {'schema_version':1,'checkpoint':'whole-label-pr850-after-published851','previous_checkpoint':{'file':'frontier-source-pr846.json','sha256':PREVIOUS_SHA256,'publication_pr':851,'publication_commit':'2738f7fa7c3a6e4b9f90ec98ca8886c40c74c9b4','necessary_pairs':597},'remaining_label_count':5,'remaining_ids':sorted(r['id'] for r in kept),'profile_counts':counts,'new_full_label_exclusion_ledger':ledger,'new_source_edge_exclusions':[],'pair_accounting':{'input_necessary_pairs':597,'additional_removed_pairs':6,'remaining_necessary_pairs':591,'counting_rule':'Remove the three correlated pairs of each excluded label once, not again as source-edge cuts.'},'complete_original_source_coverage':report,'twenty_orbit_tail_scope':TAIL_SCOPE,'source_pins':pins,'source_pins_sha256':PINS_SHA256,'records':kept,'deferred':[{'pr':848,'commit':'77ef1c43e58ca05937ad878f81840274a3a9c064','action':'Not integrated: index113 ff and conditional index127 branch require separate scope accounting.'}],'pr845_usage':'Necessary cubic templates used only as a geometric prerequisite of PR850, never alone as an exclusion.','boundary':deepcopy(snapshot['boundary']),'scope':'Exactly two complete-label exclusions relative to pinned written hypotheses. G3.11.8ae96830fd21 and Source2 remain untouched.'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();result=build(*load_inputs());p=ROOT/'frontier-through850.json'
 if a.write:p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==result,'Artifact differs from replay')
 print(json.dumps({'status':'PASS','labels':5,'profiles':result['profile_counts'],'necessary_pairs':591,'new_pair_cuts':6,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()},sort_keys=True))
if __name__=='__main__':main()
