#!/usr/bin/env python3
"""Finite accounting certificate conditional on the pinned written exhaustion theorem."""
import argparse, hashlib, json, re
from copy import deepcopy
import verify_source_frontier_through839 as previous
ROOT=previous.ROOT
require=previous.require
BALANCED=previous.BALANCED
COMMIT='101a101234f3464f5d07a15669e4805cc46de3a7'
PREVIOUS_SHA256='daf5e3724ce2086d559da081155166680ed5024cf865a04d03650c96df9722e2'
PINS_SHA256='6a87c1a9ff54191435393ad6215f5f0f6e990a3e5342216ab54d86986067d180'
BRANCHES={
'ff':['strict_top_D_multiplicity'], 'ee':['strict_top_P_multiplicity'], 'cc':['strict_top_V_multiplicity'],
'ef':['zero_top_impossible','rank_one_dimension_bound','rank_two_forced_onto','pr814_polar'],
'ce':['zero_top_impossible','rank_one_dimension_bound','rank_two_forced_onto','pr814_polar'],
'be':['zero_top_impossible','rank_one_dimension_bound','rank_two_forced_onto','pr814_polar'],
'cf':['zero_top_impossible','rank_one_dimension_bound','rank_two_forced_onto','pr814_actual_subsystem','pr828_horizontal_lattice'],
'bf':['zero_top_impossible','rank_one_dimension_bound','rank_two_forced_onto','pr814_zero_internal','pr819_all_nonzero_internal','pr823_actual_quotient_descent'],
'bc':['zero_top_impossible','rank_two_forced_onto_pr814','rank_one_lower_T_zero_pr839','rank_one_lower_T_nonzero_full_image_pr839','rank_one_lower_T_nonzero_Euler_P_nonzero_pr839','rank_one_lower_T_nonzero_Euler_P_zero_scalar_zero_pr839','rank_one_lower_T_nonzero_Euler_P_zero_scalar_nonzero_defect12_pr839','pr823_actual_quotient_descent'],
'bb':['zero_top_impossible','rank_one_pr814','rank_two_onto_nine_dimensional_pr836','rank_two_onto_twelve_dimensional_pr836','rank_two_nononto_only_defect12_pr819','rank_two_defect12_pr838','pr823_actual_quotient_descent']}
DIMS={'one':1,'V':3,'P':4,'D':5,'T':6,'Wp':2}
def decode(t):
 a,b,c,d,e,f,g,h=t
 require(a==d==g==0 and h==1 and b+c+e+f==2,'Not an original balanced tuple')
 return [[-2,'V']]*c+[[-2,'P']]*(e+1)+[[-2,'D']]*f+[[-3,'T']]*b+[[-4,'V']]*c+[[-5,'Wp']]*e+[[-8,'one']]*f+[[-10,'one']]
def validate_branches(branches):
 require(branches==BRANCHES,'Incomplete or changed branch coverage')
def load_inputs():
 s,c,p,o=previous.load_inputs();snapshot=previous.build(s,c,p,o)
 raw=(ROOT/'frontier-source-through839.json').read_bytes()
 require(hashlib.sha256(raw).hexdigest()==PREVIOUS_SHA256 and json.loads(raw)==snapshot,'Through839 changed')
 raw=(ROOT/'source-pins-through842.json').read_bytes()
 require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'Manifest changed')
 pins=json.loads(raw)
 for k,pin in pins.items():
  b=(ROOT/pin['local_file']).read_bytes()
  require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==pin['git_blob_sha1'],'Pinned blob changed: '+k)
 proof=(ROOT/pins['proof']['local_file']).read_text();review=(ROOT/pins['review']['local_file']).read_text()
 require(hashlib.sha256(proof.encode()).hexdigest()=='f55f5a6f1c06b0fd80db3a571f0ede56337100cd8d646a60f6cee0db768f8934','Reviewed proof mismatch')
 require(hashlib.sha256(proof.encode()).hexdigest() in review,'Review does not bind proof')
 frontier=json.loads((ROOT/pins['original_frontier']['local_file']).read_text())
 target=[r for r in frontier['cases'] if r['id']==BALANCED]
 require(len(target)==1,'Stable label not unique')
 r=target[0]
 require(r['profile']=='11' and r['original_defect']==0 and r['source_index']==72 and previous.canonical(r['A'])==previous.canonical(o['A']) and previous.canonical(r['B'])==previous.canonical(o['B']),'Original stable label mismatch')
 return snapshot,c,o,pins,proof

