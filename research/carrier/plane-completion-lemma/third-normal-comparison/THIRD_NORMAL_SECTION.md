# Third-order section on the completed fixed plane

## Result

On the explicit symplectic plane completion, the literal frozen first-, second- and full third-middle tensors admit a regular section through normal order three. The resulting structured lift is defined modulo h⁴ over Q[a,b,c,d,lambda], preserves the distinguished line P, and has the prescribed pairing +t0 h with no second- or third-order pairing coefficient.

All 40 possible cubic-order parameter coefficients are computed. Seventeen are nonzero, comprising 1,874 Laurent terms. Every term is regular on its named base/plane open and has the required line-bundle degree and character. There is no division by deformation parameters.

This is a finite-order realization on our completed plane object. It does not identify an ancestor or algebraic carrier, establish defect or reflexive-hull base-change properties, or assert that higher section orders extend.

## Fixed input and gauge

The first-order section and the second-order section are exactly those of the earlier frozen packages. The full third-middle cochain is exactly `THIRD_MIDDLE_COCHAINS.json`, SHA256 `011ba80d06f7b47a077845f377e9b22a5a9e51d808804e88e2ba4bf66c2306cd`, constructed from pinned repository commit `6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb` using the literal second primitive, regenerated D3 inverse and ordered Laurent Čech homotopy.

The second-section input has SHA256 `c6f2120accbc6d8900a4ceef9fb2ba1258fcc790dd323657b47c48c7630e905f`. `first_order_support.py` is byte-identical to the frozen first-normal checker and recomputes its 746 exact checks. `section_action_support.py` extracts the generic tensor-action functions of the previous order-two checker; its source certificate hash remains enforced.

No modification of any earlier frozen package is required. The new third-section representative uses the same ordered monomial homotopy as the lower sections.

## Cubic section equation

Write A=A_eta, B=A_kappa, C=A_nu and

    s_i(h)=v+h xi_i+h² sigma_i+h³ tau_i,
    g_ij(h)=exp(-h A-h² B-h³ C) g_ij(0).

Here xi_i=t0 q_i+s_i^(1), with t0=z in the finite base chart and t0=1 at infinity, and sigma_i lies in G I². Inverting the exponential gives the exact order-three equation

    g_ij(0) tau_j - tau_i
      = A sigma_i + (B+1/2 A²) xi_i
        + (C+1/2(AB+BA)+1/6 A³)v.

For the mixed equation use the baseline infinity-to-finite isometry, the mixed logarithms, and the finite-side xi and sigma. All operator orders matter: both AB and BA are retained.

The action on the q component is evaluated with the full local pairing

    (Omega(P,q_i), Omega(E0,q_i), Omega(E1,q_i), Omega(E2,q_i))
      = (1, a0 lambda_i[0], a0 lambda_i[1], a0 lambda_i[2]),

where lambda_i r_E=1. In particular B_lambda xi and B_lambda A_eta v are not discarded because B_lambda v=0.

For each parameter coefficient, call the right-hand side y. Its plane boundary is exactly r f. The top Laurent projection of f is checked to vanish. Set zeta=Kf and tau=K(y-r zeta); the checker verifies the resulting plane equation and then every mixed equation modulo the actual relation. The exported tau has no D component, so its third-order pairing contribution is zero.

## Concrete lambda check

The coefficient of lambda in the third-section correction is nonzero even though the second-section lambda coefficient is zero. In finite X,Y,W patches it is respectively

    -2 z³ X^-3 E0,
    -2 z³ Y^-3 E0,
    -2 z (X+Y) W^-4 E0.

The infinity correction is zero. The four lambda times a,b,c,d section coefficients vanish in the chosen gauge. These are checked finite-order outputs, with no conclusion about later lambda dependence.

## Independent direct equation check

The constructor solves the positive-exponential equation above and checks 2,320 scalar identities/regularity conditions. A separate script does not import the constructor. It reads the exported sections and expands the original negative-exponential equation directly:

    delta tau - A(g sigma_j) + (1/2 A²-B)(g xi_j)
      + (-C+1/2(AB+BA)-1/6 A³)v = 0 in G.

It transports source-side lower sections using the actual completion transitions. On a plane overlap,

    g xi_j=t0 q_i+s_j^(1)+t0 w_ij;

on the mixed overlap,

    g xi_infinity=t0 q_finite+TB s_infinity^(1)+K_i.

This retains the baseline q shifts instead of substituting the already solved lower equations. All 40 coefficients pass all finite, infinity and mixed checks. The verifier changes the parsed finite X-patch origin E0 correction by z³/X³, recomputes the edge through the same equation function used by the positive checks, and rejects it with the exact nonzero quotient residual -z³/X³ on edge01. The direct checker records 1,442 checks.

Both scripts pass normally and with Python -O; stdout and all generated section receipts/coefficients agree byte-for-byte. Exact Fraction arithmetic is used, with no numerical sampling. Separate review independently derived the full noncommutative cubic exponential identity, inspected the implementation and audited all 1,874 exported terms for degree, character and regularity.

## Uniqueness with the middle gauge fixed

For every k≥1, H⁰(G I^k)=0. Indeed B I^k has filtration lines

    O(3,-3-k), O(0,-k), O(4,-4-k), O(3,-4-k),

whose H⁰ groups vanish. Also A I^k=O(3,-6-k) has H¹=0 by the product formula and the vanishing of H¹ of line bundles on P². The exact sequence 0→A I^k→B I^k→G I^k→0 gives the claim.

Consequently, with the middle transitions and lower section jet fixed, two regular kth corrections with the same prescribed kth pairing coefficient differ by H⁰(G I^k), hence coincide. This applies directly to the computed first, second and third corrections, including the nonzero prescribed first pairing. Different B representatives can differ by the line relation; different middle gauges are not identified by this uniqueness statement.

## Files and boundary

`THIRD_NORMAL_SECTION_CORRECTIONS.json` exports all 40 coefficients. `THIRD_NORMAL_SECTION_CHECKS.json` and `THIRD_NORMAL_DIRECT_EQUATION_CHECKS.json` contain the exact checks. `SHA256SUMS` freezes the package.

The next uncomputed finite-order input would be a full fourth-middle cochain and its quartic descent equations, followed by a separate section obstruction check. Neither follows from the present finite calculation alone.
