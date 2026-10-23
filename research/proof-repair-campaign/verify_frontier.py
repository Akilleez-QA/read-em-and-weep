#!/usr/bin/env python3
"""Deterministic frontier intersection only. No geometric/source-instance experiments."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INPUT_SHA256 = {
 'quotient-frontier-23.json': 'f0f6a9cf30cb5314ae6ccf06c613096ce69c0f9c851fe7104a37b908cf7d8015',
 'pr796-same-source-witness-intersection.json': '7c085250359b5445e8ef8da3f35763d495d5319660ca34c63aaf447078658bd5',
 'pr796-pinned-quadratic-block-proof.md': '622763aac375db7e17bc7cab472f1afda0477b0f769371a3b3ef845cd5c9e3b1',
 'pr798-proof.md': '4ddb4c7993039cf0e4504c2cd7403b45925a508a6489cc366ac9892ba39f53e0',
 'pr799-proof.md': '3a55f2c37548c7b05bf0f39f775ab37807c9f852d3601f77271fc0dd052022ed',
 'pr800-proof.md': 'f300e8ee2f36b85d1698b89f1150f20e6842bae925866c75506c340d78a4044d',
}
LABEL_CUTS = [
 {'source':'pr796','kind':'full_label','ids':['G3.12.34bc2083d563']},
 {'source':'pr798','kind':'full_label','ids':['G3.12.37914c53373c','G3.12.eed6acb13f3e']},
 {'source':'pr799','kind':'full_label','ids':['G3.11.003c6b04f1cc']},
 {'source':'pr800','kind':'full_label','ids':['G3.11.18ad6075be86','G3.11.86279023dea2']},
]
SPLIT=[[-2,'P'],[-2,'D'],[-3,'T'],[-8,'one'],[-10,'one']]
WTAIL=[[-2,'P'],[-2,'D'],[-3,'T'],[-9,'W']]
ALLOWED={'G3.12.37914c53373c':[SPLIT], 'G3.12.eed6acb13f3e':[SPLIT,WTAIL]}

def require(ok, message):
 if not ok: raise ValueError(message)
def canonical(blocks): return tuple(sorted(tuple(b) for b in blocks))
def profile(identifier):
 parts=identifier.split('.')
 require(len(parts)==3 and parts[0]=='G3' and parts[1] in ('11','12','21'),'Invalid stable ID')
 return parts[1]
def counts(ids):
 c=Counter(map(profile,ids));return {p:c[p] for p in ('11','12','21')}
def pair_set(pairs):
 out={tuple(p) for p in pairs}
 require(len(out)==len(pairs),'Duplicate source pair')
 return out

def apply_label_cuts(ids, cuts):
 require(len(ids)==len(set(ids)),'Duplicate baseline ID')
 alive=set(ids);seen=set();ledger=[]
 for cut in cuts:
  require(cut['kind']=='full_label','Source-edge cuts cannot be counted as labels')
  removed=set(cut['ids'])
  require(len(removed)==len(cut['ids']),'Duplicate ID inside cut')
  require(not seen & removed,'Double label exclusion')
  require(removed <= alive,'Unknown or previously excluded ID')
  before=len(alive);alive-=removed;seen|=removed
  ledger.append(dict(cut,removed_label_count=len(removed),before_label_count=before,
                     after_label_count=len(alive),after_profile_counts=counts(alive)))
 return sorted(alive),ledger

def load_inputs():
 for name,sha in INPUT_SHA256.items():
  require(hashlib.sha256((ROOT/'inputs'/name).read_bytes()).hexdigest()==sha,'Input hash mismatch: '+name)
 pins=json.loads((ROOT/'source-pins.json').read_text())
 for name,pin in pins.items():
  b=(ROOT/pin['local_file']).read_bytes()
  require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==pin['git_blob_sha1'],'Git blob mismatch: '+name)
 return (json.loads((ROOT/'inputs/quotient-frontier-23.json').read_text()),
         json.loads((ROOT/'inputs/pr796-same-source-witness-intersection.json').read_text()),pins)

def build(base, prior, pins):
 ids=base['remaining_ids']
 require(len(ids)==base['remaining_count']==23,'Baseline count mismatch')
 require(counts(ids)==base['profiles']=={'11':19,'12':3,'21':1},'Baseline profile mismatch')
 require(set(base['new_excluded_ids']).isdisjoint(ids),'Inherited cut reintroduced')
 remaining,ledger=apply_label_cuts(ids,LABEL_CUTS)
 require(len(remaining)==17 and counts(remaining)=={'11':16,'12':0,'21':1},'Current profile mismatch')
 rows={r['id']:r for r in prior['records']}
 require(len(rows)==len(prior['records'])==23 and set(rows)==set(ids),'Stable ID coverage mismatch')
 catalog={e['id']:canonical(e['blocks']) for e in prior['E_catalog']}
 require(len(catalog)==len(prior['E_catalog'])==28,'E catalog collision')
 qcount=len(prior['Q_catalog']);edge_ledger=[];baseline_count=0;prior_count=0
 for identifier,r in rows.items():
  require(r['profile']==profile(identifier),'Record profile mismatch')
  kept=pair_set(r['remaining_source_pairs']);removed=pair_set(r['removed_source_pairs'])
  require(kept.isdisjoint(removed),'Pair retained and removed')
  require(len(kept)==r['remaining_count'] and len(removed)==r['removed_count'],'Pair count mismatch')
  original=kept|removed
  require(len(original)==r['input_count'],'Input pair accounting mismatch')
  require(all(e in catalog and 0<=q<qcount for e,q in original),'Unknown source catalog reference')
  permitted={canonical(b) for b in ALLOWED.get(identifier,[])}
  expected={p for p in original if identifier != LABEL_CUTS[0]['ids'][0] and
            (identifier not in ALLOWED or catalog[p[0]] in permitted)}
  require(kept==expected,'PR796 full-block intersection mismatch')
  baseline_count+=len(original);prior_count+=len(kept)
  if identifier in ALLOWED:
   edge_ledger.append({'source':'pr796','kind':'source_edge','id':identifier,
    'removed_pairs':sorted(map(list,removed)),'removed_pair_count':len(removed),
    'label_count_delta':0,'later_full_label_exclusion':'pr798'})
 require((baseline_count,prior_count)==(2138,1996),'Pinned pair totals mismatch')
 require(sum(x['removed_pair_count'] for x in edge_ledger)==64,'Source-edge subtotal mismatch')
 require(prior['remaining_ids']==sorted(i for i,r in rows.items() if r['remaining_count']),'Prior surviving ID mismatch')
 current_records=[{'id':i,'profile':rows[i]['profile'],'A':rows[i]['A'],'B':rows[i]['B'],
    'baseline_pairs':rows[i]['remaining_source_pairs'],'baseline_pair_count':rows[i]['remaining_count']}
    for i in remaining]
 tuple_count=sum(r['baseline_pair_count'] for r in current_records)
 require(tuple_count==1790,'Current baseline tuple mismatch')
 subsequent=[]
 for cut in LABEL_CUTS[1:]:
  subsequent.append({'source':cut['source'],'kind':'full_label','ids':cut['ids'],
   'removed_pr796_baseline_pairs':sum(rows[i]['remaining_count'] for i in cut['ids'])})
 require(sum(c['removed_pr796_baseline_pairs'] for c in subsequent)==206,'Post-PR796 partition mismatch')
 return {'schema_version':1,'scope':'Executable campaign planning dependency: exact stable-label frontier and intersection with the pinned prior necessary pair relation. Written geometric theorems are assumptions, not machine-certified here.',
  'not_proof_completion':True,'geometric_constraints_fully_encoded':False,
  'baseline_label_count':23,'remaining_label_count':17,'remaining_ids':remaining,
  'remaining_profile_counts':counts(remaining),'full_label_exclusion_ledger':ledger,
  'source_edge_exclusion_ledger':edge_ledger,
  'inherited_exclusions_not_recounted':base['new_excluded_ids'],
  'pair_accounting':{'prior_23_label_relation':2138,'pr796_full_label_pairs_removed':78,
   'pr796_source_edge_pairs_removed':64,'pr796_22_label_relation':1996,
   'subsequent_full_label_pairs_removed':206,'current17_baseline_relation':tuple_count},
  'subsequent_pair_removal_ledger':subsequent,
  'pair_boundary':'1,790 is exactly the existing PR796 necessary relation restricted to current17 stable IDs. Newer geometry on surviving source edges is not asserted encoded; these are not realizations or an actual-instance rank result.',
  'input_sha256':INPUT_SHA256,'source_pins':pins,
  'upstream_dependency_hashes_not_rerun':prior['upstream_input_sha256'],
  'catalog_reference':'inputs/pr796-same-source-witness-intersection.json: E_catalog and Q_catalog; E numbers are local references, not stable mathematical IDs.',
  'records':current_records}

def main():
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args()
 result=build(*load_inputs());dest=ROOT/'frontier.json'
 if args.write: dest.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 require(json.loads(dest.read_text())==result,'frontier.json differs from deterministic replay')
 print(json.dumps({'status':'PASS','labels':17,'profiles':result['remaining_profile_counts'],
  'baseline_pairs':1790,'frontier_sha256':hashlib.sha256(dest.read_bytes()).hexdigest()},sort_keys=True))
if __name__=='__main__':main()
