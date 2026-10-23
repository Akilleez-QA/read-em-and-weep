#!/usr/bin/env python3
"""Authenticate this portable mathematical review and replay every checker."""
from pathlib import Path
import hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parent
manifest=json.loads((ROOT/'MANIFEST.json').read_text())
for entry in manifest['files']:
    raw=(ROOT/entry['file']).read_bytes()
    if len(raw)!=entry['bytes'] or hashlib.sha256(raw).hexdigest()!=entry['sha256']:
        raise RuntimeError('package authentication failed: '+entry['file'])
for folder in (ROOT,ROOT/'author'):
    for flags in ([],['-O']):
        run=subprocess.run([sys.executable,*flags,str(folder/'verify.py')],capture_output=True,text=True,cwd='/tmp')
        if run.returncode or run.stdout!=(folder/'RESULT.json').read_text():
            raise RuntimeError('replay failed: '+str(folder))
run=subprocess.run([sys.executable,str(ROOT/'test_controls.py')],capture_output=True,text=True,cwd='/tmp')
if run.returncode or run.stdout!=(ROOT/'CONTROLS.json').read_text():
    raise RuntimeError('negative control replay failed')
print(json.dumps({'status':'PASS','authenticated_files':len(manifest['files']),'author_replays':2,'independent_replays':2,'negative_controls':6},indent=2,sort_keys=True))
