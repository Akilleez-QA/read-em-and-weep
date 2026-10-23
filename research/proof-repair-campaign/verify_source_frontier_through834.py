#!/usr/bin/env python3
"""Complete-case O26 source accounting; no production proof or instance evaluation."""
import argparse
from copy import deepcopy
import hashlib
import json
import verify_source_frontier_through828 as previous
ROOT=previous.ROOT
require=previous.require
PREVIOUS_SHA256='22583c253816f9ef9e6a45a525dd10869870c45d1277fe184e102839e6a1755c'
PINS_SHA256='5864571b4b2d7d11438d2a135d35bb52018123fa3b0e90a8c07e2600a9580145'
D='G3.11.dc58cc54f352';W='G3.11.4b6dad66f329';T='G3.11.8ae96830fd21'
SOURCES={
 'E0':deepcopy(previous.prior.SOURCES['E0']),
 'E10':deepcopy(previous.prior.SOURCES['E10']),
 'E6':deepcopy(previous.prior.SOURCES['bf']),
 'U6':deepcopy(previous.SOURCES['ef']),
 'E3':deepcopy(previous.SOURCES['cf']),
 'U13':{'coefficients':[0,0,0,0,1,0,1,0],'blocks':[[-2,'P'],[-2,'P'],[-2,'D'],[-5,'Wp'],[-9,'W']]},
 'E12':{'coefficients':[0,0,1,0,0,0,1,0],'blocks':[[-2,'V'],[-2,'P'],[-2,'D'],[-4,'V'],[-9,'W']]},
 'E13':{'coefficients':[0,1,0,0,0,0,1,0],'blocks':[[-2,'P'],[-2,'D'],[-3,'T'],[-9,'W']]},
}
COVERAGE={
 'new829':{'mode':'all_divisors','cases':{'0':'PR829 Sections2-5','12':'PR829 Section2 excludes two-P injection into Sym16','20':'PR829 Section2 excludes two-P injection into Sym8'},'dependencies':['pr829']},
 'new834':{'mode':'all_divisors','cases':{'0':'PR834 Sections2-5','12':'PR813 Section3, reused explicitly in PR834 Section2','20':'PR813 Section7 top coefficient must be P+D, reused explicitly in PR834 Section2'},'dependencies':['pr813','pr834']},
 'old_E0_D':{'mode':'all_divisors','cases':{'0':'PR817 Section7 excludes E0 for dc58cc54f352 by the projected negative horizontal O(-8)','12':'PR813 excludes every delta12 source of all three labels','20':'PR813 Section7 permits only matching E6/E13 with top P+D, not E0 with top P+2D'},'dependencies':['pr813','pr817']},
 'old_E10_W':{'mode':'all_divisors','cases':{'0':'PR817 Section7 excludes E10 for 4b6dad66f329 by the projected negative horizontal O(-8)','12':'PR813 excludes every delta12 source of all three labels','20':'PR813 Section7 permits only matching E6/E13 with top P+D, not E10 with top P+2D'},'dependencies':['pr813','pr817']},
 'mismatch_E0_W':{'mode':'divisor_independent_quotient','argument':'PR817 Section7: only the single O(-10) source summand can map to W O(-9), so it cannot surject onto the rank-two negative quotient. This precedes the internal-image analysis and has no delta=0 premise.','dependencies':['pr817']},
 'mismatch_E6_W':{'mode':'divisor_independent_quotient','argument':'PR813 Section3: only the O(-10) summand of E6 can map to W O(-9), with image rank at most one. The same source/target degree mismatch holds independently of the top-system divisor; Section7 invokes it again.','dependencies':['pr813']},
}
def rule(label,source,coverage):return {'label':label,'source':source,'kind':'source_edge','coverage_certificate':coverage}
RULES=[rule(D,'U6','new829'),rule(W,'U6','new829'),rule(W,'U13','new829'),rule(D,'E3','new834'),rule(W,'E3','new834'),rule(W,'E12','new834'),rule(D,'E0','old_E0_D'),rule(W,'E10','old_E10_W'),rule(W,'E0','mismatch_E0_W'),rule(W,'E6','mismatch_E6_W')]
# Exact scope evidence is checked against the pinned bytes, not inferred from a frontier summary.
EVIDENCE={
 'pr813':['delta belongs to {0,12,20}.','delta=12 is impossible for every source of all three labels.',
 'delta=20 is possible only for the matching E6/E13 sources of the first two labels.',
 'The mismatch E6 for the W O(-9) quotient is impossible because only its O(-10) summand maps there, giving image rank at most one.'],
 'pr817':['For G3.11.dc58cc54f352 with E0','For G3.11.4b6dad66f329 with E10',
 'the same W-tail label cannot have source E0 even before the internal-image analysis: in E0 the only summand capable of mapping to W O(-9) is the single O(-10), so its image has rank at most one and cannot surject onto the rank-two negative quotient.']}

