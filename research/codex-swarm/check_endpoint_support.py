"""Endpoint refinement on SAME 360/720 domains; Boolean paths only."""
import contextlib,hashlib,io,json,runpy,subprocess,itertools,collections
from pathlib import Path
PIN='6e28c6b59f8245779f6c03a20798e4de6842ae19'
def check(c,m):
 if not c:raise ValueError(m)
def read(path,blob):
 raw=subprocess.check_output(['git','-C',str(Path(__file__).resolve().parents[2]),'show',PIN+':research/hm/null-support-certificates/'+path])
 actual=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
 check(actual==blob,'outer source drift '+path)
 return raw
outer=read('outer_partition_source_binding.py','1dcb9d5e0def4fba2268f4c54de6409b137ed05e')
read('owned_scalar_denominator_binding.py','b1fee3ac562bce5f561adb5b6ab03103f148efa6')
# No module execution: bind exact inspected source bytes and load only our
# independent Boolean model script, which authenticates model blob itself.
for witness in [b"CARRIER_POWER = 54",b"LEGAL_POWER = 29",b"empty sum=0 unless k=0",b"n_j>=",b"Q_b=B_b*Cbar_b for b<=s"]:
 check(witness in outer,'formula witness absent')
with contextlib.redirect_stdout(io.StringIO()):
 d=runpy.run_path(str(Path(__file__).with_name('check_higher_literal_support.py')))
key=d['key'];selectors=d['selectors'];alphabet=d['alphabet'];out=[]
for q in [3,4]:
 domain=[alphabet[:s+2] for s in range(4-q,5)]
 raw=list(itertools.product(*domain));check(len(raw)==(360 if q==3 else 720),'same denominator')
 for row in ([3,4,5,6] if q==3 else [7,8]):
  counts=collections.Counter();anchors=collections.Counter();unknown=[]
  for sample in raw:
   if sample[-1] not in [5,4]:counts['endpoint_weight_zero']+=1;continue
   ordered=tuple(sorted(sample,key=key));a=ordered[:q-1]
   if any(key(a[j])>=key(a[j+1]) for j in range(q-2)):
    counts['strict_prefix_zero']+=1;continue
   paths=selectors(q,a,row)
   if not paths:counts['boolean_path_zero']+=1;continue
   counts['unknown']+=1;anchors[a]+=1
   unknown.append({'sampled_carriers':sample,'sorted_carriers':ordered,'anchor':a,'residual_paths':paths})
  check(sum(counts.values())==len(raw),'classification coverage')
  out.append({'q':q,'row':row,'raw_domain_size':len(raw),'counts':dict(counts),'unknown_anchors':[{'anchor':a,'tuples':n} for a,n in anchors.items()],'unknown_records':unknown})
print(json.dumps({'status':'pass','source_commit':PIN,'outer_source_blob':'1dcb9d5e0def4fba2268f4c54de6409b137ed05e','same_raw_denominator':True,'partition_zero_rule':'last sampled standard15 permits only primary4 or auxiliary5','domain_is_flag_superdomain':True,'no_q2_or_incumbent_scan':True,'physical_source_evaluated':False,'results':out},sort_keys=True,indent=2))
