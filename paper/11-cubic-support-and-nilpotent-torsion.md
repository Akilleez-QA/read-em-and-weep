# 11. The cubic support and its nonreduced torsion

## 11.1 The actual support is a smooth genus-four curve

The degree-eight operator defect of [Section 10.6](10-midpoint-operator-residue.md#106-the-exact-degree-eight-quotient-and-double-cubic-bundle) is the pushforward of L₂ = O_(2D)(-2,12), where D is the actual cubic divisor of bidegree (3,3) in Y = P(W′)×P(W). The [support theorem][C] proves that D is smooth and integral, of genus four, with

    K_D = O_D(1,1),       T = O_D(1,-1),       ord(T) = 5.

Both projections give degree-three pencils. The canonical model is the intersection of a smooth quadric and a cubic surface in P³. These are properties of the actual support, not of a substituted generic (3,3) curve.

The proof uses the actual regular cubic/quintic pair. Finite degree three over the negative projection line allows at most three irreducible components, each fixed by the projective A5 action. The small-bidegree character calculation permits no proper invariant component: the first common nontrivial representation occurs at bidegree (3,3). Thus D is integral and reduced. Its arithmetic genus is four, while any singular point would have an orbit of at least twelve points. That exceeds the total possible singularity delta invariant, so D is smooth.

The local quintic generators agree on D and give a nowhere-zero section of O_D(5,-5), trivializing T⁵. The sequence

    0 → O_Y(-2,-4) → O_Y(1,-1) → T → 0

has no ambient H⁰ and no left-hand H¹. Hence H⁰(D,T)=0, so T is nontrivial. Since five is prime, its order is exactly five.

## 11.2 A 9-to-36-to-27 filtration of the residue sections

The conormal of D in Y is O_D(-3,-3) = K_D⁻³. Restriction of the actual line L₂ to D gives the exact sequence

    0 → K_D²⊗T³ → L₂ → K_D⁵⊗T³ → 0.

The identifications of the two end terms use T⁵ = O_D only on D. They do not extend that equality to 2D or split the sequence. The two end degrees are twelve and thirty; both H¹ groups vanish. Riemann–Roch gives

    0 → H⁰(K_D²⊗T³) → H⁰(L₂) → H⁰(K_D⁵⊗T³) → 0,
          dimension 9       dimension 36       dimension 27.

Their actual equivariant characters are, respectively,

    P4⊕D5,
    A⊕2V⊕3P4⊕3D5,
    A⊕2V⊕2P4⊕2D5.

This is an intrinsic filtration of the residue domain. It is not the distinct 32-dimensional kernel of the operator boundary to P4 in Section 10.6. [Filtration and characters][C].

## 11.3 The intrinsic nilpotent boundary is onto P4

Let π project to L = P(W). The nilpotent subbundle of the defect is

    N₈ = π_* O_D(-5,9) = O_L(4) ⊕ W′ O_L(1).

The first summand is exactly the scalar class-of-N subbundle. The actual regular-pair presentation gives

    0 → V O_L(-4) → T6 O_L(-1) → N₈ → 0.

It follows that H⁰(N₈) = D5⊕P4. Comparison with the actual gauge extension from Section 10.6 identifies the restricted operator boundary with the quotient

    0 → D5 → H⁰(N₈) → P4 → 0.

The D5 injection is the already proved nonzero extension boundary, so this P4 channel is genuinely nonzero. It is not inferred from an allowed representation type. Nevertheless, the actual corrected operator residue is not shown to lie in N₈ or to have a nonzero P4 component there. [Intrinsic boundary theorem][C].

## 11.4 The ambient five-torsion relation fails on the double curve

The [nilpotent Picard comparison][P] proves

    O_(2D)(5,-5) ≠ O_(2D).

Thus the ambient line T₀ = O_(2D)(1,-1) is not five-torsion, although its restriction T is. With J = O_D(-3,-3), the square-zero unit sequence gives

    0 → H¹(D,J) → Pic(2D) → Pic(D) → 0.

The kernel is an additive complex vector space of dimension twenty-one; its invariant part is one-dimensional. Multiplication by five is invertible on this kernel.

For actual quintic changes gⱼ = gᵢ + fpᵢⱼ, the ratios on 2D are 1 + fpᵢⱼ/gᵢ modulo f². Multiplication by the nowhere-zero quintic on D identifies J with O_D(2,-8), whose pushforward is V O_L(-8). Under this sheaf isomorphism the nilpotent Picard class is exactly the actual nonzero quintic-relation extension

    e ∈ [V⊗H¹(O_L(-8))]^Γ.

This proves nontriviality through an actual class comparison, rather than mapping a nonzero extension through an unspecified arrow.

If K(c) denotes the nilpotent line-bundle class for c ∈ H¹(D,J), then

    T_tors = T₀ ⊗ K(-e/5)

has exact order five and restricts to T. It is the unique five-torsion line-bundle isomorphism class with that restriction. This is uniqueness of a line-bundle class on the double cubic, not a canonical trivialization, an identification of normal bundles, or a lift of the midpoint to the next ambient thickening.

## 11.5 What remains open

The support geometry, both split square-boundary channels, and the intrinsic nilpotent boundary provide additional structure for calculating the actual corrected residue. No comparison identifies the nonzero Picard class e or its derivative with the positive cubic value. In particular, none of these nonzero auxiliary maps proves that the specified residue survives the 32-dimensional kernel, avoids cancellation, or survives the actual second-symbol quotient.

The absolute Ψ value, four-versus-five decision, and original repair remain open. All sources below are pinned to the accepted public PR543 commit. Their geometric proofs have independent checks and universal verifiers; these are not proof-assistant certificates or selected-instance coefficient/rank tests.

## Pinned source references

[C]: https://github.com/Akilleez-QA/read-em-and-weep/blob/14fc90d90f74998c10ea9f2b45cf5b8aeac96bae/research/hm/order-four-quadratic-load/ACTUAL-CUBIC-SUPPORT-IS-GENUS-FOUR-WITH-EXACT-FIVE-TORSION.md
[P]: https://github.com/Akilleez-QA/read-em-and-weep/blob/14fc90d90f74998c10ea9f2b45cf5b8aeac96bae/research/hm/order-four-quadratic-load/ACTUAL-CUBIC-FIVE-TORSION-FAILS-ON-ITS-DOUBLE.md
