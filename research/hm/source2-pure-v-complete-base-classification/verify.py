#!/usr/bin/env python3
"""Exact bookkeeping for the exhaustive universal scheme classification."""
from pathlib import Path
import hashlib
import itertools
import json
import sympy as S

ROOT = Path(__file__).resolve().parent
checks = []

def check(label, value):
    if not value:
        raise RuntimeError(label)
    checks.append(label)

for item in json.loads((ROOT / 'INPUTS.json').read_text()):
    data = (ROOT / item['local_path']).read_bytes()
    check('sha256 ' + item['label'], hashlib.sha256(data).hexdigest() == item['sha256'])
    blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    check('git blob ' + item['label'], blob == item['git_blob'])

a, b = S.symbols('alpha beta')
forms = {'ell5': b-2*a, 'ell3': b+2*a, 'rank': b+a, 'conic': b}
rows = {k: [S.diff(f, a), S.diff(f, b)] for k, f in forms.items()}
for x, y in itertools.combinations(rows, 2):
    check('distinct projective lines ' + x + ' ' + y, S.Matrix([rows[x], rows[y]]).det() != 0)
product = S.prod(forms.values())
check('open stratum product', S.expand(product - b*(b+a)*(b-2*a)*(b+2*a)) == 0)
check('infinity in open stratum', S.expand(product.subs(a, 0) - b**4) == 0)
check('all exceptional lines homogeneous', all(S.Poly(f, a, b).total_degree() == 1 for f in forms.values()))

cases = [
    {'stratum': 'ell5', 'condition': 'beta=2alpha', 'C5_local_lengths': [6]*6, 'C3_local_lengths': [1]*10, 'extra_reduced_points': 0, 'length': 46},
    {'stratum': 'ell3', 'condition': 'beta=-2alpha', 'C5_local_lengths': [4]*6, 'C3_local_lengths': [3]*10, 'extra_reduced_points': 0, 'length': 54},
    {'stratum': 'rank', 'condition': 'beta=-alpha', 'C5_local_lengths': [4]*6, 'C3_local_lengths': [1]*10, 'extra_reduced_points': 15, 'length': 49},
    {'stratum': 'conic', 'condition': 'beta=0', 'C5_local_lengths': [4]*6, 'C3_local_lengths': [1]*10, 'extra_reduced_points': 12, 'length': 46},
    {'stratum': 'open', 'condition': 'beta(beta+alpha)(beta-2alpha)(beta+2alpha)!=0', 'C5_local_lengths': [4]*6, 'C3_local_lengths': [1]*10, 'extra_reduced_points': 0, 'length': 34},
]
for case in cases:
    check('exact local sum ' + case['stratum'], sum(case['C5_local_lengths']) + sum(case['C3_local_lengths']) + case['extra_reduced_points'] == case['length'])
check('four distinct finite lengths', sorted(set(c['length'] for c in cases)) == [34, 46, 49, 54])
check('length46 schemes distinguished', cases[0]['extra_reduced_points'] != cases[3]['extra_reduced_points'])
check('five disjoint nonzero strata', len(cases) == len(forms)+1)
result = {'status': 'pass', 'count': len(checks), 'checks': checks, 'strata': cases,
          'zero_pair': 'zero ideal sheaf; entire plane base scheme; no finite length',
          'scope': 'nonic component ideal sheaf only; actual coefficient and source occurrence unselected'}
print(json.dumps(result, indent=2))
