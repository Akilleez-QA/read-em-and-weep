# Reproduction and verification scope

The published package contains PROOF.md, REVIEW.md, REPRODUCE.md, verify.py and audit-inputs/manifest.json. It does not duplicate the six upstream source files.

From this package's directory, first download the exact source bytes using the immutable commit and path in each manifest entry. This uses only Python's standard library and checks the Git blob hash before writing each file:

    python - <<'PY'
    from pathlib import Path
    from urllib.request import urlopen
    import hashlib
    import json

    root = Path.cwd()
    inputs = root / 'audit-inputs'
    manifest = json.loads((inputs / 'manifest.json').read_text())
    base = 'https://raw.githubusercontent.com/Akilleez-QA/read-em-and-weep/'
    for item in manifest:
        url = base + item['commit'] + '/' + item['path']
        with urlopen(url, timeout=60) as response:
            data = response.read()
        digest = hashlib.sha1(
            b'blob ' + str(len(data)).encode() + b'\0' + data
        ).hexdigest()
        if digest != item['blob']:
            raise RuntimeError('Source hash mismatch: ' + item['name'])
        (inputs / item['name']).write_bytes(data)
        print(item['name'], digest)
    PY

This writes audit-inputs/ALGEBRA.md, GENERATION.md, BRANCH.md, DOUBLE-LINE.md, FIRST.md and SECOND-NONZERO.md without text decoding, newline normalization or terminal-newline additions. Network access to GitHub is required. If the repository requires authentication, obtain those same immutable files through an authorized authenticated GitHub client instead; retain their exact bytes and verify them against the unchanged manifest. Do not substitute a branch head or a newer revision.

Then run:

    python verify.py
    python -O verify.py

The verifier checks the exact six copied originals against their immutable Git blob IDs, the irreducible-multiplicity bottlenecks, and bounded scalar/formal-series bookkeeping. It does not evaluate any actual HM/source coefficient, parameter, point, derivative, matrix or instance rank. Its checks remain active under optimization.

The mathematical proof is PROOF.md. Its decisive imported nonzero second-Bockstein theorem is the same q0+t a two-term cohomology pencil, not a higher or differently normalized lifting gate. The proof explicitly compares its original first correction with the surjective-block correction using global first-Bockstein vanishing.

The independent whole-proof mathematical review is recorded in REVIEW.md. The tiny verifier checks bookkeeping and source authentication only; it does not replace that review, reprove the imported geometry, or constitute proof-assistant formalization.

No external write, branch creation, publication or merge is part of this package's preparation.
