#!/usr/bin/env python3
"""Combine proved universal Gauss exclusions; no source-instance computations."""
from pathlib import Path
import contextlib
import io
import runpy

here = Path(__file__).parent
with contextlib.chdir(here), contextlib.redirect_stdout(io.StringIO()):
    vp = runpy.run_path(str(here / 'verify_three_v_p4_backward_gauss.py'))
    vd = runpy.run_path(str(here / 'verify_v_d5_backward_gauss.py'))
    zero = runpy.run_path(str(here / 'verify_zero_quadratic_backward_gauss.py'))

frozen = {p[0] for p in vp['frozen']['remaining']}
assert frozen == {p[0] for p in vd['frozen']['remaining']}
assert frozen == {p[0] for p in zero['frozen']['remaining']}
assert len(frozen) == 5
groups = [set(vp['wanted'].values()), {vd['profile']}, {zero['profile']}]
assert [len(g) for g in groups] == [3, 1, 1]
assert all(not groups[i] & groups[j] for i in range(3) for j in range(i))
assert set.union(*groups) == frozen
assert frozen - set.union(*groups) == set()

# The cited persistence theorem bounds both lengths by three. The frozen
# geometric proofs exclude (3,3) and (2,3); the complete union excludes (3,2).
excluded = {(3, 3), (2, 3), (3, 2)}
remaining = {(k, l) for k in range(1, 4) for l in range(1, 4)} - excluded
assert remaining == {(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (3, 1)}
assert max(k+l for k, l in remaining) == 4
assert {(k, l) for k, l in remaining if k+l == 4} == {(1, 3), (2, 2), (3, 1)}
print('PASS: all five terminal types excluded; no (3,2) primal type remains.')
print('PASS: together with frozen (3,3) and (2,3), every rank-three plateau has k+l<=4.')
print('NOT CLAIMED: generic rank-three exclusion, square rank 28, or smoothing closure.')
