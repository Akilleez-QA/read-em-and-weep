# 5. Separate V51 deformation geometry

This section is a comparison with the independent primary-geometry line attributed in the public discussion to **Mr. Slop**. It is not part of the proof of the adjoint rank theorem. The claims below are summarized from the actual PR634, PR635, PR637–641 and PR644 proofs and reviews, including their pinned inputs; no implication from V51 deformation theory to the remaining adjoint obstruction is asserted.

## 5.1 The marked functors

Work over C with V51 and L₀ = O_V51(1). Consider local Artin C-algebras with residue C, with fixed special-fiber markings. Let F be the polarized pair deformation-class functor and G the abstract deformation-class functor. Their values are isomorphism classes, not groupoids.

The pinned inputs give H⁰(Θ_V51) = 0, h¹(Θ_V51) = 576, h¹(O_V51) = 60, H²(O_V51) = 0, and formal unobstructedness. For sufficiently large m, let n = h⁰(L₀ᵐ). The high-power Hilbert germ is smooth of dimension n² + 635. Its tangent kernel over the pair functor is pgl_n, of dimension n² − 1; forgetting the polarization has the 60-dimensional Picard tangent kernel. Hence dim T_F = 636 and dim T_G = 576.

PR633 supplies an actual smooth pointed étale Hilbert chart carrying an actual relatively ample root L with Lᵐ ≅ O(1). This is the algebraic family in which the slices are cut; it is not an assumed algebraization of an arbitrary formal arc.

## 5.2 Algebraic slices and formal universality

PR634 constructs nested smooth pointed locally closed subschemes

    S_576 ⊂ S_636 ⊂ H′,

by choosing tangent complements and cutting them out with regular functions having the required independent cotangent classes. Their completed bases prorepresent G and F, respectively. Noncanonically, the completed local rings are power-series rings in 576 and 636 variables.

Tangent isomorphism alone is not the argument. Across each small extension with kernel J, the actual lift classes form torsors under H¹(Θ_V51) ⊗ J and H¹(A_L₀) ⊗ J. Marked abstract automorphisms vanish because H⁰(Θ_V51) = 0. Pair automorphisms remain as scalars, but every such scalar lifts, so they do not create a hidden quotient of the lift-class torsor. The classifying map between lift torsors is equivariant for the central Kodaira-Spencer isomorphism. Induction on Artin length then proves existence and uniqueness of the classifying map at every order.

The nested inclusion gives a noncanonical natural section G → F of polarization forgetting. It does not say the polarization is unique: the other 60 Picard directions remain.

## 5.3 Formal symmetry and exact Artin stabilizers

Let Γ = Aut(V51), of order 3000, with normal subgroup U = (Z/5)². PR635 begins with the universal marked abstract functor of PR634, not just its tangent space T = H¹(Θ_V51). Changing the special-fiber marking defines the Γ-action. Averaging a lift of the cotangent space to the maximal ideal of its complete regular local ring produces equivariant formal parameters. The formal inverse function theorem then gives one simultaneous, noncanonical Γ-equivariant identification

    G(A) ≅ T ⊗ m_A

for every local Artin C-algebra A. This is a formal linearization, not an algebraic Γ-stable slice.

Because H⁰(Θ_V51) = 0, reduction of a fixed-base automorphism to its central fiber is injective over every Artin base. Its image is exactly the stabilizer in Γ of the marked class. Lifts of a specified central automorphism, when they exist, are unique; this uniqueness forces the group law. Thus H-fixed abstract classes are precisely deformations carrying the specified H-action. Their functors are represented by smooth linear fixed germs with tangent space Tᴴ.

There are six order-five subgroups H of U. Each abstract fixed germ has dimension 96, any two distinct such germs meet only in the constant germ, and Tᵁ = 0. The reduced formal arrangement of nonidentity fixed germs has codimension 288. On a nonreduced Artin base, however, the points of its scheme-theoretic union need not be the union of the component point sets. Actual automorphism retention is the union of fixed sets, with each automorphism group computed by its stabilizer. Likewise unmarked classes are Artin action-groupoid orbits, not points of the invariant ring. These distinctions are part of the result. [PR635 proof][S635].

## 5.4 Delayed complete symmetry breaking

