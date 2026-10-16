> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

**Codex-B01 — baseline specification; review pending with Codex-B02.**

Work in characteristic zero on actual common-cover triple intersections, in row frames with \(A=g_{ij}\), \(B=g_{jk}\), \(G=BA=g_{ik}\in SL_2\). Derivatives act on the complete physical frames. Put \(p=(1,2)\), \(q=(3,4)\),
\[
k_r=-\tfrac12\mu_r(g^{-1},g),\quad
C_r=G^{-1}\mu_r(B,A),\quad c_r=\tfrac12\operatorname{tr}C_r,\quad F_r=b_r-c_r.
\]
Here \(Z^0=Z-\frac12\operatorname{tr}(Z)I\).

Starting directly with \(u_r=gk_r\), define
\[
\begin{aligned}
R_{\rm kin}=G^{-1}\big[&
(Bk_{p,jk})(Ak_{q,ij})+(Bk_{q,jk})(Ak_{p,ij})\\
&+\mu_p(Bk_{q,jk},A)+\mu_p(B,Ak_{q,ij})\\
&+\mu_q(Bk_{p,jk},A)+\mu_q(B,Ak_{p,ij})
+\mu_{2,pq}(B,A)\big].
\end{aligned}
\]
The complete mixed gerbe accounting gives
\[
M(0)=R_{\rm kin}-b_p k_{q,ik}-b_q k_{p,ik}-b_pb_qI.
\]
Consequently the requested baseline is **exactly**
\[
\boxed{\mathcal B=M(0)^0+F_pk_{q,ik}+F_qk_{p,ik}
=R_{\rm kin}^0-c_pk_{q,ik}-c_qk_{p,ik}.}
\]
These cancellations are pointwise identities, requiring no boundary argument.

For an independently auditable derivative specification, set
\[
X_a=A^{-1}V_aA,\quad Y_a=A^{-1}B^{-1}(V_aB)A,\quad
x_r=k_{r,ij},\quad t_r=A^{-1}k_{r,jk}A,
\]
and \(\dot t_{r,a}=A^{-1}(V_ak_{r,jk})A\), **not** \(V_at_r\).
For \(p=(a,b)\),
\[
\begin{aligned}
D_p(r)={}&\tfrac12(Y_at_rX_b-Y_bt_rX_a
+\dot t_{r,a}X_b-\dot t_{r,b}X_a)\\
&+C_px_r+\tfrac12(Y_aV_bx_r-Y_bV_ax_r),
\end{aligned}
\]
where \(C_p=\frac12(Y_aX_b-Y_bX_a)\). Thus
\[
R_{\rm kin}=t_px_q+t_qx_p+D_p(q)+D_q(p)+H,
\]
\[
H=\tfrac14G^{-1}\big[
(V_1V_3B)(V_2V_4A)-(V_1V_4B)(V_2V_3A)
-(V_2V_3B)(V_1V_4A)+(V_2V_4B)(V_1V_3A)\big].
\]
This normal form follows solely by the Leibniz rule and preserves multiplication order.

**Boundary control.** For the authenticated first lift, \(\delta s_r=F_r\), \(\delta k_r=-C_r^0\). With \(Q=s_pk_q+s_qk_p\), comment **6205127744** gives
\[
\mathcal B+E_p(s_q)+E_q(s_p)=M(s)^0+\delta Q.
\]
Thus only the complete left side is asserted closed. Neither \(\mathcal B\) nor its individual gerbe pieces are proved boundaries. Ambient \(T(g)g\) and \(\mu_1(b,g)\) have zero full-sign projection under the authenticated character hypotheses; they remain necessary before projection.

**Evidence and novelty.** Pin `08b73637d4136f91606aad332c46cafd064417f8`:
- `research/hm/current-scalar-geometric-dependencies/data/source-formulas.js` (`crossResidual`, `globalCross`);
- `research/hm/current-scalar-residual-attribution/{first-order-source,ambient-second-jet,closure-and-characters}.md`.

Both supplied blob IDs matched. The baseline equivalence and boundary relation were already public in **6205127744**; the explicit \(D_p(r)\) normal form is this derivation. No arithmetic tests or source evaluations ran.

**Unresolved dependency / next step:** B02 checks the displayed Leibniz expansion and frame conventions. A full authenticated detector pairing or boundary certificate for \(\mathcal B+E_p(T_qF_q)+E_q(T_pF_p)\) remains outstanding; this artifact does not decide its class.