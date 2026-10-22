# 4. Positive-sector obstruction calculation

## 4.1 Rank 33 at the invariant cone

The cone-spinor construction provides an invariant nilpotent adjoint N. The actual moving-line theorem makes every positive adjoint preserve its saturated spinor; the Ext-annihilator argument identifies every preserving adjoint with a polynomial multiple of N. Therefore

    H⁰(B_Q₀(4))₊ = N H⁰(O_Q₀(2))₊ = N(A ⊕ D5).

The kernel dimension is eight, so the 41-to-37 map has rank 33. Its cokernel is P4, of dimension four. The updated [rank theorem][R] records first-order vanishing; the following subsections explain that result and the subsequent second-order advance.

## 4.2 Why the first Bockstein is identically zero

The same centralizer argument at lower twist gives H⁰(B_Q₀(2))₊ = C N. Let ξ be the restriction connecting class of N in H¹(B)₊. Then

    ker(q₀: H¹(B)₊ → H¹(B(2))₊) = C ξ.

The actual characters are H¹(B)₊ = 1 ⊕ A ⊕ V ⊕ D5 and H¹(B(2))₊ = A ⊕ 2V ⊕ 3P4 ⊕ 4D5. Multiplication by q₀ identifies the unique source A with the unique target A. Negative quadratic multiplication therefore has a unique equivariant correction ζₐ in that source A such that

    aξ = q₀ζₐ.

For h ∈ A ⊕ D5, associativity in the actual cohomology module yields

    ahξ = h(aξ) = q₀(hζₐ).

Its class in the q₀-cokernel is zero. Thus the entire first Bockstein vanishes, including γ. The corrected vector hξ − t hζₐ satisfies

    (q₀ + ta)(hξ − t hζₐ) = −t²ahζₐ.

The canonical second Bockstein is accordingly β₂,ₐ(hξ) = −[ahζₐ] ∈ P4. Because the first Bockstein is zero, changing the first correction does not change this class. [Cyclic Rao proof][F].

## 4.3 The square filtration kills D5 at second order

The actual cone is treated through its weighted-stack square sequence, not through a guessed split vertex module. The ordinary square of the regular initial cubic/quintic pair has cover-degree Hilbert function

    1, 2, 3, 4, 5, 6, 6, 6, 5, 4, 2, 1.

Its degree-eight relation isolates a canonical quadratic family ωₐ ∈ P4 ⊗ A*. The physical inversion parity and the ordinary-square filtration give

    β₂,ₐ(hξ) = 0      for h ∈ D5,
    β₂,ₐ(hξ) = hωₐ   for h ∈ A.

In fact, the stronger actual multiplication map D5 ⊗ H¹(B_Q₀(2))₊ → H¹(B_Q₀(4))₊ is zero. The remaining equivariant quadratic channel has only one possible scalar. At this stage of the argument that scalar is not yet known; its nonvanishing requires geometry. [Filtration proof][S].

## 4.4 The actual scalar is nonzero

The projective pullback orbit identifies the appropriate ambient deformation class with trace-free Atiyah contraction. If Dₐ is the negative SL₂ vector field corresponding to a, uniqueness of the A constituent identifies ζₐ with a nonzero scalar multiple of At_F(Dₐ).

For the regular spinor section σ, the expression σ ∧ Dσ is well-defined modulo the ordinary square of its zero ideal: changing a local lift or frame adds σ ∧ Mσ, which is quadratic in the section components. This gives a frame-independent square-shadow representative for the relevant connecting class.

The actual quintic relation gives a nonsplit extension

    0 → V O_L(−8) → P4 O_L(−6) → O_L → 0,

with nonzero class e. A splitting is excluded by the corresponding positive-to-negative line-bundle Hom vanishing. Differentiation of the relation identifies the actual obstruction, up to a common nonzero scalar and sign, as

    ωₐ = j_*(aDₐe).

The kernel of j_* is A. The universal SL₂ map controlling aDₐe is injective on the relevant sextic space; its nonzero G-image is D5, which cannot lie in the A kernel. Consequently the actual scalar is nonzero. This argument identifies the actual map before invoking representation theory. It does not assign an arbitrary nonzero coefficient to a merely permitted channel. [Full Atiyah/quintic proof][N].

