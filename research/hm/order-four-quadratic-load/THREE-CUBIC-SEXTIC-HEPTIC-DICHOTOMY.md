# Three cubics with a curve base: integral sextic or a marked ACM heptic

## Scope and conclusion

Assume the generic HM hyperplane section Z⊂H=P3 consists of 25 reduced spanning points, no three collinear, with a=h0(I_Z(2))=0 and b=h0(I_Z(3))=3. Assume its full cubic base has a positive-dimensional component. Retain the established normalizer transitivity on the 25 labels, quintic sheaf generation with finite base exactly Z, and the reusable degree-five constant-Plücker family exclusion.

Then there is a unique integral component D of the reduced cubic curve base containing all 25 points. The marked points are smooth on that reduced curve base. The degree of D is either six or seven.

In the degree-seven alternative the entire cubic base scheme is D, and D is ACM of arithmetic genus five with minimal resolution

0→O_P3(−4)⊕O_P3(−5)→3O_P3(−3)→I_D→0.

Equivalently its three cubics are the maximal minors of a 3-by-2 matrix whose columns have degrees one and two. The three entries of the linear column are independent; their common zero is a canonical point P∈D, and P lies outside Z generically.

The integral degree-six alternative is not excluded here and is not identified with the already excluded genus-three four-cubic sextic. In particular its genus and Plücker span cannot be imported from that different branch.

## 1. No fixed surface, and all labels lie on the reduced curve base

Let V=H0(I_Z(3)), of dimension three. A maximal common factor of its cubics would have degree one or two: degree three would make V one-dimensional. The factor is canonical. The subset of marked labels on it is invariant over the generic hyperplane parameter field and hence empty or all. If all, a=0 is contradicted. If none, dividing all cubics by the factor gives equations of degree at most two through Z, again contradicting a=0. Thus there is no fixed surface.

Choose two general cubics F,G∈V with no common factor; Y=V(F,G) is a degree-nine complete-intersection curve. Let B_red be the reduced union of the positive-dimensional components of the full cubic base. It is nonempty by hypothesis, and deg B_red≤9. Canonical label transitivity makes Z∩B_red empty or all. If empty, the reduced union R of the remaining components of Y has degree at most eight and contains Z. A third cubic in V can avoid every component of R, because none is a base component. Its proper intersection with R then gives 25≤3deg R≤24, a contradiction. Hence Z⊂B_red.

This argument is the positive-dimensional case of FINITE-CUBIC-BASE-RIGIDITY.md, and does not assert that all b=3 systems have a curve base.

## 2. The marked points lie on one integral component

The singular locus of B_red is finite and canonical. A quintic generator combination can avoid every component of B_red and has intersection length 5deg B_red≤45. At a singular point of a reduced curve, a nonzerodivisor quotient has length at least two; length one would make the maximal ideal principal and the one-dimensional local ring regular. If all 25 labels were singular they would contribute at least50, impossible. Transitivity therefore implies that no marked point is singular on B_red.

In particular each marked point belongs to exactly one irreducible component. The nonempty marked subsets on components form a canonical partition. Transitivity makes its blocks equal in size, so their number divides25. There are at most nine components, leaving one or five marked components. Five components would each contain five points; none could be a line, by no-three-collinear. Their total degree would then be at least ten, impossible. Hence one integral component D contains all Z.

Intersecting D with a proper quintic gives deg D≥5. The degree-five case is excluded by the pinned reusable constant-Plücker family theorem: the quintic cut has length25 and equals Z, so all six minors restrict proportionally; D is the canonical integral marked component and spans H, exactly as required by that theorem. Thus 6≤deg D≤9.

Since D is a base component and contains Z, its cubic space equals V:

H0(I_D(3))=H0(I_Z(3)), of dimension three.

## 3. Residual duality excludes degree eight and nine

The integral curve D is locally Cohen–Macaulay. Link it in the complete intersection Y=V(F,G) of type (3,3), and let R be the residual closed curve defined by I_R=I_Y:I_D. Complete-intersection linkage makes R locally Cohen–Macaulay, with degree 9−deg D. Residual duality gives

I_D/I_Y≅ω_R(−2),

because ω_Y=O_Y(2). Since H1(I_Y(3))=0 and h0(I_Y(3))=2, twisting and taking sections yields

