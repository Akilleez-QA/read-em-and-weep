# Independent mathematical audit

Reviewed proof SHA256 `d9ff304b9c01cc1931b6f3aaa498ac4898e64067d8e795b73e3a563273575753`.

The final convention explicitly centers the entire complex, including P, N and Q, by one degree. This clarification was reread and checked before rebinding; it makes the scalar-valued alternating form grading-correct.

Verdict: PASS under the explicit PR228 family and PR248 comparison hypotheses. This is mathematical review, not formal verification.

1. At axis primes the regular local dimensions are four or five. The three depth inequalities give depth at least two without assuming flatness of P. Any torsion associated prime would lie on the axis and violate these inequalities. The total module is therefore reflexive.
2. The descended alternating form is perfect off codimension four. Reflexive extension of it and its inverse proves total ordinary self-duality, without asserting local freeness.
3. The Hom multiplication sequence gives exactly the stated dual-base-change injection and torsion cokernel. The grade-four dual monad calculation is valid on the total fivefold as well as its fourfold fibers. Comparison on the free locus identifies the map with the original elementary modification and fixes its character.
4. The four fourth powers annihilate P and form a regular sequence. The Koszul change-of-rings collapse and the complementary-monomial Frobenius pairing prove the relative Ext formula. The net grading shift is +16 minus 12, hence +4. Orientation factors must remain in equivariant claims.
5. The universal-coefficient exact sequence follows by reducing a finite projective resolution, which remains exact because N is B-flat. Torsion in Ext1 controls ordinary-dual base change; torsion in Ext3 separately supplies the additional dimension in fiber Ext2. The lengths and the projective dimensions follow as stated.
6. Maps from the modified sheaf to its reflexive hull extend uniquely across the vertex. Stability makes the hull simple, so all scalar-valued bilinear pairings on the modified sheaf are multiples of the same alternating form. Their nonzero associated maps have precisely the length-one quotient, not a determinant on a nonexistent bundle frame.
7. Derived dualizing the elementary modification gives D(Q)[-4] and the cone D(Q)[-3] in the displayed positions. The cone of the ordinary pairing into the derived dual has cohomology Q, P, D(P), D(Q) in degrees zero through three. Ordinary self-duality and derived self-duality are correctly distinguished.

The strengthened exclusion concerns semistable fillings of the same fixed generic sheaf under PR248's hypotheses. It does not exclude unstable fillings, changes of generic object, or establish any result for the actual c2=5 HM source or its six pure diagonal conditions. No selected source instance or large computation was evaluated.
