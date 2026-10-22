# Proof repair: current progress and remaining obstruction

**Craig Ward** · Working paper v0.3 · 22 October 2026  
**Published-source cutoff: 09:08 UTC.** The section-count theorem dates to 21 October, 22:57 UTC; subsequent results sharpen its obstruction and geometry, not its numerical conclusion.

## The problem and current theorem

This paper develops a proof-repair program in the Horrocks-Mumford setting. Its immediate problem is to determine sections of the trace-free adjoint bundle B=End₀(F) restricted to a general smooth inversion-even quadric Q. The broader source-recovery, higher-lifting and Weil-class algebraicity objectives remain open. Eliminating a possible route or classifying an auxiliary map is progress, but neither substitutes for completing those objectives.

The current theorem is

    h⁰(B_Q(4))₋ = 0,
    h⁰(B_Q(4))₊ ∈ {4,5},
    h⁰(B_Q(4)) ∈ {4,5}.

The signs denote physical inversion eigenspaces. “General” means on a nonempty Zariski-open subset, not on every quadric or special fiber. **The proof does not decide between four and five.** [Integrated theorem][G]; [notation and scope](paper/01-current-status.md).

The positive cohomology map has source dimension 41 and target dimension 37. Its rank at the invariant rank-three cone q₀ is 33. The actual first Bockstein is zero. The second is zero on the D5 summand and has generic rank three on A, raising the generic positive rank to at least 36. The actual third Bockstein is zero, including the additional specialized kernel line at the six second-symbol axes. Thus the final rank is still 36 or 37. [Odd proof][O]; [cone rank][R]; [first vanishing][F]; [second filtration][S]; [actual second nonvanishing][N]; [third vanishing](paper/15-third-vanishing-and-fourth-frontier.md).

## What changed at this cutoff

[Chapter 25](paper/25-complete-two-two-exclusion-and-actual-third-neighborhood-square.md) adds three bounded advances:

1. **The entire (2,2) maximal rank-three profile is excluded.** Endpoint rank drop closes the last three necessary pairs. Six of nine profiles are now excluded; (1,1), (1,2), and (2,1) remain possible. SF≥3 and square rank≥27 do not improve.
2. **The existing corrected J3 is square-zero on actual 3Q.** This is proved for the indicated actual global primitives, with the conic determinant unit retained. It neither computes the primitive nor constructs a 3Q midpoint bundle or evaluates the fourth gate.
3. **The remaining (1,2) profile has bounded degrees and defect.** The original defect is zero or twelve; the twelve-defect branch has just two necessary degree pairs and saturated second dual quotient. Neither is excluded or realized.

The [whole-project progress map](paper/progress-map.md) retains separate fixed denominators: nine profiles, 35 pairs and 2,947 records. The (2,2) histories are 35→34→24→7→3→0 pairs and 2,947→1,880→1,221→723→354→0 records. The 27 scoped inventory universes overlap and are not a global family count. Completed early lanes distinguish excluded from passed cases. There is no overall completion percentage.

## The exact remaining obstruction

After second order in a general negative direction, the surviving source is D5, dimension five, and the remaining target is a line. Since the actual third vanishes, a nonzero fourth or later Bockstein would give rank 37 and four sections. If the last cokernel survives every higher obstruction along the pencil, the rank remains 36 and the count remains five. The last generic finite Smith exponent is **4 ≤ e ≤ 31**, or the cokernel is permanent.

The corrected fourth representative is

    B₄|D5 − B₃|A L.

There are four allowed channels, two visible on squares and two divisible by the discriminant. None of their actual coefficients has been evaluated. The canonical raw cubic and its unique correction L_can are nonzero even though their final third quotient is zero. The corrected fourth source has nonzero parameter trace. These are facts about the input, not the resulting fourth obstruction. [Canonical fourth input and complete test](paper/16-canonical-fourth-input-and-complete-test.md).

