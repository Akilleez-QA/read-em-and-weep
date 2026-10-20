# Independent review

Proof SHA256: `f305f6b8daa1806dffd77a8c3bde9d9cb33d11b37d019a702121d24b5ef2bbb7`.

Verdict: PASS under the exact PR274 and PR300 family hypotheses, over local Artin complex algebras with trivial H action. This is a mathematical review, not a machine-formal check.

The nontrivial cotangent weights exclude constant terms even when those terms are nilpotent: the relevant nonzero complex character differences remain units over the coefficient algebra. Applying the same argument to the inverse proves preservation of the full augmentation ideal. Distinct weights and the transitive cyclic action make both cotangent and top commutants scalar over the coefficient algebra; no field-only use of Schur's lemma is required.

The completion step is justified by Noetherian flat completion and a finite projective resolution. The degree-one base-change assertion uses specifically the B-flat total Ext2 premise, not blanket cohomology base change. The finite-support defect is already complete. The inverse-semilinear direction on Ext is checked by composing a dual functional with F and then with phi inverse. Since the automorphism centralizes H, this introduces no character or local-duality orientation twist.

Initial multiplication is functorial under these semilinear maps. The cotangent and top maps multiply its source by a single unit. Higher-order coordinate terms disappear there. The ten-column presentation then gives exactly the initial linear relation span, with the isolated two-coordinate block A(1,-a). Equality with A(1,-b) forces a=b by first-coordinate comparison, valid with zero divisors.

The added nonlinear example is valid: the fifth power of the four-variable product is invariant under the normal abelian subgroup, cyclic permutation, and specified central character. Its substitution has identity linear part and an inverse obtained degree by degree over any stated Artin base. The allowed coordinate group therefore genuinely exceeds fixed-ring generator changes.

The conclusion excludes even unmarked semilinear equivalences inside this centralizer category. It does not classify normalizer-permuting coordinate maps, coefficient-algebra automorphisms, character twists, arbitrary coordinate changes, or other deformation directions. No actual HM/source instance, obstruction value, or large computation was evaluated.
