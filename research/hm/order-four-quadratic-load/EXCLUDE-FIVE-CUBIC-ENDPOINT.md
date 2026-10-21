# The no-quadric five-cubic endpoint is impossible

## A reusable family exclusion

Retain the actual HM evaluation geometry and primary vanishings used in EXCLUDE-UNIQUE-QUADRIC-ENDPOINT.md. There cannot be a rational family over a dense open set of hyperplanes H of geometrically integral curves D_H with all the following properties:

- D_H is contained in H and spans H;
- deg(D_H)>=5 and C intersect H is contained in D_H;
- the actual Plucker evaluation map is constant on D_H minus C.

Indeed the last condition supplies a rationally varying two-dimensional kernel K_H in U=H0(F(3)). Since it vanishes at the section points, its image lies in the three-dimensional incidence of (p,K), p in C and K contained in the rank-three evaluation kernel at p. The four-dimensional hyperplane parameter space therefore has positive-dimensional fibers over K.

On an irreducible such fiber, finitely many curve components of the common zero scheme of K cannot contain the integral nonplanar D_H for varying H: each curve spans only one hyperplane. A fixed integral surface component S contains D_H for a dense subset. A general H in that fiber does not contain S, so deg(S)>=5.

The projective Heisenberg group fixes the four global sections and preserves each degree-ten section zero scheme. Component orbits have sizes 1,5,25. The degree bound forces S to be invariant. If no component line of C lay in S, all 25 section-point maps on the irreducible fiber would have finite, hence constant, image. Their spanning property would make H constant. Thus S contains a component line, and Heisenberg transitivity makes it contain all C.

An invariant integral surface has degree divisible by five, by its Hilbert polynomial and the nontrivial central characters in degrees not divisible by five. Its degree is between five and ten. Degree ten forces it to be the entire section zero scheme; the section Koszul sequence and H1(F(-2))=0 then give h0(I_S F(3))=1, contradicting the two independent sections in K. Degree five forces a quartic equation by the hyperplane-section bound h0(O_S(4))<=55<70, contradicting I_C(4)=0.

These are exactly the arguments of Sections 1-5 of EXCLUDE-UNIQUE-QUADRIC-ENDPOINT.md. They use no quadric or genus hypothesis. That file supplies the scheme-theoretic justifications: evaluation is rank one on C, section zeros are pure local complete intersections, and the degree-ten equality is scheme-theoretic.

For the Heisenberg action one may alternatively use the established isomorphism Lambda²U=I_C(5), all of whose sections are invariant. Trivial exterior-square action forces each group element to act on U as plus or minus the identity; a group of odd order has no minus-identity image. Thus U is fixed, without any additional character calculation.

## Application to the no-quadric endpoint

Suppose a=0 and b=5 generically. FIVE-CUBIC-ENDPOINT.md proves that the canonical reduced cubic base curve D_H is an integral quintic containing all 25 section points, and that its six restricted quintics are proportional. It spans H because I_D(2)=0. Hence its actual Plucker evaluation is constant off the section points, and its constant two-section kernel varies rationally with H. All hypotheses of the preceding exclusion hold. This is a contradiction.

Therefore

    a=0 implies b<=4.

Together with EXCLUDE-UNIQUE-QUADRIC-ENDPOINT.md, the surviving generic possibilities are now

    a=0, 0<=b<=4; or a=1, b=4 or 5.

If a=0 and b=4, FINITE-CUBIC-BASE-RIGIDITY.md still forces a canonical reduced cubic base curve containing the whole section. That case has not been excluded. The a=1 cases also remain open.

## Scope

This removes another endpoint by the actual global evaluation geometry, not by expected dimension or a selected computation. It does not prove a=0, a vanishing cubic system, residual trace transversality, the original fixed-pair property, or full Q4. No selected HM/source coefficients, matrices, planes, or experiments were evaluated.
