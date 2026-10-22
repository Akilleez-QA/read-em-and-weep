# Narrowing the search space in a proof-repair program

## Adjoint restrictions, exact exclusions, and a remaining higher obstruction

**Craig Ward**  
Working edition **v0.3** | Section-count theorem cutoff: **21 October 2026, 22:57 UTC**; living-paper update **22 October 2026, 00:16 UTC**  
Separate V51 comparison checked through PR640, 22 October 2026.

### Abstract

This working paper organizes a coefficient-free proof-repair program around statements that can be proved, excluded, or left explicitly open. For the adjoint bundle B = End₀(F) in the Horrocks-Mumford setting, the odd part of H⁰(B_Q(4)) vanishes for a general smooth inversion-even quadric Q. The positive multiplication map has rank 33 at the invariant rank-three cone. Its first Bockstein vanishes identically; its second Bockstein kills a five-dimensional summand and is a nonzero quadratic channel of generic rank three on the remaining three-dimensional summand. It follows that the general total section count is either four or five. The distinction is a genuinely higher obstruction, not a missing first-order scalar. We give the dependency chain, explain the exclusions that make it shorter, and distinguish these results from a separate deformation-theoretic construction for V51. Neither the original source-recovery problem nor Weil-class algebraicity is claimed to be solved.

### Reading order

1. [Current theorem and notation](01-current-status.md)
2. [Completed exclusions and superseded routes](02-completed-exclusions.md)
3. [Odd-sector vanishing](03-odd-sector.md)
4. [Positive-sector obstruction calculation](04-positive-sector.md)
5. [Separate V51 deformation geometry](05-v51-comparison.md)
6. [Dependencies, reproducibility, and change log](06-dependencies-and-changelog.md)
7. [Earlier primary and Rao reductions](07-primary-and-rao-reductions.md)
8. [Finite normal-extension tower](08-finite-normal-extension-tower.md)

The files are sections of one paper, not independent claims of completion. Immutable public source links identify the mathematical versions summarized. The proofs are mathematical arguments with supplementary universal checks, not proof-assistant certificates. This edition is maintained in Markdown; no PDF is part of this edition.

### Higher-obstruction update

Section 4 now includes the actual secondary multiplication tensor for β₃ and a distinct square-endpoint Gauss comparison. Saturated-flag geometry gives generic square-endpoint rank at least 26, without improving the rank-36 smoothing bound or deciding the four-or-five alternative.

### Finite normal-extension update

Section 8 classifies exactly two marked G-equivariant fixed-determinant formal-extension isomorphism classes, both represented by ambient bundles; both later scalar gates vanish. Section 4 excludes all rank-two Gauss plateaux, proving generic SF ≥ 3 and positive-square rank ≥ 27. Neither result changes the main section-count theorem. The normalized normal quadratic coefficient is κb² on abc ≠ 0, with κ now proved nonzero geometrically and no parameter-specific cancellation locus. Its numerical value is not computed.

### Central result

For a general smooth inversion-even quadric Q in the specified family,

    h⁰(B_Q(4))₋ = 0,
    4 ≤ h⁰(B_Q(4))₊ ≤ 5,
    4 ≤ h⁰(B_Q(4)) ≤ 5.

The possible values are integers, so the last two quantities are four or five. The argument does not select one of the two alternatives. See the [integrated theorem][G] and the proofs below.

## Pinned source references

[O]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ec080c229105457eafcd2583c8a47b362627a62e/research/hm/order-four-quadratic-load/SPECIAL-D5-OCTIC-NONEXTENSION-EXCLUDES-A12.md
[R]: https://github.com/Akilleez-QA/read-em-and-weep/blob/eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c/research/hm/order-four-quadratic-load/POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md
[F]: https://github.com/Akilleez-QA/read-em-and-weep/blob/846968261441fef2cad247d22b66d37aed3f0f8f/research/hm/order-four-quadratic-load/POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md
[S]: https://github.com/Akilleez-QA/read-em-and-weep/blob/04fb081d710f1d7e175f252601b96dddcd93106e/research/hm/order-four-quadratic-load/POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md
[N]: https://github.com/Akilleez-QA/read-em-and-weep/blob/9f28cb10c38d7a0e29c1eb994594325fea7f22bf/research/hm/order-four-quadratic-load/ACTUAL-SECOND-BOCKSTEIN-NONZERO-BY-ATIYAH-QUINTIC.md
[G]: https://github.com/Akilleez-QA/read-em-and-weep/blob/72aa6fb732a803eb9201f45f1f82e60f54d296b4/research/hm/order-four-quadratic-load/POSITIVE-GENERIC-FOUR-OR-FIVE-SECTIONS.md

7. [Earlier primary and Rao reductions](07-primary-and-rao-reductions.md)
8. [Finite normal-extension tower](08-finite-normal-extension-tower.md)

The earlier full-family reduction is retained in Section 7: both actual quadratic flanks are generically good, but their canonical 20-to-20 extension boundary remains a separate condition. This is logically distinct from the inversion-even four-or-five theorem.

The V51 comparison is updated through PR640: exact order-five U-obstruction, algebraic conductor gluing, and twelve reduced positive-section axes. The full nonreduced jump scheme is not identified.

The fixed actual cubic probe has zero first-normal variation (Section 4.11), not a known zero value. The midpoint square-zero adjoint exists on 2Q but its nonzero scalar obstruction blocks extension to 3Q (Section 8.9).
