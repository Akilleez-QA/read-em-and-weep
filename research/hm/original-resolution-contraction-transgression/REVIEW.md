# Independent audit: contraction transgression and the bounded Q2 ansatz

## Verdict and scope

Reviewed analysis proof: `PROOF.md`, SHA-256 `124c816bbc665fa26db60dc02ca3dc6cb34f6cea31982c00093b98e60987d9b3`. This hash was verified against the completed file.

Accepted as an exact regular cochain reduction and as a failure of one explicitly bounded **universal** primitive ansatz. It is not a proof that the actual source residual vanishes, a proof that it does not vanish, or a proof that the contraction contribution and Q2 cannot have another primitive.

The source is Akilleez-QA/read-em-and-weep PR79, frozen at `8fb699a29b10ee6a53af8f74fb5f909e4c82d6e9`. PR1's handoff is [comment 6246445896](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6246445896). Both PRs and the comment were read directly. PR79's returned head matched the requested pin. The ID0 terminal-certificate lane was not duplicated. No repository or external-service writes, physical source evaluation, source-jet construction, source numerical specialization, detector execution, coefficient enumeration, or large computation was performed.

The independent audit checks the source signs, ordered-edge conventions, frame defects, full-cover regularity under the pinned premises, the exact Q2 residual, the complete 24-term sign projection, and two tiny invented controls. The central transgression and rational-control coefficient were independently derived before reading the analysis worker's draft. That draft's physical derivative formulas, closure diagnostic, full-nerve extension, and complete-survivor equations were then separately checked.

## 1. Frozen mathematical inputs

The following files were read at the pin above under `research/hm/null-source-integration/`:

- `complete-raw-remainder/supertrace_projection_followup.md`, especially equations (2), (13)–(18), and (21); Git blob `f606285d39dd59c9d89a69f93761d9374007a777`.
- `complete-raw-remainder/supertrace_projection_review.md`.
- `complete-raw-remainder/PROOF.md`, especially equations (13)–(15).
- `complete-raw-remainder/curvature_descent_followup.md`, especially equations (3), (5), (6), and (8).
- `complete-raw-remainder/pivot_connection_descent.md`, especially equations (12)–(16), (18)–(21).
- `../null-permutation-sector/REVIEW.md`, read separately for the genuine full ordered-nerve extension.
- `closed-k-source-review/REVIEW.md`; Git blob `3616fe3768b5e73b7917c30c82ca6591b0acc043`.

The BI proof at `e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/source-boundary-analysis/PROOF.md` was separately checked for the exact E and row-Cech sign conventions. Previously accepted source regularity and contraction identities are premises, rather than being re-proved by executing their physical model.

## 2. Row transport and the projection defect

On an ordered triple `(i,j,k)`, set `A=g_ij`, `B=g_jk`, `g_ik=BA`, and transport a matrix at j to i by `X_j^i=A^-1 X_j A`. Put

    L_a=A^-1 V_a A,
    U_a=A^-1 B^-1(V_a B)A,
    theta_i=(Gamma_i^0)^t=−kappa_i^t,
    chi_ij=(Q_ij^0)^t.

Here Q is the projection-descent defect, not the kinetic Q2. The accepted column-frame relation is

    G_ij Gamma_j G_ij^-1 − dG_ij G_ij^-1 − Gamma_i = Q_ij,
    G_ij=g_ij^t.

Taking the tracefree part and transposing yields, with no extra scalar connection term,

    theta_j^i − theta_i = L_ij + chi_ij.                 (A)

The corrected induced difference is exactly `z_ij=−L_ij^t`. An untransported-array term `dlog(nu_j/nu_i)I` must not be inserted. Bilinear coefficient traces satisfy `tr(X^t wedge Y^t)=tr(X wedge Y)`; importing the cubic exterior-transpose sign into this bilinear identity would be an error.

