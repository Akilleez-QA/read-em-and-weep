# Actual third obstruction as a secondary multiplication tensor

## New actual reduction

Write M_j=H1(P4,B(j))_+, V=M_2, U=M_4, K=ker(q0:V->U), P=coker(q0:V->U), and C=coker(q0:M_0->V). All multiplications below are in the actual ambient cohomology module.

The proved cone multiplication theorem has a stronger ambient consequence than the existence of the particular third correction:

    h V is contained in q0 V for EVERY h in D5.                 (1)

Indeed restriction V->H1(B_Q0(2)) and multiplication commute. The product by h is zero in H1(B_Q0(4)) by POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md. The kernel of U->H1(B_Q0(4)) is exactly q0 V by the restriction long exact sequence. Surjectivity of the lower restriction is not needed.

There is consequently a canonically defined actual tensor

    Psi: A tensor D5 tensor C -> P,
    Psi(a,h,[x])=[a v], where q0 v=h x.                          (2)

In particular the third computation can be made on a fixed lower cokernel, instead of making a separate correction choice for each h and a. Formula (2) is not a tensor determined by the cone square ideal alone: q0 division takes place in the actual ambient module and retains its normal extension.

## Independence checks

Existence of v follows from (1). If v is replaced by v+k with k in K, the output changes by [a k]=0, exactly the proved first-Bockstein vanishing.

If x is replaced by x+q0 y, with y in M_0, then v can be replaced by v+h y. The change of output is [a h y]=[h(a y)]=0 by (1), since a y lies in V. Thus (2) descends to C. These are distinct checks; the second is not supplied just by first-Bockstein vanishing.

All operations are linear, and the choices disappear, so Psi is G-equivariant. It is a genuine secondary multiplication operation of the actual module. No choice of a splitting of q0 or of a quintic generator is part of its definition.

The same construction permits any positive quadric b in place of a, because (1) also kills b K (and q0 obviously does). In that case the result is identically zero: b v belongs to q0 V. Hence the secondary operation in its first argument factors through the negative quadratic summand A, not through the full space of even quadrics.

## Exact application to the actual cubic gate

Set t(a)=[a zeta_a] in C, using the canonical actual orbit class zeta_a. The actual third correction equation is q0 v=a h zeta_a=h(a zeta_a). Thus

    beta3_a(h xi)=Psi(a,h,t(a)) modulo im beta2_a.               (3)

The sign relative to the square-shadow class theta_a=-t(a) is correspondingly negative. No sign convention affects vanishing.

The quadratic lower class t is a G-map Sym^2 A->C. Its invariant component vanishes because C=V+3P4+3D5 has no trivial constituent. Therefore (3) probes Psi only on the particular actual D5-valued quadratic family t, not on an arbitrary point of the thirty-dimensional C. The nonzero square-boundary image of t is known; injectivity of Psi on that image is NOT proved.

## Dual certificate with no correction vector

Choose an orientation of A and P. Let lambda_a in P* be the exterior product of the three actual second-symbol columns; it is polynomial of degree six in a and nonzero off the known degeneration scheme Z. Regard it also as a covector on U annihilating q0 V.

The covector v -> lambda_a(a v) on V kills K by beta1=0. It therefore descends uniquely to a covector eta_a on q0 V, characterized by

    eta_a(q0 v)=lambda_a(a v).                                  (4)

Equations (1) and (4) give the correction-free scalar certificate

    T(a,h)=eta_a(h a zeta_a).                                   (5)

It is homogeneous of degree nine in a and linear in h, and equals lambda_a applied to the actual cubic representative. Off Z, T vanishes exactly when the actual third quotient vanishes. Any extension of eta_a from q0 V to U gives the same value in (5); the difference annihilates q0 V, where its argument lies. A fixed linear section of q0 makes eta polynomial of degree seven, so (5) is globally polynomial, including Z. Scaling orientations only rescales this certificate.

Thus either computing Psi on the actual Atiyah-derived D5 family, or computing the dual normal lift (4), is sufficient. Neither may be replaced by a cone-only square-ideal calculation without proving compatibility with the actual normal extension.

## Scope

This proves a new actual ambient divisibility statement (1), a canonical secondary tensor on the entire lower cokernel, its positive-argument vanishing, and the exact actual third formula (3). It does not determine either of the two third-channel coefficients, improve the finite Smith bound, or prove generic maximal rank. No actual coefficients, actual matrix evaluations, rank tests are used.

## Dependencies and reproduction

- [Actual square filtration and D5 multiplication vanishing](POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md).
- [First Bockstein vanishing](POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md).
- [Actual second scalar nonvanishing](ACTUAL-SECOND-BOCKSTEIN-NONZERO-BY-ATIYAH-QUINTIC.md).
- [Third-channel and square-direction gate](THIRD-BOCKSTEIN-POLARIZATION-AND-SQUARE-DIRECTION-GATE.md).

Run `python verify_positive_third_secondary_tensor.py` for the universal polynomial identities. Its passing result checks the stated algebraic bookkeeping, not the geometric inputs or actual third nonvanishing.
