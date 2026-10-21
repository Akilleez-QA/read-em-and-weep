# Independent review: cubic separation and degree-nine defect bound

## Verdict and reviewed artifact

**PASS: mathematical proof reviewed, not formally checked.**

Reviewed `PROOF.md`, SHA-256 `91479569cd7a5be705db41e4d74023dbd8cfb6f001e777568ab91f53c17a94bc`.
The review accepts the immutable established inputs cited there and independently checks the new deductions, including the geometric and representation-theoretic interfaces. No selected Horrocks–Mumford coefficients, matrices, ranks, or source-instance computations were evaluated.

## 1. Reider application

The null-locus argument is sound. For an irreducible curve other than a distinguished section, both I-intersection and fiber-intersection are nonnegative. Vanishing of their sum forces verticality; smooth fibers and each component of the twelve singular fibers have positive I-intersection. Thus the null curves are exactly the 25 distinguished sections. Their pairwise disjointness follows from the stated intersection identity and positivity of intersections of distinct curves on the smooth surface.

For L=3(I+F), the calculations L²=45 and K_X+L=3H are correct. Reider applies to nef line bundles, not only ample ones. The basepoint alternatives are (L·D,D²)=(0,-1),(1,0); separation alternatives are (0,-1),(0,-2),(1,0),(1,-1),(2,0). The latter includes infinitely near points. Divisibility excludes the positive L-intersections, and every effective zero-intersection divisor is a nonnegative integral sum of disjoint (-5)-sections. Its square is a negative multiple of five, excluding every remaining case. Both global generation and all length-two separation follow, hence very ampleness of the complete |3H|.

The exact statement was checked in Robert Lazarsfeld, *Lectures on Linear Series*, Theorem 2.1, printed p.7 (PDF page7), with its proof in §§3–4:
https://www.math.stonybrook.edu/~roblaz/Reprints/Lazarsfeld.LLS.pdf
This is an author-hosted mathematical exposition with proofs, not the original Reider article. Original publication metadata is verified at:
https://annals.math.princeton.edu/1988/127-2/p04
Igor Reider, *Vector bundles of rank 2 and linear systems on algebraic surfaces*, Annals of Mathematics 127 (1988), 309–316. The original article's full text was not separately inspected. No square-nine boundary exception is relevant at square45.

## 2. Actual quotient and strict growth

Very ampleness separates the two distinct normalization points over each node by a section with one zero value and one nonzero value. Thus its branch difference is nonzero, regardless of trivialization. This establishes nonzero projection of the cubic image onto every one-dimensional quotient stalk; it does not assert that the full difference map is already surjective.

A linear form avoiding all nodes trivializes all twists of the quotient. At each node, multiplication by an ambient function on this quotient is multiplication by its common residue on both branches. Consequently the stated diagonal operators really are the action on T, not an unrelated interpolation model. Equality of consecutive images makes the common image stable under every generator and hence all products and linear combinations. Distinct affine support points imply that these functions generate all coordinate idempotents, exactly as proved in the manuscript. Stability and nonzero projection onto every coordinate therefore force the full direct sum. This argument does not require the chosen trivialization or the intermediate spaces to preserve a chosen Heisenberg matrix realization.

## 3. Heisenberg central character

The direct geometric source is BHM, printed pp.60–61: the translation action lifts trivially on O(F), lifts on O(I) with primitive scalar commutator, and extends by tensor products to O(pI+qF). Printed p.63 identifies H⁰(I+2F) with V* equivariantly. Thus H has a primitive central character and the center acts trivially on the underlying surface. The normalization sequence is equivariant, so its nth twist and the image of its difference map have that character to the nth power. A possible inverse character or primitive change of generator does not change the condition 5∤n.

Source:
https://mathweb.tifr.res.in/Documents/Publications/Studies/Vector-Bundles-On-Algebraic-Varieties.pdf

For completeness, the dimension-divisibility claim can be checked without an irreducible classification. If generators A,B satisfy AB=ζ^n BA with ζ^n primitive, B carries each A-eigenspace isomorphically to the next of five distinct eigenvalues. Every eigenvalue orbit contributes five times a common eigenspace dimension. Hence the image dimension is divisible by five. Finite-order operators are diagonalizable over C. No divisibility is claimed at degree5.

## 4. Vanishing and regularity

The rank bounds 5,10,11,15,20,25,30 in degrees3–9 follow correctly from strict growth until full rank and divisibility in all those degrees except5. If full rank is reached sooner, it persists by multiplication with the avoiding linear form. The normalization long exact sequence and the stated H¹(X,nH)=0 then give H¹(S,O_S(n))=0 for n≥9.

The higher-cohomology and regularity consequence is also correct: H²(O_S(8))=H²(O_X(8H))=0, and support dimension two removes the remaining regularity conditions. Therefore O_S is 10-regular, yielding complete-section multiplication surjectivity from degree10 onward. This is not projective normality or ideal-sheaf regularity. The manuscript preserves this distinction, as well as the unresolved exact ranks in low degrees.

## Final revision reconciliation

The final manuscript was read in full after the author added direct BHM page references, corrected the Reider page citation, and changed its status to independently reviewed. These changes are editorial and match the reviewed mathematics. All requested citation improvements are resolved. The hash above pins this final manuscript; it is ready for publication with this review.
