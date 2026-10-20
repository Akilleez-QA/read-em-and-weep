# Translation KS classes are graded-central: the proposed annihilator gives no detector reduction

## Result and scope

Under the accepted background-family hypotheses, let X=C^4, Y=(P^1)^4, q:X→Y the fixed product of elliptic double covers, N the fixed line bundle, and F the pullback of the accepted HM bundle to Y by the coefficient map. The background family is

    E_s = N ⊗ q^* τ_s^* F,

where τ_s is the factorwise translation z_i↦z_i+s_i on Y. Let W be its four-dimensional KS image. Then

    ab = (−1)^m ba  for every a∈W and b∈Ext^m_X(E,E).

Consequently P_W=span{ab+ba:a∈W,b∈Ext^1(E,E)} is ZERO. The source-family membership [R]∈P_W^⊥ therefore gives no restriction on [R], globally or on the authenticated full-sign detector sector. This does not compute [R], its class, any detector, or the dimension of an Ext group. This argument itself does not settle a mixed second-star lifting problem.

The proof uses the fixed covering's eigensheaves as modules, not an action on its branched algebra. No translation of X, moving branch locus, or automorphism of q_*O_X as an algebra is asserted.

## 1. Fixed covering decomposition

Let G=(Z/2)^4. Since q is finite flat in characteristic zero,

    q_*O_X = ⊕_{S⊂{1,2,3,4}} L_S,
    L_S = ⊠_i M_i,  M_i=O_{P1}(−2) if i∈S, O_{P1} otherwise.

For one elliptic double cover q_i:C→P1, trace splits q_{i*}O_C=O⊕M, with M an odd line bundle. Finite pushforward preserves Euler characteristic, so 0=χ(O_C)=χ(O)+χ(M)=1+(deg M+1). Hence deg M=−2 and M≅O(−2). Taking external products proves the decomposition above. This uses only genus one, degree two, and characteristic zero.

The character of L_S is the product of the sign characters indexed by S. End cancels the line factor N, and finite pushforward with the projection formula gives

    Ext^m_X(E_s,E_s)_S
      = H^m(Y, End(τ_s^*F) ⊗ L_S).

The same identification works relatively over any dual-number tangent A=k[ε]/ε². It commutes with reduction to the central fiber. One can replace F by its accepted bounded locally free complex throughout; End then means the derived End complex, giving identical statements.

Each L_S has a translation linearization. Indeed O(−2) can be identified with the canonical line of P1, whose pullback under an automorphism is canonically its canonical line by the derivative; O has its usual linearization. Take their external tensor product. If a particular identification of the fixed cover eigensheaf with these lines is chosen, transport this linearization through it. It reduces to identity at s=0. No compatibility with products L_S⊗L_T→q_*O_X is required.

## 2. Every Ext class extends over every background tangent

Fix a tangent c and let τ_A be translation z_i↦z_i+εc_i, an automorphism of Y_A reducing to identity. Write F_A=τ_A^*(F⊗A). Linearization gives

    End(F_A)⊗(L_S⊗A)
      ≅ τ_A^*((End(F)⊗L_S)⊗A).

Pullback by the A-automorphism τ_A induces an isomorphism of derived global sections with that of the unpulled sheaf. Base extension over k is flat; for example a finite affine Cech complex proves

    RΓ(Y_A, End(F_A)⊗L_S,A)
      ≅ RΓ(Y, End(F)⊗L_S) ⊗_k A.

These isomorphisms reduce to identity on the central fiber. Therefore reduction from relative H^m to central H^m is surjective for every m and every S. Using the fixed finite q and the projection formula, this is precisely surjectivity

    H^m(X_A,End(E_A)) → H^m(X,End(E)).

It concerns the actual background bundle E_A on the fixed X_A. It is not only a statement about an unrelated translated cover. In particular every b∈Ext^m(E,E) has an extension as an End(E_A) cohomology class.

## 3. The connecting map is the KS graded commutator

The exact sequence of sheaves on the fixed X

    0 → End(E) --ε--> End(E_A) → End(E) → 0

has connecting homomorphism

    ∂_a: Ext^m(E,E) → Ext^{m+1}(E,E),
    ∂_a(b) = ab − (−1)^m ba,

up to a uniform convention sign which does not affect vanishing. This is the standard obstruction to deforming an endomorphism/cohomology class together with a deforming bundle. Here it also follows directly in the fixed-term accepted resolution: if d_A=d+εα, with α representing the KS class a, the End differential changes by

    D_A(u)=D(u)+ε(αu−(−1)^|u|uα).

In a total Cech model this is the same graded commutator with the Koszul signs. Taking a central cocycle and any lift computes the connecting homomorphism by this formula. The exact sequence and the surjectivity proved in §2 give ∂_a=0. Thus W is graded-central on all Ext groups. For m=1 the displayed expression is ab+ba, proving P_W=0.

This does not assert a multiplicative trivialization of the relative Ext algebra. Multiplication in the cover algebra depends on its branch equations, which the module comparison need not preserve. The connecting-map argument only needs extensions of individual classes; it does not need algebra compatibility of the auxiliary comparison.

## 4. Full-sign hypercohomology filtration and the apparent route

