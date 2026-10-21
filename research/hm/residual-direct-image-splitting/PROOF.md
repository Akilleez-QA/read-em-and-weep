# Splitting the residual derived direct image

Status: authored structural proof; independently mathematically reviewed in REVIEW.md, not formally checked. Work over C. No selected actual HM/source instance or numerical rank is evaluated.

## 1. Dependencies and statement

Use the notation and actual-scheme identifications of:

- [PR577](https://github.com/Akilleez-QA/read-em-and-weep/pull/577), commit **563fc7036faa4965e55bda3bec5b82ae5360fa6c**, `research/hm/residual-fibration-defect/PROOF.md`;
- [PR572](https://github.com/Akilleez-QA/read-em-and-weep/pull/572), commit **a20545dcc4c0e26dc1bb8af17852db63696ec7b1**, `research/hm/residual-canonical-decic/PROOF.md`;
- [PR574](https://github.com/Akilleez-QA/read-em-and-weep/pull/574), commit **3c92fdc469f6870520e7a9d905b5ab9199a5bf37**, `research/hm/primary-conductor/PROOF.md`.

Thus ν:X→S is the finite normalization of the actual primary surface, π:X→B=P¹ its modular elliptic fibration, h:B→Γ the normalization of the integral six-nodal canonical decic, and g:S→Γ satisfies gν=hπ. Set N=R¹π_*O_X≅O_B(-5). The conductor quotient T=ν_*O_X/O_S is the sum of thirty residue fields. Set Q=h_*O_B/O_Γ and K=coker(Q→g_*T), with the canonical injection of PR577. Each stalk K_q at a node q of Γ is annihilated by the maximal ideal and has dimension four; length(K)=24.

We prove that the extension left open in PR577 splits:

    R¹g_*O_S ≅ K ⊕ h_*O_B(-5).

More strongly, in the bounded derived category of coherent O_Γ-modules,

    Rg_*O_S ≅ O_Γ ⊕ K[-1] ⊕ h_*O_B(-5)[-1].             (1)

All shifts are cohomological: a sheaf F[-1] has its only cohomology in degree one. These are existence statements for splittings, not assertions of canonical complementary summands or of multiplicative/formal-algebra splittings. The canonical torsion subsheaf remains K.

## 2. The point-restriction factorization

Let W⊂X be the reduced union of the sixty preimages of the thirty double points of S. At each double point, the normalization quotient is the difference of the residues on its two branches. Consequently the sheaf map defining that quotient factors as

    ν_*O_X → ν_*O_W → T.                                (2)

The last arrow is the difference of the two residues at each pair. This is a global factorization, not merely a description of the induced map on degree-zero direct images. It follows either directly from the conductor ideal upstairs, which is the reduced ideal of W, or by gluing the residue-difference descriptions at the thirty disjoint supports. Any choices of signs in residue coordinates leave this factorization unchanged intrinsically.

Write A=Rπ_*O_X. PR577 gives H⁰(A)=O_B, H¹(A)=N and no other cohomology. Its truncation triangle is

    O_B → A → N[-1] → O_B[1].

Since B is a smooth projective curve and N is invertible,

    Ext²_B(N,O_B)=H²(B,N^∨)=0.

Hence A≅O_B⊕N[-1], compatibly with the displayed truncation. The restriction morphism A→π_*O_W obtained from O_X→O_W has zero component on N[-1], because

    Hom_{D(B)}(N[-1],π_*O_W)
      = Ext¹_B(N,π_*O_W)
      = H¹(B,N^∨⊗π_*O_W)=0.                            (3)

Here π_*O_W is a finite-support coherent sheaf and has no positive cohomology. Also Rπ_*O_W=π_*O_W, since W is finite. No flatness of g is used.

The exact functor h_* preserves this vanishing. Applying derived direct image to (2), using gν=hπ and the exactness of finite direct images, therefore shows that

    h_*A → g_*T

has zero component on h_*N[-1]. Importantly, this conclusion uses the factorization over the smooth normalization B. It does not assert that Ext¹_Γ(h_*N,g_*T) vanishes on the singular curve Γ.

## 3. Splitting off the elliptic summand

The normalization sequence gives a distinguished triangle

    Rg_*O_S → h_*A → g_*T → Rg_*O_S[1].

By Section 2 its middle arrow, under A≅O_B⊕N[-1], is (d,0), where d:h_*O_B→g_*T is the residue-difference morphism of PR577. Let C be the two-term complex

    C = [h_*O_B --d--> g_*T],

placed in degrees zero and one. Taking a cone of (d,0) and shifting by minus one gives an isomorphism

    Rg_*O_S ≅ C ⊕ h_*N[-1].                             (4)

This is the elementary cone decomposition for a morphism that is zero on one direct summand; existence suffices, so no functorial choice of cones or null-homotopies is being asserted.

PR577 identifies ker(d)=O_Γ and coker(d)=K. Taking degree-one cohomology in (4) proves

    R¹g_*O_S ≅ K ⊕ h_*N.

In particular the specific extension class of PR577 in Ext¹_Γ(h_*N,K) is zero. This conclusion does not require that the entire ambient Ext group vanish. The torsion summand K is intrinsically determined; we do not select a canonical section of the quotient map onto h_*N.

## 4. Splitting the remaining Postnikov extension

The only cohomology of C is H⁰(C)=O_Γ and H¹(C)=K. Its truncation triangle is

    O_Γ → C → K[-1] → O_Γ[1].

Its obstruction to splitting belongs to Ext²_Γ(K,O_Γ). We check global, not just stalkwise, vanishing.

The nodal curve Γ is Gorenstein of pure dimension one. Every local ring O_{Γ,q} has injective dimension at most one as a module over itself. Thus the coherent sheaves of local Ext satisfy

    sheaf-Ext^j_Γ(K,O_Γ)=0 for j≥2.

The sheaf sheaf-Ext¹_Γ(K,O_Γ) has finite support, so its H¹ is zero. In the local-to-global Ext spectral sequence

    H^p(Γ,sheaf-Ext^q_Γ(K,O_Γ)) ⇒ Ext^{p+q}_Γ(K,O_Γ),

all terms of total degree two vanish: q≥2 vanishes by the local Gorenstein property, p=q=1 vanishes by finite support, and p=2,q=0 vanishes by the dimension of Γ. Therefore

    Ext²_Γ(K,O_Γ)=0.                                    (5)

This argument applies to K even though a skyscraper at a node need not be perfect. Equivalently, coherent duality with the invertible dualizing sheaf ω_Γ gives Ext²_Γ(K,O_Γ)=Ext²_Γ(K⊗ω_Γ,ω_Γ)=H^{-1}(Γ,K⊗ω_Γ)^∨=0.

The truncation triangle splits, giving C≅O_Γ⊕K[-1]. Combined with (4), this proves (1).

## 5. Consequences and scope

This resolves a missing structural dependency in PR577: the length-24 defect does not form a nontrivial extension of the normalization's elliptic H¹ contribution. Both the sheaf extension and the remaining derived Postnikov extension vanish for different reasons: point restriction on B kills the former, while one-dimensional Gorenstein duality on Γ kills the latter.

The ambiguity of the sheaf splitting can be measured exactly. Put B'=h_*O_B(-5). The set of sections of R¹g_*O_S→B' is a nonempty torsor under Hom_Γ(B',K): the difference of two sections factors uniquely through K, and adding any such homomorphism to a section gives another section. At each node q, K_q≅k(q)^4 is annihilated by m_q, while B'_q/m_qB'_q has dimension two. Indeed, after completion the normalization is C[[s]]⊕C[[t]], the pushed-forward line bundle is free of rank one on each branch, and reduction by m_q=(s,t) leaves one residue coordinate on each branch. Therefore

    Hom_{O_{Γ,q}}(B'_q,K_q)
      = Hom_{k(q)}(B'_q/m_qB'_q,K_q)

has dimension eight. Since K is supported at the six nodes, these local Hom spaces are independent and exhaust the global Hom space. Consequently the space of sheaf splittings is an affine torsor of dimension **48** over C. This quantifies the choice of complementary summand; it does not assert that no additional geometric structure could distinguish a choice.

As a consistency check, applying derived global sections gives

    h¹(S,O_S)=h¹(Γ,O_Γ)+length(K)+h⁰(B,O_B(-5))
             =6+24+0=30,
    h²(S,O_S)=h¹(B,O_B(-5))=4.

These numerical values already occur in PR574 and are not claimed as new results.

This theorem is about Rg_*O_S as a complex of O_Γ-modules. It does not assert a splitting of the dualizing complex on the non-Cohen–Macaulay surface S or on the mixed-dimensional incidence scheme; the nonsplitting results of PR576 concern different objects on different spaces. Nor does (1) establish flatness, a flat cohomology-and-base-change theorem, a multiplicative splitting, or any first-order, higher-order, or algebraicity statement for an HM deformation. No selected evaluation or large computation is involved.
