# Polynomial comparison weights through the fixed source

## Scope

This is a next step after the accepted translated background-source family. It constructs algebraic comparison weights agreeing with the original weights at parameter zero. It does not assert a numerical Bezout witness, a finite cutoff, a detector value. Independent review is recorded separately.

Use one shifted factor, z=x-s and y^2=z^3-z, with sigma(s)=sigma(x)=1 and sigma(y)=0. The source complex is pulled back at v=e_k(x), while the root frames use y/z. At s=0 this is the original source. Work over a characteristic-zero field k, and retain the established homogeneous carrier cover and original standard target charts.

## 1. Actual homogeneous legal sections

On the shifted target factor P^1 with homogeneous coordinates [X:Y], the root legal opens are represented by

    L_0=Y,
    L_1(s)=(X-sY)((X-sY)^2-Y^2).

Their degrees remain one and three. They have no common zero on any parameter fiber: at Y=0, L_1=X^3 is nonzero. On the finite chart the factors are 1 and z(z^2-1). On the inverse-x chart t=Y/X they are t and

    A B,  A=1-st,  B=A^2-t^2.

This includes the additional factor A that cannot be omitted away from s=0. The unshifted factors retain their original legal sections. The original homogeneous carrier sections are evaluated at v(x), not v(z).

For every geometric parameter and target point, at least one carrier section and one legal section in each factor are nonzero. Thus the products associated to the actual carrier/mask owners cover the family of each standard target chart. This is the same complete Cartesian owner family used in the original full comparison; if a reduced owner list is substituted, its covering property must be separately proved.

## 2. Unit ideal over the parameter ring

Fix one standard target chart, with coordinate ring R_0=k[t_1,t_2,t_3,t_4], where each t_i is its finite or inverse coordinate. Set R=R_0[s]. For every actual owner o in this chart define

    C_o(s)=H_o(v(x))^54 product_i L_(o,i)(s)^29,

using the regular local representatives of the homogeneous sections on this chart. Powers do not change the zero locus. The family-cover assertion in section 1 implies that these C_o have no common geometric zero over the algebraic closure of k. Therefore their ideal is the unit ideal in R. One may prove this by the weak Nullstellensatz over the algebraic closure, followed by faithful flatness of the field extension. Consequently polynomial R_o(s) exist with

    sum_o C_o(s) R_o(s)=1.

No specific R_o or bound on their polynomial degrees is computed or asserted.

## 3. Matching the original partition exactly

Let the original polynomial witnesses on this same chart be Q_o^0, satisfying sum C_o(0)Q_o^0=1. Regard them as s-independent elements of R, and define

    e(s)=1-sum_o C_o(s)Q_o^0,
    Q_o(s)=Q_o^0+e(s)R_o(s),
    rho_o(s)=C_o(s)Q_o(s).

Then e(0)=0, hence Q_o(0)=Q_o^0 and rho_o(0)=rho_o^0 exactly. Also

    sum_o C_o(s)Q_o(s)
      =sum_o C_o(s)Q_o^0+e(s)sum_o C_o(s)R_o(s)=1.

Thus the family partition specializes to the original fixed partition, rather than merely to an unrelated choice of Bezout witnesses. This construction is performed chartwise with the same owner-to-target assignment. The ordinary full comparison uses all of these original target tags and every sampled source occurrence.

The cochain-map assertion has the following precise domain. Fix a coefficient line bundle F on Y times the parameter line, with its original standard frames. Put D_o(s)=H_o^16 product_i L_(o,i)(s)^10. Let S_D be the all-ordered source cochains such that multiplication by the product of D_o over ALL original source occurrences extends the cochain regularly to the FULL original tagged standard intersection over k[s]. These are extensions in the appropriate homogeneous coefficient line, with every original target tag retained. Faces preserve this property after multiplying by the additional missing owner's regular clearing section, so S_D is a subcomplex.

On S_D, the product of the own rho_o clears every sampled occurrence: rho_o/D_o is regular on that owner's chart. The original full-target argument therefore gives a regular k[s]-linear comparison into the ordinary sixteen-chart standard complex. The usual face calculation, using sum rho=1 at the omitted occurrence, proves it is a cochain map. It specializes exactly to the original comparison. This does not assert that any particular moving source belongs to S_D; that membership is a separate uniform all-chart theorem. A unit-sum partition alone cannot regularize arbitrary source cochains.

