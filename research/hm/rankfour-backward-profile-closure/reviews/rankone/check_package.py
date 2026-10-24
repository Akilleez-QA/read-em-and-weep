#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,subprocess,sys
R=Path(__file__).resolve().parent;A=R.parents[1]/'dependencies/rankone'
def require(ok,msg):
 if not ok:raise RuntimeError(msg)
manifest=json.loads((A/'MANIFEST.json').read_text())
for item in manifest:
 raw=(A/item['path']).read_bytes()
 require(len(raw)==item['bytes']and hashlib.sha256(raw).hexdigest()==item['sha256'],'frozen author manifest '+item['path'])
for flags in([],['-O']):
 p=subprocess.run([sys.executable,*flags,str(A/'verify.py')],capture_output=True,cwd='/tmp')
 require(p.returncode==0 and p.stdout==(A/'RESULT.json').read_bytes(),'author normal/optimized frozen replay')
p=subprocess.run([sys.executable,str(A/'test_controls.py')],capture_output=True,cwd='/tmp')
require(p.returncode==0 and p.stdout==(A/'CONTROLS.json').read_bytes(),'eight executed author mutation controls')
a=json.loads((A/'RESULT.json').read_text());b=json.loads((R/'RESULT.json').read_text())
def shape(s):return tuple(sorted((x['degree'],x['coefficient'])for x in s))
aa={shape(x['kernel']):x for x in a['raw_domain']};bb={shape(x['N']):x for x in b['domain']}
require(len(aa)==53 and set(aa)==set(bb),'complete rank-three domain agreement')
for key,x in aa.items():
 y=bb[key]
 require(x['c3']==y['c3']and x['margin']==y['section_margin']and x['dual_targets']==y['Q_targets']and x['passes']==y['passes'],'all fifty-three exact section margins, common targets and decisions agree')
def degree_rows(rows):return {(x['a'],x['b'],tuple(x['defects']),tuple(x['quotient_degrees']))for x in rows}
def own_rows(rows):return {(a,b,tuple(ds),tuple(cs))for a,b,ds,cs in rows}
for name in ('low_exclusions','upper_exclusions'):
 aa={shape(x['kernel']):x for x in a[name]};bb={shape(x['N']):x for x in b[name]}
 require(set(aa)==set(bb),'complete '+name+' domain')
 for key,x in aa.items():
  y=bb[key]
  require(degree_rows(x['defect_rows'])==own_rows(y['degree_rows']),'all attached ramified degree rows agree')
  if name=='low_exclusions':require(x['endpoint_degree']==y['a']and x['endpoint_domain']==len(y['endpoint_domain'])and x['survivors']==len(y['joint_survivors'])==0,'all low endpoint domains and empty survivors agree')
  else:
   require(x['upper_euler']==y['chi_Z4']and x['upper_target']==y['H0_B_dual'],'complete upper endpoint and target characters agree')
   require(x['V_margin']==y['V_margin']==y['V_source']-y['V_target']==1,'reported V multiplicities verified')
require(a['counts']==b['counts']==[53,16,7,9],'final exact counts')
require(a['new_checks']==929 and a['dependency_checks']==3278,'final author check totals')
require(not a['complete_profile_claim']and not b['complete_profile_claim'],'focused theorem only')
print(json.dumps({'status':'PASS','author_new_checks':929,'author_dependency_checks':3278,'independent_checks':b['checks'],'author_normal_and_optimized_replay':True,'author_executed_mutations':8,'complete_domain_comparison':[53,16,7,9],'all_margins_targets_and_ramified_rows_compared':True,'all_nine_upper_characters_compared':True,'reported_multiplicities_validated':True,'author_hashes':{n:hashlib.sha256((A/n).read_bytes()).hexdigest()for n in ['PROOF.md','verify.py','RESULT.json','MANIFEST.json']}},indent=2,sort_keys=True))
