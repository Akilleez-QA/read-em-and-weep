# Independent mathematical review

Verdict: PASS for polynomial parameter descent and the 23/7/16 dimensions, relative to the explicitly pinned actual geometric dependencies. No unresolved mathematical gap was found in the stated argument. This does not evaluate the actual scalar or fourth Bockstein and does not prove the vertex square-ideal condition.

## Checks

1. The global cochain spaces and actual section spaces used in the two lifting steps are fixed finite-dimensional representations. The first map is linear on the space of pairs (C,V) with V closed; its right side a h Z_a has bidegree (2,1). A linear section of its image yields a polynomial completion without choosing parameter-dependent inverses. Averaging that section is legitimate because Gamma is finite in characteristic zero. The input family is equivariant, so the resulting completion family is equivariant.

2. Compatibility of the second lift is not inferred from separate pointwise primitives. PR685 explicitly extends a J3 after every allowed completion change. Therefore the particular polynomial a J3 constructed in the first step lies in the image of the fixed restriction map from fourth- to third-neighborhood actual section spaces. The dense-open image condition extends to the entire affine parameter space by projection to the fixed cokernel. A second linear section gives J4 of bidegree (3,1). No cochain-to-bundle or simultaneous-primitive compatibility is missing.

3. Multiplication gives J4 squared bidegree (6,2). The square-zero restriction to 3Q and the rank-two scalar identity put this square in the fixed last-layer scalar subspace. Extraction of S4 is linear there. PR687 removes both completion and fourth-lift choices with the marking, U_a and source correction fixed. It does not remove arbitrary changes of those fixed inputs.

4. The parameter-space bundle twists are correct. Universal multiplication by a cubed times h has parameter degree (3,1), so it maps H6 tensor O(3,1) into H14 tensor O(6,2). Every projective source is nonzero on the integral Q. Multiplication is therefore injective on every fiber, yielding a subbundle and a locally free cokernel. Fiberwise containment of S4 implies that its cokernel section is zero on the reduced parameter variety. It then has a unique regular global preimage. This is a valid proof of polynomial division and has no parameter-pole gap.

5. Global sections of O(3,1) identify the descended family with a tensor in H6 tensor Sym^3(A*) tensor D*. Uniqueness supplies equivariance, and PR692 removes the projection outside the fixed 27-dimensional block T. Polynomial density extends this target statement and the polynomial definition to zero-source parameters. No division at zero parameters or Hartogs extension of the nonreflexive ideal I squared is being used.

6. The character decompositions distinguish the two three-dimensional representations A and V. The target is A+2V+2P+2D, of dimension 27; the parameter representation is 3A+3V+3P+4D, of dimension 50. Their equivariant Hom dimension is 3+6+6+8=23. The proof uses coordinate duals correctly and only invokes self-duality for the abstract representation count.

7. The square-direction restriction is the restriction of cubic polynomial functions on A to its Veronese conic. Its kernel is the principal discriminant ideal in degree three, namely Delta A*. The quotient is Sym^6(W*). Tensoring and taking finite-group invariants preserves exactness, so the equivariant restriction is surjective and its kernel consists exactly of discriminant multiples of bilinear families. A tensor D=A+V+P+D gives kernel dimension 1+2+2+2=7; the quotient consequently has dimension 16. These describe possible families, not realized degrees of freedom in the fixed actual scalar.

8. The linearity and normalization inputs were checked against the pinned published sources. The canonical multiplied-lift theorem explicitly supplies the equivariant linear U_a family and its fixed differential; injectivity of multiplication by q squared gives linear Z_a. Sections 2 and 3 of FOURTH-BOCKSTEIN-AFTER-ACTUAL-THIRD-VANISHING identify the polynomial correction L(a)h and its compatible fixed-probe b, supporting bilinearity. The actual ladder confirms the finite global cochain construction. The cited PR685, PR687, PR691 and PR692 proofs were read locally and used with their stated scopes.

## Verification and limitations

The final bounded verifier was independently executed and passed. It uses exact abstract binary-icosahedral characters to check the target, parameter, discriminant-kernel and visible-quotient representations, including Sym^4(U)=D and Sym^8(U)=P+D. It does not formally verify the geometric descent or reprove the actual geometric dependencies.

The actual element of the 23-dimensional possible family space remains unknown. Vanishing on all square directions would leave the seven-dimensional possible discriminant-multiple subspace, not prove global vanishing. Nothing here establishes the vertex I squared containment, scalar vanishing, a fourth Bockstein value, or algebraicity. No selected actual HM/source coefficients, points, derivatives, matrices or ranks were evaluated, and no external repository changes were made during this review.

Reviewed PROOF.md SHA-256: `1ddb69addc060c13e017cf0e941e979d63f8bbaec8de178f7de0bd277e00af7d`.
Reviewed verify.py SHA-256: `82cad82e57abbec3e47ce71e0188e46db3f5c48de02ee4a24e26916913621661`.
