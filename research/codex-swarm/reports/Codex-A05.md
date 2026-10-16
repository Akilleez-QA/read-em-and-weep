> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

Codex-A05 — **owner-preserving normalization contract; no detector verdict.**

Domain: characteristic zero, actual common vertices \(v=(e,b,m)\), complete corrected \(R^\sharp\). Pin: `08b73637d4136f91606aad332c46cafd064417f8`. Supplied source/model blob IDs verified.

**1. Ownership and Laurent rule.** Index denominator charges by full vertex and factor channel; retain occurrence provenance. Multiplication adds charges, addition uses componentwise maxima. Equal carriers never erase multiplicity. Sort by carrier/mask, then standard tag, auxiliary first; retain alternating signs. Apply nonlinear source formulas in their prescribed source order.

Suppose an authenticated clearing identity is
\[
P=c\prod_o A_o^{p_o},
\]
where \(P\) is homogeneous polynomial, \(c\) has twist \(w\), and \(A_o\) has multidegree \(d_o\). Each occurrence’s weight must satisfy
\[
\rho_o=A_{o,e_o}^{p_o}Q_o.
\]
Then, in the common finite frame,
\[
c\prod_o\rho_o=P(x)\prod_oQ_o(z_{e_o})\prod_i x_i^{-m_i},
\quad
m_i=\sum_{o:e_{o,i}=1}p_od_{o,i}.
\]
Here \(z_{e,i}=x_i\) or \(x_i^{-1}\). Numerator degree is \(w_i+\sum_op_od_{o,i}\); append no extra twist. The exact demand predicate is
\[
a_i+\sum_{e_{o,i}=0}b_{o,i}
-\sum_{e_{o,i}=1}b_{o,i}-m_i=\kappa_i.
\]
An uncanceled denominator means Laurent-polynomial extraction is not yet admitted.

**2. Required factor identities.** Retain:
\[
F_j=v_j^4-\prod_{k\ne j}v_k,\quad
h_j=v_jF_j,\quad a=v_0v_1v_3v_4,\quad
v_j^5=h_j+v_2a.
\]
Primary channels are \((v_j,F_j)\); auxiliary channels are \((v_0,v_1,v_3,v_4)\), including hidden homogenizing \(v_0\) powers. Require the entrywise seed-clearing identities, pivot inverses, determinant-one transition identity, and exact powered carrier/legal partition quotients. Keep inner N14/legal1 distinct from outer54/legal29.

Carrier \(0\) and auxiliary may merge only under the specific selected-row identities in `research/hm/current-scalar-geometric-dependencies/source-identity.md`, §3. They remain distinct general owners.

**3. Cancel before differentiating.** First certify the combined inserted-owner quotient \(U=P/D\), with
\(D=\prod_oA_o^{p_o}\) retaining suffix ownership. For any derivation \(V\),
\[
VU=\frac{D(VP)-P(VD)}{D^2},\qquad
VD=\sum_o p_o(VA_o)A_o^{p_o-1}
\prod_{r\ne o}A_r^{p_r}.
\]
Reduce through certified identities afterward. This retains weight derivatives; separate raw Leibniz pieces need not be regular.

Frozen jets require constant \(N_v=D_v(p)\):
\[
V_Sg^{phys}_{uv}=N_v(V_S\hat g_{uv})N_u^{-1}.
\]
They do not authorize differentiating bare core transitions. The selector conversion \(\bar R_{10}=\nu_a^2R^{phys}_{10}\) cancels exactly once.

Evidence: pinned `research/hm/current-scalar-geometric-dependencies/{frames-and-poles.md,data/source-formulas.js,data/model.json}`; GitHub comments **6141322825, 6142890819, 6205249609, 6205660472**.

Original progress: joined normalization/derivative contract. C01/C04/C10 proposals consumed; their demands still require authenticated owned quotient/support bindings. Reject carrier collapse, unsupported exceptional merger, ambiguous frames, or uncanceled extraction. No arithmetic tests ran.

Reviewer: **Codex-V03/V04, pending**. Next: bind one unreserved demand to these identities and its exact frame/twist ledger. No full-detector nonvanishing or completeness follows.