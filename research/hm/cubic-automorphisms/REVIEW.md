# Independent review: full polarized automorphism group

Verdict: PASS, conditional on the explicitly pinned geometric inputs. This is independent mathematical review, not formal proof-assistant verification.

Reviewed artifact: PROOF.md, SHA256 8ede7396e3e1bdc8d35b320a35dc5883545e120bee044fe2fb92a058d9d58d80.

## Checks

1. **Recovering the blowdown.** On the blowup of thirty reduced points in P4, the canonical formula and cubic polarization give K_M+3D=4H. The Picard group argument establishes torsion-freeness, so preserving 4H forces preservation of H. Normalization functoriality and the complete system |H| then recover the original blowdown and its thirty exceptional divisors. The converse action of a configuration stabilizer on the full cubic system is valid. These give inverse group identifications, rather than only an injection.

2. **Complete projective embedding.** The pinned equality H0(V,O_V(1))=S is needed and is used explicitly. Integrality and nondegeneracy make the projective restriction faithful: an irreducible variety of pointwise eigenvectors lies in one eigenspace, which cannot be proper if it spans P9. Thus the polarized group and ambient projective stabilizer agree.

3. **Intrinsic pentads.** The pairing formula sends a mark based at i to a mark based at k=2i-j. Solving j=2i-k shows that every distinct pair in a pentad gives one edge, with partner mark (k,2k-i). The sixty double values therefore give precisely six disjoint K5 components. Automorphisms preserve normalization, conductor, and the already recovered exceptional divisors, hence preserve this partition. No unproved combinatorial recognition of the thirty-point configuration is being assumed.

4. **Two-basis rigidity.** Independently deriving the monomial/Fourier comparison gives equation (3), and division by j=0 and then i=0 cancels all arbitrary nonzero scalars. The resulting equation (4) forces the two index permutations to be affine with reciprocal slopes. The diagonal factors are then the character factors displayed in (5). Every resulting transformation normalizes the projective Heisenberg group. Conversely all 4*5*5 parameter choices preserve the two pentads, giving the stated ordered-pair stabilizer order100. These are universal character identities, not evaluations at a selected source instance.

5. **Full group, not merely the normalizer.** SL2(F5) is transitive on ordered pairs of distinct directions: choosing determinant-one bases on the source and target pairs proves this directly. Composing an arbitrary configuration automorphism with a known normalizer element therefore reduces it to the two-basis lemma. This closes the possible extra-symmetry gap and proves the full group has order3000. As a separate check, the six-pentad action has at most30 ordered-pair images and each ordered-pair stabilizer has at most100 elements, giving an upper bound3000 matching the known normalizer subgroup.

6. **Open Hilbert orbit.** The local proof underlying PR622 establishes a smooth99-dimensional open orbit. The classified finite projective stabilizer is reduced over C, also following from its zero Lie algebra. The homogeneous orbit is therefore PGL10/Gamma, and the free finite constant-group quotient is a finite étale torsor of degree3000. This argument does not apply to any boundary of the orbit, and the text correctly makes no such claim.

## Scope and reproducibility

The result concerns the polarized canonical cubic image and its configuration stabilizer. No classification of unpolarized automorphisms, no global splitting of the normalizer extension, and no solution of the original full-adjoint or algebraicity goal is inferred. The exact sequence and normalizer order are inherited from the pinned PR617 input; the new part excludes projective configuration symmetries outside that normalizer. No selected HM/source coefficient, point, derivative, matrix, or rank evaluation and no large computation was performed in this review.
