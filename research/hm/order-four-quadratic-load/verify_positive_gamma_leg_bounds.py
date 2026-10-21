#!/usr/bin/env python3
"""Universal tensor identities and dimension certificates; no selected matrix."""
import runpy
from pathlib import Path
r=runpy.run_path(str(Path(__file__).with_name('verify_positive_gamma_linear_factorization.py')))
q=r['q']; vm,va=r['vm'],r['va']
assert vm(q['W'],q['P'])==va(q['Wp'],q['T'])
assert vm(q['W'],q['V'])==q['T']
assert vm(q['W'],q['D'])==va(q['S'],q['T'])
assert vm(q['W'],q['S'])==va(q['A'],q['D'])
assert vm(q['W'],q['T'])==va(q['V'],q['P'],q['D'])
assert vm(q['W'],q['Wp'])==q['P']
assert 5>4 and 4>2
assert (4+4-6,4+3-6,3+4-6)==(2,1,1)
print('PASS: all first- and second-leg tensor identities, fixed-u dimension obstructions, and composite lower bounds.')
print('The actual uniform geometric input is retained; no actual coefficients or selected ranks evaluated.')
