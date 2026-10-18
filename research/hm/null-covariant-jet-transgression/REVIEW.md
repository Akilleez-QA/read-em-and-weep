# Independent bounded review

## Verdict

PASS, conditional on the exact input contract in the frozen rank-two collection and complete remaining-target normal form. The new identity is an exact transgression of the complete S2 family. It is not a vanishing theorem, residue evaluation, independent global domain theorem, or physical execution claim.

## Independently checked derivation

Write D_a for commuting physical derivations. For an invertible A, differentiation of the inverse gives D_a(A^-1)=-A^-1(D_a A)A^-1. Hence D_a L_b=A^-1 D_aD_b A-L_aL_b. All currents are traceless by the supplied contract. Rank-two polarization gives tf(L_aL_b)=[L_a,L_b]/2, and the scalar parts cancel because D_a L_b is traceless. Therefore

    D_a L_b=H_ab-[L_a,L_b]/2.

For any matrix-valued X, the moving-frame product rule is

    D_a(A^-1 X A)=A^-1(D_a X)A+[A^-1 X A,L_a].

Apply the preceding normalized-current identity to B before transporting. The result is

    D_a U_b=J_ab-[L_a,U_b]-[U_a,U_b]/2.

Thus H_ab=nabla^P_a L_b and J_ab=nabla^Q_a U_b with P_a=L_a/2 and Q_a=L_a+U_a/2. Both jets are symmetric because the original physical derivatives commute; no ordinary derivative of a frozen stripped frame is used. In particular

    nabla^P_a U_b=J_ab-[T_a,U_b]/2.

The curvature of P is F^P_ac=-[L_a,L_c]/4. The curvature of Q is F^Q_ac=-[U_a,U_c]/4, retaining the full L transport terms. Since H_cd=nabla^P_c L_d,

    nabla^P_a H_cd-nabla^P_c H_ad=[F^P_ac,L_d].

The four-entry signed sum is antisymmetric under a↔c with b,d held fixed. It therefore replaces nabla^P_a H_cd by half the last curvature expression. Consequently the differentiated Phi contributes exactly -sum e[U_b,[[L_a,L_c],L_d]]/64. Moving it to the other side yields the stated positive C4. The factor is (1/8)(1/2)(1/4), and its sign is not optional.

The other product-rule contribution is [J_ab,H_cd]/8 minus [[T_a,U_b],H_cd]/16. The remaining transport mismatch belongs in M2. Rank-two Fierz contraction expands it as

    [[T_a,U_b],H_cd]/2
      =d(U_b,H_cd)T_a-d(T_a,H_cd)U_b.

Combining its L_a component with the old -d(U_b,H_cd)L_a leaves the displayed +d(U_b,H_cd)U_a. All old terms linear in H or J remain. Therefore this is an audit of the whole S2 formula, not only its [J,H] term. Q4 remains exactly the prior full quartic remainder; adding C4 changes its displayed representation but is not an extra cancellation.

## Full dual-kernel audit

For arbitrary nonconstant same-frame W, trace cyclicity and the product rule give

    d(W,nabla^P_a Phi_a)
      =D_a d(W,Phi_a)-d(nabla^P_a W,Phi_a).

The plus connection inside nabla^P W follows because ad(P) is skew-adjoint for d. Pairing the complete formula yields an ordinary scalar divergence, d(W,C4), and the H/J pairings with

    H-adjoint = a_ab W-d(W,L_b)U_a+d(W,U_a)U_b
                    -d(W,U_b)T_a-[nabla^P_a W,U_b],
    J-adjoint = b_cd W-d(W,U_d)L_c-d(W,U_c)L_d,

all weighted by e/8. W must be the complete adjoint of the original test, staircase, extraction and full insertion kernel in its literal order. D_a W differentiates every varying factor of that complete kernel. A constant test does not make the complete W constant. The ordinary divergence has not been shown to have zero global trace or residue; the new flux needs its own legal source/domain argument. Existing Ccur, test/selector, overlap/homotopy and K Delta Z terms remain unchanged.

## Evidence and negative controls

The author's checker verifies the whole transgression, its nonzero formal current-jet coefficient, both midpoint curvatures, and failures after omitting curvature, reversing its sign, dropping transport mismatch, or dropping linear jets. The independent audit checker verifies the nonconstant dual adjoint, ordinary derivative plus connection decomposition, both midpoint transport identities, Fierz and trace skew-adjointness. It rejects deletion or sign reversal of the full kernel derivative, deletion of the connection adjoint, and frozen A transport.

These are exact universal scalar-coordinate coefficient identities over Q, with no substituted source/model/owner/jet values. The independent audit reuses only the author's scalar polynomial/Lie-operation implementation; its formulas and negative controls were written separately. It does not pretend to be a second independent algebra engine. No physical matrix-polynomial products, production imports, experiments, remote authentication, external writes or publication occurred. Runtime failures use explicit exceptions rather than Python assert; optimized runs retain every check.

## Symmetry and boundary of covariance

The four signed complements and symmetric H/J index sorting were checked against the frozen original convention. The identity is equivariant under simultaneous constant conjugation, and covariant as an identity for connections and sections transformed by their proper laws. It does not identify half of a physically redefined Maurer-Cartan current with an arbitrarily gauge-transformed connection: changing the original physical trivialization requires transforming the entire normalized input contract. No gauge or owner-domain extension follows merely from the word covariant.

## Independently reviewed quartic addendum

The bounded QUARTIC_ADDENDUM.md also passes. Its R22 and three-U terms copy the full retained Q4 without alteration. Reverse the two innermost brackets in 32 C4=[U_3,[BL_12,L_4]]-[U_4,[BL_12,L_3]] and add the old slot-3/4 terms. This gives exactly +{ad_L3,ad_U4}BL_12-{ad_L4,ad_U3}BL_12. Applying the already checked Fierz identity to both double brackets proves its trace expression, including the -2 Delta_34 coefficient. Thus only the LLUL and LLLU current multidegrees change. The two newly introduced z-coordinate coefficients are respectively +1/8 and -1/8, so these changed maps survive. The other twelve mixed sectors are unchanged and nonzero; both pure sectors remain zero. This is formal polynomial support, not a physical specialization.

The author's additional checker verifies the formula, trace collection, all sixteen projections, and both new coefficients. The independent additional checker compares C4 against the original four-entry transgression, verifies the symmetric double-adjoint trace identity, rejects curvature omission/sign reversal, and confirms that each monomial contains exactly one current from each of the four slots. It also reconstructs each full polynomial from all sixteen projections, guarding against incomplete or misleading sector filters. All four checkers use only rational scalar-coordinate polynomials. Their dependence on shared algebra code is disclosed; no independent physical computation is implied. This addendum changes none of the main proof's domain, adjoint, residue, source, or complete-remainder qualifications.
