# Independent comparison audit

Reviewed PROOF.md against the independently established universal spectral construction in ../boundary-relative-rigidity/SIMPLE_SPECTRUM_AUDIT.md.

## Verdict

The mathematical constructions agree exactly. The single surviving branch is Spec(A/I), with I the coordinate ideal of beta(s_1,s_2) and beta(s_1,s_3). The Newton residual ideal equals this ideal, rather than merely its radical, tangent ideal, or an ideal with the same closed points. The tangent map to coker(J_vert) has precisely the claimed kernel. The displayed residual-vector criterion detects full Artin lifting and correctly distinguishes it from first-order vanishing.

## Checks

1. The vertical Jacobian is injective because the relative tangent space vanishes. Selecting a nonzero 2x2 minor is valid. Every Newton inverse exists over A; quadratic improvement and nilpotence make termination exact. Difference factorization proves uniqueness over local Artin test algebras. Testing the quotient A/I and the quotient A/I_res in both directions proves equality of the ideals without relying on restricted functors alone.
2. The branch-dependent simple-spectrum proof is correct. In dimension two the traceless selfadjoint discriminant is a nondegenerate binary quadratic, and the determinant on all selfadjoint matrices is a nondegenerate ternary quadratic. Their maximal totally isotropic linear spaces have dimensions one and one, respectively. Both resulting degeneracies produce an isotropic common eigenvector, contradicting beta's diagonal nonvanishing. The separate universal conic proof also covers the zero-branch case.
3. Simple residue roots lift over A and their unit differences give spectral projectors. The eigenline equations force all off-axis coordinates to vanish exactly over arbitrary test rings. The candidate ideals are J_12+J_13, J_12+J_23, and J_13+J_23. In the one-branch case the first two cross ideals lie in m and J_23=A, as claimed.
4. The pair of scalar forms is split-surjective onto A^2 because its reduction has rank two. Therefore K' is free and both residual vectors lie in mK'. Their coordinate generator bound and tangent kernels are valid. No independence of the generators is inferred.
5. In a spectral chart the two separating-operator equations have unit linear coefficients, so the selected Newton solution is x*=0. The other residuals are the cross coordinates divided by the unit diagonal q-norms. This explicitly verifies compatibility.
6. For a prescribed square-zero polar lift alpha':A -> R', kernel M, the intrinsic obstruction is [g] -> alpha'(g) from I/I^2 to M. It factors through I/m_A I for a small extension. The residual-vector tests are generator presentations of this map. Their simultaneous vanishing is intrinsic; their individual coordinates need not be independent or invariant under changing presentation.

## Minor wording corrections requested

Replace the two occurrences that use m² to mean an ordered pair by m×m, reserving m² for the ideal square throughout. Qualify the claim that residual evaluations are independent of choices: they are functorial and independent of auxiliary line-lift choices for a fixed presentation, while their tuples change with equation generators. The ideal and the vanishing criterion are invariant. Neither correction affects the proofs.

No numerical residual values, physical realizations, source mutations, or external computations are claimed.

## Status of this record

This is a historical mathematical audit, not a new formal verification or a new execution of tests.
