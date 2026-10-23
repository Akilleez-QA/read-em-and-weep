# Independent review: PASS

Reviewed exactly the whole-source exclusion for G3.11.ea6bced3bddf, original source125 tuple (0,1,0,0,0,1,0,1). No other source or whole-label exclusion is certified by this review.

Exact reviewed files:

- PROOF.md SHA256: 57b6b69c9dc1229b937ca3767baaeb5ee5a080b97bca7b81a3dd01529e9d2c4b
- verify.py SHA256: 91f6c8728939f75d675080d7870e04e85fde66dd4a0cefc40b2607e27e830138

## Structural audit

1. The cubic-T obstruction is valid. Strict-top and the invariant-divisor bound make the degree-seven quotient onto. Its kernel is V O(-4)+Wp O(-5); the twist-three H1 budget Wp and twist-four Euler character V determine it completely. The internal image vanishes, so the first increment is exactly O(6). Rank-one Gauss increments and the third-derivative coefficient-span bound exhaust the possible lengths. The two-increment branch is killed by the absence of an invariant in Sym4 W, and the three-increment branch violates total degree.

2. The lower-P-row-zero reduction covers all three inherited high-(P+D) kernels. Its only possible nonzero internal image is O(-10), with no unsaturated line branch. The zero-image branch reduces to the cubic obstruction. The nonzero branch necessarily contains a complete direct linear summand in the projected first span, which contradicts its vanishing H0. The restriction of a nonzero lower P row to the canonical Euler Wp O(-3) is therefore nonzero and onto; its attempted factorization through Wp O(-1) has zero equivariant Hom.

3. The high-D kernel exhaustion is complete. Its rank is four and degree is -26. The rank partitions 4, 3+1, 2+2, 2+1+1, and 1+1+1+1 are all covered. The scalar H1-budget atoms are exactly O(-6) and O(-10), so only Wp O(-5)+O(-6)+O(-10) remains. The stated internal Hom channels are exhaustive. After quotienting by the tautological Wp image, a nonzero P component of the O(-10) map remains nonzero because its possible factorization through Wp O(-5) has zero Hom. The projected degree-seven covariant is basepoint-free. Thus each listed internal image is saturated, including the simultaneous rank-three image, and the four first-span degrees and the two surviving splittings are justified.

4. For the constant A+P first span, the exact intersection with E is D O(-2)+O(-8), rather than an abstract complement taken to be horizontal. The scalar, T, and P-only cases of the remaining line injection are exhaustive. In the T case, the nonzero tautological map is an isomorphism on the indicated twist-one H1 groups, forcing the entire rank-nine quotient to degree -2 and coefficient P+D. In the P-only case, dualizing the already established degree-six P quotient gives the actual constant V quotient. Both resulting reductions are valid.

5. The crucial second constant span is genuine. After projecting the actual constant A, D O(-2) has first span T O(-1); its quadratic coefficient span has rank seven, degree zero, and representation V+P. Lifting through A gives a constant rank-ten C. The Wp O(-3) in E intersect M is intrinsic to the original P summand: it has no T component and cannot acquire a D lift because Wp is absent from D W. Its derivative has zero negative O(-10) component by ordinary degree and supplies the nonzero lower positive direction, while M/N supplies the high direction. Therefore the generic image of C/N is precisely the positive rank-two subbundle of Q. Saturation of that positive subbundle gives actual factorization, and equality of degree 24 makes the generically invertible determinant a nonzero constant. This establishes C/N = O(18)+O(6) everywhere, not merely generically, and E intersect C=N.

6. The final constant projection has rank nine, degree -30, and saturated derivative image O(-10). The three possible component cases of its remaining O(-8) line are exhaustive. The T case has injective H1 map, dual to the surjective multiplication Sym5 W tensor W -> Sym6 W; the P-derived Wp-only case creates a forbidden positive O(6) summand. The remaining cases have H0=0. Strict-top then forces every splitting degree to be at most -10, contradicting degree -30 at rank nine.

No connection-compatible abstract splitting was assumed in these arguments. Constant projections, saturation, exact intersections, and the use of total degree were checked separately from character arithmetic. No mathematical gap requiring an amendment was found in the reviewed version.

## Reproduction and restrictions

Independently inspected and ran verify.py. It returned:

    PASS: high-D kernel, 42 fixed internal Hom checks, polar and cubic-T identities, original source125 bf identity.
    No source/model evaluation, support search, all-twist envelope, or current frontier count was performed.

The verifier validates both immutable input Git blobs before testing the original source and stable-label identities. Its bounded universal character checks support, but do not replace, the geometric arguments above. The review selected no actual HM/source coefficients, parameters, points, derivative evaluations, instance matrices or ranks, and performed no scan or large computation. Nothing was published during this review.
