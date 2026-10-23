#!/usr/bin/env python3
"""Original ten-tuple label gate, with no second charge for prior source cuts."""
import argparse,hashlib,json
from copy import deepcopy
import verify_source_frontier_through882 as previous
ROOT=previous.ROOT;require=previous.require;accounting=previous.accounting
PREVIOUS_SHA256='c1e76e7f91e0eb5ff8f6b33c25427ad51693802d5aa771735a94627498f02740'
PINS_SHA256='df74df2b255751b87e9ff6729093de0a13f52bc4ffd0689c7d43b868fe5e969a'
LABEL='G3.11.ad509d55173f';COMMIT='75d3a9bb5287ddc3dc22bf4651602b257d6507fb'
NAMES=['ff','ef','ee','cf','ce','cc','bf','be','bc','bb']
SOURCES={'ff':848,'ef':846,'ee':None,'cf':868,'ce':846,'cc':None,'bf':881,'be':846,'bc':874,'bb':877}
FILES={'PR846.md':'inputs/pr846-proof.md','PR848-FF.md':'inputs/pr848_proof.md','PR868-CF.md':'inputs/pr868_proof.md','PR874-BC.md':'inputs/pr874_proof.md','PR877-BB.md':'inputs/pr877_proof.md','PR861-CF-REDUCTION.md':'inputs/pr861_proof.md','PR881-BF.md':'inputs/pr881_proof.md'}
SCOPE={'ff':'PR848 entire index113 ff; not conditional index127 scalar branch','ef':'PR846 section3 no divisor; both kernels, all0/W7/O8 internal images, both channel-row cases','ee':'strict_top_P_multiplicity3_gt2','cf':'PR861 divisor0 plus PR868 divisor12; actual intersections and proven doubledivisor saturation','ce':'PR846 section5 no divisor; both kernels internalzero; rank11 quadratic gap','cc':'strict_top_V_multiplicity2_gt1','bf':'PR881 both divisors, five kernels, all internal images, C7/C9/C12/C8, saturation before dual','be':'PR846 section4 no divisor; both kernels internalzero','bc':'PR874 both divisors, complete kernels, changed tail, proven saturation','bb':'PR877 both divisors, five kernels, all images, both extensions, proven saturation'}
def sym(n):
 names=['one','W','A','S','D','T','V','P','Wp'];edges=[('one','W'),('W','A'),('A','S'),('S','D'),('D','T'),('T','V'),('T','P'),('P','Wp')]
 old={k:0 for k in names};cur=dict(old);cur['one']=1
 for _ in range(n):
  nxt={k:-old[k] for k in names}
  for x,y in edges:nxt[x]+=cur[y];nxt[y]+=cur[x]
  old,cur=cur,nxt
 return cur

