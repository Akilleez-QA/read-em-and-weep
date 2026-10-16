# Independent review of the supertrace projection

Reviewed on 2026-10-16: `supertrace_projection_followup.md`, SHA-256 `4746299d43310e2ab39010f8ee8704ff3459d97e2ea4500e45911e37effa095e`.

## Verdict

Accepted under the source premises stated in the note. The physical cohomology normalization, the row/column transpose sign, both surviving differential-defect terms, and the weighted-supertrace localization are correct. The compact ordered-edge representative (21) follows with the displayed signs and factors.

The full-complex term K_h remains necessary. Neither this identity nor its invented controls establish its vanishing, a global boundary, source symmetry, or a finite-cutoff certificate. The note states those limits accurately.

This review is a mathematical check of the pinned source conventions and displayed identities. No physical source matrix, polynomial, jet, or overlap was evaluated. The accompanying tiny invented-complex test was read; its already reported executions were not repeated.

## 1. Physical cohomology frames and the transpose

The crucial normalization is the whole ambient transport, not just the scaling of the split columns. The [pinned first-order source, sections 1 and 4](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md) supplies the own-frame cohomology columns

    I_alg,i diag(1,nu_i^(-2)).

Their ambient complex term has line weight +1. Transport to the common reference multiplies the entire block by nu_i, yielding

    I_i=I_alg,i diag(nu_i,nu_i^(-1)),
    P_i=diag(nu_i^(-1),nu_i) P_alg,i.

Thus P_i I_j is precisely the physical determinant-one column transition G_ij=g_ij^t. A scalar factor nu_i/nu_j would arise only from comparing the own-frame columns without the ambient transport. The note correctly excludes that comparison.

The split connection makes I_i parallel. Therefore the difference of the two induced split connections, expressed in the i-frame, has coefficient

    z=P_i Z_ij I_i=-dG_ij G_ij^(-1).

Since G_ij=g_ij^t, transposition reverses the product, giving z=-(g_ij^(-1)dg_ij)^t=-L_ij^t. There is no extra central logarithmic derivative.

In the same fixed physical frame, A_i=Omega_i-k a_i and Omega_i I_i=-dI_i. Since k is +1 on the middle block,

    P_i A_i I_i=-P_i dI_i-a_i I_2.

Taking the tracefree part proves (15). Furthermore S=2A_i+Z+k eta/2 gives s^0=2kappa_i+z. Because tr(z wedge z)=0 coefficientwise,

    (1/2)tr(s^0 wedge z)=-tr(kappa_i wedge L_ij^t).

These statements require the fixed parallel cohomology basis specified in section 5. The note correctly does not transport the derivative formula for kappa unchanged under a new nonconstant cohomology gauge.

## 2. Supertrace and differential-defect signs

For internal-degree-zero X, the contraction identity and graded cyclicity give

    str((1-IP)X)=str(DhX+hDX)
                =-str(hXD)+str(hDX).

Both D and hX are odd, which is the origin of the minus. Thus str(X)=tr(PXI)+str(h[D,X]). This calculation is coefficientwise and adds no exterior or Čech sign.

Inserting IP+Dh+hD between A and B in PAB I yields

    P A D h B I=-P[D,A]h B I,
    P A h D B I=P A h[D,B]I.

These verify all signs in (5). When [D,B]=0, the surviving correction is exactly

    str(h[D,A]B)-tr(P[D,A]h B I).

Neither surviving term can be discarded solely because B is a chain map.

For the actual pivot connections, [D,k]=-2D and flat split compatibility give

    [D,A_i]=dD+2a_i D=T_i,
    T_i-T_j=eta D.

Hence Z=A_j-A_i-k eta/2 is a chain map, while [D,S]=2T_bar. Antisymmetrizing the preceding product identity and dividing by two gives exactly K_h(T_bar,Z), with a plus supertrace term and a minus projected trace term as in (2).

The determinant reduction and str(k)=0 give str(A_i)=str(Z)=0. Since Z is a chain map, tr(PZI)=str(Z)=0. This justifies using s^0 in the rank-two product; it does not imply s itself is traceless.

## 3. Weighted localization to the first vertex

Apply the coefficientwise projection identity to kZ. Cohomology has weight +1, so tr(PkZI)=tr(z)=0. With [D,Z]=0,

    str(kZ)=-2str(hDZ).

Independently, str(k^2)=-30 and Z=A_j-A_i-k eta/2 give

    str(kZ)=tau_tilde_j-tau_tilde_i+15eta.

Therefore

    str(hDZ)=-(tau_tilde_j-tau_tilde_i)/2-(15/2)eta.

The signs in (17) are correct. Since T_bar=T_i-eta D/2 and PD=0,

    K_h(T_bar,Z)=K_h(T_i,Z)
                  +(eta/4) wedge(tau_tilde_j-tau_tilde_i).

The eta wedge eta term vanishes. The ordinary-wedge identity (11) subtracts eta wedge(tau_tilde_i+tau_tilde_j)/4. Combining the two leaves -eta wedge tau_tilde_i/2, exactly as in (18).

## 4. Final scalar formula and control

Substituting (18) in the pivot-descent representative and using tau_tilde_i=tau_i-30d_i leaves the scalar-form terms

    (eta/2) wedge tau_j+15eta wedge d_i+30d_i wedge d_j.

Because eta=q+2(d_j-d_i),

    15eta wedge d_i+30d_i wedge d_j=15q wedge d_i.

This verifies the coefficient +15 and the first-endpoint ordering in (21). The original -15q_c q_d/8 term is retained. The expression is valid on the specified increasing edges with the admitted alternating extension; it does not change the source ordering.

The tiny control in section 8 is consistent: on its single contractible pair, h=1/r, T_x=1 and Z_y=1/u give str(hT_xZ_y)=1/(ru), while the projected correction and induced z vanish. Direct multiplication also gives W_xy=1/(ru). It correctly demonstrates that the algebraic defect term can survive the stated chain-map and trace conditions, without deciding a source-specific cancellation or global class.

Applying complementary E operators still differentiates the actual moving I, P, h, D, connection coefficients, and currents. Neither eta nor q wedge d_i has the vanishing derivative property of the isolated original q_c q_d term. The note preserves these obligations and makes no unsupported cutoff or vanishing claim.
