# Reproduction

The public packet consists of PROOF.md, INPUTS.json, verify.py, REPRODUCE.md and REVIEW.md. The audit-inputs directory is intentionally omitted. Python3 with its standard library suffices. No actual HM/source coefficients, selected parameters, points, jets, matrices or instance ranks are inputs.

Reconstruct the exact immutable input bytes from INPUTS.json. From the packet directory run:

```python
import hashlib,json,pathlib,urllib.request
root=pathlib.Path('.')
out=root/'audit-inputs'
out.mkdir(exist_ok=True)
for item in json.loads((root/'INPUTS.json').read_text()):
    url=('https://raw.githubusercontent.com/Akilleez-QA/read-em-and-weep/'
         +item['ref']+'/'+item['path'])
    data=urllib.request.urlopen(url).read()
    if len(data)!=item['bytes']: raise RuntimeError('length mismatch')
    if hashlib.sha256(data).hexdigest()!=item['sha256']:
        raise RuntimeError('SHA256 mismatch')
    blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if blob!=item['blob']: raise RuntimeError('Git blob mismatch')
    (out/(item['key']+'.md')).write_bytes(data)
```

Do not normalize line endings, reserialize Markdown, or append a newline. Then run `python3 verify.py` and `python3 -O verify.py`. Both must report PASS. The checker uses exact rational arithmetic in Q(sqrt(5)) on nine fixed group classes, not numerical sampling or actual-instance computation. Its explicit checks remain active with Python optimization enabled.

The mathematical verification is the written proof, especially the two determinant rotations in Section2, the actual residual containment in Section3, and the snake/diagonal compatibility in Section5. The checker verifies immutable provenance and fixed arithmetic only; it does not prove these geometric interfaces automatically.
