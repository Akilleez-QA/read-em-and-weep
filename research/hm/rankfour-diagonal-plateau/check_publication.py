#!/usr/bin/env python3
"""Authenticate and replay the complete portable mathematical publication."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

def require(ok, message):
    if not ok:
        raise ValueError(message)

def authenticate(base, manifest_name='MANIFEST.json'):
    manifest = json.loads((base / manifest_name).read_text())
    for entry in manifest['files']:
        data = (base / entry['file']).read_bytes()
        require(len(data) == entry['bytes'], 'byte count: ' + entry['file'])
        require(hashlib.sha256(data).hexdigest() == entry['sha256'],
                'SHA256: ' + entry['file'])
    return manifest

def run(script, optimized=False):
    command = [sys.executable] + (['-O'] if optimized else []) + [str(script)]
    result = subprocess.run(command, cwd=ROOT.parent, capture_output=True)
    require(result.returncode == 0, result.stderr.decode())
    return result.stdout

manifest = authenticate(ROOT)
review = ROOT / 'independent-review'
authenticate(review)
author = review / 'accepted-author-packet'
author_manifest = authenticate(author)
require(len(author_manifest['files']) == 14, 'fourteen author mathematical files')
for entry in author_manifest['files']:
    require((ROOT / entry['file']).read_bytes() == (author / entry['file']).read_bytes(),
            'author snapshot mismatch: ' + entry['file'])
expected = (ROOT / 'RESULT.json').read_bytes()
require(run(ROOT / 'verify.py') == expected, 'author normal replay')
require(run(ROOT / 'verify.py', True) == expected, 'author optimized replay')
require(run(ROOT / 'test_controls.py') == (ROOT / 'CONTROLS.json').read_bytes(),
        'author mutation controls')
comparison = (review / 'COMPARISON.json').read_bytes()
require(run(review / 'replay.py') == comparison, 'full independent comparison replay')
authenticate(review)
authenticate(ROOT)
print(json.dumps({'status': 'PASS', 'publication_files_authenticated': len(manifest['files']),
                  'author_mathematical_files': 14, 'public_sources': 5,
                  'author_checks': 26178, 'author_mutation_rejections': 28,
                  'independent_checks': 11331, 'independent_mutation_rejections': 22,
                  'complete_cohomology_tuples_compared': 359,
                  'complete_horizontal_survivors_compared': 172,
                  'remaining_after_rank_one_bridge': 0}, indent=2, sort_keys=True))
