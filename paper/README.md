# Narrowing the search space in a proof-repair program

## Adjoint restrictions, exact exclusions, and a remaining higher obstruction

**Craig Ward**  
Working edition **v0.3** | Section-count theorem cutoff: **21 October 2026, 22:57 UTC**; living-paper draft through **22 October 2026, 03:14 UTC**  
Separate V51 comparison includes PR641 and PR644; three-channel family dependency pinned to PR643, 22 October 2026.

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
9. [Actual Atiyah factor and six exceptional directions](09-actual-atiyah-factor.md)
10. [Midpoint operator residue and remaining global value](10-midpoint-operator-residue.md)
11. [Cubic support and nonreduced torsion](11-cubic-support-and-nilpotent-torsion.md)
12. [Explicit harmonic cochain and remaining family gate](12-harmonic-cochain-and-family-gate.md)
13. [Canonical diagonal and actual vector cochain](13-canonical-diagonal-and-vector-cochain.md)
14. [Conditional square-gate osculation and vertex geometry](14-square-gate-osculation-and-vertex-geometry.md)

The files are sections of one paper, not independent claims of completion. Immutable public source links identify the mathematical versions summarized. The proofs are mathematical arguments with supplementary universal checks, not proof-assistant certificates. This edition is maintained in Markdown; no PDF is part of this edition.

### Higher-obstruction update

Section 4 now includes the actual secondary multiplication tensor for β₃ and a distinct square-endpoint Gauss comparison. Saturated-flag geometry gives generic square-endpoint rank at least 27, without improving the rank-36 smoothing bound or deciding the four-or-five alternative.

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

The earlier full-family reduction is retained in Section 7: both actual quadratic flanks are generically good, but their canonical 20-to-20 extension boundary remains a separate condition. This is logically distinct from the inversion-even four-or-five theorem.

The V51 comparison now includes the exact nonreduced section-jump schemes: the positive-section ideal is J⁵, with generic transverse length 1365 along the twelve axes and an embedded identity. Full Γ-linearizability holds exactly for polarization powers divisible by five, with a unique action on each admissible fixed line bundle. These are separate comparison results, not a solution of the adjoint gate.

Section 8.7 replaces the missing historical three-channel-family citation with PR643's standalone proof of the exact subbundle torus and its gauge/coordinate transitivity. The replacement supports the normal coefficient and two-extension chain without computing the positive cubic.

The fixed actual cubic probe has zero first-normal variation (Section 4.11), not a known zero value. The midpoint square-zero adjoint exists on 2Q but its nonzero scalar obstruction blocks extension to 3Q (Section 8.9).

### Actual lower-factor update

Section 9 proves the actual nine-dimensional image, classifies the six exceptional fixed directions, and describes the full parameter-family cokernel as a six-point elementary modification. Every square direction is injective for this lower map. Its subsequent annihilating multiplication and normal operator lift remain distinct; no composite nonvanishing is inferred.

### Actual midpoint operator update

Section 10 identifies the fixed actual secondary value with the global boundary of a corrected midpoint operator residue. The corrected Hessian symbol now matches the actual midpoint lift; the canonical harmonic constants are 1/112, −1/20 and 1/144, and the conic boundary vanishes. The vertex quotient is now the exact 32 → 36 → P4 sequence, with M₈ = A O(6)⊕V O(4), and both split square-boundary channels are nonzero. The actual residue still must be inserted and taken through the actual second-symbol quotient.

Section 4.13 adds the (2,3) Gauss exclusion, all three two-D5, six further large quadratic-section, single-V and all three single-P4 quadratic exclusions in (3,2), and the bound of two for its restricted cubic pairing. Together with the prior two exclusions, at most 13 of 28 formal primal types remain, with no improved numerical rank bound. Section 10 also attributes the distinct existing-pair rigidity and classical equation-complex acyclicity to Mr. Slop's PR646–647, without transferring their invariant vanishings to the positive operator. The four-or-five theorem remains unchanged.


