# Alternative proof of exceptional fiber cohomology

The dimension theorem and relative support conclusion are already proved in [the exceptional-surface result in PR116](https://github.com/Akilleez-QA/read-em-and-weep/blob/e906fb83ca5ae4f5c75e7ca7a61863b984f15a0d/research/hm/null-factor-surfaces/exceptional-surface-0514/RESULT.md). The following complete alternative derivation uses codimension-two extension of Hom maps; it is not a new dimension theorem. Its relative rank and base-change conclusions agree with [the relative Chern constraints](https://github.com/Akilleez-QA/read-em-and-weep/blob/01c96a7e1b24685eacd5d1dc52ed0ea026490146/research/hm/relative-models/relative-chern-constraints/PROOF.md).

## Statement

Work over the complex numbers. Let C be a smooth elliptic curve with a degree-two map π:C→P¹, let σ:P¹×P¹→Sym²(P¹)=P² be the symmetric quotient, and put p=σ∘(π×π):C²→P², of degree eight. Thus C² denotes a product of elliptic curves, not the affine plane. Use the natural two deck involutions and the geometric factor swap, with the ordinary product linearization on the cover algebra. These are the cover and linearization of [the factor-surface proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/e906fb83ca5ae4f5c75e7ca7a61863b984f15a0d/research/hm/null-factor-surfaces/relative-surface-0502/RESULT.md) and [its deck addendum](https://github.com/Akilleez-QA/read-em-and-weep/blob/e906fb83ca5ae4f5c75e7ca7a61863b984f15a0d/research/hm/null-factor-surfaces/relative-surface-0502/DECK_ADDENDUM.md). Let E be an unstable restriction of normalized HM to any plane, and let G_b=End₀(p*E). A line twist does not change this coefficient bundle. Then

    (h⁰(G_b), h¹(G_b), h²(G_b)) = (4, 128, 4).

In the fiber deck-character order (++),(−+),(+−),(−−), the h¹ dimensions are

    (31, 33, 33, 31).

The both-odd swap-odd sector, which is the fiber coefficient sector selected by the retained permutation sign, has

    (h⁰, h¹, h²) = (0, 15, 3).

On stable planes this same sector has dimensions (0,12,0). Thus every exceptional plane produces an exact jump of three in both its retained-sector h¹ and h² dimensions. This is a fiber-cohomology statement; it is not a calculation of an actual source obstruction, a torsion length, a scheme-theoretic multiplicity, or the dimension of global obstruction classes.

## 0. Exact finite pushforward and relative setup

Each elliptic double cover has π_*O_C=O⊕O(−2). The symmetric quotient has σ_*O=O⊕O(−1), with invariant and anti-invariant summands respectively. Projection formula gives σ_*O(−2,−2)=O(−2)⊕O(−3).

For the mixed term, identify the universal quadratic divisor Δ⊂P¹×P² with P¹×P¹, by remembering a chosen root and its residual root. Its divisor sequence, twisted by O(−2,0), is

    0 → O(−4,−1) → O(−2,0) → O_Δ(−2,0) → 0.

Push to P². Vanishing of both H⁰ groups on P¹ gives

    0 → σ_*O(−2,0) → O(−1)^3 → O → 0.

By P¹ duality the last arrow consists of the three coefficients of the universal quadratic, hence is the Euler-sequence map. Thus the kernel is Ω¹_P²; symmetry treats O(0,−2). This proves the actual bundle decomposition, with the deck order (++),(−+),(+−),(−−),

    p_*O_(C²) = (O⊕O(−1)) ⊕ Ω¹ ⊕ Ω¹ ⊕ (O(−2)⊕O(−3)).

For the relative conclusion in Section 6, let B=C² be the other pair of elliptic factors, let r:C⁴=C²×B→B be projection, and let f:C⁴→Sym⁴(P¹)=P⁴ be divisor addition after the four double covers. Assume the coefficient bundle is F=N⊗f*HM for a line bundle N, with the stated natural equivariance on End(F). For b∈B, the remaining two P¹ points define a nonzero quadratic h, the fiber map lands in the plane P(h·Sym² V), and F_b is a line twist of p*E_h. The good locus consists of stable E_h. The cited factor-surface proof shows that it is nonempty and dense: the plane-family image has Plücker degree nine, whereas Boralevi's irreducible unstable surface has degree twenty-five. These premises are not an identification of a different coefficient object from numerical data alone.

The finite pushforward derivation is also recorded in [the public localization statement](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6260145920).

## 1. The two unstable resolution types imply a uniform section sequence

Boralevi, Corollary 2.2, https://arxiv.org/pdf/math/0602002v2, gives exactly two unstable normalized-plane resolution types, (5)(0,3,3) and (4,5)(0,3,3,4). Either gives h⁰(E)=1 and h⁰(E(−1))=0 directly. Indeed h⁰(E(t)) for t≤1 is obtained from the displayed generators, since H¹ of any line bundle on P² is zero. In particular h⁰(E(1))=3 and h⁰(E(t))=0 for t<0.

The unique section has no divisorial zeros: a positive-degree divisorial zero would yield a section of E(−d), d≥1, contradicting the preceding vanishing. As E is locally free of rank two on the smooth surface, its nonempty zero scheme Z is zero-dimensional lci, with length c₂(E)=4. Consequently

    0 → O → E → I_Z(−1) → 0.                         (1)

This conclusion includes the special unstable stratum. No coordinates or entries of a HM monad are used.

## 2. Negative endomorphisms and the untwisted algebra

For every integer t, codimension-two extension across Z gives

    Hom(I_Z(−1), E(t)) = H⁰(E(t+1)).                  (2)

One way to verify this is to restrict a homomorphism to P²\Z, where I_Z is O, then extend the resulting section of the locally free bundle E(t+1) across codimension two. The extension is unique and gives the original homomorphism after multiplication by I_Z.

For t<0, every map E→E(t) annihilates the unique section O→E, since H⁰(E(t))=0. Hence (1) and (2) identify Hom(E,E(t)) with H⁰(E(t+1)). For t=0, any endomorphism acts by a scalar on the one-dimensional H⁰(E); subtracting that scalar identity makes it annihilate O. Therefore

    h⁰ End(E)       = 1 + h⁰(E(1)) = 4,
    h⁰ End(E)(−1)  = h⁰(E) = 1,
    h⁰ End(E)(−j)  = 0, j≥2.                        (3)

The kernel of End(E)→End(H⁰(E)) is the three-dimensional space in (2) at t=0. Since each element factors through E→I_Z(−1) and has image in the section O (all H⁰(E(1)) come from H⁰(O(1))), it is square-zero and tracefree. Thus these three elements are exactly H⁰ End₀(E).

## 3. The mixed summands do not acquire exceptional H⁰ or H²

Tensor the Euler sequence with End E:

    0 → End E tensor Ω¹ → End E(−1)^3 → End E → 0.   (4)

Let u be a nonzero generator of H⁰ End E(−1). The map on H⁰ sends a triple of constants to (a₀x₀+a₁x₁+a₂x₂)u. This is injective: a nonzero polynomial times a nonzero section of a locally free sheaf on integral P² cannot vanish. Therefore H⁰(End E tensor Ω¹)=0. By the self-duality of End E, Serre duality, and T_P²(−3)=Ω¹_P², its H² also vanishes. Its Euler characteristic is

    3 chi(End E(−1)) − chi(End E) = −34,

so h¹(End E tensor Ω¹)=34 even on the unstable locus.

## 4. Complete cohomology and scalar subtraction

Riemann–Roch and c₁(E)=−1,c₂(E)=4 give chi(End E(t))=2t²+6t−11. Serre duality gives h²(End E(t))=h⁰(End E(−t−3)). From (3), the triples (h⁰,h¹,h²) are

    End E:       (4,15,0)
    End E(−1):   (1,16,0)
    End E(−2):   (0,16,1)
    End E(−3):   (0,15,4)
    End E⊗Ω¹:    (0,34,0).

Use the exact finite pushforward in Section 0. Before removing scalar endomorphisms, the four deck sectors are respectively End E⊗(O⊕O(−1)), End E⊗Ω¹, End E⊗Ω¹, and End E⊗(O(−2)⊕O(−3)). The scalar O_{C²} contributes H⁰=1 in (++), H¹=1 in each mixed sector, and H²=1 in (−−). Trace splitting is canonical in characteristic zero. Subtraction gives

    deck (++):  (4,31,0)
    deck (−+):  (0,33,0)
    deck (+−):  (0,33,0)
    deck (−−):  (0,31,4).

Summing gives (4,128,4), and chi=−120 as a check.

## 5. The retained swap-odd exceptional jump

Under the natural factor swap, the both-odd deck generator product is even. Thus sigma_*O(−2,−2)=O(−2)_+⊕O(−3)_−. The both-odd swap-even triple is (0,16,1), and the swap-odd End contribution is (0,15,4). The scalar H²(O(−3)) has this same odd swap character and dimension one. The tracefree odd-sector triple is therefore (0,15,3).

This sign also matches Serre duality upstairs: a nonzero two-form on C² is odd under swapping its two elliptic factors and odd under each individual deck involution. Thus the three (++), swap-even tracefree H⁰ classes pair with the three (−−), swap-odd H² classes; the remaining (++), swap-odd H⁰ class pairs with (−−), swap-even H². No unexplained Koszul sign is inserted in the algebra pushforward.

## 6. Precise useful consequence and limits

Let T denote the both-odd swap-odd summand of R²r_*End₀(F) on the whole base B. Coherent top-degree base change for this relative surface identifies T⊗k(b) with the corresponding H² on the fiber: the higher R³ vanishes, so the top-degree base-change map is an isomorphism. Consequently its set-theoretic support is exactly the inverse image of the unstable-plane locus, and its fiber dimension is exactly three at every point of that locus. In particular, if the exceptional set is nonempty, this retained-sector R² sheaf is nonzero; exceptional support is not merely a hypothetical place where something might survive.

The good-locus W is the corresponding rank-12 R¹ eigensubbundle. At exceptional points the fiber cohomology dimension is 15. Do not identify that number with the fiber dimension of a globally extended R¹ sheaf without checking its base-change map. Likewise, the dimension-three top cohomology does not determine the length or annihilator of T, nor does it assert a rank-three vector bundle on a reduced exceptional locus. If the exceptional locus is finite, T is a finite-length nonzero sheaf when nonempty, but its length remains undetermined.

This theorem does not establish nonvanishing of any specified global retained class. A nonzero top direct-image sheaf can interact with Leray differentials and need not be hit by any of the thirty specified source directions. Base-deck, base-swap, and pair-exchange requirements remain separate. No statement here locates the exceptional set or proves it nonempty.