def exhaustion(original,catalog,proof,branches=BRANCHES):
 validate_branches(branches)
 parsed=[(name,[int(v) for v in t.split(',')]) for name,t in re.findall(r'^\d+\. (\w+) = \(([0-9,]+)\)',proof,re.M)]
 require(len(parsed)==10 and [t for n,t in parsed]==original['compatible_E_types'],'Proof differs from exact original ten tuples')
 require(len({tuple(t) for n,t in parsed})==10 and {n for n,t in parsed}==set(BRANCHES),'Duplicate tuple or source name')
 out=[]
 for name,t in parsed:
  blocks=decode(t);eid=previous.identify(catalog,{'coefficients':t,'blocks':blocks})
  require(sum(DIMS[r] for d,r in blocks)==17 and sum(d*DIMS[r] for d,r in blocks)==-54,'Universal source rank/degree mismatch')
  out.append({'source_name':name,'multiplicity_tuple':t,'blocks':blocks,'matched_local_E_id':eid,'branch_coverage':branches[name],'rank':17,'degree':-54,'new_pair_cuts':0})
 return out

def build(snapshot,catalog,original,pins,proof):
 coverage=exhaustion(original,catalog,proof)
 require(snapshot['whole_label_gate']['status']=='held_closed','Predecessor gate changed')
 ids=snapshot['registered_ids'];require(len(set(ids))==len(ids)==9 and BALANCED in ids,'Duplicate or missing registered ID')
 rows=snapshot['records'];require(len(rows)==9 and {r['id'] for r in rows}==set(ids),'Stable records mismatch')
 removed=next(r for r in rows if r['id']==BALANCED)
 require(removed['remaining_source_pairs']==[] and removed['remaining_source_pair_count']==0,'Cannot recount existing source pairs as label cut')
 records=deepcopy([r for r in rows if r['id']!=BALANCED]);remaining=sorted(set(ids)-{BALANCED})
 counts={p:sum(r['profile']==p for r in records) for p in ['11','12','21']}
 require(counts=={'11':7,'12':0,'21':1} and sum(r['remaining_source_pair_count'] for r in records)==759,'Accounting mismatch')
 return {'schema_version':1,'checkpoint':'whole-label-through842','previous_checkpoint':{'file':'frontier-source-through839.json','sha256':PREVIOUS_SHA256,'registered_labels':9,'necessary_pairs':759,'gate':'held_closed'},'remaining_label_count':8,'remaining_ids':remaining,'profile_counts':counts,'new_full_label_exclusion_ledger':[{'id':BALANCED,'kind':'whole_label','proof_commit':COMMIT,'original_source_index':72,'original_defect':0,'complete_original_tuple_count':10,'actual_additional_pair_count':0}],'new_source_edge_exclusions':[],'pair_accounting':{'input_necessary_pairs':759,'additional_removed_pairs':0,'remaining_necessary_pairs':759},'whole_label_gate':{'status':'discharged_by_pinned_written_exhaustion','original_ten_tuple_catalog_independently_verified':True,'immutable_full_exhaustion_publication_verified':True,'publication_commit':COMMIT},'original_ten_tuple_exhaustion':coverage,'source_pins':pins,'source_pins_sha256':PINS_SHA256,'records':records,'split_residual':deepcopy(snapshot['split_residual']),'boundary':{'formal_lean_proof':False,'global_completion':False,'source2_closed':False,'realization_count':False,'geometric_constraints_fully_encoded':False,'meaning':'Finite replay verifies identity, exact tuple and branch accounting against immutable written mathematical inputs; it does not formalize their geometric proofs or assert surviving witnesses are realizable.'}}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();result=build(*load_inputs());p=ROOT/'frontier-through842.json'
 if a.write:p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==result,'Artifact differs from replay')
 print(json.dumps({'status':'PASS','labels':8,'profiles':result['profile_counts'],'necessary_pairs':759,'additional_pair_cuts':0,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()},sort_keys=True))
if __name__=='__main__':main()
