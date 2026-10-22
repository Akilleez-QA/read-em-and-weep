# 13. The canonical diagonal and actual vector cochain

## 13.1 The upper quartic is an actual Gram composite

The quartic map M_κ from Section 12.3 is now identified with an actual composite, not just a nonzero permitted channel. Let i be the inclusion in the nonsplit quintic-relation sequence

    0 → V O_L(−3) → P4 O_L(−1) → O_L(5) → 0.

Choose invariant symmetric nondegenerate pairings on V and P4. The [Gram theorem][G] proves

    M_κ = c iᵗ(3)i(5): V O_L(2) → V O_L(6),     c≠0.

The proof first lifts the actual n_h uniquely through

    0 → O_L(−2) → P4 O_L(4) → V O_L(6) → 0.

Its obstruction is an equivariant map D5→H¹(O_L(−2))=1, hence zero; the absence of H⁰(O_L(−2)) gives uniqueness. The lift descends through the actual quartic quotient D5 O_L→V O_L(2), since its restriction to W′ O_L(−3) cannot map to O_L(−2). The remaining equivariant Hom space is one-dimensional, giving c i(5). Nonzeroness comes from the established actual multiplication M_κ, not from assuming a composite of nonzero maps is nonzero.

The inclusion i(5) remains a rank-three subbundle everywhere, with quotient O_L(10). Its Gram composite loses rank where its image meets the kernel line of iᵗ(3). Both tr M_κ and tr(M_κ²) vanish by the absence of invariants in Sym⁴W and Sym⁸W. Cayley–Hamilton therefore gives the twisted-endomorphism identity

    M_κ³ = (det M_κ) id_V.

At each of the twelve simple determinant zeros, M_κ has rank two and is regular nilpotent: after any scalar identification of the line fibers it is one length-three Jordan block. Its square has rank one, producing an intrinsic kernel flag independent of that scalar choice. This cube is matrix composition under the pushforward identifications, not multiplication by κ³ on D. The nontrivial torsion-line factor prevents an inference that D is a cyclic triple cover.

Mr. Slop's complementary [PR653][RS] identifies the geometric sheet lost at these fibers. For the two trigonal projections p₁,p₂ of the actual genus-four curve D, their reduced ramification orbits R₁,R₂ each have twelve points and are disjoint. Their quotient signature is (2,5,5), and

    p₁^*Ω₁=2R₁+R₂,      p₂^*Ω₂=R₁+2R₂,      div κ=R₁.

Thus the determinant pullbacks have common reduced support of length twenty-four, not disjoint support. An exceptional p₂-fiber is 2r+s, with r∈R₂ and s∈R₁. Multiplication by κ is a unit on the double sheet 2r and zero on the simple sheet s; its completed-base elementary divisors are (1,1,t). The exceptional vector equation n_h(ℓ)=0 is exactly the condition that h have a double root at p₁(r), rather than a condition on the nilpotent direction of 2r. For nonzero h it holds at at most two of the twelve exceptional base points. A nonzero a can kill at most two further points, so the actual upper entry is nonzero at at least eight of them. This excludes orbit-wide upper-entry disappearance, not cancellation in the full normal class.

## 13.2 The diagonal is fixed by the canonical residue inverse

Normalize D_a=a_s∂_t−a_t∂_s, retaining the actual nonzero Atiyah scalar k. Let 𝒬 denote the actual quartic quotient D5 O_L→V O_L(2), identified through the socle pairing. Its induced map on sections after twisting by two is an isomorphism. The [canonical diagonal theorem][D] defines the global scalar correction u uniquely by

    𝒬(u)=k a Lie_(D_a)(𝒬h).

In the chart z=t/s, with normalized positive cover coordinates,

    D_a=2a∂_z+(a_z/2)E,
    Λ=2k a a_z h−u,
    A₁₁=Λ/2−m,              A₁₂=−2k a²n_h.

Here E is the positive-cover Euler field, and H D_af=m f+2k a²n_h g with H=k a h. The effective scalar Λ is local; u is a global mixed quartic. They must not be identified.

The fixed-determinant derivation uses the canonical subline action γ=−u/2 and the operator-induced relation matrix M=γI−A_full. An arbitrary relation matrix only fixes its trace modulo (f,g) and cannot replace M in the exact calculation. The natural determinant action gives tr A_full=−4(a_z/2)H. Passing to the tracefree connection then gives precisely the displayed Λ, including its sign and factor two. Thus the diagonal is no longer an independent unspecified scalar, but its contribution to the global shadow is still unevaluated.

## 13.3 The normalized source-frame formula and its scalar-extension term

Let τ be the unnormalized second positive binary transvectant,

    τ(v,w)=v_xx w_yy−2v_xy w_xy+v_yy w_xx.

All derivatives in τ are in positive cover variables. On a pure quintic overlap g_j=g_i+pf, put

    m_(h,i)=(h f_z−n_h g_i)/f,       Γ_sc=u+2k a a_z h.

The regular coefficient m_(h,i) belongs to the **source i-frame**. The harmonic discrepancy K belongs to the **target j-frame**, and only the trace uses g_j. The exact formula is

    K₁₁=−(k/3)a²τ(p,n_h),
    K₂₁=k a²U+τ(p,Γ_sc)/30,
    U=2τ(p,m_(h,i))/15−τ(p²,n_h)/15
        −τ(p,p)n_h/3+τ(h,p_z)/15.

Its physical square-ideal shadow is (2f g_j K₁₁−f²K₂₁)/ν for q₀=νq. Replacing m_(h,i) by m_(h,j)=m_(h,i)−pn_h without compensation would lose a term. Replacing g_j in the trace by g_i would likewise omit 2pf²K₁₁. These are actual frame conventions, not interchangeable notations. [Normalized cochain][D].

