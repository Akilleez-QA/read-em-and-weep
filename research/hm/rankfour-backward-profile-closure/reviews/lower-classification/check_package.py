#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,subprocess,sys
R=Path(__file__).resolve().parent;A=R.parents[1]/'dependencies/lower-exclusion/lower-image'
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
def pair(row,independent=False):return shape(row['image']),shape(row['N']if independent else row['kernel'])
require({pair(x)for x in a['final_pairs']}=={pair(x,True)for x in b['final_necessary_cases']},'complete thirteen final pairs agree')
aa={pair(x):x for x in a['preliminary_pairs']}
bb={pair(x,True):x for d in b['kernel_domains']for x in d['survivors']}
require(set(aa)==set(bb)and len(aa)==23,'complete twenty-three preliminary pairs agree')
for key in aa:
 x,y=aa[key],bb[key]
 require(x['c3']==y['c3']and shape(x['quotient'])==shape(y['B']),'every actual quotient B and its degree agree')
 require(x['margin']==y['section_margin'],'every exact two-backstep character margin agrees')
 require(x['extension_character']==y['ordinary_Ext'],'every ordinary Ext character agrees')
 require(x['Q_type_targets']==y['Q_types'],'all common dual target types agree')
for x in a['domain_results']:
 y=next(d for d in b['kernel_domains']if shape(d['image'])==shape(x['image']))
 require(x['ordinary_degree_window']==[y['N_min_degree'],y['N_max_degree']]and x['candidate_count']==y['initial_shapes'],'intrinsic N domain windows and counts agree')
 require({shape(z['kernel'])for z in x['candidates']}=={shape(z)for z in y['all_N_shapes']},'complete intrinsic N shape domains agree')
# Full case-degree and torsion data are compared independently of case numbering.
def degree_key(x,independent=False):
 return (*pair(x,independent),x['a'],x['b'],tuple(x['defects']),tuple(x['graded_degrees']if independent else x['quotient_degrees']))
require({degree_key(x)for x in a['case_degree_ledger']}=={degree_key(x,True)for x in b['case_degree_rows']},'all fifty case-degree rows agree')
def torsion_key(x,independent=False):
 if independent:return (*degree_key(x,True),tuple(x['nu']),tuple(x['tau']),tuple(x['N_degrees']),tuple(x['C_degrees']))
 return (*degree_key(x),tuple(x['kernel_defects']),tuple(x['quotient_defects']),tuple(x['kernel_degrees']),tuple(x['quotient_block_degrees']))
require({torsion_key(x)for x in a['torsion_ledger']}=={torsion_key(x,True)for x in b['torsion_partition_rows']},'all ninety-six torsion partitions and subquotient degrees agree')
for x in a['removed_pairs']:
 y=next(z for z in b['eliminated_low_cases']if pair(z,True)==pair(x))
 require(x['a']==y['lower_endpoint_degree']and x['endpoint_Euler3']==y['chi_endpoint_3']and x['endpoint_Euler4']==y['chi_endpoint_4'],'all ten endpoint Euler contradictions agree')
 require({shape(z)for z in x['endpoint_survivors']}=={shape(z)for z in y['endpoint_survivors']},'all ten complete endpoint survivor sets agree')
require(len(b['nontrivial_ordinary_Ext_cases'])==2 and all(x['ordinary_Ext']=={'P':1}and x['equivariant_Ext_dimension']==0 for x in b['nontrivial_ordinary_Ext_cases']),'reported ordinary and invariant Ext values match actual verified computation')
require(a['checks']==3278,'final author check count')
print(json.dumps({'status':'PASS','author_checks':a['checks'],'independent_checks':b['checks'],'author_files_authenticated':len(manifest['files']),'author_normal_and_optimized_replay':True,'complete_domains_agree':['23 preliminary pairs with full margins, Ext and dual target data','13 final pairs','10 endpoint exclusions','50 case-degree rows','96 torsion partitions and subquotient degree rows'],'ordinary_Ext_P_cases':2,'equivariant_Ext_dimensions':[0,0],'author_hashes':{n:hashlib.sha256((A/n).read_bytes()).hexdigest()for n in ['PROOF.md','verify.py','RESULT.json','MANIFEST.json']}},indent=2,sort_keys=True))
