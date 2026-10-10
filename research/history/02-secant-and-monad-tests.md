# Reconstruction 02: secant carriers, local obstructions and monad failures
Period: 2026-10-10, approximately 02:17–02:58 UTC.

This reconstructs recorded calculations; they were not rerun in preparing this document. Source claims and this investigation’s conclusions are distinguished. Scope restrictions are part of every conclusion.

## 1. Separate candidate existence from all-order deformation

[Markman v2, Lemma 11.3](https://arxiv.org/html/2509.23403v2) gives a semiregularity criterion including surjectivity of evaluation. Question 11.4 asks whether the weaker image-restricted condition suffices. These passages were reread during reconstruction.

A first-order ambient obstruction in im(ev) does not put all intrinsic higher obstructions there. An image-stability, formality or quotient argument would still be needed. This was identified before claiming any carrier as a repair.

Finite translation-plus-tensor equivariance was considered using [Perry v2, Theorem 1.2](https://arxiv.org/pdf/2604.00511). A principal Θ line bundle does not simply descend under arbitrary nonzero translations: the tensor compensation and coherent action must be constructed.

## 2. Correct the cyclic secant character, around 02:17–02:36

The literal O(Θ) twist in [Markman v2, §12](https://arxiv.org/html/2509.23403v2) was first flagged as a possible typo. Independent character calculations subsequently required O(3Θ). The source still prints Θ, as confirmed during reconstruction.

For odd d≥3 and n=(d+9)/2, the corrected object has χEnd=16nd. The recorded quotient calculation used:
- quotient Q length 4d−2;
- h⁰≤4d−1;
- h¹≥4 from rank-one trace splitting;
- negative Ext vanishing and fourfold duality;
and obtained h²≥8d+10>28.

The stronger symmetry audit found trivial translation stabilizers for adjacent smooth theta intersections. A rank-one determinant fixes the tensor factor; finite translation–tensor groups in this architecture have order g dividing n, yielding h²≥n(8d+4)/g+6>28.

These dimension bounds rule out full semiregularity for these quotients, not the weak condition on im(ev). That required a different test.

## 3. Find an extra smoothing tangent

The invariant Ext¹ space was not exhausted by translations and Picard twists. A cyclic-curve smoothing tangent was checked against monomial syzygies and partial-normalization lifting.

At the local triple ideal (ac,bc,bd), deforming the Hilbert–Burch matrix gives generators
(ac−t₁d, bc−t₁t₂, bd−at₂).
The outer-neighbor theta-product section supplies a global first-order tangent with nonzero local T¹. The local quadratic correction was explicit; global all-order gluing was not established.

## 4. Test actual Poisson/gerbe evaluation, completed by 02:48

For ξ=π+dΠ, Π=ιπθ²/2, the secant character is annihilated. At a normalized isolated node, the minimal free resolution has degree-two endomorphism boundaries in the maximal ideal. Star-product commutators give a nonzero constant class for suitable global π, while the gerbe contribution is locally zero.

This investigation’s completed calculation concludes ev_F(ξ)≠0 despite ξ·ch(F)=0. It rejects the weak criterion for this corrected object.

The paired source class ξ₁−ξ₂ was then transported through Orlov’s equivalence. The recorded audit identified ξ′=κ−κa, with a=c₁(P)/2 and κ an actual polarized Weil tangent. Künneth preserves the nonzero evaluation. Thus this specific object has an actual intended first-order deformation obstruction, beyond merely having too much Ext².

## 5. Try cones and additional literal carriers

Negative ample-line additions split for the literal Orlov normalization. Correctly B-twisted positive lines in the tested triangle orientation preserve the nonzero evaluation through naturality and Ext¹ vanishing. The bounds propagate through finite towers in that orientation. This did not exclude arbitrary cones, extension orientations or unrelated higher-rank objects.

Two additional [Markman v2 families](https://arxiv.org/pdf/2502.03415) were tested:
- Example 8.2.3 with free isolated points: lifting inclusion into a free rank-one module would induce a Poisson deformation of a skyscraper quotient, contradicted by commuting scalar coordinate actions.
- Example 8.2.4, theta-supported rank-zero carrier: a local resolution for (y,z) over R/(x) produces a nonzero constant star-composition obstruction modulo maximal-ideal boundaries.

These are local tests of the literal families, not universal claims about singular sheaves.

## 6. Test smooth surfaces and numerical characters

For I_Z(aθ), Z a smooth complete intersection of bθ,cθ, matching the character forced a=3(b+c)/4 and (b+c)²=4bc. Hence d=−b²/4<0, incompatible with the requested d>0.

For a smooth-surface ideal with canonical class proportional to θ|S, the recorded intersection calculation forced K_S=(4a/3)θ|S and then a²+9d=0. Non-proportional canonical classes were not excluded.

The proposed Schoen-surface ideal failed a positivity test: [On Schoen surfaces, p.60](https://ems.press/content/serial-article-files/43374?nt=1) identifies a nonzero holomorphic two-form restricting to zero on S. The desired positive θ² cycle identity would have positive Ω∧Ω̄ integral. The contradiction applies to that ideal realization, not every use of Schoen cycles.

## 7. Second candidate inventory, around 02:36

Twenty proposals were recorded: filtered Maurer–Cartan contraction; essential-S¹ Hicks surgery; matrix local systems; bulk-parameter rank; ambient-detected new homology; tropical smoothing; dimension stabilization; higher-rank secants; noncyclic incidence; larger categorical symmetry; isotypical projectors; nonexternal eightfold objects; a differential-graded-Lie higher-obstruction proof; hyperholomorphic/moduli constructions; Prym/cyclic covers; direct Kuga–Satake maps; SO determinant cycles; dominating Hilbert components; independent companion audit; auxiliary-existence/global-obstruction tests.

Only proposals with concrete tests elsewhere in this reconstruction should be called executed. A proposed conditional report was not a solution.

## 8. Signed-twist monad, around 02:52–02:58

The candidate
L⁻¹⊕8 → O⊕18⊕L²⊕L⁻² → L⊕8
passed an alternating-Chern-character test: 4 Re exp(i√2 mθ). No exact-ended construction was established.

It failed before exact-endedness was needed. The maximal L² summand contributes H²(O) surviving in the three-column hypercohomology calculation; compensated evaluation acts nontrivially there while annihilating the total character.

The audited extension covers three-consecutive-degree complexes of powers of one ample line bundle with Pic⁰ twists, after cancellation of invertible constant blocks. Lower-power incoming d₃ requires a fourth column. Equal maximal summands are not acyclic; their relevant d₂ vanishes because their representatives have zero outgoing sheaf maps. Longer complexes may escape through higher differentials, and unrelated middle bundles are not excluded.

## Outcome

The literal secant and three-term line-power candidates were retired within their precise scopes. A genuine Horrocks–Mumford bundle construction became the next branch. No original theorem was solved.
