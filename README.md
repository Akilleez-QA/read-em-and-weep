# Proof repair: current progress and remaining obstruction

**Craig Ward** · Working paper v0.3 · 22 October 2026  
Section-count theorem cutoff: 21 October, 22:57 UTC; living-paper draft through: 22 October, 05:24 UTC (22 October, 01:24 EDT). Positive operator sources: PR543 third vanishing at 86e5aed, fourth reduction at 2f81e35, canonical fourth-input results at 4e16e69 and lower comparison/test at c85c756, absolute lower sources at a90d2ddd and trace/reconstruction/envelopes at c9c54d50 and smallest Gauss quotient exclusion at 0a95ace9; Gauss plateau closure through dfbdd9f; complementary extractor, normal-form, divisor, ramification and spectral results: PR648–659; distinct equation comparisons: PR646–647. V51 comparison: PR641 and PR644; family dependency: PR643.

## The problem

This repository develops a proof-repair program in the Horrocks-Mumford setting. The immediate problem is to determine the sections of the trace-free adjoint bundle B = End₀(F), restricted to a general smooth inversion-even quadric Q. The broader source-recovery, lifting, and Weil-class algebraicity objectives remain open. Narrowing the possible maps and eliminating incorrect routes is part of the mathematical result, not a substitute for a completed proof.

## Main result so far

For general smooth Q in the specified family,

    h⁰(B_Q(4))₋ = 0,
    h⁰(B_Q(4))₊ ∈ {4, 5},
    h⁰(B_Q(4)) ∈ {4, 5}.

The subscripts are the physical inversion eigenspaces. “General” means a nonempty Zariski-open set, not every quadric or special fiber. The current proof does **not** decide between four and five. [Integrated theorem][G].

## Why the search space is smaller

1. **Odd sector closed.** The last special D5 octic nonextension excludes the remaining residual rank-two branch. The actual six-to-ten smoothing map is injective, giving generic odd vanishing. [Proof][O].
2. **Positive cone rank fixed.** At the invariant rank-three cone q₀, the actual positive map has source dimension 41, target dimension 37, rank 33, kernel A ⊕ D5 of dimension eight, and cokernel P4 of dimension four. [Proof][R].
3. **The first-order route is excluded.** The cyclic Rao identity aξ = q₀ζₐ makes the entire first Bockstein zero. The former scalar γ is zero, not unknown; nonzero individual linear legs do not imply a nonzero composite. [Proof][F].
4. **Second order advances three ranks, not four.** The square filtration kills D5. The remaining A-to-P4 quadratic family has a nonzero actual scalar by Atiyah differentiation of the nonsplit quintic extension, and its universal symbol has generic rank three. Hence generic positive rank is at least 36. [Filtration][S]; [actual nonvanishing][N]; [rank consequence][G].

## Earlier reduction on the full quadratic family

On the full P¹⁴ of quadrics, the actual primary map is generically injective and the actual residual map is generically surjective on a common dense open containing smooth quadrics. The section reductions a = 0, b ≤ 1 and the unique-cubic normal-jet argument establish the required square Rao injectivity. What remains there is a canonical 20-to-20 extension boundary δ; good flanks do not prove δ invertible. A specific Segre family of decomposable representation tensors is provably bad for full invertibility. These full-family statements must be distinguished from the later inversion-even analysis. [Primary and Rao reductions](paper/07-primary-and-rao-reductions.md).

## The remaining gate

After second order in a general negative direction, the surviving source is D5, of dimension five, and the remaining target is a line. The actual third Bockstein now vanishes identically, including the extra specialized kernel line at the six axes. A nonzero fourth or later Bockstein would give rank 37 and four sections. If the last target survives all higher obstructions along the pencil, the rank stays 36 and the section count stays five. The last generic finite Smith exponent is therefore 4 ≤ e ≤ 31, or the cokernel is permanent. The corrected fourth representative is B₄|D5−B₃|A L, with four allowed channels; none of its coefficients has been evaluated. No higher nonvanishing is claimed here. [Third-vanishing theorem and proof](paper/15-third-vanishing-and-fourth-frontier.md). Closing this gate would still not automatically solve the original source or algebraicity problem.

