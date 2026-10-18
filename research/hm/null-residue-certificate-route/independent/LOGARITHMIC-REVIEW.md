# Independent logarithmic-tangent audit

Let R=k[x1,...,xn] with characteristic-zero field k and nonzero D in R. Regard a polynomial tuple A=(A_i) as the derivation A=sum A_i partial_i. Define div A=sum partial_i A_i.

The denominator-one certificate

    pND = D div A - A(D)

implies D divides A(D). Thus every such certificate lies in the full logarithmic tangent module

    Der(-log D) = { A in R^n : A(D) belongs to (D) }.

This is an exact restriction, not a heuristic ansatz. Conversely, restricting the certificate equation to this full module loses no solutions. In combination with the independently proved Laurent theorem, it preserves the complete existence criterion.

## Factorwise criterion, including multiplicities

Write D=c product_a q_a^m_a for distinct irreducible nonconstant q_a and a nonzero constant c. Then

    A in Der(-log D) iff q_a divides A(q_a) for every a.

Indeed, put D=q^m E with gcd(q,E)=1. The identity

    A(D)=m q^(m-1) E A(q)+q^m A(E)

and D|A(D) imply q|mEA(q). Since m is nonzero in k and q is prime and coprime to E, q|A(q). Conversely, if A(q_a)=b_a q_a, the product rule gives A(D)/D=sum_a m_a b_a in R. Constant D gives the unrestricted module R^n and an empty sum.

Characteristic zero is essential to this implication as stated: in characteristic l, the derivative of q^l vanishes and would erase that factor's tangency constraint.

## Twisted divergence identity

For a logarithmic polynomial derivation v with v(q_a)=b_a q_a and any polynomial f,

    div(f v / D)
      = [v(f)+f*(div v-sum_a m_a b_a)] / D.

This is just the quotient and product rules and does not presume vanishing of a geometric period. When pF=pN/D has the required Laurent and trace interpretation, an exact identity

    pN = sum_l [v_l(f_l)+f_l*(div v_l-sum_a m_a b_(l,a))]

certifies the desired zero pairing. A generating family spanning the entire polynomial module, with unrestricted polynomial multipliers, is exact. An incomplete family, degree-truncated multipliers, or an incomplete syzygy computation is only a sufficient search space. Even with the known bound on the final tuple A, cancellation in a module-generator representation may prevent transferring that bound directly to each multiplier f_l without a separate proof.

This addendum confirms the algebraic interface. It supplies no actual retained certificate, factorization of a production denominator, module computation, physical evaluation, or resource admission.

## Audit of the explicit complete submodule

The separately supplied `logarithmic/PROOF.md` strengthens full-module parametrization: with D=x^d C and N=CQ, the n fields v_i=C*x_i*e_i suffice for every zero-residue Laurent target. This claim is accepted. Substituting A_i=C*x_i*h_i gives

    D*partial_i A_i-A_i*partial_i D
      = D*C*[x_i*partial_i h_i+(1-d_i)*h_i].

The derivatives of C cancel exactly. The remaining diagonal operator on x^b has eigenvalue b_i+1-d_i. Only the simultaneous resonance b=d-1 survives all n operators, precisely the Laurent residue monomial. If any d_i=0, the formal resonance has a negative coordinate and is absent from the polynomial numerator space, consistent with automatic zero residue in that case. The stated total-degree and coordinate bounds on h_i follow from deg_j(pQ)=deg_j(pN)-deg_j C. This supplies an explicit complete baseline without computing a full tangent module.

The separate logarithmic checker was reproduced in normal and optimized Python. Its nonmonomial-denominator positive identity, negative mutation, and successful missing second-generator control passed. The proof that the first generator alone cannot produce the target is a monomial argument in the accompanying text, not an exhaustive computational search. No production computation is involved.
