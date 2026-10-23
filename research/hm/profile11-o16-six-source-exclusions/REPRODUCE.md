# Reproduce the fixed O(16) checks

Use Python 3. The verifier uses only the standard library. It checks fixed universal characters, kernels, Hom spaces and six original source identities, not selected source data or all-twist envelopes.

From the directory containing `verify.py`, create `audit-inputs/` and download exactly these two immutable files into it:

1. `audit-inputs/one-one-endpoint-necessary-pairs.json`

   URL: https://raw.githubusercontent.com/Akilleez-QA/read-em-and-weep/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json

   Git blob SHA1: `fe0afa410d89340d3082dc814277f89fbb582c19`

2. `audit-inputs/rank-three-quotient-frontier-144.json`

   URL: https://raw.githubusercontent.com/Akilleez-QA/read-em-and-weep/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json

   Git blob SHA1: `8b5971092f9ef762584912609fd5e9301c4e271d`

Preserve the exact downloaded bytes, including final newline status. Check each file with `git hash-object PATH`; its output must equal the corresponding Git blob SHA1 above. These are Git object hashes, not the plain SHA1 of the file bytes.

Then run:

```sh
python verify.py
```

Expected final output:

```text
PASS: nine declared kernel atoms; four exact kernels; 80 fixed atomic Hom checks; polar characters; all six original source-edge identities.
No source/model evaluation, support search, all-twist envelope, or current frontier count was performed.
```

The mathematical connection, saturation and branch-exhaustion proofs are in `PROOF.md`; arithmetic checks do not replace them. The original catalogs are necessary overlists, and this check does not produce a current source-frontier count or a whole-label exclusion.
