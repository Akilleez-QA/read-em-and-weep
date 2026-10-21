# Independent review of the determinantal cone exclusion

Reviewed artifact: PROOF.md, SHA-256
58d866004421d66f652de61751eb202d2dcf850de3d2514f4ec3493016216ab6.

Verdict: the structural exclusion and sharpness certificate are correct, conditional on the explicitly pinned PR503 Betti family and equivariant comparison restrictions. This is an independent mathematical review with exact rational arithmetic checks, not proof-assistant formal verification. The pinned earlier results are treated as hypotheses rather than reproved here.

## Checks

1. The primary source, Eisenbud–Schreyer, https://arxiv.org/html/0712.1843v3, Theorem 0.2, supplies a positive rational decomposition of a finitely generated graded Cohen–Macaulay module's Betti table into pure tables of the same codimension. Nonzero finite length over the five-variable polynomial ring satisfies the codimension-five hypothesis. The displayed Herzog–Kühl formula immediately preceding Theorem 0.1 is the one used in the proof.
2. Positive coefficients and nonnegative pure entries prohibit support cancellation. Every pure sequence therefore starts at zero, has second entry four and fifth entry eight, and has the remaining entries in the displayed support. Strict increase leaves exactly the six possibilities in the proof's parametrization. Only the two with third and fourth entries five and six can contribute at homological degree three, internal degree six.
3. For those two sequences the ratio is 15(c-5)/[24(c-6)], giving 5/6 and 25/32. The other supported pure diagrams contribute zero to that numerator. Summation proves k<=130/3, hence k<=43 for integral k. Intersecting with the assumed equivariant alternatives excludes exactly k=45.
4. All four normalized pure vectors were independently recomputed from the product formula using Python Fraction arithmetic. The stated affine decomposition matches every supported Betti entry at k=0 and k=130/3. Since both sides are affine in k, these two exact endpoint checks establish the entire identity. Additional exact substitutions at k=15,25,35 also pass. All coefficients are nonnegative throughout the closed interval; zero-coefficient summands are omitted at the endpoints.
5. The chain is ordered coordinatewise. Theorem 0.1 guarantees its pure rays belong to the rational Cohen–Macaulay Betti cone. Thus every surviving parameter passes this cone test. This is not a claim of realization by a cyclic quotient or by the actual determinantal quotient.
6. The conclusion that rho is nonzero, and that at least one of the two irreducible source channels injects, uses the pinned equivariance and irreducibility assumptions. The proof does not select a channel or assert simultaneous injectivity. It correctly avoids deducing Tor nonvanishing from the positive-degree lift in PR506.

No actual selected HM/source-instance matrix, rank, coefficient, or parameter evaluation was performed. No first-order source value, higher-order lifting, or algebraicity conclusion was checked or claimed.