For the full-sign character, L_all=K_Y=O(−2,−2,−2,−2). The accepted End complex has degrees r=−3,...,3 with terms sums of O(r,r,r,r), hence its full-sign pushforward terms are sums of O(r−2,r−2,r−2,r−2). Kunneth on (P1)^4 gives exactly:

- r≤0: only q=4 can be nonzero;
- r=1: all sheaf cohomology vanishes;
- r≥2: only q=0 can be nonzero.

In E1^(r,q)=H^q(End^r⊗K_Y), the only total-degree-one position is (−3,4). After the row differential, its only possible outgoing higher differential is d5:(−3,4)→(2,0). Thus Ext^1_full-sign has just the surviving (−3,4) filtration piece, namely the kernel of this d5 on E2 (the intermediate pages have no possible nonzero differentials).

The potential total-degree-two pieces are (−2,4) and (2,0). Explicitly their associated-graded terms are ker[d5:E2^(−2,4)→E2^(3,0)] and coker[d5:E2^(−3,4)→E2^(2,0)], respectively. No degeneration or splitting of the resulting filtration is assumed.

A background KS cocycle is a deck-invariant global internal-degree-one variation. Its polarized action on the leading full-sign Ext^1 representative appears to send (−3,4) to (−2,4). Filtration data alone cannot rule out a secondary contribution to (2,0) if this leading contribution becomes a boundary. The all-character extension argument above proves that the TOTAL polarized class vanishes. It kills both the leading route and any secondary correction, without evaluating either map or asserting an unproved spectral-sequence degeneration.

## 5. Serre character bookkeeping

The deck representation on H^4(O_X) is full-sign: each elliptic H^1(O_C) is odd. Consequently the Serre product of an S-character Ext^2 class with a T-character Ext^2 class can contribute to the trace only if S△T is the full set. Choosing a volume form identifies this target line with k but does not make that identification deck-equivariant.

In particular a FULL-SIGN obstruction component pairs with INVARIANT Ext^2 classes, not with full-sign Ext^2 classes. Since W is invariant, only invariant b could furnish the corresponding P_W tests. Showing only P_W's full-sign part zero would therefore not suffice by itself to exclude constraints on a full-sign obstruction. The proof above establishes vanishing for every character, including the required invariant one, so it resolves this issue.

The authenticated 32-dimensional/30-retained detector labels do not enter this proof. Without their precise interpretation one must not identify any named scalar functional with a particular Yoneda product. Since P_W=0, there are no nonzero Yoneda-product functionals of this prescribed kind to identify or eliminate.

## Geometric prerequisite and comparison scope

The only model-specific prerequisite for Sections 1–3 is [the fixed-polarization coefficient family, PR179](https://github.com/Akilleez-QA/read-em-and-weep/blob/2b03992b32d2f5cf0509b6f4840adf08369f54b7/research/hm/cubic-loci/foundation-p01/COEFFICIENT-FAMILY.md), with its exact presentation hypothesis. The mixed-source identities are not prerequisites for centrality. The present proof supplies its own fixed-cover eigensheaf decomposition.

The translation family is the subfamily of the published full coefficient family obtained from the four binary factors (b_i T+(a_i+s_i b_i)U). It has the same fixed line bundle N and fixed carrier X. Its tangent map into the projectivized coefficient parameter space is injective: if its derivative is a scalar multiple λv, then δv₀=0 and v₀=1 force λ=0; δv₁=Σc_i=0 and δv₂=(Σc_i)e₁−Σc_i z_i=0 then force every c_i=0 by algebraic independence of the z_i. The published coefficient-family KS injectivity therefore gives four independent translation classes. This is a restriction of the existing 79-dimensional theorem, not an additional four-dimensional contribution. The all-degree centrality theorem does not require the rank of this image.

The source-family endpoint calculation in the companion mixed-residual note is a distinct representative-level derivation, not a premise of this theorem. The established ordinary invariant-product vanishing is also not used: that theorem concerns two invariant degree-one inputs, whereas Sections 1–3 concern every Ext degree and every deck character. All multiplication-sensitive limitations above remain in force.

No source or detector value is evaluated. Any independent mixed-vanishing theorem under additional source/target premises is outside the scope of this argument; historical statements of an open problem are not a claim that later work has not resolved a particular case.

## 6. Explicit degree-one endpoint primitive in the inherited row convention

Choose a regular family Cech cocycle b(ε) representing an extension of b∈Ext^1(E,E), on a fixed affine refinement over the dual numbers. Such a representative exists by §2 and affine acyclicity; its reduction can be used as the chosen representative of b. Use the source row convention T_ij(M)=G_ij^−1 M G_ij and a_ij=G_ij^−1 dot g_ij. Then

    b_ik=b_ij+T_ij b_jk,
    a_ik=a_ij+T_ij a_jk,
    (δ dot b)_ijk=a_ij(T_ij b_jk)−(T_ij b_jk)a_ij.

Set h_ij=b_ij a_ij. Expanding its differential in matrix order gives

    (δh)_ijk=−b_ij(T_ij a_jk)−(T_ij b_jk)a_ij.

Therefore the regular degree-one cochain B=dot b−h satisfies

    δB=a cup b+b cup a.

This is an explicit representative-level nullhomotopy for every generator of P_W. It does not set either individual product to zero. All family frame variations are included in dot b, just as in the inherited mixed-class endpoint argument.
