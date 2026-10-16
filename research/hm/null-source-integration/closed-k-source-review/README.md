# Independent review of the source-bound closed-K obstruction

The verdict in `REVIEW.md` is **accepted**. The actual carrier pair (0,1) has discrepancy coefficient −20/v1; repeated-last-carrier single-bit mask triples have a nonzero target-pair δK while Ω=0. The common-ambient linkage and coefficient 19 are verified. This refutes the closed-K/H1 shortcut and remains compatible with the full-S4-sign boundary theorem.

## Reproduce the metadata checks

Place this directory anywhere inside the repository. The checker locates the repository root automatically by walking its ancestors, then reads the exact files named in `source-pins.json`:

    python check_metadata_independent.py
    python -O check_metadata_independent.py

Alternatively supply the repository root as the only argument. A checkout containing different versions of the pinned inputs is rejected; the manifest records an immutable commit and Git blob for each input. No network access is used at runtime.

The two source data inputs already live in `research/hm/null-operator-compiler/`. The six reviewed note/checker inputs already live in `research/hm/null-source-integration/complete-raw-remainder/`. No duplicate model or source-formula payload is needed.

The checker reads bytes and sparse metadata only: support intersections, unique exponent records, exact exponent shifts, degrees and leading coefficient records. It never evaluates a source polynomial or point, constructs a source transition or jet, or runs Ω. Its PASS result authenticates these inputs and structural facts; the mathematical frame, trace, valuation and pullback proof is in `REVIEW.md`.

`check-normal.json` and `check-optimized.json` are matching successful receipts from a relocated repository-shaped checkout. `review-receipt.json` records the frozen review digests and scope. `SHA256SUMS` authenticates the packaged files.
