#!/usr/bin/env python3
"""Typed coverage integration. Does not certify any imported geometric theorem."""
from pathlib import Path
import copy,hashlib,json,re
ROOT=Path(__file__).resolve().parent
TUPLES={'D':[1,1,1,0,0,1,0,0],'P':[1,1,1,0,1,0,0,0],'V':[1,1,2,0,0,0,0,0],'Z':[1,2,1,0,0,0,0,0]}
PROOFS={'p':'d3e4714dc5808474ae664824c36a2d81975e29d40a6f2c99309542afdba8713a','vz':'b344bb861ac283d1f997de2ac7d281938913a4a9e471a0c7545e81ed2e6d8e61','d':'7a21b3efdd1326266623093f3b1d2c6f95c13027c73c8d3ccb005134b9ed443e','two':'fcc0f3479a921935e68738856bf50178bf91d822087f708ee1636f262c02e6ae','last':'590dfb8da397d866059bf341b66eca2c7e408819fbf3fa2d7257313ab1f5d619'}
PINNED={'inputs/actual-gauss.md': {'ref': 'db51525015bb7c5e825833d550d08dedf6f6ea96', 'path': 'research/hm/order-four-quadratic-load/POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md', 'sha256': '0928dd8261ac0d2659188af6520b564611b289cd0e271185ef5f4e3bafe3a6a2', 'git_blob_sha1': '303c6927265296440470b9dd4015fe6e8d55ca4d', 'bytes': 5414}, 'inputs/actual-splitting.md': {'ref': 'db51525015bb7c5e825833d550d08dedf6f6ea96', 'path': 'research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md', 'sha256': 'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256', 'git_blob_sha1': 'b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3', 'bytes': 9672}, 'inputs/pr1123-proof.md': {'ref': '504b7eb800407dfc7e6340c98c72cdd553939f54', 'path': 'research/hm/primary-terminal-slope-obstruction/PROOF.md', 'sha256': 'd5feb4b4478b5ec8178a049124179d25473b2e2526b20823a40f6dc60095e28e', 'git_blob_sha1': '43cc2fe6ac82d7cb01b8c32dc2ef906212c3b705', 'bytes': 9616}, 'inputs/profile11-pairs.json': {'ref': 'db51525015bb7c5e825833d550d08dedf6f6ea96', 'path': 'research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json', 'sha256': '6002ad138a41d98c351130a29703722979f31b8da90d7c75a120f28bf89480eb', 'git_blob_sha1': 'fe0afa410d89340d3082dc814277f89fbb582c19', 'bytes': 58635}, 'inputs/profile11-proof.md': {'ref': 'db51525015bb7c5e825833d550d08dedf6f6ea96', 'path': 'research/hm/order-four-quadratic-load/ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md', 'sha256': '8d3f7f9f0492484edc104cf070ed72be4b969545a1e4b184be37a00dc5e7cac0', 'git_blob_sha1': 'dcacf0bcdef8377c1ed7654e5b82659ea409456e', 'bytes': 8356}, 'inputs/strict-top.md': {'ref': 'db51525015bb7c5e825833d550d08dedf6f6ea96', 'path': 'research/hm/order-four-quadratic-load/NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md', 'sha256': '53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08', 'git_blob_sha1': 'd7506dae49b4be43230450c4132bd5db91f137ef', 'bytes': 4983}, 'inputs/p-PROOF.md': {'ref': '0dfc26b49b18fb60dce58e95f1d74c7d06d16378', 'path': 'research/hm/p-source-profile11-closure/PROOF.md', 'sha256': 'd3e4714dc5808474ae664824c36a2d81975e29d40a6f2c99309542afdba8713a', 'git_blob_sha1': '8ec40c1c02bb20d96282c5c88f0d8718da32f010', 'bytes': 9852}, 'inputs/p-RESULT.json': {'ref': '0dfc26b49b18fb60dce58e95f1d74c7d06d16378', 'path': 'research/hm/p-source-profile11-closure/RESULT.json', 'sha256': 'bf1474124d411dc5c417613bcb74932de0214b085551005b587d6c2e00bca997', 'git_blob_sha1': '641751c15d12217c78ebe6f121f0d20273577378', 'bytes': 202118}, 'inputs/vz-PROOF.md': {'ref': '49c8d0226a7e79928a016783553fa8c29c2c6b9a', 'path': 'research/hm/v-z-profile11-closure/PROOF.md', 'sha256': 'b344bb861ac283d1f997de2ac7d281938913a4a9e471a0c7545e81ed2e6d8e61', 'git_blob_sha1': 'd0df93a8cf6d74aa215b59643889e5a2078f51c2', 'bytes': 9746}, 'inputs/vz-RESULT.json': {'ref': '49c8d0226a7e79928a016783553fa8c29c2c6b9a', 'path': 'research/hm/v-z-profile11-closure/RESULT.json', 'sha256': 'c651d43d108b882267b9f749ed2c0b02f59837350a8026f2e9da81469b9dfca4', 'git_blob_sha1': '787d1361a735daaffa5d04be81c1397e1e9cca0a', 'bytes': 126853}, 'inputs/d-PROOF.md': {'ref': '54f5a5b76932e56714dfc74730e175271701dfc2', 'path': 'research/hm/d-source-profile11-frontier/PROOF.md', 'sha256': '7a21b3efdd1326266623093f3b1d2c6f95c13027c73c8d3ccb005134b9ed443e', 'git_blob_sha1': '0b8602c79942c71fecefa8442ff9bf04bccde9dc', 'bytes': 9642}, 'inputs/d-RESULT.json': {'ref': '54f5a5b76932e56714dfc74730e175271701dfc2', 'path': 'research/hm/d-source-profile11-frontier/RESULT.json', 'sha256': 'bd593940ff604883e2293f2609b04654050a70b0d7a26c36048ccbd93d6420f3', 'git_blob_sha1': 'c102745d9bcea1e8410fb71839f14c4097ba5d42', 'bytes': 255886}, 'inputs/two-PROOF.md': {'ref': 'd80532ed02932af6b3ea5fb0b159d985f98fdfba', 'path': 'research/hm/d-two-endpoint-exclusions/PROOF.md', 'sha256': 'fcc0f3479a921935e68738856bf50178bf91d822087f708ee1636f262c02e6ae', 'git_blob_sha1': '18e4c655daf492aeff7fe0e0d5646dbbddeab2e9', 'bytes': 12859}, 'inputs/two-RESULT.json': {'ref': 'd80532ed02932af6b3ea5fb0b159d985f98fdfba', 'path': 'research/hm/d-two-endpoint-exclusions/RESULT.json', 'sha256': '21b3e2fbd935ee1708326a39f443e3af4e6b359d65b52b259822e067c80b6ca4', 'git_blob_sha1': 'd8536e3c89e94a7b8e67c6cecc7caaa33a0fd63d', 'bytes': 500}, 'inputs/last-PROOF.md': {'ref': '06ad9fa84964e0c803a09106a581baeb46ee987d', 'path': 'research/hm/d-last-scalar-pair/PROOF.md', 'sha256': '590dfb8da397d866059bf341b66eca2c7e408819fbf3fa2d7257313ab1f5d619', 'git_blob_sha1': '565eca172dc411c8c2a5f2342773f863488f467f', 'bytes': 13351}, 'inputs/last-RESULT.json': {'ref': '06ad9fa84964e0c803a09106a581baeb46ee987d', 'path': 'research/hm/d-last-scalar-pair/RESULT.json', 'sha256': '6ae1126050a074efcc989a7b7536ca8bb230078f9ce9167e553144d75278d5ea', 'git_blob_sha1': '878183a1cf8fc0b4847f03818750a467ab5e66a9', 'bytes': 3178}}
checks=0
def need(ok,label):
 global checks
 checks+=1
 if not ok: raise ValueError(label)