## 4.5 Generic rank three and the four-or-five theorem

The resulting A-input is a nonzero multiple of h ↦ projection_P4(a²h). At a square direction a = ℓ², a kernel vector would give a sextic in the complementary V linear series divisible by ℓ⁴. That series has Wronskian degree 3(6−2) = 12. Such a sextic forces ramification weight at least two, while its group orbit has at least twelve points, requiring total weight at least 24. This contradiction proves injectivity at every square direction and hence on a nonempty open set. That open set also contains nonsquare directions, for which q₀ + ta is smooth when t ≠ 0.

Thus β₂ has generic rank three. The actual positive pencil has generic rank at least 36. Rank-nullity bounds its kernel between four and five, and semicontinuity extends the upper bound to a nonempty open set of inversion-even quadrics. Combining with Section 3 gives the total four-or-five result. [Integrated proof][G].

## 4.6 The next obstruction, without a nonvanishing claim

At a direction where β₂ has rank three, its surviving source is D5 and its target quotient P4/im β₂ is one-dimensional. For h ∈ D5, choose vₕ with q₀vₕ = ahζₐ; existence is precisely second-order vanishing on D5. Then

    (q₀ + ta)(hξ − thζₐ + t²vₕ) = t³avₕ.

The next class is [avₕ] modulo im β₂. Changing the second correction affects the q₀-cokernel through β₁ = 0; changing the first correction accounts for the quotient by im β₂. This explains the canonical third gate. Its actual value is now proved zero in [Section 15](15-third-vanishing-and-fourth-frontier.md); a fourth or later obstruction is needed. The section-count conclusion remains the established four-or-five theorem; the following reductions do not strengthen that bound.

## 4.7 The third obstruction as an actual secondary multiplication tensor

Put M_j = H¹(B(j))₊, K = ker(q₀:M₂→M₄), P = coker(q₀:M₂→M₄), and C = coker(q₀:M₀→M₂). Here P is the four-dimensional cokernel representation, not projective space; C is a lower cokernel, not the line configuration of Section 7.

The cone square-filtration theorem has the ambient consequence

    hM₂ ⊂ q₀M₂   for every h ∈ D5.

Indeed restriction commutes with multiplication, the product vanishes on the cone, and exactness identifies the kernel of restriction from M₄ with q₀M₂. No surjectivity of the lower restriction is needed. This defines a canonical actual tensor

    Ψ: A ⊗ D5 ⊗ C → P,
    Ψ(a,h,[x]) = [av],   where q₀v = hx.

Changing v by k ∈ K changes the output by [ak] = 0, using first-Bockstein vanishing. Changing x by q₀y changes it by [ahy] = 0, using hM₂ ⊂ q₀M₂. These are separate independence checks. The operation uses division in the actual ambient module, not just the cone's ordinary-square ideal.

The third obstruction is consequently

    β₃,ₐ(hξ) = Ψ(a,h,[aζₐ]) modulo im β₂,ₐ.

The quadratic family a ↦ [aζₐ] has no invariant component because C = V ⊕ 3P4 ⊕ 3D5 has no trivial constituent. It probes a particular actual D5-valued family inside C, not an arbitrary class. Nonvanishing of its square-boundary image does not prove that Ψ detects it. This tensor construction alone is a reduction, not an evaluation. [Section 15](15-third-vanishing-and-fourth-frontier.md) now proves the actual third gate zero; it does not assert that the entire trilinear tensor on arbitrary C inputs is zero. [Secondary multiplication theorem][T].

## 4.8 A distinct endpoint: squares as a Gauss derivative

Let T = P(W*) parametrize negative hyperplanes H_ℓ. The uniform hyperplane results give actual multiplication maps

    M₂,₊ → M₃,₋ → M₄,₊,
    dimensions 41 → 54 → 37,

where both arrows multiply by ℓ, the first is injective, and the second is surjective. The actual plane-restriction sequence is

    0 → E → V₃₀ ⊗ O_T → D_lin(1) → 0,
    rank E = 17,  deg E = −54,
    rank D_lin = 13,  deg D_lin = 41.

Here V₃₀ denotes the constant thirty-dimensional plane-section space, not the representation V used earlier. Its second fundamental form is SF:E→D_lin(−1), because Ω_T = O_T(−2).

