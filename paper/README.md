# Narrowing the search space in a proof-repair program

## Adjoint restrictions, exact exclusions, and a remaining higher obstruction

**Craig Ward**  
Working edition **v0.3** | Section-count theorem cutoff: **21 October 2026, 22:57 UTC**; living-paper draft through **22 October 2026, 06:18 UTC**  
Separate V51 comparison includes PR641 and PR644; three-channel family dependency pinned to PR643, 22 October 2026.

### Abstract

This working paper organizes a coefficient-free proof-repair program around statements that can be proved, excluded, or left explicitly open. For the adjoint bundle B = End₀(F) in the Horrocks-Mumford setting, the odd part of H⁰(B_Q(4)) vanishes for a general smooth inversion-even quadric Q. The positive multiplication map has rank 33 at the invariant rank-three cone. Its first Bockstein vanishes identically; its second Bockstein kills a five-dimensional summand and is a nonzero quadratic channel of generic rank three on the remaining three-dimensional summand. It follows that the general total section count is either four or five. The actual third Bockstein now vanishes identically, including at every specialized direction. The remaining generic finite Smith exponent is 4–31, or the last cokernel is permanent. The distinction is a fourth-or-later obstruction, not a missing first- or third-order coefficient. We give the dependency chain, explain the exclusions that make it shorter, and distinguish these results from a separate deformation-theoretic construction for V51. Neither the original source-recovery problem nor Weil-class algebraicity is claimed to be solved.

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
10. [Midpoint operator residue and global quotient](10-midpoint-operator-residue.md)
11. [Cubic support and nonreduced torsion](11-cubic-support-and-nilpotent-torsion.md)
12. [Explicit harmonic cochain and family reduction](12-harmonic-cochain-and-family-gate.md)
13. [Canonical diagonal and actual vector cochain](13-canonical-diagonal-and-vector-cochain.md)
14. [Conditional square-gate osculation and vertex geometry](14-square-gate-osculation-and-vertex-geometry.md)
15. [Actual third vanishing and the fourth-order frontier](15-third-vanishing-and-fourth-frontier.md)
16. [Canonical fourth input and complete test](16-canonical-fourth-input-and-complete-test.md)
17. [Absolute lower source and secondary endpoint](17-absolute-lower-source-and-secondary-endpoint.md)
18. [Actual cone lift and nonzero nilpotent trace](18-actual-cone-lift-and-nilpotent-trace.md)
19. [Actual endpoint values and last Gauss quotient](19-actual-endpoint-values-and-last-gauss-quotient.md)

The files are sections of one paper, not independent claims of completion. Immutable public source links identify the mathematical versions summarized. The proofs are mathematical arguments with supplementary universal checks, not proof-assistant certificates. This edition is maintained in Markdown; no PDF is part of this edition.

### Current obstruction and Gauss status

[Section 15](15-third-vanishing-and-fourth-frontier.md) proves zero for the actual third gate through exact meromorphic-source comparison, square-channel vanishing, actual cokernel-fiber vanishing at six axes, and the septic-conic argument. The extra specialized kernel line is checked separately. The six second-symbol degeneracy points are length-four complete intersections (x²,y²). Nonzero lower classes and the full local opposite-pole residue in Section 13 coexist with global final cancellation. Section 15.7 adds the corrected fourth representative B₄|D5−B₃|A L and four allowed channels, two square-visible and two discriminant-divisible. Fourth coefficients remain unevaluated. [Chapter 16](16-canonical-fourth-input-and-complete-test.md) proves the canonical raw cubic and L_can nonzero, identifies the effective 13 → 25 → 12 lower quotient and forced corrected-source trace, and gives the complete 3+1 ideal-sheaf-jet plus C5-square-fiber test. None of these results computes a fourth coefficient.

The full corrected C5-square lower source is nonzero, already in the canonical realization Cminus≅H⁰(D,O_D(−2,10)). Absolute midpoint and Atiyah sections recover the previously lost polynomial-nine data. A global trace null-homotopy isolates the secondary endpoint P4, whose actual normal variation is now nonzero; its nilpotent square-shadow component must still be retained in the adjoint lift. Secant restriction plus parameter trace reconstructs lower families as 13→11+2, while the two endpoint channels restrict isomorphically as 2→2. None of these results evaluates a fourth coefficient. See [Chapter 17](17-absolute-lower-source-and-secondary-endpoint.md). The rank-two Gauss branch now has only (8,2), after four complete quotient-shape exclusions. Its twenty possible K splittings reduce to eleven after the doubled-sector exclusion. These are a different counting unit from the earlier quotient/type pairs. The rank-one branch and entire (3,1) profile remain open.

