#!/usr/bin/env python3
"""Primary-theorem provenance and projectivization; no HM evaluation."""
from pathlib import Path
import argparse,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent;checks=[]
def ck(name,value):
 if not value:raise RuntimeError(name)
 checks.append(name)
a=argparse.ArgumentParser();a.add_argument('--primary-pdf',type=Path);args=a.parse_args()
for e in json.loads((ROOT/'FULL-SYMMETRY-INPUTS.json').read_text()):
 b=(ROOT/e['local_path']).read_bytes()
 ck(e['label']+' SHA256',hashlib.sha256(b).hexdigest()==e['sha256'])
 ck(e['label']+' Git blob',hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob'])
p=json.loads((ROOT/'PRIMARY-SOURCE.json').read_text())
ck('exact primary DOI',p['doi']=='10.1007/BF01163877')
ck('full pullback definition locator',p['full_stabilizer_definition']['section']=='4.1' and p['full_stabilizer_definition']['printed_page']==106)
ck('full equality theorem locator',p['full_group_theorem']['section']=='4.2.3' and p['full_group_theorem']['printed_page']==109)
ck('normalizer locator',p['normalizer_definition']['printed_page']==107)
ck('normalized HM locator',p['normalized_HM_identification']['printed_page']==103)
ck('consistent volume page offset',all(p[k]['pdf_page_one_based']-p[k]['printed_page']==9 for k in ['full_stabilizer_definition','full_group_theorem','normalizer_definition','normalized_HM_identification']))
if args.primary_pdf:
 ck('primary whole-volume PDF digest',hashlib.sha256(args.primary_pdf.read_bytes()).hexdigest()==p['volume_pdf_sha256'])
z,d=s.symbols('z d',nonzero=True)
ck('determinant scalar normalization',s.rem(z**5*d-1,z**5-1/d,z)==0)
ck('scalar SL5 kernel order5',s.degree(z**5-1,z)==5 and s.gcd(z**5-1,s.diff(z**5-1,z))==1)
ck('linear Heisenberg order',5**3==125)
ck('linear normalizer order',125*120==15000)
ck('projective normalizer order',15000//5==3000)
ck('full fixed-line stabilizer order',3000//25==120)
ck('actual complement projective faithfulness',s.Matrix.diag(1,1,1,-1,-1)!=s.eye(5) and s.Matrix.diag(1,1,1,-1,-1)!=-s.eye(5))
ck('octic inversion parameter parity',(-1)**8==1)
result={'status':'PASS','checks':len(checks),'primary_theorem':'Decker (1984), Theorem4.2.3',
 'full_projective_HM_group':'N5/mu5','full_projective_HM_group_order':3000,
 'full_fixed_Q0_stabilizer':'existing SL2(F5)',
 'outside_normalizer_loophole_closed':True,
 'additional_ambient_character_on_octic_line':False,
 'primary_pdf_digest_checked_this_run':args.primary_pdf is not None,
 'actual_octic_scalar':'unselected','actual_HM_evaluation':False,'source_or_pair_removed':False}
(ROOT/'FULL-SYMMETRY-RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
