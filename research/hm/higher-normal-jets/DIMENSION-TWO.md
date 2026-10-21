# The actual evaluation rank-drop locus has dimension two

## Inputs

Let e:E=3Q(-1) -> 10O on P4 be the actual primary Euler-quotient evaluation and let D=D_9(e) be its scheme of maximal minors. This is not the different primary-bad eightfold in P14.

- PR555 at ff5a3164337016e96e3a29a9ad37891130a66e29 proves dim D<=2.
- PR554 at eb16c0e38e5157dc2902273cea3939b3410057c7 proves the rank-eight locus is exactly thirty reduced points and there is no smaller rank.
- PR562 at 86b643fe2adecbd321d1c8f98be84fe2082bcd10 gives twenty-five pairwise disjoint projective lines contained in D, all of rank nine.
- The companion PROOF.md, using PR563 at 56c3c4c37bd51fc710eec4b80662c5506f357f8f, constructs a sixth-order normal thickening S_6 of each of these lines as a closed subscheme of D. At a generic point of a line which is a one-dimensional component, this forces scheme multiplicity at least seven.

## Contradiction to dimension one

The lines give dim D>=1. Suppose dim D=1. The maximal-minor locus of the dual map 10O -> E* (ranks ten and twelve) then has its expected codimension three. The expected-codimension maximal-minor theorem (Eagon-Northcott) makes it Cohen-Macaulay of pure dimension one; the expected-codimension Thom-Porteous formula gives

[D]=c_3(E*) in A^3(P4).

The dual Euler sequence gives

0 -> Q*(1) -> 5O(1) -> O(2) -> 0,

so, with H the hyperplane class,

c(E*) = (1+H)^15/(1+2H)^3.

Its degree-three coefficient is

455 - 630 + 360 - 80 = 105.

Therefore the one-cycle D would have degree 105, with its generic scheme multiplicities included.

Each of the twenty-five distinct lines is a one-dimensional irreducible component under the hypothesis dim D=1. Localizing the closed embedding S_6 -> D at its generic point gives a surjection from the Artinian local ring of D onto the length-seven algebra C(L)[z]/(z^7). The multiplicity of that line in the fundamental cycle is consequently at least seven. Since every line has degree one and all other component degrees and multiplicities are nonnegative,

deg D >= 25*7 = 175.

This contradicts deg D=105. Thus dim D cannot be one; the pinned upper bound yields dim D=2.

## Exact conclusion and limits

The actual rank-at-most-nine locus contains at least one surface component and has no component of dimension larger than two. Every surface component is generically rank nine, because the rank-eight locus is finite.

This argument does not prove that each of the twenty-five lines lies on a surface component, that any component is reduced or smooth, normality, irreducibility, or a value of the order-seven obstruction. The number 105 is the degree forced under the contradicted expected-codimension hypothesis; it is not asserted to be the degree of the actual two-dimensional locus.

No selected source coefficient, actual matrix, numerical rank, or large computation is used. This is a structural dimension obstruction obtained from finite equivariant thickening and the universal expected-codimension degeneracy-class formula.

## Public dependency links

- https://github.com/Akilleez-QA/read-em-and-weep/pull/555
- https://github.com/Akilleez-QA/read-em-and-weep/pull/554
- https://github.com/Akilleez-QA/read-em-and-weep/pull/562
- https://github.com/Akilleez-QA/read-em-and-weep/pull/563
