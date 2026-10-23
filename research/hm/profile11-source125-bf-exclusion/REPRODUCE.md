# Reproduce the source125 bf checks

Use Python 3. The verifier uses only the standard library. It checks fixed universal characters and one exact original source identity, not selected source data or a new all-twist envelope.

From the directory containing verify.py, create audit-inputs/ and download the following two immutable files there, preserving their exact bytes and final newlines:

1. one-one-endpoint-necessary-pairs.json

   https://raw.githubusercontent.com/Akilleez-QA/read-em-and-weep/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json

   Git blob SHA1: fe0afa410d89340d3082dc814277f89fbb582c19

2. rank-three-quotient-frontier-144.json

   https://raw.githubusercontent.com/Akilleez-QA/read-em-and-weep/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json

   Git blob SHA1: 8b5971092f9ef762584912609fd5e9301c4e271d

These are Git object hashes, not plain SHA1 hashes of the file bytes. The verifier checks the Git object hashes itself before reading either JSON.

Run:

```sh
python3 verify.py
```

Expected output:

```text
PASS: high-D kernel, 42 fixed internal Hom checks, polar and cubic-T identities, original source125 bf identity.
No source/model evaluation, support search, all-twist envelope, or current frontier count was performed.
```

The connection, saturation, exact-intersection and branch-exhaustion arguments are in PROOF.md. Arithmetic checks do not replace them. The audit inputs are necessary overlists, and this single-source result supplies neither a current source-frontier count nor a whole-label exclusion.