def read(name): return json.loads((ROOT/name).read_text())
def partition(groups,want,label):
 flat=[i for group in groups.values() for i in group]
 need(len(flat)==len(set(flat)),label+' disjoint')
 need(set(flat)==set(want),label+' exhaustive')
def validate(c,manifest,require_public=False):
 need(c['profile']==[1,1] and c['maximal'] is True and c['actual'] is True and c['conditional_necessity'] is True,'actual maximal conditional scope')
 need(c['sources']==['D','P','V','Z'],'four sources exactly')
 need(c['source_exclusions']=={'P':'p-PROOF.md','V':'vz-PROOF.md','Z':'vz-PROOF.md'},'source closure coverage')
 need(c['D_frontier']==[32,50,52],'three exact D ordered pairs')
 need(c['pair_exclusions']=={'32':'two-PROOF.md','50':'last-PROOF.md','52':'two-PROOF.md'},'pair closure coverage')
 need(c['conclusion']=='no_actual_maximal_profile_11' and c['proof_assistant_verified'] is False,'no scope promotion')
 need(len(manifest)==16 and len({x['file'] for x in manifest})==16,'all sixteen distinct inputs')
 for x in manifest:
  need(x['file'] in PINNED and {k:x[k] for k in ['ref','path','sha256','git_blob_sha1','bytes']}==PINNED[x['file']],'exact immutable dependency lock')
  b=(ROOT/x['file']).read_bytes()
  need(len(b)==x['bytes'],'input size')
  need(hashlib.sha256(b).hexdigest()==x['sha256'],'input SHA256')
  need(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['git_blob_sha1'],'Git blob')
  if require_public: need(bool(x['ref'] and re.fullmatch('[0-9a-f]{40}',x['ref'])),'immutable public pin required')
  if x['ref']: need(x['url']=='https://github.com/Akilleez-QA/read-em-and-weep/blob/'+x['ref']+'/'+x['path'],'exact public URL')
 for k,h in PROOFS.items():
  need(hashlib.sha256((ROOT/('inputs/'+k+'-PROOF.md')).read_bytes()).hexdigest()==h,'accepted proof '+k)
 rows=read('inputs/profile11-pairs.json');need(len(rows)==159,'frozen necessary list size')
 need(set(c['pairs'])=={'32','50','52'},'pair signatures exhaustive')
 for i in [32,50,52]:
  need(c['pairs'][str(i)]=={k:rows[i][k] for k in ['A','B','defect']},'ordered pair signature '+str(i))
  need(TUPLES['D'] in rows[i]['compatible_E_types'],'D compatibility')
 p=read('inputs/p-RESULT.json');vz=read('inputs/vz-RESULT.json');d=read('inputs/d-RESULT.json')
 for s in ['P','V','Z']:
  expected=[i for i,r in enumerate(rows) if TUPLES[s] in r['compatible_E_types']]
  data=p if s=='P' else vz['sources'][s]
  actual=data['P_compatible_indices'] if s=='P' else data['compatible_indices']
  need(actual==expected,'original source membership '+s)
  partition(data['partition'],expected,s)
  if s!='P': need(data['survivors']==[],'empty source residual '+s)
 partition(d['summary'],range(159),'D all frozen records')
 need(d['summary']['remaining']==c['D_frontier'],'frontier connection')
 need(d['summary']['incompatible_D']==[i for i,r in enumerate(rows) if TUPLES['D'] not in r['compatible_E_types']],'original D compatibility complement')
 need(sum(len(v) for k,v in d['summary'].items() if k!='incompatible_D')==102,'D compatible count')
 return True

