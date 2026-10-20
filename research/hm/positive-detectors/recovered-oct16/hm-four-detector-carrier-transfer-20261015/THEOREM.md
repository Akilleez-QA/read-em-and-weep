# Four current detector rows: signed six-carrier comparison

## Result and scope

The generic chain-map argument closes the current four-detector comparison. It does not require the older nine-entry positive detector. For each of the retained h,j,p,r rows, the complete trace-free old lift, followed by the authenticated legal-mask projection, yields a closed scalar Cech4 cochain on the six carriers. Its actual target coefficient is the signed staircase/determinant formula below. Six rational cochain entries suffice per detector and may be reused across the24 staircases. Their arithmetic, partition acquisition, exact Laurent extraction, widths and memory are still unpriced.

This is a comparison of the full obstruction class. It does not preserve individual old/fresh branches or transfer prior branchwise exclusion inventories to the new representative.

## 1. The rows and global line bundle

Use the original finite output frame and zero-based row/column indices. At internal degree−2 write F20:K2→K0 and F31:K3→K1. The retained rows are

- Lh=F31[0,1]−F20[2,6]−F20[3,9];
- Lj=F31[1,1]−F20[3,7]−F20[4,5];
- Lp=F31[5,0]+F20[1,3]+F20[4,2];
- Lr=F31[6,0]+F20[0,3]+F20[2,4].

Set each row to zero on other internal degrees. The independently authenticated source row check proves Ld_End=0 for all ten elementary W:K3→K0, using d_End W=(W ev,gamma W). It is an identity in homogeneous v, not a numerical check of a residual. See ../hm-terminal-demand-independent-20261015/SOURCE-ROW-AUTHENTICATION.md.

Local annihilation alone would not suffice for a global statement. The required additional equation is supplied by the pinned frames-and-poles.md §2: EVERY internal-degree r coefficient of the included original-frame complex transforms on an infinity-coordinate subset S by

c_S=τ^(r−2)c(x_i=1/t_i),  τ=product_(i in S)t_i.

This follows there from the homogeneous primitive degrees, opposite physical inclusion/projection factors, one τ^-1 per HPL homotopy, and full-sign stripping τ^-2. Section4 supplies the included-tail diagonal-line cancellation and line-independent prefix. Consequently all twelve entries above at r=−2 share τ^-4. Their constant linear combinations glue into F=O(-4,-4,-4,-4). No extra endpoint-dependent line factor is inserted into a row. The row identity therefore gives a global map of complexes End(K)_fullsign→F placed in degree−2. This does not assert row completeness or nonvanishing of their values.

## 2. Full total-complex naturality

Let J be the COMPLETE closed total lift, including its Cech5/internal−3 term. In the pinned convention δJ2=d_End J3, hence δL(J2)=0. For a total boundary J'-J=DB, its internal−2/Cech4 component is δB_(3,−2) plus a signed incoming d_End term. Applying L kills that incoming term, leaving δL(B_(3,−2)). Thus the scalar class is unchanged. The bottom component is used in proving closedness; it is not dropped without justification.

The old trace-free replacement has already been authenticated by its rho62 primitive, and old/fresh lifts represent the same full-sign class. Apply the global row to that comparison. This establishes equality of the actual four scalar cohomology classes with the chosen trace-free old representative. There is no need to borrow a certificate for a different row.

Let Jbar=Pi_L J on the genuine old (b,m) source domain. Pi_L is a scalar weighted sum with a regular ordered prism, commuting with both the Cech and internal differentials. Since L is O-linear and globally equivariant, L Pi_L=Pi_L L. Define

Y_d,A=L_d(Jbar^(4,−2)_A),  A an increasing five-subset of (*,0,1,2,3,4).

Then δY_d=0, and Y_d represents the same scalar class. Carrier24 bounds apply to Jbar, hence to each Y_d. Repeated carrier tuples vanish by alternation AFTER Pi_L. Individual physical repeated-carrier terms need not vanish.

## 3. Exact determinant regrouping

Fix a standard staircase e^σ_0,...,e^σ_4 for σ in S4, with its existing orientation sign sign(σ). Let ρ_e,b be an admitted carrier partition on that standard chart, with sum_bρ_e,b=1; inadmissible carrier choices are assigned zero. Use cutoff24 and the actual chart-local carrier polynomials to clear this new representative. Every rational section is restricted and transported to the SAME finite output frame before forming the sum.

