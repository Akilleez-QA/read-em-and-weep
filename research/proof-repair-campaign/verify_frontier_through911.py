#!/usr/bin/env python3
"""Close only the independently exhausted original source125 label gate."""
import argparse,hashlib,json
from copy import deepcopy
import verify_source_frontier_through907 as previous
from verify_frontier_through884 import sym
ROOT=previous.ROOT;require=previous.require;accounting=previous.accounting
LABEL='G3.11.ea6bced3bddf';COMMIT='64945ab759c313f1aa35611f91236ee7deb387dd'
PREVIOUS_SHA256='f7b9a00a617792d9127c787e386ab7ab46933e78b94fe2d5340b7368aa60deda'
PINS_SHA256='70367df9c1b804d08180ddd708d85df81e3509e02453962409471ba744413196';BASELINE_SHA256='3315d80f651911f87e8b12006263994cd591a4b5938e621fcf6bda111332b77c'
NAMES=['ff','ef','ee','cf','ce','cc','bf','be','bc','bb']
PRS={'ee':846,'ef':860,'bf':875,'cf':882,'be':887,'ce':893,'cc':895,'bb_bc':906}
SCOPE={'ff':'strict_top_D_multiplicity2_gt1_not_fiber_injectivity','ef':'lowerPzero_included_three_kernels_all_four_internal_images','ee':'forced_twoP_kernel_both_kernels_all_internalzero','cf':'lowerPzero_excluded_both_highD_spans_all_scalar_component_cases','ce':'both_lowerV_rows_highP_onto_or_divisor12_both_restricted_q_cases','cc':'two_targetV_not_strict_top_raw_divisor_and_coherent_tail','bf':'lowerP_nonzero_all_highD_images_scalar_and_T_cases','be':'both_lowerrow_and_divisor_alternatives_three_kernels_negative_residual','bc':'scalarO10_retained_quartic_zero_and_nonzero_actual_quotients','bb':'scalarO10_retained_actual_constantA_P_linearT_excluded'}
def gitsha(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def load_inputs():
 s,c,p=previous.load_inputs();snapshot=previous.build(s,c,p)
 raw=(ROOT/'frontier-source-through907.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PREVIOUS_SHA256 and json.loads(raw)==snapshot,'Through907 changed')
 raw=(ROOT/'source-pins-through911.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'Gate manifest changed');pins=json.loads(raw)
 for pin in pins.values():require(gitsha((ROOT/pin['local_file']).read_bytes())==pin['git_blob_sha1'],'Pinned gate input changed')
 review=(ROOT/pins['REVIEW.md']['local_file']).read_text()
 for key in ['PROOF.md','COVERAGE.json']:require(hashlib.sha256((ROOT/pins[key]['local_file']).read_bytes()).hexdigest() in review,'Gate review binding mismatch')
 require(pins['original_endpoint']['git_blob_sha1']=='dcacf0bcdef8377c1ed7654e5b82659ea409456e','Necessary universe foundation mismatch')
 return snapshot,c,pins,json.loads((ROOT/pins['COVERAGE.json']['local_file']).read_text())
def coverage_report(coverage,scope=SCOPE):
 require(scope==SCOPE,'Incomplete branch scope')
 require(coverage['stable_label']==LABEL and coverage['source_index']==125 and coverage['catalog_commit']=='db51525015bb7c5e825833d550d08dedf6f6ea96' and coverage['closure_state']=='exact_ten_row_dependencies_complete','Wrong gate scope')
 orig=json.loads((ROOT/'inputs/original-one-one-pairs-db515250.json').read_text())[125];front=json.loads((ROOT/'inputs/pr842-original_frontier.json').read_text())['cases'];matches=[r for r in front if r['id']==LABEL]
 require(len(matches)==1 and matches[0]['source_index']==125 and matches[0]['original_defect']==orig['defect']==coverage['original_defect']==0,'Original source identity mismatch')
 for key,other,value in [('A','A_q',[[-10,'one'],[4,'one'],[16,'one']]),('B','B_q',[[-18,'one'],[-6,'one'],[8,'one']])]:require(orig[key]==matches[0][key]==coverage[other]==value,'Endpoint mismatch')
 rows=coverage['rows'];require([r['name'] for r in rows]==NAMES and [r['tuple'] for r in rows]==orig['compatible_E_types'] and len({tuple(r['tuple']) for r in rows})==10,'Not original ordered ten tuples')
 proofs=coverage['proofs'];require(set(proofs)==set(PRS),'Missing or extra theorem')
 # Independent immutable predecessor pin lookup, not trust in the new coverage alone.
 known={}
 for f in ROOT.glob('source-pins*.json'):
  if f.name=='source-pins-through911.json':continue
  d=json.loads(f.read_text())
  if isinstance(d,dict):
   for pin in d.values():
    if isinstance(pin,dict) and 'local_file' in pin and 'git_blob_sha1' in pin:known[pin['git_blob_sha1']]=pin
 for name,pr in PRS.items():
  p=proofs[name];require(p['pr']==pr and p['status']=='published' and p['git_blob'] in known,'Theorem source mismatch');old=known[p['git_blob']]
  require(p['commit']==old['commit'] and p['path']==old['path'] and p['url']==old['url'],'Immutable theorem provenance mismatch')
  b=(ROOT/old['local_file']).read_bytes();require(gitsha(b)==p['git_blob'] and all(m in b.decode() for m in p['scope_markers']),'Exact theorem bytes/scope mismatch')
 bb=proofs['bb_bc'];b=(ROOT/'inputs/pr906_proof.md').read_bytes();rev=(ROOT/'inputs/pr906_review.md').read_bytes();require(hashlib.sha256(b).hexdigest()==bb['sha256'] and hashlib.sha256(rev).hexdigest()==bb['review_sha256'] and gitsha(rev)==bb['review_git_blob'] and bb['sha256'] in rev.decode(),'Complete bb/bc exact review mismatch')
 target={k:sym(6)[k]+sym(18)[k] for k in sym(6)};require({k:v for k,v in target.items() if v}=={'A':1,'V':2,'P':3,'D':1},'ff target mismatch')
 result=[]
 for r in rows:
  a,b,c,d,e,f,g,h=r['tuple'];require((a,d,g,h)==(0,0,0,1) and b+c+e+f==2 and r['name']=='b'*b+'c'*c+'e'*e+'f'*f,'Tuple naming mismatch')
  blocks=accounting.decode(r['tuple']);expanded=[[-j,rep] for j,rep,m in r['bundle'] for _ in range(m)];require(accounting.canonical(blocks)==accounting.canonical(expanded),'Decoded multiset mismatch')
  require(r['proof']==('direct_ff' if r['name']=='ff' else 'bb_bc' if r['name'] in ['bb','bc'] else r['name']),'Wrong row theorem')
  if r['name']=='ff':require(f+g==2>target['D'],'No direct ff obstruction')
  result.append(dict(r,source_definition={'coefficients':r['tuple'],'blocks':blocks},complete_scope=scope[r['name']]))
 return result

def build(snapshot,catalog,pins,coverage):
 report=coverage_report(coverage);rows=snapshot['records'];ids=snapshot['remaining_ids'];require(len(rows)==len(set(ids))==4 and {r['id'] for r in rows}==set(ids),'Input label set mismatch')
 row=next(r for r in rows if r['id']==LABEL);require(row['remaining_source_pairs']==[] and row['remaining_source_pair_count']==0,'Cannot remove unaccounted source pairs')
 kept=deepcopy([r for r in rows if r['id']!=LABEL]);counts={p:sum(r['profile']==p for r in kept) for p in ['11','12','21']};require(counts=={'11':2,'12':0,'21':1} and sum(r['remaining_source_pair_count'] for r in kept)==146,'Final accounting mismatch')
 raw=(ROOT/'frontier.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==BASELINE_SHA256,'Fixed campaign805 changed');base=json.loads(raw);before={(r['id'],*p) for r in base['records'] for p in r['baseline_pairs']};after={(r['id'],*p) for r in kept for p in r['remaining_source_pairs']};require(len(before)==1790 and len(after)==146 and after<=before and len(base['remaining_ids'])==17,'Fixed baseline relation mismatch')
 residual=[]
 for row in kept:
  sources=[]
  for e in sorted({p[0] for p in row['remaining_source_pairs']}):
   defs=[r for r in catalog if r['id']==e];require(len(defs)==1,'Residual source ID mismatch');definition=defs[0];require(accounting.identify(catalog,definition)==e,'Residual multiset mismatch');sources.append({'coefficients':definition['coefficients'],'blocks':definition['blocks'],'necessary_pair_count':sum(a==e for a,q in row['remaining_source_pairs'])})
  residual.append({'id':row['id'],'profile':row['profile'],'necessary_pair_count':row['remaining_source_pair_count'],'remaining_source_definitions':sources})
 return {'schema_version':1,'checkpoint':'whole-label-through911','previous_checkpoint':{'file':'frontier-source-through907.json','sha256':PREVIOUS_SHA256,'necessary_pairs':146},'remaining_label_count':3,'remaining_ids':sorted(r['id'] for r in kept),'profile_counts':counts,'new_full_label_exclusion_ledger':[{'kind':'whole_label','id':LABEL,'original_source_index':125,'proof_commit':COMMIT,'complete_original_source_count':10,'removed_pairs':[],'actual_additional_pair_count':0}],'new_source_edge_exclusions':[],'pair_accounting':{'input_necessary_pairs':146,'additional_removed_pairs':0,'remaining_necessary_pairs':146},'complete_original_source_coverage':report,'source_pins':pins,'source_pins_sha256':PINS_SHA256,'records':kept,'residual_source_summary':residual,'boundary':deepcopy(snapshot['boundary']),'fixed_campaign805_comparison':{'baseline_file':'frontier.json','baseline_sha256':BASELINE_SHA256,'baseline_labels':17,'final_labels':3,'labels_removed':14,'baseline_necessary_pairs':1790,'final_necessary_pairs':146,'necessary_pairs_removed':1644,'remaining_ids_subset_of_original':set(r['id'] for r in kept)<=set(base['remaining_ids'])},'scope':'Only original source125 label gate closes. Source2, index127 and8ae remain. Necessary pairs are not realizations. No formal proof or actual-instance claim.'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=build(*load_inputs());p=ROOT/'frontier-through911.json'
 if args.write:p.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==r,'Artifact differs from replay');print('PASS through911: 3 labels (2/0/1), 146 necessary pairs unchanged; fixed805 17/1790 -> 3/146')
if __name__=='__main__':main()