Choose a tangent vector v with trivial Γ-stabilizer and an integer k ≥ 1. In the simultaneous formal coordinates, take the arc tᵏv. Over A_n = C[t]/(tⁿ⁺¹), its abstract deformation has

    Aut_(A_n)(X_n) = Γ     for n < k,
    Aut_(A_n)(X_n) = {1}   for n ≥ k.

For n ≥ k, the equation tᵏ(γv − v) = 0 forces γv = v, since the coefficient vector is over C and tᵏ is nonzero in A_n. For k ≥ 2 the first-order class is zero, yet all nonidentity central automorphisms fail to extend from the prescribed kth order onward.

The pinned effectivity theorem realizes the compatible system as a projective family over the complete DVR C[[t]]. The finite-jet realization theorem also gives a polarized family on a smooth finite-type curve with the same threshold: matching through order k suffices, because the zero kernels of automorphism reduction propagate triviality to all higher Artin orders even if the later terms differ. Proper formal faithfulness supplies the corresponding fixed-base automorphism conclusion for these families.

This does not assert that the entire chosen arc descends to the finite-type curve, that a geometric generic fiber has trivial automorphism group, or that automorphisms moving the parameter are absent. Nor can a section-loss theorem requiring nonzero first-order variation be applied to the k ≥ 2 construction. [PR635, Sections 4–6][S635].

## 5.5 Compatible equivariant splitting of polarization classes

PR637 extends the formal comparison to the actual forgetful transformation F → G. Preserving the isomorphism class of L₀ is sufficient to define a Γ-action on pair classes: different central line-bundle identifications differ by a constant scalar, which is absorbed by an isomorphism of marked pairs. Their composition discrepancies likewise disappear on classes. This does not provide coherent Γ-actions on the line bundle itself.

Let P = H¹(O_V51), of dimension 60. The equivariant cotangent injection induced by forgetting has an equivariant complement, by finite-group semisimplicity in characteristic zero. Averaged lifts of that complement, together with the images of equivariant parameters for the abstract ring, form a full cotangent basis of the pair ring. The formal inverse function theorem respects the given ring homomorphism, yielding a noncanonical natural Γ-equivariant identification

    F(A) ≅ G(A) × (P ⊗ m_A),

under which forgetting is the first projection. Setting the second coordinate to zero gives an equivariant section. This is a compatible relative splitting, not merely separate linearizations of two unrelated formal germs. No algebraic or convergent equivariant splitting is asserted. [PR637, Sections 1–2][S637].

## 5.6 Six cyclic fixed pair germs and their common polarization directions

The normalization conductor identifies P with sixty difference-of-values fibers at the double points. Its full Γ-action must be treated as a signed permutation representation, because exchanging the two branches changes the difference's sign.

For U, the actual paired-mark action has two orbits of length five in each of six pentads. Their stabilizers have odd order and cannot exchange two branches. Each orbit therefore has trivial stabilizer action on its difference fiber. This proves

    P|U = 12·1 ⊕ 2 Reg₀(U),
    T_F|U = 12·1 ⊕ 26 Reg₀(U),

where Reg₀(U) is the sum of the 24 nontrivial characters. The dimensions are 60 and 636, respectively. The sign issue is resolved for U by the actual branch action, not suppressed by an unsigned-permutation assumption.

For an order-five subgroup H, precisely four nontrivial U-characters are trivial on H. Hence dim Pᴴ = 20 and dim T_Fᴴ = 96 + 20 = 116. The compatible formal splitting makes these dimensions valid for fixed-class germs at every Artin order. Distinct order-five subgroups generate U, so

    Fᴴ ∩ Fᴷ = Fᵁ,
    dim Fᵁ = 12.

Thus the six cyclic fixed pair-class germs have a common twelve-dimensional germ of polarization classes on the constant underlying abstract deformation. After simultaneous linearization, they are a common twelve-dimensional subspace plus six distinct 104-dimensional character sectors. This differs from the abstract germs, whose pairwise intersection is the constant point.

The inversion involution preserves each U-orbit of nodes but exchanges its ordered branches relative to U-transport. It acts as −Id on all twelve U-invariant conductor directions. Therefore P^Γ = 0 and the full Γ-fixed pair-class germ is constant at every Artin order; already U together with inversion suffices. This is a fixed-class assertion, not a linearization of the constant line bundle. [PR637, Sections 3–5][S637].

## 5.7 Fixed classes versus honestly linearized line bundles

