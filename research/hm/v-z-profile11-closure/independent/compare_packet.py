import json,hashlib
from pathlib import Path
R=Path(__file__).parent;P=R.parent
def need(x):
 if not x:raise RuntimeError('packet mismatch')
auth=json.loads((R/'AUTHENTICATION.json').read_text())
for m in json.loads((P/'INPUTS.json').read_text()):
 a=next(a for a in auth if a['ref']==m['ref'] and a['path']==m['path'])
 need(a['sha256']==m['sha256'] and a['git_blob']==m['git_blob_sha1'] and a['bytes']==m['bytes'])
 need((P/m['file']).read_bytes()==(R/'originals'/a['name']).read_bytes())
x=json.loads((R/'RESULT.json').read_text())['sources'];y=json.loads((P/'RESULT.json').read_text())['sources']
for key,a in x.items():
 b=y[key];need(a['tuple']==b['source_tuple']);need(a['compatible']==b['compatible_indices'])
 for stage in ['cubic','quartic','capacity']:need(a[stage]==b['partition'][stage])
 for rr in a['records']:
  ar=next(t for t in b['certificates'] if t['index']==rr['index']);need(ar['stage']==rr['kind'])
  if rr['kind']=='quartic':need(ar['negative']==rr['negative'])
  else:
   need(ar['ordinary_B']==rr['ordinary_B']);need(ar['exact_cap']==rr['max_capacity']);need(ar['actual_degree_L']==rr['degree_L']);need(ar['gap']==rr['gap'])
   need([e['cap'] for e in ar['all_height_capacities']]==rr['caps_h10_to5'][::-1])
 for rr in a['incompatible_witnesses']:
  ar=next(t for t in b['incompatible_records'] if t['index']==rr['index'])['first_failure']; ir=rr['witnesses'][0]
  need(ar['twist']==ir['twist'] and ar['negative']==ir['negative'])
  need(ar['condition']=={'H1E-H1A':'H1(A)<=H1(E)','H1Edual-H0B':'H0(B)<=H1(E(-u))'}[ir['condition']])
print('PASS: exact partitions, every quartic witness, every capacity, all 250 first incompatibility witnesses, and all eight freshly authenticated originals')
