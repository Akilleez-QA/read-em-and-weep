# Reconstruction 03: global geometry and the Horrocks–Mumford branch
Period: 2026-10-10, approximately 02:46–03:35 UTC.

Historical executions are identified below; this document does not claim they were rerun during reconstruction. The snapshot intentionally preserves uncomputed quantities.

## 1. Third inventory and product geometry

Twenty proposals were recorded: direct products; nonproduct embeddings with product topology; fiber bundles; clean plumbing; preinstalled full Hicks support; periodic generating families; Lagrangian correspondences; tropical lifting; singular-cycle desingularization; Lefschetz matching cycles; matrix bounding cochains; signed-twist monads; universal sheaves; nonabelian-cover pushforwards; distinct-carrier extensions; non-subcanonical surface ideals; nonexternal Fourier–Mukai kernels; dominating correspondence families; arithmetic specialization; formal boundary certification.

Concrete geometric tests:
- A q/p-torus surgery yields a genuine embedded graded genus-two block, using [Abouzaid–Smith](https://arxiv.org/abs/0903.3065) and [Hicks](https://arxiv.org/abs/2204.06432).
- Its fourfold product has Betti vector (1,16,100,304,454,304,100,16,1), χ=16 and contraction kernel dimension 20.
- The target requires a different class/kernel. Linear-algebra tests ruled out identifying them by scaling, isogeny or real linear change.
- Class-preserving surgery with b₂=b₆=104 creates an invisible four-dimensional H₆ kernel under the stated H²-surjectivity hypothesis.
- Clean gluing requires at least eight independent divisor classes; the natural splitting has twelve cross-factor directions. One connected locus fails.
- A d=1 graph-column model can span twelve directions using fifteen columns, but overlap and simultaneous-plumbing problems remain. A proposed graph-orientation obstruction was not checked and is not a conclusion.

Geometric expansion was paused in favor of the new bundle tests. Nonproduct class-changing geometry remains open.

## 2. Construct an actual HM carrier, around 02:58

Normalized Horrocks–Mumford H on P⁴ has c₁(H)=−h, c₂(H)=4h². For finite f:X⁴→P⁴ defined by five sections of O(2mΘ), set E=f*H⊗O(mΘ). Then
c₁(E)=0, c₂(E)=15m²θ², ch(E)=2 Re exp(i√15 mθ).

This construction is actual, unlike the numerical monad. Its squareclass is 15: it addresses Q(√−15), not arbitrary imaginary quadratic fields.

The recorded first-order audit used determinant-flat rank-two curvature scalarity and polarized relative deformations. It verified the sixteen-dimensional annihilator: six compensated bivectors and ten polarized complex directions. The weak first-order kernel condition passed.

Sources: [original HM paper](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf), [stable pullback, Theorem 2.5](https://arxiv.org/html/2203.03246). First-order success does not answer [Markman’s Question 11.4](https://arxiv.org/html/2509.23403v2).

## 3. Reject shortcuts, around 03:04–03:09

For the simple normalized carrier at m=1, χEnd=7200 and h²=7198+2h¹>28; ordinary fourfold semiregularity is unavailable.

The literal Orlov self-pair is not a shifted coherent sheaf: its top relative Fourier–Mukai image is nonzero torsion, alongside lower cohomology. A stable-bundle/reflexive-sheaf hyperholomorphic result does not apply unchanged.

[H8 v3.2.0, Proposition p2flat](https://github.com/creelie/H8/blob/v3.2.0/tex/sections/10c5_polarised.tex#L777-L829) requires a base dimension e−k with k the FULL semiregularity kernel. The carrier and the stated external self-pair give e−k<0. This rejects that sufficient criterion, not actual deformability.

## 4. Build and execute a finite atlas, around 03:10

Explicit seed: C:y²=x³−x, X=C⁴, N=O(Σ∞ᵢ). The map f is given by coefficients of ∏(uᵢT+vᵢS), has degree 384 and f*O(1)=N².

A twelve-by-five HM matrix α and β=αᵗJ were reconstructed from the original wedge formulas. Six projective chart types cover P⁴. The initial inverse-x product cover alone only trivializes N², so it did not justify an N-trivialized 96-chart assertion. A later explicit correction uses C\\{∞} and C\\{(0,0),(1,0),(−1,0)}, with N frames 1 and y/x; its sixteen product opens restore the bound of at most 96 after intersection with the six projective opens. The corrected cover is specified in PR #2. Quotient-frame formulas supply rational transition matrices.

Recorded exact sparse-integer-polynomial executions:
- βα=0 in all 25 entries;
- primary β minor = abcd−1;
- primary α minor = 1−abcd;
- auxiliary β minor = cd;
- auxiliary α minor = −a²c.

The same identities were separately reconstructed and executed. An exact Q(ζ₅) check covered 125 points omitted by the five primary opens. Symbolic coverage already handles them through the auxiliary open. A floating-point triple-overlap residual below 3×10⁻¹⁴ was only a sanity check; the cocycle follows from quotient coordinates.

These are finite algebra checks, not deformation-obstruction computations. The executable atlas verifier should be preserved unchanged in its own focused artifact.

## 5. Reduce the order-two problem, around 03:18–03:21

Use Moyal μ₁,μ₂ and a locally constant analytic Čech gerbe representative for B=15Π. An arbitrary algebraic Čech representative cannot be substituted. Refine to an analytic good cover with SL₂ frames.

The recorded analytic derivation:
- K=μ₁(g⁻¹,g) is traceless.
- A duality-fixed first-order correction has a=sI−K/2.
- The scalar Čech equation for s has zero class by rank-two scalarity and the compensated Chern identity.
- Local second-order affine adjustment yields a traceless, closed obstruction class O₂⁰.
- Scalar flat-line twists do not change that class.
- For arbitrary first-order u∈H¹(End₀E), O₂(u)=O₂⁰+L(u)+u².
- A determinant-preserving dual-number/Chern-connection argument and the ∂∂̄ lemma give L=0.

Thus, for the fixed ambient two-jet, some lift exists iff u²=−O₂⁰. Nonzero O₂⁰ alone rejects only duality-fixed lifts. Averaging solutions with different first-order terms is invalid. No all-order conclusion follows.

Primary context: [Baranovsky–Huey, Theorem 1 and Lemma 9](https://arxiv.org/html/2607.12910), [Pecharich, Theorem 1.3](https://arxiv.org/html/1010.3671). These papers do not compute this carrier’s obstruction.

## 6. Execute finite Ext-sector checks, around 03:18–03:31

The cancelled line complex is
5N⁻¹ → 15N → 10N³ → 2N⁵.
The finite End-model term dimensions are (354,18296,43084,18296,354), total 80384, Euler characteristic 7200. These are term dimensions, not Ext dimensions.

Historical exact executions, with independent reconstruction recorded:
- Weight 2: total-degree-one source 640; d₁ rank 450; d₃ rank 100 on the 190 kernel; d₅ rank 90 on the remaining 90.
- Weight 3: source 1280; d₁ rank 1250; d₅ rank 30.
- Weight 4: source 2560; d₁ rank 2550; d₅ rank 10.
- The initial 720×640 d₁ matrix had 2880 signed additions and exact rank 450; this earlier intermediate kernel 190 was not final cohomology.

The recorded tensor Čech homological-perturbation audit identifies these as vanishing Ext¹ deck sectors of weights 2,3,4. Only weights 0 and 1 remain in Ext¹.

The baseline quadratic obstruction lies in trivial and full-sign sectors. No Yoneda square of remaining Ext¹ classes, nor second-order ambient HH² correction, changes its full-sign component. That isolates a diagnostic component; it does not evaluate it.

## 7. Construct a smooth fixed-X family, around 03:30

A smooth 87-dimensional family with injective Kodaira–Spencer map was established in the recorded analysis:
- 79 projectivized five-section directions;
- 4 translation directions;
- 4 Picard tensor directions.

Finite projective stabilizer of HM was checked using both [Manolache, Proposition 2](https://imar.ro/~increst/1985/34_1985.pdf) and the original HM representation-theoretic argument.

At this snapshot, the equality h¹EndE=87 remains unconfirmed. Therefore versality and universal square-vanishing remain conditional. Even fixed-X smoothness would not establish noncommutative or Weil ambient unobstructedness.

## Snapshot frontier

Uncomputed: actual O₂⁰, its full-sign component, complete Ext¹ count, and all-order ambient deformation. No theorem repair has been established. The next decisive calculation is the actual obstruction, not another numerical-character match.

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


- [Exact Ext model and executable certificates, PR #5](https://github.com/Akilleez-QA/read-em-and-weep/pull/5)
