# Conditional coordinate comparison for a four-dimensional frame

## Algebraic scope and conventions

Work over the rational polynomial ring S = Q[u0,...,u33], or any commutative Q-algebra receiving a homomorphism from S. The explicit weights B2, B3 and Wj are defined by `weights.json`: multiply each listed polynomial by its outer rational scale. Repeated monomial indices mean repeated factors. No weight or source literal is inverted. Formal nonzero polynomials need not remain nonzero after specialization.

Let x=v1, y=v2, z=v4, t=v3. Let a1,a2,a3,a4 belong to R[x^±1,y^±1,z^±1][[t]], where R is such a Q-algebra. Write a_j^(n)[b] for the coefficient of x^b1 y^b2 z^b4 t^n. The same notation applies to f_r. Only central and first-normal coefficients are used below. In particular, first-normal means the coefficient of t, equal to the derivative at t=0, not a derivative of an already restricted central coefficient.

Define the one-form A = a1 dv1+a2 dv2+a3 dv3+a4 dv4 and frame

    J0 = ∂1+x∂2+y∂3+t∂4,
    J1 = −∂2−x∂3−y∂4,
    J2 = ∂3+x∂4,
    J3 = −∂4.

Set f_r=A(J_r). Consider exactly the following functional L:

    B2 f0^(0)[1,−3,1] + B3 f0^(0)[1,−1,0]
    + W1 f1^(0)[0,−1,0] + W2 f1^(0)[2,−4,1]
    + W5 f1^(1)[1,−3,0]
    + W7 f2^(0)[−1,−1,0] + W8 f2^(0)[1,−4,1]
    + W9 f2^(1)[−3,1,0] + W11 f2^(1)[2,−4,0]
    + W12 f3^(0)[−2,−1,0] + W13 f3^(1)[−4,1,0]
    + W14 f3^(1)[1,−4,0].

## Theorem

L equals the twelve-term functional

    B2 a1^(0)[1,−3,1] + B3 a1^(0)[1,−1,0]
    + B2 a2^(0)[0,−3,1] − W2 a2^(0)[2,−4,1]
    − W5 a2^(1)[1,−3,0]
    + B3 a3^(0)[1,−2,0] + W9 a3^(1)[−3,1,0]
    − W5 a3^(1)[0,−3,0] + W11 a3^(1)[2,−4,0]
    + W8 a4^(0)[0,−4,1] − B3 a4^(0)[0,−2,0]
    − W2 a4^(0)[2,−5,1].

This is an equality of linear coefficient functionals, not a value for L or a nonvanishing claim. There are eight central and four first-normal terms in this presentation; this does not assert a minimal representation after source specialization.

## Proof

At t=0 the frame gives

    f0=a1+x a2+y a3,
    f1=−a2−x a3−y a4,
    f2=a3+x a4,
    f3=−a4.

The same formulas apply to first-normal coefficients of roots1,2,3. For root0 the correct first-normal formula instead has the extra central term a4^(0). L has no root0 first-normal input, so this coupling creates no branch here.

For a monomial x^m1 y^m2 z^m4, its product with a_j shifts a requested target b to b−m. Substitution in the twelve inputs of L gives 26 branches grouped at 18 distinct component/order/target keys. Exactly six of their weights vanish:

    a2^(0)[0,−1,0]: B3−W1,
    a3^(0)[−1,−1,0]: −W1+W7,
    a4^(0)[−2,−1,0]: W7−W12,
    a3^(0)[1,−4,1]: B2−W2+W8,
    a4^(1)[−4,1,0]: W9−W13,
    a4^(1)[1,−4,0]: −W5+W11−W14.

The saved explicit arrays defining the weights give

    W1=W7=W12=B3, W13=W9,
    B2−W2+W8=0, W11−W14−W5=0.

These can be checked coefficientwise without assigning any value to the u variables. For a short independent verification of the last two identities, order their union of monomials as

    A=u2 u6 u13 u20, B=u4 u6 u7 u21,
    C=u4 u6 u8 u20, D=u6² u8 u25,
    E=u6 u7 u16 u21, F=u6 u8 u16 u20,
    G=u6 u13 u22 u26, H=u6 u13 u24 u26.

Their scaled coefficient vectors are

    B2 = (−1/4,0,0,1/4,0,0,−1/4,1/4),
    W2 = (1/2,3,−6,−1/2,−5/4,17/4,1/2,−1/2),
    W8 = (3/4,3,−6,−3/4,−5/4,17/4,3/4,−3/4).

Thus B2−W2+W8=0. On the ordered monomials (B,C,E,F),

    W5=(0,3,−5/4,−7/4),
    W11=(1/2,−33/2,6,10),
    W14=(1/2,−39/2,29/4,47/4),

so W11−W14−W5=0. The equalities involving B3 follow directly from the seven shared entries in the arrays, and W9=W13=−u6² u7 u13/4. The remaining twelve groups are precisely the displayed conclusion. This proves the theorem over S and therefore under every specialization to R.

## Derivative convention and source-interface requirements

Suppose a source request is w[v^τ]R_u ∂k F for k in {1,2,4}, with coefficient extraction in the indicated product well-defined (for example, for Laurent polynomials, or whenever the relevant coefficient convolution is finite). Then a field term F[a] contributes

    w a_k R_u[τ−a+e_k] F[a].

This follows by differentiating its Laurent monomial and remains valid for negative exponents. Once included in a completed root weight, this factor must not be applied again during the frame substitution. Differentiating a product v^m a_j gives the same total factor: the frame-monomial and component derivatives contribute m_k and a_k−m_k, respectively. A source using different density or derivative conventions requires a new interface derivation.

Application of this abstract theorem to the historical FULL V12 source requires three additional premises, none established by this theorem:

1. Frame/source binding. The exact original source uses the displayed physical frame, FULL V12 field, edge(1,2), owner2, no seed pivot, and the stated transposition, density and derivative conventions. Root, owner, coordinate and pivot indices must not be interchanged.
2. Pair completeness. A source-bound support and complete-pair certificate exhausts the selected predecessor records and proves that their entire retained functional is exactly L, with only the jointly cancelling pair88/107 removed. The documented counts are59 predecessor rows and57 retained rows (9 root0 and48 roots1–3); copies of selected records alone do not prove exhaustion. No individual member of a cancelling pair is asserted zero.
3. Current/source binding. An authenticated full DAG/query certificate identifies each source coefficient and the rational provider scales with these explicit polynomial weights in the same34-variable namespace. Coincident node numbers across distinct namespaces do not supply this identification.

These are mathematical hypotheses, not facts supplied by a hash or by the present formal arrays. Until they are discharged, the result is an abstract conditional coordinate identity, not a reconstruction of a source instance. It neither alters a shifted317 representation nor transfers root-field support restrictions to individual coordinate components. No actual HM coefficient evaluation, cohomology conclusion, algebraicity claim or new original-row deletion follows.
