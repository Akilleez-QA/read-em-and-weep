# A finite cubic base scheme forces exactly three cubics

## New conclusion

Let Z be any reduced length-25 subscheme of P3 over C. If its full cubic linear system has finite base scheme, then

    h0(I_Z(3))=3.

The complete intersection used in the proof need not be reduced, and its residual length-two scheme need not be disjoint from Z.

Applied to the generic HM section in the a=0 branch, this sharpens the existing b<=5 result: if b=4 or b=5, the reduced cubic base curve is nonempty and contains all 25 section points. It is not a proof that b<=3 in every case, nor a proof of the required product-trace transversality.

## 1. The complete-intersection trace pairing

Choose three general cubics f,g,h through Z. Finite base locus allows them to be chosen as a regular sequence: choose f nonzero; choose g avoiding its finitely many irreducible factors; then choose h avoiding all components of the resulting complete-intersection curve. Put X=V(f,g,h), a length-27 complete intersection.

The Koszul resolution, twisted by five, is

    0→O(-4)→3O(-1)→3O(2)→O(5)→O_X(5)→0.

Its successive connecting maps give the trace

    tr:H0(O_X(5))→H3(O(-4))=C.

In particular tr vanishes on the restrictions of all ambient quintic forms. Dualizing the same Koszul resolution identifies the dualizing sheaf of X with O_X(5); the displayed trace is its duality trace, up to a common nonzero scalar. Finite-scheme duality therefore makes multiplication followed by trace a perfect pairing

    H0(O_X(3)) × H0(O_X(2)) → C.

This use of duality includes nonreduced complete intersections. Equivalently, the local complete-intersection rings are Artinian Gorenstein, and the duality functional is nonzero on each local socle.

## 2. Residual duality without a disjointness assumption

Let J=I_Z/I_X, considered as an ideal sheaf in O_X. The exact sequence

    0→J→O_X→O_Z→0

gives length(J)=2. Define Y by the annihilator ideal Ann_(O_X)(J), equivalently by I_Y=I_X:I_Z.

For an Artinian Gorenstein algebra A with perfect multiplication functional lambda, the orthogonal complement of an ideal J is its annihilator. Indeed, if lambda(aJ)=0, then lambda(ajb)=0 for every b in A because jb lies in J; perfection forces aj=0 for every j. Consequently J pairs perfectly with A/Ann(J). Applying this on X shows that Y has length two and yields the perfect pairing

    H0(J(3)) × H0(O_Y(2)) → C.

This argument allows Y to overlap Z and allows X to have nilpotents along Z. No identification with two complementary reduced points is made.

Every length-two subscheme of projective space imposes independent conditions on quadrics. Here is a direct proof. After choosing a linear form nonzero on its support and dehomogenizing, two distinct points are separated by an affine linear function. At a double point, its algebra is C[epsilon]/(epsilon²); because it is a closed subscheme of affine space, some affine coordinate has nonzero epsilon coefficient. Thus constants and affine linear functions span its length-two algebra in either case. Homogenizing with the chosen nonvanishing linear form proves that ambient quadrics surject onto H0(O_Y(2)).

## 3. Every cubic through Z already vanishes on X

Take p in H0(I_Z(3)). Its restriction to X lies in H0(J(3)). For every ambient quadric q,

    tr((p|X)(q|X))=tr((pq)|X)=0,

because pq is an ambient quintic. By the preceding surjectivity, p|X pairs to zero with all of H0(O_Y(2)). Perfection forces p|X=0. Therefore

    H0(I_Z(3))=H0(I_X(3))=span(f,g,h),

which proves b=3.

This is the degree-three instance of the residual Cayley--Bacharach formula with index 3+3+3−4=5: the potential extra cubic quotient is dual to the failure of Y to impose independent conditions on quadrics. The proof above establishes this instance directly rather than assuming a formula for reduced complementary point sets.

## 4. Consequence in the generic HM no-quadric branch

Retain the premises and notation of NO-QUADRIC-CUBIC-BOUND.md: a=0, and b<=5 is already proved. Suppose b>=4.

First the cubic system has no common surface factor. Its maximal common factor g is canonical, of degree one or two (degree three would force b=1). Over the generic hyperplane function field, the subset of the 25 labels on V(g) is invariant under the semilinear normalizer action, so transitivity makes it empty or all. If all labels lie on g, a=0 is contradicted by a quadric equation, multiplying g by a linear form if necessary. If none do, dividing each cubic by g gives degree at most two equations through every point of Z, again contradicting a=0 (and, for linear quotients, spanning). Thus no fixed surface exists.

The preceding theorem excludes finite cubic base locus when b>=4. Let D be the reduced union of its curve components. The same canonical-label argument makes the subset Z∩D empty or all. If empty, two general cubics cut a degree-nine complete-intersection curve containing D; the reduced union R of its other components has degree at most eight and contains all 25 points. A third cubic can avoid all components of R, since they are not base curves, giving 25<=3 deg(R)<=24, impossible. Hence all Z lie on D.

A quintic generator combination avoiding the components of D gives deg D>=5, and I_D(2)=0. These are the exact geometric consequences needed for the existing curve-Hilbert bound. In particular both remaining values b=4 and b=5 require a canonical reduced nonplanar base curve containing the whole section. No such curve is asserted to exist or excluded.

## Inputs and scope

The algebraic theorem uses only the Koszul resolution and duality for a zero-dimensional complete intersection; its trace and annihilator argument are given explicitly. The HM consequence uses the already pinned generic normalizer transitivity, absence of section quadrics, and quintic sheaf generation from NO-QUADRIC-CUBIC-BOUND.md. It does not use an integral-curve uniform-position or lifting theorem.

No selected HM/source coefficients, planes, ranks, matrices, or experiments were used. No external action was taken.

A checked published formulation is Gold--Little--Schenck, “Cayley--Bacharach and evaluation codes on complete intersections,” arXiv:math/0311129v2, Theorem 1.2, PDF pages 3–4 (attributed there to Davis--Geramita--Orecchia): https://arxiv.org/pdf/math/0311129 . Its hypotheses allow mutually residual CLOSED SUBSCHEMES of a complete intersection, not only disjoint reduced point sets, and its index is sum(d_i)−m−1. Applied with m=3 and all d_i=3, it gives exactly h0(I_Z(3))−h0(I_X(3))=h1(I_Y(2)). The proof above supplies the needed instance independently.
