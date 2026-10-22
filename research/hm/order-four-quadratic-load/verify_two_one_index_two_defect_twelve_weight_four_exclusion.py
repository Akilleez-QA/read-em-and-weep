#!/usr/bin/env python3
"""One reduced torsion alternative excluded by a forced actual image and degree bound."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
PINNED={'rank-three-quotient-frontier-144.json':'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad','two-one-rank-eleven-endpoint-splittings.json':'4704e794183cb1a2b0bf5069e3baedafeedc9ae186c40dea2917766100d23a16','TWO-ONE-PRIMAL-INTERIOR-AND-ENDPOINT-QUOTIENT-CONSTRAINTS.md':'e7b6bd952f51a1cabd589c4715a346c7180c7b91178d5acf33ba26ff81a84843','NEGATIVE-GAUSS-FLAGS-HAVE-A-FINITE-DEGREE-ENVELOPE.md':'90aa42a0eded9cd3118d086a4ebf82ce98ff4e4c3682e1baaea61e5928f94088'}
assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
rows=json.loads((ROOT/'rank-three-quotient-frontier-144.json').read_text())['cases']
p=json.loads((ROOT/'two-one-rank-eleven-endpoint-splittings.json').read_text())['pairs'][2]
ID='G3.21.d610e381ed75';row=next(r for r in rows if r['id']==ID)
assert row['profile']=='21' and row['source_index']==2
A=[[-8,'one'],[2,'one'],[16,'one']];B=[[-18,'one'],[-4,'one'],[6,'one']]
assert row['A']==p['A']==A and row['B']==p['B']==B and p['a']==10
alternatives=[x for x in p['alternatives']if x['s']==12 and x['torsion']==[[12,4]]]
assert len(alternatives)==1
C=[e-2 for e,n in A];assert C==[-10,0,14]
weights=[e%10 for e in C];assert weights==[0,0,4]
# Reduced target top4 is supplied solely by high; its kernel is high(-D12).
J=[C[0],C[1],C[2]-12];assert J==[-10,0,2]
n=11;degreeM=-48-2*p['a']+12;assert degreeM==-56
lam=sorted(J,reverse=True)
heights=[(a,b,n-a-b)for a in range(n+1)for b in range(a+1)if 0<=n-a-b<=b]
assert len(heights)==16
values=[sum(h*d-h*(h+1)for h,d in zip(v,lam))for v in heights]
capacity=max(values);maximizers=[list(h)for h,v in zip(heights,values)if v==capacity]
assert capacity==-60 and maximizers==[[6,5,0]] and degreeM>capacity
out=dict(scope='Only source2 s12 torsionO4|D12 alternative excluded; no whole-s12 or quotient-label exclusion.',source_hashes=PINNED,theorem_commit='8ddbcedc7e01f33ae9aacff56df8da0a33503b57',id=ID,profile='21',source_pair_index=2,A=A,B=B,second_defect=12,excluded_torsion=[[12,4]],C_degrees=C,C10_weights=weights,forced_J_degrees=J,rank_M=n,degree_M=degreeM,number_of_partitions=len(heights),capacity=capacity,maximizing_heights=maximizers,gap=degreeM-capacity)
(ROOT/'two-one-index-two-defect-twelve-weight-four-exclusion.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',ID,'only s12 weight4 alternative excluded: actual degree−56 exceeds complete capacity−60.')
