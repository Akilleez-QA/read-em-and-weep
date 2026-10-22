# A dual fourth certificate with the second image normalized away

## Result and scope

The actual third Bockstein is zero. On the open parameter set where beta2 has rank3, the fourth D5 obstruction can be tested by TWO actual dual divisions and one prescribed normalization. No fourth value is computed here. The construction retains the required nonzero third lifting correction through its normalization; it does not discard that correction.

Use the actual ambient vector spaces V=M2 (dimension41), U=M4 (dimension37), q=q0:V->U of rank33, and K=ker q=(A+D5)xi. Multiplication by a gives a:V->U. Let lambda_a be the degree-six cofactor covector on P=coker q, viewed also on U, annihilating im(beta2_a). It is nonzero off Sigma.

## 1. Two dual divisions

The first-Bockstein vanishing gives aK contained in qV. Thus

    eta_a(qv)=lambda_a(av)                          (1)

defines a functional on qV. This is the same first dual division as in POSITIVE-THIRD-SECONDARY-MULTIPLICATION-TENSOR.md.

Let S_a be the span in U of the three actual vectors a b zeta_a, with b in A. Their classes modulo qV are beta2_a(b). On the rank3 open set,

    dim S_a=3,    S_a intersect qV=0.

There is consequently a functional phi_a on U with

    phi_a|qV=eta_a,    phi_a|S_a=0.                 (2)

Since qV+S_a has dimension36, any two such phi_a differ by a scalar multiple of lambda_a.

For any g in A+D5,

    phi_a(a g xi)=phi_a(q g zeta_a)
                =eta_a(q g zeta_a)
                =lambda_a(a g zeta_a)=0.          (3)

The last equality is the second-symbol annihilator property for g in A and the actual beta2(D5)=0 for g in D5. Hence phi_a a kills K, and a SECOND dual division is defined by

    rho_a(qv)=phi_a(av).                           (4)

Only rho_a on qV is needed.

## 2. The exact fourth value

Choose the canonical-probe corrections

    q v_h=a h zeta_a,
    [a v_h]=beta2_a(b),
    q w_h=a(v_h-b zeta_a).

The existence of the unique polynomial b is the proven third-vanishing factorization. The fourth scalar is

    lambda_a(a w_h)
       =eta_a(a(v_h-b zeta_a))
       =phi_a(a v_h)-phi_a(a b zeta_a)
       =rho_a(q v_h)
       =rho_a(a h zeta_a).                        (5)

The second term was removed by the prescribed normalization(2), not by claiming that b vanishes. Thus(5) provides a normalized dual certificate: b is encoded by the three normalization conditions in(2), not omitted.

If phi_a is replaced by phi_a+c lambda_a, equation(4) changes rho_a by c eta_a. Its change in(5) is

    c eta_a(a h zeta_a)=c lambda_a(a v_h)=0,

exactly the already proved actual third vanishing. Therefore the value in(5) is independent of the remaining affine choice in phi_a. It also does not depend on the choice of v_h or w_h, by(1)-(4) and the standard second-image quotient.

## 3. Parameter degree and exceptional fibers

With lambda of degree6, eta has degree7, phi can be chosen rational homogeneous of degree7, and rho has degree8. The certificate(5) has degree10 in a and is linear in h. Although this particular normalized dual description is only defined off Sigma, its scalar extends polynomially: a fixed equivariant splitting of qV gives v_h quadratic and w_h cubic after the global linear b correction, so the equal expression lambda_a(a w_h) is a degree-ten polynomial.

The polynomial is the contraction of the actual fourth gate with the cofactor covector. On the rank3 open set, where the surviving target is a line, it vanishes exactly when that fourth value vanishes. At Sigma, lambda_a=0; ordinary polynomial evaluation does NOT test the full specialized ideal-sheaf fiber or the additional surviving A-kernel line. No extension of that equivalence to Sigma is claimed.

The remaining evaluation problem is the ACTUAL functional rho_a on a h zeta_a. Neither dual division is determined by the cone ideal alone. This note gives a further exact interface, not a nonvanishing claim or a complete proof repair.

## Reproduction

Run verify_fourth_normalized_dual_certificate.py. It checks the universal dimensions, homogeneous degrees, normalization freedom, and formal cancellation identities. The actual cohomology and comparison inputs are the cited earlier results. No actual coefficient or instance matrix/rank evaluation is used.
