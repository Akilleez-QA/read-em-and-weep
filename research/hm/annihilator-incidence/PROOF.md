# The annihilator incidence resolves the primary surface and attaches thirty bridges

Status: authored structural proof; independently reviewed in REVIEW.md; not formally checked. Work over C. No selected actual source point, matrix, coefficient, or rank is evaluated.

## Dependencies and statement

PR573, commit 6c2dbd48edea0577acf063a60e1edbbbe92ced5c, identifies D=D9(e) globally as a closed subscheme with the reduced integral degree-fifteen primary surface S. Here e:3Q(-1)->10O on P4. PR570, commit e5e55594ef2b99cefb81c4c02b22cb45e1ff0025, identifies its normalization with X=S(5), using BHM Section 4.5 Propositions 9-11: X is smooth, S has exactly thirty transverse ordinary surface double points, and their completed local rings are C[[u1,u2,v1,v2]]/(u_i v_j). PR554, commit eb16c0e38e5157dc2902273cea3939b3410057c7, supplies exactly thirty rank-eight points and no lower-rank points. Each rank-eight point is singular on D: after splitting off a unit block its maximal minors are quadratic in entries vanishing there, so its Zariski tangent space is all of the ambient four-dimensional tangent space. Since D=S is a surface with exactly thirty singular points, the two thirty-point sets coincide. Rank(e)=9 elsewhere on S.

Define Z in P4 times P9 by e_x^*(k)=0. Then:

1. Z is reduced. Its unique two-dimensional irreducible component is isomorphic to X=S(5), not merely birational to X.
2. Z has exactly thirty further irreducible components, each the full vertical P1 above a double point of S.
3. Each vertical P1 meets X in two distinct reduced points, namely the two normalization preimages of the node. There are no other intersections.
4. At either attachment point its completed local ring is

   C[[a,b,t]]/(ta,tb).

   Away from the attachments the vertical components are smooth one-dimensional components, and X is smooth everywhere.
5. Scheme-theoretically, Z is obtained from X and these thirty P1s by gluing the two endpoints of each P1 to the corresponding two points of X. The projection Z->S has connected fibers. The normalization of Z is the disjoint union of X and the thirty P1s.

The proof below is a universal local matrix lemma. It does not infer a matrix normal form merely from a set-theoretic degeneracy locus.

## A universal matrix lemma at a transverse surface node

Let R=C[[u1,u2,v1,v2]], m its maximal ideal, I=(u_i v_j), and let B be a 4-by-2 matrix with entries in m. Suppose I2(B)=I exactly. Write U and V for the two complementary tangent planes. We prove that, over A=R/I, invertible row and column operations and separate formal changes of coordinates on the two branches turn B into

   [ u1  0  ]
   [ u2  0  ]
   [  0 v1  ]
   [  0 v2  ].                                           (1)

This assertion is over A, not necessarily over R. That is sufficient for the incidence.

### The linear terms force the correct Segre rulings

Let L be the degree-one part of B. Since the degree-two part of I is four-dimensional, the quadratic minors of L span precisely all four cross products u_i v_j. In particular L restricted to either U or V has rank at most one identically. Neither restriction can have image dimension at most one as a linear map from its tangent plane into matrices: in that event all cross minors would depend on at most one linear coordinate of that branch and span a space of dimension at most two. Thus both images are two-dimensional vector spaces of matrices of rank at most one.

A two-dimensional linear space of rank-one matrices has one fixed tensor factor. Indeed, for independent tensors c tensor r and d tensor s, the sum has rank at most one only if c,d are dependent or r,s are dependent. Thus on each branch either the column factor is fixed and the row varies, or the row factor is fixed and the column varies.

If both branches have fixed columns, every cross minor is a scalar multiple of the same bilinear form det(r(u),s(v)), so the span of quadratic minors has dimension at most one. If just one branch has a fixed column while the other has a fixed row s, each cross minor has the common linear factor det(r(u),s) on the first branch; their span has dimension at most two. These alternatives contradict dimension four.

Consequently both branches have fixed rows and varying columns. The two fixed rows must be independent, since otherwise every matrix in the combined linear pencil has rank at most one. Change the column basis to make these rows (1,0) and (0,1). Let C and E be the respective two-dimensional column spaces in C4. The cross minors are the coordinates of c(u) wedge d(v). Their span has dimension four, equivalently C tensor E -> Lambda^2 C4 is injective. If C and E had a nonzero intersection, a tensor w tensor w would lie in its kernel. Hence C and E are complementary. A constant row change and separate linear coordinate changes put L into (1).

### Rank-one factorization extends each kernel line

Restrict B to the branch C[[u1,u2]]. Its first column c has first two entries with independent linear terms, so those entries form a regular parameter system. In particular they have no common nonunit divisor. Every 2-by-2 minor vanishes, so the second column is h c for a scalar h in the fraction field. Since all h c_i belong to the regular local UFD and the c_i have greatest common divisor one, h belongs to that ring. Its constant term is zero, because the second column has no linear terms. The row (1,h) therefore extends regularly and is nonzero at the origin.

