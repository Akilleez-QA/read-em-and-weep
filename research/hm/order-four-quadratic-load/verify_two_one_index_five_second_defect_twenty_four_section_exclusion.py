#!/usr/bin/env python3
"""Two torsion structures give the same universal seven-to-five obstruction."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
PINNED={'rank-three-quotient-frontier-144.json': 'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad', 'two-one-rank-eleven-endpoint-splittings.json': '4704e794183cb1a2b0bf5069e3baedafeedc9ae186c40dea2917766100d23a16', 'TWO-ONE-PRIMAL-INTERIOR-AND-ENDPOINT-QUOTIENT-CONSTRAINTS.md': 'e7b6bd952f51a1cabd589c4715a346c7180c7b91178d5acf33ba26ff81a84843'}
assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
front=json.loads((ROOT/'rank-three-quotient-frontier-144.json').read_text())
p=json.loads((ROOT/'two-one-rank-eleven-endpoint-splittings.json').read_text())['pairs'][5]
ID='G3.21.ed1df480d8d2';row=next(c for c in front['cases']if c['id']==ID)
A=[[-8,'one'],[4,'one'],[16,'one']];B=[[-18,'one'],[-6,'one'],[6,'one']]
assert row['source_index']==5 and row['profile']=='21' and row['A']==p['A']==A and row['B']==p['B']==B
assert row['status']=='not_excluded' and p['a']==12
alts=[a for a in p['alternatives']if a['s']==24]
assert [a['torsion']for a in alts]==[[[24,4]],[[12,2],[12,4]]]
C=[e-2 for e,n in A];weights=[e%10 for e in C]
assert C==[-10,2,14] and weights==[0,2,4]
h0=lambda degree:max(degree+1,0)
# Cyclic top4 can only be supplied by high; socle2 may also receive middle.
assert weights.count(4)==1 and (4-12)%10==2
assert h0(C[0]+2)==0 and h0(C[2]+2-24)==0
cyclic_bound=h0(C[1]+2);assert cyclic_bound==5
# Semisimple tops2,4 force the two distinct source components separately.
assert weights.count(2)==weights.count(4)==1
middle_kernel=h0(C[1]+2-12);high_kernel=h0(C[2]+2-12)
assert middle_kernel==0 and high_kernel==5
semisimple_bound=middle_kernel+high_kernel
rankM=11;degM=-48-2*p['a']+24;chiM4=5*rankM+degM
assert degM==-48 and chiM4==7>max(cyclic_bound,semisimple_bound)
out=dict(scope='One whole second-defect24 branch excluded; quotient case and frontier143 unchanged.',source_hashes=PINNED,id=ID,source_pair_index=5,A=A,B=B,excluded_second_defect=24,remaining_second_defects=[s for s in p['retained_second_defects']if s!=24],torsion_alternatives=[a['torsion']for a in alts],C_degrees=C,C10_weights=weights,cyclic_H0_J_two_upper_bound=cyclic_bound,semisimple_H0_J_two=semisimple_bound,H0_M_four_lower_bound=chiM4)
(ROOT/'two-one-index-five-second-defect-twenty-four-section-exclusion.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',ID,'s24 impossible for cyclic and semisimple alternatives: >=7 sections cannot inject into<=5.')
