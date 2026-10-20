# Independent audit of the global nilpotent incidence

Status: PASS for final Sections 1–8. The global image twist is corrected, the generic-kernel exclusion has been checked in its final written form, and no corrections remain. This audit is frozen.

## Global incidence isomorphism

The universal tensor line R in sl(S)⊗det S gives A:S→S⊗M with M=R*⊗det S. On the reduced nilpotent incidence all geometric fibers are regular nilpotent, by rank-one exclusion. Constant ranks on a reduced finite-type base give actual kernel subbundles; the rank-one and rank-two kernels define the inverse flag morphism. Globally the image description is ker A²=(im A)⊗M⁻¹, rather than an untwisted equality with im A.

The forward construction is algebraic. The recovered q has the stated transition, and substitution gives k'=ab²k, so its nonzero tensor line glues. The universal nilpotent normal form gives its kernel and kernel-square flags. The two maps are inverse on closed points and therefore as morphisms on the reduced schemes: the ideal of the diagonal pulls back to functions vanishing on every closed point. No inference from a mere proper bijection is made, and no unreduced scheme isomorphism is asserted.

## Dimension estimates

The proper incidence has dimension at most three. Upper semicontinuity of proper fiber dimension makes each H_d closed. Restriction to an integral component and the generic-fiber dimension formula give dim H_d≤3−d. This applies to constructible strata without a kernel-bundle assertion across rank jumps.

Every kernel of dimension three has a nilpotent point by projective intersection in P². A four-dimensional kernel has its nonempty nilpotent curve, as imported; a determinant-zero three-net has a conic. Thus dim G3≤3, dim G4≤2, and the singular-net-containing locus has dimension at most two. All stated special pencil and net bounds follow from the same fiber estimate.

The frame dimension bookkeeping is correct: add three for the torus bundle, with the finite orientation cover not changing dimension. Contributions from G3 and G4 are at most seven; pencils contribute at most eight, dropping to seven in the determinant-identically-zero branch and at most six in the nonzero-determinant branch with a nilpotent point. Therefore a nine-dimensional independent component can only have a dense line-kernel base. The stated generic criterion, prior to its exclusion, is equivalent to this condition. Closing a nine-dimensional independent component cannot embed it properly into a larger component meeting that open.

## Independent check of the stronger exclusion

Suppose the generic kernel is a line with determinant zero. The coherent kernel L of E→J is torsion-free and S2 by the depth lemma applied to its torsion-free image; it is therefore reflexive. On the smooth Grassmannian, a reflexive rank-one sheaf is invertible. Its quotient is the torsion-free image, so its inclusion into E is primitive at codimension-one points. Untwisting gives a line U=L⊗(det S)⁻¹ mapping to sl(S).

The trace-square is a section of U⁻². It cannot vanish generically, since that would give nilpotent kernel lines over a dense open. If it has any zero, its nonzero section defines an effective Cartier divisor. At that divisor's generic point the kernel inclusion is primitive and nonzero, hence supplies a regular nilpotent kernel line. This produces a five-dimensional subset of the nilpotent image, contradicting its dimension bound three. Thus q is nowhere zero, U² is trivial, and Pic(G)=Z forces U trivial.

Finally H0(End S)=C: the flag projection P(S)→P(V) has connected Grassmannian fibers and pushforward of its structure sheaf O, giving H0(S*)=V*. Any endomorphism of S, composed with S→V⊗O, comes from a fixed endomorphism of V preserving every three-plane. It then preserves every line and is scalar. Its trace-free part is zero. This contradicts the nonzero map from U=O and excludes the generic line-kernel determinant-zero possibility. Combined with the earlier strata, independent zeros have dimension at most eight.

No actual operation instance, selected point, source matrix, or physical value was evaluated.

## Final consequences

The final Sections 7–8 pass. The contradiction excludes the sole possible nine-dimensional independent branch, yielding dim Z_ind≤8. A possible eight-dimensional component must have a five-dimensional spectral line-kernel base or arise from the nilpotent-free pencil branch with nonzero determinant over a five-dimensional base. Neither existence nor exclusion of these remaining branches is established. The full-Grassmannian line-bundle argument is correctly not extended to a line kernel defined only on a divisor.