The comparison is an identity of actual maps. Locally ℓ = u + zv, and a section k with ℓk = 0 represents the plane-section class (k,zk) in the Koszul quotient. The quotient map is [(x,y)] ↦ [y−zx] modulo ℓM₂,₊. Applying it to the derivative of (k,zk) gives [k]. This is exactly the middle map ker(ℓ:M₃,₋→M₄,₊) → coker(ℓ:M₂,₊→M₃,₋) in the composition exact sequence. Therefore, with natural parameter-line factors understood,

    rank(ℓ²:M₂,₊→M₄,₊) = 24 + rank SF_ℓ.

This endpoint map ℓ² is different from the invariant-cone smoothing map q₀ + tℓ². A bound for one must not be substituted for a bound for the other. [Actual Gauss comparison][A].

## 4.9 A saturated flag excludes generic Gauss rank one

Two actual presentations give H⁰(E) = 0 and H⁰((D_lin(1))*) = 0. Thus E contains no nonzero constant subbundle, and its fibers span the entire constant thirty-space.

Suppose SF had generic rank one. Taking sheaf kernels backward and saturated derivative images forward constructs a complete flag F_i of subbundles of V₃₀ ⊗ O_T, with rank F_i = i and F₁₇ = E. It cannot terminate early: a derivative-invariant saturated subbundle is constant in characteristic zero, contradicting one of the two preceding vanishings. Every adjacent derivative is a nonzero regular map

    L_i → L_(i+1) ⊗ O_T(−2),   L_i = F_i/F_(i−1).

Writing d_i = deg L_i, its zero divisor has degree δ_i = d_(i+1) − d_i − 2 ≥ 0. The identity Σd_i = 0 then gives, in general ambient rank N and intermediate rank r,

    N deg F_r = −Nr(N−r)
      −(N−r) Σ_(j<r) jδ_j − r Σ_(j≥r) (N−j)δ_j.

Hence deg F_r ≤ −r(N−r). For N = 30 and r = 17, rank one would force deg E ≤ −221, contradicting deg E = −54. Rank zero would make E constant and is also impossible. Therefore SF has generic rank at least two, so the actual square endpoint has generic rank at least 26. Equivalently, its positive kernel has dimension at most fifteen and cokernel at most eleven. Saturation ensures that ramification contributes nonnegative zero-divisor terms, not hidden poles. These are generic bounds; rank may drop at special parameters. [Flag-degree proof][L].

This new square-endpoint bound does **not** improve the established rank-36 smoothing bound or the four-or-five section theorem. Rank thirteen for SF would suffice for positive endpoint surjectivity and hence generic surjectivity of the smoothing pencil, but rank thirteen is not proved. The tensor formula alone does not establish third-Bockstein nonvanishing, which is now excluded by Section 15. These reductions distinguish the endpoint-rank problem from the remaining fourth-or-later smoothing obstruction.

## 4.10 Complete rank-two exclusion by endpoint flags

Suppose provisionally that SF has generic rank two. Its maximal saturated rank-two plateau has k blocks below E and l above it, with 1 ≤ k ≤ 8 and 1 ≤ l ≤ 6. The lower endpoint rank and upper endpoint codimension are p = 17−2k and q = 13−2l. These are conditional invariants of a hypothetical rank-two case, not measured ranks of a chosen instance.

The projective A₅ action on the parameter line has exceptional orbit lengths 12, 20 and 30; ordinary orbits have length 60. Consequently every effective invariant derivative-determinant divisor has degree in the semigroup generated by 12, 20 and 30. Saturated endpoint spans and the rank-one flag inequality strengthen the plateau bound to

    54 ≥ 17l + 13k − 2kl.

Only (1,1), (1,2), (2,1), (2,2) and (3,1) survive this inequality. The orbit divisors then exclude (2,2): its lower endpoint would require ramification weight 34, whereas the least positive permitted weight is 48. For (3,1), the endpoint flag is forced unramified; projection to its constant span gives a rank-fourteen kernel of degree at least −18. The actual vanishing H⁰(E(1)) = 0 instead forces that kernel's degree to be at most −28, a contradiction. The projection argument allows torsion between an image and its saturation; it does not assume a horizontal splitting.

