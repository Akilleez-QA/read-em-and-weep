#!/usr/bin/env python3
"""Universal invariant divisor/representation exclusions, not actual zeros."""
import runpy,json
from pathlib import Path
r=runpy.run_path(str(Path(__file__).with_name('verify_pure_cross_block_couplings.py')))
invdegrees=[n for n in range(25) if r['inner'](r['one'],r['sy'](n))]
assert invdegrees==[0,12,20,24]
report={}
for idx,row in enumerate(r['rows'],1):
    candidates=[]
    for p in range(max(d for R,d in row)+1):
        for q in range(7):
            if p+q not in (12,20,24):continue
            dim=sum(r['inner'](r['sy'](6-q),r['vm'](R,r['sy'](d-p)))
                    for R,d in row if d>=p)
            if dim:candidates.append({'p':p,'q':q,'residual_invariants':dim})
    report[idx]=candidates
assert report[1]==report[2]==report[5]==[]
assert report[3]==[{'p':9,'q':3,'residual_invariants':1}]
print('PASS: nonempty off-diagonal common divisor total degree is12,20,24.')
print('PASS: types1,2,5 admit no off-diagonal common divisor.')
print(json.dumps({'necessary_candidates_only':report},indent=2))