The residue identity also gives

    𝒬(Γ_sc)=2k a²(𝒬h)_z.

This proves divisibility by a² only after restriction to D. The local derivative on the right is a connection coefficient with inhomogeneous frame transformation, not a global section of a formally assigned twist. For local lifts ℓ_i, the precise statement is

    Γ_sc−2k a²ℓ_i=f l_i,

where l_i is a positive linear form with its actual base factor. The terms τ(p,f l_i)/30 remain in K₂₁. No argument has made them commutators or global coboundaries; ambient divisibility by a² is not asserted.

## 13.4 An actual vector representative in a fifteen-to-twelve quotient

The unique Gram lift in Section 13.1 supplies the compatible local primitive v_i with

    v_j−v_i=τ(p_ij,n_h).

The [vector-cochain theorem][V] then represents the actual lower class by R/ν, where

    R_ij=−K₂₁+(2k/3)a²p_ij v_i.

For the exact check, set d_i=−(k/3)a²v_i. In the transported coefficient frames,

    δ(2f g_i d_i)=2f g_j(d_j−d_i)+2pf²d_i.

Since d_j−d_i=K₁₁, subtraction from 2f g_jK₁₁−f²K₂₁ leaves f²R. Thus this is an actual square-ideal coboundary reduction. The source primitive v_i and the target trace g_j have different roles; the factor ν⁻¹ and its base-frame transport remain throughout.

The two actual extension sequences are

    0 → V O_L(−6) → P4 O_L(−4) → O_L(2) → 0,
    0 → V O_L(−4) → P4 O_L(−2) → O_L(4) → 0.

Their connecting maps identify

    H¹(P4 O_L(−4)) = H¹(V O_L(−6))/A,      15−3=12,
    H¹(P4 O_L(−2)) = H¹(V O_L(−4))/D5=P4,  9−5=4.

The A and D5 embeddings are the actual extension boundaries, not selected representation copies. Multiplication by a commutes with the sequences and carries the lower ambiguity into the upper ambiguity. The actual third value is the resulting P4 class followed by the actual second-symbol quotient. An explicit vector representative does not remove that last quotient or decide the class.

## 13.5 The actual scalar correction surjects onto the fifteen-space

The [Gaussian theorem][GS] determines the image of the actual u in Section 13.2. Polarize a² to a negative quartic S∈Sym⁴W=D5. With the unnormalized first negative transvectant,

    𝒬(u(S,h))=(k/2)(S,𝒬h)₁,
    D5_positive ⊗ D5_negative → H⁰(D5 O_L(2))

is surjective. The target is A⊕V⊕P4⊕D5 of dimension fifteen; the kernel is 1⊕P4⊕D5 of dimension ten. This is a uniform theorem for the actual scalar map, not a selected matrix-rank evaluation.

For the geometric input, put K=ker 𝒬=W′ O_L(−3). Its actual second fundamental map into V O_L is nonzero, since otherwise the kernel's Grassmannian classifying map would be constant, contradicting degree −6. A saturated rank-one image is excluded by the absence of W′ in SymʲW for 0≤j≤3. The maximal minors have degree six, below the minimum invariant orbit length twelve, so the map has rank two everywhere:

    0 → W′ O_L(−3) → V O_L → O_L(6) → 0.

Under the invariant apolar pairing, an annihilator z of the Gaussian image obeys

    𝒬ᵗ z_z−2(𝒬_z)ᵗz=0.

Restricting to K puts z in the kernel of the transposed second fundamental map. The dual exact sequence, twisted by four, identifies this kernel with O_L(−2), which has no sections. This proves surjectivity; the actual section isomorphism induced by 𝒬 transports it back to u. Character subtraction then gives the stated kernel, without guessing the relative repeated P4 and D5 coefficients.

Surjectivity of this factor does not evaluate the full vector cochain R: the quintic-extension correction and final second-symbol quotient remain. In particular it is not a proof that the third shadow is nonzero.

## 13.6 What is not yet evaluated

The actual Gram primitive and the canonical diagonal now specify the vector cochain, including the scalar-extension correction. Neither the a² terms nor the last τ(p,Γ_sc) term can be discarded independently; their combined global class and possible cancellation remain uncomputed. The nonzero Gram composite and its exceptional nilpotent fibers do not imply a nonzero third gate.

These published geometric comparisons and universal checks retain the actual bundle, nonsplit quintic relation and physical equation frame. No selected HM coefficients, actual-instance matrices or numerical ranks are evaluated. The generic four-or-five theorem and original repair status are unchanged.

## Pinned source references

[G]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ebc38deccf2d0abcdd7b185c73dd57bae8682f59/research/hm/order-four-quadratic-load/ACTUAL-UPPER-QUARTIC-IS-A-GRAM-COMPOSITE.md
[D]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ebc38deccf2d0abcdd7b185c73dd57bae8682f59/research/hm/order-four-quadratic-load/ACTUAL-CONE-DIAGONAL-IS-CANONICAL-RESIDUE-INVERSE.md
[V]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ebc38deccf2d0abcdd7b185c73dd57bae8682f59/research/hm/order-four-quadratic-load/ACTUAL-THIRD-SHADOW-AS-A-CANONICAL-VECTOR-COCHAIN.md

[GS]: https://github.com/Akilleez-QA/read-em-and-weep/blob/15adb8e5ea61f07e87df6a0044b7375e580fe7f3/research/hm/order-four-quadratic-load/ACTUAL-CANONICAL-SCALAR-CORRECTION-SURJECTS-ONTO-FIFTEEN-SPACE.md
[RS]: https://github.com/Akilleez-QA/read-em-and-weep/blob/348954d279e0acae8ef75d0dd5eab58c5eae8928/research/hm/cubic-ramification-signature/PROOF.md
