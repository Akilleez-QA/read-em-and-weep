# Raw connection transgression: complementary derivatives and the exact frame defect

## Result

This continues the complete-remainder formula without changing its published proof or tests. It gives four new formula-level reductions:

1. The raw edge gerbe correction contributes **exactly zero** to both complementary operators E, by the actual coordinate dependence of q.
2. The theta-linear part of those operators depends only on weighted split-determinant Hessians. Under the accepted complete-cover and physical-frame premises, these reduce further to mixed logarithmic Hessians of the source's pivot coordinate.
3. A local split-connection rewrite removes an explicit scalar coboundary, but its candidate edge primitive has a computable frame defect. It cannot be declared a global boundary without canceling that defect.
4. The obstruction to simply replacing the four connection blocks by their cohomology block is an explicit contraction involving the covariant derivative of the actual complex differential.

These statements do not prove that the complete remainder is a global boundary. No physical matrix, polynomial, jet, coefficient, or owner list is evaluated, and no new runtime or test is used.

## 1. Source conventions

The inputs are the [original first-order source, §§1–4](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md), its [physical frame theorem, §§1–2,4](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/frames-and-poles.md), and [BI, equations(1),(2),(7)](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/source-boundary-analysis/PROOF.md).

Use block labels r=0,1,2,3, signs sigma=(-,+,-,+), ranks n=(5,15,10,2), and line weights k=(-1,1,3,5). To avoid confusing the rank-two transition with a split basis, denote the source's two nontrivial split matrices U0 and U1 by S_i and T_i here. The extreme split matrices are identities. In the prescribed physical vertex frame,

    B_i^(r) = -(d U_i^(r))(U_i^(r))^(-1) - k_r gamma_i I.

Every product of B matrices is taken in the same ambient physical block frame. They are differences of connections and hence tensorial. The common frame's coordinate derivatives are physical; all transport derivatives are retained.

For a pair (c,d), define

    W_ij;cd = sum_r sigma_r tr(B_i,c^(r) B_j,d^(r)
                              - B_i,d^(r) B_j,c^(r)),
    tau_i,c = sum_r sigma_r k_r tr(B_i,c^(r)).

The exact raw scalar is

    s_raw,cd,ij = W_ij;cd/4
      + [q_c,ij(tau_i,d+tau_j,d)-q_d,ij(tau_i,c+tau_j,c)]/8
      - 15 q_c,ij q_d,ij/8.                                  (A)

Here q is the old half-N-squared connection-difference cocycle from the source, after physical contraction. It is not dlog(nu), the logarithmic derivative of the refined line-frame ratio.

## 2. Complementary differentiation removes the edge gerbe term exactly

Take a distinct coordinate a outside {c,d}. The actual source gives

    q_c,ij = (mask_j[c]-mask_i[c]) y_c/x_c,

so V_a q_c,ij=V_a q_d,ij=0. The coordinate transport at infinity preserves this separated dependence. Consequently

    V_a s_raw,cd,ij = (V_a W_ij;cd)/4
      + [q_c,ij V_a(tau_i,d+tau_j,d)
         - q_d,ij V_a(tau_i,c+tau_j,c)]/8.                    (B)

The last term of(A) was retained and differentiated; its derivative is zero. The same argument applies to both E_p(s_raw,q) and E_q(s_raw,p), because p and q are disjoint. It does not permit omitting the edge correction from the first-order scalar equation itself.

The first derivative in(B) is explicitly

    V_a W_ij;cd = sum_r sigma_r tr(
        (V_a B_i,c) B_j,d + B_i,c(V_a B_j,d)
       -(V_a B_i,d) B_j,c - B_i,d(V_a B_j,c)).                 (C)

For each block the old connection is locally scalar and flat, and the split connection is flat. Thus

    V_a B_i,c - V_c B_i,a = -[B_i,a,B_i,c].                  (D)

In particular V_a tr(B_i,c)=V_c tr(B_i,a). These equations constrain the actual block derivatives; they are not declarations that complementary scalar derivatives are arbitrary.

## 3. The theta-linear derivative is a split-determinant Hessian

Since sum_r sigma_r n_r k_r^2=-30, the weighted trace is exactly

    tau_i = -dlog det(S_i) + 3 dlog det(T_i) + 30 gamma_i.     (E)

Here dlog det(U) means tr(U^(-1)dU), an algebraic rational one-form. No logarithm branch or logarithmic extension is introduced. It must not be confused with the unweighted supertrace: sum_r sigma_r n_r k_r=0 is a different identity.