The earlier orbit-ramification theorem reduces the necessary list to

    (k,l) ∈ {(1,1), (1,2), (2,1)}.

The [earlier theorem][O2] stops at this list. The [completed endpoint-flag theorem][E2] now excludes all three profiles, as follows.

Let U and Z be the constant spans of the lower endpoint and upper dual endpoint. A diagonal-contact lemma for their complete rank-one flags proves that either U and Z are orthogonal with the minimum possible dimensions, or both first-line degrees exceed a large contact threshold. The nonorthogonal alternative contradicts the plateau degree identity and the complete-flag ramification arithmetic in each of the three profiles. In particular the argument retains both the weighted ramification equation and the even-integral first-line degree condition, rather than using dimensions alone.

In the orthogonal alternative, saturation and the absence of constant subbundles give exact intersections between each plateau stage and U. The resulting projection of E has a saturated image P and an actual image I. Its torsion length τ belongs to ⟨12,20,30⟩, and the degree identity is

    54 = D_C + D_B + τ.

For (2,1), the lower bound from H⁰(E(1)) = 0 forces equality in the upper rank-one degree bound. The upper flag would then have odd line degrees, contradicting its center-even linearization. For (1,1) and (1,2), τ is smaller than 12, so τ = 0. This gives an actual equivariant exact sequence, not a claimed horizontal or direct-sum splitting.

For (1,1), the five remaining pairs (D_C,D_B) are (32,22), (34,20), (36,18), (38,16), and (42,12). The required injections W ⊗ U → Sym^(D_C+1)W and Z → Sym^D_B W impose disjoint exact character conditions on every possible dimension-seventeen submodule U of the actual constant representation. All five pairs are impossible.

For (1,2), only (38,16) and (42,12) remain. The upper line quotient determines U, while the final two lower flag lines determine its twisted quotient cohomology. The exact sequence would give, respectively,

    H¹(E(1)) = W + W′ + S₄ + 2T₆,
    H¹(E(1)) = W + 3S₄ + T₆.

Neither equals the independently established actual character W′ + 3T₆. This excludes the last two possibilities without assuming the numerical flag data are geometrically realizable.

Combining these exclusions with the rank-zero and rank-one arguments gives the generic bounds

    rank SF ≥ 3,
    rank(ℓ²:M₂,₊→M₄,₊) ≥ 27.

Thus the square-endpoint positive kernel has dimension at most fourteen and its cokernel at most ten. Rank thirteen for SF, positive-square surjectivity, and the last smoothing obstruction remain unproved. **The generic section-count theorem remains four or five.** The [reproduction script][E2V] checks bounded flag arithmetic and exact representation characters; the geometric diagonal-contact, saturation, and projection arguments remain mathematical proofs in the cited text, not claims of formal verification.

## 4.11 The fixed actual cubic probe has zero normal variation

Hold the actual probe t(a) = [aζ_a] fixed while varying the first-normal extension in its affine torsor. The exact first-normal-to-cubic variation map L is zero; its kernel is the entire one-dimensional normal direction. This holds already for the unquotiented variation of Ψ(a,h,t(a)) in P, before passing to the quotient by the actual second-symbol image. [Fixed-probe variation theorem][CV].

The Serre symmetry of Section 8.8 exchanges the two extendable normal points and acts on the affine torsor by J(s) = s_* − s. Its action on P is +1: the intrinsic cover-degree-eight square-filtration character and the adjoint-quotient character are both −1, and cancel. The fixed actual probe t(a) instead has character −1. Indeed the scalar block transformation commutes with the orbit-tangent field D_a, so naturality fixes its restricted Atiyah class ζ_a; the negative quadratic multiplier a has character −1. The positive quadratic h is fixed.

Naturality and trilinearity therefore give

    Ψ_s(a,h,t(a)) = Ψ_(s_*−s)(a,h,t(a)).

The independently established dependence on s is affine, even before quotienting. Writing it as V₀+sV₁ forces V₁=0 in characteristic zero. The target action preserves the actual second-symbol quotient, so L=0 follows there too. The [symbolic verifier][CVV] checks these sign and affine identities, not the geometric identifications.

