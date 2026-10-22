#!/usr/bin/env python3
"""Two universal cohomology obstructions exclude the full index2 defect20 branch."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
PINNED={'rank-three-quotient-frontier-144.json': 'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad', 'two-one-rank-eleven-endpoint-splittings.json': '4704e794183cb1a2b0bf5069e3baedafeedc9ae186c40dea2917766100d23a16', 'TWO-ONE-PRIMAL-INTERIOR-AND-ENDPOINT-QUOTIENT-CONSTRAINTS.md': 'e7b6bd952f51a1cabd589c4715a346c7180c7b91178d5acf33ba26ff81a84843'}
assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
front=json.loads((ROOT/'rank-three-quotient-frontier-144.json').read_text())
p=json.loads((ROOT/'two-one-rank-eleven-endpoint-splittings.json').read_text())['pairs'][2]
ID='G3.21.d610e381ed75';row=next(c for c in front['cases']if c['id']==ID)
A=[[-8,'one'],[2,'one'],[16,'one']];B=[[-18,'one'],[-4,'one'],[6,'one']]
assert row['source_index']==2 and row['profile']=='21' and row['A']==p['A']==A and row['B']==p['B']==B
assert row['status']=='not_excluded' and p['a']==10
alts=[a for a in p['alternatives']if a['s']==20]
assert [a['torsion']for a in alts]==[[[20,0]],[[20,2]]]
C=[e-2 for e,n in A];weights=[e%6 for e in C]
assert C==[-10,0,14] and weights==[2,0,2]
rankK=14;degK=-54-p['a'];minimumJ=degK-13*(-3)
assert degK==-64 and minimumJ==-25
h0=lambda e:max(e+1,0)
h1=lambda e:max(-e-1,0)
# T0: only the middle component can supply the quotient, so J is forced.
J0=sorted([C[0],C[1]-20,C[2]])
assert J0==[-20,-10,14]
H1K2=-(rankK*3+degK) # H0K2=0 by the published top bound<=-3.
H1J2=sum(h1(e+2)for e in J0)
assert H1K2==22<24==H1J2
# T2: middle component vanishes. If high vanishes, O(-30) splits off J.
assert weights[1]!=2 and C[0]-20==-30<minimumJ
# High must be nonzero on D20: restriction on H0(O16) is injective.
assert h0(C[2]+2-20)==0 and h0(C[0]+2)==0
H0J2_bound=h0(C[1]+2);assert H0J2_bound==3
rankM=11;degM=-48-2*p['a']+20
chiM4=rankM*5+degM
assert degM==-48 and chiM4==7>H0J2_bound
# Riemann--Roch h0M4>=chiM4, while derivative injects H0M4 into H0J2.
out=dict(scope='Full second-defect20 branch excluded for one case; quotient frontier unchanged.',source_hashes=PINNED,id=ID,source_pair_index=2,A=A,B=B,excluded_second_defect=20,remaining_second_defects_relative_to_endpoint=[0,12,24],C_degrees=C,C6_weights=weights,J_minimum_degree=minimumJ,zero_weight_alternative=dict(J_degrees=J0,H1_K_two=H1K2,H1_J_two=H1J2),weight_two_alternative=dict(forbidden_low_kernel_degree=-30,H0_J_two_upper_bound=H0J2_bound,H0_M_four_lower_bound=chiM4))
(ROOT/'two-one-index-two-second-defect-twenty-exclusion.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',ID,'full s20 branch excluded: H1 surjection22->24 or H0 injection>=7-><=3.')
