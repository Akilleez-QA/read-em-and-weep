Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

Supporting dependency only: this complete source text is not a fresh result of this packet.

# Small addendum: the exact quartic change caused by midpoint transgression

This bounded addendum refines only the parent proof’s Q4+C4 slot. All its M2, full covariant-adjoint correction, complete-normal-form families and evidence limits remain unchanged.

## Collected formula

Keep BL_ab=[L_a,L_b], BU_ab=[U_a,U_b], Delta_ab=d(U_a,L_b)−d(U_b,L_a), and the original R22 exactly as in the parent proof. For any X,Y write

    {ad_X,ad_Y}Z=[X,[Y,Z]]+[Y,[X,Z]].

Split the original R31 by current type. Its three-U/one-L part is

    R31^(3U)=(1/32)sum_((a,b),(i,j)){
                  [U_b,[L_a,BU_ij]]−[U_a,[L_b,BU_ij]]},

where the pair list is exactly ((1,2),(3,4)), ((3,4),(1,2)). Then

    Q4+C4 = R22 + R31^(3U) + R13_new,                    (A)

    32 R13_new = [L_1,[U_2,BL_34]]−[L_2,[U_1,BL_34]]
                  +{ad_L3,ad_U4}BL_12
                  −{ad_L4,ad_U3}BL_12.                 (B)

Thus the extra curvature changes only the two single-U assignments with U in slot 3 or 4. All six two-U/two-L sectors, all four three-U/one-L sectors, and the single-U assignments in slots 1 and 2 are unchanged. Both pure sectors remain zero. All fourteen mixed assignment maps remain nonzero as universal maps.

This asymmetry comes from the chosen flux, which differentiates in axes 1 and 2. It is not a new physical asymmetry or full-S4 projection.

## Direct proof and trace collection

The four signed complementary entries give exactly

    32 C4=[U_3,[BL_12,L_4]]−[U_4,[BL_12,L_3]].

The old single-U contribution in slots 3,4 was

    ([L_3,[U_4,BL_12]]−[L_4,[U_3,BL_12]])/32.

Adding these two expressions and reversing the innermost brackets gives precisely the last two terms in (B). No cancellation of R22 or the three-U part is involved.

Rank-two contraction gives the exact identity

    {ad_X,ad_Y}Z
       =4d(X,Y)Z−2d(X,Z)Y−2d(Y,Z)X.

Consequently the changed slot-3/4 part of R13_new can equivalently be written

    (1/16){d(L_4,BL_12)U_3−d(L_3,BL_12)U_4
             +d(U_3,BL_12)L_4−d(U_4,BL_12)L_3
             −2 Delta_34 BL_12}.                        (C)

The slot-1/2 terms in the first line of (B) remain intact. This is a compact quartic collection, not a universal cancellation.

## Explicit surviving coefficients

Use universal traceless coordinates (z,x,y), with bracket and trace structure constants as in the parent proof. In the z-coordinate of Q4+C4 the coefficients are

    coefficient of z_L1 x_L2 z_L4 y_U3 = +1/8,
    coefficient of z_L1 x_L2 z_L3 y_U4 = −1/8.

Both coefficients were zero in Q4 alone. They are introduced by C4. This proves that the two changed assignment maps remain nonzero and that the transgression genuinely changes their polynomial support rather than merely rescaling all of Q4. These are coefficients of universal formal polynomials, not evaluations or choices of physical current values.

## Checks and limits

check_quartic.py independently assembles the supplied full Q4 and C4, verifies (A)–(C) coefficientwise, projects all sixteen L/U multidegrees, and checks both displayed coefficients. Normal and optimized runs pass. The scalar-polynomial helper and baseline assembly are copied from the supplied rank-two checker; there are no physical source imports, jet evaluations, matrices, matrix-polynomial products or numerical experiments.

This author check does not establish actual source nonvanishing. It supplies no physical-cost, new domain, boundary or residue result. The complete expression still contains M2 and the nonconstant-kernel derivative; no other family has been removed.
