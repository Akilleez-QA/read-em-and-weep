# 6. Dependencies, reproducibility, and change log

## 6.1 Claim register

1. **Generic odd vanishing.** The final octic nonextension excludes the last residual branch, completing the actual six-to-ten injectivity argument. Main source [O].
2. **Invariant positive rank 33.** The spinor centralizer and moving-line closure identify the eight-dimensional cone kernel. Main source [R]. The cited updated source records first-scalar vanishing, proved in [F].
3. **First positive Bockstein zero.** The actual cyclic Rao identity forces γ = 0. Main source [F].
4. **Second positive Bockstein kills D5.** Ordinary-square filtration leaves only the three-dimensional A input. Main source [S]. Its undecided-scalar boundary is superseded by [N].
5. **Actual second scalar nonzero.** Atiyah differentiation and the nonsplit quintic extension identify and prove nonvanishing of the actual channel. Main source [N].
6. **Generic total section count four or five.** The universal symbol is generically injective on A; combine positive rank at least 36 with odd vanishing. Main source [G].
7. **Separate marked V51 formal universality.** The 636/576 algebraic slices represent marked Artin classes after completion. See Section 5; not an input to items 1–6.

8. **Earlier full-family reduction.** General hyperplane sections have a = 0 and b ≤ 1. The unique-cubic square-jet argument gives generic square Rao injectivity. Together with generic primary injectivity, this gives a common smooth open of good flanks and an exact remaining 20-to-20 boundary. Section 7 includes the pinned case-exclusion chain and the specific Segre failure family; it does not assert full-family invertibility or identify representation tensors with polynomial products.

The principal chain is [R] → [F] → [S] → [N] → [G], with [O] supplying the separate odd closure. Each source also lists its finer geometric dependencies. A citation to a source means the stated result is used with those hypotheses, not that every intermediate result has been restated in this paper.

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
