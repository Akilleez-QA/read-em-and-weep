# The beta parameter map cannot dominate P(U*)

## Scope and dependencies

Work over C. Let E be the HM rank-two bundle on P4 with determinant O(5), U=H0(E) of dimension four, and C the reduced union of 25 skew lines. Assume evaluation U⊗O→E has rank two off C, rank one on C, and its minors generate I_C. For every three-space B⊂U, let X_B be the rank-at-most-one degeneracy scheme of B⊗O→E. Use the independently established facts that X_B is pure of dimension two, locally Cohen–Macaulay, and degree 15. These are proved in BETA-DEGENERACY-SURFACE.md at 26240e70230aef0de1f1b8714a06bd644adeec69. The active-point quotient input is recorded in BETA-SPLIT-IMAGE-BOUNDARY.md at d755d22d3bf460fe314dd846bda1e893d682b71c.

Assume the residual beta branch supplies an algebraic family of integral nonplanar sextics D_H⊂H, arithmetic genus three, containing Z_H=C∩H, for H in a dense open of dual P4. Its beta assignment is a rational map f:H↦B_H∈Gr(3,U)=P(U*), and D_H⊂X_{B_H}. As usual shrink the hyperplane open so each H meets every component of C transversely in one point. No smoothness or Gorenstein assumption on D_H is made.

## 1. Rank-one points on C are smooth points of X_B

Suppose B evaluates with rank one at p∈C. Locally, a unit entry permits row and column operations putting its matrix in the form

[1 0 0; 0 a b].

Thus X_B is cut out by (a,b). Since it is codimension two in a smooth fourfold, this is a regular sequence. On X_B, the image A of B is a line subbundle of E, and Q=E/A is a line bundle. Choose a fourth section completing B to U. Its image q in Q generates the ideal of C inside X_B: the three extra minors reduce to q and its multiples after the same operations, and all six minors generate I_C.

Consequently O_{C,p}=O_{X_B,p}/(q). The ring O_{X_B,p} is Cohen–Macaulay of dimension two, and its quotient has dimension one, so q is a nonzerodivisor. The quotient is regular because p lies on one smooth component of the disjoint union C. Lifting a generator of its maximal ideal, together with q, generates the maximal ideal of O_{X_B,p}. Hence its embedding dimension is at most two, and it is regular. Therefore X_B is smooth at p.

In particular all active points Z_H are smooth points of X_{B_H}. Any non-Cartier obstruction for D_H on that surface is away from Z_H.

## 2. A general X_B is smooth everywhere

Set V=P4\C. Evaluation is surjective on V, so its dual embeds E* into U*⊗O_V and defines a morphism

g:P_V(E*)→P(U*).

Here P(E*) parametrizes one-dimensional subspaces of the fibers of E*. Its total space is a smooth fivefold. For [λ]∈P(U*) and B=ker λ, the fiber g^{-1}([λ]) is scheme-theoretically X_B∩V: factoring λ through E_x is equivalent to rank(B→E_x)≤1; that rank cannot be zero because ker(U→E_x) has dimension two. The factorization is unique projectively. This is also the usual incidence description by maximal minors, so the identification is scheme-theoretic, not just set-theoretic.

Every X_B has a point outside C, since its support has dimension two whereas C has dimension one. Thus g is dominant (indeed surjective on closed points). Its generic fiber is regular: its local rings are localizations of regular rings on the smooth total space. The function field of the characteristic-zero target is perfect, so the generic fiber is geometrically regular and smooth. The nonsmooth locus of this finite-type morphism is closed in its source; its image is constructible and misses the generic point of the irreducible target. A constructible subset missing the generic point cannot be dense. Removing its closure gives a dense target open over which every fiber is smooth. This argument does not require g to be proper.

On C, rank-one evaluation defines the regular map κ:C→P(U*) sending p to ker(U→E_p). Its image is closed of dimension at most one. If [B] is outside κ(C), B evaluates with rank one at every point of C. Section 1 then shows X_B is smooth along all of C. Intersecting this complement with the preceding open proves that X_B is a smooth projective surface for every B in a nonempty open W⊂P(U*).

## 3. Adjunction excludes moving sextics on smooth X_B

Fix B∈W. Everywhere on X=X_B there is an exact sequence

0→A→E|X→Q→0,

with A,Q line bundles, and K=ker(B⊗O_X→A) of rank two. The regular determinantal embedding has normal bundle Hom(K,Q). Thus, up to the harmless constant determinant line det B,

det N_{X/P4}=A⊗Q^2,
ω_X=O_X(-5)⊗A⊗Q^2=Q,

because A⊗Q=det E|X=O_X(5). The fourth section cuts out C scheme-theoretically, hence Q≅O_X(C).

Every integral curve D=D_H⊂X is Cartier because X is a smooth surface. This conclusion, rather than an assumption, also makes D Gorenstein; D need not be smooth. Since D⊂H and contains Z=C∩H, scheme-theoretically D∩C=Z, of length 25. Therefore deg Q|D=25. Adjunction gives

ω_D≅Q|D⊗O_D(D),
deg O_D(D)=(2p_a(D)−2)−25=4−25=−21.

A line bundle of negative degree on an integral proper curve has no nonzero section. Hence H0(N_{D/X})=H0(O_D(D))=0. The Hilbert scheme of curves on X has zero Zariski tangent space at D, so D cannot belong to a positive-dimensional algebraic family of distinct curves on X.

## 4. Dimension drop

If f:dual P4⇢P(U*) were dominant, a general B∈W would have a positive-dimensional fiber, of dimension 4−3=1. After taking an irreducible fiber component and shrinking to a flat family, its sextics D_H would be distinct: an integral nonplanar sextic in P3 spans its unique ambient hyperplane H. This would contradict Section 3 on the fixed smooth X_B.

Therefore f is not dominant, and dim closure(f(dual P4))≤2. More precisely, the general B in its image must have singular X_B; indeed any smooth X_B and any positive-dimensional family in its f-fiber produce the same contradiction. The constructed open W is disjoint from the image on the domain of definition: by the fiber dimension inequality, every nonempty fiber there has dimension at least one, and the same argument applies after selecting a positive-dimensional component.

## What remains

This eliminates the dominant three-dimensional beta-image alternative, not the entire beta branch. A surviving beta assignment has image dimension at most two and general fibers of dimension at least two, supported on exceptional singular degeneracy surfaces. Along any such D the rank-one surface locus is lci and ω_X|D=O_D(Z), but D need not be Cartier there. Section 1 places every possible non-Cartier point away from the 25 marked points. No smoothness, normality, or Cartier property on the remaining exceptional surfaces has been inferred.

This is a symbolic deduction. No source coefficients, selected matrices, numerical rank computations, scans, local-model spike, or one-shot experiment were used.
