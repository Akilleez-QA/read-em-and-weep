"""Necessary top coefficient injections for both negative Gauss kernels.
Reads frozen records; writes only a new compact summary. No map instances.
"""
from pathlib import Path
import json,runpy,io,contextlib,hashlib,sys
from functools import lru_cache
from collections import Counter
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
 r=runpy.run_path(str(ROOT/'verify_negative_vertex_scalar.py'))
names=('one','W','Wp','A','V','P','S','D','T')
@lru_cache(None)
def product_mult(n,m,d):
 ch=r['vmul'](r[m],[r['sym'](d,x) for x in r['W']])
 a,b=r['inner'](r[n],ch)
 assert b==0 and a.denominator==1
 return int(a)
def check(K,C):
 assert K and all(c>0 for _,_,c in K)
 assert len({(j,n) for j,n,c in K})==len(K)
 j=min(x[0] for x in K)
 failures=[]
 for d,n,c in K:
  if d!=j:continue
  cap=sum(product_mult(n,m,e+j-2) for e,m in C if e+j-2>=0)
  if c>cap:failures.append(dict(top_degree=-j,irrep=n,multiplicity=c,target_multiplicity=cap))
 return failures
raw=(ROOT/'two-two-exact-kernel-compatible-records.json').read_bytes()
records=json.loads(raw); assert len(records)==1880
survive=[];failed=Counter(); removed_pair_reasons={}; splitting_counts=Counter()
for x in records:
 ks=[K for K in x['K_splittings'] if not check(K,x['A'])]
 ls=[L for L in x['L_splittings'] if not check(L,x['B'])]
 splitting_counts['K_before']+=len(x['K_splittings']);splitting_counts['L_before']+=len(x['L_splittings'])
 splitting_counts['K_after']+=len(ks);splitting_counts['L_after']+=len(ls)
 if ks and ls:survive.append(dict(x,K_splittings=ks,L_splittings=ls))
 else:failed['both' if not ks and not ls else 'K' if not ks else 'L']+=1
key=lambda x:json.dumps([x['A'],x['B']],separators=(',',':'))
pairs=Counter(key(x) for x in survive)
removed=[]
for k in sorted(set(map(key,records))-set(pairs)):
 xs=[x for x in records if key(x)==k]
 reasons={side:sorted({json.dumps(z,sort_keys=True) for x in xs for N in x[field] for z in check(N,x[c])}) for side,field,c in [('K','K_splittings','A'),('L','L_splittings','B')]}
 removed.append(dict(A=xs[0]['A'],B=xs[0]['B'],records=len(xs),failure_certificates={s:[json.loads(z) for z in zs] for s,zs in reasons.items()}))
assert len(survive)==1221 and len(pairs)==24
assert failed=={'L':659}
assert Counter(x['defect'] for x in survive)=={0:1064,12:157}
assert len(removed)==10
for p in removed:
 for x in records:
  if x['A']==p['A'] and x['B']==p['B']:
   for L in x['L_splittings']:
    assert min(j for j,n,c in L)==4
    assert sum(c for j,n,c in L if j==4 and n=='V')==2
 assert sum(product_mult('V',m,e+2) for e,m in p['B'] if e+2>=0)==1
# Input content is unchanged. Optional full output is new and distinctly named.
assert (ROOT/'two-two-exact-kernel-compatible-records.json').read_bytes()==raw
if '--full' in sys.argv:
 (ROOT/'two-two-kernel-top-multiplicity-records.json').write_text(json.dumps(survive,indent=2)+'\n')
out=dict(input_sha256=hashlib.sha256(raw).hexdigest(),before_records=len(records),after_records=len(survive),before_pairs=len(set(map(key,records))),after_pairs=len(pairs),defect_counts=dict(Counter(x['defect'] for x in survive)),failed_record_sides=dict(failed),splitting_counts=dict(splitting_counts),removed_pairs=removed,pairs=[dict(A=json.loads(k)[0],B=json.loads(k)[1],records=v) for k,v in sorted(pairs.items())])
(ROOT/'two-two-kernel-top-multiplicity-summary.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('pairs','removed_pairs')},indent=2))
print('PASS: both actual derivative top-multiplicity constraints; ten removed pairs have the common 2V versus 1V obstruction.')
