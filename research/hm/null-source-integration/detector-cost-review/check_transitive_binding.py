"""Metadata-only AC01 transitive-binding regression control.

python -B check_transitive_binding.py /path/to/repository

Exit 0: both mutations rejected. Exit 1: at least one mutation was accepted.
Only whole_envelope.py is imported. Mutated SR dependencies are never imported
or executed. Originals are unchanged; each mutation uses a temporary copy.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile

p=argparse.ArgumentParser()
p.add_argument('repository',type=Path)
a=p.parse_args()
base=a.repository.resolve()/'research/codex-swarm'

def load(path):
    s=importlib.util.spec_from_file_location('ac01_binding_control',path)
    m=importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m

def files_for_build(root):
    marker=json.loads((root/'detector-realization/producer-ready.json').read_text())
    pins=json.loads((root/'detector-realization/source-pins.json').read_text())
    return {*(row['path'] for row in pins['local_dependencies']),
      'detector-admission/whole_envelope.py','detector-realization/producer-ready.json',
      'scalar-compiler/compiler.py','transport-binding/lift_schema.py',
      'inserted-coefficients/interfaces.py',
      *('detector-realization/'+name for name in marker['files'])}

files=files_for_build(base)
before={name:hashlib.sha256((base/name).read_bytes()).hexdigest()for name in files}
reference=load(base/'detector-admission/whole_envelope.py').build()
cases=[('interfaces_parity','inserted-coefficients/interfaces.py',
        'sign=(-1)**sum','sign=(+1)**sum'),
       ('imported_loop_length','scalar-compiler/compiler.py',
        'for perm in itertools.permutations(range(4)):',
        'for perm in itertools.permutations(range(1000000)):')]
failed=False
for label,name,old,new in cases:
    with tempfile.TemporaryDirectory()as tmp:
        root=Path(tmp)/'swarm'
        for rel in files:
            target=root/rel;target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(base/rel,target)
        target=root/name;source=target.read_text()
        if source.count(old)!=1:raise RuntimeError('Mutation target has changed: '+label)
        target.write_text(source.replace(old,new))
        try:
            output=load(root/'detector-admission/whole_envelope.py').build()
        except ValueError as e:
            print(json.dumps(dict(control=label,mutation_rejected=True,reason=str(e))))
        else:
            failed=True
            print(json.dumps(dict(control=label,mutation_rejected=False,
                                  envelope_unchanged=output==reference)))
after={name:hashlib.sha256((base/name).read_bytes()).hexdigest()for name in files}
if before!=after:raise RuntimeError('Source files changed during control')
raise SystemExit(1 if failed else 0)
