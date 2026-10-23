# Reproduction and provenance

Run `python3 verify.py` beside the proof. The proof itself supplies all
connection, saturation, exact-intersection, and equivariant divisor arguments.
The verifier checks only bounded declared character identities and exact
original source membership, not selected actual source data or a frontier.

Place these original files in the adjacent `audit-inputs/` directory:

- `one-one-endpoint-necessary-pairs.json`, Git blob `fe0afa410d89340d3082dc814277f89fbb582c19`.
- `rank-three-quotient-frontier-144.json`, Git blob `8b5971092f9ef762584912609fd5e9301c4e271d`.

Both are at commit `db51525015bb7c5e825833d550d08dedf6f6ea96` under
`research/hm/order-four-quadratic-load/` in Akilleez-QA/read-em-and-weep.

The immutable public support proofs are PR796 at
`d2b43060c83328dd5118aee6b9288fcfa0c873ac` and PR802 at
`e484640a6565c278321bf6557860262c1ac1b7df`, at the proof paths cited in
PROOF.md. Original actual-source and strict-top inputs are at the original
pin above. No current frontier total or selected source realization is
a premise or an output of this package.
