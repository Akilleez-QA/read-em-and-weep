# Reproduction and scope

Publish only PROOF.md, REVIEW.md, INPUTS.json, REPRODUCE.md and verify.py. The omitted audit-inputs directory consists of exact immutable public repository originals, not unpublished data.

Reconstruct the originals from the same directory as this packet:

```sh
python - <<'PY'
from pathlib import Path
from urllib.request import urlopen
import hashlib,json
root=Path('.'); (root/'audit-inputs').mkdir(exist_ok=True)
for item in json.loads((root/'INPUTS.json').read_text()):
    url='https://raw.githubusercontent.com/Akilleez-QA/read-em-and-weep/'+item['ref']+'/'+item['path']
    b=urlopen(url).read()
    if len(b)!=item['bytes']: raise RuntimeError('length: '+item['key'])
    if hashlib.sha256(b).hexdigest()!=item['sha256']: raise RuntimeError('SHA256: '+item['key'])
    h=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    if h!=item['blob']: raise RuntimeError('Git blob: '+item['key'])
    (root/'audit-inputs'/(item['key']+'.md')).write_bytes(b)
PY
python verify.py
python -O verify.py
```

Python standard library only. The verifier authenticates the four exact public proof originals and checks fixed nine-class character identities, endpoint dimensions, the source2 kernel/quotient degrees and the terminal symmetric type. It does not evaluate any actual HM/source coefficient, point, parameter, jet, matrix or instance rank.

The central mathematical steps are the natural equality E_C=E_{-2}, its identification with the actual embedded NC4 and joint-negative kernel, the independent restricted Koszul isomorphism, and transport of the marked transversality. These are written proofs subject to independent mathematical review, not claims certified by the arithmetic checker alone. The source2 pure-V compatible-radical hypothesis is retained, and neither source realization nor an endpoint-branch selection follows.