Marked exchange of the two actual ambient endpoints now sends one fourth gate to the negative of the other in the same actual second-symbol cokernel. Both gates therefore have the same vanishing locus, but neither value is determined. The endpoints are distinct; odd exchange does not make either a fixed point and force zero. No fourth operation on a midpoint affine line is introduced. [Marked comparison](paper/21-gauss-closure-and-second-normal-residue.md#213-marked-endpoint-exchange-constrains-but-does-not-evaluate-the-fourth-gate).

The next normal calculation must assemble the higher-weight actual affine error and endpoint comparison before ambient division and the final quotient can be evaluated. Chapter 24 now establishes global primitive existence and an exact actual 5Q boundary target, not their explicit evaluation. One nonzero local summand, a nonzero lower source, and the now-determined multiplier do not establish nonzero fourth value. The leading weight-four correction retains both affine terms and the scalar trace; it does not construct a global square-zero midpoint on a third neighborhood. [Exact current boundary](paper/22-full-saturation-and-cartan-koszul-multiplier.md#227-evidence-and-the-remaining-frontier).

## What the lower-source results do establish

The actual lower Atiyah map surjects onto its nine-dimensional target and is injective in a fixed direction except at six reduced nonsquare C5 axes. Every square direction is injective. The subsequent multiplication from the thirty-dimensional lower space to P4 has rank four in every nonzero direction, an eighteen-dimensional common kernel, and a canonical 9→21→12 description on the negative Serre eigenspace. Nonzero or surjective factors do not prove a nonzero composite. [Atiyah input](paper/09-actual-atiyah-factor.md); [lower multiplication](paper/10-midpoint-operator-residue.md#108-the-whole-lower-multiplication-has-uniform-rank-four).

The fixed midpoint operator has an intrinsic residue description Ψ=δ(r). The conic contribution is zero; the vertex quotient is 32→36→P4. The actual cubic support is smooth of genus four, with exact five-torsion, and its double has a 9→36→27 residue filtration. The harmonic cochain, canonical diagonal, vector representative and polar residues retain the actual equation and scalar corrections. Nonzero local opposite-pole terms coexist with the later proved cancellation in the global final third class. [Midpoint residue](paper/10-midpoint-operator-residue.md); [cubic support](paper/11-cubic-support-and-nilpotent-torsion.md); [harmonic cochain](paper/12-harmonic-cochain-and-family-gate.md); [canonical vector cochain](paper/13-canonical-diagonal-and-vector-cochain.md).

The full corrected C5-square lower source is nonzero. Absolute midpoint and Atiyah sections recover the polynomial-nine data lost by the effective vector shadow; the exact comparison is 13→25→12. The actual normal trace has both components nonzero, and a global conic Euler correction completes the homogeneous pair to a genuine G(4) section. These results justify actual lower-source comparisons without declaring every polynomial tangent representative extendible. [Absolute source](paper/17-absolute-lower-source-and-secondary-endpoint.md); [actual cone lift](paper/18-actual-cone-lift-and-nilpotent-trace.md).

Two canonical endpoint evaluations then reconstruct the complete quadratic lower normal-variation family, including both parity components and a common nonzero scale. Every nonzero parameter gives a nonzero entire endpoint map; this does not mean every source vector has nonzero image. Mr. Slop's intrinsic reconstruction and square-secant factorization refine that lower map. The sextic's twelve simple determinant zeros describe saturation on the square conic, not the ambient smoothing pencil. [Actual values](paper/19-actual-endpoint-values-and-last-gauss-quotient.md); [reconstruction and scale](paper/20-reconstructed-endpoint-and-rank-one-frontier.md); [latest fixed-map theorem](paper/21-gauss-closure-and-second-normal-residue.md#217-mr-slop-the-actual-square-secant-map-and-its-sextic-factor).

The new normalization χ̄=−Bλ/(4ν²)n_ap belongs to the fixed midpoint pair's scalar square obstruction. It is distinct from the independent constant C_mult, now determined by the complete homotopy, and does not erase the normal scale markings in the earlier endpoint theorem. Keeping the equation q₀=νq, apolar marking and positive-transition versus bracket sign is essential.

## Gauss geometry and separate comparison problems

The square specialization has rank(ℓ²)=24+rank SF. Saturated-flag degree and endpoint arguments exclude SF ranks one and two, establishing SF ≥ 3 and square rank ≥ 27. Later exclusions remove the entire (3,3), (2,3), (3,2), (3,1), (1,3), and now (2,2) maximal profiles. The remaining possible profiles are (1,1), (1,2), (2,1), not realized geometries. This does not prove SF ≥ 4. It does not improve the generic smoothing rank bound. [Gauss argument](paper/04-positive-sector.md); [full (1,3) closure](paper/22-full-saturation-and-cartan-koszul-multiplier.md#222-full-saturation-excludes-the-entire-13-profile).

On the full P¹⁴ of quadrics, the actual primary and residual flanks are generically good on a common dense open containing smooth quadrics. A canonical 20-to-20 extension boundary remains; good flanks do not prove it invertible. This full-family problem is distinct from the inversion-even theorem. [Primary and Rao reductions](paper/07-primary-and-rao-reductions.md).

The finite normal-extension tower, its two-root structure and the monad-family transitivity are retained with their fixed markings. The separate V51 comparison includes nonreduced section-jump schemes and polarization-linearization results, but does not settle the adjoint gate. [Normal tower](paper/08-finite-normal-extension-tower.md); [V51 comparison](paper/05-v51-comparison.md).

## Attribution, reading order and evidence

The proof chain and its verifiers are developed in [PR543](https://github.com/Akilleez-QA/read-em-and-weep/pull/543). Mr. Slop's complementary PR646–670 results are attributed individually in the relevant chapters; map detection, equation-complex comparisons, lower reconstruction and actual rank conclusions are not collapsed into one claim. Earlier conditional divisor and ramification routes remain in [Chapter 14](paper/14-square-gate-osculation-and-vertex-geometry.md); their nonzero actual third-gate antecedent was later excluded. The paper does not present those conditional curves as actual constructions.

Start with [current theorem and notation](paper/01-current-status.md), then [Chapter 25](paper/25-complete-two-two-exclusion-and-actual-third-neighborhood-square.md) for the latest bounded update. The [twenty-five-chapter index](paper/README.md) supplies the full reading order. The [dependency register and dated change log](paper/06-dependencies-and-changelog.md) preserve intermediate frontiers, exact source links and reproduction instructions. Earlier chapter bodies remain intact with supersession notes; a dated historical “open” statement does not override the current closure.

The latest included PR543 sources are 914f839bc525a1edf52d9734e9844950647419e0 (seven-pair and three-pair refinements), bcb820f06b0d3df35c96f928360f1e973e552c65 (asymmetric degree bounds), 2bd41cac562738b3c526f529d51c56f8b6010632 (actual J3 square-zero), and c8975a41912b28938bc5b912e6637698a9652195 (complete (2,2) exclusion). [Chapter 25](paper/25-complete-two-two-exclusion-and-actual-third-neighborhood-square.md) links each immutable proof and verifier. Earlier chapters preserve their source ledgers. Later unreviewed work is excluded.

These are authored mathematical arguments with supplementary universal identity and character checks, not proof-assistant certificates. No selected Horrocks-Mumford coefficients or actual matrix-rank experiments are used for the summarized conclusions. This working edition is modular Markdown; no PDF is part of it.

## Repository layout and provenance

- **This README** is the current progress paper; [paper/](paper/README.md) holds its focused sections.
- **[upstream/openai-math/](upstream/openai-math/README.md)** preserves the original OpenAI/math snapshot unchanged, including manuscripts, Lean sources, reasoning traces and licenses. See [archive provenance](upstream/README.md).
- **Research proofs and verifiers remain in their existing pull requests and immutable commits.** This reorganization does not merge or certify every research branch. [PR543](https://github.com/Akilleez-QA/read-em-and-weep/pull/543) contains the current adjoint proof chain; [PR1](https://github.com/Akilleez-QA/read-em-and-weep/pull/1) records mathematical coordination.

## Pinned source references


[O]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ec080c229105457eafcd2583c8a47b362627a62e/research/hm/order-four-quadratic-load/SPECIAL-D5-OCTIC-NONEXTENSION-EXCLUDES-A12.md
[R]: https://github.com/Akilleez-QA/read-em-and-weep/blob/eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c/research/hm/order-four-quadratic-load/POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md
[F]: https://github.com/Akilleez-QA/read-em-and-weep/blob/846968261441fef2cad247d22b66d37aed3f0f8f/research/hm/order-four-quadratic-load/POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md
[S]: https://github.com/Akilleez-QA/read-em-and-weep/blob/04fb081d710f1d7e175f252601b96dddcd93106e/research/hm/order-four-quadratic-load/POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md
[N]: https://github.com/Akilleez-QA/read-em-and-weep/blob/9f28cb10c38d7a0e29c1eb994594325fea7f22bf/research/hm/order-four-quadratic-load/ACTUAL-SECOND-BOCKSTEIN-NONZERO-BY-ATIYAH-QUINTIC.md
[G]: https://github.com/Akilleez-QA/read-em-and-weep/blob/72aa6fb732a803eb9201f45f1f82e60f54d296b4/research/hm/order-four-quadratic-load/POSITIVE-GENERIC-FOUR-OR-FIVE-SECTIONS.md
