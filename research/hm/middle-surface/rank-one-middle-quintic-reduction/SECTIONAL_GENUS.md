# The invariant integral quintic has sectional arithmetic genus one

## Result and hypotheses

Work over C, as in PROOF.md and INDEPENDENT_AUDIT.md. Let Y be the nonempty integral degree-five surface obtained there. Its H5 action is the restriction of the standard irreducible five-dimensional representation on P4. Import only the already proved Hilbert congruence g = 1 modulo 5, where

    P_Y(t) = 5 binom(t,2) + (6-g)t + chi(O_Y).

Then g=1. No normality, smoothness, arithmetic Cohen–Macaulayness, or value of chi(O_Y) is required or concluded.

The proof below establishes all needed properties of a general hyperplane section even when Y is singular and not Cohen–Macaulay. It gives an elementary bound 0 <= g <= 5, sufficient for the congruence, so the main conclusion does not depend on a delicate version of Castelnuovo's theorem. A verified published statement of the sharper arithmetic bound g <= 2 is also recorded.

## 1. Y is nondegenerate

The vector-space span of the affine cone over Y is a nonzero H5-invariant linear subspace of the standard five-dimensional representation. Irreducibility forces this span to be the entire representation. Thus Y lies in no hyperplane of P4.

One can check the requisite irreducibility directly: in the standard Schrödinger basis, one generator is diagonal with five distinct eigenvalues and a second cyclically permutes the five eigenspaces. A subspace invariant under both is a sum of eigenspaces stable under this transitive cycle, hence is zero or the whole space.

## 2. A general scheme-theoretic hyperplane section is integral

Let C=Y intersect H as a scheme. We must address embedded points, since mere set-theoretic Bertini irreducibility would not suffice.

First, the non-Cohen–Macaulay locus of Y is a finite set. Indeed, Cohen–Macaulayness is open for schemes of finite type over a field. At every point of codimension at most one, the local ring of the integral surface Y is either a field or a one-dimensional local domain. The latter has depth one and is Cohen–Macaulay. Thus the closed non-Cohen–Macaulay locus has no point of codimension zero or one; on the Noetherian surface Y it is a finite set of closed points.

Choose H avoiding this finite set. Since Y is integral and H does not contain Y, its equation is a nonzerodivisor on O_Y. At every point of C, quotienting the Cohen–Macaulay local ring O_Y by that nonzerodivisor gives a Cohen–Macaulay local ring of C. Thus C is a Cohen–Macaulay pure one-dimensional scheme, in particular it has no embedded associated points.

Bertini irreducibility gives that C is irreducible for general H. A precise reference, valid without smoothness of Y, is the Stacks Project, Lemma 37.32.3:

https://stacks.math.columbia.edu/tag/0G4C

To check its hypotheses in this case, take the full hyperplane system restricted to Y. It is basepoint free. Two general members intersect in a nonempty zero-dimensional scheme (degree five), so an irreducible component of that intersection has codimension two. A third hyperplane can avoid any selected point of that intersection. These give conditions (3) and (4) of the lemma; Y is geometrically irreducible over C.

Finally, C is generically reduced. The regular locus U of Y is smooth over C. Smooth Bertini applied to its hyperplane embedding says that C intersect U is smooth for general H (Stacks Project, Lemma 33.47.3):

https://stacks.math.columbia.edu/tag/0FD4

The complement Y minus U has dimension at most one. Choose H not containing any of its one-dimensional components; its intersection with H then has dimension at most zero. Hence the irreducible curve C has generic point in U, and is generically smooth, hence generically reduced. A Noetherian scheme that is generically reduced and has no embedded associated points is reduced. Therefore C is integral.

All the preceding conditions hold on nonempty open subsets of the dual projective space, so they can be imposed simultaneously. Nothing here says that C avoids the whole singular locus of Y, or that C itself is everywhere smooth.

## 3. The section is a nondegenerate quintic in H=P3

Its degree is five by the hyperplane-section exact sequence and the leading coefficient of the Hilbert polynomial.

For completeness, nondegeneracy of Y alone is not to be substituted for a proof of nondegeneracy of the scheme C. Here is that proof. Write h for the equation of H. The exact sequence on Y is

    0 -> O_Y --h--> O_Y(1) -> O_C(1) -> 0.

Because Y is integral and projective over C, H^0(Y,O_Y)=C. If an ambient linear form ell vanishes on C, exactness on global sections gives ell|_Y = a h|_Y for some scalar a. Then ell-a h vanishes on Y. Section 1 implies ell=a h as ambient linear forms. Consequently the only ambient linear forms vanishing on C are multiples of h. Equivalently, C is contained in no plane of H=P3.

