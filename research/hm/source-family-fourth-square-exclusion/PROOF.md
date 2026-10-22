# No nonzero positive source has universal fourth-square vanishing in the negative direction

## Statement

Retain the actual canonical source/frame and all hypotheses of PR739, PR729 and PR725. Write A_- = H^0(L,O_L(2)), L=P^1, H=D5, and k=C(L). To avoid confusion, use A=a^2 h for the positive scalar multiplier, not for A_-. Fix the actual pair n and its first-normal lift T in one fixed negative chart, and V=(k[X,Y]/(f3))_8. Put d=[d2] in V; PR729 proves d is nonzero.

For EVERY nonzero h in H, the set

    Z_h = {a in A_- minus {0}: K_actual(a,h)=0}

is the punctured kernel of a nonzero C-linear map A_- -> V. In particular its projectivization is a proper projective linear subspace of P(A_-), of dimension at most one (possibly empty). On its nonempty Zariski-open complement the actual fourth-square scalar is nonzero. This is an existential and family-level exclusion, not an evaluation at any selected a or h.

No conclusion about beta4 or algebraicity follows. In particular this does not show nonvanishing at a previously chosen actual direction, nor identify a source direction surviving a separate Bockstein quotient.

## Exact inputs and source audit

1. [PR739 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/9b67dae4d91e81b9e514f4072bfc3774ffd0028f/research/hm/actual-scalar-compatibility/PROOF.md), commit 9b67dae4d91e81b9e514f4072bfc3774ffd0028f: in the fixed physical harmonic frame,

       s_actual=-a L_can(a,h),
       K_actual(a,h)=K0(a,h)-a^2 L_can(a,h)d.             (1)

   K0 denotes the zero-leading-scalar local class, not an alteration of the actual global ladder.
2. [PR729 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/c384ae419983a5031af19c37674df020de1aa5da/research/hm/firstnormal-scalar-slope/PROOF.md), commit c384ae419983a5031af19c37674df020de1aa5da: arbitrary such local zero-scalar inputs have regular q^2 solutions, h-divisible cubic scalar C, and a well-defined immutable class. The class d is nonzero for every regular pair, without square-freeness assumptions.
3. [PR725 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/397c7473691a08a839ccf7e9abeed06002b48bab/research/hm/modular-vertex-elimination/PROOF.md), commit 397c7473691a08a839ccf7e9abeed06002b48bab: two exact graded divisions and a fixed k-linear section give a k-linear right inverse to the trace equation. The immutable class is independent of the section or local R choice.
4. [PR713 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/5b3943980ecaef78ee7f56fbc015d40955fb24f0/research/hm/leading-vertex-obstruction/PROOF.md), commit 5b3943980ecaef78ee7f56fbc015d40955fb24f0, sections 2 and 4: K_actual is the reduction modulo f3 of the actual fourth-square scalar class. Its nonvanishing implies nonvanishing of the actual global fourth-square scalar rho4. Vanishing of K alone is only a necessary gate for rho4=0.

The following three source files were read directly at commit 8d8b5be4ce62c3055bb53be9e16d29cc63072f04 in research/hm/order-four-quadratic-load/:

- [ACTUAL-MULTIPLIED-NILPOTENT-COHERENCE-FIXES-ENDPOINT-SCALE.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-MULTIPLIED-NILPOTENT-COHERENCE-FIXES-ENDPOINT-SCALE.md), sections 3-4: the same fixed chart generator N_r=U_(r^2)/r^2 works for every a; U_a=alpha(z-kappa q/r^2)U_(r^2). Thus its leading n,T are independent of a. Coordinate/frame choice here is abstract; no coefficient or point is evaluated.
- [ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md): J3=(ah-qb)U_a-q^2 C_h with b=L_can(a,h), and the beta4 boundary has a separate quotient. This fixes the source normalization and prevents replacing square nonvanishing by a beta4 conclusion.
- [ACTUAL-CANONICAL-RAW-CUBIC-HAS-A-NONZERO-LINEAR-LIFTING-CORRECTION.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-CANONICAL-RAW-CUBIC-HAS-A-NONZERO-LINEAR-LIFTING-CORRECTION.md), sections 2 and 6: L_can is globally polynomial, linear in a and h, and

       L_can(a,h)=gamma S_h(a), gamma != 0,
       H ~= Sym^2_0(A_-),                             (2)

  where S_h is self-adjoint and trace-free for the invariant nondegenerate form. In particular h nonzero implies S_h nonzero. Only this established structural theorem is imported; no earlier eigenline calculation is rerun or evaluated.

## 1. Homogeneity with the source frame held fixed

The harmonic coefficient algebra is k-linear: the operators differentiate only the positive variables, so every negative rational function, including a, is a coefficient scalar. This is essential. Scaling a here does not move the generator N_r, the pair f3,g5, T, the quotient V, or d.

For zero leading scalar, put

    P_A=A n,
    M_A=A T+B1(A,n),
    N=n+qT,
    W_A=[q^2](A*N),
    V_A=[q^3](A*N).

All four displayed matrix coefficients are k-linear in the arbitrary quartic A. Write N*N=q^2 d2 Id+q^3 d3 Id+O(q^4). The known q^2 identity is

    E_A+A tr(nW_A)=A^2 d2,
    E_A=sc(M_A^2+B1(P_A,M_A)+B1(M_A,P_A)+B2(P_A,P_A)).

Consequently the right-hand side of the trace equation is

    tr(nR_A)=-E_A/A=tr(nW_A)-A d2,                  (3)

which is k-linear in A and a polynomial. It is not necessary to invert h in the polynomial ring. Apply the fixed k-linear right inverse supplied by PR725 to (3). This defines R_A linearly in A. Hence, for any c in k,

    (P_(cA),M_(cA),R_(cA))=c(P_A,M_A,R_A).

