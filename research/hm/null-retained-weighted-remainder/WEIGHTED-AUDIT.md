# Independent audit: weighted transgression

## Verdict

ACCEPT at the explicitly admitted geometric/source scope. The partition-difference identity, annihilation of the sign-primitive ansatz, and full eight-term derivative remainder are correct. The trace normalization agrees with null-retained-weighted-remainder. This is an exact reformulation of the first-stage target, not a proof that its ten conditions vanish, and it leaves all thirty retained conditions open. No correction to WEIGHTED-RESULT.md is required.

This audit used static file reading and hand derivation only.  Geometric source denotations, genuine permutation linearization, flat connection identities, regularity, and class comparison are imported precisely as stated, not independently established by this audit.

## Sources checked

- null-retained-weighted-remainder/FILTRATION-RESULT.md, all sections.
- null-retained-weighted-remainder/FILTRATION-RESULT.md and WEIGHTED-AUDIT.md, especially the canonical first quotient, polarization convention, and finite-duality normalization.
- null-canonical-alternating-transfer/RESULT.md, especially the distinction between representative equality and class equality, the optional full-deck projection, and the canonical coefficient inclusion.
- null-pair-quotient-bracket/pair-quotient-0512/RESULT.md §5 and null-mixed-duality-reversal/DUALITY-RESULT.md §§2–3, for projector and trace identifications.
- null-complete-remainder-normal-form/RESULT.md, for the full baseline, four fluxes, combined derivative normal form, and conditional domain statements.
- null-second-order-raw-closure/PROOF.md and inputs/complete-residual-proof.md, for the closed complete five-branch representative and literal E operator.
- null-alternating-primitive/PROOF.md, for the corrected primitive, common-frame connection convention, and regularity qualifications.

No fresh remote authentication of those reports is claimed.

## 1. Signed cosets and coefficient 1/9

For the order-eight stabilizer H of the unordered partition 12|34, choose a decomposition S4 = disjoint union of t_i H. The half-polarization σ is H-invariant. With R_H=e_H R and r_i=sgn(t_i)t_i R_H, direct grouping of the 24-term projector gives

    eR = (1/3) Σ_i r_i,
    e(σR) = (1/3) Σ_i σ_i r_i,  σ_i=t_iσ.

No assumption that R itself is H-homogeneous is used. In particular, R_H is the full H-sign projection, including block exchange; it should not be replaced by only the two inner-swap projections. Replacing t_i by t_i h changes neither σ_i nor r_i: hσ=σ and hR_H=sgn(h)R_H cancel the extra sign. This also checks that coset convention and signed source transport are consistent.

For central coefficients σ_i, direct expansion gives

    Σ_{i<j}(σ_i−σ_j)(r_i−r_j)
      = 3Σ_i σ_i r_i − (Σ_iσ_i)(Σ_i r_i).

Thus Σ_iσ_i=0 converts the weighted average to exactly 1/9 times the pair-difference sum. There is no extra sign, factor of two, or surviving factor of six. All r_i include the complete geometric source action, not a permutation of bare formula labels.

## 2. Polarization differences and annihilation of the ansatz

With q_ab=(z−x_a)(z−x_b), the coefficients are (a,b,c)=(1,−x_a−x_b,x_a x_b). Substitution in bb′−2(ac′+a′c) gives exactly the stated σ_12|34. Expanding the three expressions verifies

    σ_1+σ_2+σ_3=0,
    σ_1−σ_2=3(x1−x4)(x3−x2),
    σ_1−σ_3=3(x1−x3)(x4−x2),
    σ_2−σ_3=3(x1−x2)(x4−x3).

These are polynomial identities, not values at a physical model. Homogeneous polarization gives their global line-valued meaning. The affine difference factors are never inverted, so no branch or collision locus is silently removed.

Because σ is H-invariant, its full invariant average is (σ_1+σ_2+σ_3)/3=0. If eP=P, then gP=sgn(g)P, and hence

    e(σP) = (average_g gσ)P = 0.

The row differential commutes with the geometric action and multiplication by the global section. Therefore e(σδP)=δe(σP)=0 as well. Applying e to the known primitive is legitimate: δ(eP)=e(δP)=eR. This conclusion applies to the sign-projected primitive. It does not claim that weighting every possible unprojected primitive is zero.

The mean-subtraction identity n_i=r_i−δP is also exact: Σ_i n_i=0 and Σ_iσ_i n_i=Σ_iσ_i r_i. It supplies no primitive for a partition difference and imposes no hidden vanishing on the new remainder.

## 3. Complete source and all eight Leibniz terms

