## 2. Exact physical-to-rational derivative bridge

Let K=k(x_0,...,x_3), A=K[y_0,...,y_3]/(y_i^2-C_i(x_i)), in characteristic zero. Write b_m for the squarefree mask basis and pi for coefficient of b_15, WITHOUT another division by the deck product. The source has C_i=x_i^3-x_i, but the identity below is universal for any nonzero C_i of one coordinate. Let V_i x_j=delta_ij y_i and V_i y_j=delta_ij C_i'/2.

For EVERY Z in A,

    pi(V_i Z) = partial_i pi(y_i Z).                         (A)

Proof: in both sides only Z's mask 15 XOR 2^i contributes. That mask does not contain i. V_i differentiates its rational coefficient and adds y_i, with no basis-derivative contribution; multiplication by y_i also adds that bit without C_i. All other masks contribute zero to both sides. This is a linear identity on arbitrary rational coefficients, not a statement that pi commutes with V_i.

Consequently, for arbitrary a,s in A,

    pi(a V_i s) = partial_i pi(y_i a s) - pi((V_i a)s).       (B)

This follows from Leibniz and (A). It is valid with arbitrary moving-frame parity and arbitrary rational poles. It neither assumes that a is rational-x nor requires termwise Laurentness. It introduces no extra deck division. The derivative on the right is exactly the ordinary rational coordinate derivative required by the residue theorem. In particular, the apparent physical-versus-rational mismatch does not prevent integration by parts after complete extraction.

## 3. The complete finite kernel, specified without evaluating it

Use P=(0,1), Q=(2,3), and reserve p for the retained polynomial test, e.g. p=(x_0 x_1+x_2 x_3)^2 for ID0.

FRAME CONVENTION: F_spec is in the pinned common finite trivialization. The imported original-resolution/full-sign conversion is tau^(r-2), hence tau^-4 at J2 degree -2; tau=1 on this finite chart. This conversion is already part of the source interpretation, not a missing multiplier to append to w_lambda or an extra deck division. The inert program explicitly records degree-minus2-tau-minus4, finite-tau1, full-deck-mask15. If the same circuit is instead written in another trivialization with a nonconstant scalar conversion f, include f in the complete kernel (and its algebraic baseline) before applying (B): the derivative is V_i(p f a), retaining V_i(f). No chartwise constant-factor assumption is authorized. See dependencies/ID0-correctness-boundary.md, assumptions D and its frame/extraction argument, and dependencies/HPL-lift-lowering.md section 5. For each original outer owner tuple o on a standard staircase, sort once into t with the actual source parity. Keep all five original owners in its weight product.

Expand the LINEAR operator

    L[-H_-1 delta H_0 delta j(-)] on t,
    L(X)=X_(3,1)[5,0]+X_(2,0)[1,3]+X_(2,0)[4,2].

Linearity over A is legitimate: these homotopies, restrictions, transposition, selector and multiplications introduce no coordinate derivatives. Each face-and-homotopy path lambda retains a source-increasing residual triple tau_lambda and an A-linear scalar functional ell_lambda on its 2x2 row matrix. It retains its ordered H/E prefixes and suffixes and its matching I(-)^t P inclusion. Define w_lambda to contain the staircase sign, sorting parity, path coefficient (including the J2 minus) and the product of ALL FIVE original outer weights. No source term is rebuilt on a different nonlinear order. No repeated physical-label zero shortcut or pruning is needed.

Equivalently this definition can keep the finite composition unexpanded: ell_lambda is merely the coefficient of each residual occurrence in the syntactic linear circuit. It specifies exact rational/curve-algebra functions from the pinned source; it is not an arbitrary unknown detector. No outer-owner alphabet, weight, or model value is evaluated to define it.

For tau=(i,j,k), write A0=g_ij, B0=g_jk, G=g_ik and

    R_alg = tf(G^-1 M) + F_Q k_P,ik + F_P k_Q,ik,

where M consists, IN ORDER, of

    U_P,jk U_Q,ij + U_Q,jk U_P,ij
    + mu_P(U_Q,jk,A0) + mu_Q(U_P,jk,A0)
    + mu_P(B0,U_Q,ij) + mu_Q(B0,U_P,ij) + mu2(B0,A0)
    - b_P U_Q,ik - b_Q U_P,ik - b_P b_Q G,

U_r=g k_r, k_r=-mu_r(g^-1,g)/2, F_r=b_r-tr(G^-1 mu_r(B0,A0))/2. Thus R_alg retains all ten baseline terms and both Fk branches, rather than using a pre-gerbe baseline.

For r=(a,b), complementary q, E_r(s_q) has the following four (axis, current, edge, sign/2) entries:

    (a,L_b,jk,+1/2), (b,L_a,jk,-1/2),
    (b,U_a,ij,+1/2), (a,U_b,ij,-1/2),

L_d=A0^-1 V_d A0, U_d=A0^-1 B0^-1(V_d B0)A0. Include this table twice, (r,q)=(P,Q),(Q,P). Set

    a_(lambda,e) = w_lambda * sign_e/2 * ell_lambda(current_e),
    s_e = s_raw(q,edge_e).

Both endpoints and all transports remain. RawSource.T is the pinned s_raw leaf, NOT the N14 scalar solver. Scalar-free here means independent of these explicit s_raw leaves; R_alg still contains its full transition derivatives.

The mathematical preterminal ID0 scalar is exactly

    F_spec = pi[ sum_lambda w_lambda ell_lambda(R_alg)
                 + sum_(lambda,e) a_(lambda,e) V_(axis_e) s_e ].     (C)

This is just the authenticated full scalar circuit expanded linearly. pi is applied after forming the same full weighted sum. Using linearity to prove (C) makes no termwise Laurent claim.