def load_inputs():
 s,c,p=previous.load_inputs();snapshot=previous.build(s,c,p)
 raw=(ROOT/'frontier-source-through882.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PREVIOUS_SHA256 and json.loads(raw)==snapshot,'Through882 changed')
 raw=(ROOT/'source-pins-through884.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PINS_SHA256,'Gate manifest changed');pins=json.loads(raw)
 for pin in pins.values():
  b=(ROOT/pin['local_file']).read_bytes();require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==pin['git_blob_sha1'],'Gate input changed')
 review=(ROOT/pins['REVIEW.md']['local_file']).read_text()
 for key in ['PROOF.md','coverage.json','source-proof-pins.json']:require(hashlib.sha256((ROOT/pins[key]['local_file']).read_bytes()).hexdigest() in review,'Gate review binding mismatch')
 coverage=json.loads((ROOT/pins['coverage.json']['local_file']).read_text());sourcepins=json.loads((ROOT/pins['source-proof-pins.json']['local_file']).read_text())
 require(set(sourcepins)==set(FILES),'Missing theorem dependency')
 for k,local in FILES.items():
  b=(ROOT/local).read_bytes();require(hashlib.sha256(b).hexdigest()==sourcepins[k]['sha256'] and hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sourcepins[k]['git_blob'],'Exact source theorem mismatch')
 return snapshot,c,pins,coverage,sourcepins

def coverage_report(coverage,sourcepins,scope=SCOPE):
 require(scope==SCOPE,'Incomplete original branch coverage')
 require(coverage['stable_label']==LABEL and coverage['source_index']==113 and coverage['original_commit']=='db51525015bb7c5e825833d550d08dedf6f6ea96','Gate scope changed')
 original=json.loads((ROOT/'inputs/original-one-one-pairs-db515250.json').read_text())[113];frontier=json.loads((ROOT/'inputs/pr842-original_frontier.json').read_text())['cases'];matches=[r for r in frontier if r['id']==LABEL]
 require(len(matches)==1 and matches[0]['source_index']==113 and matches[0]['original_defect']==original['defect']==0,'Original identity mismatch')
 for k,v in [('A',[[-10,'one'],[2,'one'],[16,'one']]),('B',[[-18,'one'],[-4,'one'],[8,'one']])]:require(original[k]==matches[0][k]==v,'Original endpoints changed')
 rows=coverage['coverage'];require([r['name'] for r in rows]==NAMES and [r['tuple'] for r in rows]==original['compatible_E_types'] and len({tuple(r['tuple']) for r in rows})==10,'Not the complete original ordered ten tuples')
 target={k:sym(4)[k]+sym(18)[k] for k in sym(4)};require({k:v for k,v in target.items() if v}=={'A':1,'V':1,'P':2,'D':2},'Strict-top target mismatch')
 result=[]
 for r in rows:
  a,b,c,d,e,f,g,h=r['tuple'];require((a,d,g,h)==(0,0,0,1) and b+c+e+f==2 and r['name']=='b'*b+'c'*c+'e'*e+'f'*f,'Tuple/name mismatch')
  if SOURCES[r['name']] is None:
   require(r['kind']=='strict_top','Direct case replaced');top={'V':c+g+h-1,'P':d+e+g+h,'D':f+g};require(any(top[k]>target[k] for k in top),'No strict-top obstruction')
  else:
   require(r['kind']=='whole_source' and r['pr']==SOURCES[r['name']],'Wrong source lemma')
   require(r['url']=='https://github.com/Akilleez-QA/read-em-and-weep/blob/'+r['commit']+'/'+r['path'] and r['url'] in {p['url'] for p in sourcepins.values()},'Theorem pin not authenticated')
  result.append(dict(r,source_definition={'coefficients':r['tuple'],'blocks':accounting.decode(r['tuple'])},complete_scope=scope[r['name']]))
 dependency='https://github.com/Akilleez-QA/read-em-and-weep/blob/7b5b3371a82cb92f46ea60895e45617d0891a5b0/research/hm/profile11-source113-cf-reduction/PROOF.md'
 require(sourcepins['PR861-CF-REDUCTION.md']['url']==dependency and dependency in (ROOT/'inputs/pr868_proof.md').read_text(),'Missing complete cf dependency')
 return result

def build(snapshot,catalog,pins,coverage,sourcepins):
 report=coverage_report(coverage,sourcepins);rows=snapshot['records'];ids=snapshot['remaining_ids'];require(len(rows)==len(set(ids))==5 and {r['id'] for r in rows}==set(ids),'Input identity mismatch')
 row=next(r for r in rows if r['id']==LABEL);require(row['remaining_source_pairs']==[] and row['remaining_source_pair_count']==0,'Gate cannot silently remove unaccounted pairs')
 kept=deepcopy([r for r in rows if r['id']!=LABEL]);counts={p:sum(r['profile']==p for r in kept) for p in ['11','12','21']}
 require(counts=={'11':3,'12':0,'21':1} and sum(r['remaining_source_pair_count'] for r in kept)==351,'Final accounting mismatch')
 return {'schema_version':1,'checkpoint':'whole-label-through884','previous_checkpoint':{'file':'frontier-source-through882.json','sha256':PREVIOUS_SHA256,'necessary_pairs':351},'remaining_label_count':4,'remaining_ids':sorted(r['id'] for r in kept),'profile_counts':counts,'new_full_label_exclusion_ledger':[{'kind':'whole_label','id':LABEL,'original_source_index':113,'proof_commit':COMMIT,'complete_original_source_count':10,'removed_pairs':[],'actual_additional_pair_count':0}],'new_source_edge_exclusions':[],'pair_accounting':{'input_necessary_pairs':351,'additional_removed_pairs':0,'remaining_necessary_pairs':351,'counting_rule':'All index113 pairs were already charged to source-edge stages; close only the original-ten-tuple label gate.'},'complete_original_source_coverage':report,'source_theorem_pins':sourcepins,'source_pins':pins,'source_pins_sha256':PINS_SHA256,'records':kept,'boundary':deepcopy(snapshot['boundary']),'scope':'Only index113 label gate closes. Source2, index125, index127 and8ae are untouched. No Lean or actual-instance claim.'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();result=build(*load_inputs());p=ROOT/'frontier-through884.json'
 if args.write:p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==result,'Artifact differs from replay');print('PASS through884: 4 labels (3/0/1), 351 necessary pairs unchanged, original ten-source gate closed')
if __name__=='__main__':main()
