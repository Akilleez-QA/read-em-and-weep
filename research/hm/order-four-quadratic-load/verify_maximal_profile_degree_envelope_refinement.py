#!/usr/bin/env python3
"""Retain all derivative patterns allowed by maximal profile lengths one or two."""
from pathlib import Path
from collections import Counter
import hashlib,json
ROOT=Path(__file__).resolve().parent
PINNED={'rank-three-quotient-frontier-144.json':'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad','all-profile-dual-degree-envelope-increment.json':'183047fd6055f8fa42881ffac4acfa37e9b4415583df80ef2e219de284b25374','NEGATIVE-GAUSS-FLAGS-HAVE-A-FINITE-DEGREE-ENVELOPE.md':'90aa42a0eded9cd3118d086a4ebf82ce98ff4e4c3682e1baaea61e5928f94088','ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md':'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256'}
assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
rows=json.loads((ROOT/'rank-three-quotient-frontier-144.json').read_text())['cases']
prior=json.loads((ROOT/'all-profile-dual-degree-envelope-increment.json').read_text())
ids=set(prior['remaining_ids']);assert len(ids)==39
D={'one':1,'W':2,'Wp':2,'A':3,'V':3,'P':4,'S':4,'D':5,'T':6}
excluded=[];checked=[]
for r in rows:
 if r['id']not in ids:continue
 for side,n,length in [('A',14,int(r['profile'][0])),('B',10,int(r['profile'][1]))]:
  assert length in [1,2]
  lam=sorted([e for e,c in r[side]for _ in range(D[c])],reverse=True);assert len(lam)==3
  all_h=[(a,b,n-a-b)for a in range(n+1)for b in range(a+1)if 0<=n-a-b<=b]
  # q_j=#{i:h_i>=j}. Length1: q1<=2. Length2: q1=3 and q2<=2.
  def allowed(h):
   q=[sum(v>=j for v in h)for j in range(1,max(h)+1)]
   return q[0]<=2 if length==1 else q[0]==3 and q[1]<=2
  hs=[h for h in all_h if allowed(h)]
  assert hs==[h for h in all_h if h[2]==length-1]
  values=[sum(h*d-h*(h+1)for h,d in zip(v,lam))for v in hs]
  cap=max(values);deg=-54-sum(lam)
  rec=dict(id=r['id'],profile=r['profile'],side=side,rank=n,plateau_length=length,ordinary_degrees=lam,actual_degree=deg,capacity=cap,gap=deg-cap,maximizing_heights=[list(h)for h,v in zip(hs,values)if v==cap])
  checked.append(rec)
  if deg>cap:excluded.append(rec)
new={r['id']for r in excluded};assert new=={'G3.11.cb21c818278d','G3.21.7d21add56d56'}
assert len(checked)==78 and len(excluded)==2
assert all(r['side']=='B' and r['plateau_length']==1 and r['ordinary_degrees']==[6,-8,-8] and r['actual_degree']==-44 and r['capacity']==-46 for r in excluded)
remaining=sorted(ids-new);counts=dict(Counter(r['profile']for r in rows if r['id']in remaining))
assert len(remaining)==37 and counts=={'11':29,'12':4,'21':4}
previous=set(prior['historical_excluded_ids'])|{prior['prior_exclusion']['id']}|set(prior['primal_excluded_ids'])|{r['id']for r in prior['new_exclusions']}
assert len(previous)==143 and previous.isdisjoint(ids)
assert previous|new|set(remaining)=={r['id']for r in rows} and len(rows)==182
out=dict(scope='Two further quotient labels excluded by maximal-profile degree capacities, no profile closure.',source_hashes=PINNED,base_commit='1869b195a6c474b973497814b8e04075cba062b4',theorem_commit='8ddbcedc7e01f33ae9aacff56df8da0a33503b57',before=39,after=37,remaining_by_profile=counts,allowed_height_rule='h3=length-1, retaining every nonincreasing nonnegative height vector of the correct rank',new_exclusions=excluded,previous_excluded_ids=sorted(previous),remaining_ids=remaining)
(ROOT/'maximal-profile-degree-envelope-refinement.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: maximal-profile refinement39->37, counts29/4/4; two dual gaps of2; all182 stable IDs preserved.')