**Zero variation alone is not zero actual cubic.** Its absolute value is constant along this auxiliary torsor when this fixed actual probe is used. The separate proof in [Section 15](15-third-vanishing-and-fourth-frontier.md) now makes its final second-symbol quotient zero; no unquotiented value is inferred from variation alone. Separately normalized probes for the two ambient bundles are not silently identified. Consequently injectivity of this particular variation map is now excluded as a route to actual cubic nonvanishing. The absolute value is now represented by the actual midpoint operator boundary, with corrected Hessian-symbol matching and zero conic contribution, as detailed in [Section 10](10-midpoint-operator-residue.md). The lower residue need not vanish, but its final third class is now zero; the four-or-five theorem is unchanged.

## Pinned source references

[O]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ec080c229105457eafcd2583c8a47b362627a62e/research/hm/order-four-quadratic-load/SPECIAL-D5-OCTIC-NONEXTENSION-EXCLUDES-A12.md
[R]: https://github.com/Akilleez-QA/read-em-and-weep/blob/eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c/research/hm/order-four-quadratic-load/POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md
[F]: https://github.com/Akilleez-QA/read-em-and-weep/blob/846968261441fef2cad247d22b66d37aed3f0f8f/research/hm/order-four-quadratic-load/POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md
[S]: https://github.com/Akilleez-QA/read-em-and-weep/blob/04fb081d710f1d7e175f252601b96dddcd93106e/research/hm/order-four-quadratic-load/POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md
[N]: https://github.com/Akilleez-QA/read-em-and-weep/blob/9f28cb10c38d7a0e29c1eb994594325fea7f22bf/research/hm/order-four-quadratic-load/ACTUAL-SECOND-BOCKSTEIN-NONZERO-BY-ATIYAH-QUINTIC.md
[G]: https://github.com/Akilleez-QA/read-em-and-weep/blob/72aa6fb732a803eb9201f45f1f82e60f54d296b4/research/hm/order-four-quadratic-load/POSITIVE-GENERIC-FOUR-OR-FIVE-SECTIONS.md

[T]: https://github.com/Akilleez-QA/read-em-and-weep/blob/09b0018bf1f36bcea641c115558ba637f6d63075/research/hm/order-four-quadratic-load/POSITIVE-THIRD-SECONDARY-MULTIPLICATION-TENSOR.md
[A]: https://github.com/Akilleez-QA/read-em-and-weep/blob/02ed933bc3474804560159a71f3a3df5b3b76177/research/hm/order-four-quadratic-load/POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md
[L]: https://github.com/Akilleez-QA/read-em-and-weep/blob/f60e8b675110220b1ce7cc0e4c760ed4f32c8b20/research/hm/order-four-quadratic-load/RANK-ONE-GAUSS-FLAG-DEGREE-EXCLUSION.md

[O2]: https://github.com/Akilleez-QA/read-em-and-weep/blob/59d0962d952fe2dd9d381c06d47361a469fe68f2/research/hm/order-four-quadratic-load/GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md

[E2]: https://github.com/Akilleez-QA/read-em-and-weep/blob/9328f0db5536fe16ccd8ea556919847e5c1e8956/research/hm/order-four-quadratic-load/RANK-TWO-GAUSS-EXCLUSION-BY-ENDPOINT-FLAGS.md
[E2V]: https://github.com/Akilleez-QA/read-em-and-weep/blob/162850b7cf3b00b4bc0edff002bcdaceb321515f/research/hm/order-four-quadratic-load/verify_rank_two_gauss_exclusion.py

