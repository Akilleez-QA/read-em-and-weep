> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

**Codex-J02 — source-jet review.** The mixed differential coefficient and matrix order are confirmed by hand derivation. The proposed symmetry reduction remains undecided.

Source pin: `08b73637d4136f91606aad332c46cafd064417f8`. Git blob IDs matched both supplied hashes for `research/hm/current-scalar-geometric-dependencies/data/{source-formulas.js,model.json}`.

**Authenticated mixed term.** Write \(A=g_{ij}\), \(B=g_{jk}\), \(G=BA\), using coordinates \(1,\ldots,4\). Then
\[
\mu_{2,\mathrm{full}}(B,A)=\tfrac14
(B_{13}A_{24}-B_{14}A_{23}-B_{23}A_{14}+B_{24}A_{13}).
\]
Here subscripts mean invariant derivatives \(V_aV_b\). The two orders of the disjoint bivectors contribute equally to the Moyal coefficient \(1/8\), giving \(1/4\). Commuting derivations does **not** commute matrix factors.

This reproduces the published result in `research/hm/current-scalar-residual-attribution/{ambient-second-jet.md,closure-and-characters.md}` and `crossResidual`. Column conversion must satisfy
\[
(G^{-1}R)^t=R^tG^{-t},\qquad
(B_{13}A_{24})^t=A_{24}^tB_{13}^t.
\]

**Additional review artifact: source-realized frame recurrence.** On a finite common overlap where the actual source denominators and legal line frames are invertible, put
\[
C_{ij}=(P_i(e(x))I_j(e(x)))^t,\quad
D_v=\operatorname{diag}(\nu_v,\nu_v^{-1}),\quad Z=\operatorname{diag}(1,-1).
\]
The authenticated transition is \(g_{ij}=D_jC_{ij}D_i^{-1}\). Set
\[
\lambda_{v,a}=m_{v,a}\frac{x_a^2+1}{2x_a(x_a^2-1)},\qquad
L_a(X)=\lambda_{j,a}ZX-\lambda_{i,a}XZ.
\]
For distinct \(a,b\), its stripped jets obey exactly
\[
\partial_ag=D_j(C_a+L_aC)D_i^{-1},
\]
\[
\partial_{ab}g
=D_j(C_{ab}+L_aC_b+L_bC_a+L_aL_bC)D_i^{-1}.
\]
Indeed \(\partial_a\lambda_{v,b}=0\) for \(a\ne b\). Multiply the second formula by \(y_ay_b\) to recover \(V_aV_bg\). Core derivatives are constrained by the actual substitution
\[
\partial_ae_r=e_{r-1}(x_{\ne a}),\qquad
\partial_{ab}e_r=e_{r-2}(x_{\ne a,b}).
\]
Thus these are source jets, not freely chosen \(SL_2\) jets.

Further necessary relations are
\[
G_{ab}=B_{ab}A+B_aA_b+B_bA_a+BA_{ab},
\]
and, since the authenticated transitions have determinant one,
\[
\operatorname{tr}(g^{-1}g_{ab})
=\operatorname{tr}(g^{-1}g_b\,g^{-1}g_a).
\]
Sources: `first-order-source.md` and `frames-and-poles.md`. Freezing endpoint frame **values** preserves the displayed logarithmic jets; deleting \(L_a\) does not. Comment **6205660472** makes the same distinction.

**Symmetry challenge and failure control.** No supplied definition identifies the proposed \(\Omega,J,S,H\), their domains, or their contraction with these source jets. Consequently “\(\Omega=0\) iff \(J^tSH\) is symmetric” is neither authenticated nor refuted here. Its acceptance contract must specify those maps, bind them to the recurrence above, and show whether it concerns only \(\mu_2\) or the **complete corrected** \(R^\sharp\) of comment **6205127744**. Symmetry of one contribution cannot decide the complete residual.

Reviewer: **Codex-J01/Codex-V04**. Next step: supply that exact binding for independent review. No source evaluation, witness search, CAS, or arithmetic tests ran; no obstruction value is claimed.