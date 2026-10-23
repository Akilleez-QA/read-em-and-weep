# Fixed-minor global-cone response certificate

This package supplies a new explicit finite certificate for the source-response
factorization proved geometrically in PR908. It does not instantiate the HM
matrices, select an HM source, remove a source case, or complete the proof.

For a complete fixed global differential D and separately authenticated
physical extraction L, one nonzero maximal minor B gives two multiplication
identities certifying rank and descent. The response on the exact-source
image is L[:,J] adj(B) s[I] / det(B). All source-membership coordinates are
checked before evaluation. Fixed D means no division by a source parameter.
The extension outside the exact image is explicitly not physical.

Read PROOF.md for the full typed theorem, its pivot independence on im D,
its localization boundary, and the remaining physical authentication gates.
PR914's source-specific normalization theorem is preserved as a separate
conditional requirement; it is not inferred from matrix factorization.

Reproduce with Python 3 and SymPy 1.14.0:

    python verify_minor_certificate.py
    python -O verify_minor_certificate.py

Each run reports 144 checks and 17 rejected negative controls. These are
universal polynomial and synthetic finite-dimensional diagnostics, not
actual HM coefficient/rank evaluations and not proof-assistant verification.
Inputs are exact immutable public source copies, authenticated in the checker.
