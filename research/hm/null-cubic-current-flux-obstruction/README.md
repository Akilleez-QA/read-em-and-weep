# Universal cubic-current flux exclusion

Start with RESULT.md for the exact theorem and hand certificate, then REVIEW.md for the independent audit and SOURCE-PINS.md for its bounded premise contract.

Read-only verification (Python 3, standard library):

    python audit_check.py
    python -O audit_check.py

The checker resolves its certificate relative to its file and works from another working directory. It reports row embedding rank 144, 96 derivative columns, image rank 94, augmented rank 95, and certificate pairing 1/8 with M2. It uses only exact formal scalar-coordinate coefficient algebra. The logs audit-normal.json, audit-optimized.json and audit-other-cwd.json record successful independent runs.

The optional author solve.py reconstructs the 96-by-144 system and rewrites its colocated certificate.json. author-normal.txt and author-optimized.txt record its portable runs; author-CHECK.txt is the supplied original run log.

Verify exact file inventory, every bundled hash, source pins, clean public paths, and reproduced normal/optimized/other-working-directory audit logs:

    python verify_bundle.py

The verifier also works from another working directory. SHA256SUMS hashes every bundled file except itself; its exact inventory is enforced. A changed manifest alone is not an external authenticity guarantee, so use the separately supplied archive digest when authenticating delivery.

This is a bounded formal route exclusion. It does not establish nonzero actual source M2, a residue or a global obstruction. No source/model/owner/jet evaluation, physical matrix products, production imports, external writes or publication was performed.
