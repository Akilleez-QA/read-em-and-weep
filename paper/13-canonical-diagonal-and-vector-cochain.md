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

Mr. Slop's [PR654][SG] constructs a distinct spectral curve S→L from the twisted Gram endomorphism M:V O_L→V O_L(4), with equation λ³=det M. It is smooth of genus ten, totally ramified at the twelve determinant zeros, and is not the genus-four cubic support D. The actual spectral line ℒ has π_*ℒ=V O_L and ℒ²=π^*O_L(8). Consequently ℒ⊗π^*O_L(−4) has exact order two, while Θ=ℒ⊗π^*O_L(−1) is an ineffective theta characteristic. The complete centralizer is

    Cent(M)=O_L⊕O_L(−4)⊕O_L(−8).

In particular there is no nonzero trace-free commuting operator of degree below four. These constraints apply to commuting corrections only: no commutation of the actual R with M has been proved, and the spectral construction does not evaluate its class.

Mr. Slop's [PR655][SD] shows that the nontrivial spectral two-torsion is not invariant under the cubic deck transformation. Neither the spectral module nor its theta characteristic admits a nonidentity deck lift, even after a base-line twist. Its conjugates generate a connected étale Klein-four cover of S; the composite over L has A4 group and genus 37. An order-three quotient is a genus-nine tetragonal curve C with balanced direct image O_L⊕V O_L(−4).

[PR656][TC] identifies C with the actual smooth (4,4) Gram curve b(v,v)=b(v,Mv)=0 on the fixed Gram conic times L. It has canonical line O_C(2,2), two degree-four projections, and gonality exactly four. This is an actual curve construction, unlike the excluded conditional degree-eighteen third-gate curve in Chapter 14.

[PR657][TRC] proves that the two reduced twelve-point ramification orbits R₁,R₂ are disjoint, with Ram(pᵢ)=2Rᵢ, pullbacks 3R₁+R₂ and R₁+3R₂, and A5 quotient signature (3,5,5). The ruling difference O_C(1,−1) has exact order five; it gives a connected étale genus-41 cyclic cover with commuting A5 action and quotient signature (3,3,3,3,3). This genus-nine five-torsion, the genus-ten spectral two-torsion, and the genus-four support five-torsion are different classes on different curves. No torsion transfer or fourth-obstruction value is inferred.

The vector-cochain statements below concern the effective twelve-dimensional lower quotient, not the full C/J₀ class. [Chapter 16](16-canonical-fourth-input-and-complete-test.md) gives the exact thirteen-dimensional information loss and explains why keeping the full homogeneous normal matrix does not recover it.

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

The [vector-cochain theorem][V] then represents the actual lower class in the effective twelve-dimensional quotient by R/ν, where

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

## 13.6 The actual quintic scalar cup is an isomorphism

Let p represent the actual nonzero quintic extension e∈H¹(V O_L(−8)). The [swapped-quotient theorem][SC] identifies the actual cup map

    C_e: H⁰(D5 O_L(2)) → H¹(V O_L(−6)),
    u ↦ [τ(p,u)]

as an isomorphism of fifteen-dimensional representations, each with character A⊕V⊕P4⊕D5. It therefore surjects onto the reduced twelve-dimensional source after quotienting by the actual connecting A. Subsequent multiplication by every a≠0 is onto P4. These statements concern a factor of the tied vector cochain.

To identify that factor, swap the two projections of the actual cubic D and use the inverse of its nowhere-zero quintic trivialization, rather than a new unrelated section. The resulting complete intersection has degree-six socle O(2); its perfect degree-four/degree-two pairing gives the actual quotient on P(W′),

    0 → W O(−3) → D5_negative O → A_negative O(2) → 0.

After twisting by two, its section map is an isomorphism. Its coefficient tensor is proportional to the polarized actual e tensor in the one-dimensional invariant space V⊗A⊗D5_negative. This tensor comparison occurs before taking fifteen-dimensional section spaces; their four-dimensional equivariant Hom space alone would not identify the map. The swapped socle functional is used here, not the swapped quintic extension class.

Transposing via apolar forms and Serre duality gives C_e, up to a nonzero scalar. With the source's convention the universal positive identity is

    ⟨τ(r,u),v⟩₂ = 24⟨u,rv⟩₄.

Combining this isomorphism with Section 13.5 proves that the isolated polarized u term fills the fifteen-space. Its reduced image is V⊕P4⊕D5, with kernel 1⊕A⊕P4⊕D5 in D5_positive⊗D5_negative. The prescribed affine-frame scalar and a² terms in R are still tied to u; this scalar-factor argument does not evaluate their sum or final quotient. The latter is now zero by Section 15.

## 13.7 A twelve-point polar representative

Twist the quintic inclusion and write i:V O_L(−2)→P4 O_L. The [polar-normal-form theorem][PN] proves a second actual Gram identity

    N=𝒬𝒬ᵗ=d iᵗi,        d≠0.

