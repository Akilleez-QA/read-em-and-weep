# Eliminate quadratic and undifferentiated scalar primitives from the HM pairing

## Checked result and scope

The transition-only lift permits a stronger reduction than transposing a generic quadratic circuit. The full-sign obstruction has a closed trace-free representative whose dependence on the scalar solutions is **linear and only through complementary first derivatives**. Neither scalar solution nor their product need be materialized to pair this representative with an authenticated finite detector.

This is a symbolic identity, not a numerical evaluation or an executable complexity certificate. No physical polynomial values, residuals, samples, jets, partition expansions, or source coefficients were generated.

The formula inputs below are pinned at commit `08b73637d4136f91606aad332c46cafd064417f8`, particularly [source-formulas.js](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/data/source-formulas.js), `crossResidual` and `globalCross`; the transition-only proof fixes the actual scalar solver and common-cover ordering.

## 1. Conventions

Let p=(1,2), q=(3,4). All formulas use physical determinant-one row transitions and their actual invariant vector-field derivatives. On an increasing common-cover triple i,j,k, put

- A=g_ij, B=g_jk, G=g_ik=BA;
- C_p=G^(-1) mu_p(B,A), c_p=tr(C_p)/2;
- b_p=(15/4) q_(1,ij) q_(2,jk), and F_p=b_p-c_p;
- K_p=mu_p(g^(-1),g), k_p=-K_p/2;
- x_p=s_p I+k_p, u_p=g x_p, with delta s_p=F_p.

For row-End cochains, delta k=A^(-1) k_jk A-k_ik+k_ij. Write kbar_p=A^(-1) k_p,jk A.

The identity delta K_p=2C_p-tr(C_p)I implies

    delta k_p=-C_p^0,      C_p^0=C_p-c_p I.

Each k_p is traceless. Indeed with L_a=g^(-1)V_a(g), differentiation of the inverse gives

    K_p=(-L_a L_b+L_b L_a)/2,
    k_p=[L_a,L_b]/4.

All appearances of inverse and derivative here are symbolic source identities, not computed values.

## 2. Precisely specified baseline

Let M(s_p,s_q) be G^(-1) times the pinned `globalCross` residual, evaluated formally using u_p=g(s_p I+k_p), u_q=g(s_q I+k_q).

Let M0 mean that SAME `globalCross` expression with u_p^0=g k_p and u_q^0=g k_q. In particular M0 includes

    -b_p k_q,ik - b_q k_p,ik - b_p b_q I.

M0 is only a baseline expression. Its chosen first transitions need not solve the first-order equation, and M0 is not asserted to be closed.

If instead a baseline is taken from `crossResidual` BEFORE the gerbe subtraction, replace the two +F k corrections below by (F-b)k=-c k. This distinction prevents a missing-gerbe-term error.

## 3. Exact derivative operator

For p=(a,b), define the traceless currents

    L_d=A^(-1)V_d(A),
    U_d=A^(-1)B^(-1)V_d(B)A.

For a scalar edge cochain t, define the matrix triple cochain

    E_p(t)=1/2 [
       (V_a t_jk)L_b - (V_b t_jk)L_a
       + (V_b t_ij)U_a - (V_a t_ij)U_b
    ].

This comes directly from the product rule in

    G^(-1)[mu_p(B t_jk,A)+mu_p(B,A t_ij)].

The undifferentiated part is (t_jk+t_ij)C_p. Since det(A)=det(B)=1, all L_d,U_d and E_p(t) are traceless. The argument uses the physical derivative, so it does not discard line-frame derivatives.

## 4. Exact trace-free identity

Put W=s_q k_p+s_p k_q as an edge cochain. Then

    M(s_p,s_q)^0
      = M0^0 - delta W
        + F_q k_p,ik + F_p k_q,ik
        + E_p(s_q) + E_q(s_p).                     (1)

Here superscript 0 means X-tr(X)I/2, not evaluation at zero.

For the terms involving s_q and k_p, subtracting the baseline gives

    s_q,jk k_p,ij + s_q,ij kbar_p
        +(s_q,jk+s_q,ij) C_p^0.

Substitute C_p^0=-(kbar_p-k_p,ik+k_p,ij). This becomes

    -s_q,jk kbar_p-s_q,ij k_p,ij
        +(s_q,jk+s_q,ij)k_p,ik
      = -delta(s_q k_p)+(delta s_q)k_p,ik.

This proves the first correction in (1); exchange p and q for the second. The derivative terms are precisely those in section 3. All quadratic s_p s_q terms are scalar and therefore have zero trace-free projection. Scalar gerbe terms likewise have zero trace-free projection. The gerbe terms involving k already belong to M0 and cancel in the difference.

As an independent full-matrix check, with Q=s_p s_q I+W one gets

    M(s_p,s_q)-M0
      = -delta Q + F_q k_p,ik + F_p k_q,ik
        + (b_p b_q-c_p c_q)I + E_p(s_q)+E_q(s_p).

Taking trace-free parts recovers (1); see also `hm-scalar-pairing-elimination-audit.md` and `scalar-reduction-root-check.md` for the baseline convention.

## 5. Why removing the central part preserves the actual class

The actual first lifts solve the prescribed first-order problem. Consequently the actual full-sign normalized residual M(s_p,s_q) is a closed End(E) Cech 2-cochain, by the pinned [closure and characters proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/closure-and-characters.md).

In characteristic zero, the invariant decomposition

    End(E)=O I direct-sum End_0(E)

is a Cech chain splitting: conjugation preserves trace and fixes I. Hence its central and trace-free parts are separately closed.

