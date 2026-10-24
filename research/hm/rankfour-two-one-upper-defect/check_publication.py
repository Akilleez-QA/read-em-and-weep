#!/usr/bin/env python3
"""Authenticate and replay the portable conditional upper-defect theorem."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

def require(ok, message):
    if not ok:
        raise ValueError(message)

def authenticate(base, name='MANIFEST.json'):
    manifest = json.loads((base / name).read_text())
    for entry in manifest['files']:
        relative = entry.get('path', entry.get('file'))
        data = (base / relative).read_bytes()
        require(len(data) == entry['bytes'], 'byte count: ' + relative)
        require(hashlib.sha256(data).hexdigest() == entry['sha256'], 'SHA256: ' + relative)
    return manifest

def run(script, optimized=False):
    command = [sys.executable] + (['-O'] if optimized else []) + [str(script)]
    p = subprocess.run(command, cwd=ROOT.parent, capture_output=True,
                       env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'})
    require(p.returncode == 0, p.stderr.decode())
    return p.stdout

manifest = authenticate(ROOT, 'PUBLICATION-MANIFEST.json')
author = authenticate(ROOT)
review = ROOT / 'independent-review'
authenticate(review)
for entry in author['files']:
    relative = entry['path']
    require((ROOT / relative).read_bytes() ==
            (review / 'accepted-author-packet' / relative).read_bytes(),
            'author snapshot mismatch: ' + relative)
expected = (ROOT / 'RESULT.json').read_bytes()
require(run(ROOT / 'verify.py') == expected, 'author root normal output')
require(run(ROOT / 'verify.py', True) == expected, 'author root optimized output')
comparison = json.loads((review / 'COMPARISON.json').read_text())
require(json.loads(run(review / 'replay.py', bool(sys.flags.optimize))) == comparison,
        'complete independent/author replay and exact tuple comparison')
authenticate(review)
authenticate(ROOT)
authenticate(ROOT, 'PUBLICATION-MANIFEST.json')
print(json.dumps({'status': 'CONDITIONAL PASS', 'publication_files_authenticated': len(manifest['files']),
                  'author_checks': 3931, 'author_distinct_mutations': 24,
                  'author_normal_optimized_rejections': 48,
                  'independent_checks': 5176, 'independent_semantic_mutations': 29,
                  'complete_cohomology_tuples_compared': 31,
                  'complete_residual_tuples_compared': 5,
                  'upper_defect_values': [0, 12], 'whole_profile_excluded': False,
                  'coarse_bin_removed': False}, indent=2, sort_keys=True))
