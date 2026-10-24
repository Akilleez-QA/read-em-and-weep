#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,subprocess,sys
R=Path(__file__).resolve().parent;A=R.parents[1]/'dependencies/lower-exclusion'
def require(ok,msg):
 if not ok:raise RuntimeError(msg)
manifest=json.loads((A/'MANIFEST.json').read_text())
for item in manifest['files']:
 raw=(A/item['file']).read_bytes()
 require(len(raw)==item['bytes']and hashlib.sha256(raw).hexdigest()==item['sha256'],'frozen author manifest '+item['file'])
for flags in([],['-O']):
 p=subprocess.run([sys.executable,*flags,str(A/'verify.py')],capture_output=True,cwd='/tmp')
 require(p.returncode==0 and p.stdout==(A/'RESULT.json').read_bytes(),'author normal/optimized frozen replay')
a=json.loads((A/'RESULT.json').read_text());b=json.loads((R/'RESULT.json').read_text())
def shape(s):return tuple(sorted((x['degree'],x['coefficient'])for x in s))
aa={(shape(x['image']),shape(x['kernel']),shape(x['quotient'])):x for x in a['obstructions']}
bb={(shape(x['image']),shape(x['N']),shape(x['B'])):x for x in b['cases']}
require(len(aa)==13 and set(aa)==set(bb),'all thirteen actual image/kernel/quotient cases agree')
for key,x in aa.items():
 y=bb[key]
 require(x['upper_endpoint_Euler4']==y['chi_Z4'],'full upper-endpoint Euler character agrees')
 require(x['derivative_target_H0']==y['H0_B_dual'],'full derivative target character agrees')
 require(x['physical_V_excess']==y['V_kernel_lower_bound']==1,'exact reported physical V excess agrees')
 require(y['V_Euler_multiplicity']==y['chi_Z4'].get('V',0),'reported source multiplicity matches character')
 require(y['V_target_multiplicity']==y['H0_B_dual'].get('V',0),'reported target multiplicity matches character')
 obs={n:x['upper_endpoint_Euler4'].get(n,0)-x['derivative_target_H0'].get(n,0)for n in set(x['upper_endpoint_Euler4'])|set(x['derivative_target_H0'])}
 require(x['obstruction']=={n:v for n,v in obs.items()if v},'full obstruction is the reported source minus target')
require(a['total_checks']==16582 and a['additional_checks']==661,'author check totals')
require(len(a['new_negative_controls'])==12,'author twelve executed controls')
require(a['case_rows_excluded']==b['covered_case_degree_rows']==50 and a['positive_case_rows_excluded']==b['positive_case_degree_rows_retained']==37,'complete numerical case coverage')
require(a['torsion_partitions_excluded']==b['covered_torsion_rows']==96 and a['positive_torsion_partitions_excluded']==b['positive_torsion_rows_retained']==83,'complete torsion coverage')
require(a['only_residual_image']=={'degree':9,'coefficient':'1','necessary_source':'D'}and b['remaining_image_rank']==1 and not b['whole_ordered_profile_excluded'],'residual rank-one scope unchanged')
print(json.dumps({'status':'PASS','author_checks':a['total_checks'],'author_new_checks':a['additional_checks'],'independent_checks':b['checks'],'author_files_authenticated':len(manifest['files']),'author_normal_and_optimized_replay':True,'complete_obstruction_vectors_compared':13,'case_rows_compared':50,'torsion_rows_compared':96,'physical_V_excesses':[1]*13,'reported_multiplicities_validated':True,'author_hashes':{n:hashlib.sha256((A/n).read_bytes()).hexdigest()for n in ['PROOF.md','verify.py','RESULT.json','MANIFEST.json']}},indent=2,sort_keys=True))