## New fourth-input results and complete test

The canonical raw cubic is nonzero and fills the second-symbol image in every direction, despite its zero final third quotient. Its unique canonical correction L_can is nonzero and onto A; arbitrary Schur gauges require comparison. The corrected fourth source has a forced nonzero parameter trace. The vector cochain R retains only the effective twelve-space, not the full lower class: an exact 13 → 25 → 12 comparison identifies the missing data, and keeping the full homogeneous normal matrix still loses the polynomial nine-space. The missing positive P4 contains normal variation, but is not proved filled or nonzero.

The entire fourth D5 family is determined by its first ideal-sheaf jet at one semisimple axis and one C5-square fiber, with test dimensions 3+1. This is not ordinary derivative evaluation, and the C5 fiber alone detects only one of two square channels. Mr. Slop’s PR658 supplies the preceding square-plus-fiber kernel and full-square-plus-jet criterion. All four actual fourth coefficients remain unevaluated. [Canonical fourth input and complete test](paper/16-canonical-fourth-input-and-complete-test.md).

## Absolute lower source and secondary endpoint

The full corrected C5-square lower source is nonzero, already in the canonical realization Cminus≅H⁰(D,O_D(−2,10)). Absolute midpoint and Atiyah sections recover the previously lost polynomial-nine data. A global trace null-homotopy leaves a precise but unevaluated secondary endpoint P4; its nilpotent square-shadow component must still be retained in the adjoint lift. Secant restriction plus parameter trace reconstructs lower families as 13→11+2, while the two endpoint channels restrict isomorphically as 2→2. None of these results evaluates a fourth coefficient.

Mr. Slop’s PR659 gives a complementary secant-plus-C5-square 3+1 fourth-family test, distinct from the axis ideal-jet test. Separately, section envelopes first reduce the five rank-two Gauss quotient overlists from 140 to 77 necessary quotient/type pairs. Exact derivative kernels then exclude the smallest quotient entirely, leaving four shapes and 73 necessary pairs, not realized geometries or an exclusion of the (3,1) profile. [Absolute lower source and remaining endpoint](paper/17-absolute-lower-source-and-secondary-endpoint.md).

## New higher-obstruction reductions