For an H-fixed pair class, the underlying scheme has its unique specified H-action, and each pullback of the line bundle is individually isomorphic to it. Chosen isomorphisms may fail the group law by a scalar two-cocycle. The obstruction to an honest H-linearization lies in H²(H,A*), with trivial action on units because the base is fixed and H⁰(O_XA) = A.

The decomposition A* = C* × (1 + m_A), the nilpotent logarithm, and finite-group averaging give

    H²(H,A*) ≅ H²(H,C*).

There is no new infinitesimal obstruction beyond the central one. PR637 leaves the central obstruction open; PR638 computes it for U as a nonzero class of exact order five, as detailed in Section 5.8. PR644 establishes the same exact divisibility criterion for full Γ-linearization in Section 5.11. A Γ-equivariant section of class functors alone still does not supply this result: the fifth-power action requires the separate descent argument.

For cyclic H of order five, H²(H,C*) = C*/(C*)⁵ = 0, so H-fixed pair classes do admit H-linearizations. Without a chosen central linearization they are not canonical, because characters can twist them. Once a central linearization is fixed, the lift is unique up to isomorphism by vanishing of the infinitesimal degree-one and degree-two cohomology. Scalar automorphisms remain; uniqueness of the isomorphism is not asserted. [PR637, Section 6][S637].

## 5.8 The central obstruction is now computed

PR638 computes the previously unresolved U-obstruction from the actual cubic representation. The order-125 Heisenberg cover H has generators g,s with gs = zsg and z = ζ·Id on its five-dimensional module. On the actual complete cubic section space, contained in Sym³(A*), its center acts by ζ⁻³. The same primitive scalar acts on L₀. Thus the lifted generator commutator on L₀ᵐ is ζ⁻³ᵐ. Global units are scalars, so changing the lifts cannot change this commutator. Conversely, when 5 divides m, the existing H-linearization descends to U. Therefore

    L₀ᵐ is U-linearizable if and only if 5 divides m.

The obstruction has exact order five. The reduction isomorphism of Section 5.7 makes this criterion persist over every Artin U-fixed pair class. For divisible m there are 25 central linearization classes, a torsor under Hom(U,C*); a specified central class lifts uniquely up to isomorphism, with scalar automorphisms retained. The original polarization instead admits a compatible H-linearization with its primitive central weight. Cyclic linearizations cannot be combined across independent U-directions. Restriction excludes Γ-linearization when 5 does not divide m. The separate sufficiency proof for Γ is given in Section 5.11, not inferred from this U-calculation. [PR638][S638].

A further consequence is that every nonconstant U-fixed polarized formal arc has generic degree-one section dimension zero or five. The central character forces divisibility by five. Torsion-free global sections over C[[t]] inject after reduction into the ten-dimensional central space. Equality at ten would restore the complete embedding at every Artin order and, by the pinned embedded rigidity theorem, make the marked pair arc constant. Delayed higher-order arcs are included; no nonzero first-order abstract deformation is required.

## 5.9 Actual conductor gluing and the twelve section axes

PR639 realizes both counts by actual algebraic families. Let ν:M→V51 be the normalization and D = ν*L₀. Its sixty double values have two preimages each. Changing their fiber identifications by independent units produces invertible line bundles L_λ with fixed pullback D. The conductor fiber-product description verifies invertibility and base-change compatibility, including over nonreduced parameter rings. A common scalar on D cancels from each ratio, so there is no additional diagonal quotient of the sixty gluing parameters.

Taking one common ratio λ_i on each of the twelve U-orbits gives T₁₂ = (G_m)¹². These are genuine marked polarization classes on the constant scheme V51, with an ample open neighborhood of the identity. The degree-zero gluing factor is U-linearized, but tensoring it with L₀ does not remove L₀'s order-five obstruction. If E_i:S→W_i is evaluation on the ith orbit, then over every C-algebra R,

    H⁰(V_R,L_λ) = ⋂ᵢ ker((1−λ_i)E_i).

Each E_i is surjective onto a five-dimensional irreducible H-module. Its kernel K_i has dimension five and is irreducible. The ten evaluations from one pentad form the actual complete character basis, proving complementarity for that pentad's two kernels. Hence a single active ratio has five sections, while two active ratios in a pentad have none; both counts occur in algebraic polarized families. [PR639][S639].

