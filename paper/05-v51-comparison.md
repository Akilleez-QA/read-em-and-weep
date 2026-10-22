# 5. Separate V51 deformation geometry

This section is a comparison with the independent primary-geometry line attributed in the public discussion to **Mr. Slop**. It is not part of the proof of the adjoint rank theorem. The claims below are summarized from the actual PR634, PR635, PR637, PR638, PR639 and PR640 proofs and reviews, including their pinned inputs; no implication from V51 deformation theory to the remaining adjoint obstruction is asserted.

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

There is no new infinitesimal obstruction beyond the central one. PR637 leaves the central obstruction open; PR638 now computes it for U as a nonzero class of exact order five, as detailed in Section 5.8. Sufficiency for full Γ-linearization remains unresolved. Consequently a Γ-equivariant section of class functors does not by itself choose honestly Γ-linearized line bundles.

For cyclic H of order five, H²(H,C*) = C*/(C*)⁵ = 0, so H-fixed pair classes do admit H-linearizations. Without a chosen central linearization they are not canonical, because characters can twist them. Once a central linearization is fixed, the lift is unique up to isomorphism by vanishing of the infinitesimal degree-one and degree-two cohomology. Scalar automorphisms remain; uniqueness of the isomorphism is not asserted. [PR637, Section 6][S637].

## 5.8 The central obstruction is now computed

PR638 computes the previously unresolved U-obstruction from the actual cubic representation. The order-125 Heisenberg cover H has generators g,s with gs = zsg and z = ζ·Id on its five-dimensional module. On the actual complete cubic section space, contained in Sym³(A*), its center acts by ζ⁻³. The same primitive scalar acts on L₀. Thus the lifted generator commutator on L₀ᵐ is ζ⁻³ᵐ. Global units are scalars, so changing the lifts cannot change this commutator. Conversely, when 5 divides m, the existing H-linearization descends to U. Therefore

    L₀ᵐ is U-linearizable if and only if 5 divides m.

The obstruction has exact order five. The reduction isomorphism of Section 5.7 makes this criterion persist over every Artin U-fixed pair class. For divisible m there are 25 central linearization classes, a torsor under Hom(U,C*); a specified central class lifts uniquely up to isomorphism, with scalar automorphisms retained. The original polarization instead admits a compatible H-linearization with its primitive central weight. Cyclic linearizations cannot be combined across independent U-directions. Restriction excludes Γ-linearization when 5 does not divide m, but sufficiency for Γ is not established. [PR638][S638].

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

The reduced positive-section support is precisely twelve coordinate subtori, each isomorphic to G_m, meeting only at the identity. It has pure dimension one and codimension eleven in T₁₂, also after restriction to the ample neighborhood. This determines the **reduced support**, not the full nonreduced determinantal or Fitting jump scheme. [PR640][S640].

For distinct orbit directions with λ_i = 1+tᵏ and λ_j = 1+tˡ over R_n = C[t]/(tⁿ⁺¹), complementarity identifies the section module with

    (W_i ⊗ Ann_Rn(tᵏ)) ⊕ (W_j ⊗ Ann_Rn(tˡ)).

Its dimension is 5 min(k,n+1) + 5 min(l,n+1). The reduction image in the central ten-dimensional section space has dimension ten before the earlier change, five between the two change orders, and zero from the later order onward. Over C[[t]] it is zero. These exact modules prevent a mistaken inference of base-change equality from the field-valued counts.

## 5.10 Scope boundaries

These are results about marked Artin class functors and their symmetries. The pair groupoid is not represented by the pair-class germ; no global unmarked algebraic moduli space or algebraic equivariant slice is constructed. Arbitrary formal arcs need not be algebraic or convergent. Fixed-base symmetry breaking does not classify geometric generic-fiber automorphisms. Fixed pair classes do not erase the central U/Γ line-bundle linearization obstruction.

None of these constructions recovers the original ten sections, identifies these deformations with the original Horrocks-Mumford source, proves the remaining positive Bockstein nonzero, or settles the full-adjoint or Weil-class algebraicity goal. Updating this comparison records the separate published research; it is not a new proof of progress on the adjoint obstruction.

## Exact sources and review status

- [PR634 algebraic-slice proof][S634] and [independent review][R634], commit 895e3a61098f50eccc0a4dc22b58606a28125355.
- [PR635 formal symmetry proof][S635] and [independent review][R635], commit 71e35caf75753046d8508724f33ba463698718ae.
- [PR637 equivariant polarization proof][S637] and [independent review][R637], commit a5fd5de0044a12bc7bb33f3431b1aa7eae7031b6.
- [PR638 central-obstruction proof][S638] and [review][R638]; [PR639 conductor-gluing proof][S639] and [review][R639]; [PR640 kernel-classification proof][S640] and [review][R640]. These are open draft research PRs, not claims that these proofs are merged.
- Public coordination statements: [PR634](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6328234004), [PR635](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6328423942), and [PR637](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6328655884).

Each proof lists immutable earlier geometric and representability inputs. The associated reviews are mathematical reviews conditional on those inputs, not proof-assistant verification. This comparison is checked through PR640 at the pinned versions; later claims are outside its scope.

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
