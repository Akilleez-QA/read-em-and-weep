# Canonical residue trace and its nonsplit thirty-point extension

Status: authored structural proof, independently mathematically reviewed in REVIEW.md; not formally checked. Work over C. No selected HM/source evaluation is performed.

## 1. Dependencies and notation

Use the actual primary surface S, normalization ν:X→S, modular elliptic fibration π:X→B=P¹, canonical six-nodal decic Γ, normalization h:B→Γ, and residual morphism g:S→Γ with gν=hπ. Exact dependencies are:

- PR574, commit 3c92fdc469f6870520e7a9d905b5ab9199a5bf37, `research/hm/primary-conductor/PROOF.md`: 0→O_S→ν_*O_X→T→0 with thirty reduced length-one conductor quotients; K_S has cohomology ν_*ω_X in degree −2 and T^D in degree −1, where T^D is the finite dual of T.
- PR577, commit 563fc7036faa4965e55bda3bec5b82ae5360fa6c, `research/hm/residual-fibration-defect/PROOF.md`: g_*O_S=O_Γ, N=R¹π_*O_X=O_B(−5), and the actual difference map d:h_*O_B→V:=g_*T factors through Q:=h_*O_B/O_Γ by an injection ι:Q→V. At each of the six nodes, Q is one-dimensional and V is five-dimensional; after consistently orienting the two normalization branches, ι is the diagonal map. Its cokernel K has length 24, four at each node.
- PR579, commit 78746b35576c319dd6100c2ec6d4f628100b2200, `research/hm/residual-direct-image-splitting/PROOF.md`: Rg_*O_S≅O_Γ⊕K[−1]⊕h_*N[−1] as modules, noncanonically. In particular the actual conductor map factors through restrictions to sixty points on X; its component on the elliptic N[−1] summand vanishes before pushing along h.

For a finite-support sheaf F on Γ write F^D=Ext¹_Γ(F,ω_Γ), the sheaf of Ext, canonically its finite dual. Finite duality identifies V^D=g_*T^D. Write K_S for the absolute dualizing complex normalized so a smooth surface has ω[2]. All shifts are cohomological.

We prove a canonical description of E:=H^{−1}(Rg_*K_S), including the actual trace E→ω_Γ. In fact the actual five-to-one grouping of the conductor points supplies a canonical averaged trace splitting E≅ω_Γ⊕K^D. Nevertheless its different natural thirty-point residue extension is nonsplit at every node.

## 2. Derived duality and cohomology

Proper duality gives

    Rg_*K_S ≅ RHom_Γ(Rg_*O_S,ω_Γ[1]).                 (1)

The trace in (1) is dual to the actual unit O_Γ→Rg_*O_S. Finite duality for h gives

    RHom_Γ(h_*N,ω_Γ) ≅ h_*(N^∨⊗ω_B)=h_*O_B(3).

There are no positive sheaf Ext here: N is invertible on smooth B, and finite duality identifies h^!ω_Γ with ω_B. Likewise RHom_Γ(K,ω_Γ)=K^D[−1]. Dualizing PR579's module splitting yields

    Rg_*K_S ≅ h_*O_B(3)[2] ⊕ (ω_Γ⊕K^D)[1].         (2)

The full derived splitting in (2) is initially an existence statement. Section 4 will distinguish a canonical splitting of the trace in degree −1 using the actual conductor components; it does not select a canonical full derived splitting. In particular

    H^{−2}(Rg_*K_S)=h_*O_B(3),
    E≅ω_Γ⊕K^D,
    H^j(Rg_*K_S)=0 for j≠−2,−1.

The trace induces a canonical exact sequence

    0→K^D→E→ω_Γ→0.                                  (3)

For completeness, this also follows directly by dualizing the canonical truncation O_Γ→Rg_*O_S→(R¹g_*O_S)[−1]. The only sheaf Ext¹ of R¹g_*O_S is K^D, since its torsion-free quotient h_*N has no positive sheaf Ext against ω_Γ. Higher sheaf Ext against ω_Γ vanish on the Gorenstein curve. Thus the trace kernel in (3) is intrinsic. Sequence (3) splits globally, either by (2) compatibly with truncation or because Ext¹_Γ(ω_Γ,K^D)=H¹(Γ,ω_Γ^{-1}⊗K^D)=0. The set of all its splittings is a torsor under Hom_Γ(ω_Γ,K^D), a vector space of dimension 24. Section 4 constructs a distinguished splitting from the actual conductor decomposition; thus the existence of other splittings does not prevent this geometry from selecting one canonically.

## 3. The canonical thirty-residue extension

Dualizing the surface normalization sequence gives the triangle

    T^D → ν_*ω_X[2] → K_S → T^D[1].                 (4)

The elliptic canonical bundle formula and projection formula give

    π_*ω_X=O_B(3),      R¹π_*ω_X=O_B(−2)=ω_B.

Applying Rg_* to (4), and taking cohomology in degrees −2 and −1, therefore gives the canonical exact sequence

    0→h_*ω_B→E→V^D→0.                               (5)

The left-hand inclusion uses the actual relative trace of π. It must not be replaced by an arbitrary complement in (2).

Dualizing the curve normalization sequence gives

    0→h_*ω_B→ω_Γ --res--> Q^D→0.                    (6)

This is the usual nodal residue sequence. Intrinsically its last arrow is the dual of O_Γ→h_*O_B→Q; choosing an orientation of the two branches identifies it with one branch residue of a dualizing differential, whose other branch residue is its negative.

