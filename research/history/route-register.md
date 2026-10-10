# Research-route register

Initial snapshot: 2026-10-10, 03:35 UTC; checked update: 03:41 UTC. This is a tracking document, not a repaired proof.

## Checked update — 2026-10-10, 03:41 UTC

This update supersedes the earlier pending Ext-count and conditional-square statements while preserving those checkpoints as history.

The complete exact calculation gives:
- Ext dimensions in degrees 0,…,4: (1,87,7372,87,1).
- Trace-free dimensions: (0,83,7366,83,0).
- Ext¹ dimension per character of weight 0,1,2,3,4: (79,2,0,0,0). There are four singleton characters, so 79+4·2=87.
- Euler characteristic: 1−87+7372−87+1=7200.

The finite certificate has been rerun with exact arithmetic, and all character sectors have also been independently reconstructed. These checks establish the finite model’s stated cohomology; they are not formal proof-assistant certification.

Combined with the smooth 87-dimensional fixed-X family and its injective Kodaira–Spencer map, the exact Ext¹ count makes that tangent map an isomorphism. Every ordinary first-order class extends in the smooth family. Hence all ordinary fixed-base Yoneda squares vanish.

The actual ambient second-order obstruction O₂⁰ remains uncomputed. For the fixed Moyal/gerbe two-jet, the previous criterion u²=−O₂⁰ now reduces to O₂⁰=0. Neither its vanishing nor nonvanishing is asserted. Ordinary fixed-X unobstructedness is not ambient all-order unobstructedness and does not prove any original theorem.

