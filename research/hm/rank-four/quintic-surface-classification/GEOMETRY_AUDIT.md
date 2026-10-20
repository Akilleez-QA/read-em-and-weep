# Audit: ruled reduction and exclusion of the elliptic ruled case

## Verdict

The proposed geometric reduction is valid over C, including for a singular, nonnormal integral surface. The elliptic ruled case is impossible for the stipulated faithful projective group G = A semidirect SL_2(F_5), with A = (C_5)^2 and its standard two-dimensional F_5 action. No classification of degree-five embedded surfaces is needed.

Two details should be explicit: the smoothness theorem on the resolution is the characteristic-zero basepoint-free version of Bertini, and a general hyperplane must avoid the finitely many images of contracted curves. Faithfulness on the surface also deserves the short justification below.

This audit imports the proved statement that the general scheme-theoretic hyperplane section D of Y is integral and has arithmetic genus one, from SECTIONAL_GENUS.md. It does not replace that proof or audit the separate rational-surface obstruction.

## 1. Resolution and the general pulled-back section

Let pi:S -> Y be a projective resolution, factoring through the normalization. Put L = pi^*O_Y(1). The five-dimensional ambient hyperplane system is basepoint free on S, even if it is not the complete system |L|. The bundle L is nef, L^2 = deg(Y) = 5, and L is big (its given sections define a birational morphism onto a surface).

There are only finitely many curves contracted by pi, and their images form a finite set Z. Indeed, the normalization is finite; the exceptional locus of a surface resolution has finitely many irreducible curves, and any curve contracted by the composite is among these. Choose a general hyperplane H avoiding Z. Then pi has finite fibers over D = Y intersect H: a positive-dimensional fiber would contain a contracted curve. Consequently pi^{-1}(D) -> D is proper and quasi-finite, hence finite.

A general member C = pi^{-1}(D) of the pulled-back ambient hyperplane system is smooth. One can prove precisely the needed Bertini assertion without assuming the morphism S -> P^4 is an immersion. Consider

    I = {(s,H): pi(s) lies in H} subset S x (P^4)^*.

The projection I -> S is a P^3-bundle, so I is smooth and integral. The other projection is proper and dominant. Its generic fiber is regular: its local rings are localizations of regular local rings of I. Its field of definition C((P^4)^*) has characteristic zero, hence is perfect, so this regular finite-type generic fiber is smooth. Openness of the smooth locus and properness show that all fibers over a nonempty open subset of the dual projective space are smooth. These fibers are exactly C.

For the regular-over-perfect-field implication, see Stacks Project, Section 33.25, especially Lemma 33.25.3:
https://stacks.math.columbia.edu/tag/04QM

This proof avoids accidentally applying the immersion-specific Bertini lemma to the resolution map. The hyperplane-integrality input on Y is separately proved in the imported artifact.

The divisor C is nonempty and purely one-dimensional. Since C -> D is finite, every irreducible component of C dominates D. The generic point of D lies in the dense open set over which pi is an isomorphism; choose H generally so that D is not contained in its complement. Therefore C has exactly one component and maps birationally to D. Smoothness implies that C is reduced, so C is a smooth integral projective curve. In fact C is the normalization of D.

The exact sequence

    0 -> O_D -> (pi|C)_*O_C -> Q -> 0

has Q of finite length. Euler characteristics give

    g(C) = p_a(D) - length(Q) <= 1.

Thus g(C) is zero or one. Nonnormality of Y creates no problem; it is not asserted that D itself is smooth or that pi is an isomorphism along D.

## 2. Negative canonical intersection and ruledness

Adjunction on the smooth surface S gives

    K_S.L = 2g(C) - 2 - L^2 = 2g(C) - 7,

so this number is either -7 or -5. If any positive multiple mK_S were effective, nefness of L would imply mK_S.L >= 0. Therefore all positive plurigenera vanish and kappa(S) = -infinity.

The required classification input is only the classical ruledness criterion: a smooth projective complex surface of Kodaira dimension minus infinity is birationally ruled. A primary source for the underlying criterion is Bombieri–Mumford, “Enriques' Classification of Surfaces in Char. p, II,” Introduction and Preliminary Reductions, first page: for a smooth complete minimal surface over a field of any characteristic, existence of a curve of negative canonical intersection is equivalent to ruledness. The paper explicitly recalls this result from Mumford's Part I.
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1976d--EnrClass-II-NC.pdf

It also yields the conclusion directly here. Contract (-1)-curves to a smooth minimal model q:S -> S_0. Write K_S = q^*K_{S_0} + E with E effective exceptional. Nefness of L gives

    K_{S_0}.q_*C = K_S.L - E.L < 0.

A general C is not q-exceptional; hence q_*C is an effective nonzero curve and S_0 has a curve of negative canonical intersection. The cited minimal-surface criterion makes S_0 ruled. This is an alternative to invoking the whole Enriques–Kodaira classification.

The earlier original source is D. Mumford, “Enriques' classification of surfaces in char. p: I,” Global Analysis (1969), pp. 325–339:
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1969b--EnrClass-I-NC.pdf

## 3. The ruling base has genus at most one

