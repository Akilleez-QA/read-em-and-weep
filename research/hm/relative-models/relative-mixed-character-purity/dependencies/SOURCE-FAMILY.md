> Publication scope: Uniform family purity, not a new central parity ledger; conditional actual-source identities remain explicit. Source-stage audit/checker references describe historical evidence, not fresh execution or bundled executable artifacts. Named source identities are hypotheses unless separately proved below.

# Joint projective source family, closed residual, and the central twelve directions

## Result and evidence level

Work in characteristic zero with X=C^4, C:y²=z³−z, Y=(P¹)^4, q:X→Y, the binary-product map σ:Y→P⁴, and N=⊠O_C(O). Let H denote the cohomology bundle of the specified homogeneous complex. Fix the roots, their legal frames, and the physical vector fields on X.

The SAME homogeneous raw-source recipe extends regularly over an identity neighborhood of

    E_(φ,g)=N⊗(g∘σ∘φ∘q)*H,
    (φ,g)∈(PGL₂)^4×PGL₅.

Its disjoint mixed residual R_(φ,g) is closed on the actual common family cover. This assertion is conditional on the inherited identification of the pinned source with the homogeneous split-frame, determinant-normalized and raw-residual recipes stated in FIRST-LIFT-STRUCTURAL, and its rational-denotation conventions. We do not reauthenticate the underlying production source. For global contraction and primitive regularity one may use PR79's global-cover theorem, retaining its explicit imported exact A-receipt premise. The determinant-one normalization is an additional inherited input, not a consequence of PR79's A identity alone.

The construction below authenticates changes of target affine chart and square-line trivialization by an explicit homogeneous-weight calculation. It is not a substitution into an unchanged v₀=1 formula. Thus no further family-specific chart compatibility premise is needed once those inherited homogeneous-source identifications are admitted.

For every tangent a in the joint KS image, the resulting actual mixed class obeys

    a[R]−[R]a=0 in Ext³_X(E,E).

Assuming the separately audited KS injectivity/intersection results, that image has dimension 33. Independently of the raw-source extension, the entire 12-dimensional factorwise PGL₂ KS image is graded-central in Ext*(E,E). Consequently only the 21-dimensional quotient of the joint image by this central subspace can supply potentially useful polarized-product tests. This is a bound on first-argument directions, not a bound of 21 on the dimension of their Yoneda-product span. No such direction is proved noncentral, and no product or detector is proved nonzero or eliminated.

## 1. Fixed line bundles and the joint geometric parameter

Choose an identity neighborhood S of (PGL₂)^4×PGL₅ with regular GL₂ and GL₅ representatives, equal to identity at the base point. The four generating pairs of sections of O_C(2O) are transformed by the four GL₂ matrices. Multiply the resulting binary linear forms and apply the GL₅ matrix to their five coefficients. This gives five generating sections s₀,…,s₄ of N² on X×S: a product of four nonzero binary linear forms is nonzero, and an invertible linear combination preserves generation. They define the joint map F:X×S→P⁴ and an identification F*O(1)=N².

Hence N⊗F*K has fixed terms 5N⁻¹,15N,10N³,2N⁵. PR79 gives a locally split presentation on its six opens, conditional on A; arbitrary pullback preserves that splitting. Its degree-zero cohomology is the stated family E_(φ,g). The choice of GL representatives is fixed throughout; no global PGL₅ linearization of O(1) is claimed.

Let e_i be any of the fixed legal root frames of N. Choose any local frame ell of N² and write the five sections as s_j=v_j ell. Put

    c_i=e_i²/ell.

This is a unit wherever both frames are defined. One can always take ell=e_i², giving c_i=1; for direct comparison with an actual target pivot chart take ell to be a nonvanishing section s_p, so v_p=1. Nothing requires p=0. Refining by these target-chart choices, the legal opens and the pulled-back carrier opens gives a cover of X×S.

## 2. Authentication of changing target charts

Use the exact homogeneous weights from PR79 and FIRST-LIFT-STRUCTURAL:

- gamma, delta, ev have weight 1;
- I₀,P₀,W,L have weight 0;
- I₁ has weight 1;
- P₁,H₀,H₁,eta have weight −1.

Here W,L,eta refer to the pivot-dependent splitting of evaluation on the specified carrier; its pivot is retained. The two differently weighted I columns are never identified with a globally untwisted two-column map.

