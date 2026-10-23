# Canonical transfer restricts the nine-branch gate to the conic line

**Craig Ward · 23 October 2026 · PR1069**

[Immutable full proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/41bc20cade3198306c492c0c46399d71eb0d51c4/research/hm/source2-pure-v-canonical-transfer/PROOF.md).

## New branch-to-coefficient restriction

Under actual compatible pure-V hypotheses, endpoint dimension nine forces the unique quadratic lift to have the form

    R=γR₁,       γ possibly zero.

Thus β=0 in the fixed basis R=αR₁+βR₂. If the actual gate is nonzero, its only possible projective line in this branch is [1:0], the conic line. By the completed nonic classification and original-fourth ideal transfer, its component scheme is exactly Z plus twelve reduced ambient conic points, of total length 46. It is not the other length-46 scheme at [1:2].

If γ=0, the gate is zero and the component base scheme is the whole plane. Neither zero/nonzero nor endpoint nine/sixteen is selected. A nonzero β would force endpoint sixteen, but the converse from β=0 to endpoint nine is not proved. The five-stratum universal classification remains valid; its five nonzero strata are no longer all available within endpoint nine.

## Choice-independent actual transfer

Put Z_Q=im Q (distinct from the length-34 base scheme Z), and let s:I4→P_h be the inverse of Q|P_h. For an equivariant right inverse G_Q:Z_Q→N2, define Π_a=hT_aG_Q. This is independent of G_Q: a difference of right inverses maps to ker Q=A+I2, but Z_Q has no A constituent, so its image lies in I2 and hT_a kills it. Non-equivariant right inverses are not covered.

The literal identities are

    Π_a I4=0,       QΠ_a=L_a h|Z_Q,
    B(a,b)=Π_a T_b s:I4→I2,
    Π_a T_b h=B(a,b)j4.

These retain mixed directions in the fixed negative quadratic space. The symmetric bilinear channel space has dimension two and the alternating space dimension one. No alternating vanishing, independent variability or mixed commutation is asserted.

## The diagonal is the actual lift, with plus sign

Choose quotient corrections x1=−G_QT_as and x2=−G_QT_ax1. The raw second differential vanishing on the whole quotient P summand ensures that x2 is defined in the actual image Z_Q, not merely after an additional image quotient. Using hQ=j2 gives

    R_a=j2x2=−hT_ax1=+hT_aG_QT_as=B(a,a).

The unique equivariant lift theorem identifies this with the actual canonical R in its fixed source/target conventions. This is not a substitute lift modulo a syzygy or an unsupported sign convention.

## Why endpoint nine removes the second coefficient

In endpoint nine, F4=NC4=I4+D_C and h(NC4)=0. Since Π kills I4 exactly, B factors through the nonzero actual D descendant A⊗I4→D_C and the linear transfer A⊗D_C→I2. Both equivariant channel spaces have dimension one. Their respective forms are νL_b* with ν nonzero, and λρ_D(a) with λ possibly zero. Here the adjoint is complex bilinear, not Hermitian. Therefore

    B(a,b)=λνρ_D(a)L_b*,       R_a=γρ_D(a)L_a*=γR₁(a).

The unknown product γ=λν is independent of the intervening identification of D_C. The nonzero P graph proved in PR1066 does not affect this factorization, because Π annihilates I4. It cannot be used to conclude γ is nonzero.

No comparable coefficient restriction is asserted in endpoint sixteen, where the required factorization through NC4 need not exist. The theorem does not prove original rank 36 impossible, actual source occurrence, Q-preservation of NC/NR or a graded extension of h. The four necessary source-dual pairs remain.
