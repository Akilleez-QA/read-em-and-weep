> Historical mathematical record, 16 October 2026. Statements of PASS and check counts below refer to the original recorded verification, not a new execution. See PUBLICATION-SCOPE.md at the common series root for current scope, imported premises, and source/public hash bindings.

# Exact all-constant single-position kernel

## Statement

Work over Q with the authenticated perfect HM complex L in genuine degrees -1,0,1,2, let B=End(L), and use the specified global epsilon splitting

    W = H²(B(-3)) direct_sum H²(B(-4)) direct_sum H²(B(-5)),
    (G0,G1,G2) |-> aG0+aUG1+aU²G2,

where

    a=(X1Y2-X2Y1)(X3Y4-X4Y3),
    U=X1X2Y3Y4+Y1Y2X3X4,
    beta2=v2²-v1v3+2v0v4.

Let S_kappa evaluate all30 constant scalar maps at the single Laurent position

    kappa=(-1,-1,-3,-3).

These are the negative-block scalar rows and their indicated Laurent coefficient. S_kappa is not the positive detector ell(n,p)=p[7]-p[25], nor its pulled-back Phi assembled from78 staircase summands. This theorem supplies no restriction or evaluation of that different ell/Phi functional.

Then

    ker S_kappa
      = {(-v2 eta-beta2 zeta, eta, zeta):
          eta in H²(B(-4)), zeta in H²(B(-5))}.

Its dimension is12, and rank S_kappa on W is20.

Under the separately authenticated inversion action, the positive target is

    W+ = H²(B(-3))+ direct_sum H²(B(-4))+, dimensions8+4,

since H²(B(-5))+=0. Hence

    ker(S_kappa restricted to W+)
      = {(-v2 eta, eta, 0): eta in H²(B(-4))+}.

Its dimension is4 and the restricted rank is8. Every nonzero eta gives a nonzero class invisible to all30 single-position evaluations. In the global epsilon realization this class is a(U-v2)eta.

## Proof

A constant scalar row has freely chosen thirty beta_i,b coefficients and the determined coefficients

    alpha_a,5b+k = -sum_i beta_i,b gamma_i,a,k.

By the genuine-degree supertrace

    Str(FE)=-tr(F20 E02)+tr(F31 E13),

its corresponding global internal-degree+2 dual cycle has

    E13[b,i]=beta_i,b,
    E02[5b+k,a]=sum_i beta_i,b gamma_i,a,k.

These are exactly all cycles in the authenticated K30 graph. Modulo the complete incoming d5 image they span

    A0=H²(B(-2)), dimension20,

which is the Serre-linear dual of H²(B(-3)). No truncated positive complex is substituted for this quotient.

For q=X3²X4²Y1²Y2² and the homogeneous alternating discriminant Delta, the authenticated global trace identity gives

    Alt(q a(A+UB+U²C))/Delta = 4(A+v2B+beta2C).

This identity is independent of the constant matrix row. Thus for every constant scalar row represented by E, its single-position value on (G0,G1,G2) is

    4 <G0+v2G1+beta2G2, E>.

All twists agree: G0, v2G1 and beta2G2 belong to H²(B(-3)). Polynomial multiplication commutes with the full total differential. In particular, if E is a d5 boundary, multiplication must be applied to its complete total primitive; it gives a genuine boundary in the shifted complex. Hence these expressions depend only on the stated cohomology classes.

The E classes span the full Serre dual A0, so all thirty values vanish if and only if

    G0+v2G1+beta2G2=0 in H²(B(-3)).

Solving for G0 gives the displayed complete kernel. The map to H²(B(-3)) is surjective by taking G1=G2=0, so its rank is20. The kernel dimension is dim H²(B(-4))+dim H²(B(-5))=10+2=12.

The polynomials v2 and beta2 are inversion fixed, all three epsilon generators are inversion fixed, and the specified Serre pairing is equivariant. Restricting the same map to W+ therefore gives the surjection

    H²(B(-3))+ direct_sum H²(B(-4))+
       -> H²(B(-3))+, (G0,G1) |-> G0+v2G1.

Its rank is8 and its kernel is the graph eta |-> (-v2 eta,eta), dimension4. The second component proves this graph is injective regardless of the rank of multiplication by v2. Nonzero eta does not need a separately computed nonzero v2 eta.

## Comparison with the full-family theorem

The reviewed PR80 theorem establishes that all30 maps at all81 positions have zero kernel on W and on W+. The single-position result above identifies a precise obstruction to dropping the other positions without a new sufficient-subfamily proof.

On the same positive12 target:

- Four named maps h,j,p,r at kappa: rank4, kernel8.
- All30 constant maps at kappa: rank8, kernel4.
- All30 constant maps at all81 positions: rank12, kernel0.

None of these ranks evaluates the actual obstruction. The class a(U-v2)eta is a counterexample family to single-position completeness, not a claim that the actual obstruction belongs to it.

## Dependencies and review

The complete source authentication and conditional PR80 challenge are in AUDIT.md in this directory. The argument uses the already independently reviewed global epsilon generator/trace bridge, K30/d5 quotient, and inversion-positive dimensions. It introduces no elimination or source arithmetic.

The single-position graph and counterexample were independently checked by the separate leading-kernel review. That review confirmed the full-total-primitive multiplication requirement and the concrete primal family a(U-v2)eta.
