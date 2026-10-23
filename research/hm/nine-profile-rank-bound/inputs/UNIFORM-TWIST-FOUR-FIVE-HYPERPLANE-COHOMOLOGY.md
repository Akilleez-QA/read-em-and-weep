# Exact twist-four and twist-five hyperplane cohomology

Let H run through every actual hyperplane in the negative pencil, including the twelve double-plane parameters. Write B_H=End_0(F_H), T=P(W*), and pi:X->T for the universal hyperplane. All parity labels use the actual HM inversion.

## Theorem

For every H the cohomology dimensions, listed as (even,odd), are

    H0(B_H(4)) = (17,3),      H1(B_H(4)) = (0,5),
    H0(B_H(5)) = (46,17),     H1(B_H(5)) = (0,0).

In both twists all cohomology of degree at least two vanishes. These are uniform fiber statements, so the corresponding direct images are vector bundles with base change at every parameter.

Besides the already proved quotient

    48 O_T -> C_lin(2) -> 0,

there is a second everywhere-surjective actual plane boundary

    30 O_T -> D_lin(1) -> 0,                         (1)

where

    0 -> 41 O_T(-1) -> 54 O_T -> D_lin -> 0.          (2)

Thus D_lin has rank 13 and degree 41, D_lin(1) has degree 54, and the kernel of (1) is the actual even section bundle E4,+ of rank 17 and degree -54. No splitting of either quotient or kernel is asserted.

## 1. Higher cohomology in twist four

Use the actual section curve C and the same residual chain as in SURJECTIVE-PLANE-BOUNDARY-BY-CONIC-RESIDUALS.md. At ordinary parameters this is residual successively by the three distinct conic planes; at a special parameter it is the exact z,x,x chain for the actual conic plus Ferrand double. No new section or ribbon specialization is needed.

For I_C^2(7), the twists in that proof decrease from (8,7,6) to (7,6,5), and the last residual is I_C(4). At ordinary parameters the plane traces, after removing the square of the own-conic equation, are

    I_Z1^2 I_Z2^2(3),
    I_Z1   I_Z2^2(2),
    I_Z1   I_Z2  (1).

At the special parameters they are

    I_T^2(3),       I_Z^2 I_T0(2),       I_Z I_T0(1),

where T is a complete intersection of two plane quadratics. Every displayed plane sheaf has H2=0: for the ideals of finite schemes this follows from the nonnegative twist of O_P2, and for I_T^2(3) it follows either the same way or from its complete-intersection square resolution. All have H3=0 by support dimension. H1 need not vanish and is not discarded.

The actual primary positive-twist cohomology gives H2(F_H(3))=H3(F_H(3))=0. This uses only the ambient positive-twist higher vanishings in

    0 -> F(2) -> F(3) -> F_H(3) -> 0.

The section sequence

    0 -> O_H(1) -> F_H(3) -> I_C(4) -> 0

therefore gives H2(I_C(4))=H3(I_C(4))=0. Chasing the three residual exact sequences proves H2(I_C^2(7))=H3(I_C^2(7))=0. Finally

    0 -> F_H(3) -> B_H(4) -> I_C^2(7) -> 0

gives

    H2(B_H(4))=H3(B_H(4))=0.                         (3)

This does not require a new ambient adjoint multiplication rank or higher-cohomology assertion.

## 2. Euler characteristic and parity

For the normalized restriction, c1(F_H)=-H and c2(F_H)=4H^2, so

    ch(B_H)=3-15H^2,
    chi(B_H(t))=3 binomial(t+3,3)-15(t+2).

In particular chi(B_H(4))=15 and chi(B_H(5))=63.

The preceding plane-boundary theorem proves every higher cohomology group of B_H(5) zero. Its relative plane sequence and the known odd twist-four section bundle A O_T(-5) give h0(B_H(5))_+=48-5+3=46. Thus h0(B_H(5))_-=63-46=17.

Since all sections and cohomology of B_R(5) are inversion-even, the odd part of the plane sequence identifies

    H0(B_H(5))_- = H0(B_H(4))_+

up to its one-dimensional odd normal-coordinate factor. Therefore h0(B_H(4))_+=17. The previously proved square bundle gives h0(B_H(4))_-=3. Combining (3) with chi=15 shows h1(B_H(4))=20-15=5. Its already identified odd part is the rank-five fiber of C_lin(1), so the even part is zero.

Importantly, H1(B_H(3))_- has dimension 13, not zero. Its vanishing is neither used nor claimed.

## 3. The second actual plane quotient

The odd block of the actual universal ambient multiplication in twist three is (2): its kernel is zero because H0(B_H(3))_-=0 at every parameter. Its cokernel is D_lin=(R1 pi_*p*B(3))_-, a rank-13 vector bundle. The ambient H2(B(2))=0 is the established primary-to-adjoint input identifying this cokernel with the actual R1, as in EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md.

The relative plane sequence in twist four is

    0 -> p*B(3) tensor pi*O_T(1)
      -> p*B(4) -> B_R(4) external-tensor O_T -> 0.

The normal line reverses parity. Taking its even direct-image sequence and using H0(B_H(3))_-=0 and H1(B_H(4))_+=0 yields

    0 -> E4,+ -> 30 O_T -> D_lin(1) -> 0.            (4)

This is the claimed actual interpolation quotient, not a map specified only by dimensions. The remaining section bundles satisfy

    E4,- = A O_T(-5),
    E5,- = E4,+(1),
    0 -> A O_T(-4) -> E5,+ -> G -> 0,

where G=ker[48 O_T -> C_lin(2)]. Their ranks and degrees are

    E4,+: (17,-54),       E4,-: (3,-15),
    E5,+: (46,-48),       E5,-: (17,-37).

The two surjective plane boundaries still do not decide whether the actual divided-difference or Hermite smoothing vectors lie in their respective kernel bundles. No generic or special smoothing rank is inferred.

## Dependencies

- SURJECTIVE-PLANE-BOUNDARY-BY-CONIC-RESIDUALS.md: the full residual chains and twist-five vanishing.
- TORSION-FREE-HYPERPLANE-AND-QUADRATIC-TARGETS.md: C_lin is a vector bundle and all fiber base changes hold.
- EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md and UNIFORM-HYPERPLANE-LOWER-VANISHING-AND-JUMP-BOUND.md: actual parity, square bundles, and ambient cohomology blocks.
- verify_conic_residual_interpolation.py: universal residual-degree, formal regular-pair colon, and Euler/bundle-numerics checks. This verifier does not substitute for the geometric hypotheses proved in the cited artifacts.
