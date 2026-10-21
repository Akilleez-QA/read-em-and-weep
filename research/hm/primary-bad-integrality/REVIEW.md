# Independent review of primary-bad integrality and rationality

Reviewed exact file: PROOF.md, SHA256 b15e359a700cdfb1e4dd8c5106f90d11ae33c2804d8998956f51ec996afab14d.

Verdict: the new argument is mathematically sound conditional on its explicitly pinned dependencies. This is an independent mathematical review, not proof-assistant verification and not a fresh derivation of every inherited HM representation theorem.

## Checks

1. The equivariant map and twists are correct. The Euler inclusion is Omega^1(2) into A* tensor O(1), so its composition with dual evaluation is a 15-by-10 linear matrix with the same fiber rank. The exterior formula at PR543 commit 7bf725bcd857a2deb975f9ecb80fca32e7833ae0 and the Euler/invariant statement at commit 8d24a12c4af9c922db2052a360c96a053dcba5b8 were read directly from their pinned GitHub files.

2. The gcd of nonzero maximal minors spans an N-character because their span is stable. Perfectness makes the character trivial. Central weight restricts its possible degree to 0, 5, or 10; the pinned invariant-quintic exclusion eliminates 5. Degree 10 makes every Plucker coordinate a constant times the same polynomial. The resulting fixed ten-plane lies in U'^* tensor x^perp for every x in the dense rank-ten open. Contraction of any fixed tensor with x is a linear map, and vanishing on this dense set forces the tensor to be zero. This contradiction correctly excludes degree 10 without any target irreducibility assumption. The scalar line-bundle twist does not affect the ten-plane.

3. The rank-nine incidence has dimension at most 2+5=7, and the thirty rank-eight fibers have dimension six. Their union is the inverse image of the closed rank-drop locus. Its proper projection has dimension at most seven. The rank-ten inverse image is a smooth irreducible rank-five-kernel projective bundle, of dimension eight. Purity of B from PR554 rules out any further irreducible component supported by the smaller exceptional image. Nilpotents in either incidence or B are not discarded in making these support-dimension arguments.

4. Equal dimensions give a zero-dimensional generic fiber of the main incidence. Away from the exceptional image the full fiber is the projectivization of the primary kernel and lies entirely in the main bundle. Therefore generic primary kernel dimension is one. This is not an unsupported inference that a generically finite map has degree one: degree one follows separately from the scheme-level unique-kernel-line graph.

5. On an invertible four-minor chart, row and column operations reduce the 10-by-5 matrix to an identity four-block and a six-entry Schur column. Its maximal-minor ideal is exactly those six entries. The incidence forces four kernel coordinates to zero and normalizes the remaining projective coordinate, leaving precisely those six equations. Thus the graph isomorphism holds before B is known reduced. Over the nonempty open avoiding the exceptional image, it identifies B with an open subscheme of the smooth projective bundle.

6. Cohen-Macaulayness supplies the absence of embedded associated primes. Together with irreducible support and generic reducedness this eliminates the nilradical. For the homogeneous ring, saturation excludes torsion supported only at the irrelevant vertex; hence the integral projective scheme gives a prime homogeneous maximal-minor ideal. No unsupported normality or global smoothness conclusion is drawn.

7. The kernel graph gives a birational map from the projective bundle to B. A vector bundle is trivial over a sufficiently small nonempty open of its integral base, so that bundle is birational to P4 times P4. The rational-eightfold conclusion is correct.

## Scope

The review accepts the generic rank-ten input from PR547 and the exact rank strata, purity, Cohen-Macaulayness, saturation, and degree 210 from PR554 as pinned dependencies. No selected actual HM/source-instance polynomial, coefficient, matrix, minor, or numerical rank was evaluated. There was no large computation. These results concern primary multiplication and do not settle full-adjoint invertibility, higher-order lifting, algebraicity, or the original selected instance.
