#!/usr/bin/env python3
"""Proof-chain integration only; no actual coefficients or instance ranks."""
from pathlib import Path
from copy import deepcopy
import hashlib,json,os,subprocess,sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'dependencies'
LOW=BASE/'lower-exclusion';ONE=BASE/'rankone'
checks=0
def require(ok,msg):
 global checks
 checks+=1
 if not ok:raise RuntimeError(msg)
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
MANIFESTS={
 'lower-exclusion':'3fc3e1f1d66993ae92c59c3790565ff1bf871192c31961fcdf9776168dcb6e5b',
 'rankone':'7f54078b1620316bfc7f1675533c3a364632280a121868d58ad5f75e126e2701'}
PROOFS={
 'lower-exclusion/cubic-image/PROOF.md':'0e291e31481530df3163ed6abc3d433a4e402c98e9258d3a329b05b51a2ea507',
 'lower-exclusion/lower-image/PROOF.md':'f6f807996ccca5b05233af8964bbbaa4f3913f79e4955ea2b4906462db3f2751',
 'lower-exclusion/PROOF.md':'4cbd25f10abfdc864687e71f44cd17de7589d3d031d1035849737487b9f3adb1',
 'rankone/PROOF.md':'0ac173c28a40d6f98df75ae7218fe0fc8a7c03a4e0c3b022f87a97969a403cd8'}
CHECKERS={
 'lower-exclusion/cubic-image/verify.py':'6d4f66ca5ac1be539a09ef791775e782bc4cafba56dbf18131b0bb7586a21242',
 'lower-exclusion/lower-image/verify.py':'8bfaf601c8817fb0ab3af19a5aff734efdad09a318491c1bec7d8430818cb0f6',
 'lower-exclusion/verify.py':'44d793fa6972371e3870f3e682fb468292189b9d16a9db135b75f7b58c73ea39',
 'rankone/verify.py':'4164413cea33bbae469763460aa83e82c3a21e36e4dca92d3b66869e5456d01f'}
DAG={
 'originals':[],
 'cubic_image':['originals'],
 'lower_classification':['originals'],
 'lower_exclusion':['cubic_image','lower_classification'],
 'rankone':['originals','lower_classification'],
 'integration':['cubic_image','lower_exclusion','rankone']}
def acyclic(graph):
 visiting=set();done=set()
 def visit(n):
  if n in visiting:raise RuntimeError('circular proof dependency')
  if n in done:return
  if n not in graph:raise RuntimeError('unretained proof dependency')
  visiting.add(n)
  for d in graph[n]:visit(d)
  visiting.remove(n);done.add(n)
 for n in graph:visit(n)
 return sorted(done)
def authenticate():
 files=[]
 for name,pin in MANIFESTS.items():
  root=BASE/name;require(sha(root/'MANIFEST.json')==pin,'immutable package manifest '+name)
  m=read(root/'MANIFEST.json');items=m['files']if isinstance(m,dict)else m
  for x in items:
   rel=x.get('file',x.get('path'));p=root/rel
   require(p.is_file()and p.stat().st_size==x['bytes'],'full dependency bytes '+name+'/'+rel)
   require(sha(p)==x['sha256'],'full dependency hash '+name+'/'+rel)
   files.append(name+'/'+rel)
 for file,pin in {**PROOFS,**CHECKERS}.items():require(sha(BASE/file)==pin,'explicit proof/checker pin '+file)
 sources={}
 for folder in (LOW/'cubic-image',LOW/'lower-image',ONE/'dependency'):
  for item in read(folder/'INPUTS.json'):
   raw=(folder/item['file']).read_bytes();name=Path(item['file']).name
   require(hashlib.sha256(raw).hexdigest()==item['sha256'],'full original SHA '+name)
   require(len(raw)==item['bytes'],'full original bytes '+name)
   require(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==item['git_blob_sha1'],'full original Git blob '+name)
   identity={k:item[k]for k in('sha256','bytes','ref','path','url','git_blob_sha1')}
   if name in sources:require(sources[name]['identity']==identity,'same original and immutable commit '+name)
   else:sources[name]={'identity':identity,'copies':[]}
   sources[name]['copies'].append(str((folder/item['file']).relative_to(ROOT)))
 require(len(sources)==6,'exactly six common complete original premises')
 require(sum(len(x['copies'])for x in sources.values())==17,'all five-plus-six-plus-six original copies checked')
 require(len(acyclic(DAG))==6,'complete acyclic theorem graph')
 return files,sources

def replay(path,snapshot):
 cmd=[sys.executable]+(['-O']if sys.flags.optimize else [])+[str(path)]
 p=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
 require(p.returncode==0,'dependency execution: '+str(path.relative_to(ROOT))+': '+p.stderr[-200:])
 data=json.loads(p.stdout);require(data==read(snapshot),'byte-data equivalent dependency replay '+str(path.relative_to(ROOT)))
 return data

