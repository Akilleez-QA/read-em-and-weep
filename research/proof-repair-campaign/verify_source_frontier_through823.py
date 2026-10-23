#!/usr/bin/env python3
"""Narrow source-stratum integration; no new whole-label exclusion or experiment."""
import argparse
from copy import deepcopy
import hashlib
import json
import verify_frontier_through806 as prior
ROOT=prior.ROOT
require=prior.require
HISTORICAL_SHA256='4100c591275feae312a0182511337cf4b4131901730932366bbe68ea3dcf9bbc'
PINS_SHA256='781d6cf48f3ab957540da61b7da9ef7729884c0197f0f689f763af66c79243d3'
O26='G3.11.8ae96830fd21'
BALANCED='G3.11.73682b4c817f'
SOURCES={
 'E0':{'coefficients':[0,0,0,0,0,2,0,1],'blocks':[[-2,'P'],[-2,'D'],[-2,'D'],[-8,'one'],[-8,'one'],[-10,'one']]},
 'E10':{'coefficients':[0,0,0,0,0,1,1,0],'blocks':[[-2,'P'],[-2,'D'],[-2,'D'],[-8,'one'],[-9,'W']]},
 'E18':{'coefficients':[1,0,1,0,0,2,0,0],'blocks':[[-2,'D'],[-2,'D'],[-3,'Wp'],[-4,'V'],[-8,'one'],[-8,'one']]},
 'bf':{'coefficients':[0,1,0,0,0,1,0,1],'blocks':[[-2,'P'],[-2,'D'],[-3,'T'],[-8,'one'],[-10,'one']]},
}
RULES=[
 {'rule':'o26_E0','label':O26,'source':'E0','kind':'source_edge','coverage':'all_divisor_strata','dependencies':['pr813-proof.md','pr817-proof.md']},
 {'rule':'o26_E18','label':O26,'source':'E18','kind':'source_edge','coverage':'all_divisor_strata','dependencies':['pr813-proof.md','pr822-proof.md']},
 {'rule':'balanced_bf','label':BALANCED,'source':'bf','kind':'source_edge','coverage':'all_internal_J_cases','dependencies':['pr814-proof.md','pr819-bf-subsystem.md','pr823-BF-THIRD-BACKWARD-QUOTIENT.md','pr823-BF-FINITE-BACKWARD-DESCENT.md']},
]
UNENCODED=[
 {'source':'pr813-proof.md','scope':'Other O26 labels G3.11.dc58cc54f352 and G3.11.4b6dad66f329','condition':'delta=12 excluded; delta=20 forces a matching degree-ten subsystem; delta=0 not decided by PR813','action':'No broad source-edge deletion; the old pair schema has no divisor coordinate.'},
 {'source':'pr817-proof.md','scope':'Other O26 E0/E10 source strata','condition':'Basepoint-free delta=0 hypotheses required','action':'Not promoted to an all-divisor cut here.'},
 {'source':'pr814-proof.md','scope':'bc source in low-positive split/balanced labels','condition':'Rank-two top branch excluded, rank-one branch not eliminated by that assertion','action':'No whole-source deletion.'},
 {'source':'pr814-proof.md','scope':'cf and split-ce sources','condition':'Forced constant subsystems, not source exclusions','action':'No source-edge deletion.'},
 {'source':'pr819-cubic.md','scope':'Balanced bb source','condition':'Generic rank two and non-onto top image forces a length-twelve cubic Wp subsystem','action':'No source-edge deletion; no assertion about onto branch.'},
 {'source':'pr821-proof.md','scope':'bb source in split/balanced labels','condition':'Onto top branch has two possible constant spans; split torsion branch impossible, balanced torsion retains separate cubic branch','action':'No whole-source deletion or realization inference.'},
 {'source':'pr814-proof.md','scope':'Other complete ef/be exclusions in both low-positive labels and balanced ce','condition':'These are full-source exclusions, not merely conditional, but outside this narrowly requested integration','action':'Explicitly deferred; this checkpoint is not a complete all-publications source frontier.'},
]

def load_inputs():
 snapshot=prior.build(*prior.load_inputs())
 raw=(ROOT/'frontier-through806.json').read_bytes()
 require(hashlib.sha256(raw).hexdigest()==HISTORICAL_SHA256,'Historical through806 changed')
 require(json.loads(raw)==snapshot,'Historical through806 replay mismatch')
 raw=(ROOT/'source-pins-source-through823.json').read_bytes()
 require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'Source pin manifest changed')
 pins=json.loads(raw)
 for key,p in pins.items():
  b=(ROOT/p['local_file']).read_bytes()
  require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==p['git_blob_sha1'],'Proof Git blob mismatch: '+key)
 catalog=json.loads((ROOT/'inputs/pr796-same-source-witness-intersection.json').read_text())['E_catalog']
 return snapshot,catalog,pins

def canonical(blocks):return tuple(sorted(tuple(b) for b in blocks))
def identify(catalog,definition):
 by_blocks=[e for e in catalog if canonical(e['blocks'])==canonical(definition['blocks'])]
 by_tuple=[e for e in catalog if e['coefficients']==definition['coefficients']]
 require(len(by_blocks)==len(by_tuple)==1 and by_blocks[0]['id']==by_tuple[0]['id'],'Block/tuple mismatch or ambiguous source')
 return by_blocks[0]['id']

