#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,subprocess,sys,os
R=Path(__file__).resolve().parent;A=R.parents[1]
def require(ok,msg):
 if not ok:raise RuntimeError(msg)
manifest=json.loads((A/'MANIFEST.json').read_text())
for item in manifest['files']:
 raw=(A/item['file']).read_bytes()
 require(len(raw)==item['bytes']and hashlib.sha256(raw).hexdigest()==item['sha256'],'frozen author manifest '+item['file'])
for flags in([],['-O']):
 p=subprocess.run([sys.executable,*flags,str(A/'verify.py')],capture_output=True,cwd='/tmp',env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
 require(p.returncode==0 and p.stdout==(A/'RESULT.json').read_bytes(),'author complete normal/optimized integration replay')
p=subprocess.run([sys.executable,str(A/'test_controls.py')],capture_output=True,cwd='/tmp')
require(p.returncode==0 and p.stdout==(A/'CONTROLS.json').read_bytes(),'thirteen executed author contract mutations')
a=json.loads((A/'RESULT.json').read_text());b=json.loads((R/'RESULT.json').read_text())
require(a['integration_checks']==221 and a['lower_exclusion_reported_checks']==16582 and a['rankone_reported_checks']==4207,'final stage check counts retained without claiming deduplication')
require(a['excluded_image_ranks']==b['excluded_restricted_image_ranks']==[1,2,3,4]and a['remaining_image_ranks']==b['remaining_restricted_image_ranks']==[],'exhaustive rank partition')
require(a['profile']==b['profile_excluded']==[3,1]and a['contract']['actual_ranks']==b['actual_ranks']==[17,13,30],'same ordered profile and unequal bundles')
require(a['contract']['one_fixed_copy']and not a['contract']['canonical_or_unique_copy_assumed']and not a['contract']['evaluation_bundle_injectivity_assumed'],'one arbitrary fixed section-copy contract')
require(not a['coarse_profile_count_updated']and not a['contract']['claims_generic_SF_at_least_five'],'exact one-profile scope')
source_names=set();copies=0
for folder in (A/'dependencies/lower-exclusion/cubic-image',A/'dependencies/lower-exclusion/lower-image',A/'dependencies/rankone/dependency'):
 for x in json.loads((folder/'INPUTS.json').read_text()):
  name=Path(x['file']).name;source_names.add(name);copies+=1
  require((folder/x['file']).read_bytes()==(R/'inputs'/name).read_bytes(),'all full original copies match independently reviewed originals')
require(len(source_names)==6 and copies==17,'six complete originals across seventeen copies')
paths={'cubic-image':'dependencies/lower-exclusion/cubic-image','lower-classification':'dependencies/lower-exclusion/lower-image','lower-exclusion':'dependencies/lower-exclusion','rankone':'dependencies/rankone'}
for tag,folder in paths.items():
 for n in ('PROOF.md','verify.py','RESULT.json'):
  require((A/folder/n).read_bytes()==(R/'inputs'/(tag+'-'+n)).read_bytes(),'all four constituent theorem bytes match independent acceptance pins')
print(json.dumps({'status':'CONDITIONAL PASS','author_integration_checks':221,'author_dependency_stage_checks':[16582,4207],'shared_checks_not_claimed_disjoint':True,'independent_integration_checks':b['checks'],'author_files_authenticated':len(manifest['files']),'author_normal_and_optimized_replay':True,'author_mutations_executed':13,'complete_originals':6,'identical_original_copies':17,'four_constituent_theorems_match_independent_acceptance':True,'same_fixed_T6_copy':True,'exhaustive_rank_partition':[1,2,3,4],'author_hashes':{n:hashlib.sha256((A/n).read_bytes()).hexdigest()for n in ['PROOF.md','verify.py','RESULT.json','MANIFEST.json']}},indent=2,sort_keys=True))
