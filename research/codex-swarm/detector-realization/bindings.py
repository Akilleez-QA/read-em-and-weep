"""Read-only exact dependency authentication; this performs no field arithmetic."""
from pathlib import Path
import hashlib,json,subprocess
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
REPO=BASE.parents[1]

def authenticate():
    pins=json.loads((HERE/'source-pins.json').read_text())
    for row in pins['local_dependencies']:
        if hashlib.sha256((BASE/row['path']).read_bytes()).hexdigest()!=row['sha256']:raise ValueError('source dependency changed: '+row['path'])
    for row in pins['git_objects']:
        raw=subprocess.check_output(['git','show',row['commit']+':'+row['path']],cwd=REPO)
        if hashlib.sha256(raw).hexdigest()!=row['sha256']:raise ValueError('source object mismatch')
    return pins

def actual_model():
    from raw_engine import require_aggregate_admission
    require_aggregate_admission()
    pins=authenticate();row=next(r for r in pins['git_objects']if r['path'].endswith('hm-pinned-model.json'))
    return json.loads(subprocess.check_output(['git','show',row['commit']+':'+row['path']],cwd=REPO))
