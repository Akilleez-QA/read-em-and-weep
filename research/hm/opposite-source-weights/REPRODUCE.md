# Reproduction and boundaries

This package uses three exact original proofs, identified by immutable commit, path, Git blob, SHA256, and byte count in INPUTS.json. All three were retrieved from their pinned public repository versions and compared byte for byte with the working copies. Their earlier geometric dependencies remain in force.

## Reconstruct the omitted original inputs

In a clone of Akilleez-QA/read-em-and-weep containing the three pinned commits, run this Python snippet from this package directory. It extracts raw Git bytes without line-ending normalization and verifies both hashes and the byte count:

    import hashlib, json, pathlib, subprocess
    out = pathlib.Path('audit-inputs')
    out.mkdir(exist_ok=True)
    for entry in json.loads(pathlib.Path('INPUTS.json').read_text()):
        data = subprocess.check_output(['git', 'show', entry['commit'] + ':' + entry['path']])
        assert len(data) == entry['bytes']
        assert hashlib.sha256(data).hexdigest() == entry['sha256']
        framed = b'blob ' + str(len(data)).encode() + b'\0' + data
        assert hashlib.sha1(framed).hexdigest() == entry['git_blob_sha1']
        (out / ('PR' + str(entry['pr']) + '.md')).write_bytes(data)

If the package is outside the clone, supply git's -C option with the clone directory. Alternatively fetch the raw contents of the immutable public URL recorded in each entry and apply the same checks. No branch name or mutable default-branch version substitutes for the recorded inputs.

## Fixed abstract arithmetic

Run:

    python verify.py
    python -O verify.py

The verifier uses explicit RuntimeError checks. Its nine-class character definitions and lambda-ring coefficients follow PR928's published formula, now applied to twist three. It checks the whole Euler character and reduced source E, not only their dimensions. It then uses five fixed binary-stabilizer weights to check source-induction contributions, the exhaustive signed pairings, and the cyclic/semisimple invariant Ext weights. There are no actual HM/source parameters, matrix entries, ranks, point evaluations or scans.

The sheaf-theoretic interpretation, cohomological vanishings, exact evaluation construction, global equivariant Ext identification and local-freeness criterion require the written proof and independent mathematical review. Arithmetic tests do not replace them, and no proof-assistant certification is claimed.

The source/target-character limitation is proved by abstract equivariant models for all six quotient bundles. These models are not asserted to occur in actual HM multiplication. The actual local module and extension scalar remain unevaluated.