Its nonzeroness is geometric: a three-dimensional subspace of the nondegenerate symmetric five-space D5 cannot be totally isotropic. The one-dimensional quartic Hom space then identifies N with the already known Gram map. Its degeneracy orbit E consists of the same twelve reduced points.

On L∖E the orthogonal right inverse is S=𝒬ᵗN²/det N, with exactly twelve simple poles and rank-one residues in ker 𝒬. If F=k a Lie_(D_a)(𝒬h), the global scalar is

    u=S(2)F−jw,

where j:W′ O_L(−1)→D5 O_L(2) is the actual kernel inclusion. The unique meromorphic w matches the principal parts of S(2)F. Acyclicity of W′ O_L(−1) gives uniqueness, not w=0; the extension correction remains.

The actual sextic evaluation q:P4 O_L→O_L(6) has orthogonal lift qᵗ/(qqᵗ). Its corresponding meromorphic quintic generator g_⊥ has simple poles on E and canonical Gram primitive v_⊥=0. For a regular target generator g_x=g_⊥+p_xf, write p_x=r_x/z+O(1). The source remains g_⊥, so m_⊥=m_x+n_hp_x. Self-adjoint regular nilpotence gives τ(r_x,r_x)=τ(r_x,n_h(x))=0. Substitution into the full source-frame formula yields the exact double term

    R=(k/15)a(x)²τ(h,r_x)z⁻²+O(z⁻¹).

All other possible double contributions cancel; the global scalar correction contributes to the simple layer. The twelve nonzero isotropic r_x give twelve distinct square lines ℓ_x². The map h↦τ(h,r_x) is onto V with kernel ℓ_x³W′. Thus for nonzero a,h at least nine double coefficients are nonzero. This local statement has no direct cohomological nonvanishing consequence, as the next reduction shows.

## 13.8 Removable double layers and the final residue test

Put F_low=V O_L(−6). Since F_low(E)=V O_L(6) has no H¹, global meromorphic sections of F_low(2E) surject onto its whole second-principal-part layer. Every double layer can therefore be removed, including the preceding nonzero coefficients. The resulting simple-layer class is canonical modulo the global simple-pole sections:

    H¹(V O_L(−6)) = H⁰(F_low(E)/F_low)/H⁰(F_low(E)),
    dim = 36−21=15.

At the upper twist the analogous quotient has dimension 36−27=9. Multiplication by a respects these sequences, carrying the actual connecting A below into the connecting D5 above. Their further quotients have dimensions twelve and four. No elimination of the double layer determines the remaining simple-layer class. [Exact polar reduction][PN].

In compatible local Serre frames write the physical representative as

    R/ν=D_x/z²+B_x/z.

For c∈P4* annihilating im β₂,ₐ, put ζ=a iᵗc∈H⁰(V O_L(4)). The actual final class vanishes exactly when, for every such c,

    Σ_(x∈E) [⟨D_x,ζ′(x)⟩+⟨B_x,ζ(x)⟩]=0.

The actual dual sequences ensure that these tests annihilate both connecting subspaces as well as the second-symbol image. **For a outside the second-symbol degeneracy scheme Σ, the annihilator is one-dimensional.** Every square direction satisfies this condition, since Σ is disjoint from the discriminant conic. On Σ the criterion uses its full, possibly larger annihilator.

The formula is a coordinate-independent residue in transported frames, not a selected point evaluation. If D_x,B_x instead denote raw R coefficients, the physical coefficients are D_x/ν(x) and B_x/ν(x)−D_xν′(x)/ν(x)². Thus the nonconstant physical normalization also changes the simple layer. Their global vanishing in the final third quotient is now established in [Section 15](15-third-vanishing-and-fourth-frontier.md) by an exact change of meromorphic source and the six-axis argument, rather than by discarding individual polar terms.

## 13.9 A uniform C5 simple root and a nonzero opposite-pole contribution

Fix any x in the twelve-point polar orbit E, and let y∈E be the other fixed point of its order-five projective stabilizer. Take a≠0 square with divisor 2x, and h≠0 in the unique positive-quartic character detectable by the final third quotient at a. These hypotheses are essential; the theorem is uniform over this stabilizer orbit, not an assertion for arbitrary h. The [C5 correction theorem][C5] proves that the actual vector-valued scalar u has exactly one common zero, of order one, at x. In particular u(y)≠0 and u is not divisible by a.

In an arbitrary stabilizer eigenbasis, with a=t² and h=X⁴, the weight constraints and actual quotient kernels give

    u=b₀ XY³t²+b₁ X³Yst,        b₀b₁≠0.

The nonvanishing at y follows from the actual twist-one connecting map: the would-be quotient after division by s has a nonzero boundary. The other coefficient cannot vanish without contradicting the cubic kernel at x. Thus Γ_sc also has exact order one at x, although 𝒬(Γ_sc) has exact order five. Restriction to the cubic hides a lower-order extension contribution.

