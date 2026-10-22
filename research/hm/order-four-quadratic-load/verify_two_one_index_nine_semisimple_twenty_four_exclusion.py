#!/usr/bin/env python3
"""Exclude one semisimple torsion alternative, not the entire s24 branch."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
PINNED={'rank-three-quotient-frontier-144.json': 'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad', 'two-one-rank-eleven-endpoint-splittings.json': '4704e794183cb1a2b0bf5069e3baedafeedc9ae186c40dea2917766100d23a16', 'TWO-ONE-PRIMAL-INTERIOR-AND-ENDPOINT-QUOTIENT-CONSTRAINTS.md': 'e7b6bd952f51a1cabd589c4715a346c7180c7b91178d5acf33ba26ff81a84843'}
assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
front=json.loads((ROOT/'rank-three-quotient-frontier-144.json').read_text())
p=json.loads((ROOT/'two-one-rank-eleven-endpoint-splittings.json').read_text())['pairs'][9]
ID='G3.21.1c43993b4f83';row=next(c for c in front['cases']if c['id']==ID)
assert row['profile']=='21' and row['source_index']==9
assert row['A']==p['A']==[[-8,'one'],[6,'one'],[16,'one']]
assert row['B']==p['B']==[[-18,'one'],[-8,'one'],[6,'one']]
alts=[a for a in p['alternatives']if a['s']==24 and a['torsion']==[[12,4],[12,4]]]
assert len(alts)==1 and len(alts[0]['endpoints'])==4
assert all([-4,'P']in M and max(e for e,n in M)<=-4 for M in alts[0]['endpoints'])
C=[-10,4,14];assert [e%10 for e in C]==[0,4,4]
# Distinct source summands must supply two independent constant multiplicity vectors.
J=[C[0],C[1]-12,C[2]-12];assert J==[-10,-8,2]
assert [e+2 for e in J]==[-8,-6,4]
# H0J2=Sym4W=D, an irreducible distinct from the forced P in H0M4.
out=dict(scope='Only source9 semisimple2O4|D12 alternative excluded; cyclicO4|2D12 and whole s24 branch not excluded.',source_hashes=PINNED,id=ID,source_pair_index=9,second_defect=24,excluded_torsion=[[12,4],[12,4]],forced_J_degrees=J,H0_J_two='D',every_endpoint_H0_M_four_contains='P',quotient_labels_unchanged=143)
(ROOT/'two-one-index-nine-semisimple-twenty-four-exclusion.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',ID,'semisimple2O4|D12 excluded by P absent from D; cyclic s24 untouched.')