PR640 proves the stronger result that **all twelve kernels are pairwise complementary**. The actual normalizer acts transitively on the twelve node-orbit labels through PSL₂(F₅). Equality classes of kernels form an invariant block system. An order-five point stabilizer has only its order-ten normalizer and the whole group as proper alternatives for a larger block stabilizer. Thus blocks can only be singletons, the two-element pentad fibers, or the whole twelve-point set. The known complementary pentad pair excludes both nonsingleton cases. Irreducibility then turns distinctness into pairwise complementarity, without assuming a coherent Γ-linearization of L₀.

Writing A(λ) = {i : λ_i ≠ 1}, the exact field-valued classification is

    h⁰(V,L_λ) = 10  if |A(λ)| = 0,
                 5  if |A(λ)| = 1,
                 0  if |A(λ)| ≥ 2.

The reduced positive-section support is precisely twelve coordinate subtori, each isomorphic to G_m, meeting only at the identity. It has pure dimension one and codimension eleven in T₁₂, also after restriction to the ample neighborhood. PR640 determines this **reduced support**; the full nonreduced Fitting scheme is supplied separately by PR641 in Section 5.10. [PR640][S640].

For distinct orbit directions with λ_i = 1+tᵏ and λ_j = 1+tˡ over R_n = C[t]/(tⁿ⁺¹), complementarity identifies the section module with

    (W_i ⊗ Ann_Rn(tᵏ)) ⊕ (W_j ⊗ Ann_Rn(tˡ)).

Its dimension is 5 min(k,n+1) + 5 min(l,n+1). The reduction image in the central ten-dimensional section space has dimension ten before the earlier change, five between the two change orders, and zero from the later order onward. Over C[[t]] it is zero. These exact modules prevent a mistaken inference of base-change equality from the field-valued counts.

## 5.10 Every determinantal section threshold and the embedded identity

Let R = C[λ₁±¹,…,λ₁₂±¹], x_i = 1−λ_i, m = (x₁,…,x₁₂), and J = (x_i x_j : i < j). For the universal conductor-gluing line bundle L on V51 × T₁₂, write p for projection to T₁₂. PR641 fixes the intrinsic convention

    Z_r = V(Fitt_(54+r)(R¹p_*L)),       1 ≤ r ≤ 10.

These are the natural determinantal h⁰ ≥ r schemes. Their exact ideals are

    I(Z_r) = J^(6−r) m^(r−1),          1 ≤ r ≤ 5,
    I(Z_r) = m^(11−r),                6 ≤ r ≤ 10.

The actual normalization cohomology is essential. H⁰(M,D) has dimension ten, H¹(M,D) has dimension five, and all higher groups vanish. The constant normalization complex splits over C; its degree-one free summand has no derived map to the degree-zero conductor target. The normalization sequence therefore gives a two-term free model

    R¹⁰ → R⁶⁰ ⊕ R⁵,       s ↦ ((x_i E_i(s))_i, 0)

for Rp_*L. The five zero rows retain H¹(M,D), rather than silently discarding it. Thus R¹p_*L is the cokernel, h¹ = 55+h⁰ at field points, and the stated Fitting ideal is the ideal of (11−r)-minors. The cokernel model makes its base-change compatibility precise; no arbitrary base-change assertion for H⁰ is used.

The fixed primitive Heisenberg character has a unique five-dimensional irreducible representation E. Hence the ten-dimensional source is E ⊗ C² and each E_i is Id_E ⊗ ℓ_i. Pairwise complementarity makes all two-row determinants of the constant forms ℓ_i nonzero. Reordering identifies the differential's nonzero block with five copies of a 12-by-2 matrix B, whose ith row is x_iℓ_i. Therefore I₁(B) = m and I₂(B) = J. Balanced block minors give the equality of ideals

    I_k = ∑_(2a+b=k, a+b≤5) J^a m^b.

Since J ⊂ m², the term with a = max(0,k−5) contains all the others. Substituting k = 11−r gives every displayed threshold. This establishes the ideals, not merely their radicals. [PR641, Sections 2–4][S641].

In particular Z₁ has ideal J⁵. Along each axis's generic point its local ideal is the fifth power of the eleven-variable transverse maximal ideal, with length binomial(15,11) = 1365. More generally, for r ≤ 5 the generic transverse length of Z_r is binomial(16−r,11).

