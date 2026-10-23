# Independent exact-version review

## Verdict and binding

**PASS.** No mathematical defect was found in the complete proof or its bounded verifier, including the abstract-pencil corollary in Section 7.

Reviewed artifacts:

- `PROOF.md`, SHA256 `26af205f8393a6a131341715998db1def399065a12c1c7eee50cf4bc441fe7fd`.
- `verify.py`, SHA256 `8d2311fa31bd7d55b6cecb104a1875177a060af1b63429c082003c65591754a5`.

These hashes were checked before and after the review. This verdict applies to these exact versions. The proof and verifier were not edited.

## Independently checked mathematical points

1. **Clebsch channels and conventions.** Under the invariant self-dual/apolar identifications, the adjoints of the multiplication restrictions are the displayed Clebsch projections of the covariant tensored with the formal homogeneous vector. Each channel is determined up to a nonzero scalar. Contraction gives the stated kernels `O(26)`, `O(24)`, and `Wp O(27)`. Exactness on invariant global sections follows from vanishing of the relevant first cohomology and exactness of invariants. The injective multiplication channels give precisely the asserted injectivity and isomorphism statements. There is no adjoint reversal or rank conclusion based merely on matching multiplicities.

2. **Nonempty balanced locus.** The three block determinants have the asserted bidegrees. Injectivity of the P-to-T map excludes at most one projective direction proportional to the fixed V-to-T vector, in addition to the one kernel direction of P-to-Wp. For every remaining formal P direction, the two D exclusions are proper hyperplanes. This proves a nonempty open subset of the irreducible three-dimensional parameter product without selecting a member.

3. **Splitting and gauge classification.** Surjectivity of multiplication excludes every base point of the coefficient system. Its kernel twisted by one is acyclic, forcing all kernel summands to have degree minus two. The equivariant Euler calculation gives `P+2D`. Conversely this splitting gives the multiplication isomorphism. Constant gauge over the identity of the fixed base preserves exactly the image coefficient subspace, since every automorphism of the quotient line is scalar. Thus the two projective multiplicity parameters are complete invariants of these blocks.

4. **Derivative torsion.** Euler's identity places F in its quadratic first-polar image B. The quotient in equation (11) is the untwisted derivative image, so `deg B=-deg Delta` is correct. The surjection from copies of `O(-1)` implies that B's splitting degrees are at least minus one; the inclusion in the constant bundle makes them at most zero. The resulting defect bound is fifteen. The only positive invariant divisor within that bound is the reduced degree-twelve orbit. The unique V component factors as `f12 v16`, and the invariant-divisor argument proves that `v16` is nowhere zero. At every point of that orbit the V component of the value vanishes but its derivative does not. Equivalently the constant V fiber lies in the kernel fiber and the second fundamental form is nonzero on it. This excludes the only possible defect and proves the everywhere onto derivative.

5. **Maximal profile in Section 7.** At the backward endpoint, the intersection of the kernels of the quotient's value and first derivative has derivative rank one when the second jets are independent. A fifteen-dimensional independent section system has this property generically in characteristic zero. The degree-ten residual line contributes a separate rank-one derivative. At the forward endpoint, the two disjoint residual cases have independent increments in disjoint constant spaces. In the shared-D case, generic injectivity of the P projection of `U_2^8` separates it from `U_3^10`, which has zero P projection. The four-dimensional P system has the required generic second-jet independence. The other projected residual system likewise has independent jets to the required order generically. Consequently both endpoint ranks are exactly two and the intervening rank-three profile is exactly `(1,1)`.

6. **Dual quotient and reconstruction.** The first derivative is onto its saturated image, not merely generically onto an abstract quotient. Dualizing this subbundle factorization therefore gives exactly `A_q^*(-2)` with no torsion defect. The quotient Q is globally generated. A degree-zero summand would give a nonzero constant functional annihilating E, contrary to full constant span; hence all degrees of Q are positive and `Q(-1)` is globally generated. Multiplication by any nonzero formal linear form is injective on the indicated sections. Its cokernel on sections of Q is the corresponding fiber, and the constant ambient space surjects onto that fiber. This proves the second pencil's uniform surjectivity. The commuting relation follows from multiplication of linear forms. The weakened full-faithfulness statement in the pinned PR862 applies with these hypotheses, including possible degree-one summands of Q.

7. **Three normal-form families and scope.** The maximal-slope subbundle F is intrinsic, and its constant span is C. Therefore an equivariant ambient isomorphism cannot change its block parameter. Projection to the quotient by C gives the intrinsic residual class; PR858's three intrinsic pairs distinguish those classes. Conversely equal block parameters and equal residual classes give equivalent direct sums. This establishes three copies of the open family for the stated abstract normal forms. It does not identify a member with the fixed actual HM tensors, verify additional full-module relations, or exclude a frontier label. The proof explicitly preserves these boundaries.

## Computational verification and restriction compliance

The supplied verifier was read in full and run successfully. Its output was:

`PASS: universal degree28 multiplicities, Euler channels, and pencil characters.`

An independent exact character calculation over `Q(sqrt(5))`, using the fixed binary-icosahedral character definitions, separately checked every displayed symmetric-power identity, the required tensor identities, the balanced-kernel character, and all three reconstructed pencil characters. It also passed. This is independent of the verifier's McKay-recursion implementation.

No actual or abstract parameter was selected. No source coefficient, point, derivative value, matrix, selected-instance rank, experiment, scan, or large computation was used. The only executed mathematical calculations were the declared small universal representation identities. Nothing was published as part of this review.
