# Independent bounded review

PASS for the stated universal polynomial route exclusion, conditional on the supplied fixed-frame definitions of M2 and normalized physical jets. This is not an actual source calculation, residue or global obstruction.

## Full physical derivative, and what is projected

For commuting V_a, L_b=A^-1 V_b A satisfies V_a L_b=H_ab-[L_a,L_b]/2 by inverse differentiation and traceless rank-two polarization. If Y_b=B^-1 V_b B, then differentiation of literal A^-1 Y_b A contributes [U_b,L_a]. Thus V_a U_b=J_ab-[L_a,U_b]-[U_a,U_b]/2. The moving A transport is not omitted. Applying these full identities to a cubic current polynomial yields a term with one symmetric jet and two currents, plus terms with four currents. A current-only R4 cannot change the first part. The coordinate checker tests this necessary jet-linear identity only; it does not test the quartic transport coefficients. The preceding derivation is the separate justification that the projection is the actual physical derivative's projection.

The symmetry H_ab=H_ba and J_ab=J_ba is imposed exactly. At the formal second-jet level there are no additional traceless symmetric-jet constraints from determinant one: the trace of the second normalized derivative is fixed by the first jets, while its traceless symmetric component remains free. No derivative of H or J occurs in the tested flux class. Higher compatibility identities therefore do not add row relations here. None of this claims the user's particular source attains arbitrary formal jets.

## Ansatz completeness (precise scope)

The domain is constant-rational linear combinations of simultaneous-conjugation-equivariant, polynomial cubic vector expressions, with each of the three axes other than the differentiation axis occurring once, and arbitrary L/U choices. For each of the eight color choices, the three invariant maps d(X,Y)Z, d(X,Z)Y, d(Y,Z)X span. Equivalently, invariant rank-four tensors on the three-dimensional adjoint representation are the three metric pairings; the invariant alternating rank-three tensor produces no further rank-four tensor. Nested brackets reduce by the displayed rank-two identity. Thus there are exactly 4*8*3 columns in this domain. This claim adds no jet-dependent, denominator-dependent, source-specific or dual-kernel-dependent fluxes, and makes no statement about other differential orders or combined target families.

## Independent quotient and coefficient audit

The independent audit_check.py was written without importing the author's solver or polynomial helpers. It uses only Python standard-library exact rational arithmetic. Each formal traceless vector has independent scalar coordinates (z,x,y), with d(X,Y)=2z_X z_Y+x_X y_Y+y_X x_Y. It expands all 144 invariant row vectors into scalar monomials and independently proves that their embedding has rank 144. Consequently the eight-row coefficient functional is well-defined after all algebraic rank-two vector identities; it is not merely a left null vector in an overcomplete presentation.

The checker independently constructs all cubic fluxes as scalar-coordinate vectors, applies the formal jet-linear physical derivative coordinate by coordinate, and decodes into the independent row space. It constructs the entire N=8M2 directly from the literal supplied formula using T=L+U, retaining every sign and both H and J families. The rebuilt image rank is 94; adjoining the target gives rank 95. The supplied eight-row certificate annihilates every one of the 96 columns and pairs with N to 1, hence M2 to 1/8. The explicit eight-column cancellation table in RESULT.md was also compared with the certificate. The result does not rely on Gaussian elimination's reported rank: the hand certificate suffices after row independence is established.

Normal, optimized, and different-working-directory runs all pass with identical reports. Explicit exceptions retain checks under python -O. Flipping one certificate sign and omitting the target are rejected as negative controls. These controls do not purport to independently check full transport, global source premises or the entire earlier midpoint theorem.

## Boundaries

This excludes M2=sum V_a F_a+R4 in exactly the tested class. The same jet-symbol obstruction applies if these flux derivatives include an auxiliary current-linear connection commutator, since that changes only the quartic part. This does not prove any specialized M2 or full residue is nonzero. It does not establish a pole/owner domain, global exactness, obstruction class, closure, or the absence of a broader flux. Nonconstant full dual kernels retain their adjoint derivative. Existing Q4, C4, Phi, and all other complete-target families are unchanged.

No actual source/model/owner/current/jet values were substituted, no matrix objects or physical matrix-polynomial products were formed, no production code imported, and no network or external publication was performed. Scalar-coordinate expansion is formal coefficient algebra, not a physical evaluation.
