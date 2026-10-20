# Same-carrier jet collapse and the remaining raw scalar divergence

## Scope

This is a structural identity on actual legal source tuples whose auxiliary carrier is the same at every vertex. It is not a numerical specialization, a new frame choice, or a statement about all tuples sampled by the comparison/HPL operators. Same output tags do not imply same input carriers. No actual source/model/matrix/polynomial/point/jet evaluation or source computation is used.

The accepted source identity is

    g_ij = D(nu_j)(P_ci I_cj)^t D(nu_i)^-1,
    P_c I_c=Id, D(z)=diag(z,z^-1),
    nu_i=product_d r_d^(m_i,d), r_d=y_d/x_d.

The invariant V_d acts on factor d alone. These premises are established in the accepted structural closure/product-root proofs and reused by the same-pair ordinary-twist proof. That earlier proof addresses a different associativity obstruction; the present conclusion concerns the mixed baseline, new jet transgression, and surviving scalar derivatives.

## 1. Cartan reduction without evaluating a primitive

On a genuine all-same-carrier tuple, the morphism identity P_c I_c=Id gives

    g_ij=D(nu_j/nu_i).

Put h=diag(1,-1), rho_d=(V_d r_d)/r_d, lambda_d=(m_j,d-m_i,d)rho_d and eta_d=(m_k,d-m_j,d)rho_d. Do not identify rho_d with the source coefficient q_d: those are different frame-comparison quantities.

For A=g_ij, B=g_jk, G=BA, the literal physical currents are

    L_d=A^-1 V_d A=lambda_d h,
    U_d=A^-1 B^-1(V_d B)A=eta_d h.

All these currents commute, and V_a lambda_b=V_a eta_b=0 when a differs from b. Differentiating the cocharacter identity gives, for distinct a,b,

    A^-1 V_a V_b A=lambda_a lambda_b Id,
    A^-1 B^-1(V_a V_b B)A=eta_a eta_b Id.

Consequently every cross-axis normalized traceless jet H_ab and J_ab is zero. This does not assert that same-axis normalized jets vanish.

These are identities of rational sections in the original physical trivialization. The accepted regular transition interpretation makes them identities on their genuine legal intersections. On every standard finite/infinity representation chart one transports these same identities and the invariant V_d; no reference connection is reset to zero. Equality on the dense common rational chart extends to the regular sections on each chart. At a same-bit factor the coefficient with exponent difference zero is identically zero, so no inverse of r_d at its zeros is demanded. When the exponent difference is nonzero, both legal bit opens are present and r_d is a unit on their intersection. Diagonal chart changes preserve the Cartan line. Thus this is not an inference from one sampled point or from generic invertibility of a jet matrix.

## 2. Every new algebraic jet slot vanishes

In PR79 b80a710530a5d5d9b1844196bc446459daf0732f, the four signed complementary entries are (13,24,+), (14,23,-), (23,14,-), (24,13,+). Every H and J appearing there has distinct axes. Thus the displayed formulas give

    Phi=0, M2=0, S2=0.

All current brackets vanish, giving Q4=C4=0, and hence R_alg=0. The midpoint curvatures vanish on this restricted source family too. The kernel-adjoint term involving Phi is zero because Phi itself is zero, not because the kernel is constant. This does not eliminate the older scalar-current flux Z or its kernel derivatives.

There is an independent direct check against the literal raw source formulas. Its

    k_(a,b)=-( (V_a g^-1)(V_b g)-(V_b g^-1)(V_a g) )/4
           =[theta_a,theta_b]/4

vanishes. Thus u=gk and its derivatives vanish on this open, all six u-dependent kinetic terms and both negative b u terms vanish, and both Fk branches vanish. In the remaining mixed Moyal term every differentiated pair has distinct axes; after normalizing by G^-1 its products are scalar multiples of Id. In the compiler's zero-based directions, the exact central coefficient is

    G^-1 mu2(B,A)
       = (eta_0 lambda_1-eta_1 lambda_0)
         (eta_2 lambda_3-eta_3 lambda_2) Id/4.

