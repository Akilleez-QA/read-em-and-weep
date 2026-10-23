# Reproduce the source125 bb/bc fixed checks

Run with Python3 using only the standard library. The companion verifier is standalone and uses exact rational arithmetic in Q(sqrt(5)); it does not evaluate a selected source map or source coefficients.

## Immutable inputs

Repository: Akilleez-QA/read-em-and-weep.

Source commit: db51525015bb7c5e825833d550d08dedf6f6ea96.

Place these two original files in audit-inputs/ beside verify.py:

1. research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json
   Git blob: fe0afa410d89340d3082dc814277f89fbb582c19
   https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json
2. research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json
   Git blob: 8b5971092f9ef762584912609fd5e9301c4e271d
   https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json

For example, from an authenticated checkout containing that commit:

    mkdir -p audit-inputs
    git show db51525015bb7c5e825833d550d08dedf6f6ea96:research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json > audit-inputs/one-one-endpoint-necessary-pairs.json
    git show db51525015bb7c5e825833d550d08dedf6f6ea96:research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json > audit-inputs/rank-three-quotient-frontier-144.json
    python3 verify.py

The verifier validates the exact Git-blob hashes before reading source index125 and the stable label. It checks only the two fixed original tuples bb=(0,2,0,0,0,0,0,1) and bc=(0,1,1,0,0,0,0,1), not a source scan.

Expected output:

    PASS: 42 fixed Hom checks, exact kernel/cohomology identities, and pinned source125 bb/bc identities.
    Two source exclusions only; no whole-label coverage or current frontier count is certified by this verifier.
    No selected actual source, coefficient, parameter, point, derivative, matrix, instance rank, scan, or large computation.

## Mathematical dependency

The actual-bundle conventions, quadratic gap, and complete-Sym6 obstruction are pinned to the published cf slice:

- PR882, commit ef8ed8d457494608472a2c07de776e9162b2c20f.
- research/hm/profile11-source125-cf-exclusion/PROOF.md.
- https://github.com/Akilleez-QA/read-em-and-weep/blob/ef8ed8d457494608472a2c07de776e9162b2c20f/research/hm/profile11-source125-cf-exclusion/PROOF.md

The latter obstruction is restated in PROOF.md Section7. Arithmetic verification does not replace the actual-connection, saturation, genuine constant-space, and exact-sequence arguments. REVIEW.md binds an independent whole-proof review to the exact candidate bytes. This package does not certify a complete ten-source coverage table or a frontier decrement.
