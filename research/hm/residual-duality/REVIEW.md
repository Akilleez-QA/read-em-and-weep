# Independent mathematical review

Result: PASS. This is independent mathematical review, not proof-assistant or formal verification. No selected HM/source coefficients, matrices, ranks, or numerical source instances were evaluated.

## Reviewed dependencies and scope

The review uses the actual normalization and dualizing-complex interface in PR574 at 3c92fdc469f6870520e7a9d905b5ab9199a5bf37, the five-to-one conductor grouping and difference injection in PR577 at 563fc7036faa4965e55bda3bec5b82ae5360fa6c, and the derived module splitting in PR579 at 78746b35576c319dd6100c2ec6d4f628100b2200. The relevant normalization sequences and the actual map descriptions were checked against those proof texts. This is not an independent reconstruction of the entire HM foundation.

## Checks

1. **Duality shifts.** With absolute dualizing complexes normalized by dimension, proper duality uses ω_Γ[1]. A finite-support sheaf F satisfies RHom(F,ω_Γ)=F^D[−1]. Hence dualizing K[−1] against ω_Γ[1] gives K^D[1]. Finite duality gives RHom(h_*O_B(−5),ω_Γ)=h_*O_B(3), with no positive sheaf Ext, so the elliptic summand contributes h_*O_B(3)[2]. These shifts give precisely degrees −2 and −1 as claimed.

2. **The actual thirty-residue extension.** Dualizing the surface normalization sequence gives T^D→ν_*ω_X[2]→K_S→T^D[1]. Its pushed-forward degree −1 sequence is 0→h_*ω_B→E→V^D→0. The projection to h_*ω_B[1] is dual to the actual degree-zero inclusion h_*O_B→h_*Rπ_*O_X. Therefore its extension class is induced by the actual difference map d, not an arbitrary map of the same dimensions. Factoring d through Q identifies the extension with the pullback of the nodal residue sequence. The natural trace and residue maps give the compatible map E→ω_Γ×_{Q^D}V^D; it is an isomorphism on the identical kernel h_*ω_B and quotient V^D, hence is the asserted canonical isomorphism.

3. **Coordinate-free averaging.** The thirty point-support summands of T are intrinsic. At each base node all five components ι_z:Q_q→V_z are isomorphisms by PR577's actual residue-difference formula. Thus (1/5)Σι_z^{-1}pr_z is a well-defined retraction V_q→Q_q without a basis, ordering, or orientation choice. Relabeling points only permutes the sum; changing a residue coordinate changes its component map and inverse compatibly. Dualizing this retraction and using the fiber product selects the stated canonical trace section. Its existence is compatible with the 24-dimensional affine family of other sections.

4. **Local nonsplitting.** At a base node R=C[[s,t]]/(st), the normalization's regular differentials form m_Rη inside ω_R=Rη. The fiber-product module is {(fη,r):f mod m_R=Σr_j}. Its submodule killed by m_R is exactly the four-dimensional sum-zero residue space, since R has zero socle. An R-linear section of the quotient onto C^5 would have image in that four-dimensional submodule, whose image in C^5 is proper. Such a section cannot exist. Completion is faithfully flat, so this excludes splitting of the original algebraic stalk sequence and hence of the global thirty-residue extension.

5. **Compatibility boundaries.** Splitting the trace quotient E→ω_Γ and failing to split the residue quotient E→V^D concern different short exact sequences. Neither conflicts with the module isomorphism E≅ω_Γ⊕K^D. The full derived decomposition is still asserted only as an existence statement. No flatness, multiplicative formality, splitting of K_S on S, full-adjoint boundary invertibility, original-source membership, higher lifting, or algebraicity follows.

The proof therefore supplies a genuine new canonical-map description and a nonsplit natural extension, rather than merely the numerical equality 30−6=24.
