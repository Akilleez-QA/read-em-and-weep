# Independent mathematical review

Result: PASS for the proof in PROOF.md with SHA256
3fec4b2ce8f91a59c4ba09fbfd0514fffbcafe4c072e7d4a4e2e4b3dabc93652.

The new universal annihilator-support lemma is correct. This review independently checked the following points.

1. With the natural dual pairing between V tensor W and V* tensor W*, the actions of E12, E21 and diag(1,-1) give exactly c(B)=0, d(A)=0 and c(a)=d(b). These three equations are necessary and sufficient, since those operators span sl(W).
2. Every vector in A intersect B is annihilated by both projections of K. Full V*-support means that their sum spans all of V*, so this intersection is zero. No assertion that either projection alone is surjective is needed.
3. When A intersect B=0, the two restriction maps B-perp to A* and A-perp to B* are separately surjective. After the harmless minus sign on the second component, their direct sum surjects onto (A direct_sum B)*, which restricts surjectively to L*. The kernel is precisely K. Thus dim K=2n-dim A-dim B-l, and dim A+dim B>=l gives the asserted bound.
4. At the generic point, dim(x wedge A0)=4. The pinned actual exterior formula identifies the annihilator in the lemma with the generic kernel of beta. Replacing the naturally dual factor W* by W through the invariant alternating form is an invertible change on that factor and leaves V*-support unchanged.
5. For n=5 and l=4, full support gives dim K<=2. This contradicts the dimension three required by rank seven. Together with the credited prior rank alternatives, generic rank ten follows.

The five exact dependency documents cited in PROOF.md were fetched at their pinned commits and checked for the assertions used: the exterior formula at 7bf725bcd857a2deb975f9ecb80fca32e7833ae0; remaining rank alternatives at d6ddff0f1a663df9b102a9fd8d8f915f2d9142d6; full support at 622aebd082db42057cd5b8502e941229ff499e58; the two-channel criterion at 3fec79146becd5ffee965614dcc50e13de9eb532; and evaluation degeneracy at cef412c142ad8d154cdb18a9967ab6459217cd11. This review verifies the new inference from those mathematical inputs; it does not constitute a fresh audit of every earlier representation-theoretic dependency.

The consequences stated in Section 3 follow with the specified boundaries. Generic injectivity of beta implies injectivity of its third exterior contraction, hence independence of the two determinant-channel images. The previous Chern obstruction supplies nonempty degeneracy, while generic rank ten makes that locus proper. The maximal-minor bound gives codimension at most three; degree 105 remains conditional on expected codimension three.

This is independent mathematical review, not formal proof-assistant verification. No selected HM/source-instance value, coefficient, numerical matrix rank, minor, or large computation was evaluated. The argument is valid over the function field and does not select a point. It proves neither full adjoint quadratic invertibility nor residual surjectivity, the lift-boundary isomorphism, the original selected-pair membership, Q4 vanishing, higher lifting, or algebraicity.