def main():
 c=read('COVERAGE.json'); m=read('INPUTS.json');validate(c,m,require_public=True)
 rejected=[]
 def reject(name,change):
  a,b=copy.deepcopy(c),copy.deepcopy(m);change(a,b)
  try:validate(a,b,require_public=True)
  except (ValueError,KeyError):rejected.append(name);return
  raise RuntimeError('accepted invalid mutation: '+name)
 for s in ['D','P','V','Z']:reject('remove source '+s,lambda a,b,s=s:a['sources'].remove(s))
 for s in ['P','V','Z']:reject('remove source exclusion '+s,lambda a,b,s=s:a['source_exclusions'].pop(s))
 for i in ['32','50','52']:
  reject('remove pair exclusion '+i,lambda a,b,i=i:a['pair_exclusions'].pop(i))
  reject('alter ordered B '+i,lambda a,b,i=i:a['pairs'][i]['B'].append([0,'one']))
  reject('alter defect '+i,lambda a,b,i=i:a['pairs'][i].__setitem__('defect',99))
 reject('replace V by duplicate P',lambda a,b:a['sources'].__setitem__(2,'P'))
 reject('swap pair proof',lambda a,b:a['pair_exclusions'].__setitem__('50','two-PROOF.md'))
 reject('drop maximality',lambda a,b:a.__setitem__('maximal',False))
 reject('claim global rank-three exclusion',lambda a,b:a.__setitem__('conclusion','no_rank_three'))
 reject('claim proof assistant',lambda a,b:a.__setitem__('proof_assistant_verified',True))
 reject('drop geometry premise',lambda a,b:a.__setitem__('conditional_necessity',False))
 for i in range(len(m)):
  reject('remove input '+str(i),lambda a,b,i=i:b.pop(i))
  reject('corrupt hash '+str(i),lambda a,b,i=i:b[i].__setitem__('sha256','0'*64))
  reject('wrong public pin '+str(i),lambda a,b,i=i:b[i].__setitem__('ref','f'*40))
  reject('missing public pin '+str(i),lambda a,b,i=i:b[i].__setitem__('ref',None))
 print(json.dumps({'checks':checks,'mutation_rejections':len(rejected),'mutations':rejected,'source_partition':['P excluded','V excluded','Z excluded','D implies 32/50/52'],'D_pair_partition':{'two':[32,52],'last':[50]},'result':'conditional maximal profile (1,1) closure coverage PASS','limitations':'Typed finite coverage and byte integrity only; imported geometry remains a mathematical premise; not Lean verification.'},indent=2,sort_keys=True))
if __name__=='__main__':main()
