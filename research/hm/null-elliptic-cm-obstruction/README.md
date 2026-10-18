# Elliptic CM: source-bound constant-intertwiner obstructions

## Lead result
For the pinned HM gamma presentation, the 375 constant-coefficient equations in 250 unknowns have full column rank: M gamma(v)=gamma(Sv) N forces M=N=0. The independent implementation uses a different coefficient assembly and integer fraction-free elimination. The identity-action control has rank 249 and admits (I15,I5). The independent implementation also replays every selected-row step of the author's exact pivot certificate.

Read CONSTANT-GAMMA-ADDENDUM.md, then REVIEW.md. RESULT.md retains the full source report, its earlier diagonal-cycle and prime-divisor carrier obstructions, contextual downstream caveats, and the 26-even/4-odd polynomial-weight classification. Weight parity does not establish detector characters. No result here excludes rational gauges or proves bundle non-isomorphism or detector vanishing.

## Portable checks
Run these standard-library scripts from any working directory:

- python verify_inventory.py
- python check.py
- python check_weights.py
- python check_constant_independent.py
- python constant_gamma_check.py

All substantive checks have normal and optimized (-O) logs. The three independent checks also have other-working-directory logs. The author checker reproduces its two certificate files deterministically. No production module is imported and no physical source, jet, numeric sample, or polynomial-matrix product is evaluated. Only pinned literal supports, integer exponent labels, and the explicitly bounded constant-coefficient linear system are used.

## Evidence and scope
model.json is the complete inert 16,803-byte frozen model. SOURCE_EXCERPTS.json contains bounded exact coordinate, rational decoder, curve and homogeneous-convention excerpts; PINS.json gives immutable public URLs and whole-source hashes. The original decoder excerpts were compared byte-for-byte to their pinned source ranges. weight-metadata.json preserves the inherited 30-request metadata and its own interpretation; only its integer weight-parity statements are independently checked here. This packet does not re-prove that metadata's geometric classification or authenticate a current remote repository head.

SHA256SUMS inventories every other regular file. verify_inventory.py rejects changed, missing or extra files, including stale logs. Files are self-contained and contain no machine-specific source paths.
