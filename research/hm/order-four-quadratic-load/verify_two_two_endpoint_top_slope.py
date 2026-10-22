"""Endpoint strict-slope necessary characters; no endpoint rank assumption."""
from pathlib import Path
import runpy,io,contextlib,json,hashlib,sys
from collections import Counter
ROOT=Path(__file__).resolve().parent
# Read the character helper definitions without executing its output section.
source=(ROOT/'verify_two_two_second_interior_euler.py').read_text().split("raw=(ROOT/")[0]
ns={'__file__':str(ROOT/'verify_two_two_second_interior_euler.py')}
with contextlib.redirect_stdout(io.StringIO()):exec(compile(source,'second_interior_character_helpers','exec'),ns)
chi,names=ns['chi'],ns['names']
def check(N,A):
 h=chi(tuple((e,n) for e,n in A if e>=0),0)
 ca=chi(A,2);kn=chi([(-j,n) for j,n,m in N for _ in range(m)],4)
 return tuple(x+y-z for x,y,z in zip(h,ca,kn))
raw=(ROOT/'two-two-second-interior-euler-records.json').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='bfbe3ac01a6c110192b8640a96150906283e3cf49e54b31012052c683bb358f9'
records=json.loads(raw);assert len(records)==723
assert len({json.dumps([x['A'],x['B']],separators=(',',':')) for x in records})==7
out=[];cert={}
key=lambda x:json.dumps([x['A'],x['B']],separators=(',',':'))
for x in records:
 ks=[N for N in x['K_splittings'] if min(check(N,x['A']))>=0]
 cert.setdefault(key(x),set()).update(check(N,x['A']) for N in x['K_splittings'])
 if ks:out.append(dict(x,K_splittings=ks))
pairs=Counter(map(key,out))
assert len(out)==354 and len(pairs)==3
assert all(len(v)==1 for v in cert.values())
removed=sorted(set(cert)-set(pairs))
assert len(removed)==4
assert all(next(iter(cert[k]))[names.index('V')]==-1 for k in removed)
summary=dict(input_sha256=hashlib.sha256(raw).hexdigest(),before_records=723,after_records=354,before_pairs=7,after_pairs=3,pairs=[dict(A=json.loads(k)[0],B=json.loads(k)[1],records=v,envelope=dict(zip(names,next(iter(cert[k]))))) for k,v in sorted(pairs.items())],removed_pairs=[dict(A=json.loads(k)[0],B=json.loads(k)[1],envelope=dict(zip(names,next(iter(cert[k]))))) for k in removed])
(ROOT/'two-two-endpoint-top-slope-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
if '--full' in sys.argv:(ROOT/'two-two-endpoint-top-slope-records.json').write_text(json.dumps(out,indent=2)+'\n')
assert (ROOT/'two-two-second-interior-euler-records.json').read_bytes()==raw
print(json.dumps({k:v for k,v in summary.items() if k not in ('pairs','removed_pairs')},indent=2))
print('PASS: endpoint strict-slope character envelopes exclude four pairs; no endpoint derivative rank assumption.')
