# Source-to-result dependency inventory

This inventory distinguishes public replay inputs from the still-unpackaged
source-regeneration chain. Hashes identify bytes, not mathematical proofs.

## Public inputs supplied here

- All 24 full terminal quotient exports, one for each permutation of four axes.
  `data-pins.json` records their original SHA-256 values.
- The unchanged final result and compact 47-row relation record.
- An exact tuple-exponent arithmetic oracle and the portable downstream
  contraction checker. These need Python 3's standard library only.

These suffice for the commands in README.md. No hidden dependency is needed to
run the supplied-quotient replay. The logical attribution of those coefficients
to the actual geometric class requires the additional chain below.

## Existing public mathematical foundations

- The normalized HM finite model is pinned by
  [PR #5](https://github.com/Akilleez-QA/read-em-and-weep/pull/5), commit
  `add03476d9055aa00e1e00778eea6332cf8e01cc`, including
  `research/hm/ext-model.md` and `research/hm/verify-hm-ext.js`.
- The historical symbolic cochain and complete local End(K) transfer are in
  [PR #31](https://github.com/Akilleez-QA/read-em-and-weep/pull/31), commit
  `5d9ddb2a1e85b3bd6b43111e25e97cfe59d8cc86`. This fixed-chart package is a
  foundation and regression test, not the later weighted all-mask source.
- The separately staged scalar-proof package supplies scalar-chain-map,
  residue and structural-relation checks. Its geometric source hypotheses must
  be matched by the unpublished regeneration chain; they are not discharged by
  the downstream replay alone.

## Still to package for end-to-end regeneration

1. The mixed line/carrier coefficient generator and its normalized model inputs,
   producing the unsigned carrier-tail (2,3,4) coefficient DAG with SHA-256
   `31cd62eb3062801ca19073464c276fbe016fa4024fbcdcf48d3893358e3fcc18`.
2. Exact weighted-mask moments, tagged rational arithmetic, inverse seeds,
   model denominators and scalar prefactors. The recorded
   `build_local_representative.js` combines all 4,096 mask choices using 256
   moment features, applies exactly one J2 minus, and clears denominator
   h1^13 h2^14 h3^14 h4^14. The resulting rational numerator DAG has SHA-256
   `0254c93650e6ca6c1e9cbbb01810704eede98d10d0b75229fcff5d8fa2123e66`.
3. Leading-coefficient extraction in all four axes, normalized free-tag
   circuits, and exact secondary reverse-jet construction for all ordered pairs.
   Historical entry points are `leading_two_jet.js`, the leading-source
   builders, `normalize_free_tags.py`, and `build_compact_secondary_jet.py`.
4. Per-symbol integer clearing and metadata checks: integer weights must satisfy
   D_node*c/product(D_child^e) in Z, and the terminal root denominator is 64.
5. Portable generalized exact evaluators, plain-data resumable configurations,
   and fresh source-hash bindings. The historical evaluators used separate
   v1/v2/v3 programs and bound configurations to original program/data hashes.
   Relocation must not silently reuse those old configuration identities.
6. Independent source identification and terminal factor reconstruction checks,
   including the rational applicability of the integral structural identities.

The checkpoint/archive files are not necessary publication targets. Small
source code and pinned generative inputs should be published separately, with a
fresh-workspace reproduction command and explicit resource needs. Until that
package exists, this PR intentionally claims only public downstream replay of
the recorded scalar result, with source attribution supplied by the separately
recorded calculation rather than reproduced end to end here.
