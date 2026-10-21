# General eight points of the actual sextic admit an integral elliptic pencil

## Statement

Let Gamma be the actual smooth nondegenerate rational sextic in P3 established at 3edb50b13b8a5ce876f52a2085ecc8d16b3181c0. A general ordered eight-tuple of points of Gamma lies on a smooth quadric Q0 and a second quadric Q1 such that C=Q0 intersect Q1 is integral and smooth at the eight points. It has arithmetic genus one. Global smoothness of C is unnecessary.

Consequently no integral quintic surface is triple at these eight points, by the twice-subtraction proof in TWIST-THREE-QUINTIC-SECANT-OBSTRUCTION.md. Coupling this open eight-point statement with the separately proved source-root dominance excludes the degree-five primitive twist-three nondominant image generically in the source quadric. Neither assertion treats the eight points as general points of P3.

## 1. Sectional monodromy of quadric cuts

Apply the quadratic Veronese embedding to Gamma. Its image is an integral curve of degree twelve in its linear span. Hyperplane sections are precisely restrictions of ambient quadrics of P3. In characteristic zero the sectional monodromy is the full symmetric group S12: Borys Kadets, Sectional monodromy groups of projective curves, Proposition 1.1 (and Remark 3.5), arXiv:1809.07293v4, https://arxiv.org/pdf/1809.07293 . The proposition was read directly in the primary paper. Passing from the effective linear system on Gamma to ambient quadric coefficients adds connected affine fibers on suitable projective charts, so the same ordered-section covers over ambient quadrics are irreducible.

In particular, over the open locus of transverse quadric cuts, the cover parametrizing any specified number of ordered distinct intersection points is irreducible. A proper closed incidence condition on such a cover fails for every corresponding subset over a general quadric.

## 2. A six-point witness

Choose six general points of Gamma in linear general position. Six points of P3 in linear general position lie on a unique twisted cubic T. They impose six independent conditions on quadrics, so quadrics through them form a four-dimensional vector space. The three-dimensional I_T(2) is a proper subspace. A quadric Q* in the difference cuts T in exactly the six reduced points, since O_T(2) has degree six.

It follows that the entire four-dimensional quadric system has base scheme exactly those six reduced points: the three quadrics generating I_T and Q* generate the reduced six-point ideal locally. Off those points the system is basepoint free; at them its first derivatives span the cotangent space. Bertini and the basepoint derivative statement therefore give a smooth general member Q0. It can also be chosen transverse to Gamma at all twelve intersection points and outside I_T(2).

Thus there exists a transverse smooth quadric cut with a six-subset whose unique twisted cubic is not contained in Q0. By the irreducibility in section 1, for a general smooth transverse Q0, no six-subset of Gamma intersect Q0 has its twisted cubic contained in Q0. Linear general position of all such six-subsets follows in the same way: one can start with six general points of Gamma. In particular, no four of the twelve points are coplanar and no three are collinear.

This argument does not require Gamma to lie on no quadric. The effective Veronese span can have lower dimension; ambient quadrics through six still form the stated four-dimensional vector space.

## 3. Every nonzero (2,2) curve through eight is integral

Fix a general Q0 as above and eight points of Gamma intersect Q0. The vector space H0(Q0,O(2,2)) has dimension nine, so there is a nonzero section vanishing at all eight points. Lift it to a quadric Q1 not proportional to Q0, and write C=Q0 intersect Q1.

Suppose C is not integral. Its total degree is four. A line can contain at most two of the eight points, and a plane conic at most three. If the reduced support has total degree at most three, it cannot contain eight points: a twisted cubic would need at least eight and therefore contain a forbidden six-subset; a conic and a line contain at most five; three lines contain at most six. The planar-cubic possibility also contains at most three.

For reduced degree-four support, two conics contain at most six points; a conic and two lines contain at most seven. Four lines would need two points on each. On a smooth quadric a divisor of class (2,2) consisting of four lines has two lines from each ruling. Two lines from opposite rulings span a plane, which would contain four marked points, impossible. The remaining possibility is a twisted cubic plus a line, with at least six marked points on the twisted cubic. It is contained in Q0 and contradicts section 2. A planar cubic plus a line contains at most five. This exhausts reducible supports and nonreduced divisors, so C is integral.

## 4. The marked points can all be chosen smooth on C

An integral (2,2) curve on a smooth quadric has arithmetic genus one. The genus formula for normalization implies its singular locus contains at most one point.

To make the genericity argument precise, use the irreducible cover parametrizing Q0 and eight ordered distinct points of its twelve-point Gamma section. Shrink to a nonempty open where the dimension of the space of (2,2) sections through the eight points is constant. Its projectivization is an irreducible projective bundle. The permutation group S8 acts by permuting labels and does not alter the section space. All its curve members on the good base are integral by section 3.

For each i, the locus where the chosen curve is singular at its ith marked point is closed. If their union filled the irreducible total space, one of these closed loci would be the whole space. Label permutation then makes all eight the whole space, forcing eight distinct singular points on an integral arithmetic-genus-one curve. This is impossible. Hence a general chosen curve is smooth at all eight marked points.

The marked points are noncoplanar. The integral elliptic-pencil criterion now applies.

## 5. Passage to a general tuple on Gamma

At most one independent quadric can contain a nondegenerate integral sextic. Two independent quadrics without a common factor have intersection degree four; if they have a common plane, their common zero set is a plane union a line, and an integral nondegenerate curve cannot lie in it. Thus the quadratic restriction space on Gamma has dimension at least nine.

General eight points impose eight independent conditions on this restriction space. Hence ambient quadrics through a general ordered tuple form a two-dimensional vector space. The incidence over general Gamma^8 is therefore a P1-bundle of dimension nine. Its general member does not contain Gamma (the subspace of quadrics containing Gamma has vector dimension at most one). Consequently its projection to quadric parameter space has finite fibers, since a quadric not containing Gamma cuts it in a finite scheme. Its image has dimension nine and is dominant. It meets the transverse open, where it agrees with the irreducible ordered eight-point section incidence from section 1.

The good locus constructed above is a nonempty open of this irreducible incidence (and of the auxiliary projective bundle choosing Q1). Its projection to Gamma^8 is dominant and constructible, so it contains a nonempty open. Therefore a general ordered eight-tuple on Gamma admits the required pencil.

The independent-conditions fact follows inductively: as long as a nonzero section remains, its zero set on an integral curve is finite, so the next general point cuts the remaining section space by one. Thus no interpolation assumption about unrelated general points of P3 enters the proof.

## Status

This is a symbolic generic exclusion of the degree-five twist-three nondominant branch after combining with the separately established source-root dominance. It does not exclude the degree-four nondominant image or any dominant twist-three eigenquotient, and it is not a complete proof repair. No source coefficients, numerical ranks, or external writes were used.
