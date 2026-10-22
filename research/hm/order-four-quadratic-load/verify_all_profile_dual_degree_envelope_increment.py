#!/usr/bin/env python3
"""Standalone dual increment after the unrestricted primal degree envelope."""
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
# Recompute the primal baseline from published inputs, with no output imports.
primal={r['id']for r in active if -54-sum(degrees(r['A']))>capacity(degrees(r['A']),14)[0]}
assert len(primal)==46 and PRIOR_ID not in primal
current=[r for r in active if r['id']!=PRIOR_ID];assert len(current)==143
all_dual=[]
for r in current:
 lam=degrees(r['B']);assert len(lam)==3
 deg=-54-sum(lam);cap,hs=capacity(lam,10)
 if deg>cap:all_dual.append(dict(id=r['id'],profile=r['profile'],B_degrees=lam,degree_L=deg,capacity=cap,gap=deg-cap,maximizing_heights=hs,already_primal=r['id']in primal))
dual={r['id']for r in all_dual};overlap=dual&primal;increment=dual-primal
assert len(dual)==86 and len(overlap)==28 and len(increment)==58
historical=sorted(r['id']for r in rows if r['status']=='excluded')
remaining=sorted(r['id']for r in current if r['id']not in primal|dual)
counts=dict(Counter(r['profile']for r in current if r['id']in remaining))
assert len(remaining)==39 and counts=={'11':30,'12':4,'21':5}
inc_counts=dict(Counter(r['profile']for r in all_dual if not r['already_primal']))
assert inc_counts=={'11':52,'21':6}
assert len(set(historical)|{PRIOR_ID}|primal|increment|set(remaining))==182
assert len(historical)+1+len(primal)+len(increment)+len(remaining)==182
out=dict(scope='58 new dual exclusions after primal46; no profile closure or realization.',source_hashes=PINNED,theorem_commit=THEOREM_COMMIT,prior_exclusion=dict(id=PRIOR_ID,commit=PRIOR_COMMIT),combined=dict(before_primal=143,after_primal=97,after_dual=39,remaining_by_profile=counts),dual_totals=dict(excluded_on143=86,already_primal=28,new_increment=58,new_by_profile=inc_counts),new_exclusions=[r for r in all_dual if not r['already_primal']],overlapping_primal_ids=sorted(overlap),primal_excluded_ids=sorted(primal),historical_excluded_ids=historical,remaining_ids=remaining)
(ROOT/'all-profile-dual-degree-envelope-increment.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: dual86, overlap28, increment58;97->39; profiles30/4/5; all182 IDs preserved.')
