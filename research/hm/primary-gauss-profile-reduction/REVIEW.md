# Independent whole-proof review

**Verdict: PASS, for the stated conditional, profile-specific result only.**

Review completed 2026-10-23. This review is bound to the following SHA-256 digests:

- `PROOF.md`: `350133fbc70ad5925d7d1369d947b873c7b29118244f2283ba5b1e47eebd349a`
- `RESULT.json`: `0f426f09ad15efd8a7c5b44438733fe9a453c566fec9378c48459c6eed5f86fb`
- `INPUTS.json`: `0582bde7aa9d1d800bd0ebecc403f14ca6f83390f2422136014f499d5e0d648b`
- `verify.py`: `6aded8eacf3203f47301b8f63edcf6e71434b052a3ee208b60cec3b0c581b058`
- `characters.py`: `5b3b1d415f26ca467670afeb73357cbb0e9c125a6b1acd25155b6d85eef4e4f1`

The verdict is not a global COV theorem, a certification of the later 182-to-23 historical exclusion chain, or a realization claim for any retained row.

## 1. Imported hypotheses and actual-object identity

I read the complete nine frozen source documents/data files and recomputed their byte counts, SHA-256 digests, and Git-blob SHA-1 digests against the manifest. All match. The packet author's fresh public-byte authentication is accepted; this review did not repeat its remote fetches.

The original profile-(1,2) ten-pair theorem and profile-(2,1) thirteen-pair theorem are explicitly imported necessity theorems. Their displayed lists agree with the relevant fixed rows. The JSON supplies stable labels, not geometric necessity. In particular, the separate second-dual defect in profile (1,2) is not identified with its zero original defect.

PR1123's four possibilities concern the actual kernel bundle E and are independent of occurrence of a later source-pair ledger entry. PR1124 constructs its primary subbundle in that same E through the actual terminal pencil, with a common parameter/determinant convention; it also proves the quotient's top-degree bound. The new argument retains E's original saturated inclusion in the constant ambient bundle for every derivative. It never substitutes the terminal-pencil inclusion as the Gauss inclusion. No ordinary complement is promoted to a horizontal or multiplication-compatible complement.

## 2. Geometric proof checks

### Cubic coefficient visibility

