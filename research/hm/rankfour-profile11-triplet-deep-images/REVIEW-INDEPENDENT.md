# Independent whole-proof review

## Verdict and exact subject

ACCEPT, conditional on the actual geometric hypotheses and the accepted five-kernel theorem explicitly imported by the proof. No mathematical correction to the reviewed proof is required. This is a whole-proof mathematical review, accompanied by independent exact checks; it is not proof-assistant certification of the transitive geometric inputs.

Reviewed file: `PROOF.md`.

Reviewed SHA256: `09424f92b56ce3b907968ccae3c065ececbfbc800fb4db0f79a04a3863f74e26`.

The review includes the clarifying sentence in Section 1 that a rank-two image containing the saturated canonical J must equal J. It does not apply automatically to a later modified proof.

Retained inputs, independently rehashed:

- `inputs/five-kernels.md`: `4d06da768074a6e813ed295a088d862ce328a4cd33b739e88e20ac1f315de36a`.
- `inputs/top-four.md`: `56bb8a0aa5ada0f550e0967ef9e535838e9162c2ff2e5ced039a3f6ddb2aacf0`.
- `inputs/low-top.md`: `c3d21cb63ffac4c69247e8deba8ef352f673ac3a7b2f91507bc54fbecae943af`.

The input manifest records the five-kernel proof at immutable commit `7d71f0e2a3963cff64a069198f4415c5cfd0fe9b`, path `research/hm/rankfour-profile11-triplet-kernels/PROOF.md`. I checked the local manifest's commit identifiers, byte lengths, SHA256 digests and Git blob hashes against the retained files. The task parent separately reports a fresh byte-for-byte comparison with that published immutable input; this review does not claim an additional independent network retrieval.

## 1. Scope and dependency boundary

The proof correctly retains the physical line, determinant convention, actual constant rank-thirty ambient, source E, maximal plateau endpoint bound, and accepted actual five-kernel alternatives. It does not replace the actual derivative with an arbitrary map between bundles with these splittings. It imports the common actual V-row surjection onto J, the two already established full images, and the terminating actual coherent-image filtration. Its new arguments do not assume the original transpose defect is zero.

The target conclusion is correctly limited: all five kernel forms remain necessary possibilities, and none is realized. Only the negative-image branch for K5 is excluded. The surviving K3 negative-image branch receives a forced actual derivative flag, not an existence assertion.

## 2. Rank three and the negative-image dichotomy

The common J inclusion gives rank at least two. Because J is a subbundle of the full target A_q(-2), a rank-two coherent image containing J has a rank-zero quotient injecting into the locally free quotient by J. Such a quotient vanishes, so the image is exactly J. Its kernel would have rank eleven and degree -60. The terminating two-column inequality gives degree at most -61, a contradiction. Consequently the generic derivative rank is exactly three in every branch.

For K3 and K5, ordinary degree leaves only the displayed O(-10) source able to reach the negative coordinate. A nonzero such component is a scalar isomorphism. The same row cannot reach O(4), since the degree-fourteen invariant multiplicity is zero. Modulo J it therefore supplies the entire negative coordinate, not merely a graph involving the positive coordinate. Any additional positive scalar-target image would have generic rank two modulo J and violate the rank-three endpoint bound. This establishes the exact coherent image J+O(-10). For K4 the negative component is excluded directly by degree.

The proof here uses the coherent image, not its saturation; no connection-compatible splitting is being assumed.

## 3. All-height equality and its consequences

For the negative image, the first actual kernel F1 has rank ten and degree -50. The accepted actual derivative construction gives the injections G_j into I(-2j), the nonincreasing ranks, and termination. Thus the column-height bound legitimately applies to the top degrees (1,1,-10).

Writing z=h3 and x=h1, with h2=10-z-x, its right side is identically

    -50 - z - (3/2)z^2 - (1/2)(2x+z-10)^2.

Since z is nonnegative and the actual degree equals -50, equality forces z=0 and x=5. Thus h1=h2=5, q_j=2 for j=1,...,5, and all other q_j vanish. This is an exact all-height argument, not a scan or an assumed optimal height pattern.

Every determinant-degree inequality has a nonnegative deficit. Their sum is zero, so each is equality. For G_j the degree is 2-4j. In wedge-square I(-2j), the upper summand has this degree and the cross terms have degree -9-4j, eleven lower. Consequently the determinant of the projection to W(1-2j) is nonzero, and equal degrees make that projection an everywhere isomorphism. Its graph component into O(-10-2j) has degree difference -11 and vanishes. Therefore the actual coherent image is precisely W(1-2j), without a hidden torsion defect.

The same rank and degree comparison makes every induced map G_j -> G_(j-1)(-2) an everywhere isomorphism. In particular F5=W(-9), F6=0, and successive saturated forward transforms recover F4,F3,F2,F1. Those relations follow from the actual derivative maps; they are not imposed on an ordinary Birkhoff splitting.

## 4. Principal parts and the actual coefficient-system issue

The universal identity is valid with the stated convention. For n>=k, complete polynomial evaluation onto P^k(O(n)) is surjective. At a formal covector ell, its kernel consists precisely of the degree-n forms with order at least k+1 of vanishing. Contracting n-k factors with ell maps onto Sym^k W tensor O(n-k) and has the same kernel: in the universal monomial description, exactly the terms with transverse exponent greater than k vanish. The remaining k+1 terms have nonzero contraction factors in characteristic zero. Both maps are bundle quotients of the same complete system with equal kernels, so the quotient identification is global and equivariant. The fixed determinant pairing gives the stated dual identity.

This universal formal-coordinate argument does not select or evaluate an actual geometric instance, point, jet, parameter or source coefficient.

