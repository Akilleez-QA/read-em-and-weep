# Eight-root position dominance for arbitrary skew-line configurations

## Statement

Let L_1,...,L_N be pairwise disjoint projective lines in P^4 over C. Fix a selection pattern n_i in {0,1,2} with sum n_i=8. On the finite ordered-root cover of the open set of quadrics meeting every L_i transversely, record the selected intersection points, ordering the two roots when n_i=2. The resulting map to the product of eight copies of the corresponding L_i is dominant. The same holds after any fixed isomorphisms L_i -> Gamma.

Consequently any nonempty Zariski-open condition on eight independently general points of Gamma holds for every such selection from Q intersect (union L_i), for general Q. The finite union over selection patterns and root choices remains a proper bad locus. This does not itself prove that the desired regular elliptic quadric pencil is a nonempty open condition on Gamma^8; that is a separate geometric input.

No selected quadric, coefficient calculation, or numerical rank is used.

## 1. Quadrics interpolate three skew lines

Restriction H^0(P^4,O(2)) -> direct sum of H^0(L_i,O(2)) is onto for any three pairwise skew lines.

For two lines, their vector spaces are complementary in their P^3 span. Quadrics restricting to either line can plainly be chosen independently. Inside this P^3 write coordinates as two pairs (u,v); quadrics vanishing on both lines are all four bilinear forms u_a v_b. A third line skew to both is the graph v=T u of an invertible 2 by 2 matrix. Restriction of these bilinear forms spans all quadratic forms in u. Thus restriction to all three lines is onto when they lie in P^3.

Otherwise let H be the P^3 spanned by the first two lines. The third line meets H in a point p not on those lines. The four bilinear quadrics have base locus precisely the union of those two lines in H, so one is nonzero at p. After prescribing the first two restrictions, add a suitable such quadric to obtain the desired third-line value at p. Finally add ell_H times arbitrary linear forms; on the third line these supply exactly the two-dimensional space of quadratic sections vanishing at p. This gives any third-line restriction.

Equivalently, under the degree-two Veronese embedding into P(Sym^2 C^5), the vector span U_i of the conic nu_2(L_i) has dimension 3; two such spaces have sum dimension 6; any three have sum dimension 9.

## 2. Generic point interpolation with multiplicities of selection

For any collection of at most nine slots assigned to the lines, with at most three slots per line, independently generic points in the slots have independent Veronese vectors.

Indeed assign the vector space U_i to each slot on L_i. For every subset of slots, the sum of the assigned spaces has dimension at least the number of slots: one distinct line contributes dimension 3; two contribute 6; three or more contribute at least 9. The linear independent-transversal criterion therefore applies.

For completeness that criterion follows by induction. Given spaces V_1,...,V_s with dim(sum_{i in J} V_i)>=|J| for every J, if a nonempty proper subset J is tight, choose independent vectors for J, quotient by their span (which equals the sum for J), and apply induction to the remaining spaces. If no nonempty proper subset is tight, choose any nonzero v_s in V_s and quotient by its span; each subset of the remaining spaces loses at most one dimension and still satisfies the required inequalities. Lift the resulting independent choices.

The independent choices can be made on the actual Veronese conics, not merely their vector spans. The wedge of the choices is a multilinear function. If it vanished on the product of the conics, successive linear spanning in each slot would make it vanish on the product of the U_i, contrary to the independent transversal. Thus independence holds on a nonempty open subset of the product of lines. Coincident choices on one line are automatically avoided there.

In particular eight generic selected points impose eight independent linear conditions on ambient quadrics. Moreover their quadrics do not contain any specified source line: append a generic ninth point on that line and apply the same result (there are at most three slots on it). Independence of all nine gives a quadric vanishing at the first eight but not at the ninth. This simultaneously excludes containment of every source line, since there are finitely many.

## 3. A dominating incidence component

Over the independent-point open subset of the eightfold product, quadrics through the selected points form a projective bundle of fiber P^6. Its total dimension is 8+6=14 and it is irreducible. The preceding paragraph supplies a dense open where quadrics contain none of the source lines. Its projection to P^14 then has finite fibers, because on each line there are only two roots and finitely many ordered selections. Its image therefore has dimension 14, hence is dominant. In particular it meets the open of smooth quadrics transverse to all source lines.

This constructs a component dominating both the source-quadric space and the product of root-position parameters. We must still exclude additional generic components with special root positions; mere generic interpolation would not by itself suffice.

## 4. Irreducibility of the ordered-root cover

For each selected line L_i, the discriminant Delta_i of the restricted binary quadratic is an irreducible quadratic polynomial in ambient quadric coefficients: restriction to H^0(L_i,O(2)) is surjective and the binary-quadratic discriminant is an irreducible rank-three quadratic form. The divisors (Delta_i=0) are pairwise distinct, since simultaneous restriction to two skew lines is surjective and one binary form can have a double root while the other has distinct roots.

In the rational function field of P^14, their square classes are independent. To see this, trivialize the coefficient line on an affine chart. At the prime divisor Delta_i=0, Delta_i has valuation one, while each other Delta_j has valuation zero. Hence no nonempty product of the Delta_i is a square. Chart changes multiply the discriminants by squares and do not alter the assertion.

Adjoining the square roots of the m selected-line discriminants therefore gives a field extension of degree 2^m. A chosen root of each binary quadratic generates exactly this extension; the other root is then determined. This is the function field of the ordered-root cover, which is thus irreducible. Selecting two roots on one line with an order still adds only the same root choice, not another quadratic extension.

The component in Section 3 is consequently the entire generic ordered-root cover. Its map to the eightfold product is dominant. A proper closed bad locus in that product pulls back to a proper closed subset of the cover, whose image in the source open is proper because the cover is finite there. This proves simultaneous generic avoidance for all root choices and all finitely many selection patterns.

## Application and remaining input

For the actual 25 pairwise skew evaluation lines, each restriction kappa|L_i is an isomorphism onto the same rational sextic Gamma. The proposition therefore proves the previously missing independence of the eight kappa parameters selected by a general source quadric, even when two marks come from one line. There are no exceptional distinct-line patterns.

To exclude the quintic triple-point alternative, it remains separately to prove that a nonempty open subset of Gamma^8 admits two quadrics whose intersection is a smooth integral elliptic quartic, with the eight points noncoplanar. The existing secant obstruction then applies. No general-position assertion in ambient P^3 is substituted for that Gamma-specific existence statement.