In the polar representative, R is regular at x and has zero double coefficient at y. The **full** opposite-pole contribution, not just its isolated scalar summand, is nevertheless nonzero. In the volume-compatible coordinate v=−s/t with a=1, let m_y be the regular target coefficient. The exact ratio and residue are

    u(y)=−8k m_y(y),
    Res_y(R/ν)=−τ(r_y,u(y))/(60ν(y))
              =(2k/(15ν(y)))τ(r_y,m_y(y))≠0.

The ratio comes from the symplectic pairing of the two actual cubic representations and the actual socle-annihilation identities. In abstract coefficient-line notation the symplectic relation is AD+BC=0. This is a universal tensor identity, not chosen numerical HM data. Retaining the source relation m_⊥=m_y+n_hp and the oriented coordinate is necessary for the sign and factor. Since the double coefficient at y is zero, the physical normalization contributes no derivative correction there.

This contribution pairs nontrivially with the local final test ζ=a iᵗc. It does **not by itself** evaluate the global residue sum. [Section 15](15-third-vanishing-and-fourth-frontier.md) now proves that sum zero in the final quotient by an exact meromorphic-source comparison. The nonzero full local residue remains valid: the other contributions cancel it globally. This does not settle the four-or-five theorem.

## 13.10 What the later vanishing does and does not say

The actual Gram primitive and the canonical diagonal now specify the vector cochain, including the scalar-extension correction. Neither the a² terms nor the last τ(p,Γ_sc) term can be discarded independently. [Section 15](15-third-vanishing-and-fourth-frontier.md) evaluates their final third class as zero using the full formula and transported frames. The nonzero Gram composite, scalar-cup isomorphism and nonzero double coefficients do not imply a nonzero third gate: every double layer is removable. The C5 calculation also gives a nonzero full local simple residue, but its tied global sum in the final third quotient is now zero. The detecting square input even has a nonzero lower class modulo A whose cup by a is exact; zero final obstruction is not zero lower cochain.

These published geometric comparisons and universal checks retain the actual bundle, nonsplit quintic relation and physical equation frame. No selected HM coefficients, actual-instance matrices or numerical ranks are evaluated. The generic four-or-five theorem and original repair status are unchanged.

## Pinned source references

[G]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ebc38deccf2d0abcdd7b185c73dd57bae8682f59/research/hm/order-four-quadratic-load/ACTUAL-UPPER-QUARTIC-IS-A-GRAM-COMPOSITE.md
[D]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ebc38deccf2d0abcdd7b185c73dd57bae8682f59/research/hm/order-four-quadratic-load/ACTUAL-CONE-DIAGONAL-IS-CANONICAL-RESIDUE-INVERSE.md
[V]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ebc38deccf2d0abcdd7b185c73dd57bae8682f59/research/hm/order-four-quadratic-load/ACTUAL-THIRD-SHADOW-AS-A-CANONICAL-VECTOR-COCHAIN.md

[GS]: https://github.com/Akilleez-QA/read-em-and-weep/blob/15adb8e5ea61f07e87df6a0044b7375e580fe7f3/research/hm/order-four-quadratic-load/ACTUAL-CANONICAL-SCALAR-CORRECTION-SURJECTS-ONTO-FIFTEEN-SPACE.md
[RS]: https://github.com/Akilleez-QA/read-em-and-weep/blob/348954d279e0acae8ef75d0dd5eab58c5eae8928/research/hm/cubic-ramification-signature/PROOF.md

[SC]: https://github.com/Akilleez-QA/read-em-and-weep/blob/bdc66692b5814b65e568615639cd86a2b0cd5d0c/research/hm/order-four-quadratic-load/ACTUAL-QUINTIC-SCALAR-CUP-IS-A-SWAPPED-QUOTIENT-ISOMORPHISM.md
[PN]: https://github.com/Akilleez-QA/read-em-and-weep/blob/bdc66692b5814b65e568615639cd86a2b0cd5d0c/research/hm/order-four-quadratic-load/ACTUAL-VECTOR-SHADOW-HAS-A-TWELVE-POINT-POLAR-NORMAL-FORM.md

[C5]: https://github.com/Akilleez-QA/read-em-and-weep/blob/5e1d5ab619dfb2e765232d021be0373d9d2bed19/research/hm/order-four-quadratic-load/ACTUAL-C5-SQUARE-CORRECTION-HAS-A-SIMPLE-ROOT.md
[SG]: https://github.com/Akilleez-QA/read-em-and-weep/blob/f0c94ff7979652c094da3efaa11fea4629dbf59a/research/hm/gram-spectral-geometry/PROOF.md

[SD]: https://github.com/Akilleez-QA/read-em-and-weep/blob/b33a4f9c86a370ad4e96ba3cc1843ed9ef70bfe7/research/hm/spectral-deck-obstruction/PROOF.md
[TC]: https://github.com/Akilleez-QA/read-em-and-weep/blob/561f4cf5e4ad23a9f384936816d7a6ef0bd07dd6/research/hm/tetragonal-canonical-model/PROOF.md
[TRC]: https://github.com/Akilleez-QA/read-em-and-weep/blob/d55aa293629c54036d47da439fc1e1bf99e2f941/research/hm/tetragonal-ramification-constraints/PROOF.md