Write S birational to B x P^1, with B smooth projective. Resolve this birational map by further blowing up S, giving a smooth T with a morphism f:T -> B and a birational morphism T -> S. Replace L by its pullback and choose its general section C after doing so. The previous argument remains valid; a general C avoids the finitely many blowup centers, and its genus and self-intersection do not change.

For a general fiber F of f, the birational morphism T -> Y is nonconstant on F: its isomorphism locus is dense in T and meets a general fiber. Thus L.F > 0. The integral curve C in |L| is consequently horizontal, and f|C:C -> B is a nonconstant, hence finite, morphism. In characteristic zero it is separable. Hurwitz gives

    2g(C)-2 = deg(C/B)(2g(B)-2) + ramification_degree.

Since g(C)<=1, this forces g(B)<=1. Therefore Y is rational or birationally ruled over an elliptic curve.

## 4. Faithfulness survives passage to birational models

A projective linear transformation that fixes Y pointwise must be the identity on P^4. To see this, choose a matrix representative. Every point of Y lies in the projectivization of an eigenspace. There are finitely many eigenspaces; integrality forces Y into one of their projectivizations. Nondegeneracy makes that eigenspace the whole ambient vector space, so the matrix is scalar.

Thus the stipulated faithful projective action of G restricts faithfully to Y. It acts faithfully on C(Y), and hence by birational transformations on any birational model. No equivariant choice of resolution or minimal model is necessary for the following argument.

## 5. The elliptic ruling is preserved by every birational transformation

Suppose C(Y) = C(E)(t) with E a smooth genus-one curve. Any birational transformation of E x P^1 induces an automorphism of E. Indeed, compose it with projection to E. Restriction to a general P^1 fiber is a rational map P^1 -> E; it extends to a morphism and must be constant by Hurwitz. Therefore the composite factors rationally through E. Applying the same reasoning to the inverse proves that the resulting rational map E -> E is birational, hence an automorphism of the smooth projective curve E.

This construction is compatible with composition and gives a homomorphism

    G -> Aut(E).

It is the canonical ruling/Albanese action, but the preceding argument proves the needed invariance directly and avoids assumptions about a selected resolution carrying regular G-actions.

## 6. The base action is trivial

Over C, Aut(E) = E(C) semidirect Aut(E,0), with Aut(E,0) cyclic of order 2, 4, or 6. Hence Aut(E) is solvable (indeed metabelian). Verified source: J. S. Milne, Elliptic Curves, Chapter IV, Proposition 7.13 and Remark 7.18, printed pages 139–141:
https://www.jmilne.org/math/Books/ectext6.pdf

The group G itself is perfect. Here is a direct check, avoiding a group-table citation. In SL_2(F_5), let u(t) be the upper unipotent matrix with upper-right entry t and let d = diag(2,3). Then

    d u(t) d^{-1} = u(4t),   [d,u(t)] = u(3t).

Thus every upper unipotent lies in the commutator subgroup. The same argument applies to lower unipotents; upper and lower unipotents generate SL_2(F_5) by elementary row operations. Therefore SL_2(F_5) is perfect. Furthermore, the element -I acts on A by -1, so

    [(-I),a] = -2a

in the additive group A. Multiplication by -2 is invertible on A, proving [SL_2(F_5),A]=A. These statements imply [G,G]=G.

Any homomorphic image of a perfect group is perfect, while a solvable perfect group is trivial. Consequently G acts trivially on E.

One can equivalently first kill SL_2(F_5) on the base and then use its commutators with A. There is no need to appeal separately to irreducibility of A or to a kernel argument.

## 7. Contradiction on the generic rational fiber

Triviality on E makes the faithful action of G an injection into

    Aut_{C(E)} C(E)(t) = PGL_2(C(E)).

In particular A=(C_5)^2 would inject. Extension of scalars embeds this PGL_2 into PGL_2 of the algebraic closure of C(E). An element of order five there is conjugate to t -> zeta t with zeta a primitive fifth root. Its two fixed points are 0 and infinity. Every commuting element preserves this pair; interchanging them would conjugate the order-five element to its inverse, which is different. Thus its centralizer preserves each fixed point and consists of t -> c t. The subgroup of these transformations of exponent five has order at most five. It cannot contain (C_5)^2.

This contradicts faithfulness. The elliptic ruled case is excluded.

## Scope of the conclusion

Under the stated group, integrality, nondegeneracy, degree, and sectional-genus hypotheses, the only remaining birational possibility is rational. Excluding that case requires the separate finite-subgroup-of-Cremona argument. The present audit establishes all geometry and the elliptic exclusion independently, without assuming Y normal, smooth, an elliptic scroll, or arithmetically Cohen–Macaulay.

## Review of the assembled PROOF.md

The version read on 2026-10-19 at approximately 16:05 UTC passes the geometry and elliptic-ruled audit. Its Section 2 is justified by Sections 1–3 above; its Section 4 is justified by Sections 5–7 above. Its first section correctly proves faithfulness of the restricted action. Its opening and boundary statements now correctly identify the sectional-genus result as separately proved and independently audited, rather than an unproved input. The finite-subgroup theorem in its rational section is outside this audit's assigned scope.

The short phrase “By Bertini” in its Section 2 can be supported by the incidence argument above. No extra assumption of normality, immersion, a regular action on a chosen resolution, or a geometrically ruled original model is needed. The primary-source automorphism reference above is available to add to Section 4 if desired.