The source agrees with the inspected five-branch formula:

    R = tf(M0)+F_q k_p,ik+F_p k_q,ik+E_p(s_q)+E_q(s_p).

M0 retains the seven kinetic terms and the three negative gerbe terms before trace projection. Both Fk terms have positive signs and complementary pairs. F is not replaced by a raw scalar endpoint.

For E_(a,b), applying the ordinary scalar Leibniz rule at each endpoint adds precisely

    +(D_aσ)s_jk L_b/2,
    −(D_bσ)s_jk L_a/2,
    +(D_bσ)s_ij U_a/2,
    −(D_aσ)s_ij U_b/2.

Applying the same rule to E_(c,d)(s_p) gives the other four terms in equation (10), with exactly the displayed signs. U_v=g_ij^−1 g_jk^−1(D_v g_jk)g_ij is the transported current in the first row frame. Neither endpoint, transport factor, nor factor 1/2 is missing. Rearranging E(σs)=σE(s)+H explains the minus H in equation (2).

Grouping by D_aσ, D_bσ and their complementary analogues gives exactly the four fluxes Z_v from null-complete-remainder-normal-form, so H_σ=Σ_v(D_vσ)Z_v. This is an equality of Leibniz expressions, not an assertion that σ has the type of the earlier Serre test. It does not remove that report’s current-curl, selector, overlap, or nonclosed-flux families.

The displayed formal partial derivatives of σ_1 are correct, as is D_vσ=y_v∂_vσ for the specified product derivations on functions of x_v. Their being nonzero polynomials does not prove the actual combined H_σ is nonzero.

## 4. Regularity and global meaning

The cochain identity (1) is regular under the imported regular-source hypothesis: finite group projection and transport preserve regular sections on a common invariant refinement; multiplication by global line-valued σ_i preserves regularity; subtraction introduces no denominators. Closure follows from δR=0 and the commuting coefficient maps.

The separated derivative expressions in equations (9)–(11) are local common-frame expressions. An ordinary derivative of an O(1)-valued section is not intrinsically defined independently of frame. WEIGHTED-RESULT.md correctly retains this caveat and identifies the combined right side of (2) intrinsically with σR. It asserts neither global descent of an isolated derivative term nor a globally chosen algebraic connection on this line bundle. A local covariant formulation must retain the line-connection contributions throughout.

Consequently the audit does not promote the displayed local eight terms into separately authenticated finite-selector inputs or stronger all-chart pole bounds. The complete-remainder report itself has conditional domain premises and combined-term covariance; those limitations remain intact.

## 5. Duality normalization and comparison boundary

Write F=m_*O_X, with Tr_alg(1)=6. Under finite duality, λ is a section of Hom(F,ω_Y), and

    Tr_m^ω(σλ)=λ(σ).

The constant inclusion is I(μ)(f)=μ Tr_alg(f)/6. Its retraction is evaluation at 1, so Tr_m^ω I=id. Therefore the constant projector on σλ is exactly I(λ(σ)). The identification of the geometric sign projector with this constant projector gives equation (4), in the common coefficient realization and with the O(1) twist retained. The /6 belongs to I, not to the duality trace. Neither the /24 group average nor the /3 partition average changes λ(σ) to λ(σ)/6.

The transfer source supplies [R]=j[C], rather than an equality of raw representatives. On an acyclic common refinement, choosing a regular comparison cochain q with R−j(c)=δq gives

    e(σR)=I(Tr_m^ω(σc))+δe(σq).

Thus any proposed primitive h of e(σR) must be adjusted to h−e(σq), projected into the relevant coefficient sector if necessary, before applying the inverse constant coefficient identification. WEIGHTED-RESULT.md does not set q to zero or claim to have computed it. If only the weaker comparison is used, the full-deck projector must be applied throughout first; the deck-invariance of σ makes that valid.

Finite duality and these coefficient maps are global at ramification. No inverse Jacobian or generic-point argument is introduced. The target remains the canonical ten-dimensional quotient test from null-retained-weighted-remainder, not a newly selected ten-dimensional complementary subspace.

## 6. No hidden zero claim

The weighted curvature identity d(fB)+(fB)^2=df∧B+(f²−f)B² follows from dB=−B²; the extra term in d(fS)=fT/4+df∧S is likewise correct. These diagnose specific failed substitutions, not all possible transgressions.

The actual open task is still to construct a regular h with δh equal to the partition-difference remainder, including the comparison adjustment above. Neither zero average of σ, exactness of eR, closure of R, nor the explicit derivative remainder implies that such an h exists. Conversely nothing here establishes nonvanishing of the actual obstruction. The report’s stopping point is accurate.
