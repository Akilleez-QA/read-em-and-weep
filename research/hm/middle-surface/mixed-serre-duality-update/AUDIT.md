# Audit of the mixed Serre-dual test and self-duality exclusion

## Verdict

PASS under the already stipulated algebraic-sheaf, marked external-product comparison, compact pure rigidity, and classical HM cohomology premises. No new obstruction evaluation or vanishing is supplied. The important newly explicit correction is the inverse in dualizing a multiplicative defect: the tracefree dual-defect operator is +Id, not −Id. Most block-exchange and canonical retained-projector assertions were already proved in the earlier corpus.

Audited comment: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6272324961 , created and updated 2026-10-19T16:45:14Z. 

## 1. Claim-by-claim verification

### Block-evenness

The product is the external product of identical corrected plane-factor ambients, so exchanging the factors gives an ambient return. The canonical linearization on E=m*HM and the unique marked comparisons of the two pure lifts give a boundary return whose square is identity. Uniqueness of arrows, not just existence of a unique isomorphism class, is the input for coherence; it uses the previously imported compact H0 vanishing. Obstruction naturality then fixes C.

The canonical-form sign is (−1)^(2·2)=+1. The two ordinary parameters commute, so their mixed product also has sign +1. There is no odd-parameter sign. This precisely agrees with retained-obstruction-comparison/PROOF.md §§4,6,7.

### Perfect duality and even dimensions

On the smooth proper fourfold X, Serre duality pairs H2(End0 E tensor omega_X) with H2((End0 E)^dual). The fiberwise trace form identifies (End0 E)^dual with End0 E in characteristic zero. Thus the displayed trace/cup/Serre pairing is perfect. Its value lies in H4(omega_X), whose canonical trace is invariant under block exchange. Hence the even and odd spaces pair orthogonally, and each equal-parity restriction is perfect. Since C is even, odd detectors annihilate it.

The number 32 is imported classical cohomology, not recomputed here. The earlier finite-trace audit already gives the even 2+10+20 dimensions and the unrelated odd 3·10 dimensions. The rank-two scalar recipient vanishes because H2(X,omega_X)=0; this is distinct from the two-dimensional finite-trace summand inside tracefree cohomology.

### Canonical 2+30 decomposition and detectors

Finite flatness of m gives the unit u:O -> F and t=Tr/6:F -> O with tu=Id. Strictly, the endomorphism projector is ut; “Tr/6” is its coordinate map onto the identified unit summand. Block exchange fixes u and t. Therefore F^+=u(O) direct-sum F0^+, with F0^+=ker(t|F^+), canonically.

Finite duality identifies m_*omega_X with Hom(F,omega_P4). The dual constant projector is precomposition with ut, equivalently f maps to [a maps to t(a)f(1)]. The complementary dual summand is Hom(F0^+,omega_P4) inside the even part. Tensoring with B0=End0(HM) and applying H2 gives exactly D_ret and T_ret in the source. Serre duality on P4 makes them perfect duals, by the same trace form on B0.

These identities prove that pairing C with every retained detector vanishes precisely when its retained projection vanishes, even if its constant projection is nonzero. They do not prove that C itself vanishes. The source’s later caveat correctly preserves this distinction.

The cohomological dimensions 2 and 30 are imported. An additive split F0^+ ≅ O(−1) direct-sum O(−2) gives the two twist groups but is not canonical. Its dual produces the old 10+20 split on the target, also noncanonical. No list of thirty previously implemented detectors is thereby certified independent or complete; the claim is about the full abstract cohomology space.

### Quotient functional

Write D_even=D_const direct-sum D_ret and T_even=T_const direct-sum T_ret, with the cross pairings zero and the diagonal pairings perfect. The functional d maps to <C,d> descends to D_even/D_const if and only if C_const=0. Alternatively <C_ret,d> always descends. This is the exact content of the caveat; merely calling the target a retained quotient does not remove the constant component.

PR79's current alternating proof concerns an authenticated raw source with its own complete geometric-action, physical-frame, regularity, and chain-compatibility premises. It does not justify transferring its alternating boundary to an unaligned frozen jet. No new alignment is inferred here. Existing marked class-level comparison results remain valid within their already stated scope; the caveat is not a rollback of them.

### Rank-two adjoint and dual defect

For a rank-two bundle, wedge is a canonical alternating pairing valued in det E. The induced adjoint is a^dagger=tr(a)Id−a, hence −Id on End0. It does not generally identify E with E^dual without the determinant twist.

A normalized top defect is 1+C with C in a square-zero ideal. Dualizing the inverse transition produces (1+C)^(-t)=1−C^t. Under the alternating identification the infinitesimal operator is therefore −dagger, which is +Id on End0. Dropping inversion would incorrectly manufacture a minus sign. There is no additional sign from pairing two cohomological degree-two classes.

Dualization changes the module side, so its destination is initially the opposite ambient. Opposite local multiplication uses reversed order; the original overlap homomorphisms remain homomorphisms for the opposite products. Their inner triple units are inverted. In the stated corrected bounded presentation those units are central, so the comment's wording is valid; one should not generalize “central” to arbitrary algebroid presentations. A determinant-valued classical pairing does not itself provide a quantized determinant bimodule or the global return equivalence.

Given an actual return whose classical carrier map is the alternating identification and whose mixed coefficient map is identity, the tracefree dual-defect constraint is tautological. An arbitrary extra classical automorphism in a return could act nontrivially on End0, so “trivially on the mixed ideal” alone should be read together with that specified classical identification. The comment is discussing precisely this canonical shortcut, not classifying every possible extra return automorphism.

Both-parameter reversal has mixed sign +1; one-factor reversal has sign −1. The latter is only a prospective sign until a compatible ambient and boundary return exists. PROOF.md now excludes the naive identity-reduction, axis-preserving opposite return with only one negative coefficient sign, already at the pure bracket level.

## 2. What is actually new

Already in the corpus:

- The complete mixed source, coboundary transformation under pure gauges, and choice-independent class: mixed-module-source-audit and actual-joint-deformation-model.
- No inference of mixed vanishing from pure rigidity, or from an untwisted ordinary Yoneda argument: corrected-mixed-secondary-class.
- Block-evenness, the finite-trace canonical projector, the distinct odd thirty-space, tracefree compatibility, and marked transport: retained-obstruction-comparison and mixed-obstruction-transport.
- The canonical retained quotient and noncanonical twist splitting, with source-action cautions: retained-sector-structural.

Newly explicit in this comment are the complete abstract Serre-dual detector formulation, its precise quotient-functional caveat, and the inverse-transpose correction excluding the proposed alternating-self-duality sign shortcut. The detector formulation is a dual restatement of the existing canonical projector, not construction or evaluation of physical detectors. The genuinely additional bounded result of this packet is the first-order impossibility theorem in PROOF.md.

## 3. Public mathematical references


Public mathematical sources:

- https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6272324961
- Its dependency comments 6271101716 and 6270678828, in the same discussion.
- https://github.com/Akilleez-QA/read-em-and-weep/pull/79 (historical comparison source).
- https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-alternating-primitive/PROOF.md , blob cbf430ace19fce3fd08dad43c6bdf8174d2d2e12.
- https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md , blob a58834ab61e18a5dedd8a7bf20bec7121bfa9165.

Local comparisons additionally include fiber-obstruction-localization/FINITE_TRACE_TARGET_SOURCE_AUDIT.md and the proof/audit files named above.
