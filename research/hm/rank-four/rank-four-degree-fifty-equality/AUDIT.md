# Self-audit of the conditional degree-fifty theorem

This is an author self-audit, not an independent review.

## Verified steps

1. Orbit exclusions need only component degree at least three. A-orbit size25 costs at least75; A-orbit size5 forces at least six disjoint A-orbits, hence degree at least90. The cubic/quartic exclusion is deliberately not imported.
2. All surviving components span P⁴ and have degree divisible by five. Faithfulness on normalization follows from nondegeneracy and the eigenspace argument, even for singular integral curves.
3. Castelnuovo at degree10 is9. A-RH gives g=25q−24+10t; with 0≤g≤9, the exhaustive possibilities are (g,q,t)=(1,1,0),(6,0,3). The initially suggested elliptic-only assertion would be false; the proof explicitly includes genus six.
4. The kernel of N_C→Aut(X_C/A) is exactly A, by the Galois function-field deck group. Consequently the genus-six quotient group's action on its three-point branch set is faithful and its order is at most6. This repair requires no classification of index-five subgroups of SL₂(F₅).
5. The elliptic case bounds the conjugation image on A by6; the standard G-action makes this bound apply to N_C/A. It is not assumed that all elliptic automorphisms themselves form a finite group of order at most6.
6. A nontrivial G-orbit of components has size at least5 because G is perfect and S₄ is solvable. Its component degree is therefore5 or10 at total degree50. The orbit bound≥20 rules it out. Multiple singleton components are excluded by the already proved degree≤45 theorem and divisibility by5.
7. Castelnuovo at degree50 is376, using 49=3·16+1. A-RH bounds the quotient genus by16. The imported genus≤13 obstruction gives the lower bound14.
8. For quotient genus16, RH value1/4 permits exactly the signatures (3,4,6),(4,4,4),(2,2,2,4). The proof gives a finite arithmetic enumeration, not an unrecorded computation. Projection of element orders4,6 to A₅ gives2,3; the projected branch cycles still generate the quotient. All three signatures are impossible.
9. At quotient genera14,15 the branch-point counts are respectively at most5,2. A normal-subgroup quotient makes the branch set G-invariant. Cyclic point stabilizers in faithful G-actions have orders at most10, so every orbit has at least12 points. Therefore the branch set is empty.
10. The two resulting normalization genera are25·14−24=326 and25·15−24=351. Neither is ruled out by the argument.

## Explicit dependencies and limits

- The normalizer action and degree-divisibility inputs are imported, not reproved. For Γ₄, line/conic exclusion imports the structural hypotheses of those proofs.
- The genus-at-most-thirteen theorem is imported and is the only substantive genus obstruction used before the elementary genus-sixteen calculation.
- The result is conditional on degree50 and does not prove that Γ₄ has degree50 or that either surviving case exists.
- Smooth normalization is essential throughout. Nothing here forces the embedded degree50 curve to be smooth or reduced as a degeneracy scheme; Γ itself was assumed to be reduced support.
- No actual source-instance evaluation is claimed.

## Addendum self-audit

The separate ADDENDUM.md additionally assumes the split group N=A⋊G, as in the stated Schrödinger normalizer setting. Matrix multiplication gives R³=I, S²=−I, RS=I+J with J²=0; all indicated orders are exact. The elementary-matrix generation formula and the affine multiplication convention were checked. The complement cocycle identity uses the central scalar z=−I and division by2 in F₅; det(I−R)=3 ensures the proposed two lifts cannot lie in a complement. Normality and standard irreducibility then force full generation of N. Riemann existence applies to the resulting surjective product-one triple. Its RH value is13/60 and its genus is326. All inertia subgroups project injectively to G, including the order-five one, so the A-action is free. This is an abstract curve construction only. It neither produces nor excludes an equivariant degree50 projective embedding.
