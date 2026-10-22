# Scalar N-W action has an exact full source companion

Executable assembly prerequisite: [PR741, immutable commit eace951d98b0c5adb0462cb2d93c09eac5b08b8b](https://github.com/Akilleez-QA/read-em-and-weep/pull/741), which contains the public PR698 source-balance foundation. The actual source/marking convention is the one in `FULL-U-CANCELLATION-GIVES-A-CONSTRUCTIVE-TWO-STAGE-C-DIVISION.md` and its public PR699 verifier.

## 1. An exact closed-input formula

Use the physical conventions of the public Clifford/source-balance foundation and `SUPPORTED-W-ACTIONS-HAVE-A-UNIFIED-FULL-EXTERIOR-ASSEMBLY.md`. Set

    j=i_w omega_W=(-w,u),       N=-2j (u,w).

For an arbitrary scalar coefficient s and positive polar covector r, take the supported VVW coefficient `s I_6 tensor N`. Let L_N(s,r) be its full skew exterior action, with the determinant adjoint retained. For **every closed two-form F**, meaning i_x F=0, the entire result is

    L_N(s,r) F = -4s (r·v) (i_v F_VV) wedge j.           (1)

Proof: the unified assembly has tr(N)=0 and K=sI, hence its primitive in W slot j is `2s E_r sum_i N[j,i]Y_i`. Since N=-2j w^t and closure gives sum_i w_iY_i=i_v F_VV, this primitive is

    -4s r wedge (i_v F_VV) wedge j.

Contraction by i_x gives (1): i_w j=0 and i_v²=0. No coefficient derivatives or hidden source corrections enter this multiplication identity.

The verifier checks (1) with an arbitrary20-coefficient three-form contracted by i_x, all positive polar coefficients free. This covers the actual monad columns, which are supplied as such contractions.

## 2. Complete U balance and the retained c column

The a column has i_v A=0; the b column has no VV part. Therefore

    L_N(s,r) A=0,          L_N(s,r) B=0                  (2)

as full exterior identities. No Euler repair or U-source correction is required for this addition. On the actual c column C,

    L_N(s,r) C=-4s (r·v) (i_v C_VV) wedge j.             (3)

In particular it has zero VV principal component but generally a nonzero mixed component. A principal-c screen alone cannot determine this contribution. Formula (3), rather than an inference from the principal quotient, is the required full companion.

The actual c-column scalar c_m multiplies (3), and any common Atiyah scale k_At and formal probe multiply the whole operator and its column together. Equations (1)–(3) use normalized columns only; they do not assign those nonzero physical scales values.

## 3. The two polar branches

For the fixed physical polar

    r=(y/(2theta),x/(2theta),z/theta),

one has r·v=q0=(xy+z²)/theta. Thus the q-polar branch of (3) is explicitly divisible by q0, with its displayed regular quotient.

For the H-polar r_H=Hr, define h_H=r_H·v. The positive trace-free H gives a harmonic quadratic h_H, not a multiple of q0 unless H=0. Now let

    Delta_D=tr(D²)/2=h²+kl,
    D=[[h,k],[l,-h]],

and choose the invariant scalar s=Delta_D. This is a permitted equivariant coefficient in the complete traceless-W family. Its exact c companion is

    -4 Delta_D h_H (i_v C_VV) wedge j.                  (4)

It vanishes on every square parameter direction, since D²=Delta_D I and the corresponding binary quadratic is square exactly when Delta_D=0. No specific direction is selected.

For generic formal D and nonzero H, (4) is nonzero even as a **raw c-column modulo q0**. Indeed the actual cubic marking is invertible, so C_VV=−f(ell z) is nonzero and independent of the positive coordinates for a nonzero c input. Positive contraction is injective on such constant positive two-forms, so some coefficient of i_v C_VV is a nonzero positive linear form. Over the field of negative/frame coefficients, q0 is irreducible of rank3, cannot divide that linear form, and cannot divide the nonzero harmonic quadratic h_H. Thus it cannot divide their product. This is a polynomial-domain proof, with no source evaluation or matrix/rank scan.

This last observation concerns the raw column, **not** its quotient by allowable source modifications and not a Bockstein value. Nor is this direction asserted independent of the current140 operators on the monad. It is an explicit fully U-balanced candidate whose remaining c companion is now known exactly.
