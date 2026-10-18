## 1. Fixed source and complete dual kernel

Use precisely the source-adjoint PROOF.md sections 3–4 and its independent review. Its frozen compiler and RawSource identify the two complementary E branches, with RawSource replacing T alone. Read the inherited compiler as inert text: Source.k gives k_r=-mu_r(g^-1,g)/2, Source.E gives the eight signs/endpoints below, and Source.residual gives the full baseline plus both Fk and E branches. The copied branches.json is the published eight-branch table, not a newly inferred owner list.

For each residual occurrence lambda with triple (i,j,k), retain its exact finite circuit functional ell_lambda and its exact original-owner/staircase/path weight w_lambda. Put

    K_lambda(X) = p w_lambda ell_lambda(X).

This notation merely gathers the already specified full weighted functional. It includes all original weights, ordered H/E/I/P factors, the selector, the one existing residual transpose, and the finite-frame convention. No factor is assumed constant. In another frame any required nonconstant conversion also belongs inside K before differentiating.

Define the coefficient derivative of this functional in the same fixed row-matrix trivialization:

    K_lambda;d(X) = V_d(K_lambda(X)) - K_lambda(V_d X).       (1)

It is A-linear in X: applying Leibniz to fX cancels the V_d(f) terms. Equivalently, if K(X)=tr(C X), then K_;d(X)=tr((V_d C)X). The trace pairing on the full two-by-two matrix module is perfect, so C exists uniquely. This does not evaluate C or add a transpose to the original source convention. Equation (1) differentiates every coefficient of K, including p and all outer/HPL/selector factors.

## 2. Transported Maurer–Cartan, with the mixed terms retained

Let A=g_ij, B=g_jk, G=g_ik=BA. For a derivative axis d set

    L_d=A^-1 V_d A,
    U_d=A^-1 B^-1(V_d B)A,
    T_d=L_d+U_d=G^-1 V_d G.

The product derivations commute; this is established for the exact curve algebra in the preceding curve-derivation bridge. Differentiating an inverse gives

    V_a L_b - V_b L_a = -[L_a,L_b].                        (2)

Applying the same identity to T and subtracting (2) gives

    V_a U_b - V_b U_a
      = -[U_a,U_b]-[L_a,U_b]-[U_a,L_b].                    (3)

In particular U is a transported current, and ordinary Maurer–Cartan with only -[U_a,U_b] is wrong. It obeys the covariant Maurer–Cartan equation for the L connection. No exterior alternation over all four slots is being taken; (2)–(3) apply independently to either existing ordered pair r=(a,b).

From the literal source k definition and the inverse rule,

    k_r,ij=[L_a,L_b]/4,
    k_r,ik=[T_a,T_b]/4.

Hence

    curl_r L=-4 k_r,ij,
    curl_r U=-4(k_r,ik-k_r,ij).                            (4)

All k terms in (4) are in the first row frame of the same triple. No transport is omitted: k_r,ik uses T, not U alone.

## 3. Exact reduction of each paired endpoint block

Fix r=(a,b), complementary q, and write s_ij=s_raw(q,i,j), s_jk=s_raw(q,j,k). For one occurrence lambda the two endpoint coefficients contributed to the old B_p are exactly

    -s_jk/2 [V_a K(L_b)-V_b K(L_a)]
    +s_ij/2 [V_a K(U_b)-V_b K(U_a)].                     (5)

These signs are obtained from the published E entries (+L_b V_a s_jk,-L_a V_b s_jk,+U_a V_b s_ij,-U_b V_a s_ij)/2 by its established adjoint. Scalar commutativity allows the displayed placement of s; no derivative acts on s in B_p.

Use (1) to separate the current derivative from the complete coefficient derivative, then use (4). Expression (5) becomes exactly

    D_lambda,r
      = -s_jk/2 [K_;a(L_b)-K_;b(L_a)]
        +s_ij/2 [K_;a(U_b)-K_;b(U_a)]
        +2(s_ij+s_jk) K(k_r,ij)-2s_ij K(k_r,ik).           (6)

This is a real reduction: the occurrence of V_a L_b−V_b L_a and V_a U_b−V_b U_a disappears entirely, with its second derivatives cancelled by commuting V_a,V_b. The remaining kernel derivatives in (6) are not renamed current derivatives: K was defined before choosing any current X and contains no inserted L or U argument. Dependencies of K on transition/HPL data remain and are differentiated normally.

Therefore the COMPLETE published remainder has the identity

    B_p = pi15 sum_lambda {
              K_lambda(R_alg)
              +D_lambda,P+D_lambda,Q
          }.                                             (7)

Here R_alg is exactly the old tf(G^-1 M)+F_Q k_P,ik+F_P k_Q,ik; M still has all seven kinetic and three negative gerbe terms. The pi15 projection is still applied once after the full sum. No individual summand is declared Laurent. Formula (7) leaves the preceding fluxes G_i unchanged, hence the established pF_spec=sum partial_i G_i+B_p remains valid without another integration by parts.

For an optional visibly combined form, write R_0=tf(G^-1 M). The SAME right side is

    pi15 sum_lambda { K_lambda(R_0)
      + sum_(r,q)=(P,Q),(Q,P) [
          (F_q-2s_q,ij) K_lambda(k_r,ik)
          +2(s_q,ij+s_q,jk) K_lambda(k_r,ij)
          -s_q,jk/2 (K_lambda;a(L_b)-K_lambda;b(L_a))
          +s_q,ij/2 (K_lambda;a(U_b)-K_lambda;b(U_a))
        ] } .                                            (8)

This only collects existing k terms. In particular F_q−2s_q,ij is not asserted zero and is not identified with a new cocycle. Neither delta s=F nor any separate-branch closure is needed anywhere in (6)–(8).

