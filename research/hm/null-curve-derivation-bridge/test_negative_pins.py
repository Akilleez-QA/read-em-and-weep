"""Run only the static checker against temporary, deliberately damaged text inputs."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
results = []
for target in ('inputs/field.py.txt', 'inputs/candidate-field.py.txt', 'reference-methods.txt'):
    for optimized in (False, True):
        with tempfile.TemporaryDirectory(prefix='curve-pin-control-') as directory:
            copy = Path(directory)
            shutil.copytree(HERE, copy, dirs_exist_ok=True, ignore=shutil.ignore_patterns('__pycache__'))
            path = copy/target
            path.write_bytes(path.read_bytes() + b'\n# Deliberate negative pin control.\n')
            command = [sys.executable] + (['-O'] if optimized else []) + [str(copy/'check.py')]
            result = subprocess.run(command, cwd=copy, text=True, capture_output=True)
            if result.returncode == 0 or ('RuntimeError: pin: '+target) not in result.stderr:
                raise RuntimeError('Expected exact pin rejection for '+target)
            results.append({'input':target,'optimized':optimized,'rejected':True})
print(json.dumps({'status':'PASS','negative_pin_controls':results},indent=2,sort_keys=True))