The full-sign scalar character on Y=(P1)^4 is O(-2,-2,-2,-2), the same character/twist convention used by the existing full-sign cover transport. Each O(-2) has tensor Cech harmonic space only in degree 1. Their fourfold tensor product therefore has scalar cohomology only in degree 4. In particular

    H^2(O_X)_full-sign = H^2(Y,O(-2,-2,-2,-2)) = 0.

Thus the entire central component of the ACTUAL CLOSED residual is exact. This argument does not discard arbitrary individual central summands of the nonclosed baseline.

It follows that the cochain

    Rsharp = M0^0 + F_q k_p,ik + F_p k_q,ik
                    + E_p(s_q)+E_q(s_p)              (2)

is closed and represents the same full-sign obstruction class: by (1), it equals M(s_p,s_q)^0+delta W. Closedness follows from this equality and delta^2=0, not from an assertion that its individual summands are closed.

## 6. Direct linear pairing without constructing s

Write the authenticated transition-only solver, separately in each pair character, as

    T = H_rho + R K_cov Pi + R A h S Pi,
    s_p=T_p F_p, s_q=T_q F_q.

R denotes pullback from the standard product cover to the common refinement. A,S,h,K_cov,Pi,H_rho are exactly the fixed maps of the transition-only note; its source-first common-vertex order remains mandatory.

Let Lambda be any authenticated linear detector applied to the new common-cover representative (2). Define multiplication operators

    B_q(f)_ijk=f_ijk k_q,ik,
    B_p(f)_ijk=f_ijk k_p,ik.

Ordinary algebraic transposes, with coefficient and cochain signs retained, give the exact formula

    Lambda(Rsharp) = Lambda(M0^0)
      + < B_q^*Lambda + T_p^* E_q^*Lambda, F_p >
      + < B_p^*Lambda + T_q^* E_p^*Lambda, F_q >.   (3)

There is no T_p tensor T_q term. This is the concrete improvement over the generic bilinear-primitive proposal.

The solver transpose is fully specified by reversing the known maps:

    T^* = H_rho^* + Pi^* K_cov^* R^*
                     + Pi^* S^* h^* A^* R^*.

The full transpose of h includes its A/B/C state filters and Koszul signs; it is not just the harmonic projection P. All three scalar-primitive summands are retained.

Equation (3) is conditional on authenticating Lambda on this refined source. It does not assert that the old four-tail circuit, 781 mask features, or three old Laurent slots already provide that authentication. The existing detector can be transported to this cover, but its regularity and coefficient demand must be specified for this representative.

## 7. Exact coefficient demand and derivative accounting

After an owned-denominator regularization has made a requested local summand Laurent-polynomial, a coefficient request has an exact finite adjoint rule. For finite Laurent supports, a multi-index kappa, and one coordinate i,

    [x^kappa](w partial_i f)
      = sum_nu (kappa_i-nu_i+1) w_nu f_(kappa-nu+e_i).

Only nu in the certified support of w and kappa-nu+e_i in the certified support of f are needed. Terms with zero displayed scalar factor may be removed. A local scalar vector-field coefficient a is included in w as w a; it is not silently declared constant.

Equivalently, using the formal residue pairing Res(w f dx_1...dx_4),

    (a partial_i)^*w = -partial_i(a w).

Hence transposing derivatives does NOT erase derivatives of partition weights: it moves them onto the exact adjoint kernel. If frame-stripped differentiation has an additional zero-order term, its transpose must be included as well. Using the exact source derivative nodes avoids confusing partial_i with V_i.

For the scalar solver's Pi and h components, compose these requests with the already proved N14 finite-demand equation

    p_i + sum_(finite rows l) a_(l,i)
        - sum_(infinity rows l) a_(l,i) - m_i = kappa_i,

and with the explicit A/B/C filtering of h. The H_rho and K_cov components must be propagated too. The quotient formulas in the finite-demand note cancel the inserted carrier and legal denominators termwise; no inverse power series is legitimate or necessary.

For remaining rational factors, finite Laurent support is not automatic. First supply the actual owned-denominator cancellation certificate for the requested regularized summand. In particular, differentiating P/D means the exact numerator identity (partial_i P)D-P(partial_i D) over D^2 unless a separately proved cancellation is used. This prevents the direct-pairing formulation from hiding the same denominator-normalization cost that defeated earlier circuits.

## 8. Remaining implementation obligations

An implementation must supply all of:

1. A frozen refined-cover linear detector Lambda and regularity comparison for the closed Rsharp; no automatic reuse of the old four-tail/mask circuit.
2. A source DAG for M0^0, F_p, F_q, k_p, k_q and the currents, using the whole-current trace simplification where independently available.
3. Backward demands for B^*Lambda and E^*Lambda, then for all three terms of T^*. This is a linear demand problem per pair, with no scalar-primitive product convolution.
4. Explicit denominator ownership, derivative rules, finite exponent predicates, cancellations and common-subexpression reuse. Propagate metadata only.
5. A full count of nonconstant products and a peak live-byte schedule including exact coefficient widths and runtime/scratch overhead. The mathematical reduction alone supplies no implementation complexity bound.

The reduction establishes a smaller mathematical target. It does not certify a practical implementation, a storage bound, or a value of the obstruction.

## Dependency scope

Companion references are identified by basename. A referenced file not supplied with this collection is an external prerequisite, not an embedded proof or a verified relative link. The reading order and unresolved conditions are listed in `proof-notes-index.md`. Reported test results describe the source audit; this proof copy does not by itself constitute a new test run.