For complementary directions a,c, V_a gamma_i,c=0. Hence, without any determinant gluing argument,

    V_a tau_i,c = -V_a tr(S_i^(-1)V_c S_i)
                  +3 V_a tr(T_i^(-1)V_c T_i).               (F)

This already replaces all theta-linear scalar uncertainty by two particular source determinants.

### Further reduction under the accepted complete-cover/frame premises

The source supplies an elementary determinant identity before any polynomial evaluation. If j(i) is the pivot, each five-dimensional block of (W,eta) has determinant plus or minus 1/v_j. The two blocks therefore give

    det(T_i) = epsilon_i nu_i^4 / v_j(i)^2,                  (G)

with a constant sign epsilon_i. The nu^4 factor is exactly the two physical eta-column factors nu^2. The physical columns of S_i have total nu power -10-2+16=4 as well.

For two carriers on the same physical line chart, their change of split bases is a chain automorphism of the same constant split complex. The paired contractible determinants cancel. With the extreme split bases fixed, this gives

    [det(S_j)/det(T_j)]/[det(S_i)/det(T_i)]
       = det(cohomology change of frame) = 1.                (H)

The last equality is the accepted determinant-one transition identity; transpose or inverse conventions do not change it. The common nu^4 factors make the ratio independent of the legal line mask.

The six carrier opens are complete for an elementary reason. Their primary equations are h_j=v_j(v_j^4-product_(k!=j) v_k), and the auxiliary equation is v0 v1 v3 v4. If some homogeneous coordinate is zero, choose a nonzero v_i; the product over its other coordinates contains the zero, so h_i=v_i^5 is nonzero. If all coordinates are nonzero, the auxiliary equation is nonzero. Thus these opens cover P4 and their pullbacks cover X. On each elliptic factor the legal opens C minus {infinity} and C minus {(0,0),(1,0),(-1,0)} also cover C, so their product refinement remains complete.

The global step uses the full source premises, not just(H): under the published homogeneous primitive and physical-frame identities, the U and Q constructions are regular inverse matrices on their own carrier/legal opens, and the physical-frame theorem proves their agreement as rational matrices at infinity before differentiation. The determinant ratio therefore glues to a nowhere-zero regular function on the connected proper product of elliptic curves. Such a function is constant. Equivalently, this is the determinant-line isomorphism for the split complex: its contractible factors cancel, the complex's total line weight is zero, and det(E) has the specified determinant-one trivialization.

Thus dlog det(S_i)=dlog det(T_i), and(E) becomes

    tau_i = 2 dlog det(T_i) + 30 gamma_i.

Combining this with(G), and using that log(nu_i) is a sum of single-coordinate terms, gives the particularly small source identity

    V_a tau_i,c = -4 V_a V_c log(v_j(i)),   a != c.           (I)

This statement is in the source's prescribed physical vertex frames. It does not erase the extreme split-basis transformations when one makes an arbitrary auxiliary change of common frame. At infinity v_local=tau_chart v_affine, where tau_chart is a product of single-axis coordinates, so its mixed logarithmic Hessian is zero. Thus(I) is compatible with the accepted physical coordinate transport. A finite-chart pivot v0=1 has zero such Hessian there; this is not a claim that a homogeneous coordinate is globally the constant1.

If the complete-cover/regular-unit premises are not being admitted in another application, retain(F) and(H) and mark the passage to(I) conditional. They are not consequences of rank two alone.

Writing P_i;ac=V_aV_c log(v_j(i)), equation(B) becomes

    V_a s_raw,cd,ij = (V_a W_ij;cd)/4
       - [q_c,ij(P_i;ad+P_j;ad)
          -q_d,ij(P_i;ac+P_j;ac)]/2.                        (J)

Inserting(J), with both endpoint terms and the actual physical currents, in the already proved E formula is an exact source-specific replacement for BOTH opaque E(raw) terms. The remaining four-block contribution is(C), not an arbitrary scalar derivative.

## 4. The tempting connection primitive and its exact defect

Work locally in one auxiliary common line trivialization alpha. Write gamma_i^alpha for the connection coefficient of the i-th old connection in that reference frame, and set

    Omega_i^(r),alpha = B_i^(r) + k_r gamma_i^alpha I.

These are the actual split-connection coefficients in that frame. The old connection differences give

    gamma_j^alpha - gamma_i^alpha = -theta_ij,
    theta_ij,c = q_c,ij/2.