For each increasing A=(a0<...<a4), set

D_σ,A=det[ρ_(e^σ_s),a_t]_(s,t=0..4).

The exact identity is

sum_(b0,...,b4) (product_sρ_(e^σ_s),b_s) Y_d,(b0,...,b4)
 = sum_(A increasing, |A|=5) D_σ,A Y_d,A.

Repeated tuples are zero; each distinct tuple has exactly one A and one permutation π. Its alternating sign is sign(π), precisely the corresponding determinant term. There is no factor5! and no extra sorting sign after the determinant. Original HPL signs are already inside Y. The six subsets are01234,*1234,*0234,*0134,*0124,*0123, using the stated carrier order.

The scalar partition map Pi_R commutes with δ because each deleted vertex weight sums to1. Its regular weighted prism compares it with restriction on a common refinement. This statement applies to the completed Y; it does not require a pole bound24 on a historical order-change primitive. The old/fresh equality is first an equality of classes, and Pi_R realizes the same canonical cover comparison for the new bounded representative.

## 4. Unchanged scalar target

Write t=(-1,-1,-3,-3), the current target coordinate. It lies in the harmonic range {-3,-2,-1}^4 for F. The requested current detector value is exactly

D_d=[x^t] sum_(σ in S4) sign(σ) sum_(A increasing,|A|=5) D_σ,A Y_d,A.

Here the bracket means the existing tensor-Cech Laurent harmonic coordinate after the fixed original-frame conversion, not a newly chosen inverse-series convention. In the standard signed staircase comparison its top component is exactly the displayed alternating sum. Coboundaries have zero harmonic coordinate, so replacing J, its cover or its regular partition leaves D_d unchanged. The full-sign y factor is stripped exactly once; the uniform τ^-4 conversion is retained. Since the staircase starts in the all-finite chart, expressing the final rational terms in that frame introduces no additional arbitrary scalar factor.

For each detector this requests at most six cochain sections, with24 determinant weights. The same sections can be shared across staircases. The previously established literal j zero on prefix*02 may reduce its request count to five if the authenticated same-row identity is retained; this optimization is not needed for the six-request theorem.

## 5. Exact remaining executable dependency

A source provider must produce the six Y_d,A as exact rational sections of the COMPLETED trace-free old lift after legal-mask averaging, with their carrier24 denominator ownership and original output frame. It must not substitute raw C2 values, unaveraged masked entries or a recomputed nonlinear residual on permuted vertices. Then an exact finite Laurent/coefficient action for the determinant-weighted sum must be supplied with multiplication, partition acquisition, width and liveness costs. The result claims no obstruction value, first-order completeness, higher-order extension or algebraicity.

## Verification and sources

check.py independently checks20 generic5x6 determinant regroupings and32 weighted Cech chain identities, using tiny synthetic integer matrices only. No source values or target coefficients are evaluated. receipt.json records52 passing controls.

Pinned sources at commit08b73637d4136f91606aad332c46cafd064417f8:
- research/hm/current-scalar-geometric-dependencies/frames-and-poles.md §§2,4 (global degree transition and line cancellation).
- research/hm/current-scalar-proof/map-and-comparison.md §§1,3 (global row-map mechanism, total-lift comparison and harmonic range; its particular two-entry row is not substituted for the current four rows).
- research/hm/current-scalar-geometric-dependencies/data/model.json (homogeneous gamma/ev rows authenticated in the independent source-row note).
- PR1 comment6141322825 §§2.2,7 (signed staircase and regular weighted comparison).
- historical imported premise hm-old-tracefree-carrier24-20261015/THEOREM.md (see PUBLICATION-SCOPE.md) and INDEPENDENT-POLE-AUDIT.md (old trace-free replacement, legal1 projection and carrier24).

Source URLs:
https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/frames-and-poles.md
https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-proof/map-and-comparison.md
https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6141322825

Independent source review confirmed the equivariance inference after freshly fetching frames-and-poles.md (blob46470b5a7198be2f8c39f9cb5f5a904ae355ec97): common τ^-4 acts on both degree−2 blocks, so each constant row is a global map. The retained names are labels for the explicit displayed rows; no historical naming or completeness statement is needed for this theorem.