Neither theta nor Gamma is being asserted to be the coefficients of one global connection on the cohomology bundle. Equation (A) retains precisely the non-global descent defect chi. Setting chi to zero is an additional assumption and is not valid for the actual source merely because each vertex connection is flat.

## 3. Exact transgression, including every correction

All components are contracted with the physical derivations. For a scalar edge cochain t and pair r=(a,b), define

    [d t wedge X]_ab = (V_a t)X_b − (V_b t)X_a,
    Theta_ij = theta_i + theta_j^i,
    C_ab(t)_ij = (1/2)[d t_ij wedge Theta_ij]_ab.

The source E operator is exactly

    E_ab(t)_ijk = (1/2)[d t_jk wedge L_ij
                                      − d t_ij wedge U]_ab.

The scalar Cech differential is `(delta t)_ijk=t_jk−t_ik+t_ij`; the End differential includes the displayed row transports. Direct expansion, using (A), gives

    delta C_ab(t) = E_ab(t) + B_ab(t),                    (B)

where

    B_ab(t)_ijk = (1/2)[d t_jk wedge chi_ij
                      −d t_ij wedge chi_jk^i
                      +d(delta t)_ijk wedge Theta_ik]_ab. (C)

To verify signs without an informal integration by parts, write x_uv=d t_uv and f=d(delta t). Then `x_ik=x_ij+x_jk−f`. Substituting this into

    2 delta C = x_jk wedge(theta_j^i+theta_k^i)
                −x_ik wedge(theta_i+theta_k^i)
                +x_ij wedge(theta_i+theta_j^i)

leaves `x_jk wedge(delta theta)_ij −x_ij wedge(delta theta)_jk^i + f wedge Theta_ik`, proving (B)–(C). This Cech calculation never differentiates theta or its transport. It therefore creates no missing commutator term at this step. If a later step differentiates `theta_j^i`, its derivative does include `[theta_j^i,L_a]`.

This identity is valid on arbitrary supplied ordered tuples. For the source, use the genuine all-tuples extension `t'=s_raw+delta h_scalar` before the 24-term action. The gerbe edge correction is symmetric under edge reversal, so t' must not first be replaced by a guessed alternating extension. Likewise K alone need not be alternating. The equation-(21) algebra is pointwise on a supplied ordered edge and uses no inequality between labels, so the same formula identifies the genuine extension there. Restrict to increasing tuples only after the full-nerve identities and geometric average. If an independently alternating scalar input is used, C has the corresponding transported alternating behavior, but that is not a premise of (B).

## 4. The exact full remainder reduction

For the complete scalar in equation (21), `delta t'_r=F_r=b_r−c_r`. For complementary pairs p=(a,b), q=(c,d), put

    P_full = C_p(t'_q)+C_q(t'_p),
    N_full = Omega+Q2+Q4−B_p(t'_q)−B_q(t'_p).

