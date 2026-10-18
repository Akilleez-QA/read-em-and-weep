# All six reference cohomology connections are diagonal and flat

This is an exact sparse-support consequence of the pinned source model, not a general flatness inference from the ambient split connections. It is confined to the original all-finite realization, with the common ambient frame and cohomology normalization used in the preceding notes.

Define the rational functions

    s_0=1, s_1=v1, s_2=v2, s_3=v3, s_4=v4,
    s_5=-v4/v1^2,
    sigma_c=dlog(s_c).

The source I/P supports imply, for all six carrier labels,

    Gamma_c^ref=P_c^ref dI_c^ref=diag(0,sigma_c).           (1)

For primary carrier c=0,...,4, only ambient row c contributes to the first diagonal component and row c+5 to the second. The selected I entries are respectively 1 and v_c, with matching P entries 1 and 1/v_c; v0=1. Off-diagonal support intersections are empty. For auxiliary carrier5, the intersections are rows5 and14. The selected I entries are 1 and -v4/v1^2, paired with 1 and -v1^2/v4. Again the off-diagonal intersections are empty. The auxiliary pivot is v0, so sigma_5 must NOT be replaced by dlog of its pivot.

These are exact identities of rational functions authenticated by the companion structural checker. No other I entries contribute to P dI, regardless of their derivatives, because the relevant P entries vanish identically.

After C_i=diag(nu_i,nu_i^-1), with ell_i=dlog(nu_i), the physical common-frame connection is

    Gamma_i=C_i^-1 Gamma_c^ref C_i+C_i^-1 dC_i
           =diag(ell_i,sigma_c-ell_i).                   (2)

Thus its local curvature is exactly zero: both entries are closed logarithmic one-forms and a diagonal one-form wedges with itself to zero. The pivot-shifted connection has the same curvature because the added scalar pivot connection is flat. This verifies actual local flatness in these frames; it does not make the projection descent defect Q or Lambda vanish.

The rank-two coefficient in the compact raw scalar therefore becomes

    kappa_i=-tf(Gamma_i)=(sigma_c/2-ell_i) h,
    h=diag(1,-1).                                       (3)

This replaces the projected ambient first-derivative calculation for kappa by two explicit logarithmic one-forms. The compact scalar still contains its contraction term K_h(T,Z), the weighted-line terms and gerbe representative; none is dropped. Derivatives of the coefficients in (3) must still be retained when applying E.

The carrier-reference projection defect is now expressible using transitions alone:

    Q_ij^ref=K_ij diag(0,sigma_j) K_ij^-1
             -dK_ij K_ij^-1-diag(0,sigma_i).             (4)

Consequently the first-jet Lambda diagnostic needs only the rational 2-by-2 transitions and their first derivatives plus these known logarithmic forms. It no longer needs independent 15-by-2 I/P derivative construction. The transitions themselves still come from the actual source and must be authenticated.

For the weighted trace A_j in the mask reduction, cyclicity further yields

    A_j=-sigma_j
         -tr(K_ij^-1 dK_ij h)
         -sigma_i (K_ij h K_ij^-1)22,                   (5)

where 22 means the second diagonal entry. Its tracefree matrix makes no difference because the conjugated h has trace zero. For carrier0, sigma_i=0, recovering the exact pair formula used in the leading-term obstruction note. Formula (5) uses sigma, not the potentially different pivot logarithm p.

These reductions do not establish any global obstruction value or extend the fixed Omega computation. Their relation to the original common-frame Lambda formula remains available for independent review alongside the prior notes.