In particular h^0(C,O_C(1)) >= 4. Integrality and projectivity give h^0(C,O_C)=1, and therefore

    p_a(C) = 1-chi(O_C) = h^1(C,O_C) >= 0.

The hyperplane sequence also gives P_C(t)=P_Y(t)-P_Y(t-1)=5t+1-g, so this arithmetic genus is exactly the integer g in the imported congruence, not the geometric genus of a normalization.

## 4. An elementary sufficient arithmetic genus bound: p_a(C)<=5

This argument applies to every integral nondegenerate degree-five curve C in P3, with arbitrary singularities.

Choose any point p in P3 outside C and project from p to P2. Restriction defines a morphism

    f:C -> D subset P2,

where D is the reduced scheme-theoretic image and is integral. The map is finite: a fiber lies on a line through p; a positive-dimensional fiber would force the integral curve C to be that line, contradicting nondegeneracy. Thus f is proper and quasi-finite, hence finite.

The projection is given by three linear forms without common zero on C, so

    f^*O_D(1) = O_C(1).

The degree formula yields

    5 = deg(C) = [C(C):C(D)] deg(D).

The plane curve D cannot be a line, because its inverse image would be a plane of P3 containing C. Since five is prime, necessarily deg(D)=5 and [C(C):C(D)]=1. Thus f is finite birational. This step needs no general-projection or secant-line theorem.

There is an exact sequence

    0 -> O_D -> f_*O_C -> Q -> 0,

where Q has finite length q>=0. The plane quintic has arithmetic genus six, including when singular. For example this follows directly from 0 -> O_P2(-5) -> O_P2 -> O_D -> 0. Because f is finite, taking Euler characteristics yields

    p_a(C) = p_a(D)-q = 6-q.

If q=0, then f_*O_C=O_D, and a finite morphism is the relative spectrum of its direct-image algebra. Hence f would be an isomorphism. Its polarization would identify O_C(1) with O_D(1). But

    h^0(D,O_D(1))=3,

as follows by twisting the plane-quintic ideal sequence by one and using H^1(P2,O_P2(-4))=0. This contradicts h^0(C,O_C(1))>=4. Therefore q>=1 and p_a(C)<=5.

Together with Section 3, this proves 0<=g<=5 using only elementary projective geometry, local algebra, and cohomology.

## 5. The sharp Castelnuovo bound, with verified reference

The stronger standard statement for an integral nondegenerate degree-d curve in P^r concerns its arithmetic genus:

    p_a(C) <= (r-1)m(m-1)/2 + m epsilon,
    d-1 = m(r-1)+epsilon, 0<=epsilon<r-1.

For d=5 and r=3, one has m=2 and epsilon=0, giving p_a(C)<=2.

A checked published source explicitly using arithmetic genus and displaying this formula is Kyunghye Cho, Changho Keem, and Seongsuk Park, "On the Hilbert scheme of trigonal curves and nearly extremal curves," Kyushu Journal of Mathematics 55 (2001), 1–12, Section 3, the discussion immediately before Proposition 3.6. It states the arithmetic-genus bound before displaying pi_0(d,r), and the adjacent proposition explicitly covers irreducible reduced nondegenerate curves. Article metadata and the formula were verified from the publisher's page and indexed PDF text:

https://doi.org/10.2206/kyushujm.55.1
https://www.jstage.jst.go.jp/article/kyushujm/55/1/55_1_1/_pdf

This paper cites Harris's Curves in Projective Space for the surrounding Castelnuovo theory. Independently, the introduction to the research article "Genus bound of curves on surfaces of almost minimal degree," Journal of Pure and Applied Algebra 229 (2025), 107891, explicitly formulates Castelnuovo's bound for a projective integral curve and its arithmetic genus, and states the general-hyperplane Hilbert-function inequality underlying it:

https://doi.org/10.1016/j.jpaa.2025.107891

The sharper bound is supplementary: the proof of g=1 in this file is already complete without using it, so no confusion between geometric and arithmetic genus in a textbook formulation can affect the conclusion.

## 6. Conclusion and precise scope

The previously established H5 congruence is g=1 modulo5. The elementary interval 0<=g<=5 contains only one integer with this residue, namely one. Hence

    g=1,
    P_Y(t)=5 binom(t,2)+5t+chi(O_Y)
          =(5/2)t(t+1)+chi(O_Y),
    chi(O_Y) is divisible by five.

This strengthens conclusion (5) of PROOF.md from a congruence to an exact sectional arithmetic genus. It does not identify chi(O_Y), impose normality or smoothness, identify Y with an elliptic scroll, or exclude the integral quintic. Any subsequent classification/exclusion must independently justify such additional claims.
