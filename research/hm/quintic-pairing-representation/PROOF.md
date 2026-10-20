# A unique finite-normalizer quintic pairing, with its scalar still unresolved

## Result

Let F be the literal normalized Horrocks–Mumford bundle, B=End₀F, M_k=H²(B(k)), and U=M_−5. For the classical finite normalizer N=H₅⋊SL₂(F₅)⊂SL₅, use the equivariant linearization transported from the original monad. Let W be the historical two-dimensional representation χ₂, and W′ its Galois-conjugate representation χ₂′. Then

    M₀ ≅ W′,   U ≅ (W′)* ≅ W′,
    Sym²U* ≅ χ₃′,
    dim Hom_N(S₅, Sym²U*) = 1.

Consequently the trace/Serre quintic pairing

    Φ(p)(u,v) = ⟨u,pv⟩

belongs to one specified one-dimensional vector space. It equals cΨ for a nonzero fixed intertwiner Ψ and an undetermined scalar c. In particular symmetry does NOT force it to be zero, and does NOT prove c≠0. This reduces the actual HM-dependent pairing to one scalar, including the zero possibility.

## 1. Verified representation input

Primary source: G. Horrocks and D. Mumford, A rank 2 vector bundle on P4 with 15,000 symmetries, Topology 12 (1973), 63–81:
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

Use the paper's §§1–2 for N and W; §4, equations (4.2)–(4.6), for the bundle cohomology; Theorem 3.5 for invariant quintics; and its appendix for the irreducible characters. Its bundle is F(3). In our normalization the relevant complete list is

    F(−2): H² = W;
    F(−1): acyclic;
    F:     H¹ = V₃;
    F(1):  H¹ = V₁⊗W′.

All other cohomology of these four twists vanishes. Here V₁ has central character ζ² and V₃=V₁* has central character ζ³. The primary formula (4.6) is especially important: the two-dimensional factor in H¹F(1) is W′, not W. The paper also gives

    V₁⊗V₃ = 1⊕Z,

where Z restricts to the sum of the 24 nontrivial characters of H₅/μ₅, and

    S₅^H₅ = χ₃⊕χ₃′.                              (1)

The locally bound, equivariant Euler coresolution, already proved in ../full-hm-image-symmetry/PROOF.md and independently audited there, is

    K⁻¹ = V₁⊗O(−1),
    K⁰  = V₃⊗Sym²W⊗O,
    K¹  = V*⊗W⊗O(1),
    K²  = W⊗O(2).

It resolves F in degree zero, with no other cohomology sheaves. Its binding to the literal presentation, rather than an unspecified bundle, is in ../hm-presentation-independent/PROOF.md. The known scalar dimension dim M₀=2 is imported from the existing verified End-cohomology calculation, not recomputed here: ../pairing-foundation-inputs/COHOMOLOGY.md, preserved item 6, records the Decker–Schreyer Proposition and the RR derivation of the row (1,24,2,0,0).

## 2. A short spectral-sequence proof of the actual two-dimensional module

Dualize K and tensor with the locally free F. This is a bounded complex quasi-isomorphic to F*⊗F=End F. Its terms, indexed by cochain degree p, are

    p=−2: W*⊗F(−2),
    p=−1: V⊗W*⊗F(−1),
    p= 0: V₁⊗Sym²W*⊗F,
    p= 1: V₃⊗F(1).

Taking the sheaf-cohomology spectral sequence and then H₅ invariants is legitimate: invariants under a finite group over C are exact. The primary cohomology list leaves exactly three nonzero invariant E₁ entries:

    E₁^(−2,2),H = W*⊗W = 1⊕χ₃,
    E₁^( 0,1),H = χ₃,
    E₁^( 1,1),H = W′.                            (2)

These are representations of N/H₅=SL₂(F₅). In the last two calculations, (V₁⊗V₃)^H₅=1 was used. Both W and its symmetric square are self-dual.

The last entry has total degree two. Its sole potentially nonzero incoming differential is d₁ from (0,1). That map is zero because Hom_SL₂(F₅)(χ₃,W′)=0. For r≥2, an incoming d_r would start at (1−r,r); the r=2 source lies in the acyclic p=−1 column, the r=3 source is (−2,3), which is zero, and larger r lie outside the complex. There is no outgoing differential because p=1 is its final column. No other invariant entry has total degree two. Therefore

    H²(End F)^H₅ ≅ W′.