Every one of the eight ordered terms in C(P,M,R) is bilinear. Thus C_(cA)=c^2 C_A. In particular with c=a^2,

    C0(a,h)=a^4 C_loc,h,
    K0(a,h)=a^3 K_h,     K_h=[C_loc,h/h] in V.         (4)

Here C_loc,h is the formal local construction at multiplier A=h, not an actual source-instance evaluation at a chosen global quadratic. Automatic divisibility in PR729 makes C_loc,h/h polynomial. Formula (4) is independent of the chosen splitting because K0 is.

Indeed K_h depends C-linearly on h. Set Z_A=R_A-W_A. PR729's factorization at s=0 is

    C_A=A(A d3+B1(A,d2)+Psi(Z_A)-tr(nV_A)).

Each term inside the parenthesis is k-linear in A. This also establishes linearity without treating exact division of a quadratic expression as automatically linear.

Combining (1) and (4) gives the central identity

    K_actual(a,h)=a^2 (a K_h-L_can(a,h)d).           (5)

All global quadratics in this formula are represented in the same rational trivialization of O_L(2). No assertion that the abstract multiplier 1 is itself the fixed actual source is involved.

## 2. Rational multiplication rigidity

Lemma. Let E=H^0(P^1,O(m)), m>=0, and let B:E->E be a C-linear map. Suppose that for one rational function r in C(P^1), B(a)=r a as rational sections for every a in E. Then r is constant and B=r Id.

Proof. E generates O(m). If r had a pole at any point, choose a section of E not vanishing there; r a would fail to be regular there, contradicting B(a) in E. Thus r is globally regular on P^1, hence constant. This is a universal basepoint-free argument, not the choice or evaluation of any actual source point. Equivalently the polar divisor of r must lie in the empty base locus of the complete linear system. QED.

The same argument applies when the universal equality is initially known only on a Zariski-dense subset of E: its difference is a linear map to rational sections, so it vanishes identically.

## 3. Excluding universal vanishing at every nonzero h

Fix h!=0, and suppose K_actual(a,h)=0 for every nonzero global a in A_-. Every nonzero section represents a nonzero element of k in the rational frame, so cancellation of a^2 in (5) is legitimate. We obtain

    a K_h=L_can(a,h)d for every a.                  (6)

Since d!=0 in the k-vector space V, (6) forces K_h=r_h d for a unique r_h in k; it then forces

    L_can(a,h)=r_h a for every a in A_-.            (7)

No functional or coefficient of V is evaluated: this is cancellation in its one-dimensional subspace kd. The rigidity lemma makes r_h constant and L_can(-,h)=r_h Id on A_-. But (2) makes this endomorphism trace-free. Since dim A_-=3 and char C=0, 3r_h=0, hence r_h=0. Equation (2), with gamma!=0 and injective h->S_h, now forces h=0, contradiction.

This proves that the C-linear map

    Phi_h:A_- -> V,    a |-> a K_h-L_can(a,h)d      (8)

is nonzero for every h!=0. Because nonzero global a is nonzero in k, (5) says exactly Z_h=ker(Phi_h) minus {0}. The kernel is a proper C-linear subspace of the three-dimensional A_-. Therefore its projectivization has dimension at most one, and its complement is nonempty and Zariski open.

V is finite-dimensional over k, not over C; this causes no issue. The image of the finite-dimensional domain in (8) spans a finite-dimensional C-space, so its kernel is an ordinary C-linear subspace. The argument computes no rank at an actual instance.

There are two useful alternatives. If K_h is not in kd, Z_h is empty, since reducing (6) modulo kd gives a nonzero scalar a times [K_h]. If K_h is in kd, Z_h consists exactly of those global quadratics satisfying the rational eigen-equation (7) for that fixed r_h. It is still proper, but its actual dimension or elements are not evaluated.

## 4. Square-direction corollary

Under A_-=Sym^2 W, the pure-square projective directions form the smooth Veronese conic nu_2(P(W)) in P(A_-). For any fixed h!=0, its intersection with P(ker Phi_h) has at most two geometric points: the latter is empty, a point, or a line, and a nondegenerate conic is not contained in a line. A line meets it in length two, allowing tangency. Consequently all but at most two pure-square projective directions have nonzero K_actual and nonzero actual fourth-square scalar for that h.

This is an abstract incidence conclusion. It does not select or evaluate a square direction, identify any exceptional directions, or evaluate the separate fourth Bockstein.

## 5. Contribution and strict limitations

This resolves a universal dependency left by PR739: the canonical actual scalar cannot cancel the zero-scalar immutable class for every negative direction at any nonzero positive source. The proof uses the specific actual source operation, not the independently variable abstract scalar of PR729. It therefore gives an actual-family exclusion stronger than the earlier exclusion from local equations alone.

For any fixed nonzero h, some directions (indeed a nonempty Zariski-open set) have nonzero immutable class and hence nonzero actual fourth-square scalar. It does not decide K or rho4 at any selected actual a; the possibly exceptional proper linear subspace remains undetermined. It also does not say K=0 suffices for rho4=0.

Most importantly, rho4 is not beta4. The latter is the separate fifth-neighborhood adjoint boundary modulo im(beta2). No implication from the nonzero scalar-square family to a nonzero beta4 value or failure of algebraicity is asserted. The existence of a direction where this scalar gate fails does not identify the direction required by any separate open goal.

No selected coefficients, points, derivatives, actual-instance matrix ranks, model examples, large computation, Gauss analysis, or identity-W work are used. The only calculation is formal linearity/bilinearity and cancellation in an abstract vector space. The source theorem's canonical nonzero normalization gamma is retained, not assigned.
