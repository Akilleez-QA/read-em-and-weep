#!/usr/bin/env python3
"""Append only the exact PR917 whole-source cut to independently replayed911."""
import argparse,hashlib,json
from pathlib import Path
from copy import deepcopy
import verify_frontier_through911 as previous
ROOT=Path(__file__).resolve().parent
require=previous.require; accounting=previous.accounting
PREVIOUS_SHA256='4957c38049d571e5b69f7e46f609a926bf7a5dbdf12ff259f98c1c64cf1fbf0f'
PINS_SHA256='274e9491401cd17a26c8a59e499dfe356e8f27eb611b2ddd492a04d4b6939b43'
LABEL='G3.11.cce6e3ba4eeb';TUPLE=[1,1,1,0,0,1,0,0];COMMIT='c17aac695580fff0ff7dacd1247ce0b8adf01a8f'
SCOPE=['913_nonzero_low_D_no_high_assumption','positive_Gauss_preimage_forces_actual_constant_A','A_captures_saturated_high_line_everywhere','exact_kernel_W_minus9','negative_external_row_separates_original_scalar','actual_target_pullback_Ext1_G_zero_unique_splitting','standalone_E0_derivative_saturated_O2','all_five_constant_budgets_and_three_residual_bundles','VplusP_contradicts_nonzero_low_D','P_traps_original_Wp_cubic','V_triangular_graph_T_preserved_negative','no_cdf_or_source2_transfer']
def gitsha(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def validate_scope(scope):require(scope==SCOPE,'Incomplete source-specific proof scope')
def load_inputs():
 args=previous.load_inputs();snapshot=previous.build(*args);catalog=args[1]
 raw=(previous.ROOT/'frontier-through911.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PREVIOUS_SHA256 and json.loads(raw)==snapshot,'Pinned911 mismatch')
 raw=(ROOT/'source-pins-through917.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'917 manifest mismatch');pins=json.loads(raw)
 for p in pins.values():
  b=(ROOT/p['local_file']).read_bytes();require(gitsha(b)==p['git_blob_sha1'] and hashlib.sha256(b).hexdigest()==p['sha256'],'Pinned source changed')
 proof=(ROOT/pins['PROOF.md']['local_file']).read_text();review=(ROOT/pins['REVIEW.md']['local_file']).read_text()
 require(pins['PROOF.md']['commit']==COMMIT and pins['PROOF.md']['sha256'] in review and pins['verify.py']['sha256'] in review,'Proof/review binding mismatch')
 dep=pins['913_PROOF'];require(dep['commit'] in proof and dep['git_blob_sha1']=='ac36f048fc0987a1c78fbd9a61bc18077963ce20' and dep['git_blob_sha1'] in proof,'Missing exact913 low-row prerequisite')
 manifest=json.loads((ROOT/pins['audit-inputs/manifest.json']['local_file']).read_text())
 known={gitsha(p.read_bytes()):p for p in (previous.ROOT/'inputs').iterdir() if p.is_file()}
 known[dep['git_blob_sha1']]=ROOT/dep['local_file']
 require(len(manifest)==6,'Six dependency pins required')
 for p in manifest:require(p['git_blob'] in known,'Dependency absent from authenticated chain')
 return snapshot,catalog,pins

def build(snapshot,catalog,pins,scope=SCOPE,target=TUPLE):
 validate_scope(scope);require(target==TUPLE,'Only exact abcf source authorized')
 require(snapshot['checkpoint']=='whole-label-through911' and snapshot['remaining_label_count']==3 and snapshot['pair_accounting']['remaining_necessary_pairs']==146,'Wrong predecessor')
 rows=deepcopy(snapshot['records']);require(len(rows)==len(snapshot['remaining_ids'])==len(set(snapshot['remaining_ids']))==3 and {r['id'] for r in rows}==set(snapshot['remaining_ids']),'Label identities differ')
 for r in rows:require(len(r['remaining_source_pairs'])==len(set(map(tuple,r['remaining_source_pairs'])))==r['remaining_source_pair_count'],'Duplicate or inconsistent pairs')
 originals=json.loads((previous.ROOT/'inputs/original-one-one-pairs-db515250.json').read_text());orig=originals[127]
 frontier=json.loads((previous.ROOT/'inputs/pr842-original_frontier.json').read_text())['cases'];actual=[r for r in frontier if r['id']==LABEL];row=next(r for r in rows if r['id']==LABEL)
 require(len(actual)==1 and actual[0]['source_index']==127 and actual[0]['original_defect']==orig['defect']==0 and target in orig['compatible_E_types'],'Original identity/defect mismatch')
 for k,val in [('A',[[-8,'one'],[2,'one'],[16,'one']]),('B',[[-18,'one'],[-4,'one'],[6,'one']])]:require(accounting.canonical(orig[k])==accounting.canonical(actual[0][k])==accounting.canonical(row[k])==accounting.canonical(val),'Wrong endpoint')
 definition={'coefficients':target,'blocks':accounting.decode(target)};eid=accounting.identify(catalog,definition)
 require(all(len(p)==2 and all(type(x) is int for x in p) for r in rows for p in r['remaining_source_pairs']),'Invalid pair ID types')
 before={(r['id'],*p) for r in rows for p in r['remaining_source_pairs']};cut={(LABEL,*p) for p in row['remaining_source_pairs'] if p[0]==eid};require(len(cut)==32,'Expected exact32 unremoved pairs')
 after=before-cut;require(len(before)==146 and len(after)==114 and not after&cut and before==after|cut,'Pair partition invalid')
 for r in rows:
  old={tuple(p) for p in r['remaining_source_pairs']};kept={p for p in old if (r['id'],*p) not in cut};r.update(input_necessary_pair_count=len(old),remaining_source_pairs=sorted(map(list,kept)),remaining_source_pair_count=len(kept),removed_source_pairs=sorted(map(list,old-kept)),removed_pair_count=len(old-kept),relation_empty=not kept)
 require({r['id']:r['remaining_source_pair_count'] for r in rows}=={'G3.11.8ae96830fd21':4,LABEL:32,'G3.21.d610e381ed75':78},'Unaffected source counts changed')
 cdf=accounting.identify(catalog,{'coefficients':[0,0,1,1,0,1,0,0],'blocks':accounting.decode([0,0,1,1,0,1,0,0])})
 require({e for e,q in row['remaining_source_pairs']}=={cdf},'Separate cdf not preserved')
 residual=[]
 for r in rows:
  defs=[]
  for e in sorted({e for e,q in r['remaining_source_pairs']}):
   ds=[x for x in catalog if x['id']==e];require(len(ds)==1 and accounting.identify(catalog,ds[0])==e,'Residual source identity mismatch');d=ds[0];defs.append({'coefficients':d['coefficients'],'blocks':d['blocks'],'necessary_pair_count':sum(a==e for a,q in r['remaining_source_pairs'])})
  residual.append({'id':r['id'],'profile':r['profile'],'necessary_pair_count':r['remaining_source_pair_count'],'remaining_source_definitions':defs})
 base=json.loads((previous.ROOT/'frontier.json').read_text());basepairs={(r['id'],*p) for r in base['records'] for p in r['baseline_pairs']};require(before<=basepairs and after<=basepairs and len(basepairs)==1790,'Fixed baseline relation mismatch')
 return {'schema_version':1,'checkpoint':'source-through917','previous_checkpoint':{'file':'frontier-through911.json','sha256':PREVIOUS_SHA256,'publication_pr':912,'publication_commit':'37fc20f8f7db3d6375e6a5da2263d57d4ae6e301','necessary_pairs':146},'remaining_label_count':3,'remaining_ids':deepcopy(snapshot['remaining_ids']),'profile_counts':deepcopy(snapshot['profile_counts']),'pair_accounting':{'input_necessary_pairs':146,'additional_removed_pairs':32,'remaining_necessary_pairs':114},'new_full_label_exclusions':[],'new_source_edge_exclusion_ledger':[{'kind':'source_edge','pr':917,'proof_commit':COMMIT,'original_source_index':127,'label':LABEL,'source_definition':definition,'matched_local_E_id':eid,'removed_pairs':sorted([list(x[1:]) for x in cut]),'actual_additional_pair_count':32,'adjudicated_label_count_delta':0}],'records':rows,'residual_source_summary':residual,'boundary':deepcopy(snapshot['boundary']),'source_branch_coverage':scope,'source_pins':pins,'source_pins_sha256':PINS_SHA256,'fixed_campaign805_comparison':{'baseline_labels':17,'remaining_labels':3,'labels_removed':14,'baseline_necessary_pairs':1790,'remaining_necessary_pairs':114,'necessary_pairs_removed':1676},'scope':'Exact original source127 abcf only. No stable-label decrement, no cdf/source2 transfer, no actual-instance or formal-proof claim. Historical911 cutoff remains146.'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=build(*load_inputs());p=ROOT/'frontier-source-through917.json'
 if args.write:p.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==r,'Artifact differs from replay');print('PASS through917:3 labels (2/0/1),114 necessary pairs=4+32+78;32 exact abcf cuts,no label cut')
if __name__=='__main__':main()
