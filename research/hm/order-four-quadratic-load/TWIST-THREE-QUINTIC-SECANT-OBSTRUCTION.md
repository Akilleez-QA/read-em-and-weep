# A secant and elliptic-pencil obstruction to the degree-five image

Continue TWIST-THREE-VERTICAL-CLASSIFICATION.md. The only degree-five nondominant image D is an integral quintic in P3 having multiplicity at least three at eight distinct points p_1,...,p_8 on the actual smooth rational sextic Gamma. Distinctness holds on the general-quadric open established there. The parameter curve is the actual kappa image, proved in KAPPA-RATIONAL-SEXTIC.md, published at 3edb50b13b8a5ce876f52a2085ecc8d16b3181c0. No generic-position claim about these eight points is made here.

## 1. Every secant is contained in D

For any two of the eight points, restrict the degree-five defining polynomial of D to their joining line. If the restriction is nonzero, its vanishing orders at the two distinct points total at least six, exceeding its degree. Hence the joining line lies in D. If no three points are collinear, these give twenty-eight distinct lines; the assertion of containment itself does not require that hypothesis.

In particular, no four of the eight points can be coplanar with no three collinear: their six joining lines would all lie in the restriction of D to that plane. An integral quintic cannot contain the plane, and a nonzero plane quintic cannot contain six distinct lines. This is a necessary condition, not a claim that the actual eight points violate it.

## 2. Integral elliptic pencils smooth at the marks are impossible

The following exact criterion is independent of the source of the eight points.

Lemma. Let eight distinct noncoplanar points in P3 lie on a smooth quadric Q0 and on a second quadric Q1 such that C=Q0 intersect Q1 is an integral arithmetic-genus-one quartic smooth at the eight marked points. Then no integral quintic surface is triple at all eight points.

Proof. An integral quintic D cannot contain Q0, so its restriction to Q0 is a nonzero effective Cartier divisor of class (5,5). At every marked point its multiplicity is at least three. The curve C has class (2,2) and is smooth at those points. If C were not a component of D|Q0, its intersection number would be twenty, but the eight local intersections would contribute at least twenty-four. Thus C is a component.

Subtract C. The residual effective divisor has class (3,3) and multiplicity at least two at the eight points. If C were not again a component, its intersection number with C would be twelve, while the marked points contribute at least sixteen. Therefore C occurs a second time.

The final residual effective divisor has class (1,1) and passes through all eight points. Every (1,1) divisor on a smooth quadric is a hyperplane section, contradicting noncoplanarity. This proves the lemma.

Consequently the eight actual points of a surviving degree-five image cannot admit such an integral elliptic pencil smooth at the marks. Since eight points always lie on at least two independent quadrics, this forces a special degeneracy of their quadric system: no chosen smooth member and second member may cut an integral elliptic quartic smooth at the eight marks. This criterion alone is not an exclusion.

## 3. Dependency needed to apply the criterion

To apply this criterion one must prove that the eight actual kappa-images selected by a general source quadric admit the pencil in the lemma (or to classify and exclude the alternative degenerate pencils). It is not legitimate to replace this by eight general points of P3, or even by eight independently general points of Gamma, without proving the required dominance or avoidance for the source-quadric parameter map. The source quadrics couple the fifty roots on the twenty-five C-lines. The earlier proof of pairwise distinct kappa-images establishes only distinctness, not this stronger pencil condition.

No selected source coefficients, matrix ranks, numerical experiments, or external writes were used.

The companion GENERAL-EIGHT-SEXTIC-POINTS-ELLIPTIC-PENCIL.md proves the needed nonempty open on Gamma^8, and EIGHT-ROOT-POSITION-DOMINANCE.md at c8805e9e18bdf6de9170cefdb2f900fe5caf4f60 transfers it to every eight-mark choice of a general source quadric. Together they close the degree-five nondominant twist-three branch. Global smoothness of the elliptic quartic is not required.