On the other branch, the analogous factorization is d(g,1), with g in the maximal ideal. Right multiplication on the first branch by [[1,-h],[0,1]] and on the second by [[1,0],[-g,1]] makes their rows (1,0) and (0,1). Both transformations specialize to the identity.

The ring A is the fiber product C[[u1,u2]] times_C C[[v1,v2]]. Thus these two changes glue to one invertible 2-by-2 matrix over A. On the first branch take the first two entries of c as new coordinates. The other two entries belong to their ideal and can be killed by elementary row operations specializing to the identity; their linear terms already vanish. Perform the analogous operation on the other branch using the last two entries of d. The two row transformations again specialize to the identity, so glue over A. This proves (1).

## Applying the lemma to the incidence

At a rank-eight point, split off an invertible 8-by-8 block of e^*:10O->3Omega(2). The residual block B has size 4-by-2 and vanishes at the point. Its 2-by-2 minor ideal is the completed ideal of D. PR573 and the transverse-node geometry give exactly I2(B)=I, so the lemma applies.

The incidence automatically factors scheme-theoretically through D. On a projective chart where the first kernel coordinate is one, the equations B(1,t)=0 express the first column as minus t times the second, making every minor vanish in the quotient. The other chart is identical with the columns exchanged. Therefore changing B over A is legitimate and loses no incidence equations or structure.

For (1), with homogeneous kernel coordinates [s:t], the equations are

   s u1=s u2=t v1=t v2=0.

On s=1, put z=t. The quotient is C[[v1,v2]][z]/(zv1,zv2), with the appropriate completion at the chosen point. It is reduced because

   (zv1,zv2)=(z) intersect (v1,v2).

It consists of a smooth surface branch z=0 and the vertical curve v1=v2=0, meeting in the reduced origin. On t=1 the other surface branch attaches at the other endpoint. Where s and t are both nonzero only the vertical curve remains, reduced and smooth. At the endpoints the completed local rings are precisely C[[a,b,z]]/(za,zb).

At rank-nine points, splitting off a 9-by-9 block gives a residual 3-by-1 block. On the unique projective kernel chart its three entries generate the maximal-minor ideal. Thus Z->D is an isomorphism there, including scheme structures. Outside D, Z is empty.

## Global identification of the surface component

Let Z0 be the reduced closure of the unique annihilator line over the smooth locus of S. The local calculation proves that Z0 has exactly the two separated smooth surface branches above each node, meeting the vertical fiber at distinct endpoints. Hence Z0 is smooth and Z0->S is proper, birational, and quasi-finite: over a node its fiber consists of exactly two points, and elsewhere it is an isomorphism. A proper quasi-finite morphism is finite. Therefore this finite normal birational cover is the normalization X of S. In particular no blowup of X at the sixty preimages is involved.

The local calculations also show that the entire Z is reduced and has no embedded components, and establish the asserted scheme gluing. They exclude any extra components: away from the thirty nodes there is only Z0, and over each node the full fiber is exactly one P1. Normalizing the reduced union separates its smooth irreducible components.

## Contribution and limits

This identifies the actual primary annihilator incidence globally, including its previously unresolved rank-eight local geometry. The degree-fifteen primary surface acquires its smooth modular normalization as the main incidence component, but the incidence itself is not a pure surface: it retains thirty one-dimensional bridges. In particular it is not the normalization of S and is not a smooth resolution in the usual pure-dimensional sense.

The statement is distinct from the full quadratic-parameter incidence in PR556 and PR558. It gives no algebraicity or lifting claim about the remaining original quadratic-boundary problem. The proof is structural; no actual source-instance evaluation or computation was performed.

## Next step: the incidence has trivial derived structure-sheaf pushforward

Let p:Z->S be the projection and let T be the reduced set of thirty double points. Let E be the disjoint union of the thirty bridge curves, and let J be the sixty reduced attachment points. The reduced scheme gluing just proved yields an exact sequence

   0 -> O_Z -> O_X direct-sum O_E -> O_J -> 0,

where the last map is the difference of restrictions. Here the structure sheaves on components are understood as their pushforwards to Z. Since X->S is finite, its higher direct images vanish. Since each bridge is P1 over a point, p_*O_E=O_T and all its higher direct images vanish. Finally p_*O_J=O_T direct-sum O_T (with one coordinate for each local branch), and there are no higher direct images.

The resulting map nu_*O_X direct-sum O_T -> O_J is surjective: after completion at every node the normalization ring is the direct sum of the two regular branch rings, whose residue maps onto the two copies of C are surjective. Its completed kernel consists of branch functions having the same residue, with that common residue equal to the constant on the bridge. This is exactly the completed fiber-product node ring of S. Surjectivity and the identification with O_S descend by faithful flatness of completion; away from the nodes both are immediate. Consequently the natural unit is an isomorphism

   O_S -> R p_* O_Z.

In particular p_*O_Z=O_S and R^i p_*O_Z=0 for i>0. This is an actual derived structure-sheaf identity despite the incidence's mixed-dimensional components and despite S not being Cohen-Macaulay at its double points. It does not assert a dualizing-sheaf trace identity or any identification with the different full quadratic-parameter incidence.
