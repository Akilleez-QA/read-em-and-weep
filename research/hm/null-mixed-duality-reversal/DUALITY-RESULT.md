# Serre-dual detectors and the failed self-duality vanishing argument

## Checked outcome

For the corrected external-product ambient and its unique pure boundary, the actual canonical mixed obstruction C is block-even. Its perfect detector space is the block-even 32-dimensional H²(X,End₀(E)), not the block-odd 30-dimensional space. There is a canonical split into two pullback detectors and thirty trace-zero finite-cover detectors. The retained component vanishes exactly when it pairs to zero with all thirty latter detectors.

The proposed elimination by rank-two self-duality fails by a precise sign: alternating adjoint is minus identity on End₀(E), but dualization of a multiplicative obstruction introduces another minus. Their product is plus identity. Even granting a compatible self-duality of the entire ambient and boundary with identity action on the mixed ideal, this supplies no additional equation on the thirty-dimensional component. This is a checked failure of this particular symmetry argument, not an evaluation of C.

## Inputs and scope

Historical public context: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6271101716 and predecessor 6270678828. Read the pinned second-order-algebroid.md (commit c8aec970fd65a105f39f4e8aeb8a17f0f0053f89), including its row convention, normalized defects, and full-sign projection. Additional dependencies: null-mixed-module-equation/RESULT.md, null-actual-pair-comparison/RESULT.md, null-pair-quotient-bracket/pair-quotient-0512/RESULT.md, null-pure-lift-uniqueness/pure-lift-uniqueness/RESULT.md, null-corrected-pure-lift/corrected-relative-lift/RESULT.md, null-module-boundary-audits/semiregularity-sector/RESULT.md, null-permutation-sector/PROOF.md.

Only universal coherent cohomology, finite duality, and symbolic defect identities are used. 

## 1. The actual canonical class is block-even

Put X=P²_z×P²_h, Y=P⁴, E=m*HM, A₀=End₀(E), J=ω_X, and τ(z,h)=(h,z). Since mτ=m, E has a canonical coherent τ-linearization. The two corrected pair presentations are copies of the same presentation. Their external product has exchange symmetry with K_z exchanged with K_h and J carrying ordinary product exchange.

Swapping top forms of degrees two and two gives (−1)^(2·2)=+1. The coefficient ideals are ordinary ungraded sheaves, and bookkeeping symbols s,t commute, so st is exchange-even. This identifies the linearization of J; it does not assert that τ acts trivially on its entire cohomology.

The compact pure lifting groupoids are contractible by the imported H⁰ and H¹ vanishings. Exchange identifies the unique pure boundary with itself; the comparison squares to identity by uniqueness. Naturality of the small-extension obstruction, equivalently mixed-module formula (6) and its gauge coboundary identity (10), gives

    τ*C=C in H²(X,A₀⊗J).

This is a statement about the actual canonical class of this ambient, not merely the target dimensions, and does not identify a frozen physical module two-jet.

The quadratic source u_jk v_ij+v_jk u_ij has the same sign: the degree-one graded commutator [u,v]=u cup v+v cup u is symmetric. Exchanging pure directions does not negate it. The ambient M, w, and bc terms also exchange with positive sign, preserving each internal matrix order.

## 2. Exact Serre pairing and its signs

The trace pairing A₀⊗A₀→O is nondegenerate in characteristic zero. Serre duality on the smooth projective fourfold gives

    H²(X,A₀⊗ω_X) × H²(X,A₀) → C,
    <C,d>=SD_X(tr(C cup d)).                         (1)

Here SD_X:H⁴(X,ω_X)→C is the canonical trace. On a common affine trivializing Čech cover, with normalized endomorphisms in their first-index frame and τ_ij(a)=g_ij⁻¹ag_ij, its degree-four representative is

    tr(C_i0i1i2 · τ_i0i2(d_i2i3i4)).                 (2)

Coefficient-line restrictions are implicit. Coboundary changes in either argument change (2) by a coboundary. Thus this is a test on the actual class, independent of the pure representatives in formula (6).

Naturality of Serre trace gives <τC,τd>=<C,d>. Therefore an even C annihilates every odd d, and the restriction of (1) to the even spaces is perfect. The even detector dimension is 32, the odd dimension 30.

Graded cyclicity contributes (−1)^(2·2)=+1 on interchanging the degree-two arguments. There is no antisymmetric Serre form here forcing these pairings to vanish. Indeed the arguments are in different spaces, canonically twisted and untwisted: a proposed self-pairing of C is undefined without extra data.

## 3. Canonical two plus thirty detector split

Let B₀=End₀(HM), F=m_*O_X. The imported finite-flat calculation gives F⁺≅O⊕O(−1)⊕O(−2), F⁻≅O(−1)^3. These are isomorphism types, not specified summand bases. Let Tr:F→O be algebra trace, Tr(1)=6, and let F₀⁺=ker(Tr|F⁺). Then canonically

    F⁺=O·1 ⊕ F₀⁺,
    D⁺=H²(X,A₀)⁺=m*H²(Y,B₀) ⊕ H²(Y,B₀⊗F₀⁺).    (3)

