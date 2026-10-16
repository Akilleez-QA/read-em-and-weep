"""Focused source-free certificate-label and rank-lift fault controls."""
import copy,json
from pathlib import Path
from review_selection import verify,image,matrix,need
cert=json.loads(Path(__file__).with_name('selection.json').read_text())
def reject(name,change):
 x=copy.deepcopy(cert);change(x)
 try:verify(x)
 except(ValueError,KeyError):return name
 raise ValueError('accepted mutation '+name)
results=[]
results.append(reject('trace-orientation',lambda x:x.update(supertrace_orientation='c=K')))
results.append(reject('duplicate-selected-label',lambda x:x['selected']['minus1']['labels'].__setitem__(1,x['selected']['minus1']['labels'][0])))
results.append(reject('out-of-domain-monomial',lambda x:x['selected']['zero']['labels'][0].update(base_monomial=[5,5])))
results.append(reject('augmented-rank-tamper',lambda x:x['selected']['zero'].update(augmented_rank_mod101=849)))
results.append(reject('matrix-binding-tamper',lambda x:x['selected']['minus1'].update(matrix_digest='0'*64)))
C=matrix(2,-1);idx=next(j for j,col in enumerate(C['data'])if col)
need(bool(image(C,[(idx,1)])),'noncycle exact control')
print(json.dumps({'status':'focused_controls_pass','rejected':results,'noncycle_integer_control':True,'physical_source_evaluated':False},indent=2))
