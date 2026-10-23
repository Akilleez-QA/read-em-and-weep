# Physical source-response normalization coupling

This package proves a new specialized consequence of the pinned PR815/PR816
interfaces, not their generic factorization/transfer algebra again.

After genuine ambient frame alignment, a source row from contraction B used
with a lower nonclosed projection from contraction A changes the proposed
scalar by `-a^3 h eta`. The defect `eta` has an explicit source-only cone
formula. It vanishes exactly when the hybrid normalization is correct as a
regular section; otherwise the correct counterterm is `+a^3 h eta`.

Scalar overlap checks alone allow a global defect in a 13-dimensional trace
space of the affine reconstruction problem. After overlap compatibility, one
independently authenticated full binary-vector calibration at any eligible
base fiber would kill that error. No point was selected or evaluated here,
and no realizability of those thirteen directions by actual HM contraction
changes is asserted.

## Files

- `PROOF.md`: complete deduction, types, hypotheses and stopping boundary.
- `REVIEW.md`: independent final-byte mathematical and diagnostic review.
- `verify_normalization_coupling.py`: standard-library free-word/q-adic test.
- `verification.log`, `verification-optimized.log`: direct replay receipts.
- `SOURCE-MANIFEST.json`: immutable source URLs, commits, exact Git blobs and
  SHA256 digests. `inputs/` contains those exact source bytes.
- `FINAL-MANIFEST.json`, `SHA256SUMS`: final artifact byte manifest.

## Reproduction

Run from this directory:

    python verify_normalization_coupling.py
    python -O verify_normalization_coupling.py

Both modes check 115 exact algebraic identities and 16 negative regressions.
The runtime guard is separate from this algebraic count. The diagnostic
has no third-party dependencies and does not import or evaluate actual HM
source data.

The diagnostic model has the common frame `g=1` built in, tensor/q
compatibility supplied by a single common operator, and the exact-tail
fixture `W=dF`. It exercises paired/mixed normalization and compensation
signs universally in that free-word fixture. It does not authenticate
physical twists/markings, prove the sheaf cohomology calculation, or replace
the general written argument.

This is reviewed written mathematics with supporting universal diagnostics,
not Lean certification. Actual physical contractions, response rows, lower
cochains, rho16 and beta4 remain unconstructed/unevaluated. Nothing in this
package constitutes a source exclusion, a full repair, or an actual-instance
scan. No publication was performed by the package author.
