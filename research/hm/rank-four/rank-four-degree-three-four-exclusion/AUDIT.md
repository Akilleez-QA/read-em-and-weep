# Author audit of the cubic/quartic component exclusion

Status: all cases checked; this file is an author audit, not an independent review.

1. The degree budget is used on the reduced union of distinct translates. Since dim Z4≤1, every translated positive-dimensional integral curve is itself a component. No multiplicity assumption is needed.
2. For A_C=1, the bound is 25d[G:H]≤125. For d=3 or4 the integer [G:H] is at most1. No unexamined index-two subgroup case remains.
3. Complement conjugacy uses the central-involution cocycle identity, not a coprime-order splitting theorem.
4. The span possibilities under full G are exactly T and V. The two-dimensional summand W cannot span an integral degree-three/four curve. The honest representation and distinct central parities prevent hidden mixed invariant subspaces.
5. Plane invariant equations are semi-invariants, but G is perfect, so they are invariants. The character averages are (10−30+20)/60=0 and (15+45)/60=1. The invariant quartic q² defines a nonreduced double conic, not an integral quartic.
6. In the full-span G case, faithfulness is justified on the normalization. The centralizer of an involution in PGL2 is the torus normalizer (including its extra component), not just a torus. It remains solvable, giving the contradiction.
7. For an axis-stable plane, the60 span orbit alone contributes degree at least180, already beyond125. No assertion about the planar curve's genus is used.
8. For an axis-stable hyperplane, the30 span count is exact. The two quadratic/linear diagonal exponents remain independent modulo constants on four indices. Thus a hypothetical D-stable curve has a faithful C5² action.
9. A degree-four curve in P3 may be elliptic or singular rational. Both cases are addressed. In the elliptic case, the polarization is pulled back to the normalization; any order-five automorphism is translation, and preservation of degree d requires5|d. The possible singularity of C does not change its line-bundle degree or the lifted action.
10. For a full-span axis-stable quartic, it is not enough to test D itself. The proof treats an arbitrary stabilizer lift (a,u) of an order-five unipotent. Its fifth power is the identity because the sum of powers of u is zero on F5². It centralizes the axis, yielding C5² rather than C25 or a nonabelian group.
11. The order20 axis stabilizer in SL2(F5) is the upper triangular Borel. Its order-five elements are unipotent with eigenvalue1, so they fix the axis pointwise. Elements with eigenvalue−1 have order10 and are not the elements selected by Cauchy's theorem.
12. No assumption that the curve is smooth, projectively normal, or linearly normal is made. Castelnuovo is used for the geometric genus; rational quartic in P4 is the only full-span case. All automorphism obstructions apply on the smooth normalization.
13. The final degree-at-least-five conclusion imports the conic exclusion, with its additional image-dimension hypothesis. The new degree-three/four theorem has no such additional hypothesis.

Deliverable: PROOF.md in this directory. No actual source-instance evaluation is claimed.