3=2+h0(ω_R(1)).

Equivalently, by duality on the possibly nonreduced locally CM curve R,

h1(O_R(−1))=1.                      (*)

If deg D=9, Y and D have equal degree; Y has generic multiplicity one along D and no other components, and its CM property forbids embedded components. Thus Y=D as schemes and h0(I_D(3))=2, a contradiction.

If deg D=8, R is a degree-one locally CM curve, hence a reduced line. But h1(O_R(−1))=h1(O_P1(−1))=0, contradicting (*). Therefore deg D is six or seven.

## 4. In degree seven the residual degree-two curve is planar

Suppose deg D=7. Then R is a pure locally CM degree-two curve satisfying (*). We check every possible support, including negative-genus double lines.

If R is reduced and irreducible, it is a plane conic. If it is the reduced union of two lines, intersecting lines form a plane conic, whereas skew lines give h1(O_R(−1))=0. A generically reduced locally CM curve has no embedded associated points, so there are no additional zero-dimensional decorations in these cases.

The remaining possibility is a double structure on a line L. Write J=I_L/I_R. The square of the line ideal vanishes on R generically; its image in O_R would otherwise be a zero-dimensional submodule, forbidden by local CM. Thus I_L²⊂I_R and J²=0. The sheaf J is a rank-one torsion-free module on the smooth line, hence J≅O_L(c) for an integer c. The surjection

I_L/I_L²≅2O_L(−1)→J≅O_L(c)

forces c≥−1. If c≥0, the exact sequence

0→O_L(c−1)→O_R(−1)→O_L(−1)→0

has vanishing H1 on both line terms, contradicting (*). If c=−1, the conormal quotient is given by two constants; a nonzero constant linear combination of the two linear equations of L belongs to I_R. Thus R is contained in a plane, where its pure degree-two scheme is a plane conic (possibly a double line).

Consequently R is always a plane conic. This is why negative-genus nonplanar double lines cannot be silently retained or discarded: their H1(O_R(−1)) is zero, and (*) specifically rules them out.

## 5. Explicit heptic normal form

Write I_R=(ℓ,q), where deg ℓ=1 and deg q=2. The two cubics can be written

F=ℓa+qb,    G=ℓc+qd,

with a,c quadratic and b,d linear. The residual ideal of R in (F,G) is

I_D=(F,G,ad−bc).

This is the usual complete-intersection residual computation, or follows directly from its Hilbert–Burch matrix. The displayed generators have the linear syzygy (d,−b,−ℓ) and the quadratic syzygy (c,−a,q). Their maximal minors recover the three cubics, and height two gives the exact minimal resolution

0→O(−4)⊕O(−5)→3O(−3)→I_D→0.

Its Hilbert numerator is 1−3t³+t⁴+t⁵, with h-vector (1,2,3,1). Hence deg D=7 and p_a(D)=5. In particular the three cubics generate the whole saturated ideal, so their base scheme is precisely D, with no additional curve or isolated base component.

There is exactly one linear syzygy, up to a scalar. Its three coefficients must be independent: otherwise their common zero contains a line, on which all maximal minors vanish. This would put a line in the integral degree-seven D, impossible. Thus their common zero is a unique point P, and the minors show P∈D. Both the syzygy line and P are intrinsic to the full cubic system. The subset of labels equal to P is therefore normalizer-invariant; it cannot be all25 distinct labels, so it is empty generically.

## Inputs and unresolved boundary

Read current PR1 handoffs 6312850973, 6312941584, and 6312966358 before this deduction. Source proof used: FOUR-CUBIC-SEXTIC-BASE.md at fd58cd7d25b213841fce0c34e5207bc84e62c42f, whose component argument is extended here to total curve degree nine, rather than importing its degree-six/genus-three conclusion. The degree-five family exclusion is EXCLUDE-FIVE-CUBIC-ENDPOINT.md at c159a09d691605f3254d4d01eca07e042647e6d0. Complete-intersection residual duality is applied to closed CM curves, not assumed disjoint or reduced residual supports.

The degree-six carrier may coexist with additional unmarked cubic-base components and has not been assigned a genus here. The heptic normal form is a necessary configuration, not its exclusion. No source coefficients, selected ranks, scans, one-shot experiments, or external writes were used.