def validate_coverage(c,pins):
 for key,x in c.items():
  require(set(x['dependencies'])<=set(pins),'Missing pinned coverage dependency')
  if x['mode']=='all_divisors':require(set(x['cases'])=={'0','12','20'} and all(x['cases'].values()),'Incomplete divisor case coverage')
  else:require(x['mode']=='divisor_independent_quotient' and bool(x.get('argument')),'Conditional coverage cannot cut whole source')

def load_inputs():
 s,c,p=previous.load_inputs();snapshot=previous.build(s,c,p)
 raw=(ROOT/'frontier-source-through828.json').read_bytes()
 require(hashlib.sha256(raw).hexdigest()==PREVIOUS_SHA256 and json.loads(raw)==snapshot,'Through828 changed or replay mismatch')
 raw=(ROOT/'source-pins-source-through834.json').read_bytes()
 require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'Source manifest changed')
 pins=json.loads(raw)
 oldpins=json.loads((ROOT/'source-pins-source-through823.json').read_text())
 for key in ('pr813','pr817'):pins[key]=oldpins[key+'-proof.md']
 for key,x in pins.items():
  b=(ROOT/x['local_file']).read_bytes()
  require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['git_blob_sha1'],'Proof blob mismatch: '+key)
  for quote in EVIDENCE.get(key,[]):require(quote in b.decode(),'Pinned scope quotation missing: '+key)
 validate_coverage(COVERAGE,pins)
 return snapshot,c,pins

def intersect(snapshot,catalog,rules=RULES,coverage=COVERAGE):
 ids={name:previous.prior.identify(catalog,d) for name,d in SOURCES.items()}
 require(len({e['id'] for e in catalog})==len(catalog),'Duplicate catalog ID')
 rows={r['id']:r for r in snapshot['records']};require(set(rows)==set(snapshot['remaining_ids']) and len(rows)==len(snapshot['records']),'Stable ID mismatch')
 relations={}
 for label,r in rows.items():
  require(r['profile']==label.split('.')[1],'Profile mismatch')
  pairs={tuple(p) for p in r['remaining_source_pairs']}
  require(len(pairs)==len(r['remaining_source_pairs'])==r['remaining_source_pair_count'],'Duplicate pair or count mismatch')
  require(all(e in {x['id'] for x in catalog} for e,q in pairs),'Unknown source reference')
  relations[label]=pairs
 original=deepcopy(relations);ledger=[];seen=set()
 for r in rules:
  require(r['kind']=='source_edge','Not a source-edge rule')
  cov=coverage[r['coverage_certificate']]
  if cov['mode']=='all_divisors':require(set(cov['cases'])=={'0','12','20'},'Incomplete divisor case coverage')
  else:require(cov['mode']=='divisor_independent_quotient' and cov.get('argument'),'Conditional cut')
  label=r['label'];key=(label,previous.prior.canonical(SOURCES[r['source']]['blocks']))
  require(key not in seen,'Double source exclusion');seen.add(key)
  eid=ids[r['source']];removed={p for p in relations[label] if p[0]==eid};relations[label]-=removed
  ledger.append(dict(r,source_definition=SOURCES[r['source']],matched_local_E_id=eid,removed_pairs=sorted(map(list,removed)),actual_additional_pair_count=len(removed),already_absent_in_input=not bool(removed),label_count_delta=0))
 records=[]
 for label in sorted(rows):
  kept=relations[label];removed=original[label]-kept
  require(not kept&removed and kept|removed==original[label],'Pair partition mismatch')
  records.append({'id':label,'profile':rows[label]['profile'],'A':rows[label]['A'],'B':rows[label]['B'],'input_necessary_pair_count':len(original[label]),'removed_pair_count':len(removed),'remaining_source_pair_count':len(kept),'remaining_source_pairs':sorted(map(list,kept)),'removed_source_pairs':sorted(map(list,removed))})
 return records,ledger,ids

