import json,hashlib,argparse
from pathlib import Path
from copy import deepcopy
ROOT=Path(__file__).resolve().parent
MANIFEST_SHA256='20d4bd14e769540c62926d90924ac97697c08b89946e81e1b97491f506fdb262'
LABEL='G3.21.d610e381ed75'
TUPLE=[0,1,0,0,0,0,1,0]
EB=[[-9,'W'],[-3,'T'],[-2,'P'],[-2,'D']]
QB=[[-2,'P'],[-2,'D'],[-6,'A'],[-18,'one']]
DIMS={'one':1,'W':2,'Wp':2,'A':3,'V':3,'P':4,'S':4,'D':5,'T':6}
GATES=['same_actual_E_ann_Qstar','actual_source2_without_tuple_restriction','constant_first_block','all_endpoint_and_coupling_classes','actual_kernel_extension','equivariant_H1_O1_zero','equivariant_H1_O12_zero','not_horizontal_residual_split']
def req(b,m):
 if not b:raise ValueError(m)
def canon(b):return sorted(tuple(x) for x in b)
def stats(b):return sum(DIMS[r] for d,r in b),sum(d*DIMS[r] for d,r in b)
def load():
 raw=(ROOT/'manifest.json').read_bytes();req(hashlib.sha256(raw).hexdigest()==MANIFEST_SHA256,'manifest changed');manifest=json.loads(raw)
 for name,entry in manifest.items():
  b=(ROOT/'inputs'/name).read_bytes();req(hashlib.sha256(b).hexdigest()==entry['sha256'],'input changed '+name)
  req(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==entry['git_blob'],'git blob changed')
 req(manifest['through917.json']['sha256']=='486c673e7ddb1c0b427f4a819abd1b4854d775d1bbc1a90a3859574cd6995496','wrong predecessor')
 return tuple(json.loads((ROOT/'inputs'/n).read_text()) for n in ['through917.json','catalog796.json','original_frontier.json'])
def build(s,c,o,gates=GATES,eb=EB,qb=QB):
 req(gates==GATES,'incomplete geometric gates');req(canon(eb)==canon(EB) and canon(qb)==canon(QB),'wrong forced bundle orientation')
 req(stats(eb)==(17,-54) and stats(qb)==(13,-54),'bundle rank or degree')
 req(s['checkpoint']=='source-through917' and s['pair_accounting']['remaining_necessary_pairs']==114,'wrong snapshot')
 source=[r for r in o['cases'] if r['id']==LABEL];req(len(source)==1 and source[0]['source_index']==2 and source[0]['profile']=='21','wrong source identity')
 rows=deepcopy(s['records']);req(len(rows)==3 and len({r['id'] for r in rows})==3,'wrong labels')
 row=next(r for r in rows if r['id']==LABEL)
 for k,v in [('A',[[-8,'one'],[2,'one'],[16,'one']]),('B',[[-18,'one'],[-4,'one'],[6,'one']])]:req(canon(row[k])==canon(source[0][k])==canon(v),'endpoint mismatch')
 es=[r for r in c['E_catalog'] if canon(r['blocks'])==canon(eb)]
 req(len(es)==1 and es[0]['coefficients']==TUPLE,'unique E matching failed');eid=es[0]['id']
 req(len({r['id'] for r in c['E_catalog']})==len(c['E_catalog']),'duplicate E ids')
 qs=[i for i,b in enumerate(c['Q_catalog']) if canon(b)==canon(qb)];req(len(qs)==1,'unique Q matching failed');qid=qs[0]
 for r in rows:
  req(r['input_necessary_pair_count']==r['remaining_source_pair_count']+r['removed_pair_count'] and len(r['removed_source_pairs'])==r['removed_pair_count'],'row partition metadata mismatch')
  p=r['remaining_source_pairs'];req(all(len(x)==2 and all(type(v) is int for v in x) for x in p),'invalid pair')
  req(len(p)==len(set(map(tuple,p)))==r['remaining_source_pair_count'],'duplicate or inconsistent pairs')
  req(all(e in {z['id'] for z in c['E_catalog']} and 0<=q<len(c['Q_catalog']) for e,q in p),'unknown pair index')
 before={(r['id'],*p) for r in rows for p in r['remaining_source_pairs']};rp=set(map(tuple,row['remaining_source_pairs']))
 req(len(before)==114 and len(rp)==78 and len({e for e,q in rp})==13 and len({q for e,q in rp})==6,'wrong source counts')
 req(rp=={(e,q) for e in {e for e,q in rp} for q in {q for e,q in rp}},'source relation not rectangular')
 req((eid,qid) in rp,'forced pair missing')
 cutE={p for p in rp if p[0]!=eid};cutQ={p for p in rp if p[0]==eid and p[1]!=qid}
 req(len(cutE)==72 and len(cutQ)==5 and not cutE&cutQ,'incorrect partition')
 cut={(LABEL,*p) for p in cutE|cutQ};after=before-cut
 req(len(after)==37 and before==after|cut and not after&cut,'partition failed')
 row.update(input_necessary_pair_count=78,remaining_source_pairs=[[eid,qid]],remaining_source_pair_count=1,removed_source_pairs=sorted(map(list,cutE|cutQ)),removed_pair_count=77,relation_empty=False)
 req({r['id']:r['remaining_source_pair_count'] for r in rows}=={LABEL:1,'G3.11.8ae96830fd21':4,'G3.11.cce6e3ba4eeb':32},'unrelated counts changed')
 return {'kind':'overdue_structural_specialization_not_new_geometric_exclusion','remaining_label_count':3,'profile_counts':{'11':2,'12':0,'21':1},'pair_accounting':{'before':114,'removed':77,'after':37},'source2':{'id':LABEL,'E_tuple':TUPLE,'E_blocks':eb,'Qstar_blocks':qb,'matched_pair':[eid,qid],'E_mismatch_removed':sorted(map(list,cutE)),'Qstar_mismatch_removed':sorted(map(list,cutQ))},'records':rows,'gates':gates,'source2_excluded':False,'actual_instance_evaluated':False,'complete_proof':False}
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--write',action='store_true');args=a.parse_args();r=build(*load());p=ROOT/'specialization.json'
 if args.write:p.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
 req(json.loads(p.read_text())==r,'replay differs');print('PASS: source2 78→1, exact72+5 cut; total114→37; three labels remain')