The constants projector is f↦Tr(f)/6. The cohomology summands have dimensions two and thirty. A noncanonical splitting computes the latter as h²(B₀(−1))+h²(B₀(−2))=10+20. Scalar End summands do not affect these H² groups because line bundles on P⁴ have no intermediate cohomology.

Finite duality gives m_*ω_X=Hom(F,ω_Y). Pairing downstairs is literally evaluation followed by SD_Y:

    (a⊗λ,b⊗f) ↦ tr(ab) λ(f).                       (4)

There is no arbitrary degree-six normalization in (1). The constant projector on λ is

    λ_const(f)=λ(1)Tr(f)/6.                         (5)

Its complement vanishes on 1. Formula (5) is the fully alternating two-dimensional projector identified in pair quotient report, dual to the constants projector in (3). Consequently

    T_ret=H²(Y,B₀⊗(F₀⁺)*⊗ω_Y)
    D_ret=H²(Y,B₀⊗F₀⁺)

are canonically perfect duals of dimension thirty, and

    C_ret=0 iff <C,d>=0 for every d∈D_ret.           (6)

Equivalently, once the two-dimensional constant projection is known to vanish, C defines a functional on H²(X,A₀)⁺/m*H²(Y,B₀), and C=0 iff that functional is zero. The quotient has dimension thirty. The vanishing prerequisite is essential: it is precisely what allows the functional to descend to the quotient. If not yet established for this transported class, also test the two pullback detectors. This argument does not independently prove the alternating projection zero.

Thus the block-odd thirty-space is annihilated automatically; D_ret is the full surviving thirty-dimensional detector space within the even 32-space. Equal dimensions do not identify them.

## 4. Rank-two self-duality has two minus signs

Every rank-two bundle has canonical determinant-valued alternating form q(v,w)=v∧w and E≅E*⊗det E. Here det E=O_X(−1,−1), using normalized HM. It must not be replaced by an untwisted E≅E*.

Define q-adjoint by q(av,w)=q(v,a†w). The rank-two identity

    a†=tr(a)Id−a

follows from q(av,w)+q(v,aw)=tr(a)q(v,w). Hence †=−Id on A₀ and +Id on scalars. Adjoint reverses products: it is an anti-automorphism, not itself a symmetry of the module deformation problem.

For a normalized multiplicative gluing defect 1+C in a square-zero ideal, the dual representation is contragredient and transforms the defect as

    ((1+C)⁻¹)^t=1−C^t.

After identifying twisted dual with E by q, its infinitesimal operator is

    C ↦ −C†.                                        (7)

The minus comes from inversion of the multiplicative defect, not cyclic permutation in Serre pairing. Čech degree two does not add a further sign to this direct calculation. As a check, g↦g^{-t} preserves the order of a product: (ab)^{-t}=a^{-t}b^{-t}. Applying plain transpose to a Čech two-cocycle and demanding invariance under +† omits the inversion and yields the wrong constraint.

Since †=−Id on A₀, (7) is +Id on every tracefree obstruction. A compatible self-duality with identity action on J would therefore say C=−C†=C, imposing nothing. Its scalar constraint would be C_scalar=−C_scalar, but H²(X,ω_X)=0 already eliminates that part.

More generally, if the comparison from the dual ambient back to the original acts on J by ε∈{±1}, the operator is ε(−†). The comparison must be established, not inferred from q. Simultaneous reversals s↦−s,t↦−t have ε=+1 at mixed order, so the usual simultaneous-reversal possibility does not improve this sign. A genuine one-factor reversal would have ε=−1 and could force vanishing; ordinary duality supplies no such symmetry.

In fact dualization first lands over the opposite algebroid. Locally the product becomes opposite; overlap maps remain F and central coherence units become A^{-1}. A simultaneous coefficient reversal also changes the unary maps v, so it is not automatically an equivalence with the specified original presentation. A determinant-valued classical form does not construct a deformed determinant-line/bimodule twist. We assert no such full equivalence here. Even granting an equivalence with ε=+1, the tracefree sign above is tautological.

Finally tr(a†b†)=tr(ab), since adjoint reverses product and trace is cyclic. Both tracefree adjoints contribute minus. There is no missing negative on one side of (1) that kills the detector functional.

## 5. Exact limitation and next test

Block-evenness and the hypothetical self-duality condition with ε=+1 permit the entire even target. After a separately certified alternating projection removal they permit the entire retained thirty-dimensional target. Perfect duality says every nonzero vector there has a detector in D_ret. This proves why these symmetry identities cannot establish its vanishing.

A further reduction requires a genuine new annihilation identity for (6), or a compatible symmetry acting nontrivially on this space. A one-factor reversal would be sufficient if actually constructed and verified, but is not presently available. No value of (6) has been evaluated.

Independent sign check: a separate reviewer confirmed inverse-transpose defect transport, absence of an extra Čech-degree sign, the need for an actual opposite-ambient comparison and its ideal action, and the distinction between the canonical-line exchange sign and the action on cohomology.
