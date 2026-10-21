# Independent review: annihilator incidence at transverse surface nodes

Verdict: PASS as a structural proof, conditional on the explicitly pinned repository dependencies. This is an independent mathematical review, not a proof-assistant certification or an actual source-instance evaluation.

Reviewed artifact: PROOF.md, SHA-256 6f161073fe974892ff38fb5005486e61086dfb5140073202335c46a8de5c757f, including the final derived structure-sheaf pushforward section.

## Scope of independent verification

The review verifies the universal local algebra, its application given the stated rank and scheme-theoretic degeneracy hypotheses, the global normalization argument, the reduced scheme gluing, and the derived pushforward. It does not independently re-prove the prior actual-map identification, its rank stratification, or the cited modular-surface geometry. These are explicit dependencies: PR573 at 6c2dbd48edea0577acf063a60e1edbbbe92ced5c, PR570 at e5e55594ef2b99cefb81c4c02b22cb45e1ff0025, and PR554 at eb16c0e38e5157dc2902273cea3939b3410057c7.

The final rank-eight/node matching clarification is also valid: the vanishing residual entries force all maximal minors to have zero linear part at each rank-eight point, so its tangent dimension is four and it is singular on the two-dimensional D=S. Equality of the two finite sets then follows from their equal cardinalities of thirty. No coordinate matching is required.

## Local matrix lemma

1. Exact equality I2(B)=(u_i v_j) is indispensable. Taking degree two gives a four-dimensional span of cross quadrics. Restricting to either branch gives zero minors. If the linear matrix map on one tangent plane had image dimension at most one, the mixed quadrics could span at most two dimensions. Thus each branch gives a two-dimensional rank-one matrix space.

2. The ruling classification is valid: two independent decomposable tensors whose entire span has rank at most one share one tensor factor. For two fixed-column rulings, all mixed minors are constant multiples of the same determinant of the varying rows. For one fixed-column and one fixed-row ruling, all mixed minors contain the same linear factor on the first branch and span at most two dimensions. Both contradict the required four-dimensional span.

3. The remaining fixed rows must be independent. After normalizing them to the coordinate rows, the mixed minors are the coordinates of the wedge map C tensor E -> Lambda^2(C^4). Their span dimension equals the rank of that map. A nonzero common vector of C and E gives the nonzero kernel tensor w tensor w. Consequently four independent minors force complementary two-dimensional column planes. This justifies the asserted linear normal form without assuming it.

4. On the first branch the first two entries of its nonzero column form regular parameters. They have no common nonunit divisor in the two-dimensional regular local UFD. If the other column is a fraction h times the first, writing h with coprime numerator and denominator shows that the denominator divides every entry of the first column, hence is a unit. Absence of linear terms in the other column forces h to have zero residue. The opposite branch has the analogous regular factor g of zero residue.

5. The two column transformations both have identity residue and therefore define one invertible matrix over the fiber-product ring. After changing each branch's parameters to the appropriate column entries, the remaining entries have order at least two. They can be eliminated using coefficients in the maximal ideal, so the row transformations also have identity residue and glue. Separate branch coordinate changes preserve the common residue field and likewise define an automorphism of the fiber product. No unsupported lifting of the normal form from the node ring to the ambient regular ring is required.

## Incidence and global geometry

On either projective kernel chart, the kernel equations express one column as a multiple of the other. Every maximal minor is therefore zero in the incidence quotient, scheme-theoretically. It is legitimate to pass to the degeneracy ring before applying its normal form. Splitting the invertible rank-eight block merely determines the other eight kernel coordinates and does not add projective components.

At an endpoint the completed ring is C[[a,b,t]]/(ta,tb). The equality (ta,tb)=(t) intersect (a,b) proves reducedness and identifies precisely one smooth surface and one smooth curve meeting at a reduced point. This reduced Noetherian ring has no embedded associated primes. At a nonendpoint of the vertical projective line the completed local ring is a regular one-dimensional ring. At rank nine the residual entries are exactly the degeneracy ideal, so the incidence is the degeneracy surface there, not merely set-theoretically equal to it. Completion is faithfully flat, so these conclusions descend to the algebraic local rings.

The closure of the graph over the dense smooth locus is irreducible. Its local surface pieces have one point at each of the two distinct endpoints over a node; these are not intersecting surface branches in the incidence. Its local rings are regular by their completions. Its map to S is proper, quasi-finite and birational, hence finite, and normality identifies it with the normalization. In particular the argument neither assumes that normalization is already an incidence component nor conceals an extra blowup. Every other irreducible component must lie in one of the thirty exceptional fibers. Each fiber is exactly one projective line, and its nonendpoint points lie on no surface component. Thus there are exactly thirty additional curve components.

The scheme gluing follows from the same local intersection identity, not solely from a description of topological components. The union's normalization is the disjoint union of its smooth surface component and thirty smooth projective lines. The incidence has connected fibers but is a reduced mixed-dimensional scheme, not a pure smooth resolution.

## Derived pushforward

The exact sequence for the union is valid with the intersection scheme consisting of the sixty reduced endpoints. The normalization map is finite. Each curve component maps to a point and has H^0(O)=C and H^i(O)=0 for i>0. The endpoint residue map from the direct sum of the two completed branch rings is surjective onto C direct-sum C. Adding the bridge constant and taking the difference of restrictions gives kernel precisely the pairs of branch functions with equal residues, which is the original node ring. Faithfully flat completion verifies both surjectivity and equality with O_S. The long exact sequence therefore gives p_*O_Z=O_S and R^i p_*O_Z=0 for i>0, with the natural unit realizing the derived isomorphism.

This conclusion is compatible with the non-Cohen-Macaulay node: it is a statement about the structure-sheaf pushforward of the mixed-dimensional incidence, not a dualizing-sheaf formula or a rational-singularity assertion.

## Boundaries

No selected actual source matrix, coefficient, point, or rank was evaluated. No large computation was used. No first-order tangent result was promoted to a higher-order claim without the UFD and gluing argument. No conclusion concerning the separate full quadratic-parameter incidence, original lifting obstruction, or its algebraicity follows from this review.