The identity is an embedded associated point of Z₁. Indeed f = x₁⁴x₂⁴x₃ has degree nine, so f ∉ J⁵, but x_i f ∈ J⁵ for every i. For i = 1,2,3 these products factor as (x₁x₂)⁴(x₁x₃), (x₁x₂)⁴(x₂x₃), and (x₁x₂)³(x₁x₃)(x₂x₃); for i ≥ 4 use (x₁x₂)³(x₁x₃)(x₂x_i). Thus the proper annihilator (J⁵:f) equals m. The witness survives torus localization because each inverted 1−x_i has constant term one. Since the minimal axis primes lie strictly below m, the associated identity is embedded. No complete primary decomposition is asserted. [PR641, Section 5][S641].

The smaller symmetry-reduced matrix B gives V(J), whereas the actual rank-ten section space gives V(J⁵). Their field points agree and their nilpotent structures differ. Neither determinantal scheme is being identified with the functor “there exists a nonzero section” on every Artin algebra; torsion sections require the separate module formulas of Section 5.9.

## 5.11 Full Γ-linearization has exactly the same divisibility criterion

PR644 proves, for every integer m,

    L₀ᵐ is Γ-linearizable if and only if 5 divides m.

Sufficiency uses actual normalization geometry. With M = Bl_Z(P⁴), exceptional divisor E, and H the pullback hyperplane class, the pinned identities D = 3H−E and K_M = −5H+3E give

    D⁵ ≅ ω_M^(−3) ⊗ O_M(4E).

The canonical bundle has its differential-induced Γ-action, and the intrinsically preserved divisor E gives O_M(E) its canonical action. Transporting their tensor action to D⁵ is independent of the chosen ordinary line-bundle isomorphism, since any two such isomorphisms differ by a constant scalar.

To descend this action, the downstairs bundle L₀⁵ and its Γ-invariant class are already specified. Choose individual lifts g*L₀⁵ → L₀⁵. Each pullback can be aligned with the prescribed action on D⁵ by a unique scalar because pullback on global units is C* → C*. The cocycle discrepancy downstairs pulls back to one, so it is one. This proves descent of the action without assuming Pic(V51) → Pic(M) injective or asserting that arbitrary normalization line bundles descend. Tensor powers and duals give sufficiency for every multiple of five; restriction to U gives necessity. The full Γ-obstruction consequently has exact order five. [PR644, Sections 1–3][S644].

The group Γ is perfect. Its quotient SL₂(F₅) is generated by elementary unipotents, all commutators; commutators with any lift of −I exhaust U because they act by u ↦ −2u. Hence Hom(Γ,C*) is trivial. Each admissible fixed line bundle has exactly one Γ-action, and exactly one of its 25 U-linearization classes extends to Γ. Scalar automorphisms still remain, so equivariant isomorphisms are not claimed unique.

For a Γ-fixed marked Artin pair class, logarithm and averaging kill the positive-degree cohomology of 1+m_R. Reduction identifies its scalar obstruction with the central one, and the same divisibility criterion persists. The action on a fixed representative is unique; a chosen central action lifts uniquely up to equivariant isomorphism, with marked scalar automorphisms retained. The full Γ-fixed pair-class germ was already constant by Section 5.6. The new result determines its honest equivariant structures, not new Γ-fixed deformations. [PR644, Sections 4–5][S644].

## 5.12 Scope boundaries

These are results about marked Artin class functors and their symmetries. The pair groupoid is not represented by the pair-class germ; no global unmarked algebraic moduli space or algebraic equivariant slice is constructed. Arbitrary formal arcs need not be algebraic or convergent. Fixed-base symmetry breaking does not classify geometric generic-fiber automorphisms. Fixed pair classes do not erase the central U/Γ line-bundle linearization obstruction.

None of these constructions recovers the original ten sections, identifies these deformations with the original Horrocks-Mumford source, proves the remaining positive Bockstein nonzero, or settles the full-adjoint or Weil-class algebraicity goal. Updating this comparison records the separate published research; it is not a new proof of progress on the adjoint obstruction.

## Exact sources and review status