def contract_from(cubic,lower,rankone):
 require(cubic['actual_Qstar3_Euler']=={'W':-2,'S4':-1,'T6':1},'positive actual T6 Euler coefficient')
 require(cubic['actual_E3_Euler']=={"W'":1,'T6':2},'unequal actual primal cubic Euler retained')
 require(cubic['plateau_ranks']==[5,9,13,17,21],'ordered actual plateau stages')
 require(cubic['rank_four_images_remaining']==0,'rank-four image theorem exhausted its domain')
 require(lower['image_quotient_pairs_excluded']==13 and lower['torsion_partitions_excluded']==96,'rank-two/rank-three actual classification exhausted')
 require(lower['positive_case_rows_excluded']==37 and lower['positive_torsion_partitions_excluded']==83,'positive lower-image defects retained')
 require(rankone['counts']==[53,16,7,9],'complete rank-one domain and two branches')
 require(all(x['survivors']==0 for x in rankone['low_exclusions']),'every low rank-one endpoint eliminated')
 require(all(x['V_margin']==1 for x in rankone['upper_exclusions']),'every upper rank-one physical V obstruction')
 require(any(r['defects'][2]==12 for x in rankone['low_exclusions']for r in x['defect_rows']),'positive last defect retained before low contradiction')
 require(cubic['canonical_single_T6_assumed']==False,'first image theorem does not require canonical T6')
 require(cubic['source_Z_assumed']==False,'l1 does not force source Z')
 require(lower['global_zero_plateau_defects_assumed']==False and cubic['globally_zero_defects_assumed']==False,'no global zero-defect premise')
 require(lower['H1_vanishing_assumed']==False,'upper cohomology preserves H1')
 require(lower['inverse_image_extension_splitting_assumed']==False,'inverse-image extensions not assumed split')
 require(rankone['complete_profile_claim']==False,'rank-one packet does not import integration conclusion')
 return {'actual_ranks':[17,13,30],'physical_A':'Sym2 W','physical_V':'other even three-space',
  'chosen_section_copy_exists':True,'one_fixed_copy':True,'canonical_or_unique_copy_assumed':False,
  'evaluation_bundle_injectivity_assumed':False,'image_nonzero':True,'full_derivative_generic_rank':4,
  'rank_exclusions':{'1':'rankone','2':'lower_exclusion','3':'lower_exclusion','4':'cubic_image'},
  'source_Z_forced':False,'global_zero_defects_assumed':False,'premises_retained':True,
  'claims_generic_SF_at_least_five':False,'claims_square_surjectivity':False}

def validate_contract(c,graph):
 require(c['actual_ranks']==[17,13,30],'actual unequal ranks contract')
 require(c['physical_A']=='Sym2 W'and c['physical_V']=='other even three-space','fixed physical marking contract')
 require(c['chosen_section_copy_exists']and c['one_fixed_copy'],'same existing section copy throughout all branches')
 require(not c['canonical_or_unique_copy_assumed']and not c['evaluation_bundle_injectivity_assumed'],'no extra section-copy assumptions')
 require(c['image_nonzero']and c['full_derivative_generic_rank']==4,'complete nonzero image rank interval')
 require(set(c['rank_exclusions'])=={'1','2','3','4'},'all four and only four image ranks covered')
 require(c['rank_exclusions']=={'1':'rankone','2':'lower_exclusion','3':'lower_exclusion','4':'cubic_image'},'correct branch theorem for each rank')
 require(not c['source_Z_forced']and not c['global_zero_defects_assumed'],'no accidental source or defect specialization')
 require(c['premises_retained'],'original necessity and geometric premises not discharged')
 require(not c['claims_generic_SF_at_least_five']and not c['claims_square_surjectivity'],'scope does not overclaim stronger global conclusions')
 acyclic(graph)
 return []
def mutate(c,g,label):
 if label=='omit-rank-one':del c['rank_exclusions']['1']
 elif label=='omit-rank-four':del c['rank_exclusions']['4']
 elif label=='lower-image-full-annihilator':c['rank_exclusions']['2']='cubic_image'
 elif label=='allow-zero-image':c['image_nonzero']=False
 elif label=='change-copy-between-branches':c['one_fixed_copy']=False
 elif label=='assume-canonical-copy':c['canonical_or_unique_copy_assumed']=True
 elif label=='assume-evaluation-injective':c['evaluation_bundle_injectivity_assumed']=True
 elif label=='swap-unequal-bundles':c['actual_ranks']=[13,17,30]
 elif label=='swap-physical-A-V':c['physical_A'],c['physical_V']=c['physical_V'],c['physical_A']
 elif label=='force-source-Z':c['source_Z_forced']=True
 elif label=='global-zero-defects':c['global_zero_defects_assumed']=True
 elif label=='circular-rankone-proof':g['rankone'].append('integration')
 elif label=='claim-SF-five':c['claims_generic_SF_at_least_five']=True
 else:raise RuntimeError('unknown executable mutation')

def derive():
 files,sources=authenticate()
 contract_only='--contract-only'in sys.argv
 lower=read(LOW/'RESULT.json')if contract_only else replay(LOW/'verify.py',LOW/'RESULT.json')
 rankone=read(ONE/'RESULT.json')if contract_only else replay(ONE/'verify.py',ONE/'RESULT.json')
 cubic=read(LOW/'cubic-image'/'RESULT.json')
 c=contract_from(cubic,lower,rankone);graph=deepcopy(DAG)
 if '--mutation'in sys.argv:mutate(c,graph,sys.argv[sys.argv.index('--mutation')+1])
 remaining=validate_contract(c,graph)
 return {'status':'CONDITIONAL PASS','claim':'The actual ordered maximal rank-four plateau (3,1) is excluded under the retained original premises.',
  'profile':[3,1],'generic_SF_rank_under_contradiction':4,'excluded_image_ranks':[1,2,3,4],
  'remaining_image_ranks':remaining,'contract':c,'proof_dependency_graph':graph,
  'source_identities':sources,'authenticated_dependency_files':len(files),
  'lower_exclusion_reported_checks':lower['total_checks'],
  'rankone_reported_checks':rankone['new_checks']+rankone['dependency_checks'],
  'shared_dependency_checks_not_deduplicated':True,'integration_checks':checks,
  'actual_instance_evaluation_used':False,'historical_enumeration_used':False,
  'coarse_profile_count_updated':False,'independent_final_chain_review_required':True}
if __name__=='__main__':print(json.dumps(derive(),indent=2,sort_keys=True))
