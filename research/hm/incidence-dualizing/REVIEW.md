# Independent review: incidence dualizing bridge

Verdict: PASS for the structural theorem, conditional only on the explicitly pinned geometric inputs of PR575 (99529ca66e1c394e2b3fbe2f8786c71433755956) and the normalization-defect statements of PR574 (3c92fdc469f6870520e7a9d905b5ab9199a5bf37).

Reviewed proof SHA-256: 96d2a4db4e32ba7267ccde6f4f789b93a95fde8b4b0993bce6b89b52aad1cf70.

This is independent mathematical review, not formal verification. No selected actual HM/source-instance evaluation or large computation was performed.

## Checks

1. The dualized gluing triangle has the correct order and shifts. With the absolute normalization K_X=omega_X[2], K_E=omega_E[1], and K_J=omega_J, it yields H^-2(K_Z)=j_X*omega_X and the displayed extension in degree -1, with no additional cohomology.

2. The local free resolution of R/(ta,tb) is exact. Its dual has Ext^1=R/(t) and Ext^2=R/(a,b). The comparison map to the Koszul resolution of R/(a,b), with components identity, t times identity, and t, satisfies both chain-map identities. Consequently the induced Ext^2 map is multiplication by t, as claimed.

3. This local calculation establishes more than the length of the quotient: the degree-minus-one sheaf is annihilated by the ideal of E and is a line bundle on E. Faithful flatness of completion justifies both assertions. Its injection from omega_E vanishes to order exactly one at every endpoint and nowhere else. The injection therefore intrinsically identifies the line bundle with omega_E(J). The resulting quotient is the simple-pole residue quotient, subject to the explicitly stated sign convention. On each bridge the two residues sum to zero and H^0 has dimension one, while H^1 vanishes.

4. The direct-image cohomology claims follow from finiteness on X and the preceding bridge cohomology. They alone would not identify the complexes; the proof correctly uses proper duality and the actual unit O_S to Rp_*O_Z to prove that the actual trace is an isomorphism. The residue pairing r(c_+-c_-) is well defined on the quotient by diagonal constants, invariant under simultaneous relabeling, and agrees with dualizing the endpoint restriction map. Thus it identifies the defect-dual lines, without choosing scalar trivializations.

5. At an attachment the truncation class lies in Ext^2_R(R/(a,b),R/(t))=C, computed by the Koszul complex over the ambient regular ring R. The proof correctly states this as ambient Ext. Ambient duality sends the proposed summands M[2], N[1] to M, N in degree zero. Their direct sum needs two generators, whereas A is cyclic. This proves that the class is nonzero and excludes a global splitting by completed-local restriction.

6. The surface consequence has the correct shift: dualizing T^D[1] gives T[-1], with nonzero cohomology in degree +1. Dualizing the other proposed summand gives B=nu_*O_X in degree zero. This contradicts O_S being concentrated in degree zero and rigorously excludes splitting of K_S as well.

## Scope

The conclusions concern the absolute dualizing complexes of the primary incidence and primary surface and their proper trace. They neither assert Cohen--Macaulayness or purity of the incidence nor a smooth or rational-singularity resolution. They do not establish selected-source evaluation, higher-order lifting, or algebraicity. No mathematical correction or unresolved dependency beyond the two stated inputs was found.
