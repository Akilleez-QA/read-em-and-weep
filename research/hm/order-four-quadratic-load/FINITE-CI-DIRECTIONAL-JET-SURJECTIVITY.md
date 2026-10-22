# Finite cubic complete intersections: all first-jet maps occur under free line-direction variation

## Scope

Work over C. Fix H=P3 inside P4 and a reduced set Z of 25 distinct points in H. Assume

h0(I_Z(2))=0, h0(I_Z(3))=3,

and that a basis f1,f2,f3 of V=H0(I_Z(3)) cuts a finite complete intersection X in H. Thus X has length27. This finiteness is an explicit additional hypothesis: b=3 alone is not claimed to imply it.

For any collection of transverse lines through the marked points, the square-hyperplane first-jet map is

j_nu: V -> Q,   Q=H0(O_Z(2))/eval H0(O_H(2)), dim Q=15.

Here nu belongs to the 75-dimensional vector space N=H0(T_H(-1)|Z), after fixing a projective normal splitting. The map sends f to the class of contraction(nu,df|Z). This is the jet criterion of DOUBLE-HYPERPLANE-JET-CRITERION.md at 18963f6d45068dd561c63420b9f0135103a9d09b, in Akilleez-QA/read-em-and-weep/research/hm/order-four-quadratic-load. The companion plane-trace criterion is at f4f1196f529f215a3813411d27e623671403be82.

## Theorem

The linear map

J: N -> Hom(V,Q), nu |-> j_nu,

is surjective. Consequently its kernel has dimension30. The locus where j_nu is not injective is an irreducible determinantal locus of codimension13 in N. More precisely, the loci where dim ker(j_nu) is at least k have codimensions

k=1: 13; k=2: 28; k=3: 45.

These are exact statements about unrestricted transverse line-direction variation with the marked points held fixed. They do not assert that the actual HM directions, or their hyperplane family, meet the injective open set.

## Proof, step 1: at least 23 independent gradient triples

At every p in Z, the Artin local ring of X has length at least one. The total length is27 and Z has25 distinct points. Hence

sum_(p in Z) (length O_X,p - 1) <= 2.

At most two marked points have local length greater than one. Let B denote these bad points and G=Z minus B. Thus |B|<=2 and |G|>=23.

For p in G, O_X,p=C. The ideal (f1,f2,f3) in the regular local ring O_H,p is therefore the maximal ideal. Their three classes generate the three-dimensional cotangent space m_p/m_p^2; because there are exactly three, they form a basis. Equivalently the differentials df_i(p) are linearly independent. Consequently the pointwise contraction map

T_H(-1)|p -> Hom(V,O_Z(2)|p)

is an isomorphism. This uses only finite-CI length and local regularity of H, not smoothness of X at the bad points.

## Proof, step 2: quadrics absorb the at-most-two uncontrolled rows

Take any linear map V->Q. Lift it to a linear map V->H0(O_Z(2)), represented by three column vectors after choosing a basis of V. The restriction map

H0(O_H(2)) -> H0(O_B(2))

is surjective because B has at most two distinct reduced points and O_H(2) separates them. For each column choose a quadric agreeing with that column on B, and subtract its evaluation. The new representative of the same map V->Q vanishes on B.

At every good point, the pointwise contraction isomorphism from step1 supplies the unique directional vector producing its three desired entries. Set the direction equal to zero at bad points. The resulting nu realizes the given map. This proves surjectivity of J. In particular dim ker J=75-45=30.

## Proof, step 3: exact determinantal codimensions

After a linear splitting of J, N is the product of its 30-dimensional kernel and the affine space of 15-by-3 matrices. The rank-at-most-r determinantal variety has codimension (15-r)(3-r). Taking r=3-k gives k(12+k), namely13,28,45. The rank-at-most-two variety is irreducible; its product with the kernel is irreducible as well. This proves all codimension assertions.

## Geometric and residual interpretations

