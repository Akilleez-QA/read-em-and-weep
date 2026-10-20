# Hom-complex derivative relations and unique transgression

Prerequisite excerpt: original Sections 1–4 only. The reversal and Massey consequences are outside this excerpt.

## 1. Inputs and conventions

Use the independent [literal presentation](../hm-presentation-independent/PROOF.md), which resolves the locally free rank-two classical HM bundle H:

    K⁻¹=5O(−1), K⁰=15O, K¹=10O(1), K²=2O(2).

Its differential d is homogeneous linear in the fixed coordinates v₀,…,v₄, and d²=0. The endomorphism Hom complex has internal degree-r term ⊕ₜ Hom(Kᵗ,Kᵗ⁺ʳ), differential ∂f=df−(−1)ʳfd. Twisting by O(−w) gives sums of O(r−w). Composition adds internal degrees and twists, with the usual Hom differential Leibniz sign. There is no additional sign on composition of the global degree-one maps used below.

The [primary Decker–Schreyer proposition](../hm_primary_source_verification.md) gives h¹(End H(−1))=5 and h¹(End H(t))=0 for t≤−2. Stability, Serre duality and Riemann–Roch give the audited rows

    Hʲ(End H(−1)): (0,5,10,0,0),
    Hʲ(End H(−2)): (0,0,20,0,0).

See [independent cohomology reduction](../pairing-foundation-inputs/COHOMOLOGY.md), items 4–6. These are imported mathematical theorems, not ranks recomputed from a finite model.

## 2. Five derivative classes and their products

Put D_i=∂d/∂v_i. Differentiation here means formal extraction of the coefficient of v_i in a specified linear differential. Thus D_i is a global degree-one element of Hom(K,K(−1)), with constant coefficient blocks. Differentiating the identity d²=0 once and twice gives

    dD_i+D_i d=0,
    D_iD_j+D_jD_i=0.

In particular each D_i is closed and D_i²=0 in characteristic zero. The twist is essential: a constant map from CₜO(t) to Cₜ₊₁O(t+1) becomes a global constant coefficient map only after the target is twisted by O(−1).

All higher cohomology of the individual terms of Hom(K,K(−1)) vanishes: its line-bundle degrees range from −4 to 2, and on P⁴ only degrees at most −5 have top cohomology. Hence its global-section complex computes hypercohomology. Its global degree-zero term is zero. The presentation's diagonal entries γ_{Z_i,i}=v_i show that the same coefficient position in D_j is δ_{ij}. Thus the five closed maps D_i are linearly independent even before passing to cohomology, and there are no degree-zero global boundaries. The primary dimension five proves that their classes form a basis of U₁. This basis is canonical relative to the fixed coordinate system and literal presentation, not coordinate-free without those choices.

To show all products vanish, work first over C with twisted Dolbeault forms. Since H¹(O(−1))=0, each class of U₁ has a trace-free representative. For trace-free rank-two endomorphisms A,B, polarized Cayley–Hamilton gives AB+BA=tr(AB)Id. Applied to two degree-one forms α,β, exchanging their scalar forms contributes a minus sign, so

    αβ−βα=tr(αβ)Id.

This identity takes values in End H(−2). Because H²(O(−2))=0, it yields ab=ba in H²(End H(−2)). On the other hand the strict derivative identity gives [D_i][D_j]=−[D_j][D_i]. Their products therefore vanish. Bilinearity and the derivative basis prove ordered vanishing for every pair in U₁.

This is a rank-two trace argument plus formal linearity of d, not an appeal to a smooth global family. The comparison of Dolbeault products with algebraic Yoneda products is standard; faithful flatness descends the resulting algebraic vanishing from C to Q, then base change proves it for the stipulated data over any characteristic-zero field.

## 3. The unique transgression

Use the hypercohomology spectral sequence

    E₁^{r,q}=H^q(P⁴,Homʳ(K,K(−2))) ⇒ H^{r+q}(P⁴,End H(−2)).

Here −3≤r≤3, and the line degree is r−2. Besides q=0, the sole nonzero slot is

    E₁^{−3,4}=H⁴(Hom(K²,K⁻¹(−2)))=H⁴(10O(−5)),

of dimension ten. It has total degree one. No d₁ leaves it within q=4, because the next line degree is −4. Since d_s has bidegree (s,1−s), its only possible later differential is

    d₅:E₅^{−3,4} → E₅^{2,0}=H²(ΓHom(K,K(−2))).

There are no incoming differentials into its source, and no earlier higher-row differential into its target. Since total H¹(End H(−2)) is zero, d₅ is injective. Since the only associated-graded contribution to total degree two is (2,0), the edge map gives the exact sequence

    0 → H⁴(10O(−5)) → H²(ΓHom(K,K(−2)))
      → H²(End H(−2)) → 0.

Thus the middle dimension is 30. The global internal degree-one term consists of O(−1)'s and is zero. Consequently the middle space is literally the kernel of the global differential from degree two to degree three: no global degree-one boundaries need to be divided out. Its elements are constant degree-two maps.

## 4. Identification of the ten relations

For a<b let P_ab=D_aD_b, with composition meaning D_b first, then D_a. These are globally closed constant degree-two maps. Section 2 shows their hypercohomology classes vanish, so they belong to the ten-dimensional kernel in Section 3. We now prove their independence by an exterior-coefficient argument.

The C₀→C₂ block of D_aD_b is r_aδ_b, where r_a is the coefficient of v_a in the final evaluation row and δ_b is the coefficient of v_b in contraction. For an oriented bivector pair (p,q), the literal contraction column is

    D_pq(v)=v_p e_q*−v_q e_p*.

Its coefficient δ_b is δ_bp e_q*−δ_bq e_p*, and evaluation by r_a gives

    δ_bp δ_aq−δ_bq δ_ap.

Therefore on this column, ∑_{a<b}c_ab r_aδ_b equals the negative of the oriented coefficient c_pq, with the convention c_qp=−c_pq. The first output row on the U_i columns isolates the five pairs (i+2,i+3); the second output row on the V_i columns isolates the five pairs (i+1,i+4). The first list consists of all adjacent unordered pairs in the cyclic five-set; the second consists of all remaining pairs. Their union is the ten-element basis of Λ²k⁵. The displayed order only changes the sign of an isolated coefficient and never mixes coefficients. Thus every c_ab must vanish if the cochain sum is zero.

This proves that the ten P_ab form an independent subspace of the ten-dimensional edge kernel. Hence

    im(d₅)=span{D_aD_b:a<b} ≅ Λ²U₁.

The last isomorphism uses the canonical derivative lift U₁→global degree-one cocycles relative to the fixed complex. No assertion is made that a preferred basis of H⁴(10O(−5)) maps to these particular ordered products with a specified normalization. Equality of subspaces, rather than a computed transgression matrix, is the result.

