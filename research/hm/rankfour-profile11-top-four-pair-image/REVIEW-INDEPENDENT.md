# Independent review of the actual positive endpoint image

## Verdict and frozen target

**PASS.** No mathematical correction is required in the reviewed proof.

Reviewed `PROOF.md` SHA256:

`db1e23909dbabd423cbeb855f0f376e7e0fac53d557fdd8aef7685b5449edfdb`

The complete proof was read, including the distinction between an actual derivative in the original constant ambient and an ordinary equivariant bundle splitting. The four complete imported sources and the preceding top-four reduction were also read. All five complete files were independently fetched afresh from GitHub at their immutable commit pins. Their full retained bytes match the fresh responses and their declared byte lengths, SHA256 values and Git blob identities; metadata and full-byte-match flags are saved in `REVIEW-AUTHENTICITY.json`. The preceding reduction has SHA256 `56bb8a0aa5ada0f550e0967ef9e535838e9162c2ff2e5ced039a3f6ddb2aacf0`.

The final proof differs from the initially reviewed version only by adding the newly available immutable PR1194 source attribution. Reversing that one sentence recovers the exact initial proof SHA256, independently confirming that no mathematics changed.

The verdict is conditional on the actual geometric premises imported by those sources. This is not a proof-assistant certification of their transitive HM geometry. It certifies the new derivation from those premises and the displayed universal representation identities.

## 1. Kernel splitting and the local tail budget

For both positive parts, the quotient has rank four and degree two. Thus the actual kernel has rank thirteen and degree minus fifty-six. Strict top bounds every degree of K by minus three. The imported source-D cubic alternative is exactly zero or S4, not an arbitrary odd representation.

Direct closed-character calculation independently confirms

- chi(K(3)) = S4 - W' - T6;
- chi(K(4)) = A_std + 2V;
- H0(A_q(1)) = S4 + 2T6;
- H0(A_q(2)) = D + 2V + 2P.

The positive S4 multiplicity in the first Euler character rules out the zero cubic alternative: H1 has genuine nonnegative multiplicities. Consequently R3 = S4 and H1(N(3)) = W' + T6.

For an irreducible tail block R(-j), j at least five, its contribution has dimension (j-4) dim R. The eight-dimensional budget therefore proves j at most twelve before checking any atoms. Central parity and constituentwise containment leave exactly the seven rows stated in the proof. This is a local irreducible budget check, not a search through kernel bundles or quotient candidates.

The character budget has only six decompositions. Their quartic H1 characters and resulting R4 are:

- W'(-5) + T6(-5): H1 = 0, so R4 = 2V - D;
- W'(-5) + V(-6): H1 = V, so R4 = 3V - D;
- W'(-5) + W'(-7): H1 = P, so R4 = 2V + P - D;
- W'(-5) + O(-10): H1 = D, so R4 = 2V;
- P(-6): H1 = P, so R4 = 2V + P - D;
- O(-12): H1 = V + P, so R4 = 3V + P - D.

Only the fourth is genuine. Hence the stated splitting of K follows without assuming anything about its derivative image. Its rank and degree independently check to thirteen and minus fifty-six.

## 2. Actual cancellation and the unique Euler line

The negative quotient projection E -> O(-8) is zero on all source rows except O(-8), simply by degree. It must be nonzero on that last line because p is a bundle surjection. Its kernel is therefore the stated rank-sixteen source subbundle E0, and restriction gives the actual exact sequence 0 -> K -> E0 -> F -> 0. This is a statement about the actual quotient map, not a horizontal decomposition. Since E0 is saturated in E and E is saturated in the original ambient, E0 is saturated in that ambient.

The evaluated S4(-3) top block of K has no Hom to the source rows except D(-2), where the equivariant Hom dimension is one. The standard binary evaluation sequence identifies its image with the complete quartic evaluation kernel. This identification is an actual subbundle equality up to nonzero scalar, rather than an equality of abstract characters. Killing that kernel makes the actual D-row factor through O(2).

The factor is nonzero. Otherwise the whole D(-2) source row would lie in K, contradicting H0(K(2)) = 0. In either positive quotient, the factor to O(4) vanishes equivariantly. The remaining factor is either a scalar isomorphism onto the O(2) summand, or a nonzero scalar multiple of the standard Euler injection O(2) -> W O(3). Thus it is saturated in both cases, and its quotient is 2O(4).

No arbitrary choice of a second Euler direction is introduced later. Both occurrences of j are the same actual line, up to its irrelevant nonzero scalar.

## 3. Cubic derivative row: exact image, not just generic image

Because K is the actual derivative kernel of E, the actual derivative of K factors through (E/K)(-2). The S4(-3) row has zero O(-10) component by ordinary degree. Its equivariant Hom to F(-2) is one-dimensional. Cubic evaluation followed by j(-2) is a nonzero member of that Hom and therefore spans it.

The actual row cannot vanish. A killed coefficient vector gives a saturated O(-3) line in K. Its own ambient derivative would land in (K/line)(-2), whose maximal degree is at most minus five. The corresponding Hom vanishes. The line would be horizontal and therefore constant in the original constant ambient, impossible for a saturated negative line over C.

