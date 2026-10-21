# Independent audit: isolated degeneracy lengths and the twenty-five lines

## Verdict

The argument is valid, conditional on the pinned structural inputs in PR555 and PR562–564. In particular, excess positive-dimensional special-fiber components do not invalidate the isolated-length bound. No global flatness is needed. The previously missing conservation step has a precise algebraic justification below.

This is an independent mathematical review, not a proof-assistant check. No selected actual HM/source evaluation, numerical matrix experiment, or public write was performed.

## Conservation lemma, with the essential separation step

Let G be a globally generated rank-twelve bundle on P3 over C, with integral c3(G)=105. Deform an arbitrary map 10O -> G along a pencil to a general map. The generic maximal-minor scheme has length 105. For an isolated special-fiber point p, the total-space ambient regular local ring has dimension four. Its maximal-minor ideal I satisfies height(I)<=3, while I+(t) being maximal-primary forces height(I)>=3. Thus its grade is three. Eagon–Northcott makes the quotient Cohen–Macaulay of dimension one. The element t is a parameter, hence a nonzerodivisor.

Base change the proper family to R=C[[t]]. The special-fiber local Artin scheme supported at p is an open-and-closed subscheme Y_p of that fiber. Stacks Project Lemma 37.53.9, Tag 0CT9, lifts it to a proper open-and-closed subscheme Z_p of the total family. This is precisely the needed isolation statement; choosing an arbitrary open neighborhood of p would not suffice.

Both fibers of Z_p over Spec R are finite: its closed fiber is Y_p, and its generic fiber is an open-and-closed subscheme of the length-105 generic fiber. A proper morphism with finite fibers is finite, by Stacks Project Lemma 37.44.1, Tag 02LS. Its finite algebra is local, since its reduction modulo t is local and R is henselian. The preceding local Cohen–Macaulay calculation, preserved by this base change, says t is injective on that algebra. It is therefore a finite torsion-free R-module, hence free of rank length(Y_p).

For different isolated points p and q, Z_p intersect Z_q is proper over R and has empty closed fiber. If nonempty, its closed image in the local trait would meet the closed point, a contradiction. The pieces are disjoint. Their generic lengths therefore add to at most 105. This proves the desired bound even with arbitrary excess components in the complementary special fiber.

Primary references, read during this audit:
- https://stacks.math.columbia.edu/tag/0CT9
- https://stacks.math.columbia.edu/tag/02LS

The argument uses only the stated decomposition theorem, not a semicontinuity assertion about isolated lengths. It does not claim that the complementary summand is flat.

## Independent checks of the remaining steps

1. General-map count: global generation gives fiberwise-surjective evaluation onto all matrices. General rank-nine degeneracy has expected codimension three, and rank-at-most-eight has codimension eight and is absent on P3. The Porteous class is c3(G). Alternatively, first choose nine everywhere-independent sections (their failure locus has expected codimension four), quotient to a globally generated rank-three bundle with the same Chern class, and take the zero scheme of the tenth section. The formal coefficient is 455-630+360-80=105.

2. Hyperplane isolation: under the assumption that no distinguished line is contained in a surface component, each is a one-dimensional irreducible component because dim D<=2. Its intersections with all other irreducible components form a finite set. A general hyperplane cuts each line away from these finite sets and does not contain a line. Its twenty-five intersection points are distinct and isolated in D intersect H. Embedded structure elsewhere does not alter this support argument.

3. Slice length: locally S6 has completed algebra C[[y]][z]/(z^7). A hyperplane transverse to the reduced line has derivative in y a unit. Formal implicit elimination of y leaves C[z]/(z^7). Because S6 embeds as a closed subscheme of D, the corresponding local degeneracy slice has length at least seven. Thus 25*7=175 contradicts the isolated-length bound 105.

4. Transitivity and smoothness: at least one line must be contained in a surface component. The transitive group preserving D preserves the union of its two-dimensional components, so all twenty-five lines have this property. At every closed point of every line the local dimension is then two, while the pinned embedding dimension is two. The local ring is regular, and over C the scheme is smooth there. This includes all points on the lines, not just generic points.

5. Normal and canonical degrees: on the smooth neighborhood the previously computed intrinsic normal kernel is the actual normal bundle O(-5). Therefore the self-intersection is -5, and adjunction gives canonical degree 3.

6. Formal extension: for n>=7, the square-zero kernel for S_n -> S_(n-1) is O(5n). Smooth-target lifting obstructions lie in H1(T_U|L tensor O(5n)) = H1(O(5n+2) direct-sum O(5n-5))=0. Finite-group averaging on the affine torsor of lifts produces equivariant compatible lifts of each chosen S6 embedding. The resulting map of completed neighborhoods is the identity on L and an isomorphism on conormal bundles; consequently it is an isomorphism on associated graded algebras, then on every finite quotient, and finally on completions. Thus §4 follows and does not require analytic convergence or algebraization.

## Scope safeguards

The result proves smoothness near the distinguished lines, not global normality, global reducedness, irreducibility, or degree 105 of D. The number 105 bounds isolated hyperplane degeneracy lengths through a general-map deformation. Formal normal-neighborhood splitting says nothing by itself about the separate original-source obstruction or algebraicity target.