### Cubic-support update

Section 11 identifies the actual smooth genus-four support with exact order-five T, the intrinsic 9 → 36 → 27 residue filtration, and the nilpotent boundary with kernel D5 and quotient P4. The ambient line O_(2D)(1,-1) is not five-torsion: its fifth power is the actual nonzero quintic-relation class. A unique nilpotent correction produces the torsion lift. These results structure the residue calculation without determining the corrected operator's value. These cubic-support and degree-eight results are pinned to PR543 commit 14fc90d90f74998c10ea9f2b45cf5b8aeac96bae.


### Uniform lower multiplication and the canonical last jet

Section 10.8 adds the actual negative-Serre-sector quotient at PR543 commit 6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0: the lower multiplication has rank four for every nonzero negative quadratic, an eighteen-dimensional common kernel on C, and a canonical 9/21/12 quotient on C⁻. Section 10.9 separately attributes PR648–649's 35/31 global restriction quotient and canonical deepest-quintic P4 slice. Neither route computes the actual corrected operator class or Ψ; the four-or-five theorem is unchanged. The later single-V and three single-P4 exclusions reduce the formal Gauss frontier to at most thirteen.


### Explicit cochain and family normalization

Section 12 gives the accepted harmonic formula for the actual leading square-ideal cochain, keeping the local equation-frame scalar r₀ and effective connection scalar Λ. The upper connection has a² times one actual quartic map, whose determinant has twelve simple zeros. The exact family coefficient reductions 11 → 6 → 2 and trace-free 9 → 5 → 2 organize the remaining evaluation, but do not reduce the previously known two-dimensional cubic gate. These operator results are pinned to d7a6ad65f2142d39fbacc01784b7620fc3a9e42c. The single-V exclusion at 4ac12f3ec8f465ef8dcbb1b6a17698fc674afe80 and three single-P4 exclusions at 15adb8e5ea61f07e87df6a0044b7375e580fe7f3 leave at most 13 of 28 formal primal types; numerical bounds and the original repair status remain unchanged.


### Corrected extractor and unique equivariant normal form

Section 11.4 adds Mr. Slop's PR650 map-level bridge: remove an actual reduced kernel lift before taking the first-normal quintic remainder. Section 12.6 adds PR651's uniquely equivariant splitting of the rank-eleven second-symbol kernel and unique polynomial normal form for a whole equivariant family with zero third class. The full rank-twenty-six lower-kernel splitting remains noncanonical. Neither result computes an actual coefficient; the two final gates remain open, independently of the later reduction to at most 13/28 formal types.


### Canonical diagonal, vector representative and conditional failure loci

Section 13 identifies the actual upper quartic as a Gram composite, proves regular nilpotence at its twelve simple exceptional fibers, fixes the diagonal by the canonical residue inverse, and retains the full source/target-frame distinction in a vector-cochain representative. The scalar-extension correction remains; no global class is evaluated. These sources and the harmonic-frame clarification are pinned to ebc38deccf2d0abcdd7b185c73dd57bae8682f59. Section 12.7 attributes PR652's fixed-divisor classification and finite base-length bounds 70/40, excess 46/16, entirely conditional on a nonzero actual third gate.


### Scalar surjectivity and conditional square osculation

Section 13.5 proves the actual canonical scalar map surjects onto the fifteen-space, with kernel 1⊕P4⊕D5, without inferring nonvanishing of the final shadow. Section 13.1 attributes to Mr. Slop's PR653 the ramification-sheet distinction and exceptional double-root criterion. Section 14 separates the conditional degree-eighteen square series, exact ramification B₂+2B₃ and fifth-jet quotient O(78), from the unconditional local calculation that the vertex double point adds no Tor. The Gaussian, both-branch three-type Gauss exclusion and square-osculation sources are pinned to 15adb8e5ea61f07e87df6a0044b7375e580fe7f3. The cutoff is 03:14 UTC; the generic four-or-five theorem is unchanged.
