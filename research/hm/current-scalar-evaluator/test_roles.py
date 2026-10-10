#!/usr/bin/env python3
"""Every synthetic role permutation with resume and Fraction comparison."""
import sys,tempfile,json,contextlib,io,copy
from pathlib import Path
from unittest.mock import patch
from itertools import permutations
import evaluate_quotient as E,validate_quotient as V,test_evaluator as T
from fractions import Fraction as F
count=0
for roles in permutations(range(4)):
 d,k,expected=T.make_case('roles');mapping=dict(zip((1,2,3),roles[1:]))
 for n in d['sumNodes']:
  for c,u,f in n['terms']:
   for v in f:v[0]=mapping.get(v[0],v[0])
 for v in d['root']['factors']:v[0]=mapping.get(v[0],v[0])
 with tempfile.TemporaryDirectory(prefix='hm-role-audit-')as temp:
  out=Path(temp);cfg={'roles':list(roles),'outputDirectory':str(out),'clearingMetadataSHA256':'fixture'};contract={'roles':list(roles),'field':'Q','fixture':'roles'}
  with patch.object(E,'contract_and_inputs',return_value=(cfg,d,k,contract)),contextlib.redirect_stdout(io.StringIO()):
   E.evaluate('fixture',-1);E.evaluate('fixture',840);receipt=V.validate('fixture',expected=False)
  q=json.loads((out/'quotient.json').read_text());got={tuple(row[:3]):F(int(row[3]),int(q['commonDenominator']))for row in q['integerQuotientCoefficients']};assert got==expected
 count+=1
print(json.dumps({'status':'PASS','syntheticRolePermutations':count,'resumeEveryPermutation':True,'fractionOracleEveryPermutation':True,'actualSourceNodesEvaluated':0}))