The actual normal trace has both α≠0 and β≠0, with β proved nonzero by restriction to 2C. Global wedge cancellation fixes γ=−1/(12ν) in the shared normalization. The nonzero conic Euler cocycle completes the homogeneous pair to a genuine global G(4) section, with full root/triangular gluing and Hartogs extension. The lowest η diagonal is nonzero. A regular scalar-lift commutator correction contributes to the displayed old-K terms in degree twelve, not four; the full actual normal-K comparison remains open, while Chapter 19 now evaluates the lower endpoint on two canonical inputs. See [Actual cone lift and nonzero nilpotent trace](18-actual-cone-lift-and-nilpotent-trace.md). PR660 gives secant fourth-family restriction plus one intrinsic cubic jet; PR661 gives two-channel endpoint detection at one C5-square secant fiber. Neither evaluates an actual endpoint or fourth value.

[Chapter 19](19-actual-endpoint-values-and-last-gauss-quotient.md) computes the actual lower endpoint at a=t²: X⁴ gives zero, while XY³ gives c_eta·3k/(Bc)[Y/z]≠0 with c_eta nonzero but unassigned. This proves injectivity of the invariant normal line into the two-dimensional endpoint-family space. Every nonzero parameter has a nonzero entire endpoint map, and every square has a nonzero secant restriction. Neither statement concerns individual inputs or evaluates the fourth obstruction.

Section 4.13 excludes all 28 formal types in the entire (3,2) Gauss profile. Every hypothetical maximal rank-three plateau satisfies k+l ≤ 4; not every rank-three case is excluded. Generic SF ≥ 3 and positive-square rank ≥ 27 remain unchanged.

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

### Structural chapters and preserved conditional results

Sections 9–13 retain the actual Atiyah input, corrected midpoint operator boundary, cubic support and torsion, harmonic cochain, canonical diagonal, vector representative and polar residue test. Their nonzero factors do not imply nonzero composites. Section 15 supplies the later actual third evaluation; it does not declare every lower cohomology class or unquotiented P4 value zero.

Mr. Slop's complementary PR646–654 remain separately attributed: marked-pair and equation-complex comparisons, the global restriction and last-jet quotients, corrected extractor, unique equivariant normal form, conditional fixed divisors, ramification sheets and distinct Gram spectral geometry. The nonzero-gate antecedents in Sections 12.7 and 14.1 are now excluded for the actual operator; the conditional degree-eighteen square curve is not an actual construction. The unconditional vertex no-Tor statement remains valid.

The current source pins are [86e5aed779f0ff64a83cf9dbe169cb2e7283b346](https://github.com/Akilleez-QA/read-em-and-weep/tree/86e5aed779f0ff64a83cf9dbe169cb2e7283b346/research/hm/order-four-quadratic-load) for third vanishing and [dfbdd9f5e18e0a2506d2ea30b01f58f6b21f570b](https://github.com/Akilleez-QA/read-em-and-weep/tree/dfbdd9f5e18e0a2506d2ea30b01f58f6b21f570b/research/hm/order-four-quadratic-load) for the completed adjacent-profile exclusion. The [dependency register and dated history](06-dependencies-and-changelog.md) retain the earlier stages, their evidence and supersession. The fourth-order structural reduction is pinned separately to [2f81e3510505ad842fb9bb00ff3a667cd36ea17f](https://github.com/Akilleez-QA/read-em-and-weep/tree/2f81e3510505ad842fb9bb00ff3a667cd36ea17f/research/hm/order-four-quadratic-load). The snapshot cutoff is 06:18 UTC; only published results are included. The new canonical inputs are pinned to 4e16e69c776bd85506341b5bb785f0d8a396bd3e, the actual lower comparison and complete test to c85c756d333281eccefdb77c4899db4f923d768e, and the preceding geometric criterion to Mr. Slop’s PR658 at 95004606fb8b2ec51ecd97e2fde0d6d0ff328407. Chapter 17 adds absolute-source results at a90d2ddd38f9ed8c28fcd8ca965f2479a12c9bf2, trace/reconstruction/envelopes at c9c54d50c94fc17cad7a14fce93b31bb22b9ea5f, the complementary PR659 test at f4f2a5d4e3351da91796b9e7af78707150eac878, and the smallest-quotient exclusion at 0a95ace992688a278ef211d981e2fdef1bd5f1ad.

Chapter 18 adds the actual trace and wedge results at 74feee620e0027d567df88d964e76cb9d7209c0c and the actual global cone lift at 30bed21aac919087a4b40f4d1079997eb21d1390. Complementary tests are pinned to PR660 at fe195ead045076fc27bfa95686fe13d738df694f and PR661 at 1325647fd916bf2daa71b11efeae6d52cfefa2cd. Chapter 19 adds the actual endpoint theorem and (6,2) exclusion at fb574c01207099eeb63960da5cb23ad2f2498a84, and the all-direction actual corollary and doubled-sector exclusion at 229e621948e9f6d80902080ad227993da3f0dced. Its structural whole-fiber input is Mr. Slop’s PR662 at f75a18fd411350adda35dedf18751eee002a39bc. Later normal-scale and higher-division work is outside this cutoff.