The final -b_P b_Q G term is also central after normalization. Taking the prescribed tracefree projection therefore kills the complete baseline. This independently verifies R_alg=0 without silently replacing F or a raw scalar by an endpoint expression.

## 3. Exact residual and literal current-curl

Retain the actual source scalar s_q,ij=s_raw(q,i,j), with no independence assertion about its complementary variables. For p=(a,b), q its complementary pair, the entire remaining p contribution is

    E_p(s_q)=h/2 [
       (V_a s_q,jk)lambda_b-(V_b s_q,jk)lambda_a
       +(V_b s_q,ij)eta_a-(V_a s_q,ij)eta_b ].

Thus the full mixed raw residual is exactly E_P(s_Q)+E_Q(s_P), a section of the Cartan line in this physical row frame. Define the original scalar-current fluxes

    Z_a=(s_q,jk lambda_b-s_q,ij eta_b)h/2,
    Z_b=(-s_q,jk lambda_a+s_q,ij eta_a)h/2,

and similarly for the exchanged pair. The cross-derivative identities in section 1 give the stronger exact equality

    R_raw=sum_d V_d Z_d.

The complete-normal-form literal curl is

    Ccur_p=2(s_q,ij+s_q,jk)k_p,ij-2s_q,ij k_p,ik=0.

No derivative of s_raw has been set to zero. Its raw block formula contains carrier-dependent traces, so product separation of nu or of q alone does not prove such a vanishing. The full scalar leaf and all eight complementary derivative slots remain.

## 4. Precise propagation and stopping point

For any coefficient-algebra-linear complete functional K on one such residual occurrence (including all actual test, weight, HPL, restriction and selector coefficients), Leibniz gives

    K(R_raw)=sum_d V_d(K(Z_d))-sum_d K_;d(Z_d),
    K_;d(X)=V_d(K(X))-K(V_d X).

Thus the bounded new source-specific reduction removes the algebraic baseline and literal current-curl on these input tuples, but leaves the full test/weight/HPL/selector derivative. In the published normal form these derivatives are represented by the coupled test/selector, overlap/cohomology correction and combined current-F defect families, with the one already accounted-for boundary. No second boundary is subtracted. Neither those remaining families nor the current-F cups are asserted zero.

On an all-same-carrier quadruple the known identity Delta Z=the signed current-F cups remains valid and useful. The exact F is generally still b minus its central current curvature, not zero. Its scalar cup products are therefore retained.

The comparison and HPL sums sample arbitrary inserted owners. An all-same-carrier restriction is stable under taking faces but does not absorb their mixed-carrier summands. Accordingly this lemma gives no vanishing of the complete compared target, no reduction in the thirty detector tests, no global flux-domain theorem and no obstruction value.

## Sources read

- PR1 current through comment 6250661140: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6250661140
- New transgression: https://github.com/Akilleez-QA/read-em-and-weep/blob/b80a710530a5d5d9b1844196bc446459daf0732f/research/hm/null-covariant-jet-transgression/RESULT.md
- Rank-two reduction: https://github.com/Akilleez-QA/read-em-and-weep/blob/b80a710530a5d5d9b1844196bc446459daf0732f/research/hm/null-rank-two-jet-reduction/RESULT.md
- Complete normal form: https://github.com/Akilleez-QA/read-em-and-weep/blob/b80a710530a5d5d9b1844196bc446459daf0732f/research/hm/null-complete-remainder-normal-form/RESULT.md
- Inert compiler source: https://github.com/Akilleez-QA/read-em-and-weep/blob/491306fd2f7f8a04c29784afa48a6cb8a467f154/research/hm/null-raw-regular-extension/inputs/compiler.py.txt

The direct literal audit reads Source.k, mu2, E and residual from the authenticated local inert compiler snapshot. RawSource's scalar override is retained, as established by the accepted complementary-scalar-derivative proof. No executable checker is offered as a substitute for these identities.