For a nonzero coefficient vector of C=(W'+T)O(-3), its line L=O(-3) is saturated in C, E, and the constant ambient bundle. The sequence with outer terms C/L and E/C bounds every degree of E/L by -2; this is a consequence of the actual primary quotient bound, not an invalid assertion that every quotient of a negative bundle is negative.

If L is killed in A_q=E/ker(beta_E), its internal second fundamental form lands in (E/L)(-2). The relevant Hom space is zero. Hence L would be horizontal, and saturation plus characteristic zero would force degree zero, a contradiction. This proves injectivity on the coefficient/global-section space W'+T. It does not assert fiberwise rank-eight injectivity into A_q.

### Iterated section envelope and rank-drop endpoints

The kernel of a vector-bundle morphism on the smooth parameter curve is saturated in its source when its quotient is identified with the torsion-free image. Thus each F_i is saturated in the original constant bundle. For a local section of F_i, its derivative lies in F_{i-1}; modulo F_i this is the second fundamental form of F_i. Its kernel is exactly F_{i+1}. Consequently the induced injection

    F_i/F_{i+1} -> (F_{i-1}/F_i)(-2)

is valid even if the derivative rank drops, even if its image is not saturated in the target, and if a later kernel is zero. Iteration gives J_i -> A_q(-2i).

Strict top-degree decrease gives maxdeg F_{r-1} <= -r-1, so H0(F_{r-1}(r))=0. The exact sequences successively bound H0(F_i(r)) by H0(F_{i+1}(r))+H0(J_i(r)); semisimplicity then gives the displayed character inequality with i=0,...,r-2. Thus r=4 has exactly three terms and r=10 exactly nine terms. No later rank-three plateau is presumed.

## 3. Exhaustion of the cases actually claimed

For profile (1,2):

- Old indices 0,2,4,12,20 fail the quotient degree test, since the four possible E types have no degree below -8.
- Old index 6 requires a surjection onto 2O(-8), whereas the source portion of degree at most -8 has rank at most one. The rank argument, not two separate nonzero-Hom tests, excludes it.
- Old index 8 fails cubic W' visibility.
- Old indices 7,21 have only two V copies in the r=4 envelope, and old index 14 has one, against at least three in H0(E(4)).

These are precisely all ten original indices. None of these arguments depends on the separate second-dual defect.

For profile (2,1): original index 0 fails degree; indices 1,8,12 fail cubic visibility. Every remaining shape except index 11 contains O(-8), forcing the exact D-type. Index 11 has W'O(-5)+O(16): the V-type and zero-top type have no source of low enough degree, and the D-type's only possible lower source has zero equivariant Hom to W'O(-5). The identity W' tensor Sym3 W=V+D verifies that last claim. The only possible source is the P-type, and the r=10 invariant deficit excludes it.

The retained original indices are exactly 2,3,4,5,6,7,9,10. Their source commit is f7071d29886c83151028576bf32e001c347cafc9. Their original defects, in that order, are 0,12,0,0,12,0,0,0. Both defect-12 rows have B_q=O(-18)+O(-8)+O(6); all other retained rows have B_q=A_q^*(-2). I checked the full ordered pairs and stable labels against the authenticated fixed data. The stable IDs are:

    2  G3.21.d610e381ed75
    3  G3.21.ae29bef8b31e
    4  G3.21.3bc00aa2165a
    5  G3.21.ed1df480d8d2
    6  G3.21.94406336f081
    7  G3.21.8de61cbbef4b
    9  G3.21.1c43993b4f83
    10 G3.21.d41783aef00b

As an extra consistency check, all eight retained rows satisfy cubic visibility and both fixed r=4 and r=10 section-envelope inequalities with the forced D-type. No sufficiency, simultaneous realizability, or compliance with every possible twist is inferred.

## 4. Independent character verification

In addition to reading the production code, I used a separate class-inner-product calculation that imports neither production module and does not use its tensor-by-W/McKay recurrence. This is a bounded calculation with abstract group characters, not an HM instance computation.

The nine standard trace values are

    2, -2, (1+sqrt(5))/2, -(1+sqrt(5))/2,
    (1-sqrt(5))/2, -(1-sqrt(5))/2, 1, -1, 0,

with class sizes 1,1,12,12,12,12,20,20,30. For standard trace x, the symmetric-power character was calculated directly as

    s_n(x) = sum_{k=0}^{floor(n/2)} (-1)^k binom(n-k,k) x^(n-2k).

A=s_2, S=s_3, D=s_4, T=s_5. V is the sqrt(5)-Galois conjugate of A, W' the conjugate of W, and P has class values 4,4,-1,-1,-1,-1,1,1,0, obtained from the A5 five-point permutation representation minus its constant line. The resulting nine irreducible characters are orthonormal under the size-weighted class inner product and their squared dimensions sum to 120. All product multiplicities below were obtained by that inner product, independently of the production recurrence.

This confirms:

- chi_G(E(4))=3V+3P+2D for each of the four types. For D-type, H0(E(4)) additionally has A and H1(E(4))=A; no accidental H1 vanishing was assumed.
- The rejected cubic characters are S+2T, 2S+2T, and S+2T as stated.
- The profile-(1,2) r=4 envelopes are A+2V+3P+3D for indices 7 and 21, and V+3P+2D for index 14.
- W' tensor Sym3 W=V+D.
- For the P-type at twist 10, the trivial multiplicities from its five displayed blocks are exactly (1,1,1,1,0), summing to four.
- For A_q=W'O(-5)+O(16), the W' terms with indices 5,3,1 each have zero trivial multiplicity. The scalar indices 26,24,22,20,18,16,14,12,10 have trivial multiplicities (0,1,0,1,0,0,0,1,0), summing to three.

The four-versus-three contradiction is therefore exact, and not a numerical approximation or a missing-high-degree-term artifact.

## 5. Execution and scope of the verdict

`python verify.py` and `python -O verify.py` both succeed, reproduce identical output, and confirm the frozen result with 242 checks. The independent class calculation also gives identical output with and without optimization. The proof's geometric necessity was reviewed separately from these arithmetic checks.

No production file was edited. No public write, historical enumeration rerun, selected HM/source coefficient, point, map, matrix, instance rank, or local-model experiment was used. The only newly written packet file is this review.

Under the expressly imported primary and original profile-specific necessity theorems, the direct exclusion of profile (1,2) and the exact D-type/eight-row restriction in profile (2,1) are proved. The eight D-type cases, profile (1,1), and any global maximal-profile/coverage dependencies remain open in the sense stated by PROOF.md.
