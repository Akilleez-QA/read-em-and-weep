# The surviving scalar row is impossible: whole source127 h-b-f exclusion

## Statement and exact dependency

The entire original source edge

    G3.11.cce6e3ba4eeb, source_index127,
    (0,1,0,0,0,1,0,1),
    E=(P+D) O(-2)+T O(-3)+O(-8)+O(-10),
    A_q=O(-8)+O(2)+O(16),
    B_q=O(-18)+O(-4)+O(6), original defect zero

is impossible. This closes the sole scalar-row branch of the pinned reduction, not just its scalar-zero subcase. No stable-label exclusion or global frontier count is asserted here.

The exact reduction used is PR885, commit

    53939364de5459822be1a32be08f2b12dbbb4280,

at the immutable source:

https://github.com/Akilleez-QA/read-em-and-weep/blob/53939364de5459822be1a32be08f2b12dbbb4280/research/hm/profile11-source127-hbf-kernel-reduction/PROOF.md

Its exact proof SHA256 is 3e3a994defbeea2cefff4b0a64a93f70e0059417f8850a79d85069c1d45ab169. This closure uses its complete branch reduction and exact remaining interface, not a presumed whole-source exclusion. The original actual presentation, strict-top theorem and both original catalogs are separately pinned at db51525015bb7c5e825833d550d08dedf6f6ea96 in the accompanying five-input manifest. The verifier checks all five immutable Git blobs and the reduction's exact proof hash before the fixed character calculation.

No selected actual HM/source coefficient, parameter, point, derivative value, matrix, rank, model, scan or large computation is used. The new step is a small equivariant cohomology obstruction after a proved saturation bound.

## 1. Exact geometry of the remaining branch

Retain the notation of the reduction. The only remaining possibility has F=P O(-2), actual first span M=(Wp+T) O(-1), full constant span C=V+P+D of dimension twelve, and N=E intersect M. Its actual saturated first span Y=N^+ satisfies

    M/F=P O,
    Y/M=W O(-3)+O(-6),
    rank Y=11, deg Y=-20,
    C O/Y=O(20),
    E^+ intersect C O=Y.                         (1)

The O(4) row of Y in A2=E^+/E vanishes. The negative O(-6) row vanishes on M and W O(-3), and is a nonzero scalar on the O(-6) summand of Y/M. Its high row is onto L=O(18), already on M. These are actual maps of bundles, as established in the endpoint-specific reduction.

Let Y0 be the kernel of that negative row on Y. The nonzero equal-degree scalar is an isomorphism, so Y0 is saturated in Y and C and

    Y0/M=W O(-3),
    rank Y0=10, deg Y0=-14.                       (2)

Put X=E intersect C O. Since E^+ intersect C=Y, X is the kernel of the actual map Y->A2. By (1)-(2) it is exactly the kernel of the onto high row Y0->L. Therefore

    0 -> X -> Y0 -> O(18) ->0,
    rank X=9, deg X=-32.                          (3)

In particular no negative row has been dropped: taking its actual kernel creates Y0 before (3) is used.

## 2. A forced positive rank-two quotient

The quotient V0=C O/Y0 has rank two and degree fourteen. It is globally generated, as a quotient of a constant bundle. Moreover H0(V0*)=0: a constant linear functional annihilating Y0 would annihilate F, whose full constant span is C. Thus every ordinary splitting degree of V0 is strictly positive.

The exact sequences and M=(Wp+T) O(-1) give

    chi_G(V0)=C-chi_G(M)-chi_G(W O(-3))
             =1+A+V+P+D.                        (4)

There are only five possible center-even positive equivariant rank-two splittings of degree fourteen. Their Euler characters are

    W O(7):             V+2P+D;
    Wp O(7):            1+A+V+P+D;
    O(2)+O(12):         1+2A+P+D;
    O(4)+O(10):         A+V+2D;
    O(6)+O(8):          V+2P+D.

This list is exhaustive: a rank-two irreducible coefficient is W or Wp at the common odd degree seven; otherwise both coefficients are trivial, with positive even degrees summing to fourteen. There are no nontrivial one-dimensional characters. Equation (4) forces

    V0=Wp O(7).                                   (5)