For the actual saturated U=F5 in H tensor O, each constant h in H* restricts to a global section of U*. Taking the order-k jet of those sections and extending O-linearly defines H* tensor O -> P^k(U*). The jet operator itself is not asserted O-linear on arbitrary sections. Dualizing this particular constant-system map gives the claimed O-linear map into the constant H bundle. In a local frame its image is the span of U and its derivatives through order k, independent of the chosen frame.

The successive forward-transform relations show that the fourth-order map has generic image F1 of rank ten. Its composite into (H tensor O)/F1 vanishes generically. That quotient is locally free because F1 is saturated, so the composite is identically zero. This justifies regular factorization through F1, rather than only a rational or generically defined map.

The source is W tensor Sym^4 W tensor O(-5)=(S4+T6)(-5), of rank ten and degree -50. The factored map has nonzero generic determinant. Its determinant line has degree zero, so its determinant vanishes nowhere; it is an everywhere isomorphism. The identical argument at lower orders recovers exactly

    F2=(A_std+D)(-6), F3=(W+S4)(-7),
    F4=(1+A_std)(-8), F5=W(-9).

Crucially, this uses completeness only to prove the universal principal-parts formula. The actual restriction map H* -> H0(U*) is never assumed onto the twenty-dimensional complete system, and the argument does not require it to be onto. The actual fourth-jet map's generic rank comes from the established derivative flag, not from any assumed coefficient completeness.

## 5. The actual cubic derivative kernel in K5

The top S4(-3) subbundle can project only into D(-2), by the displayed source degrees and inequivalent same-degree coefficients. The relevant Hom multiplicity is one, so its image is the canonical evaluation kernel. The D-row of the actual quotient then factors through O(2). It is nonzero, since otherwise D(-2) would be contained in K, contradicting its strict top. The unique equivariant O(2)->A_std(4) map is the quadratic dual-evaluation inclusion and is saturated, with cokernel W(5).

Differentiation of U3 is permitted to land in E/U3 because U3 lies in the actual derivative kernel K. Its projection to (E/D(-2))(-2) is zero by ordinary degree. Hence its own second fundamental form factors through O. It is nonzero by the negative-horizontal-subspace contradiction. The unique nonzero cubic evaluation S4(-3)->O is everywhere onto and has kernel A_std(-4).

Projecting to E/K composes this map with the saturated quadratic inclusion j(-2), so the kernel remains exactly A_std(-4), not merely a subrepresentation of sections. It is an actual saturated subbundle of K^-. If the negative-image branch held, the reconstruction would give the pure-degree-minus-five bundle (S4+T6)(-5). There is no ordinary map from A_std(-4) to that bundle. This is a rigorous contradiction confined to that K5 branch.

## 6. Positive images, defects and fiber characters

For K3 with no negative component, only the P and D rows can give a positive scalar-target image. A nonzero one has polynomial degree eight, so an invariant common zero divisor would have degree below the minimum twelve. Therefore it is everywhere onto. The already-contained J then makes the full coherent image A_std(2).

For K4 and K5 the S4 and V rows have zero positive scalar composition. A nonzero P row is likewise onto. If that row vanishes, the one-dimensional fixed degree-thirteen W-covariant space for K4 is generated by linear evaluation followed by f12, and the one-dimensional invariant degree-twelve scalar space for K5 is generated by f12 itself. The O(-10) row contributes no positive scalar component. The rank-two contradiction ensures the remaining image is nonzero. Thus its scalar coherent image is exactly f12 O(-8).

Because J is already contained in I, I is the complete inverse image of this scalar image. The abstract sequence splits equivariantly since H1(W(9))=0 and the group is finite in characteristic zero. This does not turn its embedding into a saturated one: A_std(2)/I is exactly O_Delta(4), of length twelve.

The minimum orbit size and total divisor degree show that Delta is a single reduced twelve-point orbit. The inherited linearization is correctly retained. As an additional independent check, the sequence O(-8) -> O(4) -> O_Delta(4) gives

    H0(O_Delta(4)) = Sym4 W + Sym6 W = D+V+P.

It has no trivial constituent, so replacing it by an untwisted permutation representation, or by twelve trivial fibers, would be incorrect. The reviewed proof makes neither replacement.

Throughout the theorem, derivative rank is the usual generic rank. In the defect-twelve branch the embedding of the coherent image into the target is not everywhere full rank. The proof explicitly retains that distinction; its statement must not be read as claiming pointwise rank three on Delta.

## 7. Independent checker and results

`independent_review_check.py` uses its own exact Q(sqrt(5)) character-table inner products rather than importing the author's checker or its McKay-product recurrence. It verifies character-table orthogonality, the fixed identities and Hom multiplicities used here, the inherited torsion character, fixed input/flag ranks and degrees, the exact polynomial square completions, and the input hashes/manifest. It performs no actual-instance evaluation, candidate search, height search or selected-parameter computation.

All 177 checks use explicit `require` failures, not removable Python assertions. Both invocations pass with equal check counts:

    python independent_review_check.py
    python -O independent_review_check.py

Retained results:

- `independent-check-normal.json`: PASS, 177 checks.
- `independent-check-optimized.json`: PASS, 177 checks.

Checker SHA256: `8f488171769640326301ead0c8e6572b79a87bc7d338a0b0dc1ce0b34b5bcbd7`.

Normal result SHA256: `338fb2b9d6d5e244a3423f12adb80412060e892ad7d7af479c910d75033bef4f`.

Optimized result SHA256: `b7be5298cdd87f60b6c32024ee172447215d88f4472b40fd0bebf1ce0872977f`.

The checker verifies fixed arithmetic, not the differential-geometric premises. Those are addressed in the mathematical review above and remain conditional on the imported actual setting. All files were written only to this local review packet; no public write, merge or upstream submission was performed.
