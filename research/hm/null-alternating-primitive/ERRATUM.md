# Erratum: common-ambient cohomology normalization

The earlier independent review, section 5 equation (4), and the corresponding author-proof section 4 incorrectly identified the actual induced split-connection difference as

    A^E_ij = −L_ij^t + (dlog nu_j − dlog nu_i)I.

That comparison omitted the ambient line-frame transport. The correct source identity is

    A^E_ij = −dG_ij G_ij^−1 = −L_ij^t.

For a block of weight k, the source split matrix in a common ambient frame is nu_i^k times its prescribed matrix. Every differential raises k by two, so the prescribed differential nu_i^−2 D_ref becomes D_ref after transport. In the middle block k=1, the prescribed cohomology columns (I_0,I_1 nu_i^−2) therefore become I_i diag(nu_i,nu_i^−1), exactly the determinant-normalized physical frame. Their transition is G_ij=g_ij^t.

The untransported column-array comparison equals (nu_i/nu_j)G_ij. It must be multiplied by the ambient middle-frame factor nu_j/nu_i before differentiating it as the actual transition. The prior scalar term was produced by omitting that factor.

The full alternating boundary theorem and its primitive are unchanged:

    Alt(R_raw) = delta P,
    P_ij = −(Z_i+Z_j) ∧ L_ij / 72,
    Z_i = str(B_i^3).

The corrected comparison gives the same required cubic trace, tr((A^E_ij)^3)=tr(L_ij^3). The separate scalar-shift argument for the ambient k theta term remains valid and necessary: the old common-frame coefficient is k(gamma_pres−dlog nu), so its difference is still exactly −k theta and A′=delta B−k theta remains unchanged. The two-dimensional full-sign projection conclusion, global regularity, and limits concerning the other thirty dimensions and finite-cutoff implementation are unchanged.

The corrected PROOF.md and REVIEW.md are new versions. The original frozen files and public commit history are preserved. No source-checker code was changed and no physical source evaluation was performed. The detailed source derivation is in COMMON_FRAME_CORRECTION.md.