Then the exact cochain identity is

    R(t') = delta P_full + N_full.                        (D)

The notation matters: the published raw representative obeys `R(t')=R_raw+delta H`. Thus its corresponding edge reduction is `P_full−H`, not P_full alone.

Let e_sign denote the genuine full 24-term geometric signed action on the unsorted ordered nerve. Because that action commutes with the source differential,

    (1−e_sign)R(t')
      = delta(1−e_sign)P_full + (1−e_sign)N_full.          (E)

For `(1−e_sign)R_raw`, subtract `(1−e_sign)H` from the primitive. Formula (E) uses the full geometric action on all source data, not a class-level three-coset or sorted-coordinate shortcut. It keeps Omega and Q4 and the complete scalar, weighted, gerbe, and contraction data. It neither asserts N_full=0 nor discards a non-closed subexpression.

## 5. Exact Q2 defect for the bounded contraction-only ansatz

Let K_r denote the pair contraction of the full two-term contraction scalar, and Lambda_r=delta K_r. Consider only the bounded ansatz

    P_K = (1−e_sign)[C_p(K_q)+C_q(K_p)]/4.

The exact residual of the proposed equality

    (1−e_sign)[Q2+(E_p(K_q)+E_q(K_p))/4] = delta P_K

is

    D_K = (1−e_sign)[Q2−(B_p(K_q)+B_q(K_p))/4].           (F)

Explicitly, before applying `1−e_sign`, the correction subtracted from Q2 is one eighth of

    (V_a K_q,jk) chi_b,ij − (V_b K_q,jk) chi_a,ij
    −(V_a K_q,ij) chi_b,jk^i + (V_b K_q,ij) chi_a,jk^i
    +(V_a Lambda_q,ijk) Theta_b,ik
    −(V_b Lambda_q,ijk) Theta_a,ik

plus the same six terms with `(a,b,p)` exchanged with `(c,d,q)`. This is an exact displayed failure condition, not an unspecified remainder.

Q2 in (F) is the source's complete expression. With the signed slot list `S={(ac,bd,+1),(ad,bc,−1),(bc,ad,−1),(bd,ac,+1)}`, for each record `(uv,wz,epsilon)` it contributes

    epsilon/8 * {
      [tr(U_u U_v)+tr(U_u L_v)+tr(U_v L_u)] H^0_wz
      −tr(H^0_wz U_u)L_v−tr(H^0_wz U_v)L_u
      +[tr(L_w L_z)+tr(U_w L_z)+tr(U_z L_w)] J^0_uv
      −tr(J^0_uv L_w)U_z−tr(J^0_uv L_z)U_w }.

No source computation establishes that (F) is zero. The accepted result Lambda != 0 does not by itself establish that (F) is nonzero, since its differentiated contractions and other summands could cancel. The ansatz succeeds on the actual source if and only if the complete cochain (F) vanishes there.

For checking the derivatives of Lambda, the accepted column formula becomes in row notation

    Lambda_ijk = −tr(chi_ij wedge U)
                 +(eta_ij/2) wedge[(delta tau)_jk+15q_jk]. (G)

The minus sign is from `z_jk=−U^t`, not from a bilinear trace-transpose sign.

## 6. All physical contraction derivatives remain

Write `T_c=V_c D+2a_c D`. For any complementary derivative V_a,

    V_a K_cd = str((V_a h)T_c Z_d+h(V_a T_c)Z_d+h T_c(V_a Z_d))
      −tr((V_a P)T_c h Z_d I+P(V_a T_c)h Z_d I
           +P T_c(V_a h)Z_d I+P T_c h(V_a Z_d)I
           +P T_c h Z_d(V_a I)) − (c exchanged with d),

and

    V_a T_c = V_a V_c D+2(V_a a_c)D+2a_c(V_a D).

Thus the use of the compressed K scalar suppresses no derivatives of I, P, h, or D. The derivative of the compact scalar's q wedge d_i term retains the derivative of d_i. Only the original isolated q_c q_d gerbe term has zero complementary derivatives by its proved separated-coordinate property. Neither eta, theta, Lambda, nor K inherits that separation.

The use of the derivative identities `V_a L_b=H_ab−L_aL_b` and `V_a U_b=J_ab−U_aU_b+[U_b,L_a]`, if made subsequently, must retain the latter commutator. For example `V_a theta_j,b^i=A^-1(V_a theta_j,b)A+[theta_j,b^i,L_a]`.

## 7. Full-cover regularity and its limits

Under the pinned homogeneous source/physical-frame premises, I_i and P_i are regular in the prescribed local ambient frame on each carrier/legal open, including the accepted infinity charts. Their derivatives and products are regular on that open. If the auxiliary ambient line frame changes, the entire cohomology-containing block has weight one. Consequently `P_i dI_i` changes by a scalar logarithmic derivative times the identity, which disappears from its tracefree part. This proves that theta_i as used here is regular and independent of the auxiliary ambient line trivialization.

The prescribed cohomology frames remain fixed. Recomputing `P_i dI_i` after an arbitrary nonconstant cohomology gauge introduces the usual connection derivative; it is not the same formula under conjugation alone. This audit does not permit that substitution.

K and t' are the accepted tensorial regular scalar cochains; physical vector fields preserve regular functions; transitions and inverses are regular on their legal overlaps. Therefore C(K), C(t'), and their transports are regular on the full source cover. Finite sums and the full 24-term average preserve regularity. No new divisor is inverted by these constructions.

Regularity is not a finite-degree or pole-cutoff certificate. No existing 54/29 detector-domain claim follows for P_full, P_K, or their resolution lifts. No numerical cutoff, detector value, all-order deformation, or algebraicity conclusion is asserted.

## 8. Independent tiny controls

`check_independent_controls.py` contains no physical source data or imported source evaluator. Both tests passed normally and with `python -O`.

1. The transgression identity was checked for all six distinct coordinate pairs using noncommuting determinant-one row transports, arbitrary invented scalar edge-derivative data, and genuinely nonzero chi and d(delta t) corrections. It checks `E=delta C−B` with the exact source ordering and signs.
2. For the rational germs

       A=diag(1+x2*x4,(1+x2*x4)^−1),
       B=diag((1+x1)(1+x3),((1+x1)(1+x3))^−1),

   the origin has L=0, U1=U3=h, H24=H42=h, J13=J31=I, where h=diag(1,−1). Every other distinct-coordinate cross-Hessian is zero. The repeated-coordinate J11 and J33 have nonzero tracefree parts, but never enter these four-distinct-slot formulas or their permutations. The sole contributing source Q2 record is `(13,24,+1)`, giving Q2=h/4. The independent full 24-term sign average is zero.

These germs can be realized by varying only the rank-two cohomology frame in a constant split complex. Then T=K=Lambda=chi=0 identically, so P_K=0. If desired, append constant contractible pairs of ranks 5,8,2 to obtain the exact source block dimensions `(5,15,10,2)` and weights `(−1,1,3,5)`, with constant D,h and `[D,k]=−2D`; the result is unchanged. The remaining split-basis determinant and trace conditions are then also satisfied, with the pivot connections a_i=gamma_i=q_ij=0 (distinct from the germ unit a=1+x2*x4).

Therefore the proposed bounded **universal K-only primitive** fails by precisely h/4 in this invented regular control, including after complementary projection. The actual source has additional special geometric data absent from this control. This is not an actual-source counterexample, not a nonzero cohomology class, and not a claim that Q2 plus the differentiated contraction has no different primitive.

## 9. Checks specific to the analysis proof

The proof's derivative of the first-order curvature scalar is correct:

    V_a c_cd = (1/4)tr{J_ac^0 L_d−J_ad^0 L_c
                        +U_c H_ad^0−U_d H_ac^0
                        −(L_a+U_a)(U_c L_d−U_d L_c)}.

This follows by differentiating `c_cd=tr(U_cL_d−U_dL_c)/4`; the `U_cL_aL_d` transport term cancels the corresponding current derivative, while cyclicity leaves `−L_aU_cL_d`. Trace parts of H and J multiply traceless L and U. Thus no Hessian or transport commutator was omitted. The source b_cd has zero complementary derivatives, so `V_aF_cd=−V_ac_cd` only for the specified complementary slots.

The displayed closure diagnostic also has the correct sign:

    delta E_r(t)_ijkl=−(1/2)[d(delta t)_jkl wedge L_ij
                           +d(delta t)_ijk wedge L_kl^i]_r.

It implies the necessary closure equation for a hypothetical primitive of the isolated Q2/contraction combination, but not its satisfaction or failure. In particular the nonclosedness of K alone remains insufficient.

## Conclusion

The useful output is the exact regular ordered-nerve reduction (D)–(E), and the exact Q2/contraction ansatz defect (F), including its Lambda correction. The tiny control rules out claiming that this particular ansatz is a universal cancellation theorem. The actual remaining 30-dimensional obstruction and a possible more general source-specific global primitive remain undecided.