The image U0=C O/X in Q is an actual rank-three vector bundle, and (3)-(5) give

    0 -> O(18) -> U0 -> Wp O(7) ->0.

This extension splits equivariantly because H1(Wp O(11))=0 and taking invariants is exact. Hence

    U0=O(18)+Wp O(7), rank U0=3, deg U0=32.        (6)

At this stage U0 is not assumed saturated in Q.

## 3. The possible degree-twelve saturation defect is impossible

The injection U0->Q and the projection Z0=E/X->(H/C) O have the same cokernel H O/(E+C O). Thus their saturation defects have the same length delta. Here

    rank Z0=8, deg Z0=-22, dim(H/C)=18.

The saturation Z spans H/C because E spans H. Its degrees are nonpositive, so

    h0(Z*)=8+22-delta >=18.

Consequently 0<=delta<=12. The defect divisor is invariant. The minimum positive invariant degree is twelve, so delta is either zero or twelve.

If delta=12, let U be the saturation of U0 in Q. Then U has rank3 and degree44, and R=(Q/U)* has rank10 and degree-10. Since H0(Q*)=0, every degree of Q* and its subbundle R is at most minus one. Thus R is pure degree minus one and h0(R(1))=10. Original strict-top injects H0(Q*(1)) into

    H0(B_q(1))=Sym7 W=Wp+T,

of dimension eight. The inclusion R subset Q* contradicts this dimension bound. Hence delta=0: the actual U0 in (6) is saturated in Q.

## 4. The original twist-one character gives a contradiction

Now put R=(Q/U0)*. There is an exact sequence

    0 -> R -> Q* -> O(-18)+Wp O(-7) ->0,
    rank R=10, deg R=-22.                         (7)

All degrees of R are at most minus one. The original actual presentation is

    0 -> Q* -> M3* O(-1) -> M2* O ->0,
    M2=A+2V+3P+4D,
    M3=3Wp+3S+6T.

All irreducibles are self-dual. Using H0(Q*)=H0(U0*)=0 in (7), the exact cohomology sequence gives

    H1(R)=M2-Sym16 W-Wp Sym5 W=V+P+D.             (8)

At twist one, Euler characteristics give the stronger independent constraint

    chi_G(R(1))=M3-M2 W+Sym15 W+Wp Sym4 W=-W.     (9)

The following small support argument shows that (8) and (9) are incompatible. For a degree-at-most-minus-two atom B O(-j), its H1 contribution to (8) is B Sym^(j-2) W, which must be a subcharacter of V+P+D. Its dimension is (j-1)dim B<=12, and center parity fixes the parity of B. The complete possible atoms are

    V O(-2), P O(-2), D O(-2),
    Wp O(-3), T O(-3),
    V O(-4), P O(-4),
    Wp O(-5), O(-6), W O(-7), O(-8), O(-10).     (10)

For completeness, at j=2 only V,P,D fit. At j=3 only Wp W=P and T W=V+P+D fit. At j=4 the allowed products are V A=P+D and P A=V+P+D. At j=5 only Wp S=V+D fits. At j=6 only the scalar contributes D. At j=7 only W T=V+P+D fits; Wp T contains A. At j=8 and10 the scalar contributions are V+P and P+D. Odd j>=9 exceed the dimension budget; at even j=12 the scalar already contains the forbidden A, and all larger j exceed the budget. This proves exhaustiveness without enumerating any actual source instances.

None of the atoms (10) contributes W to H1(R(1)). The degree-minus-two atoms are acyclic at twist one; the remaining contributions, in the displayed order, are

    Wp, T, T, Wp+T, T, S, S+T, T, Wp+T,

all W-free. The possible degree-minus-one coefficient contributes only to H0(R(1)), with nonnegative multiplicity of W. Therefore the W coefficient of chi_G(R(1)) is nonnegative. Equation (9) says it is minus one, a contradiction.

This eliminates the exact scalar-nonzero branch retained by the pinned reduction. Together with that independently verified reduction it excludes the entire displayed source127 h-b-f edge. It does not assert a whole-label exclusion or actual HM realization of any other abstract construction.
