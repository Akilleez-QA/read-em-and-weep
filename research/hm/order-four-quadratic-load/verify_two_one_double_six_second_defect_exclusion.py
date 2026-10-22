#!/usr/bin/env python3
"""A universal 11-to-7 endpoint section obstruction; no instance evaluation."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
PINNED={'rank-three-quotient-frontier-144.json': 'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad', 'two-one-rank-eleven-endpoint-splittings.json': '4704e794183cb1a2b0bf5069e3baedafeedc9ae186c40dea2917766100d23a16', 'TWO-ONE-PRIMAL-INTERIOR-AND-ENDPOINT-QUOTIENT-CONSTRAINTS.md': 'e7b6bd952f51a1cabd589c4715a346c7180c7b91178d5acf33ba26ff81a84843'}
assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
front=json.loads((ROOT/'rank-three-quotient-frontier-144.json').read_text())
pairs=json.loads((ROOT/'two-one-rank-eleven-endpoint-splittings.json').read_text())['pairs']
ID='G3.21.7d21add56d56';p=pairs[8]
row=next(c for c in front['cases']if c['id']==ID)
A=[[-8,'one'],[6,'one'],[6,'one']]
assert row['profile']=='21' and row['source_index']==8 and row['A']==p['A']==A
assert row['status']=='not_excluded' and p['a']==4 and p['retained_second_defects']==[0,12]
alts=[x for x in p['alternatives']if x['s']==12]
assert len(alts)==1 and alts[0]['torsion']==[[12,4]]
# C=A(-2). The low summand cannot supply top weight4; the equal high pair can.
C=[e-2 for e,n in A]
assert C==[-10,4,4] and [e%10 for e in C]==[0,4,4]
assert C[0]%10!=4
# Every nonzero constant functional on the two identical O4 summands is GL2-equivalent.
# Modifying its selected O4 along D12 changes degree4 to4-12=-8.
J=sorted([C[0],C[1]-12,C[2]])
assert J==[-10,-8,4]
# Published slope theorem: rankM=11, maxdegM<=-4, maxdeg(M^-)<=-5.
rankM=11;degreeM=-48-2*p['a']+12
assert degreeM==-44==-4*rankM
# Equality with the top-degree bound forces all11 ordinary degrees to equal-4.
M_degrees=[-4]*rankM
h0=lambda degrees,t:sum(max(e+t+1,0)for e in degrees)
source=h0(M_degrees,4);target=h0(J,2)
assert source==11 and target==7 and source>target
# M->J(-2) has kernel M^- with H0(M^-(4))=0, requiring the impossible injection.
certificate=dict(scope='One second-defect branch excluded; quotient case and frontier143 count unchanged.',source_hashes=PINNED,id=ID,source_pair_index=8,A=A,excluded_second_defect=12,remaining_second_defects=[0],torsion=[[12,4]],J_degrees=J,M_rank=rankM,M_degree=degreeM,M_degrees=M_degrees,H0_M_four=source,H0_J_two=target,obstruction='The endpoint derivative would inject an11-dimensional section space into a7-dimensional section space.')
(ROOT/'two-one-double-six-second-defect-exclusion.json').write_text(json.dumps(certificate,indent=2)+'\n')
print('PASS:',ID,'second defects {0,12}->{0}: required section injection11->7 is impossible.')
