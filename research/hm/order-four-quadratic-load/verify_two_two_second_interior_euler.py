"""Necessary second-interior Gauss Euler envelopes; abstract characters only."""
import json,runpy,contextlib,io,functools,collections
from pathlib import Path
import hashlib,sys
ROOT=Path(__file__).resolve().parent
p=str(ROOT)+'/'
with contextlib.redirect_stdout(io.StringIO()):r=runpy.run_path(p+'verify_negative_vertex_scalar.py')
names=('one','W','Wp','A','V','P','S','D','T');dims={n:int(r[n][0][0]) for n in names}
@functools.lru_cache(None)
def prod(n,d):
 c=r['vmul'](r[n],[r['sym'](d,w) for w in r['W']]);return tuple(int(r['inner'](r[m],c)[0]) for m in names)
def chi(B,t):
 v=[0]*9
 for e,n in B:
  d=e+t
  if d==-1:continue
  c=prod(n,d if d>=0 else -d-2);sgn=1 if d>=0 else -1
  v=[a+sgn*b for a,b in zip(v,c)]
 return tuple(v)
def check(N,A):
 d=min(j for j,n,m in N)
 a=chi(A,d-2);b=chi([(-j,n) for j,n,m in N for _ in range(m)],d)
 return tuple(x-y for x,y in zip(a,b))

raw=(ROOT/'two-two-kernel-top-multiplicity-records.json').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='ecb306e613b55076416f6682f205174ee88eb166dda0c007c141b92f01a86d15'
rs=json.loads(raw)
assert len(rs)==1221
assert len({json.dumps([x['A'],x['B']],separators=(',',':')) for x in rs})==24
key=lambda x:json.dumps([x['A'],x['B']],separators=(',',':'))
out=[];cert={};counts=collections.Counter()
for x in rs:
 ks=[N for N in x['K_splittings'] if min(check(N,x['A']))>=0]
 ls=[N for N in x['L_splittings'] if min(check(N,x['B']))>=0]
 counts['K_before']+=len(x['K_splittings']);counts['K_after']+=len(ks)
 counts['L_before']+=len(x['L_splittings']);counts['L_after']+=len(ls)
 if ks and ls:out.append(dict(x,K_splittings=ks,L_splittings=ls))
 for side,c in [('K','A'),('L','B')]:
  cert.setdefault(key(x),{}).setdefault(side,set()).update(check(N,x[c]) for N in x[side+'_splittings'])
pairs=collections.Counter(map(key,out))
assert len(out)==723 and len(pairs)==7
assert all(x['defect']==0 for x in out)
assert all(min(j for j,n,m in N)==3 for x in out for side in ['K','L'] for N in x[side+'_splittings'])
# Numerical bounds derived from rank11/7 endpoints and maxdeg <= -4.
for x in out:
 a=sum(e*dims[n] for e,n in x['A']);b=sum(e*dims[n] for e,n in x['B'])
 assert a in (-2,0,2) and b==-6-a
 assert 0<=2*a+4<12
 assert 0<=2*b+20<=12
removed=[]
for k in sorted(set(map(key,rs))-set(pairs)):
 c=cert[k]
 removed.append(dict(A=json.loads(k)[0],B=json.loads(k)[1],envelopes={side:[dict(zip(names,v)) for v in sorted(c[side])] for side in ['K','L']}))
assert len(removed)==17
summary=dict(input_sha256=hashlib.sha256(raw).hexdigest(),before_records=1221,after_records=723,before_pairs=24,after_pairs=7,defect_counts=dict(collections.Counter(x['defect'] for x in out)),splitting_counts=dict(counts),pairs=[dict(A=json.loads(k)[0],B=json.loads(k)[1],records=v,envelopes={side:[dict(zip(names,w)) for w in sorted(cert[k][side])] for side in ['K','L']}) for k,v in sorted(pairs.items())],removed_pairs=removed)
(ROOT/'two-two-second-interior-euler-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
if '--full' in sys.argv:(ROOT/'two-two-second-interior-euler-records.json').write_text(json.dumps(out,indent=2)+'\n')
assert (ROOT/'two-two-kernel-top-multiplicity-records.json').read_bytes()==raw
print(json.dumps({k:v for k,v in summary.items() if k not in ('pairs','removed_pairs')},indent=2))
print('PASS: actual second-interior quotient Euler constraints; 17 additional pairs excluded; determinant torsion retained.')
