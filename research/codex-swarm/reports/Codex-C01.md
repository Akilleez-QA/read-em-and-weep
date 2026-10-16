> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

Codex-C01 — symbolic contract for q=2, E12, canonical ranks [0,3). No source evaluation or exclusion scan performed.

At pin `08b73637d4136f91606aad332c46cafd064417f8`, comments #6141530883/#6205341120 specify κ=(−1,−2,−2,−2), cell CCBB. With standard bits weighted (8,4,2,1), the assigned ranks are:

| Rank | Terminal entry | Staircase | Sign |
|---|---|---|---|
| 0 | M11[9,3] | (3,11,15) | + |
| 1 | M11[9,3] | (3,7,15) | − |
| 2 | M11[10,4] | (3,11,15) | + |

These are canonical ranks, not upstream seed numbers.

For each staircase sample three full vertices v_l=(e_l,b_l,m_l). There are 16 standard tags, six carriers ordered (*,0,1,2,3,4), and 16 legal masks: 1,536 common vertices. Outer54/legal29 weights permit only b=* or b≤s and masks zero on finite coordinates, where s=|e|. Here s=(2,3,4), giving respectively 16,40,96 possible labels, hence 61,440 raw assignments per rank before further zeros. This is a label bound, not occupied support.

Sort sampled vertices by **carrier, mask, standard tag**; multiply by the sorting parity ε. Form nonlinear sources only in that source-first order. Preserve full vertex owners and repeated denominator multiplicities. Equal carriers alone give no q=2 exclusion; distinct standard tags cannot be collapsed.

For sorted vertices (a,b,c), terminal indices (r,t), define
\[
\mathcal C(X)=(I_aX^tP_a)_{r,t},\quad
J_d=g_{ab}^{-1}V_dg_{ab},\quad
Q_d=g_{ac}^{-1}V_dg_{ac}-J_d .
\]
Then the exact E12 demand is
\[
\mathcal C(E_{12}s)=\tfrac12[
 \mathcal C(J_2)V_1s_{bc}
-\mathcal C(J_1)V_2s_{bc}
+\mathcal C(Q_1)V_2s_{ab}
-\mathcal C(Q_2)V_1s_{ab}],
\qquad s=T_{34}F_{34}.
\]
Multiply by the terminal sign, ε, and the three outer weights, then request coefficient κ. This yields four signed scalar derivative-demand families per label assignment. Dimensions are I:15×2, P:2×15, and J,Q:2×2. In particular,
\[
\mathcal C(X)=\sum_{\alpha,\beta=0}^1
 I_a[r,\alpha]P_a[\beta,t]X[\beta,\alpha].
\]

**Factored separating-support rule.** For each family retain every weight, selector, current, and canceled inner quotient as a separate factor. With certified finite supports S_f, retain only tuples satisfying
\[
\sum_f e_f=\kappa,\qquad e_f\in S_f.
\]
An empty demand fiber certifies zero. Coordinate interval separation is sufficient; overlapping intervals prove nothing. In the homogeneous outer representation use exactly #6205249609’s predicate
\[
p_i+\sum_{\rm finite}a_{\ell i}
-\sum_{\rm infinity}a_{\ell i}-m_i=\kappa_i,
\]
with its owned m_i and no additional twist. Differentiate inner N14 expressions **after inserted-owner cancellation**, retaining weight and physical-frame derivatives.

Evidence: hand composition of published rules, not a new tested calculation. Pinned `research/hm/current-scalar-geometric-dependencies/data/source-formulas.js` and `data/model.json` blob IDs match the supplied IDs; signs and domain follow #6205127744, #6205249609, #6205660472. Original progress is the rank-specific four-family demand above.

Reviewer: Codex-V01/Codex-V02, pending. Unresolved: unpublished incumbent fingerprint and canceled-quotient support binding. Next step: authenticate that binding against these ranks, owners, and signs; then apply the empty-fiber rule. No instantiated exclusion, nonzero detector, or completeness proof is claimed.