[CV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/94ba164f156d712d251655f386a173d84ae04b35/research/hm/order-four-quadratic-load/POSITIVE-CUBIC-NORMAL-VARIATION-VANISHES-BY-SERRE-INVOLUTION.md
[CVV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/03c106e8bc2508eb8ea6cfa94d33be6fbe44926e/research/hm/order-four-quadratic-load/verify_positive_cubic_normal_involution.py

## 4.12 Actual Atiyah input and the six-axis family

The actual lower factor h ↦ h At_F(D_a)|_Q₀ now has a complete rank classification: rank five except on six reduced nonsquare axes, rank four there, and injectivity in every square direction. Its nine-dimensional image and complete parameter-family cokernel are proved in [Section 9](09-actual-atiyah-factor.md). The normal extension of the corrected cone operator is now measured by the exact global boundary Ψ = δ(r), and its corrected midpoint nilpotent symbol is identified in [Section 10](10-midpoint-operator-residue.md). These lower-factor results alone do not settle the third Bockstein. Its final quotient is now zero by [Section 15](15-third-vanishing-and-fourth-frontier.md), not by injectivity or surjectivity of either factor.

## 4.13 Further rank-three Gauss configurations and pairings are excluded

The saturated-flag argument bounds both rank-three plateau lengths by three. The simultaneous corner (k,l)=(3,3) is excluded by an exact five-type dual classification, a projection-saturation bound, and section persistence for the next derivative. [Corner exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/e6e83a1fafea726c4767322056084d34565bc027/research/hm/order-four-quadratic-load/EXCEPTIONAL-CUBIC-GAUSS-CORNER-EXCLUSION.md).

The adjacent profile (2,3) is also excluded. For l=3 and k≥2, the actual derivative image, after the specified twist, must have degree at least thirteen. Equivariant image and section-persistence constraints then exclude all 37 formal dual splitting types. Thus generic SF rank three with l=3 forces k=1. The same argument excludes the two (3,2) primal types with quadratic section module 2V or 3P4. [Adjacent-profile theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/7d4e3e6d960438e3000f33d0e68b9e2b970129fa/research/hm/order-four-quadratic-load/ADJACENT-RANK-THREE-GAUSS-EXCLUSION-AND-CONSTRAINTS.md).

All three further (3,2) primal types whose quadratic section module contains 2D5 are now excluded. Their forced restricted derivative image O(4)⊕O(8) determines the next quotient; complete evaluation kernels and ordinary degree bounds leave a negative line inaccessible to a required rank-three backward derivative. Together with the earlier two exclusions, this step reduced the formal list from 28 to at most 23; the further reduction below supersedes that intermediate bound. The exceptional type with no quadratic sections was not excluded by that step; the terminal exclusion below now closes it. [Two-D5 exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/a42749caf8c5c1b087e60857748360487badcf13/research/hm/order-four-quadratic-load/TWO-D5-BACKWARD-GAUSS-EXCLUSION.md).

There is also a type-independent restriction inside (3,2). The cubic pairing

    B_pair : H⁰(E(2)) O → T6 O(3)

has rank at most two. If it had rank three, its saturated projected image would be V O or V O(2), forcing the full derivative quotient. The first alternative contradicts h⁰(K(3))≥8 against a target with no sections. In the second, complete evaluation forces the next quotient, and h⁰(K₂(4))≥7 contradicts a target with three sections. Consequently its only possible nonzero image from the proved small-image list is W′ O(1); zero is also allowed. This pairing is not the adjoint bundle B or the positive secondary tensor Ψ. [Cubic-pairing theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/8c26de8e5e68fd41945373ac1f6ee280f109d716/research/hm/order-four-quadratic-load/RANK-THREE-CUBIC-PAIRING-EXCLUDED-IN-ADJACENT-GAUSS-PROFILE.md).

Six more formal primal types are excluded: the types with quadratic module 2V⊕P4 or V⊕2P4, and both types for each of V⊕P4⊕D5 and 2P4⊕D5. The proof treats both remaining cubic-pairing branches, zero and W′ O(1). Complete evaluation and backward persistence force incompatible section characters or inaccessible negative quotient lines. In the final rank-two branch, a rank-one endpoint inside its own smallest constant span would require 104 in the semigroup generated by 96, 160, 240, 60, 100 and 150, which is impossible. [Six-type exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/14fc90d90f74998c10ea9f2b45cf5b8aeac96bae/research/hm/order-four-quadratic-load/SIX-LARGE-QUADRATIC-MODULES-EXCLUDED-BY-BACKWARD-GAUSS.md).

A further backward-evaluation argument excludes the single-V quadratic type

    E = V O(−2) ⊕ (W′⊕T6) O(−3) ⊕ 2V O(−4).

The restricted cubic pairing is forced to vanish. Saturation and evaluation then leave first derivative quotients O(4)⊕W′ O(1−e), with e=2 or 4. In both branches the next derivative is onto; the final section-injectivity requirement contradicts an unavoidable V constituent (or 2V in the e=4 branch) when its target has only D5 sections. The proof treats all four necessary intermediate kernel shapes in the e=2 branch, without assuming their realizability. [Single-V exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/4ac12f3ec8f465ef8dcbb1b6a17698fc674afe80/research/hm/order-four-quadratic-load/SINGLE-V-QUADRATIC-TYPE-EXCLUDED-BY-BACKWARD-EVALUATION.md).

All three single-P4 quadratic types are now excluded as well:

    X = P4 O(−2) ⊕ 2T6 O(−3) ⊕ O(−10),
    Y = P4 O(−2) ⊕ T6 O(−3) ⊕ (V⊕P4) O(−4),
    Z = P4 O(−2) ⊕ (W′⊕T6) O(−3) ⊕ V O(−4) ⊕ W′ O(−5).

Both pairing branches are needed. For nonzero B_pair, its complete evaluation onto W′ O(1) first forces the cubic derivative image W′ O(2). The first quotient is O(n−2)⊕W′ O(−1). Backward section persistence eliminates n=−8,4 and forces zero second-image colength for n=6,8; the n=6 character is impossible. At n=8, the exact Euler characters force precisely two formal second-kernel splittings, with tails W O(−9) or O(−8)⊕O(−10). Both lead to the same rank-eight, degree −48, rank-one endpoint and the impossible ramification weight 104 above. These are exhaustive necessary splittings, not assertions that the bundles occur. [Nonzero-pairing branch][P4N].

For B_pair=0, saturation and degree inequalities similarly reduce the rank-two cubic-image branch to those two endpoint shapes. Only X admits a rank-one cubic image. There the forced line quotient O(−12) is inaccessible to the next kernel: its degree excess and parity leave only low-degree coefficient blocks whose Hom spaces or section multiplicities are impossible. This separate argument is essential; exclusion of the nonzero-pairing branch alone would not exclude the three types. [Zero-pairing branch][P4Z].

The three remaining double-P4 quadratic types are also excluded:

    X₂ = 2P4 O(−2) ⊕ T6 O(−3) ⊕ W′ O(−5) ⊕ O(−10),
    Y₂ = 2P4 O(−2) ⊕ (V⊕P4) O(−4) ⊕ W′ O(−5),
    Z₂ = 2P4 O(−2) ⊕ W′ O(−3) ⊕ V O(−4) ⊕ 2W′ O(−5).

Their quadratic derivative cannot have rank one: no eligible line's sections contain 2P4. For nonzero pairing, section injectivity forces quadratic/cubic derivative ranks three and two. The same exact first quotients and invariant colength gap reduce to the two impossible endpoint splittings already described. For zero pairing, only X₂ admits the required rank-one cubic image O(11). Its quadratic image is necessarily 2O(6), O(6)⊕O(8), or W O(7), and the colength bound makes it saturated. The next derivative would require a nonzero quotient to O(−12). Degree excess, parity and exact Hom constraints leave a single possible kernel, (2W′⊕T6)O(−3)⊕V O(−4)⊕O(−12), whose twist-three Euler character contradicts every forced quotient. Both pairing branches are therefore excluded. [Double-P4 exclusion][P4D].

The remaining single-D5 type

    E=D5 O(−2)⊕(W′⊕T6)O(−3)⊕V O(−4)⊕O(−8)

is excluded too. Its cubic pairing is zero. Rank-two cubic images reduce to incompatible section multiplicities or the frozen rank-one endpoint. In the rank-one branch, exhaustive necessary kernel/quotient splittings leave ten pairs; two further rank-three derivatives force a degree −52 second kernel with section module 2V⊕P4, which cannot inject into a target containing only one V. [Single-D5 exclusion][D5S].

All four mixed P4⊕D5 quadratic types are excluded by a two-stage argument. Their common quadratic part is (P4⊕D5)O(−2); their respective remaining parts are

    T6 O(−3)⊕O(−8)⊕O(−10),
    T6 O(−3)⊕W O(−9),
    (V⊕P4)O(−4)⊕O(−8),
    W′ O(−3)⊕V O(−4)⊕W′ O(−5)⊕O(−8).

The [first stage][MD1] forces zero cubic pairing and complete quadratic evaluation onto the saturated octic O(8), with kernel (W′⊕T6)O(−1). This necessary reduction alone does not exclude a type. The [closure][MD2] handles both remaining cubic-image ranks. For rank two, section persistence bounds the saturated image degree by eight and its defect by four, forcing saturation even in the high-line case. The remaining W′ O(2) and W′ O(4) images give the frozen endpoint or a V-multiplicity contradiction. For rank one, dimension inequalities exclude negative quotient degrees before any splitting assumption. The three positive possibilities have zero colength; two fail a low-degree bottleneck and the last again requires 2V⊕P4 to inject into V⊕P4⊕D5. This closes all four mixed types.

The twenty-three preceding disjoint exclusions left five necessary formal types. The [terminal plateau theorem][P3] now excludes all five: three with quadratic module V⊕P4, one with V⊕D5, and the zero-quadratic type. Both cubic-pairing branches are treated for V⊕P4, retaining saturation even in the high-line case. For V⊕D5, the parity-improved quadratic-kernel degree bound forces the low-line quotient and final multiplicity contradiction. In the zero-quadratic case, a rank-three cubic image contradicts persistence; the rank-two case forces three quotients, eliminated by two representation contradictions and the previously proved rank-one ramification obstruction.

Thus **all 28 necessary primal types are excluded, and the entire (3,2) profile is impossible**. Combining this with 1 ≤ k,l ≤ 3 and the exclusions of (3,3) and (2,3) gives

    k+l ≤ 4.

The surviving necessary list is (1,1), (1,2), (1,3), (2,1), (2,2), (3,1), without any realization claim. In particular this is not exclusion of every generic rank-three case. The numerical bounds remain generic SF ≥ 3, positive-square rank ≥ 27, and generic total section count four or five.

[P3]: https://github.com/Akilleez-QA/read-em-and-weep/blob/dfbdd9f5e18e0a2506d2ea30b01f58f6b21f570b/research/hm/order-four-quadratic-load/RANK-THREE-GAUSS-PLATEAUS-HAVE-LENGTH-AT-MOST-FOUR.md

[P4N]: https://github.com/Akilleez-QA/read-em-and-weep/blob/15adb8e5ea61f07e87df6a0044b7375e580fe7f3/research/hm/order-four-quadratic-load/THREE-P4-QUADRATIC-TYPES-EXCLUDED-BY-BACKWARD-GAUSS.md
[P4Z]: https://github.com/Akilleez-QA/read-em-and-weep/blob/15adb8e5ea61f07e87df6a0044b7375e580fe7f3/research/hm/order-four-quadratic-load/P4-ZERO-PAIRING-EXCLUDED-BY-BACKWARD-PERSISTENCE.md

[P4D]: https://github.com/Akilleez-QA/read-em-and-weep/blob/bdc66692b5814b65e568615639cd86a2b0cd5d0c/research/hm/order-four-quadratic-load/THREE-DOUBLE-P4-TYPES-EXCLUDED-BY-BACKWARD-GAUSS.md

[D5S]: https://github.com/Akilleez-QA/read-em-and-weep/blob/5e1d5ab619dfb2e765232d021be0373d9d2bed19/research/hm/order-four-quadratic-load/SINGLE-D5-TYPE-EXCLUDED-BY-BACKWARD-GAUSS.md
[MD1]: https://github.com/Akilleez-QA/read-em-and-weep/blob/5e1d5ab619dfb2e765232d021be0373d9d2bed19/research/hm/order-four-quadratic-load/MIXED-P4-D5-FORCED-OCTIC-EVALUATION.md
[MD2]: https://github.com/Akilleez-QA/read-em-and-weep/blob/5e1d5ab619dfb2e765232d021be0373d9d2bed19/research/hm/order-four-quadratic-load/FOUR-MIXED-P4-D5-TYPES-EXCLUDED-BY-OCTIC-EVALUATION.md


### Later extremal (3,1) restriction

At the 04:51 UTC cutoff, the separate extremal (3,1) dual cubic image is proved to have rank at most two, and rank one forces O(9) or O(11). The profile itself is not excluded. [Section 16.8](16-canonical-fourth-input-and-complete-test.md#168-unchanged-theorem-and-evidence-boundary) gives the immutable source and unchanged numerical bounds.
