# Independent mathematical review

## Verdict and exact reviewed version

Conditional PASS for PROOF.md, SHA256 b27ab6396c92cf0d893512f786bd59ae02898e4e46c998179c7cf3fc01ab7186.

The conditions are the pinned universal quadratic relation inclusion, the published symmetric-power and scalar-algebra Hilbert functions, the complete resolution of H, and the companion generalized-complex reciprocity theorem. The companion theorem is pinned to PR507 commit 87c9b317bd4b1116e63212a6d7ec2730486b2032, whose proof was read back. The final edit added that exact reference and improved spacing; the reviewed mathematics is unchanged.

## Independent checks

1. Contracting the relation inclusion by a nonzero binary covector produces multiplication by the nonzero form beta*x-alpha*y on each E coefficient. It is injective without evaluating the selected source. For each left-strand minimum degree, exterior coproduct followed by this injection remains injective because a left inverse and wedge recover i times the original exterior tensor. Generic-covector evaluation is applied to tensors whose coefficients lie in the original field; their polynomial coefficients vanish identically if the generic evaluation vanishes. This avoids confusing a fixed evaluation of the whole symmetric-power space with an injective scalar map.
2. For a=2,...,8, the dimensions of C1 in degrees 3 and 4 are 50a and 150a. The C0 dimensions are 35(a+1) and 70(a+1), and C2 first occurs in degree 4 with dimension 45(a-1). Subtraction with the proved injectivity yields the two displayed lists. The degree-3 components are minimal generators; the degree-4 list is only a list of component dimensions.
3. In C0, the ten-dimensional constant kernel generates a free direct summand before degree-6 boundaries appear. Thus its degree-5 multiples have dimension 50. The total degree-5 kernel has dimension 225-123=102, leaving exactly 52 new degree-5 generators. No assertion excluding later generator degrees is used.
4. In C1, the complete H resolution gives twenty degree-4 generators of the relevant kernel, with its first relations in degree 6. The Buchsbaum–Rim boundaries begin in degree 6, so all twenty survive and no new generator degree can appear in the quotient. Its degree-5 dimension is 100. Reciprocity exchanges these generators with the stated level socle of M3 of C7.
5. For C4, the free-term numerator is correct, including the splice gap from degree 8 to degree 12. Direct binomial coefficient arithmetic gives coefficients -95, 35 and 135 in degrees 5, 6 and 7. The support bounds follow from minimum-degree injectivity and reciprocity. The zeroth and fourth homology vanish in this interval. Hence the three paired middle-defect formulas are correct. Nonnegativity gives h5>=95 and length at least 2*(35+135)=340. This is a lower bound, not an exact length or Hilbert function.
6. The orientation factor has dimension one and does not affect these dimension or socle conclusions. No pairing symmetry or equivariant orientation trivialization is inferred.

## Scope of verification

This is independent mathematical review conditional on the named inputs, not formal proof-assistant verification. No selected actual HM/source-instance evaluation, numerical multiplication matrix or rank computation, coefficient search, or large computation was performed. The unresolved determinantal connecting parameter and fixed-source lifting/algebraicity questions remain open.
