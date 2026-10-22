#!/usr/bin/env python3
"""Standalone first-kernel application of the published finite degree envelope."""
from pathlib import Path
from collections import Counter
import hashlib,json
ROOT=Path(__file__).resolve().parent
PINNED={'rank-three-quotient-frontier-144.json':'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad','NEGATIVE-GAUSS-FLAGS-HAVE-A-FINITE-DEGREE-ENVELOPE.md':'90aa42a0eded9cd3118d086a4ebf82ce98ff4e4c3682e1baaea61e5928f94088'}
THEOREM_COMMIT='8ddbcedc7e01f33ae9aacff56df8da0a33503b57'
PRIOR_ID='G3.21.bf8462f3a0d7';PRIOR_COMMIT='f0aaf0dcc7e4503fb6199ddab4bcc8e08a679c66'
assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
f=json.loads((ROOT/'rank-three-quotient-frontier-144.json').read_text());rows=f['cases']
assert len(rows)==len({r['id']for r in rows})==182
active=[r for r in rows if r['status']=='not_excluded'];assert len(active)==144
assert next(r for r in active if r['id']==PRIOR_ID)['source_index']==11
D={'one':1,'W':2,'Wp':2,'A':3,'V':3,'P':4,'S':4,'D':5,'T':6}
def degrees(bundle):return sorted([e for e,n in bundle for _ in range(D[n])],reverse=True)
def capacity(lam,n):
 heights=[(a,b,n-a-b)for a in range(n+1)for b in range(a+1)if 0<=n-a-b<=b]
 values=[sum(h*d-h*(h+1)for h,d in zip(v,lam))for v in heights]
 best=max(values)
 return best,[list(v)for v,x in zip(heights,values)if x==best]
excluded=[]
for r in active:
 lam=degrees(r['A']);assert len(lam)==3
 deg=-54-sum(lam);cap,hs=capacity(lam,14)
 if deg>cap:excluded.append(dict(id=r['id'],profile=r['profile'],A_degrees=lam,degree_K=deg,capacity=cap,gap=deg-cap,maximizing_heights=hs))
new={r['id']for r in excluded};assert len(new)==46 and PRIOR_ID not in new
assert dict(Counter(r['profile']for r in excluded))=={'11':40,'12':6}
historical=sorted(r['id']for r in rows if r['status']=='excluded')
remaining=sorted(r['id']for r in active if r['id']not in new|{PRIOR_ID})
assert len(remaining)==97 and len(active)-len(new)==98
counts=dict(Counter(r['profile']for r in active if r['id']in remaining));assert counts=={'11':82,'12':4,'21':11}
assert len(set(historical)|new|{PRIOR_ID}|set(remaining))==182
assert len(historical)+len(new)+1+len(remaining)==182
out=dict(scope='46 quotient labels excluded by the primal degree envelope, no profile closure or realization.',source_hashes=PINNED,theorem_commit=THEOREM_COMMIT,prior_exclusion=dict(id=PRIOR_ID,commit=PRIOR_COMMIT),input_relative=dict(before=144,after=98),combined=dict(before=143,after=97,remaining_by_profile=counts),new_exclusions=excluded,historical_excluded_ids=historical,remaining_ids=remaining)
(ROOT/'all-profile-primal-degree-envelope.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: primal46 exclusions; input144->98; with prior689143->97; profiles82/4/11; all182 IDs preserved.')
