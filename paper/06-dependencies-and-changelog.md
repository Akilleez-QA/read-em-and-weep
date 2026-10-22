# 6. Dependencies, reproducibility, and change log

## 6.1 Claim register

1. **Generic odd vanishing.** The final octic nonextension excludes the last residual branch, completing the actual six-to-ten injectivity argument. Main source [O].
2. **Invariant positive rank 33.** The spinor centralizer and moving-line closure identify the eight-dimensional cone kernel. Main source [R]. The cited updated source records first-scalar vanishing, proved in [F].
3. **First positive Bockstein zero.** The actual cyclic Rao identity forces γ = 0. Main source [F].
4. **Second positive Bockstein kills D5.** Ordinary-square filtration leaves only the three-dimensional A input. Main source [S]. Its undecided-scalar boundary is superseded by [N].
5. **Actual second scalar nonzero.** Atiyah differentiation and the nonsplit quintic extension identify and prove nonvanishing of the actual channel. Main source [N].
6. **Generic total section count four or five.** The universal symbol is generically injective on A; combine positive rank at least 36 with odd vanishing. Main source [G].
7. **Separate marked V51 formal universality.** The 636/576 algebraic slices represent marked Artin classes after completion. PR635 adds formal symmetry and delayed breaking; PR637 adds equivariant polarization-class splitting, six 116-dimensional cyclic fixed pair germs with common 12-dimensional U-fixed germ, and the separate unresolved central linearization obstruction. See Section 5; not an input to items 1–6.

8. **Earlier full-family reduction.** General hyperplane sections have a = 0 and b ≤ 1. The unique-cubic square-jet argument gives generic square Rao injectivity. Together with generic primary injectivity, this gives a common smooth open of good flanks and an exact remaining 20-to-20 boundary. Section 7 includes the pinned case-exclusion chain and the specific Segre failure family; it does not assert full-family invertibility or identify representation tensors with polynomial products.

9. **Actual higher-obstruction reductions.** The third class factors through the canonical secondary multiplication tensor [T]. The independent square endpoint is the actual Gauss comparison rank(ℓ²) = 24 + rank SF [A]. A saturated complete-flag degree inequality excludes generic SF rank one, giving endpoint rank at least 26 [L]. None improves the smoothing rank 36 or the four-or-five count.

The principal chain is [R] → [F] → [S] → [N] → [G], with [O] supplying the separate odd closure. Each source also lists its finer geometric dependencies. A citation to a source means the stated result is used with those hypotheses, not that every intermediate result has been restated in this paper.

10. **Finite normal-extension tower.** Fixed determinant, G-equivariance and marked reduction to F|Q₀ leave exactly two formal-extension isomorphism classes, represented by ambient F_r and F_(−r). The first obstruction has exactly two roots; the later scalar gates vanish on both, and subsequent lifts are unique and unobstructed. The actual invariant q₀ map from twist three to twist five is zero. See Section 8 for exact pins and boundaries.
11. **Complete Gauss rank-two exclusion.** The endpoint-flag theorem excludes all three formerly remaining profiles using diagonal contact, saturated projection, and exact characters. Generic SF ≥ 3 and positive-square rank ≥ 27 follow. This does not prove rank thirteen, surjectivity, or improve the four-or-five theorem. See Section 4.10 and its immutable proof/verifier links.

12. **Universal normal quadratic coefficient.** After canonical edge normalization, d(a,b,c) = κb² on abc ≠ 0. There is no parameter-specific cancellation locus. The actual Serre-residue double cover proves κ ≠ 0 and realizes both formal branches, without determining the positive cubic. See Sections 8.7–8.8 and their immutable proof/verifier links.

13. **Fixed-probe variation and midpoint.** The actual fixed cubic probe has zero first-normal variation; its constant value remains open. At the midpoint there is a unique invariant square-zero adjoint lift on 2Q, but the obstruction −c²/(4d) blocks 3Q. No flat kernel or spinor-line lift follows. See Sections 4.11 and 8.9 for immutable proofs and universal verifiers.

