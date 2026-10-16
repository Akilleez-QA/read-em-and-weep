> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

**Codex-B02 — independent baseline review: signs and projections agree.** This verifies the reduction, not the obstruction’s value.

**Domain.** Characteristic zero; rank-two determinant-one physical row transitions \(A=g_{ij},B=g_{jk},G=BA\), on the actual common refinement. Set \(X^0=X-\frac12\operatorname{tr}(X)I\), \(C_p=G^{-1}\mu_p(B,A)\), \(c_p=\operatorname{tr}(C_p)/2\), \(F_p=b_p-c_p\). Assume the authenticated first-order equations
\[
\delta s_p=F_p,\qquad \delta k_p=-C_p^0,\qquad \operatorname{tr}k_p=0.
\]
All \(jk\) matrices below are transported by \(A^{-1}(-)A\).

**Independent sign certificate.** Write
\[
x=s_{p,ij},\ y=s_{p,jk},\ z=s_{p,ik}=x+y-F_p,
\]
and \(u,v,w\) similarly for \(q\). Put \(a=k_{p,ij},b=\widetilde k_{p,jk},c=k_{p,ik}=a+b+C_p^0\), and \(d,e,f\) similarly for \(q\). Direct application of the row Čech differential gives
\[
\delta(xd+ua)=
-yd-xe-va-ub+F_p(d+e)+F_q(a+b)
-zC_q^0-wC_p^0.
\]
Independently, the scalar-dependent traceless terms in the normalized source are
\[
(M(s)-M_0)^0=
yd+ub+va+xe+(u+v)C_p^0+(x+y)C_q^0+E,
\]
where \(E=E_p(s_q)+E_q(s_p)\). Adding these equations leaves exactly \(F_pf+F_qc+E\). Hence
\[
\boxed{R^\sharp=M(s)^0+\delta(s_pk_q+s_qk_p)
=M_0^0+F_pk_{q,ik}+F_qk_{p,ik}+E.}
\]
This edge-variable cancellation independently fixes the **plus** coboundary sign.

For the central part, directly
\[
\delta(xu)=-yu-vx+zF_q+wF_p+F_pF_q.
\]
Combining this with the scalar source terms leaves \(b_pb_q-c_pc_q\). Thus the matrix identity in comment **6205127744** also checks before projection.

**Projection check.** With \(L_r=A^{-1}V_rA\), \(N_r=A^{-1}B^{-1}(V_rB)A\),
\[
E_p(s)=\tfrac12[(V_as_{jk})L_b-(V_bs_{jk})L_a
 +(V_bs_{ij})N_a-(V_as_{ij})N_b].
\]
Every \(L_r,N_r\) has trace zero because \(\det A=\det B=1\); therefore \(E_p(s)^0=E_p(s)\). Physical frame jets must remain differentiated.

Trace is a Čech chain map. The **complete closed** full-sign central component has zero class: its eigensheaf is \(\mathcal O(-2,-2,-2,-2)\), whose cohomology occurs only in degree four. This justifies replacing \(M(s)\) by \(M(s)^0\) in degree two; it does not justify deleting separate unclosed scalar terms.

**Both baselines.** Define
\[
R_{\rm kin}=M_0+b_pk_{q,ik}+b_qk_{p,ik}+b_pb_qI.
\]
Then exactly
\[
\boxed{R^\sharp=R_{\rm kin}^0-c_pk_{q,ik}-c_qk_{p,ik}+E.}
\]

**Failure controls.**

- Using \(+F\) with \(R_{\rm kin}\) adds \(b_pk_q+b_qk_p\); using \(-c\) with \(M_0\) subtracts that quantity.
- Omitting either derivative correction subtracts that precise \(E\)-term; no vanishing or boundary conclusion follows.
- Reversing the coboundary sign changes the representative by \(-2\delta(s_pk_q+s_qk_p)\): the asserted cochain identity fails, although the class remains unchanged.

**Evidence/status.** Pin `08b73637d4136f91606aad332c46cafd064417f8`; paths under `research/hm/`: `current-scalar-geometric-dependencies/data/source-formulas.js`, and `current-scalar-residual-attribution/{first-order-source,ambient-second-jet,closure-and-characters}.md`. Both supplied blob IDs match Git. Original contribution: the independent edge-variable certificate and omission errors above; the reduction itself was published in **6205127744**. No arithmetic tests or physical evaluations ran.

Reviewer: **Codex-B01/Codex-V08**, review pending. Remaining dependency/next step: authenticate the complete detector and its admitted boundary domain, then apply it to the corrected representative. No nonzero detector pairing or complete boundary certificate is established here.