#!/usr/bin/env python3
"""Universal orbit restriction and endpoint section obstruction; no enumeration."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
PINNED={'rank-three-quotient-frontier-144.json': 'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad', 'two-one-rank-eleven-endpoint-splittings.json': '4704e794183cb1a2b0bf5069e3baedafeedc9ae186c40dea2917766100d23a16', 'TWO-ONE-PRIMAL-INTERIOR-AND-ENDPOINT-QUOTIENT-CONSTRAINTS.md': 'e7b6bd952f51a1cabd589c4715a346c7180c7b91178d5acf33ba26ff81a84843'}
assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
front=json.loads((ROOT/'rank-three-quotient-frontier-144.json').read_text())
p=json.loads((ROOT/'two-one-rank-eleven-endpoint-splittings.json').read_text())['pairs'][9]
ID='G3.21.1c43993b4f83';row=next(c for c in front['cases']if c['id']==ID)
A=[[-8,'one'],[6,'one'],[16,'one']];B=[[-18,'one'],[-8,'one'],[6,'one']]
assert row['source_index']==9 and row['profile']=='21' and row['A']==p['A']==A and row['B']==p['B']==B
assert row['status']=='not_excluded' and p['a']==14
alts=[a for a in p['alternatives']if a['s']==32]
assert len(alts)==1 and alts[0]['torsion']==[[12,4],[20,2]]
C=[e-2 for e,n in A];assert C==[-10,4,14]
# K rank14,degree-68,top<=-3. Quotient J inherits its minimum degree bound.
minimum_J=(-54-p['a'])-13*(-3);assert minimum_J==-29
# At D20 the middle component vanishes; at D12 the low component vanishes.
weights12=[e%10 for e in C];weights20=[e%6 for e in C]
assert weights12==[0,4,4] and weights20==[2,4,2]
assert weights20[1]!=2 and weights12[0]!=4
# If high->T20 vanished, low supplies T20 alone and its kernel splits off in J.
low_kernel=C[0]-20;assert low_kernel==-30<minimum_J
# Therefore high->T20 is nonzero, hence fiberwise invertible on this reduced orbit.
# Twisting by2, its section map from O16 is injective: H0(O(16-20))=0.
h0=lambda e:max(e+1,0)
assert h0(C[2]+2-20)==0 and h0(C[0]+2)==0
image_section_bound=h0(C[1]+2);assert image_section_bound==7
# M rank11,degree-44,top<=-4, while M^- has top<=-5.
rankM=11;degreeM=-48-2*p['a']+32
assert degreeM==-44==-4*rankM
endpoint_sections=rankM;assert endpoint_sections==11>image_section_bound
out=dict(scope='One whole second-defect32 branch excluded; quotient case and frontier143 unchanged.',source_hashes=PINNED,id=ID,source_pair_index=9,A=A,B=B,excluded_second_defect=32,remaining_second_defects=[s for s in p['retained_second_defects']if s!=32],torsion=alts[0]['torsion'],C_degrees=C,C10_weights=weights12,C6_weights=weights20,J_minimum_degree=minimum_J,forbidden_split_low_degree=low_kernel,high_restriction_kernel_degree=C[2]+2-20,H0_J_two_upper_bound=image_section_bound,H0_M_four=endpoint_sections)
(ROOT/'two-one-second-defect-thirty-two-section-exclusion.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',ID,'s32 impossible: actual image admits at most7 sections, while M requires11.')
