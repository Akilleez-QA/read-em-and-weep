# Reproduce the positive joint embedding checks

The five public files are PROOF.md, verify.py, INPUTS.json, REPRODUCE.md and REVIEW.md. Audit copies are omitted. Reconstruct them from an authenticated clone of Akilleez-QA/read-em-and-weep containing the exact commits in INPUTS.json. From this package directory run, replacing /path/to/clone with that clone:

```sh
python3 - /path/to/clone <<'PYINPUT'
import json,pathlib,subprocess,sys
root=pathlib.Path.cwd(); out=root/'audit-inputs';out.mkdir(exist_ok=True)
for x in json.loads((root/'INPUTS.json').read_text()):
 data=subprocess.check_output(['git','-C',sys.argv[1],'show',x['ref']+':'+x['path']])
 (out/(x['key']+'.md')).write_bytes(data)
PYINPUT
python3 verify.py
python3 -O verify.py
sha256sum PROOF.md verify.py INPUTS.json REPRODUCE.md REVIEW.md
```

Only Python's standard library is required. The verifier authenticates all four Git blobs, checks nine-class fixed representation identities and the finite Koszul indexing argument. It performs no actual HM instance evaluation. The proof's geometric deductions require mathematical review, supplied in REVIEW.md, rather than a claim of machine formalization.