The actual S4 row is consequently a nonzero scalar multiple of full cubic evaluation followed by j(-2). Full cubic evaluation has no basepoint. Its sheaf image is exactly j(-2)O at every parameter, not merely its saturation.

## 4. Quartic derivative rows: why section information is sufficient here

The same coefficient-line argument proves injectivity of the derivative on the R4 = 2V coefficient space. It does not assert injectivity on all of H0(K(4)), and the proof correctly avoids that stronger claim.

The section sequence for the actual quotient F/jO(2), twisted by two, has kernel D because H1(O(4)) vanishes. Since D contains no V, projection preserves injectivity of the 2V coefficient image. The target has exactly two V copies, so the induced V multiplicity map is an isomorphism.

A coefficient-space isomorphism alone would not generally prove pointwise surjectivity. The proof supplies the necessary extra fact: Hom_G(V(-4), O(2)) is one-dimensional. Therefore the actual row to 2O(2) is a fixed nonzero sextic V row tensored with the induced two-dimensional multiplicity map. The latter is invertible by the section argument.

The universal sextic V row is everywhere onto. Its three sections have a common zero divisor of degree at most six if it is nonempty. That divisor is invariant under the projective A5 action. A finite subgroup of the stabilizer of a point of P1 is cyclic: after moving the fixed point to infinity, a finite affine group has a common finite fixed point by averaging and becomes a finite group of scalings. A cyclic subgroup of A5 has order at most five. Thus each projective orbit has size at least twelve, precluding a nonempty invariant effective divisor of degree at most six.

This argument neither chooses a parameter nor evaluates an actual coefficient or rank. It establishes basepoint-freeness uniformly for the unique representation-theoretic sextic channel.

The quartic rows therefore surject onto the quotient F(-2)/j(-2)O everywhere. The cubic row already surjects onto its kernel j(-2)O. Combining these two sheaf statements proves that their sum has image all of F(-2), including at every parameter. Both rows have zero negative component by degree.

## 5. Full endpoint image and the adjacent Gauss pair

The original maximal profile gives generic rank beta_K at most three. The preceding actual rows already put the entire rank-three F(-2) subbundle in its sheaf image. Any remaining row with nonzero O(-10) projection would add a fourth generic image direction. Therefore the projection of every remaining row is generically zero and hence zero as a bundle morphism on this integral curve. The complete sheaf image is exactly F(-2), with no torsion or saturation defect left over.

The exact sequence 0 -> K^- -> K -> F(-2) -> 0 now yields rank K^- = 10 and degree K^- = -60. This uses the genuine image degree four, not only its generic rank.

Since F is saturated in E/K and E is saturated in the original ambient, its preimage is a saturated rank-sixteen ambient subbundle. The actual derivative image equality makes that preimage precisely K^+ = E0.

The derivative of E0 kills K because the derivative of K lies inside E0. Conversely, composing beta_E0 with the quotient onto Q(-2) gives beta_E restricted to E0. Modulo K this is the actual coherent injection of F into Q(-2), so it has no sheaf kernel. Hence E0^- = K and the generic rank of beta_E0 is exactly three. The proof does not need or claim that beta_E0 itself has an everywhere saturated image.

Finally, K/K^- is the actual image F(-2), and E0/K is F. Thus the adjacent graded derivative is the stated bundle isomorphism. None of these steps equips K/S4(-3), or any other ordinary quotient, with an unproved flat connection.

## 6. Independent arithmetic checker

`review_verify.py` uses the nine closed binary-icosahedral class characters in Q(sqrt(5)). Symmetric powers are evaluated by the closed Chebyshev polynomial, not by the author's McKay recurrence or imported verifier. It checks the orthogonality, completeness, dimensions, central parity and physical V marking of the character table, then only the fixed identities and local budget needed in this proof.

It verifies the reviewed proof fingerprint, all five retained source-file identities and their independent fresh-authentication records, both quotient Euler and section calculations, the seven local atoms, six explicit budget decompositions, unique genuine R4, fixed Hom dimensions, the source-tail cancellation, all rank and degree arithmetic, and the frozen predecessor hash. No actual instance, coefficient, point, jet, tensor, matrix or selected rank is evaluated. No historical domain or global bundle candidate enumeration is read or generated.

Both commands passed with 770 explicit checks:

    python review_verify.py
    python -O review_verify.py

All checks use explicit failure conditions, not Python assertions. Their outputs `REVIEW-RESULT.json` and `REVIEW-RESULT-OPTIMIZED.json` are byte-identical. The JSON records the reviewed proof hash and scope limitations. The geometric arguments reviewed above are manual reasoning, not claims of computational formalization.

## 7. Contribution and boundary

The proof does establish a new necessary actual-map structure for exactly the two specified positive quotient forms: the same forced K, an everywhere full positive endpoint image, the actual rank-sixteen forward transform, its predecessor, and one exact graded derivative isomorphism.

It does not exclude either form, establish its realization, address the triplet-positive third form, set the original determinant defect to zero, transfer a rank-seventeen theorem to E0, or close the maximal rank-four profile. These boundaries are stated correctly in the proof.
