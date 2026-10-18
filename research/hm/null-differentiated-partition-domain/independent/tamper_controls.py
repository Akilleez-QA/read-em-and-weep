#!/usr/bin/env python3
"""Mutate only the invented-symbol checker in memory; require rejection."""
from pathlib import Path
import json
import subprocess
import sys
source = Path(__file__).with_name('check_independent.py').read_text()
mutations = {
    'undercharged_hpl': ('homotopy = (10, 2), (9, 5), (4, 2), (6, 3)', 'homotopy = (10, 2), (9, 5), (4, 2), (5, 3)'),
    'false_derivative_divisor': ('reduced = (53,28,28,28,28)', 'reduced = (54,29,29,29,29)'),
    'missing_odd_frame': ('odd = tuple(-2*(i==d)*chart[i]', 'odd = tuple(0*(i==d)*chart[i]'),
    'drop_deleted_prefix': ('all_owners = set(tail) | {h1,h2}', 'all_owners = set(tail)'),
    'erase_repeated_target': ('if len(set(vertices)) != len(vertices):', 'if len(set(v[0] for v in vertices)) != len(vertices):'),
}
results = {}
for name,(old,new) in mutations.items():
    if source.count(old) != 1:
        raise RuntimeError('mutation anchor missing or ambiguous: '+name)
    mutated = source.replace(old,new)
    for flag in ('-B','-BO'):
        run = subprocess.run([sys.executable,flag,'-c',mutated],capture_output=True,text=True)
        if run.returncode == 0 or 'RuntimeError:' not in run.stderr:
            raise RuntimeError('mutation was not rejected by a check: '+name+' '+flag)
    results[name] = 'rejected normally and optimized'
print(json.dumps({'status':'pass','negative_controls':results},indent=2,sort_keys=True))
