#!/usr/bin/env python3
"""Regenerate the independent review and exact author/result comparison."""
from pathlib import Path
import subprocess,sys,json,hashlib
ROOT=Path(__file__).resolve().parent
def require(ok,message):
 if not ok:raise ValueError(message)
def run(argv):
 p=subprocess.run([sys.executable]+argv,cwd=ROOT,text=True,capture_output=True)
 require(p.returncode==0,p.stderr)
 return p.stdout
normal=run([str(ROOT/'independent.py')])
normal_result=(ROOT/'INDEPENDENT-RESULT.json').read_bytes()
optimized=run(['-O',str(ROOT/'independent.py')])
require(normal==optimized,'normal/optimized stdout mismatch')
require(normal_result==(ROOT/'INDEPENDENT-RESULT.json').read_bytes(),'normal/optimized full result mismatch')
(ROOT/'normal.log').write_text(normal);(ROOT/'optimized.log').write_text(optimized)
controls=run([str(ROOT/'test_independent_controls.py')])
c=json.loads(controls)
require(c['status']=='PASS'and c['rejections']==22,'independent mutation controls')
(ROOT/'INDEPENDENT-CONTROLS.json').write_text(controls)
a=json.loads((ROOT/'accepted-author-packet'/'RESULT.json').read_text())
i=json.loads(normal_result)
names=('1','W','A','S4','D','T6','P',"W'",'V')
def norm(row):
 def b(k):return tuple(sorted((x['degree'],names.index(x['coefficient']))for x in row[k]))
 return b('F0'),b('D0'),row['torsion_r'],b('B')
def conv(row):return tuple(map(tuple,row[0])),tuple(map(tuple,row[1])),row[2],tuple(map(tuple,row[3]))
ac=set(map(norm,a['horizontal_rejections']+a['rank_one_final_frontier']))
ic={conv(row)for case in i['cases']for row in case['cohom_rows']}
af=set(map(norm,a['rank_one_final_frontier']))
ifinal={conv(row)for case in i['cases']for row in case['horizontal_survivors']}
require(ac==ic and len(ac)==359,'complete 359-tuple cohomology frontier mismatch')
require(af==ifinal and len(af)==172,'complete 172-tuple horizontal frontier mismatch')
require(i['final_rank_one_bridge']['remaining']==0,'nonempty final residual')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
comparison={'status':'PASS','normal_optimized_stdout_and_full_result_equal':True,'cohomology_tuples_equal':True,'cohomology_tuple_count':len(ac),'horizontal_survivor_tuples_equal':True,'horizontal_survivor_tuple_count':len(af),'author_mathematical_manifest_sha256':sha(ROOT/'accepted-author-packet'/'MANIFEST.json'),'author_result_sha256':sha(ROOT/'accepted-author-packet'/'RESULT.json'),'independent_result_sha256':sha(ROOT/'INDEPENDENT-RESULT.json'),'author_checks':a['checks'],'independent_checks':i['checks'],'independent_subprocess_mutations':22,'remaining_after_rankone_bridge':0}
(ROOT/'COMPARISON.json').write_text(json.dumps(comparison,indent=2,sort_keys=True)+'\n')
print(json.dumps(comparison,indent=2,sort_keys=True))