- [PR634 algebraic-slice proof][S634] and [independent review][R634], commit 895e3a61098f50eccc0a4dc22b58606a28125355.
- [PR635 formal symmetry proof][S635] and [independent review][R635], commit 71e35caf75753046d8508724f33ba463698718ae.
- [PR637 equivariant polarization proof][S637] and [independent review][R637], commit a5fd5de0044a12bc7bb33f3431b1aa7eae7031b6.
- [PR638 central-obstruction proof][S638] and [review][R638]; [PR639 conductor-gluing proof][S639] and [review][R639]; [PR640 kernel-classification proof][S640] and [review][R640]. These are open draft research PRs, not claims that these proofs are merged.
- [PR641 section-jump scheme proof][S641] and [review][R641], commit 1707688f687082e08fb814dec1d6be5c09b2c4d2; [PR644 full-group linearization proof][S644] and [review][R644], commit 91a5d261974239e0887ff9ab488ad43c550348a0. Both are open draft research PRs.
- Public coordination statements: [PR634](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6328234004), [PR635](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6328423942), and [PR637](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6328655884).

Each proof lists immutable earlier geometric and representability inputs. The associated reviews are mathematical reviews conditional on those inputs, not proof-assistant verification. This comparison includes PR641 and PR644 at the pinned versions; later claims are outside its scope.

[S634]: https://github.com/Akilleez-QA/read-em-and-weep/blob/895e3a61098f50eccc0a4dc22b58606a28125355/research/hm/cubic-algebraic-deformation-slices/PROOF.md
[R634]: https://github.com/Akilleez-QA/read-em-and-weep/blob/895e3a61098f50eccc0a4dc22b58606a28125355/research/hm/cubic-algebraic-deformation-slices/REVIEW.md
[S635]: https://github.com/Akilleez-QA/read-em-and-weep/blob/71e35caf75753046d8508724f33ba463698718ae/research/hm/cubic-formal-symmetry-strata/PROOF.md
[R635]: https://github.com/Akilleez-QA/read-em-and-weep/blob/71e35caf75753046d8508724f33ba463698718ae/research/hm/cubic-formal-symmetry-strata/REVIEW.md
[S637]: https://github.com/Akilleez-QA/read-em-and-weep/blob/a5fd5de0044a12bc7bb33f3431b1aa7eae7031b6/research/hm/cubic-equivariant-polarization-splitting/PROOF.md
[R637]: https://github.com/Akilleez-QA/read-em-and-weep/blob/a5fd5de0044a12bc7bb33f3431b1aa7eae7031b6/research/hm/cubic-equivariant-polarization-splitting/REVIEW.md

[S638]: https://github.com/Akilleez-QA/read-em-and-weep/blob/e45aed7546876fcba949918232e7716283dd8f59/research/hm/cubic-linearization-obstruction/PROOF.md
[R638]: https://github.com/Akilleez-QA/read-em-and-weep/blob/e45aed7546876fcba949918232e7716283dd8f59/research/hm/cubic-linearization-obstruction/REVIEW.md

[S639]: https://github.com/Akilleez-QA/read-em-and-weep/blob/7ba345185284c42a385ebe4a3c225ded6d9164d2/research/hm/cubic-conductor-section-strata/PROOF.md
[R639]: https://github.com/Akilleez-QA/read-em-and-weep/blob/7ba345185284c42a385ebe4a3c225ded6d9164d2/research/hm/cubic-conductor-section-strata/REVIEW.md

[S640]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ffef951e71d30b3977f78e91f41a6f77fc075b5d/research/hm/cubic-orbit-kernel-classification/PROOF.md
[R640]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ffef951e71d30b3977f78e91f41a6f77fc075b5d/research/hm/cubic-orbit-kernel-classification/REVIEW.md

[S641]: https://github.com/Akilleez-QA/read-em-and-weep/blob/1707688f687082e08fb814dec1d6be5c09b2c4d2/research/hm/cubic-section-jump-scheme/PROOF.md
[R641]: https://github.com/Akilleez-QA/read-em-and-weep/blob/1707688f687082e08fb814dec1d6be5c09b2c4d2/research/hm/cubic-section-jump-scheme/REVIEW.md
[S644]: https://github.com/Akilleez-QA/read-em-and-weep/blob/91a5d261974239e0887ff9ab488ad43c550348a0/research/hm/cubic-full-group-linearization/PROOF.md
[R644]: https://github.com/Akilleez-QA/read-em-and-weep/blob/91a5d261974239e0887ff9ab488ad43c550348a0/research/hm/cubic-full-group-linearization/REVIEW.md