The actual third Bockstein is now expressed by a canonical secondary multiplication tensor, β₃,ₐ(hξ) = Ψ(a,h,[aζₐ]) modulo im β₂,ₐ. Separately, multiplication by a square ℓ² equals an actual Gauss-map comparison: rank(ℓ²) = 24 + rank SF. A saturated-flag degree argument rules out generic rank one for SF, since it would force deg E ≤ −221 rather than −54. Diagonal contact, saturated endpoint projections, and exact cohomology characters also exclude rank two, giving generic SF rank at least three and square-endpoint rank at least 27, not rank thirteen or surjectivity. [Complete exclusion](paper/04-positive-sector.md#410-complete-rank-two-exclusion-by-endpoint-flags). These are different specializations: this bound does not improve the smoothing rank 36 or the generic four-or-five count, and third-order nonvanishing is now excluded. [Detailed reductions](paper/04-positive-sector.md#47-the-third-obstruction-as-an-actual-secondary-multiplication-tensor).

The fixed actual cubic probe has zero first-normal variation, even before the second-symbol quotient. This variation map is distinct from the third lifting correction L used in the fourth-order formula. Its vanishing closes the variation-injectivity route negatively, but did not by itself determine the absolute cubic value. The separate third-vanishing theorem now gives zero in the final quotient. [Exact scope](paper/04-positive-sector.md#411-the-fixed-actual-cubic-probe-has-zero-normal-variation).

## Actual lower-map classification

The lower Atiyah multiplication now surjects onto its actual nine-dimensional target. In a fixed direction it is injective except at exactly six nonsquare C5 axes, where it loses one rank; every square direction is injective. Its entire parameter-family cokernel is a specific six-point modification of a split vector bundle. These resolve the Atiyah input map, not the absolute secondary operation applied afterward. [Proof and precise boundary](paper/09-actual-atiyah-factor.md). The subsequent multiplication from the thirty-dimensional lower cohomology to P4 is now determined too: it has rank four for every nonzero negative quadratic, with an eighteen-dimensional common kernel and a canonical 9 → 21 → 12 description on the negative Serre eigenspace. These factor results alone do not determine the corrected operator class; its final third quotient is now zero. [Uniform lower multiplication](paper/10-midpoint-operator-residue.md#108-the-whole-lower-multiplication-has-uniform-rank-four).

## Actual midpoint operator residue

The fixed actual secondary value now has the exact description Ψ = δ(r), where r is the corrected midpoint operator defect in H⁰(ω_(2Z)(5))₊ and ker δ is the image of global H⁰(G(4))₊. Full-frame covariance and invariant negative-defect acyclicity match the corrected Hessian symbol with the actual midpoint lift. The harmonic constants are 1/112, −1/20 and 1/144; the required generator primitive and equation factors remain part of the correction. The conic contribution to δ is zero. On the degree-eight vertex part, the exact global quotient is 32 → 36 → P4, with M₈ = A O(6)⊕V O(4). After dividing by the scalar nilpotent class, both split boundary channels are nonzero. These structural results do not by themselves compute the residue; the later actual-source comparison proves zero in its final third quotient. [Midpoint operator calculation](paper/10-midpoint-operator-residue.md).

The actual cubic support is a smooth genus-four curve D with exact five-torsion T = O_D(1,-1). Its double gives an intrinsic 9 → 36 → 27 residue filtration and a nonzero nilpotent boundary onto P4. The ambient torsion relation fails on 2D by the actual nonzero quintic-extension class, although a uniquely corrected five-torsion lift exists. None of these nonzero auxiliary classes has been identified with Ψ. [Cubic geometry and precise limit](paper/11-cubic-support-and-nilpotent-torsion.md).

The leading actual operator cochain is now explicit in harmonic-transition form, with its local equation-frame and effective-scalar corrections retained. Its upper connection has an a² factor multiplying one actual quartic map. That quartic factor has rank three away from twelve simple exceptional points and rank two there. The family coefficient reductions are 11 → 6 → 2, or 9 → 5 → 2 in trace-free normal form. The final two-dimensional gate was already known; normalization removes no cubic channel. The diagonal is now fixed by the canonical residue inverse, and the Gram primitive gives an actual vector-cochain representative in the fifteen-to-twelve quotient. Source connection and target trace frames remain distinct. The actual scalar correction surjects onto its fifteen-dimensional target, with kernel 1⊕P4⊕D5, and the actual quintic scalar cup is an isomorphism on that fifteen-space. A twelve-point polar form gives removable double layers and exact simple-layer quotients 36−21=15 and 36−27=9. The final residue criterion tests the full second-symbol annihilator, which is a line only outside its degeneracy scheme Σ. For a square rooted at a C5 polar point and the detectable h-character, u has a simple root and the full opposite-pole residue is nonzero. The full local contribution remains nonzero, but exact meromorphic-source comparison now proves cancellation in the global final third class. [Harmonic cochain and family gate](paper/12-harmonic-cochain-and-family-gate.md); [canonical diagonal and vector cochain](paper/13-canonical-diagonal-and-vector-cochain.md).

The separate Gauss analysis now excludes the entire (3,2) profile: all 28 necessary formal primal types are impossible. Together with the (3,3) and (2,3) exclusions, every hypothetical rank-three maximal plateau has k+l ≤ 4. This does not exclude every rank-three plateau or prove generic SF ≥ 4. The established bounds remain SF ≥ 3 and positive-square rank ≥ 27. [Complete profile exclusion](paper/04-positive-sector.md#413-further-rank-three-gauss-configurations-and-pairings-are-excluded).

Mr. Slop's complementary PR648–649 results remove the entire scalar-rescaling layer and identify the global restriction defect as a 35/31 quotient with a canonical deepest-quintic P4 slice. PR650 identifies this route with the double-cubic nilpotent boundary by corrected reduced-part subtraction and quintic extraction. PR651 makes the second-symbol kernel splitting uniquely equivariant and supplies an exact no-obstruction normal form, without evaluating its actual coefficients. PR652 conditionally classifies the fixed divisor of any nonzero third gate: none off the discriminant-divisible line, and exactly one discriminant factor on it. The finite primitive base schemes have length at most 70 or 40, with excess at most 46 or 16 beyond the second-symbol scheme. The nonzero-gate antecedent is now excluded for the actual operator. These remain structural classifications of allowed nonzero channels, not actual failure curves. [Canonical last-jet route](paper/10-midpoint-operator-residue.md#109-a-complementary-global-restriction-and-canonical-last-jet-route).

Mr. Slop's distinct PR646–647 results give rigidity of existing marked first-normal pairs and invariant acyclicity of the classical equation complex. Their negative and twist-two groups differ from the positive operator target; they do not determine Ψ or lift the midpoint to 3Q. [Comparison and attribution](paper/10-midpoint-operator-residue.md#1010-separate-pair-rigidity-and-the-classical-equation-complex).

If the actual square third channel is nonzero, it is a basepoint-free degree-eighteen series with exact ramification B₂+2B₃, an immersive birational parametrization and fifth-jet quotient O(78). The vertex double point on a square cone contributes no additional Tor term. The nonzero antecedent is now excluded: this is not a curve constructed from the actual gate. The local no-Tor result remains valid. [Square-gate geometry](paper/14-square-gate-osculation-and-vertex-geometry.md).

## Exact auxiliary normal-extension classification

With fixed determinant, G-equivariance, and marked reduction to the actual bundle on Q₀, there are exactly two formal-extension isomorphism classes, both represented by ambient bundles F_r and F_(−r). The first scalar gate has two distinct roots; the gates to 4Q and 5Q vanish on both, and all later steps are uniquely liftable and unobstructed. The actual invariant map q₀:H¹(B(3))ᴳ→H¹(B(5))ᴳ is zero. No general algebraization theorem is used, and this auxiliary classification is distinct from the now-proved positive third vanishing. [Full statement and proof chain](paper/08-finite-normal-extension-tower.md).

The canonically normalized normal quadratic coefficient is now reduced to d = κb² throughout the monad subbundle locus abc ≠ 0. The actual scheme and Serre-residue double-cover argument proves κ ≠ 0 without computing its numerical value. PR643 supplies the verified standalone three-channel-family premise, replacing the missing historical citation. This closes that dependency in the auxiliary formal classification, not the later positive third-vanishing proof or original repair. [Coefficient reduction and family proof](paper/08-finite-normal-extension-tower.md#87-the-quadratic-coefficient-has-one-universal-scalar).

The midpoint of the two extendable points has a unique invariant square-zero adjoint lift on 2Q, but the obstruction −c²/(4d) ≠ 0 blocks 3Q. No flat kernel or spinor-line lift is inferred. [Midpoint theorem](paper/08-finite-normal-extension-tower.md#89-the-midpoint-has-a-square-zero-adjoint-but-cannot-extend-to-q₃).

## Separate V51 comparison

The independent primary-geometry line attributed to Mr. Slop supplies 636/576-dimensional algebraic slices, formal symmetry breaking, and equivariant polarization-class splitting. Its conductor-gluing family has section counts 10 at the identity, 5 on one active axis, and 0 when at least two coordinates are active. PR641 determines the nonreduced positive-section ideal J⁵: twelve axes with generic transverse length 1365 and an embedded identity. PR644 proves that L₀ᵐ is fully Γ-linearizable exactly when 5 divides m, with a unique action on each admissible fixed line bundle. Neither comparison result closes the adjoint problem. [Section-jump schemes](paper/05-v51-comparison.md#510-every-determinantal-section-threshold-and-the-embedded-identity); [full-group criterion](paper/05-v51-comparison.md#511-full-γ-linearization-has-exactly-the-same-divisibility-criterion).

## Read the working paper

- [Paper index and abstract](paper/README.md)
- [Current theorem and notation](paper/01-current-status.md)
- [Completed exclusions and superseded routes](paper/02-completed-exclusions.md)
- [Odd-sector proof](paper/03-odd-sector.md)
- [Positive-sector proof](paper/04-positive-sector.md)
- [Separate V51 deformation geometry](paper/05-v51-comparison.md)
- [Dependencies, reproducible checks, and change log](paper/06-dependencies-and-changelog.md)
- [Earlier primary and Rao reductions](paper/07-primary-and-rao-reductions.md)
- [Finite normal-extension tower](paper/08-finite-normal-extension-tower.md)
- [Actual Atiyah factor and six exceptional directions](paper/09-actual-atiyah-factor.md)
- [Midpoint operator residue and global quotient](paper/10-midpoint-operator-residue.md)
- [Cubic support and nonreduced torsion](paper/11-cubic-support-and-nilpotent-torsion.md)
- [Explicit harmonic cochain and family reduction](paper/12-harmonic-cochain-and-family-gate.md)
- [Canonical diagonal and actual vector cochain](paper/13-canonical-diagonal-and-vector-cochain.md)
- [Conditional square-gate osculation and vertex geometry](paper/14-square-gate-osculation-and-vertex-geometry.md)
- [Actual third vanishing and the fourth-order frontier](paper/15-third-vanishing-and-fourth-frontier.md)
- [Canonical fourth input and complete test](paper/16-canonical-fourth-input-and-complete-test.md)
- [Absolute lower source and secondary endpoint](paper/17-absolute-lower-source-and-secondary-endpoint.md)

## Repository layout and provenance

- **This README** is the current progress paper; [paper/](paper/README.md) holds its focused sections.
- **[upstream/openai-math/](upstream/openai-math/README.md)** preserves the original OpenAI/math snapshot unchanged, including manuscripts, Lean sources, reasoning traces and licenses. See [archive provenance](upstream/README.md).
- **Research proofs and verifiers remain in their existing pull requests and immutable commits.** This reorganization does not merge or certify every research branch. [PR543](https://github.com/Akilleez-QA/read-em-and-weep/pull/543) contains the current adjoint proof chain; [PR1](https://github.com/Akilleez-QA/read-em-and-weep/pull/1) records mathematical coordination.

## Evidence and version policy

These are authored mathematical arguments with supplementary universal identity checks, not proof-assistant certificates. The references below pin immutable source versions because the research pull requests remain in development. No selected Horrocks-Mumford coefficient or actual matrix-rank experiment is used in the results summarized here. The paper is maintained in modular Markdown; a PDF is not part of this working edition.

## Pinned source references


[O]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ec080c229105457eafcd2583c8a47b362627a62e/research/hm/order-four-quadratic-load/SPECIAL-D5-OCTIC-NONEXTENSION-EXCLUDES-A12.md
[R]: https://github.com/Akilleez-QA/read-em-and-weep/blob/eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c/research/hm/order-four-quadratic-load/POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md
[F]: https://github.com/Akilleez-QA/read-em-and-weep/blob/846968261441fef2cad247d22b66d37aed3f0f8f/research/hm/order-four-quadratic-load/POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md
[S]: https://github.com/Akilleez-QA/read-em-and-weep/blob/04fb081d710f1d7e175f252601b96dddcd93106e/research/hm/order-four-quadratic-load/POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md
[N]: https://github.com/Akilleez-QA/read-em-and-weep/blob/9f28cb10c38d7a0e29c1eb994594325fea7f22bf/research/hm/order-four-quadratic-load/ACTUAL-SECOND-BOCKSTEIN-NONZERO-BY-ATIYAH-QUINTIC.md
[G]: https://github.com/Akilleez-QA/read-em-and-weep/blob/72aa6fb732a803eb9201f45f1f82e60f54d296b4/research/hm/order-four-quadratic-load/POSITIVE-GENERIC-FOUR-OR-FIVE-SECTIONS.md