Public supporting work:
- [Carrier and finite setup, PR #2](https://github.com/Akilleez-QA/read-em-and-weep/pull/2)
- [Smooth family and Kodaira–Spencer calculation, PR #3](https://github.com/Akilleez-QA/read-em-and-weep/pull/3)
- [Order-two reduction, PR #4](https://github.com/Akilleez-QA/read-em-and-weep/pull/4)

## Historical route-register snapshot

The entries below preserve the 03:35 checkpoint. The update above controls the current Ext count and Yoneda-square status.

## Scope and evidence

Targets: the withdrawn claims concerning split Weil eightfolds, Kuga–Satake correspondences for K3 surfaces, and rational Hodge classes on products of K3 surfaces. None has been established by this investigation.

“Retired” below means that the specified construction or inference failed; it never means that an original algebraicity statement is false. “Research calculation” identifies a calculation from this investigation, not a theorem asserted by the cited literature. Detailed proof capsules and executable checks should accompany focused follow-on PRs; this register is an index, not their substitute.

Primary-source facts rechecked for this register: the eightfold withdrawal notice; the EEMS signed-index formula and stabilization lemma; Markman v2, Lemma 11.3, Question 11.4 and §12. Other citations identify the mathematical foundations of the recorded tests; they do not imply that those papers contain this investigation’s new conclusions.

## Corrections that must remain visible

1. **Original stabilization sign.** Starting with I(f₁)=−m, each reverse trace contributes −1 in the manuscript convention. The resulting count is −2m, not zero. The cancellation hypothesis fails. This is explicitly stated in the [withdrawal notice](https://github.com/openai/math/blob/main/preprints/Algebraicity-of-Weil-classes-on-split-abelian-eightfolds-September-18-2026/README.md). The archived manuscript is pinned to commit adc7f1241b42e322a6451854ab7e4b4c146bf78a.

2. **The alleged Hicks/Floer action-order mismatch is withdrawn.** With common ω=dq∧dp, λ=−p dq and Seidel conventions, q₊→q₋ has index 6 and the reverse positive-action branch has index 2. Hicks k=1 matches the forward cusp. The earlier contrary assertion was a branch-labeling error. The unordered pair {2,6} and its degree-2 obstruction remain relevant; a supposed action-order mismatch is not a reason to reject surgery.

3. **EEMS signs cannot be imported unchanged.** EEMS uses I=(−1)^(n/2)χ/2 for Euclidean immersions; the eightfold manuscript uses I=(α²−χ)/2. An apparent immediate replacement proof mixed conventions. See [EEMS, proof of Corollary 1.3 and Lemma 2.1](https://arxiv.org/pdf/1303.0588).

4. **First-order control is not all-order control.** Injectivity of semiregularity on im(ev) does not itself show that later intrinsic obstructions lie there. [Markman v2, Question 11.4](https://arxiv.org/html/2509.23403v2) explicitly asks about the weaker hypothesis. Neither a large Ext² group nor failure of a sufficient criterion alone establishes an actual obstruction.

## A. Geometric routes

### G1. Repeat cancellation after repairing only the net count — retired
Negative-Euler-characteristic stabilization regions can alter the total count, but every nonempty compact superlevel region has an interior maximum. The ordinary forward trace there retains the bad local generator. Connected sums with S³×S⁵ preserve useful low-degree topology and change χ, but do not remove that local problem. This rejects the unchanged trace construction, not every stabilization geometry. Foundations: [Eliashberg–Murphy, Theorem 2.3](https://arxiv.org/pdf/1303.0586), [EEMS, Lemma 2.1](https://arxiv.org/pdf/1303.0588).

### G2. Weaken “all indices odd” to “no ordered index 2” — valid gate, failed local implementation
The abstract zero-bounding-cochain criterion is available under its exact Calabi–Yau hypotheses. Research calculation with fixed phase lifts gives forward cusp indices {2,n−2}, reverse {1,n−1}; for n=8 the forward pair is {2,6}. Global regrading does not change self-intersection indices. Thus this weakening does not fix the ordinary-ball trace. Different geometry remains possible. Source: [Akaho–Joyce, Propositions 12.2 and 13.10](https://people.maths.ox.ac.uk/joyce/AkahoJoyce.pdf).

### G3. Essential-circle Hicks surgery — support not constructed
The local index matches after correction. What is missing is an embedded, full finite-area surgery neighborhood compatible with the global immersion, grading, homology and periods. A thin isotropic core with formal framing does not supply it. A proposed blanket placement principle also faces a closed-Lagrangian obstruction test, but its complete FOOO reference and proof should be supplied before that test is promoted to a standalone public no-go theorem. Source: [Hicks, Lagrangian cobordisms and Lagrangian surgery, v3](https://arxiv.org/abs/2102.10197).

### G4. Nonorientable surgery followed by orientation cover — retired
For an orientation-reversing deck involution and invariant composite map to the torus, the rational pushforward of the top class is zero. It cannot give the required nonzero να. This is a homological obstruction to this escape only.

### G5. Products of genus-two building blocks — class mismatch
The embedded spin Maslov-zero genus-two block is genuine. The product Σ₂⁴ has χ=16, b₁=16 and b₂=b₆=100, but contraction kernel dimension 20, whereas the target specifies 16. Research linear-algebra checks also exclude placing the full target Ω inside that product kernel by a real linear change. Scaling and isogeny do not repair the mismatch. Sources: [Abouzaid–Smith, §3.6, Lemma 9.4, Proposition 9.18](https://arxiv.org/abs/0903.3065), [Hicks, Examples 4.2.5 and 4.2.9](https://arxiv.org/abs/2204.06432).

### G6. Class-preserving surgery or one clean gluing locus — insufficient
For the stated product class, increasing b₂=b₆ to 104 while retaining surjective H² restriction creates a four-dimensional ambient-invisible H₆ kernel. For codimension-two gluing, killed H² classes lie in the span of the gluing-divisor classes. Research calculations require at least eight independent divisor classes; the natural splitting requires twelve cross-factor directions. One connected locus therefore fails. Proposed graph columns span the required directions in one d=1 model, but overlapping supports, simultaneous plumbing, grading and unobstructedness are unresolved. No same-sign graph-orientation no-go is claimed. [Mak–Wu, Corollaries 2.22 and 4.13](https://arxiv.org/pdf/1509.08028) grade an existing clean pair; they do not construct this configuration.

## B. Algebraic carrier routes

Notation: θ is the chosen polarization; Π=ιπ(θ²)/2 for a holomorphic bivector π.

### A1. Literal cyclic secant complex — correction plus obstruction
The character calculation requires O(3Θ), rather than the literal O(Θ) printed in [Markman v2, §12](https://arxiv.org/html/2509.23403v2). Correcting that character does not make the object deformable.

Research tests for the corrected partial-normalization object:
- For odd d≥3, n=(d+9)/2, χEnd=16nd. The cyclic quotient has h²≥8d+10>28.
- For the unchanged rank-one theta-incidence architecture, the determinant fixes the tensor factor and the translation stabilizer limits the finite quotient order g to a divisor of n. The bound h²≥n(8d+4)/g+6 remains >28.
- These bounds reject full semiregularity; they do not alone reject the weak image criterion.
- A separate local calculation finds ξ=π+dΠ annihilating ch(F), but ev_F(ξ)≠0 at a normalized isolated node. Orlov transport of the paired class gives an actual polarized Weil tangent with nonzero evaluation.

These conclusions concern the exact corrected object and symmetry architecture. New objects or unrelated autoequivalences are not excluded.

### A2. Treat invariant Ext¹ as translations plus Picard twists — retired
A global cyclic-curve smoothing tangent has nonzero local T¹. The local Hilbert–Burch deformation of the ideal (ac,bc,bd) gives (ac−t₁d,bc−t₁t₂,bd−at₂). First-order lifting was checked; all-order global gluing was not. The tangent invalidates the claimed exhaustion of Ext¹.

### A3. Repair the obstructed object by ample-line cones/towers — scoped failure
Sufficiently negative line additions split for the literal Orlov normalization. Sufficiently positive, correctly B-twisted line additions in the tested triangle orientation preserve the nonzero evaluation obstruction by naturality and Ext¹ vanishing; the same bounds propagate through finite towers. Other cone orientations and extensions whose relevant Ext groups do not vanish remain open.

### A4. Other literal secant sheaves — local obstruction
For the free-point ideal family of [Markman v2, Example 8.2.3](https://arxiv.org/pdf/2502.03415), a putative Poisson deformation would induce a forbidden rank-one deformation of the skyscraper quotient. The partial-normalization alternative has the node obstruction above. For the theta-supported Example 8.2.4, star-composition of the local resolution produces a nonzero constant degree-two class, whereas boundaries vanish at the point. These research calculations reject these literal carriers, not all point-modified or divisor-supported sheaves.

### A5. Smooth complete-intersection and proportional-canonical surface ideals — numerical failure
For I_Z(aθ), Z a complete intersection of bθ,cθ, character matching forces a=3(b+c)/4 and (b+c)²=4bc, hence b=c and d=−b²/4<0. More generally, the tested smooth-surface ideal with K_S proportional to θ|S forces a²+9d=0. Neither realizes d>0. Smooth surfaces with independent canonical class are outside these tests.

### A6. Schoen-surface ideal with one polarization — positivity failure
The Schoen surface is holomorphic Lagrangian for a nonzero ambient holomorphic two-form Ω. Its integral of Ω∧Ω̄ is zero. The required positive multiple of θ² gives a positive integral, contradicting the proposed cycle identity. This excludes this ideal-carrier realization, including its isogeny pullbacks, not every use of Schoen classes. Source: [Ciliberto–Mendes Lopes–Roulleau, On Schoen surfaces, p.60](https://ems.press/content/serial-article-files/43374?nt=1).

### A7. Signed-twist monad and three-term line-power complexes — retired within stated amplitude
The numerical monad L⁻¹⊕8 → O⊕18⊕L²⊕L⁻² → L⊕8 has the desired alternating character, but compensated Poisson evaluation on the maximal L² summand survives in Ext². Numerical character matching was never an actual exact-ended construction.

The research generalization covers nonzero complexes in three consecutive degrees whose terms are powers of one ample line bundle with Pic⁰ twists, after constant-block cancellation. The maximal summand’s H²(O) survives: an incoming lower-power d₃ would require a fourth column. Equal maximal summands are not acyclic, but their relevant d₂ vanishes. Longer complexes and non-line middle bundles remain outside this exclusion.

### A8. Horrocks–Mumford pullback — active, restricted first-order success
Let H be normalized HM on P⁴, c₁=−h, c₂=4h². For finite f:X⁴→P⁴ defined by five sections of O(2mΘ), E=f*H⊗O(mΘ) has c₁=0, c₂=15m²θ² and ch(E)=2 Re exp(i√15 mθ). This is an actual bundle, restricted to the field Q(√−15).

Research calculations pass the weak first-order kernel test using rank-two curvature scalarity and relative polarized deformations. Stability and simplicity use [Biswas–Das–Parameswaran, Theorem 2.5](https://arxiv.org/html/2203.03246). The classical construction is in the [original HM paper](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf).

What is established computationally at the explicit elliptic-product seed: exact monad identities and atlas minors; finite Čech-transfer checks giving zero Ext¹ in deck weights 2,3,4. What is not established: the actual second-order obstruction, full Ext¹ count 87, all-order ambient deformation, or any original theorem.

### A9. HM shortcuts through ordinary semiregularity or hyperholomorphicity — unavailable
For the simple normalized seed, χEnd=7200 and h²=7198+2h¹, far above the fourfold target dimension 28. The literal Orlov self-pair has cohomology in multiple degrees, including nonzero torsion in the top relative Fourier–Mukai image, so a stable-bundle/reflexive-sheaf hyperholomorphic theorem cannot be applied unchanged.

The sufficient “base dimension e−k” criterion in [H8 v3.2.0, Proposition p2flat](https://github.com/creelie/H8/blob/v3.2.0/tex/sections/10c5_polarised.tex#L777-L829) also fails numerically: e−k<0 for this carrier and the stated external self-pair. Failure of this sufficient criterion is not an obstruction theorem.

## C. Open branches and discriminating next tests

1. **HM second order.** For a fixed Moyal/compensating-gerbe two-jet, calculate O₂⁰ and the Yoneda square map. The research reduction is: a lift exists iff u²=−O₂⁰ for some u∈H¹(End₀E); the mixed linear term vanishes. A nonzero baseline alone excludes only duality-fixed lifts. Deck-sector vanishing isolates a full-sign component that no Yoneda square or second-order ambient correction can change, but that component has not been evaluated.
2. **Complete HM deformation count.** A smooth 87-dimensional fixed-X family with injective Kodaira–Spencer map has been constructed. Equality h¹=87 remains to be verified; only then may this family exhaust first-order directions and force their squares to vanish. Fixed-X smoothness would still not prove ambient unobstructedness.
3. **Longer/higher-rank/nonexternal carriers.** Test full differentials, compensated Atiyah action and all-order deformation. Longer line complexes may have the d₃ escape unavailable in three terms. Distinct-carrier extensions and nonexternal Fourier–Mukai kernels need their actual Ext/Yoneda calculations.
4. **New global geometry.** Construct support before invoking surgery: nonproduct embeddings, bundles, several compatible clean loci, tropical or generating-family constructions, and correspondence composition. Each must preserve να, spin/orientation, H₂/H₆ injectivity, the prescribed H² kernel, grading and unobstructedness.
5. **Bounding cochains rather than eliminating generators.** Filtered Maurer–Cartan solutions, matrix local systems, bulk parameters and twisted complexes remain proposals. Required tests include filtration/energy convergence, all-order cancellation and retention of the required nonzero K-class.
6. **Direct algebraic cycle families.** Moduli, Prym/cyclic-cover, direct Kuga–Satake, determinant-cycle or arithmetic routes need a genuinely dominating family. Density of special/CM points and algebraicity on a special fiber do not by themselves supply spreading or lifting.
7. **Limited cases and dependency audits.** Restricted K3 cases or conditional implications can be useful results, but must retain their hypotheses and cannot close the original quantifiers. An unretracted companion must be checked for independence before being used.

## Publication rule for this register

Tracking PRs may record partial computations, rejected candidates and explicit gaps. A solution submission to the original project requires a complete checked proof in the original scope. No theorem repair, formal proof-assistant verification, external expert validation or novelty priority is asserted here.

## Published tracking PRs

- #1: scope and coordination
- #2: explicit carrier, atlas and exact polynomial verifier
- #3: smooth-family proof
- #4: lift-independent obstruction reduction
- #5: full exact Ext model and executable certificates
- #6: geometry/sign history
- #7: secant/surface/monad history
- #8: HM and computation history
