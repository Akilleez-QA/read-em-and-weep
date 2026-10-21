# Independent review: global primary degeneracy equality

Verdict: PASS, mathematically reviewed; not formally checked. Work over C. No selected actual HM/source coefficients, matrices, ranks or parameter instances were evaluated.

## Exact claim reviewed

The actual primary evaluation degeneracy scheme D equals the reduced integral coordinate-copy modular surface S15 globally as a closed subscheme of P4. This is an ideal-sheaf statement, equivalently equality after homogeneous saturation; it does not assert saturation of the raw maximal-minor ideal.

## Source and coordinate checks

BHM, Section 5.2 Proposition 13, printed page69, identifies the twenty-five torsion-section images as the translates of its displayed line x0=x2+x3=x1+x4=0. ADHPR, Section1, uses the cyclic shift, diagonal fifth-root action and reversal e_i→e_-i, whose negative eigenspace is this exact line. Its Section3, printed page9, explicitly states that the union of its twenty-five translates is cut out by all Heisenberg-invariant quintics. Thus the base-locus input is about precisely the coordinate copy identified in PR570, not a merely isomorphic or numerically similar configuration. Primitive Galois changes and dual conventions preserve the generated projective subgroup and reversal. Only the set-theoretic base-locus assertion is used.

Public sources checked:
- https://mathweb.tifr.res.in/Documents/Publications/Studies/Vector-Bundles-On-Algebraic-Varieties.pdf , BHM Proposition13 and Propositions9–11.
- https://arxiv.org/pdf/alg-geom/9606013 , ADHPR Sections1 and3.

## Universal quintic basis

The six products are exactly the cyclic eigen-coordinate boundary divisors. Their invariance follows either from the displayed universal Schrödinger formulas or from determinant one: the complementary generator is a monomial five-cycle, whose permutation sign is positive, so its multiplier product is one. The normalizer acts transitively on the six cyclic directions.

The Fourier weight proof is valid. The coefficient identities 1,-5,5 follow from the displayed power sums and Newton identities. Their weights give all five quadratic-phase characters, so the five q_a are independent. The sixth product has weight zero but lacks the x0^5 term in Q_0. The independent dimension computation gives26 diagonal-invariant monomials, consisting of one fixed monomial and five cyclic orbits. Thus the six products span the full invariant space. This is a universal polynomial calculation, not a selected source-instance test.

## Scheme-theoretic support argument

Since S is reduced and contained in D, I_D is contained in I_S. The quotient K=I_S/I_D is coherent and its support is normalizer-invariant. Exact torus equality from PR570 puts that support in one coordinate-boundary union. Invariance puts it in every translated union, hence in the common zero set C of the six invariant products.

At every point of C, PR566 makes D a smooth surface and S its two-dimensional reduced component. A smooth local surface ring is a domain; a same-dimensional reduced component through that point has the zero height-zero ideal. Hence D=S locally there. Thus K has no support on C and must vanish. This controls embedded and nilpotent discrepancies as well as additional components; no Cohen–Macaulay assumption on D is needed.

## Thirty-point depth defect

The added local corollary also passes. BHM gives exactly two smooth analytic surface branches with complementary tangent planes. In the completed regular ambient ring their ideals sum to the maximal ideal by Nakayama, so the reduced union is the fiber product of the two branch rings over C. This is C[[u1,u2,v1,v2]]/(u_i v_j). The normalization-style exact sequence into the direct sum of two depth-two branch rings, with quotient the residue field, gives depth one. Thus D fails local Cohen–Macaulayness precisely at those thirty points, while remaining regular elsewhere. No expected-grade determinantal Cohen–Macaulay theorem is applied to this codimension-two excess locus.

## Limits

The conclusion concerns the primary evaluation scheme on P4, not the ACM primary-bad quadratic-parameter eightfold or the residual fixed-beta surfaces. It does not establish primary square injectivity, the full-adjoint rank-twenty boundary, original selected coefficients, higher lifting, or algebraicity.