Since the entire H²(End F) has dimension two, it equals this invariant subspace. The trace splitting does not change H², so M₀≅W′. This proof does not need to identify the p=−2 to p=0 differential, the H¹End representation, or any actual HM multiplication map. It is stronger and cleaner than cancellation in a numerical Euler characteristic.

Equivariant Serre duality and the trace identification B*=B give U≅M₀*. There is no hidden determinant character: N⊂SL(V), so H⁴O(−5) is trivial. The primary character table makes W′ a determinant-one, self-dual two-dimensional module. Thus U≅W′.

## 3. Multiplicity one of the quintic trace map

The perfect trace/Serre pairing is symmetric under exchanging its two degree-two cohomology inputs. Polynomial multiplication is self-adjoint. Hence Φ indeed has values in Sym²U*, not Λ²U*. All operations used to define it are N-natural.

Because H₅ acts trivially on U, an equivariant map from S₅ to Sym²U* factors uniquely through the Reynolds projection

    R_H(p)= |H₅|⁻¹ Σ_(h∈H₅) h·p ∈ S₅^H₅.

The subgroup is normal, so this projection is N-equivariant. By the character table,

    Sym²(W′)=χ₃′.

Combining with (1) gives

    Hom_N(S₅,Sym²U*)
      ≅ Hom_SL₂(F₅)(χ₃⊕χ₃′,χ₃′)
      ≅ C.                                        (3)

Choose once a nonzero isomorphism from the χ₃′ summand to Sym²U*, and compose with its isotypic projection and R_H to obtain Ψ. Its scale is arbitrary; the statement Φ=cΨ is independent of that choice. If c≠0, Φ is surjective and its restriction to S₅^H has kernel exactly the χ₃ summand. If c=0, S₅U=0 by perfect pairing U×M₀. Thus c=0 means exactly failure of the bottom degree to reach the top via quintics.

One can also dualize Ψ: its image is the unique χ₃′ summand of (S₅^H)*. Calling this a unique net is legitimate only as a dual linear-system statement with the chosen identifications; it does not establish the actual pairing's nonvanishing.

## 4. Exact consequence for the cofactor map after lowest multiplication

Use the separately established lowest-degree multiplication isomorphism (../lowest-degree-generation/PROOF.md)

    μ:S₁⊗U → M_−4.

This assumption is used only in this section; (2)–(3) do not depend on it. Let x_s, s=1,…,5, be a basis of S₁, and let j_r, r=1,…,5, be the actual quartic conductor cofactors. Let α:M_−4→M₀^⊕5 have r-th component multiplication by j_r. Under M₀≅U* via trace/Serre duality, define

    A_Ψ:S₁⊗U → (U*)^⊕5,
    (A_Ψ(x_s⊗v))_r(u)=Ψ(x_s j_r)(u,v).

Associativity and adjointness give the exact identity

    α μ = c A_Ψ.                                  (4)

Therefore

    rank α = 0 if c=0,
    rank α = rank A_Ψ if c≠0.

The map A_Ψ is determined by the finite representation-theoretic intertwiner, the coordinate identification, and the specified conductor cofactors; it has no remaining HM multiplication coefficients beyond the scalar c. Equation (4) is a dependency reduction, not a new evaluation of A_Ψ or its rank. In particular neither its invertibility nor its singularity is asserted.

Lowest-degree generation alone does not imply S₅U=M₀: intermediate multiplication can fail to propagate. Thus μ being an isomorphism cannot be used to eliminate c=0. Conversely multiplicity one does not force c=0, because the permitted Hom space is nonzero. An independently justified nonzero value, or another structural propagation theorem, remains necessary to settle that scalar.

## Scope

Only primary-source reading, existing proof reading, finite representation theory, and a bounded spectral-sequence argument were used. No HM matrix, multiplication rank, cofactor instance, point, jet, source representative, or obstruction value was evaluated. No continuous SL₂(C) action on the HM bundle is assumed; all equivariance here is for the finite group N and its quotient SL₂(F₅). Local proof-file writes only.