Dualizing 0→Q --ι-->V→K→0 gives

    0→K^D→V^D --ι^D-->Q^D→0.                       (7)

The actual extension (5) is the pullback of (6) along ι^D. Consequently there is a canonical isomorphism, respecting both inclusions and both quotient maps,

    E ≅ ω_Γ ×_{Q^D} V^D.                            (8)

Here is a derived justification that keeps track of the extension class. In the dual of the actual normalization triangle, the extension class of (5) is obtained by projecting Rg_*ν_*ω_X[2] to its degree −1 cohomology h_*ω_B[1]. Under proper and finite duality, that projection is dual to the natural degree-zero inclusion h_*O_B→h_*Rπ_*O_X. The resulting morphism is precisely d:h_*O_B→V. Since d=ι∘(h_*O_B→Q), functoriality of duality identifies the class with the pullback of (6). This uses the actual map and its factorization, not just the dimensions of the sheaves. It also follows by dualizing the two-term complex [h_*O_B→V] in PR579; the split elliptic summand contributes only in degree −2 and does not alter this degree −1 extension.

The trace E→ω_Γ in (3) is the first projection in (8). Thus the twenty-four-dimensional defect consists exactly of the surface residues with zero total residue over each base node.

## 4. Canonical averaging, local form and a genuine nonsplitting

The sheaf T is canonically the direct sum of its thirty separate point-support summands. Over each base node q, write V_q=⊕_{z∈g^{-1}(q)∩Supp(T)}V_z. There are five such summands, each one-dimensional, and the component ι_z:Q_q→V_z of the actual injection ι is an isomorphism. Define

    r_q:V_q→Q_q,       r_q((v_z))=(1/5)Σ_z ι_z^{-1}(v_z).

This is independent of any ordering, basis or branch orientation, and r_qι=id. These maps glue across the six disjoint supports to a canonical retraction r:V→Q. Therefore V=ι(Q)⊕ker(r) canonically, with ker(r) canonically isomorphic to K via the quotient. Dualizing supplies a canonical section r^D:Q^D→V^D of ι^D. Formula (8) now gives the distinguished trace section

    ω_Γ→E,       η↦(η,r^D(res η)).

Consequently (3) is canonically split using the actual grouping of conductor points, and E=ω_Γ⊕K^D canonically with respect to this structure. This is stronger than an abstract existence of a splitting. It makes no canonical choice of the separate elliptic complement in R¹g_*O_S from PR579.


Fix a node q of Γ. Complete and choose orientations of its two branches. Put

    R=C[[s,t]]/(st),     Rbar=C[[s]]⊕C[[t]].

A generator η of ω_R can be represented by (ds/s,−dt/t). Under the finite-duality embedding, h_*ω_B consists of the regular branch differentials. In these coordinates it is m_R η⊂Rη, with m_R=(s,t). Thus (6) is

    0→m_R η→Rη→C→0,

where the last map takes the coefficient of η modulo m_R. Consistent orientation of the five surface normalization differences makes ι diagonal, so ι^D is the sum map C^5→C. Formula (8) becomes

    E_q^∧ = { (fη,(r_1,...,r_5)) : f mod m_R=Σ_j r_j }.
                                                               (9)

In particular its torsion submodule is exactly

    { (0,(r_j)) : Σ_j r_j=0 } ≅ C^4.                (10)

Indeed ω_R is torsion-free, while the displayed kernel is killed by m_R. Choosing any vector e∈C^5 with Σe_j=1 gives an R-linear splitting fη↦(fη,(f mod m_R)e) of the trace. The canonical averaged section is e=(1/5,...,1/5) in the consistently oriented coordinates. Hence E_q^∧≅R⊕C^4, in agreement with (2).

Nevertheless the natural sequence (5) is NOT split at q. If a section C^5→E_q^∧ of its residue quotient existed, its image would be killed by m_R and hence lie in the torsion C^4 of (10). Its composite with E_q^∧→C^5 therefore lies in the proper sum-zero subspace; it cannot be the identity. Equivalently the extension is the nonzero nodal normalization-residue class in the single sum direction, together with four split residue directions. Faithful flatness of completion shows the algebraic stalk extension is likewise nonsplit.

This proves nonsplitting at all six nodes, and therefore globally. It does not contradict (3), whose quotient is ω_Γ rather than V^D, or the derived module decomposition (2). The precise natural filtration, not the isomorphism class of its middle sheaf alone, carries this obstruction.

## 5. Contribution and limits

The result identifies the actual dual trace and the missing compatibility between the primary surface's thirty local conductor residues and the residual curve's six nodal residues. Exactly one sum direction at each base node carries the nonsplit canonical-residue extension; the other four directions form the intrinsic length-24 trace kernel. The five actual component isomorphisms select a canonical averaged trace splitting, although the extension with quotient all thirty residues remains nonsplit. Thus the numerical defect 30−6=24 is realized by a canonical map and an explicitly nonsplit extension, rather than by an arbitrary vector-space decomposition.

This is a statement about proper duality and canonical residue maps of the actual primary residual morphism. It is not a claim that g is flat, that K_S itself splits, that a multiplicative splitting exists, or that the full-adjoint twenty-dimensional boundary is invertible. First-order repair, prescribed-source evaluation, higher lifting and algebraicity are not established. No selected matrix, coefficient, rank or source instance is evaluated.