def intersect(snapshot,catalog,rules=RULES):
 require(len({e['id'] for e in catalog})==len(catalog),'Duplicate catalog ID')
 ids={name:identify(catalog,s) for name,s in SOURCES.items()}
 rows={r['id']:r for r in snapshot['records']}
 require(len(rows)==len(snapshot['records']) and set(rows)==set(snapshot['remaining_ids']),'Stable ID coverage mismatch')
 catalog_ids={e['id'] for e in catalog}
 relations={}
 for label,r in rows.items():
  require(r['profile']==prior.prior.historical.profile(label),'Profile mismatch')
  pairs={tuple(p) for p in r['baseline_pairs']}
  require(len(pairs)==len(r['baseline_pairs'])==r['baseline_pair_count'],'Duplicate pair or count mismatch')
  require(all(e in catalog_ids for e,q in pairs),'Unknown source reference')
  relations[label]=pairs
 require({e for e,q in relations[O26]}<={ids[s] for s in ('E0','E10','E18')},'O26 source outside theorem overlist')
 before=deepcopy(relations);ledger=[];seen=set()
 for rule in rules:
  require(rule['kind']=='source_edge','Wrong cut kind')
  require(rule['coverage'] in ('all_divisor_strata','all_internal_J_cases'),'Conditional cut cannot remove a whole source edge')
  label=rule['label'];key=(label,canonical(SOURCES[rule['source']]['blocks']))
  require(key not in seen,'Double source exclusion');seen.add(key)
  eid=ids[rule['source']]
  cut={p for p in relations[label] if p[0]==eid};relations[label]-=cut
  ledger.append(dict(rule,source_definition=deepcopy(SOURCES[rule['source']]),
    matched_local_E_id=eid,removed_pairs=sorted(map(list,cut)),
    actual_additional_pair_count=len(cut),already_absent_in_input=not bool(cut),label_count_delta=0))
 records=[]
 for label in sorted(rows):
  kept=relations[label];removed=before[label]-kept
  require(kept.isdisjoint(removed) and kept|removed==before[label],'Pair partition mismatch')
  records.append({'id':label,'profile':rows[label]['profile'],'A':rows[label]['A'],'B':rows[label]['B'],
   'input_baseline_pair_count':len(before[label]),'removed_pair_count':len(removed),
   'remaining_source_pair_count':len(kept),'remaining_source_pairs':sorted(map(list,kept)),
   'removed_source_pairs':sorted(map(list,removed))})
 return records,ledger,ids

def build(snapshot,catalog,pins):
 records,ledger,ids=intersect(snapshot,catalog)
 remaining=sorted(r['id'] for r in records if r['remaining_source_pair_count'])
 require(remaining==snapshot['remaining_ids'],'Unexpected empty source relation: do not infer a geometric full-label exclusion')
 require(len(remaining)==9 and prior.prior.historical.counts(remaining)=={'11':8,'12':0,'21':1},'Profile accounting mismatch')
 require([x['actual_additional_pair_count'] for x in ledger]==[4,4,16],'Unexpected source-edge accounting')
 total=sum(r['remaining_source_pair_count'] for r in records)
 require(total==980 and sum(r['input_baseline_pair_count'] for r in records)==1004,'Tuple accounting mismatch')
 target=next(r for r in records if r['id']==O26)
 require({e for e,q in target['remaining_source_pairs']}=={ids['E10']} and target['remaining_source_pair_count']==4,'O26 singleton mismatch')
 return {
  'schema_version':1,'checkpoint':'source-strata-through823-narrow','not_proof_completion':True,'geometric_constraints_fully_encoded':False,
  'scope':'Only all-divisor E0/E18 cuts on G3.11.8ae96830fd21 and complete bf cut on G3.11.73682b4c817f. Other source results are explicitly not integrated.',
  'historical_checkpoint':{'file':'frontier-through806.json','sha256':HISTORICAL_SHA256,'labels':9,'baseline_pairs':1004},
  'remaining_label_count':9,'remaining_ids':remaining,'remaining_profile_counts':{'11':8,'12':0,'21':1},
  'new_full_label_exclusions':[],'new_source_edge_exclusion_ledger':ledger,
  'pair_accounting':{'input_historical_pairs':1004,'additional_removed_pairs':24,'already_absent_target_edges':0,'remaining_necessary_pairs':980},
  'coverage_certificate':{
   O26:{'complete_source_overlist':['E0','E10','E18'],'divisor_alternatives':[0,12,20],
    'delta12':'PR813 excludes all source types','delta20':'PR813 excludes this label; only matching sources on two other labels may survive',
    'delta0_E0':'PR817 Section6 excludes','delta0_E18':'PR822 excludes','remaining_source':'E10','remaining_is_realizable':False},
   BALANCED:{'source':'bf','top_rank_two':'PR814 Section2 or PR819 Section1 forces rank two and onto for top P+D',
    'J_alternatives':['zero','O(-10)'],'J_zero':'PR814 Section5 excludes',
    'J_nonzero':'PR819 supplies quartic subsystem; PR823 third-backward and finite descent exclude',
    'PR823_alone_is_full_source_exclusion':False}},
  'unencoded_or_deferred_results':UNENCODED,
  'matching_rule':'Match complete degree/irreducible block multisets AND source multiplicity tuples. Local E IDs are only references. Filter existing correlated pairs; never complete a Cartesian product.',
  'source_definitions':SOURCES,'source_pins':pins,'source_pins_sha256':PINS_SHA256,
  'catalog_reference':'inputs/pr796-same-source-witness-intersection.json: E_catalog and Q_catalog',
  'proof_boundary':'Pinned written mathematical conclusions are assumptions of this finite accounting verifier. No actual-source evaluations, proof review, old experiment, realization or global theorem is performed or inferred.',
  'records':records}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 result=build(*load_inputs());p=ROOT/'frontier-source-through823.json'
 if args.write:p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==result,'Artifact differs from deterministic replay')
 print(json.dumps({'status':'PASS','labels':9,'profiles':result['remaining_profile_counts'],'remaining_necessary_pairs':980,'new_pair_cuts':24,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()},sort_keys=True))
if __name__=='__main__':main()
