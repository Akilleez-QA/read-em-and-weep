# The 25 rank-zero points have Cohen–Macaulay type two

## Scope

Let E,U,C and X_B be the actual HM evaluation data of PR543. Use the already established facts that each X_B is pure locally Cohen–Macaulay of codimension two, and the evaluation minors of U generate the reduced 25-line scheme C. Use KAPPA-RATIONAL-SEXTIC.md at commit 3edb50b13b8a5ce876f52a2085ecc8d16b3181c0: the parameter locus Gamma is a smooth rational sextic, and each component line maps isomorphically to Gamma.

This note treats the fixed beta degeneracy surface X_B, not the distinct primary bad-quadric scheme. All coordinates below are abstract regular local coordinates, not selected HM coefficients or evaluated fixtures.

## 1. Exact non-Gorenstein locus

For B in Gamma there are exactly 25 points p_i, one on each line, where B evaluates with rank zero. At each p_i the surface X_B has embedding dimension four and Cohen–Macaulay type exactly two. At every other point of X_B it is a local complete intersection and hence Gorenstein. Therefore the support of its non-Gorenstein locus is exactly these 25 points.

Proof. Work in the regular local ring R=O_{P4,p_i}, of dimension four. The matrix of B -> E has size 2 by 3 and all entries in the maximal ideal m. Its maximal minors generate the ideal I of X_B, of height two. The Hilbert–Burch complex is exact:

0 -> R^2 -> R^3 -> R -> R/I -> 0.

Every entry in its nontrivial differentials lies in m, so this is a minimal free resolution. In particular the three minors are minimal generators, and the last Betti number is two. Since R/I is Cohen–Macaulay, its Cohen–Macaulay type is two. Its defining ideal is contained in m^2, so its embedding dimension is dim(m/m^2)=4, larger than its dimension two. It is singular and non-Gorenstein.

Conversely, B cannot evaluate with rank zero off C: U evaluates onto the rank-two E there, so the fiber kernel of U has dimension two and cannot contain the three-space B. At every rank-one point of X_B a unit entry reduces its defining matrix to [1,0,0;0,a,b]. Its ideal is (a,b), of height two in a regular local ring, hence a regular sequence. This proves the converse.

These points are also precisely the singular points of X_B lying on C. Every other point of C is smooth on X_B by the Cartier smooth-curve argument in BETA-IMAGE-DIMENSION-DROP.md at f5b50172bd65d1772d1af3d4a511decc8363183e. There may be additional singular, but Gorenstein, points away from C.

## 2. Multiplicity and component budget

At each p_i the Hilbert–Samuel multiplicity satisfies e(X_B,p_i)>=3.

Indeed a general two-element minimal reduction of the maximal ideal exists over the infinite residue field. Since the ring is Cohen–Macaulay of dimension two, the multiplicity is the length of the quotient by that reduction. The two reduction generators have independent linear parts, leaving an Artinian local quotient of embedding dimension two. Its length is at least 1+2=3. This uses only a symbolic general-reduction argument, not any actual selected parameter evaluation.

Suppose the degree-ten component branch has X_B reduced with components S and its degree-five residual cycle T, as established in the surface decomposition inputs and PR565. The associativity formula for multiplicity gives

e(S,p_i) + sum_{T_j through p_i} e(T_j,p_i) >= 3,

where terms of components not passing through p_i are zero. The component multiplicities in X_B are one under the reducedness input. Thus if S is smooth at p_i, either the residual germ there has total multiplicity at least two, or the decomposition inputs cannot hold. In the five-plane residual alternative, smooth S forces at least two of those planes through p_i. A union of just two smooth reduced component germs cannot account for a rank-zero point.

This is conditional on the degree-ten/reduced-residual decomposition; it does not claim that the residual passes through every p_i when S itself is singular.

For fixed B, the 25 pointed surface germs are mutually isomorphic: H5 fixes B and X_B, and its projective quotient acts transitively on the component lines and hence on their unique rank-zero points. Their multiplicities, Cohen–Macaulay types, and first-jet alternatives therefore agree. If the degree-ten component S is H5-invariant, smoothness of S at one rank-zero point means smoothness at all 25.

In the five-plane residual alternative with S smooth at those points, every rank-zero point lies on at least two residual planes. The transitive action on the five planes then gives at least ten rank-zero points on each plane, by counting the at least 50 point-plane incidences and using equal incidence numbers. This is a necessary incidence budget, not a proof that such an arrangement occurs.

## 3. Intrinsic first-jet alternative

At p_i choose a section outside B whose evaluation is nonzero. Local row operations write the full evaluation as

[1, b1, b2, b3; 0, a1, a2, a3].

Here I_C=(a1,a2,a3), and each b_j vanishes at p_i. Because C is smooth these a_j form normal coordinates. The isomorphism kappa_L:L -> Gamma implies the derivative of (b1,b2,b3)|L is nonzero. Constant column operations among B put that derivative in the first direction; replacing the longitudinal coordinate by b1 gives regular parameters (t,a1,a2,a3), with b1=t and the first jets of b2,b3 equal to linear forms l2(a),l3(a) in the normal variables only.

The degree-two part of the initial ideal is therefore spanned by

q12=t*a2-a1*l2,
q13=t*a3-a1*l3,
q23=l2*a3-l3*a2.

There are exactly two possible forms:

- Exceptional first jet: l2=c*a2 and l3=c*a3 for one scalar c. Then q23=0 and the quadratic initial part is generated by (t-c*a1)*a2 and (t-c*a1)*a3, a height-one ideal with only two independent quadrics.
- Nonexceptional first jet: the three quadrics are independent and their ideal has height two.

To check completeness, q12 and q13 are independent. If they have a common factor, it must be linear. A factor independent of t would divide both a2 and a3, impossible. Normalize it to t-h(a). Divisibility implies a1*l2=h*a2 and a1*l3=h*a3, hence h=c*a1, l2=c*a2, l3=c*a3. Conversely these equations give the displayed exceptional factorization. In every other case the two quadrics have no common factor, and the determinantal height bound gives height exactly two. Also q23=0 is equivalent to that exceptional scalar form, and a constant linear relation among the three quadrics must have zero q12 and q13 coefficients by comparing t terms.

In the nonexceptional case, the tangent cone is exactly the codimension-two linear determinantal cone cut out by these three quadrics, and e(X_B,p_i)=3. Indeed its Hilbert–Burch resolution has shifts (0;2,2,2;3,3), so it is a pure Cohen–Macaulay degree-three cone. It surjects onto the associated graded ring of O_X,p_i. Section 2 gives multiplicity at least three for the latter, whereas a graded quotient has multiplicity at most three. Equality and unmixedness of the cone imply the kernel is zero: any nonzero ideal in this Cohen–Macaulay equidimensional ring has support of dimension two and positive multiplicity, which would strictly lower the quotient multiplicity.

No assertion is made here that the actual first jet is nonexceptional. In the exceptional case higher-order terms matter; these quadratic equations alone do not describe the full tangent cone. The three exact minors still minimally generate the local ideal even when their quadratic parts span only two dimensions.

## Boundaries

Type two and the multiplicity lower bound hold at all 25 rank-zero points for every B on Gamma. The degree-three tangent cone conclusion is conditional on the explicit first-jet criterion. No ordinary-double-point, reduced-cone, normality, or generic-jet claim has been substituted for actual data. This does not exclude the residual beta family, whose active hyperplane points avoid these rank-zero points. No selected coefficient or rank was evaluated, and no experiment was run.