Here specialization means equality of the comparison formulas on central restrictions of family cochains. No surjectivity of specialization from this family bounded complex onto every fixed-source bounded cochain, or base-change isomorphism for those complexes, is asserted.

Differentiating the partition identity gives sum sigma(rho_o)=0 on the corresponding localized family rings. All weights and witnesses vary according to these formulas; no coefficient may be frozen simply because it was fixed at s=0.

## 4. Divisibility of parameter derivatives

The derivation sigma is regular on the finite chart, where it is partial_s+partial_x on the shifted factor. On the inverse chart it is partial_s-t^2 partial_t. It therefore acts on each chart polynomial ring and extends to every required localization.

The product rule shows that sigma(C_o) is divisible by H_o^53 and each legal factor L_(o,i)^28. Terms differentiating Q_o retain the stronger C_o factor. Thus sigma(rho_o) has this same own-owner divisibility. This is an upper bound; some legal factors have stronger divisibility because their translated geometry is transported with sigma. No clearing factor is borrowed from another occurrence, and equal physical divisors do not identify distinct occurrences.

This establishes divisibility only. Applying it to a newly differentiated source expression still requires that expression's uniform all-chart owned domain. The construction does not by itself transfer an executable degree cutoff or authenticate a physical terminal.

## 4a. Regular variation on the bounded family complex

For F=O(n_1,n_2,n_3,n_4), use the natural translation lift in the shifted factor. Its finite coefficient operator is partial_s+partial_x. In the inverse coordinate t=1/x its coefficient operator is

    partial_s-t^2 partial_t+n_1 t.

Indeed f_infinity=t^(n_1) f_finite, and the extra n_1 t term cancels sigma(t^(n_1))=−n_1 t^(n_1+1). The operators therefore agree on overlaps, commute with restrictions, and satisfy the Leibniz rule with scalar coefficients. For the full-sign direct summand of q_*O_X, n_1=−2, recovering the necessary infinity odd-basis correction rather than falsely commuting the coefficient extractor with sigma.

This lift takes S_D(16/10) to S_Dplus(17/11). To see this, differentiate the cleared regular section. The lift preserves regular sections on the standard family chart; differentiating the product of H^16 and L^10 in a denominator requires at most one additional power of each own factor. The zero-order n_1 t term is regular on its chart and creates no new pole. This is an upper bound, with all original occurrence positions and tags retained.

The exact variation of the full comparison is the sum of two families: comparison of the lifted input derivative, plus the sum differentiating each of its original scalar weights once. The first is cleared by ordinary54/29 against17/11. In every term of the second, the differentiated occurrence has53/28 divisibility against16/10 and all other occurrences retain54/29. Both families are regular on the full original target intersection. No derivative of a weight is omitted, no finite truncation is introduced, and no actual-source membership assertion is added by this consequence.

## 5. A local connection check supporting uniformity

In the shifted factor's inverse-x chart let u=y/x^2. Then u^2=tAB. For mask m, the normalized root square is c_0=t and c_1=B/A. With the same global physical derivation V(t)=-u, its logarithmic coefficient is rho_m=(1/2)V log c_m. The old root coefficient is alpha_m=m u t/(AB).

Directly,

    rho_0=-u/(2t),
    rho_1=u[s A^2+t(1+A)]/(2AB),
    beta_m=alpha_m-rho_m,
    beta_0=u/(2t),
    beta_1=-s u/(2A).

These identities follow from the finite expression rho=m V log(y/z) followed by subtracting (1/2)V log x in the normalized target frame. In particular beta_1 is generally nonzero when s is nonzero; reusing the original infinity identity beta_1=0 would be wrong.

Every displayed possible pole is owned by the actual legal factor: t for bit zero and AB for bit one. Thus this previously delicate local scalar connection estimate continues to have legal allowance one. This alone does not re-prove every primitive or source-domain bound; it isolates a necessary chart check rather than assuming that all old coefficients are unchanged.

## Limits

The new construction is a polynomial family of full comparison weights through the exact original weights, with explicit own-owner derivative divisibility and a checked shifted infinity connection formula. It is conditional on the actual complete carrier/mask cover and original polynomial witnesses. No specific polynomial witness is evaluated, no checker is rerun. The parameter s varies background source data and is not the star-deformation order parameter epsilon.
