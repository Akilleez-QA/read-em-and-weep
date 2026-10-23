# The genuine pure-V quotient and its two-coefficient third gate

**Craig Ward · 23 October 2026 · PR1022 and PR1025**

Sources: [PR1022 full proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/5488bc153029391d647c3e18d9344e4e00e38a7f/research/hm/source2-pure-v-quotient-second/PROOF.md), [PR1025 full proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/09f1377f83b027ca27eea0b3a9f40a1b92c6c466/research/hm/source2-pure-v-quotient-third/PROOF.md).

## 1. Actual quotient, not an equivalent cancellation

Assume a nonzero Q-compatible pure-V source2 radical. Write M for the original family, I=im j and U=M/I. Here I=[D→P] has differential tL_a, with L_a(d)=[ad]. The actual long sequence gives H⁰(U)=A+P and H¹(U)=P. The connecting map identifies the source P with im j₄; the descended radical U→I identifies its target H¹ with im j₄ as well.

Naturality with that descended radical kills the **entire** quotient first Bockstein. Projection from M then identifies the quotient second on A with the original second. To kill the additional P channel E_a, corrected original lifts give β₃,M(d)=−[E_aL_a(d)] modulo im β₂,M. The imported original-third zero and generic surjectivity of L give generic image containment in the second-symbol image.

The latter containment is not enough by itself. The original B:A O(-2)→P O has finite rank-drop locus, so its cokernel is locally free away from finitely many points and has no codimension-one torsion. At those remaining points its local length-one free resolution over a regular surface gives depth at least one, ruling out point-supported torsion as well. Its cokernel is therefore torsion-free. Hence the containment extends globally. Matched twists force E to factor through a constant equivariant P→A map, which is zero. Thus

    β₁,U=0,   β₂,U=[B,0] on A+P.

Generically the genuine 36→33 quotient has 29 unit Smith pivots, three valuation-two pivots and a residual 1×4 matrix divisible by t³. U changes the original kernel and is **not** declared equivalent to M.

## 2. The third lands in a specific torsion-free sheaf

Let X=P(A). The actual endpoint identity f₁T̄=L f₀ and global polynomial corrections put the quotient third in

    s:P O_X(-3)→J=im L/im B.

This is a global sheaf statement proved on representatives, not a generic-fiber inference about torsion. The canonical kernel of L is O(-5), and B=−μLm with μ≠0 and m ordinary multiplication. Since B is sheaf-injective, im m intersects ker L trivially. Consequently

    0→A O(-2)⊕O(-5)→D O(-1)→J→0.

This is an actual direct-sum preimage, not an assumed horizontal splitting of U. Projection of the kernel generator into E(-1) identifies J with the **previously known** I_Z(6). The length-34 scheme Z has six length-four complete intersections and ten reduced points, as imported from PR1000. Its support and multiplicities are not new discoveries here.

## 3. Exactly two channels, neither selected

Twisting the resolution by three, using H¹(O(k))=0 on P² and taking equivariant Hom gives

    dim Hom_G(P,A⊗A)=0,
    dim Hom_G(P,D⊗Sym²A)=2.

Thus every allowable s has a **unique** equivariant homogeneous quadratic lift R:P O(-3)→D O(-1), with s=[LR], and the space is exactly two-dimensional. The two actual coefficients remain **unselected**. The calculation does not claim every abstract allowed map occurs geometrically.

## 4. Exact original-fourth comparison and its domain

Choose original corrected lifts d,−x,−y,−z with qx=T_ad, qy=−T_ax and qz=−T_ay. Their fourth representative is −T_az, while the quotient third at L_ad is represented by T̄_a z̄. With the natural endpoint identification,

    ιβ₄,M|D=−sL.

All identities are homogeneous global sheaf identities with correction ambiguities taken modulo the lower-symbol images. Generic surjectivity of L and torsion-freeness of J imply that the original fourth on **surviving D** vanishes identically iff s=0, equivalently R=0. This equivalence is not a value of the gate. Additional specialized A-kernels at second-rank-drop directions are not covered.

PR1022 and PR1025 report independent full-proof review and respectively 38 and 49 ordinary/optimized checks. The written actual-map argument uses pinned geometric inputs; synthetic tests are not proof-assistant certification. No actual coefficient, compatible radical or source is selected, and four necessary pairs across three labels remain.