With a fixed splitting, transverse projective lines through each p are parametrized by the corresponding affine3 space of normal-adjusted tangential directions. Thus N parametrizes actual collections of25 transverse lines with the fixed intersections Z, not merely formal tangent vectors. Pairwise skewness is a nonempty Zariski-open condition: when choosing each next line through a new marked point, lines meeting any already chosen line form a proper closed subset of its parameter space. The full-rank jet locus is also nonempty open by the theorem. Since N is irreducible, these two opens meet.

Therefore some pairwise-skew line arrangements through any such fixed finite-CI configuration have injective jets. This is not asserted for arrangements satisfying the additional HM bundle, symmetry, and degeneracy-locus constraints. No such constraints were imposed in the parameter space N.

For an arrangement that also satisfies the global ideal vanishings H0(I_C(1))=H0(I_C(3))=0 required by the published square-jet criterion, one has

dim ker(ell^2:M1->M3)=dim ker(j_nu),

because a=0. Thus its square residual defect has at most three dimensions, and the possible positive defects correspond to the codimension13/28/45 direction loci above. The theorem does not claim those global vanishings automatically for every free arrangement constructed here.

Changing the normal splitting adds a global section of T_H(-1), whose contraction with df is a global quadratic, hence contributes zero in Q. This gauge subspace has dimension4 and embeds in N (a nonzero constant projective vector cannot vanish at25 distinct points). It lies in the 30-dimensional kernel of J; passing to that quotient does not alter the determinantal codimensions.

## New consequence and precise remaining issue

A finite (3,3,3) base with25 reduced marked points does not impose an unavoidable square-jet defect merely through its point configuration: free transverse directions realize every possible 3-to-15 jet map. The source of a forced actual defect, if present, must lie in additional constraints on the actual line directions or bundle geometry. Conversely the codimension13 calculation alone does not prove that a particular four-dimensional hyperplane family avoids the defect locus, and is not a probability estimate or percentage of the HM search space.

No actual HM coefficient, matrix, line direction, selected rank, hyperplane instance, or consumed experiment was evaluated. This is a new symbolic deduction conditional on the finite-CI branch, not a review, actual HM transversality result, or full Q4 proof.

## Actual generic-family sharpening from transitive labels

Assume now the finite-CI branch occurs for general hyperplane sections of the actual invariant25-line arrangement, with the projective Heisenberg group acting transitively on the line labels. Then every one of the25 marked points is a simple point of X_H for general H. The residual length-two scheme is disjoint from Z_H.

Proof. Restrict to a nonempty open set of the irreducible dual hyperplane space on which the25 intersections are distinct, the cubic ideal spaces form a rank-three vector bundle, and their common zero schemes are finite complete intersections. Such an open is available under the generic finite-CI hypothesis: the cubic spaces are kernels of the algebraic evaluation map, constant rank is open, and the base-locus family is projective with zero-dimensional fibers on an open. One may also shrink by generic flatness, giving length27 throughout. Intersecting its finitely many Heisenberg translates makes the open invariant.

For each fixed line label i, the marked intersection p_i(H) is an algebraic section on this open. The rank-three cubic bundle maps by differentiation at p_i(H) into the rank-three relative cotangent bundle, with the appropriate O(3) twist. Rank less than three is a closed determinant condition. It is precisely the condition that X_H is not simple at that marked point, because the three generators cut a finite CI in a smooth threefold. For each label the condition therefore either holds identically or fails on a dense open. Intersect the finitely many latter dense opens and their group translates. The set of generically bad labels is now constant and invariant under the transitive label action. It is empty or all25. The length-excess bound at most two excludes all25. Hence it is empty.

Since all marked local algebras have length one and X_H has total length27, removing those25 open-and-closed Artin components leaves a length-two scheme supported away from Z_H. It need not be reduced. No statement about the residual scheme splitting into two rational sections of the parameter space is made.

For this actual generic finite-CI branch, the pointwise differential map is an isomorphism at every marked point. Thus it gives a vector-space isomorphism

N -> Hom(V,H0(O_Z(2))),

under which the 30-dimensional kernel of the unrestricted directional-jet map is exactly Hom(V,eval H0(O_H(2))). This is an exact description of the freely varying zero-jet directions, not a claim that the actual direction lies outside their determinantal enlargement.
