# Independent review: negative quadratic degree bound

Verdict: PASS. The full rank ceilings are30 generally and27 on squares; corresponding finite last positive Smith exponents are at most24 and21 under the stated second-page pattern. An absent final pivot remains possible.

## Frozen SHA256 hashes

- PROOF.md: 4011943795bd2ba10fd3c155d75f3b177f81e784eb19f1505dc138c262c29fbb
- verify.py: 3577951beafe5de806c879c5d48f165605537f44ef2eaa5a21fbca51e49268b7
- INPUTS.json: e4aa2d3a5c5a76f29340e0231a33f374a200c0e7797115d1e8ca735fc2761838
- RESULT.json: 343f9697e2913e0ec036cdc779f434c51a8fe729875b7177d458a72412f19bdb

## Authentication and replay

All five complete public inputs were freshly fetched at their immutable manifest commits. Full contents matched the retained files, and returned Git blob hashes matched:

- PR790: 0641ffadf54324d5520aec89767658e938815223
- PR795: 9358ec81c552913fac20f3a92d7b9f7c58105656
- Original third vanishing: 7c09fe95015d7c8d932b3a27be302ca09888112d
- PR1102: bf15288e0cbcc78f5ea81eda4af6f577996f88ed
- PR1044: 516408c24d036634f0e03e29350815c2442d2880

Independent normal and optimized executions passed all39 checks. Both outputs were byte-identical to RESULT.json. Explicit exceptions keep verification active under optimization.

## Mathematical review

1. PR790 equations22 and24 identify both reconstructed arrows simultaneously with the actual fixed original negative multiplications; they do not only match characters or identify a dual pencil. Equations25 and26 give the genuine constant idempotents with image dimensions9,18,16. PR795 supplies the complementary dimensions32,36,21. The degree-two and degree-four spaces are the original positive41-to37 component. Two negative arrows compose to the negative quadratic action and preserve these summands. Q need not preserve them.
2. Rank at most9 on the first block and at most21 on the residual block gives the general ceiling30. This is valid even when Q has arbitrary off-diagonal blocks in the same gauges.
3. The complete evaluation quotients have the stated factor orientation. On N0 the quadratic gives f tensor a modulo the degree-ten polarization; on N8 it multiplies the second factor before quotient by degree-eight polarization. Naturality of the connecting maps supplies the actual quadratic action.
4. For an arbitrary square l squared, adapted formal coordinates X=l,Y=m reduce the first polarization intersection to degree-ten forms whose eighth derivatives are all multiples of X squared. Only X to the tenth survives, so the N0 kernel has dimension1 and its rank is8. This is a covariant universal computation over the entire square orbit, not evaluation of an actual direction.
5. The N8 polarization coefficients are f_XX/2, f_XY and f_YY/2. All are divisible by X squared exactly when f lies in X to the fourth times Sym4. The kernel has dimension5, giving quotient rank10. For a product of independent linear factors the corresponding kernels are zero for N0 and l cubed m cubed Sym2 for N8, giving ranks9 and12. The monomial coefficient checks exclude cancellations as well as count candidate monomials.
6. The nonsplit residual exact sequence gives a projected image of rank at most10 and intersection with the quotient kernel of dimension at most9. Hence its square rank is at most19, and adding the separated first-block rank8 proves27. No residual horizontal splitting or actual sharpness is asserted.
7. Multilinearity of every selected37-minor kills its degree-j coefficient when j exceeds rank T, since each term then includes too many dependent T columns. This argument is independent of Q. A finite last Smith pivot of valuation e therefore gives a nonzero original minor of order6+e at most30, or at most27 on squares. The finite bounds24 and21 follow.
8. The six second-rank-drop axes are semisimple and outside the square conic, so all square directions retain the three t-squared pivots. Under zero alpha the fourth row vanishes and e is at least5. Under nonzero alpha, the same lower bound holds at the twelve reduced conic basepoints because the determinant target is locally a line and the fourth row vanishes there. None of these statements selects a later obstruction or rules out an absent pivot.

The actual source hypotheses remain conditional. No actual coefficient, point, direction, jet, source matrix or instance rank was evaluated, and no public write was performed. The arithmetic certificate supports but does not replace the actual reconstruction and exact-sequence arguments.
