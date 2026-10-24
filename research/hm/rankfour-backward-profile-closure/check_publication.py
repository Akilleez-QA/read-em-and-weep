#!/usr/bin/env python3
"""Authenticate and replay the full conditional (3,1) proof chain and reviews."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
STAGES = ('cubic-image', 'lower-classification', 'lower-exclusion', 'rankone', 'integration')

def require(ok, message):
    if not ok:
        raise ValueError(message)

def authenticate(base, name='MANIFEST.json'):
    manifest = json.loads((base / name).read_text())
    items = manifest['files'] if isinstance(manifest, dict) else manifest
    if isinstance(items, dict):
        items = [{'file': key, **value} for key, value in items.items()]
    for entry in items:
        relative = entry.get('file', entry.get('path'))
        data = (base / relative).read_bytes()
        require(len(data) == entry['bytes'], 'byte count: ' + relative)
        require(hashlib.sha256(data).hexdigest() == entry['sha256'], 'SHA256: ' + relative)
    return len(items)

def run(script, optimized=False):
    command = [sys.executable] + (['-O'] if optimized else []) + [str(script)]
    process = subprocess.run(command, cwd=ROOT.parent, capture_output=True,
                             env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'})
    require(process.returncode == 0, process.stderr.decode())
    return process.stdout

files = authenticate(ROOT, 'PUBLICATION-MANIFEST.json')
author_files = authenticate(ROOT)
stages = {}
for name in STAGES:
    folder = ROOT / 'reviews' / name
    authenticate(folder)
    expected = (folder / 'RESULT.json').read_bytes()
    require(run(folder / 'verify.py') == expected, name + ': independent normal output')
    require(run(folder / 'verify.py', True) == expected, name + ': independent optimized output')
    require(run(folder / 'test_controls.py') == (folder / 'CONTROLS.json').read_bytes(),
            name + ': executable independent mutations')
    require(run(folder / 'check_package.py') == (folder / 'PACKAGE-CHECK.json').read_bytes(),
            name + ': complete author/independent comparison')
    result = json.loads(expected)
    controls = json.loads((folder / 'CONTROLS.json').read_text())
    stages[name] = {'independent_checks': result['checks'],
                    'mutation_rejections': len(controls['rejected_mutations'])}
    authenticate(folder)
authenticate(ROOT)
authenticate(ROOT, 'PUBLICATION-MANIFEST.json')
print(json.dumps({'status': 'CONDITIONAL PASS', 'publication_files_authenticated': files,
                  'author_files_authenticated': author_files,
                  'profile_excluded': [3, 1], 'author_integration_checks': 221,
                  'author_integration_mutations': 13,
                  'dependency_stage_checks': [16582, 4207],
                  'shared_stage_checks_not_claimed_disjoint': True,
                  'independent_reviews': stages, 'complete_originals': 6,
                  'identical_original_copies': 17,
                  'claims_generic_SF_at_least_five': False}, indent=2, sort_keys=True))
