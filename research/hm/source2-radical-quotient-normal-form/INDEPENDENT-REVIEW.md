# Independent review: regular source2 radical quotient normal form

Reviewed 2026-10-23 UTC, separately from the author's self-check and without
altering the earlier radical-image reduction packet.

## Frozen artifacts

- PROOF.md SHA-256: `73d463dbd0e88e34e87b73c1cc49c4c98887d1d124bdea692a24ee1d6b144ce1`
- verify.py SHA-256: `9c61aec41f3e569c78a2ac8e8ffb03067e1c3b123287b7d8944f9523fa2bcd27`
- INPUTS.json SHA-256: `65573e8c9e23f762f894d19f4d5c913297b62a878b0226579111c1b7a4207495`

Verdict: PASS for the stated conditional fixed-negative-pencil theorem.

## Mathematical verification

Read the entire new proof and checker, and the exact PR795 input. Checked
its use against the previously read exact PR794 rank-locus proof.

1. The containment of every radical image in the genuinely embedded NC is
   stronger than a character comparison and is supplied by the pinned
   reconstruction. Outside pure V and the unique exceptional mixed
   direction, ranks18 and9 force equality of image and NC at vertices3
   and4. At vertex2 the character subtraction is V+D. Hence NC/I is
   precisely an isolated initial-vertex system, with zero arrows.

2. PR795 Section3 establishes a genuine short exact sequence of fixed
   pencils NC -> NR -> N8, including the natural connecting-map squares.
   Quotienting by I therefore gives another such exact sequence. This
   step does not assume the original residual bundle or pencil is split.

3. Independently checked the extension lemma: because the quotient maps
   p3 and p4 are isomorphisms, any G-equivariant vector-space section s2
   of p2, together with their inverses, satisfies both arrow squares.
   Naturality and injectivity of p3,p4 prove these identities for every
   fixed pencil variable simultaneously. Semisimplicity over C supplies
   s2. Thus this is a genuine arrow-level splitting, not merely a
   constituent or dimension identity.

4. PR790's genuine first summand is unaffected because I lies in NR.
   Consequently the full quotient is N0 + N8 + (V+D)[2]. PR795 Section2
   specifies N8 as the complete degree-eight osculating evaluation, so
   its isomorphism type, not just its dimensions, is independent of the
   residual endpoint and coupling. No canonical section is implied.

5. Recomputed quotient characters and dimensions:
   (A+2V+2P+3D, 2W'+2S+4T, 2V+3P+2D), hence (32,36,28).
   The exceptional mixed case leaves T at the middle vertex, so p3
   is not invertible there. The proof correctly does not extend its
   splitting argument to that case or to pure V.

6. No Q-compatibility hypothesis is used in this negative-pencil theorem.
   If compatibility holds and Q descends, it may mix the resulting
   summands. The proof does not confuse this negative-arrow decomposition
   with a decomposition of the full Q+tT problem, a horizontal splitting
   of the original residual bundle, or a full-module endomorphism.

## Reproducible evidence

Executed `python verify.py` and `python -O verify.py` independently.
Both complete with745 checks and byte-identical JSON output. All three
input SHA-256 and Git blob checks pass. Inspected synthetic test construction:
its arbitrary sections and nontrivial target coordinate shears test the
fixed-arrow section identities. These tests use no actual HM/source data.

The new mathematical content is the quotient normal-form theorem, not this
review. The theorem remains conditional on its pinned geometric inputs;
this check is not a proof-assistant certificate or a re-proof of every
upstream dependency. It does not remove a catalogue pair, identify a
compatible radical direction, or establish a complete original repair.