In the fixed e_i powers, the three differential arrays are c_i⁻¹ gamma, c_i⁻¹ delta, c_i⁻¹ ev. The actual source split arrays and inverses, with block sizes (5,1,1,8) and (8,2), are

    U_−1=Q_−1=Id₅,
    U₀=[c⁻¹gamma | I₀ | c⁻¹I₁ | c H₁ W],
    Q₀=[c H₀ ; P₀ ; c P₁ ; c⁻¹L delta],
    U₁=[W | c eta],       Q₁=[L ; c⁻¹ev],
    U₂=Q₂=Id₂.

These are precisely the arrays in FIRST-LIFT-STRUCTURAL §2, with the family homogeneous coefficients inserted.

Now replace ell by ell'=λell for an arbitrary regular unit λ, possibly depending on both X and S. Then v'=λ⁻¹v and c'=λ⁻¹c. A homogeneous primitive A of weight d has A(v')=λ⁻ᵈ A(v). Every displayed product has total weight zero in v,c. Thus EACH U_j,Q_j, and c⁻¹differential is unchanged. For example c'⁻¹I₁(v')=c⁻¹I₁(v), c'H₁(v')W(v')=cH₁(v)W(v), and c'⁻¹L(v')delta(v')=c⁻¹L(v)delta(v).

This proves compatibility on overlaps of target affine charts, including transitions away from v₀≠0. Because the arrays themselves agree, their full physical derivatives agree too. Equivalently, differentiating the scaled factors produces logarithmic derivatives of λ which cancel in these weight-zero products. Omitting those derivatives would be incorrect. The same holds for parameter derivatives. This calculation handles a variable square-line frame; it does not assume λ is constant.

Different carrier labels may choose different splittings. They are deliberately different vertices of the source cover, with the actual quotient transitions between them; they need not give identical U arrays. Only the auxiliary line trivialization at a fixed carrier/root vertex has just been shown to leave those arrays unchanged.

## 3. Actual regular family frames and determinant

PR79 supplies the carrier cover

    D₊(v_j⁵−∏v_l), j=0,…,4, and D₊(v₀v₁v₃v₄).

Its proof states that the specified primitives, with their unequal twists, are regular on these opens and that the carrier pivot is a unit. Pulling back and intersecting with root legal opens therefore makes every U and Q regular. The contraction identities give UQ=QU=Id and the same constant split arrows of ranks 5,8,2. This proves regularity and compatibility for the actual family rather than merely over its function field.

The cohomology columns in the e_i frame are I₀ and c⁻¹I₁. On the common rational reference with ell=1 and e_i=nu_i, they are nu_i I₀ and nu_i⁻¹I₁, exactly I_i diag(nu_i,nu_i⁻¹). Thus the quotient transitions recover the precise inherited row transition

    g_ij=D_j(P_i I_j)^t D_i⁻¹,
    D_i=diag(nu_i,nu_i⁻¹),

with all primitives pulled back by F. Equality on this reference identifies already regular maps; it is not used to infer regularity at infinity. Reduction at the identity recovers the original source.

The inherited homogeneous volume normalization says that the specified carrier ratio det[gamma,I,H₁W]/det[W,eta] is 1. Retain it as an input; arbitrary rank-two cohomology frames would not suffice. Its pullback gives det g_ij=1 for these actual frames, and the stored adjugate is the genuine inverse. The root and target line factors cancel in the determinant: E=N⊗F*H has det E=N²⊗F*O(−1)=O with the chosen identification. This abstract cancellation is consistent with, but does not replace, the literal volume-normalization input.

## 4. Fixed roots, full raw blocks, and actual closure over S

Extend each physical V_d from X relatively over S, killing parameter functions. The fields commute with each other and with every parameter derivative. The old root connection on N is fixed. In legal e_i frames let its coefficient be alpha_i, as in the root-line dependency. Define the SAME raw blocks, for weights k_j=−1,1,3,5, by

    B_i^j=−d_X U_i^j Q_i^j−k_j alpha_i Id.

These are differences of the actual split and old connections on the same family complex. All physical derivatives of every primitive and every c factor are retained. On overlap of legal root frames both connections transform by the usual connection rule, so their difference transforms tensorially; the ambient transition is scalar, so its coefficient conjugation is trivial. This is exactly the comparison used by the raw scalar recipe, not a new arbitrary gauge for its blocks.

The fixed old-connection differences give

    q_d,ij=(m_j,d−m_i,d)y_d/z_d,
    b_(a,b),ijk=(15/4)q_a,ij q_b,jk.

They are independent of S and retain their individual physical-factor support. Moving F does not move z,y, the branch equations, or these root connections. The universal ordered transgression proof therefore applies over S with the actual g and B: it yields the full raw scalar s_r, with all four blocks, endpoint-linear terms and the −15q_aq_b/8 correction, and the first lifts U_r=g(s_r Id+k_r), k_r=[g⁻¹V_a g,g⁻¹V_b g]/4. They obey

    U_r,jk g_ij+g_jk U_r,ij+mu_r(g_jk,g_ij)
      =U_r,ik+b_r,ijk g_ik.

No source term is frozen except the explicitly fixed root data and physical operators.

Define R_S by the complete literal homogeneous raw recipe of FIRST-LIFT-STRUCTURAL §7, including both Fk terms, both raw scalars, every E term, and the stated left normalization. That dependency proves the universal identity

    R_S=tf(M_S)+delta_S W_S,
    delta_S R_S=tf(g_il⁻¹ A_ijkl),

where, for p=(0,1),q=(2,3),

    A=mu_p(g_kl,b_q,ijk)g_ik+mu_q(g_kl,b_p,ijk)g_ik
      −g_jl mu_p(b_q,jkl,g_ij)−g_jl mu_q(b_p,jkl,g_ij).

Every term differentiates a gerbe in its complementary physical pair. Since V₂b_p=V₃b_p=V₀b_q=V₁b_q=0 over S, A=0 identically. Thus delta_S R_S=0. This is parameterwise closure of the actual residual, not differentiation of central-fiber closure or replacement of the residual by a newly chosen closed representative.

All ingredients are regular on the actual family intersections. Derivations extend to those localizations by the quotient rule. A denominator need not be preserved as an ideal. No operational pole/cutoff bound or execution admission is asserted.

## 5. Endpoint primitive for every joint tangent

Restrict to any dual-number tangent Spec k[ε]/ε² through the identity. Refine the central cover by affine opens. Nilpotent thickening preserves the underlying topology; every actual denominator with invertible central reduction remains invertible. Thus g_ij(ε),R_ijk(ε) are regular on a fixed affine cover and its overlaps.

Set G_ij=g_ij(0). Use first-vertex row-End frames, T_ij(M)=G_ij⁻¹MG_ij and a_ij=G_ij⁻¹dot g_ij. Then a is the KS cocycle, and differentiating parameterwise closure gives

    (delta dot R)_ijkl=a_ij(T_ij R_jkl)−(T_ij R_jkl)a_ij.

The exact endpoint correction h_ijk=R_ijk a_ik satisfies

    (delta h)_ijkl=−(T_ij R_jkl)a_ij+R_ijk(T_ik a_kl).

Consequently the regular cochain B_ijk=dot R_ijk−R_ijk a_ik obeys

    delta B=a cup R−R cup a.

This is the unprojected End identity. B need not be tracefree. It proves commutation with every joint KS class. It neither defines cohomological parallel transport nor proves [R] constant over S.

With a volume form on X, graded cyclicity of the Serre trace further gives [R]∈P_J^perp, where

    J=im κ_joint,
    P_J=span{ab+ba:a∈J,b∈Ext¹(E,E)}.

The 33-dimensional description of J uses the separate KS theorems; closure and the endpoint calculation themselves do not require injectivity.

## 6. All twelve factorwise directions are graded-central

This conclusion needs only the geometric bundle family, not any source or determinant-normalization premise. Write F₀=σ*H on Y. The fixed finite double cover has deck eigensheaves

    q_*O_X=⊕_S L_S,
    L_S=⊠_i O(−2) for i∈S and O for i∉S.

The proof by trace splitting and Euler characteristic is given in TRANSLATION-CENTER §1. Each O(−2) is canonically isomorphic to K_P¹ after choosing the fixed eigensheaf identification. The canonical line has a canonical PGL₂ linearization via pullback of differentials. O has its ordinary linearization. Hence every L_S is linearized for the FULL group (PGL₂)^4, not just its translation subgroup.

For any factorwise dual-number automorphism φ_A reducing to identity, E_A=N⊗q*φ_A*F₀. End cancels N. Projection formula and the linearization give

    RΓ(X_A,End(E_A))_S
      ≅RΓ(Y_A,φ_A*((End(F₀)⊗L_S)⊗A))
      ≅RΓ(Y,End(F₀)⊗L_S)⊗A.

These identifications reduce to identity at the central fiber. Therefore every Ext^m class extends over E_A. No action on the algebra q_*O_X is needed; the eigensheaves are compared as modules, so the fixed branch multiplication is not asserted invariant.

The connecting map for 0→End(E)→End(E_A)→End(E)→0 is b↦ab−(−1)^m ba, up to an immaterial uniform convention sign. Surjectivity of reduction makes it zero for all m. Thus W_F=im κ_factorwise is graded-central. Under the factorwise injectivity theorem dim W_F=12, and

    ab+ba=0 for every a∈W_F and b∈Ext¹(E,E).

This is all-character centrality. It does not assert either individual product is zero, and does not require a multiplicative trivialization of the relative Ext algebra.

## 7. Exact remaining scope

Write W_T=im κ_target. From dim J=33 and W_F⊂J with dim W_F=12, dim(J/W_F)=21. The bilinear map (a,b)↦ab+ba factors through (J/W_F)⊗Ext¹(E,E). Equivalently, P_J=P_WT and the three-dimensional diagonal-PGL₂ part of W_T already acts trivially in this polarized map. The other 21 first-argument directions may also act trivially. Centrality of W_F does not prove they do not.

No dimension of P_J is computed, no equality P_J≠0 is claimed, and no named retained scalar functional is identified with a Yoneda product. The orthogonality assertion may still be vacuous. The actual mixed lifting question [R]=0 remains open.

The essential source trust boundary is explicit: PR79 by itself supplies global primitive cover and contraction conditional on A, but not the literal homogeneous determinant normalization and complete raw-source identification. Those are the inherited FIRST-LIFT-STRUCTURAL premises used here. If those identifications are not admitted, the unconditional conclusions from the available bundle data are the joint geometric family and all-twelve graded-centrality; closure of the SAME actual residual and its endpoint consequences must then be quoted conditionally. No attempted execution here resolves that boundary.

All work consisted of static reading and formal structural reasoning. No actual source, matrix, rank, polynomial instance, point, jet, residual or detector was evaluated. 


## 8. Dimension-free extension to arbitrary generating coefficient tuples

The construction is more general than the joint automorphism family. Let S be any finite-type k-scheme with a marked k-point 0. On X×S take five sections s₀,…,s₄ of the fixed line bundle pr_X*N² which generate it everywhere and specialize at 0 to the pinned five coefficient sections. They define F_S:X×S→P⁴ with its specified identification F_S*O(1)=pr_X*N². No factorization through σ or group action is required.

Under precisely the same inherited homogeneous-source premises as above, there is a regular SAME-recipe raw source and a closed mixed residual on the common root/carrier cover of this family. For every tangent Spec k[ε]/ε²→S at 0, its KS class commutes with [R], with the explicit endpoint primitive of §5. The resulting Serre orthogonality holds for the entire KS image of this coefficient family, whatever its dimension.

Proof. In §1 replace the generating sections obtained by binary multiplication and GL transformations with the given sections. All remaining ingredients survive unchanged: the complex terms are the fixed powers N^(−1),N,N³,N⁵; the global carrier cover pulls back along F_S; on any line trivialization s_j=v_j ell and c_i=e_i²/ell; the weight-zero arrays of §2 are unchanged under arbitrary ell'=λell. Their contractions, regular inverses, and constant split arrows use only the homogeneous identities, not the origin of the v_j. The same volume normalization pulls back. The old root connections and physical derivations remain on X, extended relatively over S. Their q and b leaves are fixed and retain complementary-factor support. The universal transgression and mixed anomaly identities therefore give delta_S R_S=0 exactly as in §4. Every dual-number pullback admits the same fixed affine refinement and endpoint calculation as §5. These arguments do not require S smooth or reduced; one may instead work on a smooth tuple-parameter open if desired.

There is an actual universal parameter space for this statement. Let V=H⁰(X,N²). Inside the affine space V^5, the locus T of tuples generating N² is open: the incidence locus of (x,tuple) with all five sections zero is closed in X×V^5, and its projection to V^5 is closed because X is projective. Its complement is T. The pinned tuple belongs to T, and the tautological five sections give the family above over T. This establishes the geometric source family without claiming anything about the dimension or kernel of its KS map.

One can also divide tuple parameters by common nonzero scalar by working on an ordinary affine chart of P(V^5) and choosing its normalized representative. Such a chart carries an actual five-tuple of sections and falls under the theorem. This is a local construction on coefficient-parameter space; it is not a claim that the normalized literal residual descends under every parameter gauge without a chosen lift. The KS dimension of a projectivized coefficient family is a separate theorem and is not needed here.

The joint family is its pullback through the section-tuple construction in §1. Thus the earlier 33-dimensional special case is retained, while the source-extension theorem itself has no dimension assumption. Any stronger numerical KS conclusion or enlarged quotient count must be supplied and audited independently before being combined with this theorem.
