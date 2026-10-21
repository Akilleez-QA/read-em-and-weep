# Exact quartic-generator jumps on the twelve-point orbit

## Inputs and conventions

Work over C. Use the original module H and the actual normalizer action throughout. Set W=W′=H_0, P=P(W), and S=Sym(T). Write V=T*, E=A*, U=Sym²(W0), U′=Sym²(W), and Qspin=Sym³(W)=Sym³(W0). The normalizer representations and their chosen extensions are the original ones, not representations inferred from dimensions. Let Γ be the finite Heisenberg group and let G=N/Γ be the binary icosahedral quotient of the finite normalizer N. Since V is an actual N-representation extending the relevant Γ-irreducible, Hom_Γ(V, F) carries the genuine G-action (n·h)(v)=n h(n⁻¹v). The action of Γ on this Hom space is trivial. Thus removing V below gives genuine G-equivariant bundles, not merely projective multiplicity spaces.

Pinned inputs:
- [PR519, commit cf328c6b0d05551a52911a3a4ba420c68f6fcc6f](https://github.com/Akilleez-QA/read-em-and-weep/blob/cf328c6b0d05551a52911a3a4ba420c68f6fcc6f/research/hm/gorenstein-flat-family/PROOF.md): actual relation bundles, binary derivative identifications, and multiplication map f.
- [PR520, commit c56173aab6e9e5d7be2f2f638d6f953c9d7f93b1](https://github.com/Akilleez-QA/read-em-and-weep/blob/c56173aab6e9e5d7be2f2f638d6f953c9d7f93b1/research/hm/quartic-jump-divisors/PROOF.md): invariant-divisor argument and unique size-twelve orbit Ω.
- [PR516, commit 89b66cbede7513c4f196fdbda0ee3bb77c53d2e0](https://github.com/Akilleez-QA/read-em-and-weep/blob/89b66cbede7513c4f196fdbda0ee3bb77c53d2e0/research/hm/gorenstein-resolution/PROOF.md): degree-three generation of T_w/I, full lower surjectivity, and the Gorenstein resolution template.
- [PR522, commit d91279f87d7b69297a0419630f6beee4d4497705](https://github.com/Akilleez-QA/read-em-and-weep/blob/d91279f87d7b69297a0419630f6beee4d4497705/research/hm/quartic-rank-exclusion/PROOF.md): a(w)≤10 uniformly.
- [PR489, commit 5637cdd610fc2ec8ffbbbbfc7627b2d6c54f6873](https://github.com/Akilleez-QA/read-em-and-weep/blob/5637cdd610fc2ec8ffbbbbfc7627b2d6c54f6873/research/hm/scalar-quartic-generators/PROOF.md): I_4/(T I_3)=V⊗U.
- [PR494, commit 72ab9a7524aef8c9d1c1fd989f8b0e83826dc916](https://github.com/Akilleez-QA/read-em-and-weep/blob/72ab9a7524aef8c9d1c1fd989f8b0e83826dc916/research/hm/higher-symmetric-powers/PROOF.md): actual multiplication S_2=E⊗Sym²W and N_1=T⊗Sym²W, N_2=E⊗Sym⁴W, N=Sym²_S H.

All tensor rules below are those of the binary icosahedral quotient in Horrocks–Mumford (1973), Sections 2–3 and appendix:
T⊗E*=V⊗(U′⊕W0), W0⊗W=T4,
U′⊗W=W⊕Qspin, U⊗Qspin=W0⊕Qspin⊕R6,
Sym^d W=1,W,U′,Qspin,J5,R6,U⊕T4 for d=0,...,6.
Public source: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf .

## 1. Equivariant block decomposition

The extensions used in PR519 split as ordinary bundles because the relevant H¹(O(1)) and H¹(O(3)) vanish. Their splittings can be averaged over the finite normalizer, producing equivariant splittings. The determinant form on W is invariant. After removing the genuine normalizer representation V, the quartic map becomes

φ:(Qspin⊕W⊕T4)⊗O(−3) → U⊗O ⊕ W⊗O(−1).

The upper block has coefficient representation U⊗Sym³W=U⊗Qspin. Thus it vanishes on W and T4, and is a morphism

A:Qspin⊗O(−3)→U⊗O.

The lower block has coefficient representation W⊗Sym²W=W⊕Qspin, so it vanishes on T4. Write its remaining blocks B on Qspin and C on W. Consequently

φ = [[A,0,0],[B,C,0]].

These vanishing statements follow from inequivalent irreducibles, not from a dimension count. In particular there is no ambiguity caused by a graph between the two target summands: Hom_equivariant(W⊗O(−1),U⊗O)=Hom(W,U⊗W)=0, since U⊗W=R6.

## 2. The upper block is everywhere surjective

A is nonzero, since otherwise rank φ≤2 and a≥15, contradicting PR522. Let r be its generic rank. Its maximal-minor divisor is invariant and has degree at most 3r≤9; hence the divisor is empty by PR520. Its rank is therefore constant.

Suppose r=1. Its image is an equivariant line subbundle K=O(−d) of U⊗O with 0≤d≤3: nonpositive degree follows from the inclusion, and K(3) is globally generated as a quotient of Qspin⊗O. Dualizing the inclusion gives a nonzero equivariant map U*→H⁰(O(d))=Sym^d(W*). Since U is irreducible, this is injective. No d≤3 contains U, a contradiction.

Suppose r=2. Let K=im A and let its line quotient be (U⊗O)/K=O(d). We have 0≤d≤6 because K(3) is globally generated. Its quotient map gives a nonzero equivariant map U→Sym^d(W*), hence an injection. The displayed symmetric-power list forces d=6. Now K(3) is a rank-two globally generated bundle of degree zero on P¹, hence is trivial. Its global sections form a two-dimensional representation Z, and the surjection Qspin⊗O→K(3) gives a surjective intertwiner Qspin→Z. This is impossible because Qspin is irreducible of dimension four.

The line-bundle linearizations used here differ from the standard ones only by characters, and the binary icosahedral group is perfect, so there is no character twist to add. Thus r=3, and

0→O(−12)→Qspin⊗O(−3) --A--> U⊗O→0.

The kernel's linearization is the standard O(−12), again because there are no nontrivial characters.

## 3. The lower W block is universally nonzero and rank one

This block can be determined from the actual binary multiplication, independently of the unknown upper scalar. Dualize the map J_3/I_3→J_4/I_4 after multiplication by T. Under the derivative descriptions in PR519 it is induced by binary product differentiation

D(gh)(λ)=g(λ)D h(λ)+h(λ)D g(λ),

where g and h are binary quadratics. Since h(λ)=λ(Dh(λ))/2, its binary component is the map F_λ:W→(Sym²W)*⊗W characterized by

F_λ(v)(g)=g(λ)v+(λ(v)/2)Dg(λ).

More explicitly, the actual dual lower map has source (J_4/I_4)*=T⊗W⊗O(1) and target T*⊗E⊗W⊗O(3). It is obtained by currying the actual multiplication μ:T⊗T→Sym²T=E⊗Sym²W and then applying the displayed derivative product rule. The currying is nonzero, and its symmetric channel is the unique U′ channel; the alternating W0 channel vanishes. Thus this formula gives the actual lower map on the U′⊗W source summand up to a common nonzero normalization. The W0 summand is the alternating projection and contributes zero, in agreement with Section 1.

For completeness, compute the W projection as a universal two-dimensional tensor identity, not a selected source-instance evaluation. Choose any symplectic basis x,y of W and put λ=x*. In dual monomial coordinates,

F_λ(x)=2(x²)*⊗x+(xy)*⊗y/2,
F_λ(y)=(x²)*⊗y.

The symplectic identification (Sym²W)*≅Sym²W takes (x²)* to y², (xy)* to −2xy, and (y²)* to x². Therefore

F_λ(x)=2y²⊗x−xy⊗y,
F_λ(y)=y²⊗y.

Apply the standard contraction c:Sym²W⊗W→W normalized by c(y²,x)=−2y, c(xy,y)=y, and c(y²,y)=0. It gives

cF_λ(x)=−5y, cF_λ(y)=0.

The coefficient is nonzero in characteristic zero. Equivariance under the full binary change of coordinates makes this a universal identity for every nonzero λ. Hence the original block C:W⊗O(−3)→W⊗O(−1) is nonzero and has rank one at every point. Equivalently, the unique equivariant quadratic matrix on W is a nonzero scalar multiple of w⊗λ_w; its trace and determinant vanish. Its kernel and image are

ker C=O(−4), im C=O(−2),

and (W⊗O(−1))/im C=O.

## 4. The sole remaining map

Since A is onto, the cokernel of φ is the cokernel of its lower map restricted to ker A⊕W⊗O(−3). Modulo im C this is precisely the cokernel of a morphism

s:O(−12)→O.

It is equivariant, so s is an invariant binary form of degree twelve. We now prove that it is nonzero; multiplicity one alone would not suffice.

## 5. Structural nonvanishing of the residual invariant

Suppose s=0. Then coker φ is the equivariant line bundle O. This follows already from the construction as Q/im C, where Q=W⊗O(−1); its degree is zero, and its linearization must be trivial because G has no nontrivial characters.

The equivariant quotient map

π:U⊗O ⊕ W⊗O(−1)→O

has zero upper component: Hom_G(U,1)=0. Hence it factors as a nonzero morphism π_Q:Q→O after projection onto the lower target. But PR516, as explicitly used in PR522, proves that the full actual lower composite φ→Q is surjective as a bundle map: the ideal T_w/I is generated in degree three for every w. Therefore π_Q cannot vanish after composition with φ. This contradicts πφ=0.

Thus s≠0. Its zero divisor is an invariant effective divisor of degree twelve. By PR520 it is exactly the reduced orbit Ω. Consequently

a(w)=0 for [w] outside Ω, and a(w)=5 for [w] in Ω.

The multiplicity cokernel is an invertible sheaf on Ω, isomorphic as an ordinary sheaf to O_Ω, and has length twelve. An equivariant trivialization on Ω is not asserted. Restoring the V factor gives original cokernel length sixty. Cokernel commutes with restriction to each fiber by right-exactness of tensor product, so the fiber statements remain valid at the twelve zeros despite nonflatness of this torsion cokernel.

This determines the actual quartic-generator pattern, rather than merely listing alternatives. Every G_w has twenty cubic minimal generators; it has no quartic minimal generators off Ω and exactly five on Ω. The remaining middle Betti parameter b from PR516 is not determined by this argument.

## Scope

This is authored structural mathematics, with independent and root mathematical review recorded separately, conditional on the pinned inputs. It has not been formally checked by a proof assistant. It uses no selected actual HM/source evaluation, numerical rank experiment, coefficient search or large computation. The only explicit calculation is a universal binary product-rule and contraction identity. It does not resolve the original fixed scalar-pair residual, higher-order lifting or algebraicity questions.
