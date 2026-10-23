# Reproduction

First reconstruct the three omitted immutable inputs using the instructions below. Then run from this package directory:

    python3 verify.py
    python3 -O verify.py

Python standard library only; exact rational Q(sqrt5) arithmetic. The computation checks fixed abstract G-characters and degree/rank partitions, not an actual HM/source matrix or chosen point. It retains45 atoms, visits646 recursion states at depth at most5, and compares the entire21-bundle result to its literal list. The structural proof of the invariant Ext bound does not depend on enumeration.

The verifier additionally checks the three invariant extension atoms, five exceptional rows, degree-seven covariant character, three extension Euler identities, a target-only near-miss rejected by the source character, and all three immutable dependency Git-blob identities. Input copies were fetched from their exact commit refs and authenticated.

The geometric correctness of the evaluation resolutions, the averaged equivariant splitting, and the nowhere-zero degree-seven covariant are proved in PROOF.md, not certified by character matching. Independent whole-proof review is recorded separately.

## Reconstruct immutable inputs

INPUTS.json gives repository paths, exact commits, canonical URLs and expected Git-blob SHA1s. For each entry fetch the entire UTF-8 file from Akilleez-QA/read-em-and-weep at its exact ref (not the branch head), retaining its bytes unchanged, and save it as audit-inputs/PR<number>.md. The expected identity is SHA1 of the bytes `blob `, the ASCII decimal byte length, one NUL byte, then the complete file bytes. verify.py checks this identity before accepting the package. The six-file published package omits the three copied inputs. Reconstruct them before running verify.py; review_verify.py is independent of these copied files.

Run this byte-preserving download from the package directory (network access to raw.githubusercontent.com is required):

```sh
python3 - <<'PYINPUTS'
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen

out = Path("audit-inputs")
out.mkdir(exist_ok=True)
for item in json.loads(Path("INPUTS.json").read_text()):
    url = ("https://raw.githubusercontent.com/Akilleez-QA/read-em-and-weep/"
           + item["ref"] + "/" + item["path"])
    with urlopen(url) as response:
        data = response.read()
    identity = hashlib.sha1(
        b"blob " + str(len(data)).encode("ascii") + bytes([0]) + data
    ).hexdigest()
    if identity != item["blob"]:
        raise RuntimeError("Immutable input mismatch: PR" + str(item["pr"]))
    (out / ("PR" + str(item["pr"]) + ".md")).write_bytes(data)
    print("Verified PR" + str(item["pr"]) + ": " + identity)
PYINPUTS
```

A download or authentication failure is not a successful reconstruction. An authenticated repository checkout containing the pinned commits can instead supply identical bytes with `git show <ref>:<path>` using the exact fields in INPUTS.json; verify the recorded Git-blob identity before saving them. Do not substitute current branch versions.

## Independent replay

Run python3 review_verify.py and python3 -O review_verify.py. This independently implements the affine-E8 McKay adjacency recurrence over integers and enumerates all rank-five degree26 multisets before applying the two character constraints:48 raw atoms and277 rank-degree candidates reduce to the same21 literal solutions. This is a different completeness check from verify.py's45-atom character-pruned recursion.
