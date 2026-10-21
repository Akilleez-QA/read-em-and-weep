# No integral quartic is double at ten general points of Gamma

## Statement and source-pattern boundary

For the actual smooth rational sextic Gamma in P3, an integral quartic cannot have multiplicity at least two at ten independently general points of Gamma. Thus this excludes all degree-four primitive twist-three nondominant images whose ten-source-root pattern dominates Gamma^10. It does NOT by itself exclude the thirty exceptional patterns taking both marks on each of the five C-lines in a configuration hyperplane; their root-position images have dimension nine, and require a separate argument. See TEN-ROOT-POSITION-DOMINANCE.md for that independent distinction.

## 1. Eight double points leave at most four quartics

Take eight general points Z8 on Gamma. By GENERAL-EIGHT-SEXTIC-POINTS-ELLIPTIC-PENCIL.md (published dd6ffc10117710404a042fd5e08730aa3f543bd1), their quadrics generate a pencil with integral complete-intersection curve C of arithmetic genus one, smooth at Z8. Eight general points impose eight independent quadric conditions. Let A=O_C(2)(-Z8), a degree-zero invertible sheaf. It is nontrivial: otherwise an additional quadric restriction would vanish at the eight points, contrary to the pencil dimension.

Let V8 be the vector space of ambient quartics double at Z8. Restriction to C maps V8 into H0(C,A^2), of dimension at most one. Its kernel consists of quartics containing C. For such a quartic, the conormal class is a pair of O_C(2) sections vanishing at Z8, hence is zero because H0(A)=0. Therefore the kernel is H0(I_C^2(4)). The complete-intersection-square resolution

    0 -> O(-6)^2 -> O(-4)^3 -> I_C^2 -> 0

gives its dimension three. Consequently dim V8<=4, including the case where A is nontrivial two-torsion. No torsion-avoidance assertion is needed.

## 2. Two general double-point conditions kill its restriction to Gamma

Lemma. If W is a vector space of rational functions on P1 of dimension at most four, evaluation of value and first derivative at two independently general distinct points is injective.

To prove this, extend W if necessary to a four-dimensional rational-function space and work on an affine open avoiding poles. Linearly independent rational functions in characteristic zero have a nonzero Wronskian. Choose a point where the order-zero through order-three jet matrix is invertible. As the second evaluation point approaches the first, the determinant of the two value/derivative evaluation blocks has leading coefficient a nonzero scalar multiple of that Wronskian. Thus it is not identically zero as a function of the pair. This proves the lemma; for line-bundle sections choose a local rational trivialization.

Apply it to the restriction image of V8 in H0(Gamma,O_Gamma(4)), whose dimension is at most four. If the ninth and tenth points are independently general, a quartic double at all ten has restriction zero on Gamma. Hence it lies in H0(I_Gamma(4)). This condition holds on a nonempty open of Gamma^10.

## 3. Quartic normality and the fixed conormal image

The exact primary source used here is L. Gruson, R. Lazarsfeld and C. Peskine, On a Theorem of Castelnuovo, and the Equations Defining Space Curves, Inventiones Mathematicae 72 (1983), 491-506. Theorem (i) on printed page 492 says the restriction-surjectivity property (B_n), defined on printed page 491, holds for n>=d+1-r for a reduced irreducible nondegenerate curve of degree d in P^r. These two pages were visually checked in the author-hosted original:

https://commack.math.stonybrook.edu/robert.lazarsfeld/Reprints/Gruson.Laz.Peskine.Castelnouvu.Bound.pdf

For d=6 and r=3 this gives quartic restriction surjectivity. Since Gamma is P1 with O_Gamma(4)=O_P1(24),

    h0(I_Gamma(4))=35-25=10.

Map this ten-dimensional space to H0(Gamma,(I_Gamma/I_Gamma^2)(4)), and denote its image by N. Evaluation on ten independently general points of Gamma is injective on N. Indeed for any finite-dimensional space of sections of a vector bundle on an integral curve, a next general point lowers the dimension of the remaining nonzero section space by at least one. A nonzero section cannot vanish at the generic point. Induction proves the assertion in at most dim N<=10 steps.

Intersect this nonempty open condition with the open condition of section 2. A quartic double at the resulting ten points first contains Gamma, and its conormal section vanishes at the ten points, hence vanishes identically. Thus it is double along the entire Gamma.

## 4. An integral quartic cannot be double along a sextic

Suppose an integral quartic surface were double along Gamma. A general plane cuts the surface in an integral plane quartic by Bertini irreducibility and meets Gamma transversely in six distinct points. The plane quartic is singular at all six points, since its defining equation has multiplicity at least two there. Each singularity of an integral plane curve contributes at least one to the normalization genus defect. But a plane quartic has arithmetic genus three, so it cannot have six distinct singular points. This is a contradiction.

Therefore an integral quartic double at ten independently general points of Gamma does not exist.

## Optional strengthening using quadric-freeness

SEXTIC-QUADRIC-FREENESS-AND-TORSION-GATE.md proves Gamma lies on no quadric. This implies no nonzero quartic, even reducible or nonreduced, can be double along Gamma. In a factorization of a quartic, an irreducible factor containing Gamma has degree at least three. Hence there cannot be two such factors or a repeated such factor. All remaining factors are nonzero at the generic point of Gamma, so double vanishing would require the unique degree-three or degree-four integral factor to be singular along Gamma. A general plane section of that factor has arithmetic genus at most three, again contradicting the six marked singularities. Thus H0(I_Gamma^2(4))=0, and in fact the general-ten double-point quartic vector space is zero.

## Limits

The proof uses no Alexander-Hirschowitz assumption for general points of P3, no numerical ranks, and no selected source coefficients. It avoids the unresolved two-torsion avoidance problem entirely. The thirty codimension-one root-pattern families remain outside this generic-tuple conclusion until separately treated.