## 6.2 Reproducible supplementary checks

The following public scripts check universal identities or formal expansions supporting the argument. They do not evaluate chosen Horrocks-Mumford coefficients and are not substitutes for the geometric proofs.

- [First Bockstein verifier at 4213c50826febe60979eee2848a1030a56e7867f](https://github.com/Akilleez-QA/read-em-and-weep/blob/4213c50826febe60979eee2848a1030a56e7867f/research/hm/order-four-quadratic-load/verify_positive_first_bockstein_vanishing.py).
- [Second square-filtration verifier at 6edf99859f79409b0cee5d9b9588f65e24318869](https://github.com/Akilleez-QA/read-em-and-weep/blob/6edf99859f79409b0cee5d9b9588f65e24318869/research/hm/order-four-quadratic-load/verify_positive_second_bockstein_square_filtration.py).
- [Actual Atiyah/quintic verifier at 7581ad74cbe8b68e795463ef1e814ad02cf51dda](https://github.com/Akilleez-QA/read-em-and-weep/blob/7581ad74cbe8b68e795463ef1e814ad02cf51dda/research/hm/order-four-quadratic-load/verify_actual_second_bockstein_atiyah_quintic.py).

To reproduce an individual check, retrieve the script at its exact commit, inspect its imports and documented input assumptions, and run it with Python 3 from the source directory, supplying any listed dependencies. These checks concern finite representation identities and formal identities. This edition does not introduce new selected-instance rank or coefficient experiments. A passing script is not a formal verification certificate for an entire proof.

## 6.3 Change log for v0.3

- Reorganized the working paper into focused Markdown sections and a short index.
- Recorded completed generic odd vanishing rather than leaving the rank-two residual branch active.
- Recorded the actual invariant-cone positive rank 33.
- Replaced the obsolete unresolved/nonzero first-scalar route with the proved identity γ = 0.
- Added the square-filtration restriction, actual second-scalar nonvanishing, and generic rank-three conclusion.
- Set the main theorem to the precise four-or-five section bound, not four.
- Kept the V51 algebraic-slice result separately attributed and logically separate.
- Retained the original source-recovery, lifting and Weil-class algebraicity boundaries as open.

### Higher-obstruction addendum, 21 October 2026, 23:23 UTC

- Added the actual secondary tensor and its two choice-independence checks.
- Added the exact square-endpoint Gauss derivative comparison.
- Added the saturated-flag exclusion of generic Gauss rank one and the resulting endpoint rank bound 26.
- Preserved the distinction between square endpoints and invariant-cone smoothing; no improvement of the main section-count theorem is claimed.

### Living-paper integration, 21 October 2026, 23:53 UTC

- Integrated the previously prepared higher-obstruction and V51 comparison updates.
- Added Section 8 on the finite normal-extension tower, including the actual invariant multiplication zero and exact determinant/equivariance/marking hypotheses.
- Added the latest necessary rank-two Gauss profile list, without promoting it to a rank-three theorem.
- Retained Craig Ward's author credit and unchanged archive provenance.
- Main result remains odd vanishing and total section count four or five; no algebraization or original-repair completion is claimed.

### Normal coefficient update, 22 October 2026, 00:00 UTC

- Added the universal normal quadratic coefficient law d = κb², retaining determinant and equation-line weights.
- Explicitly left κ unknown and the later formal-extension gates unresolved.
- Did not add any tentative geometric nonvanishing or unfinalized rank-two Gauss exclusion.
- Main result remains four or five sections.

### Completed Gauss exclusion, 22 October 2026, 00:06 UTC

- Superseded the three-profile frontier by complete rank-two exclusion.
- Raised the generic positive-square lower bound from 26 to 27.
- Retained the four-or-five theorem and unknown normal constant κ; no unconfirmed normal nonvanishing added.

### Exact-two normal classification, 22 October 2026, 00:12 UTC

- Replaced the at-most-two frontier by exactly two marked G-equivariant fixed-determinant formal-extension isomorphism classes.
- Recorded ambient representatives F_r and F_(−r), geometric d ≠ 0 and κ ≠ 0, and vanishing of both later gates on both branches.
- Distinguished actual scheme homogeneity, invariant Serre residues, monad uniqueness, and formal restriction from a general algebraization claim.
- Positive cubic and original repair remain open; no unpublished variation consequence included.

### V51 comparison update, 22 October 2026, 00:13 UTC

- Read PR638–640 proofs, diffs and reviews and updated the separately attributed V51 chapter.
- Recorded the exact order-five U-obstruction, conductor section equation, pairwise complementary orbit kernels and twelve reduced axes.
- Retained the nonreduced jump-scheme and full-Γ sufficiency boundaries. This paper integration does not advance the adjoint theorem by itself.

### Variation and midpoint update, 22 October 2026, 00:15 UTC

- Closed the fixed-probe variation-injectivity route: L = 0 before quotient, while the actual constant cubic remains unknown.
- Added the unique square-zero midpoint adjoint on 2Q and the nonzero obstruction to 3Q, without flat-kernel or spinor-lift claims.
- Main count remains four or five; original repair and algebraicity remain open.

## 6.4 Standard for future revisions

A new theorem enters this paper only with its exact hypotheses, actual-map argument, and immutable public source. An allowed channel is not promoted to an actual nonzero map without the missing scalar argument. Special-fiber bounds are not promoted to uniform statements without the needed semicontinuity or base-change argument. When a later proof resolves a previously conditional branch, both the current statement and the register of superseded alternatives should change together.

The next substantive revision should decide the remaining higher positive obstruction or prove a new reduction of it. Until then, the correct current headline remains: odd zero, positive four or five, original repair incomplete.

## Pinned source references

[O]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ec080c229105457eafcd2583c8a47b362627a62e/research/hm/order-four-quadratic-load/SPECIAL-D5-OCTIC-NONEXTENSION-EXCLUDES-A12.md
[R]: https://github.com/Akilleez-QA/read-em-and-weep/blob/eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c/research/hm/order-four-quadratic-load/POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md
[F]: https://github.com/Akilleez-QA/read-em-and-weep/blob/846968261441fef2cad247d22b66d37aed3f0f8f/research/hm/order-four-quadratic-load/POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md
[S]: https://github.com/Akilleez-QA/read-em-and-weep/blob/04fb081d710f1d7e175f252601b96dddcd93106e/research/hm/order-four-quadratic-load/POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md
[N]: https://github.com/Akilleez-QA/read-em-and-weep/blob/9f28cb10c38d7a0e29c1eb994594325fea7f22bf/research/hm/order-four-quadratic-load/ACTUAL-SECOND-BOCKSTEIN-NONZERO-BY-ATIYAH-QUINTIC.md
[G]: https://github.com/Akilleez-QA/read-em-and-weep/blob/72aa6fb732a803eb9201f45f1f82e60f54d296b4/research/hm/order-four-quadratic-load/POSITIVE-GENERIC-FOUR-OR-FIVE-SECTIONS.md

[T]: https://github.com/Akilleez-QA/read-em-and-weep/blob/09b0018bf1f36bcea641c115558ba637f6d63075/research/hm/order-four-quadratic-load/POSITIVE-THIRD-SECONDARY-MULTIPLICATION-TENSOR.md
[A]: https://github.com/Akilleez-QA/read-em-and-weep/blob/02ed933bc3474804560159a71f3a3df5b3b76177/research/hm/order-four-quadratic-load/POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md
[L]: https://github.com/Akilleez-QA/read-em-and-weep/blob/f60e8b675110220b1ce7cc0e4c760ed4f32c8b20/research/hm/order-four-quadratic-load/RANK-ONE-GAUSS-FLAG-DEGREE-EXCLUSION.md