In this section wedge is ordinary form wedge with the source's Alexander–Whitney endpoint order. Direct expansion, with sum sigma n k^2=-30, yields

    sum_r sigma_r tr(B_i^(r) wedge B_j^(r))
       + theta_ij wedge(tau_i+tau_j)
     = sum_r sigma_r tr(Omega_i^alpha wedge Omega_j^alpha)
       +30 gamma_i^alpha wedge gamma_j^alpha
       -delta(gamma^alpha wedge tau)_ij.                    (K)

Both mixed transgression terms are present in this calculation. Define

    f_cd,i^alpha = (1/4) i_(V_c wedge V_d)
                              (gamma_i^alpha wedge tau_i),
    t_cd,ij^alpha = (1/4) i_(V_c wedge V_d)[
          sum_r sigma_r tr(Omega_i^alpha wedge Omega_j^alpha)
          +30 gamma_i^alpha wedge gamma_j^alpha]
          -15 q_c,ij q_d,ij/8.

Then locally

    s_raw,cd = t_cd^alpha - delta f_cd^alpha.                 (L)

The BI identity therefore provides the explicit local row-End edge correction

    K^alpha = B_p(f_q^alpha) + B_q(f_p^alpha),
    E_p(s_raw,q)+E_q(s_raw,p)
      = E_p(t_q^alpha)+E_q(t_p^alpha)-delta K^alpha,           (M)

where BI's B_ab(f)_ij is

    [(V_b f_i+V_b f_j)L_a,ij
       -(V_a f_i+V_a f_j)L_b,ij]/2.

The frame defect is explicit. If the auxiliary common line trivialization changes so that gamma_i^beta=gamma_i^alpha+rho for every i, tau_i is unchanged, and

    f_cd,i^beta-f_cd,i^alpha
        = (1/4) i_(V_c wedge V_d)(rho wedge tau_i).           (N)

Consequently

    K^beta-K^alpha = B_p(Delta f_q)+B_q(Delta f_p).            (O)

The physical rank-two transition frames are held fixed in this auxiliary comparison. If they are changed too, their ordinary conjugation/transport must additionally be included.

For a separated physical line-frame change, complementary V_a rho_c=0. Equations(I) and(N) then give the sharper defect

    V_a Delta f_cd,i = -rho_c P_i;ad + rho_d P_i;ac.          (P)

This is generally an expression requiring proof, not a certified zero. Here rho is the logarithmic derivative of the actual frame change; it is not theta=q/2. In particular one cannot identify the local f_i^alpha with a global regular scalar0-cochain simply because the connections are locally flat.

On the symmetry locus Omega=0, the new explicit local target is

    Q2+Q4+E_p(t_q^alpha)+E_q(t_p^alpha)=delta P_hat^alpha,

with compatibility

    P_hat^beta-P_hat^alpha = K^beta-K^alpha

up to a correctly handled closed edge correction. Then P=P_hat^alpha-K^alpha would be a global primitive. Establishing that cancellation and regularity is an additional source identity. The local rewrite alone does not provide it.

## 5. Why the four split blocks cannot simply be collapsed to E

The original transgression proof passes from the supertrace to the cohomology trace only for products of connection **differences that are chain maps**. Individual B_i or Omega_i coefficient matrices are not asserted to be chain maps.

There is an exact source-bound description of the omitted terms. Let D be the actual complex differential, h_j its accepted contraction, E_j=I_jP_j=1-Dh_j-h_jD, and put

    T_j,a = [D,B_j,a] = (nabla_old,j,a D).

The last equality follows from [nabla_old,j+B_j,D]=0. Define C_ij=P_i I_j and C_ji=P_j I_i. Then

    P_i B_j,a I_i - C_ij(P_j B_j,a I_j)C_ji
      = P_i h_j T_j,a I_i - C_ij P_j T_j,a h_j I_i.          (Q)

Proof: insert E_j on both sides of B_j,a. The difference is

    P_i(1-E_j)B_j,a I_i + P_i E_j B_j,a(1-E_j)I_i.

Use P_iD=DI_i=0, P_i(1-E_j)=P_i h_jD and (1-E_j)I_i=Dh_jI_i. Commuting D past B_j,a gives exactly(Q), with its displayed minus sign.

Thus a reduction of the remaining four-block term(C) to rank-two current formulas must also control these explicit covariant-differential/contraction terms. Setting them to zero would add an unproved source identity. They are precisely the extra connection data excluded from the older transition-local two-jet no-go, so that no-go does not decide the present route either.

The concrete progress is(J), the local boundary(M), and the exact compatibility defect(O)–(P), together with the projection correction(Q). The complete global boundary remains unproved.