def build(snapshot,catalog,pins):
 validate_coverage(COVERAGE,pins)
 records,ledger,sourceids=intersect(snapshot,catalog)
 ids=sorted(r['id'] for r in records if r['remaining_source_pair_count'])
 require(ids==snapshot['remaining_ids'] and len(ids)==9,'Unexpected empty relation; no whole-label theorem inferred')
 require([x['actual_additional_pair_count'] for x in ledger]==[3]*10,'Per-edge accounting mismatch')
 require(sum(r['remaining_source_pair_count'] for r in records)==810,'Tuple total mismatch')
 singletons={D:('E6',[0,20],3),W:('E13',[0,20],3),T:('E10',[0],4)}
 for label,(name,divisors,count) in singletons.items():
  r=next(r for r in records if r['id']==label)
  require({e for e,q in r['remaining_source_pairs']}=={sourceids[name]} and r['remaining_source_pair_count']==count,'O26 singleton mismatch')
 return {'schema_version':1,'checkpoint':'source-strata-through834','not_proof_completion':True,'geometric_constraints_fully_encoded':False,
 'scope':'PR829 and PR834 complete source cuts plus explicitly case-completed older PR813/817 exclusions and divisor-independent W-tail mismatch cuts. No whole-label exclusion.',
 'previous_checkpoint':{'file':'frontier-source-through828.json','sha256':PREVIOUS_SHA256,'publication_commit':'226a27bf255cbeea3c3d057bf111fcf90597b7d1','necessary_pairs':840},
 'remaining_label_count':9,'remaining_ids':ids,'remaining_profile_counts':{'11':8,'12':0,'21':1},'new_full_label_exclusions':[],
 'new_source_edge_exclusion_ledger':ledger,'coverage_certificates':COVERAGE,'checked_scope_quotations':EVIDENCE,
 'pair_accounting':{'input_necessary_pairs':840,'pr829_additional_pairs_removed':9,'pr834_additional_pairs_removed':9,'older_complete_coverage_pairs_removed':12,'additional_removed_pairs':30,'remaining_necessary_pairs':810,'historical_through806_pairs':1004,'cumulative_source_pair_cuts':194},
 'o26_remaining':{label:{'source_name':name,'source_definition':SOURCES[name],'remaining_necessary_pairs':n,'possible_top_divisor_degrees':divs,'realizability_asserted':False} for label,(name,divs,n) in singletons.items()},
 'source_definitions':SOURCES,'source_pins':pins,'new_source_pins_sha256':PINS_SHA256,
 'deferred_branch_restrictions':[{'publication':'PR830','commit':'620d5598ccc19e5e1c458a4cddb0d3a0709d83c3','scope':'Reported split-bf rank-two exclusion only; rank-one remains. Not fetched or encoded in this checkpoint.','action':'No whole-source deletion.'},{'publication':'PR836 and later','action':'Not fetched or encoded; checkpoint bounded at PR834.'}],
 'catalog_reference':snapshot['catalog_reference'],'matching_rule':snapshot['matching_rule'],'proof_boundary':snapshot['proof_boundary'],
 'records':records}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args()
 result=build(*load_inputs());p=ROOT/'frontier-source-through834.json'
 if a.write:p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==result,'Artifact differs from replay')
 print(json.dumps({'status':'PASS','labels':9,'profiles':result['remaining_profile_counts'],'remaining_necessary_pairs':810,'additional_cuts':30,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()},sort_keys=True))
if __name__=='__main__':main()
