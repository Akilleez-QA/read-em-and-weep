"""Exact torsion-character refinement; abstract identities only."""
from pathlib import Path
import runpy,io,contextlib,json
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
 r=runpy.run_path(str(ROOT/'verify_two_two_symmetric_quotient_constraints.py'))
hc,va,vs=r['hc'],r['va'],r['vs']
@r['lru_cache'](None)
def orbit(s,t):
 return va(hc(((s,'one'),),t,True),vs(-1,hc(((s-12,'one'),),t,True)))
passed=[];failed=[]
for record in r['records']:
 if record['defect']==0:continue
 A,B=record['A'],record['B'];target=r['negdual'](B)
 residues=[s for s in (0,2,4,6,8) if all(va(hc(target,t,True),vs(-1,hc(A,t,True)))==orbit(s,t) for t in range(10))]
 (passed if residues else failed).append(dict(record,orbit_weights=residues))
assert len(passed)==259 and not failed
assert len({(x['A'],x['B']) for x in passed})==7
assert all(len(x['orbit_weights'])==1 and x['orbit_weights'][0] in (2,6) for x in passed)
print('Twelve-defect records passing / failing exact orbit characters:',len(passed),len(failed))
print('Passing pairs:',len({(x['A'],x['B']) for x in passed}))
print('Failing pairs:',len({(x['A'],x['B']) for x in failed}))
(ROOT/'two-two-twelve-orbit-torsion-characters.json').write_text(json.dumps(dict(passed=passed,failed=failed),indent=2)+'\n')
