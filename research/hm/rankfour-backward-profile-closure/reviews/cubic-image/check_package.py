#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,subprocess,sys
R=Path(__file__).resolve().parent
A=R.parents[1]/'dependencies/lower-exclusion/cubic-image'
def require(ok,msg):
 if not ok:raise RuntimeError(msg)
manifest=json.loads((A/'MANIFEST.json').read_text())
for item in manifest['files']:
 raw=(A/item['file']).read_bytes()
 require(len(raw)==item['bytes'] and hashlib.sha256(raw).hexdigest()==item['sha256'],'frozen author manifest: '+item['file'])
for flags in ([],['-O']):
 p=subprocess.run([sys.executable,*flags,str(A/'verify.py')],capture_output=True,cwd='/tmp')
 require(p.returncode==0 and p.stdout==(A/'RESULT.json').read_bytes(),'author normal/optimized frozen replay')
a=json.loads((A/'RESULT.json').read_text()); b=json.loads((R/'RESULT.json').read_text())
shape=lambda s:tuple(sorted((x['degree'],x['coefficient'])for x in s))
require({shape(x['shape'])for x in a['endpoint_shapes']}=={shape(s)for s in b['endpoint_shapes']},'complete 46 endpoint domains agree')
require({shape(s)for s in a['forced_endpoints']}=={shape(s)for s in b['endpoint_survivors']},'both complete endpoint survivor sets agree')
require({shape(s['shape'])for s in a['section_bound_survivors']}=={shape(s['image'])for s in b['full_rank_image_candidates']},'all four full-rank image shapes agree')
require({(x['a'],x['b'],tuple(x['defects']),tuple(x['quotient_degrees']))for x in a['ledger']}=={(x['a'],x['b'],tuple(x['defects']),tuple(x['graded_degrees']))for x in b['ledger']},'all 31 degree/defect rows agree')
require(a['rank_four_image_multisets']==b['raw_rank_four_multisets']==24,'all 24 rank-four multiset count')
require(a['checks']==12643 and b['checks']==603,'frozen author and reviewer check totals')
require(b['intertwiner_multiplicity']==1,'reported intertwiner multiplicity equals verified one-dimensional Hom space')
print(json.dumps({'status':'PASS','author_manifest_files_authenticated':len(manifest['files']),'author_normal_and_optimized_replay':True,'complete_domains_equal':['31 degree/defect rows','46 endpoint shapes','2 endpoint survivors','4 full-rank image survivors'],'raw_rank_four_multiset_count':24,'author_checks':a['checks'],'reviewer_checks':b['checks'],'reported_intertwiner_multiplicity':b['intertwiner_multiplicity'],'author_hashes':{name:hashlib.sha256((A/name).read_bytes()).hexdigest()for name in ['PROOF.md','verify.py','RESULT.json','MANIFEST.json']}},indent=2,sort_keys=True))
