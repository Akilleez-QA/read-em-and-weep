# Full-support residual rank five: surface finiteness and dimension six

## Hypotheses, dependency status, and result

Work over C. Let V have dimension five and f:V^3 -> J be trilinear, outer symmetric and cyclic zero. Suppose A_a:V/Ca -> J, b -> f(a,a,b), is injective for every nonzero a. The finite-dimensional target J is otherwise unrestricted. Let E_u=V/Cu and let Q_u:Sym^2 E_u -> J/im A_u be the residual map (up to its harmless middle-line twist). Put K_u=ker Q_u. Thus residual rank five means dim K_u=5, not rank five of its individual tensors.

The pointwise and finite-middle conclusions below use these three tensor hypotheses. The global dimension-six conclusion ALSO uses the previously established hypothesis

    dim { [u] in P(V): rank Q_u < 10 } <= 2.                 (H)

We do not derive (H) from the three tensor hypotheses here. For the actual equivariant operation and its additional bundle hypotheses, the precise prior source is https://github.com/Akilleez-QA/read-em-and-weep/blob/feb2038a34949d8eddd670cde5871b639c26187d/research/hm/normalizer-rank-five/quintic-normalizer-exclusion/COROLLARY.md, Section 2; its generic-rank-ten assumption is discharged by https://github.com/Akilleez-QA/read-em-and-weep/blob/2756a1b6bd2cb86c38473a5ce036d437a4e2f77a/research/hm/local-defect/rank-eight-global-exclusion/PROOF.md, as recorded in https://github.com/Akilleez-QA/read-em-and-weep/blob/a383e3c1b82123cd5bb8f98256c6adb7a6bfa0da/research/hm/incidence-foundations/full-middle-two-zero/INDEPENDENT_ZERO_EXCLUSION_AUDIT.md. The equivariance, target-dimension and bundle inputs of those earlier results are not being silently added to the abstract pointwise theorem.

The complete surface exclusion is also collected in https://github.com/Akilleez-QA/read-em-and-weep/blob/3109756417e62b91a092b5a89ee412089322a986/research/hm/incidence-foundations/fullsupport-rank-five-surface-exclusion/PROOF.md. The both-nonplanar exclusion is obtained by combining https://github.com/Akilleez-QA/read-em-and-weep/blob/003f9233a60e49e389485b285af68e97d9559853/research/hm/incidence-foundations/nonplanar-factor-degree-bounds/PROOF.md, https://github.com/Akilleez-QA/read-em-and-weep/blob/eb2eb27fc092158da1afa7d6b1028be017af0c95/research/hm/incidence-foundations/quadratic-gradient-syzygy/PROOF.md, https://github.com/Akilleez-QA/read-em-and-weep/blob/1a9479838233b0080f7d15e5b4c150504160a106/research/hm/universal-polar/rank-five-quadric-maps/PROOF.md, and https://github.com/Akilleez-QA/read-em-and-weep/blob/e7cc77bf6b4005cc9e30701bdbb78e8bd2e1e2d4/research/hm/incidence-foundations/nonplanar-linear-correspondence-exclusion/PROOF.md. The new smooth-target lemma has an independent PASS audit at https://github.com/Akilleez-QA/read-em-and-weep/blob/3109756417e62b91a092b5a89ee412089322a986/research/hm/incidence-foundations/smooth-target-independent-audit/AUDIT.md. This integration uses that audited lemma as an explicit dependency; without it, the conclusions remain conditional on exclusion of the both-nonplanar compatible surface case.

**Theorem.** For a fixed operation f:

1. At every middle with dim K_u=5 and full support E_u, its separately projectivized independent-zero fiber has dimension at most two.
2. At any such full-support dimension-five residual kernel, every integral compatible rank-two surface has an ordered factor projection that is a point or a projective line. Middle points carrying any such surface belong to one fixed finite set F determined by f.
3. Under (H), the entire independent-zero locus over full-support residual-rank-five middles has separately projectivized dimension at most three and affine dimension at most six. Over the intersection of that stratum with F its affine dimension is at most five.
4. Under (H), consequently every independent-zero component generically of full-support residual rank five has affine dimension at most six. This includes components with moving middle and curve fibers.

These are dimension statements about reduced supports. They do not bound Zariski tangent spaces, multiplicities, or nilpotent structures.

## 1. Reconstruction and the diagonal

For independent a,b, the vectors A_a(b), A_b(a) are independent. Indeed a relation A_a(b)=t A_b(a), together with cyclic zero and outer symmetry, gives A_(a+t b)(b)=0, contrary to injectivity (and each individual repeated value is nonzero).

It follows that every nonzero dependent zero triple has all three projective lines equal. If the outer lines coincide, cyclic zero reduces vanishing to a repeated-input value. If they differ and the middle is in their span, vanishing is a linear combination of the two independent repeated values. Thus the dependent locus of any projective middle fiber is precisely its single diagonal point.

Choose a splitting V=Cu direct-sum E. On K=K_u there is a unique linear correction v:K -> E defined by

    f(a,u,b)=A_u(v(ab)).

For independent a,b in E, a projective ordered residual pair lifts uniquely to a zero triple exactly when v(ab) belongs to span(a,b): if v(ab)=r a+s b, the lifts are a-s u and b-r u. The identity

    f(a+alpha u,u,b+beta u)
      = A_u(v(ab)+beta a+alpha b)

proves existence and uniqueness. This reconstruction is algebraic on rank-two charts; equivalently use the finite etale ordered-factor cover in https://github.com/Akilleez-QA/read-em-and-weep/blob/f1a2157fdc195e2fcafc9c5172fa39724d7656a4/research/hm/incidence-foundations/rank-nine-independent-incidence/PROOF.md. There is no extra lift parameter.

There are no compatible nonzero squares. If e^2 belongs to K and v(e^2) belongs to Ce, the equation f(e,u,e)=-2A_e(u) would make A_e(u) proportional to A_u(e), contradicting their independence. Rank-one residual products therefore do not contribute independent-zero points. Diagonal points that enter a projective closure do not increase its dimension.

## 2. Exhaustive classification of compatible surfaces

Let X be the projective closure of an integral ordered compatible rank-two surface, and let A,B be its factor images in P(E). They have dimension at most two.

- If an image is a curve, https://github.com/Akilleez-QA/read-em-and-weep/blob/b87127f426256ea0e0ae0d8124ac01b64ae4601f/research/hm/incidence-foundations/nonlinear-curve-factor-exclusion/PROOF.md proves that it is a line, using only dim K=5 and full support.
- If an image is a point, Section 7 of that proof gives a compatible common-factor plane hU, where dim U=3 and h is not in U.
- If both images are surfaces and both are planes, https://github.com/Akilleez-QA/read-em-and-weep/blob/381ebe011d53863a2fe98d532088544c264921c1/research/hm/middle-surface/linear-graph-surface-exclusion/PROOF.md excludes them under square avoidance.
- If exactly one surface image is planar, https://github.com/Akilleez-QA/read-em-and-weep/blob/77e8e6d5c98d558f20dacba2ed235d41800fa31d/research/hm/incidence-foundations/one-planar-factor-exclusion/PROOF.md excludes the pair without compatibility assumptions.
- If both are nonplanar, https://github.com/Akilleez-QA/read-em-and-weep/blob/003f9233a60e49e389485b285af68e97d9559853/research/hm/incidence-foundations/nonplanar-factor-degree-bounds/PROOF.md shows that they coincide with an integral quadric Q, and the annihilator evaluation matrix has generic rank four and maximal-minor gcd equal to the irreducible equation of Q. Its primitive quadratic left syzygy is Cq with C symmetric, by https://github.com/Akilleez-QA/read-em-and-weep/blob/eb2eb27fc092158da1afa7d6b1028be017af0c95/research/hm/incidence-foundations/quadratic-gradient-syzygy/PROOF.md. Rank C is at least three. Rank three contradicts the nonplanar kernel image; rank four gives an ambient projective-linear involution, contradicted by https://github.com/Akilleez-QA/read-em-and-weep/blob/e7cc77bf6b4005cc9e30701bdbb78e8bd2e1e2d4/research/hm/incidence-foundations/nonplanar-linear-correspondence-exclusion/PROOF.md using dense compatibility and square avoidance. Rank five contradicts https://github.com/Akilleez-QA/read-em-and-weep/blob/1a9479838233b0080f7d15e5b4c150504160a106/research/hm/universal-polar/rank-five-quadric-maps/PROOF.md, which forces the maximal-minor gcd to be a square of a linear form.

Thus at least one factor image is a point or line. This assertion applies to any integral surface subvariety of the compatible rank-two locus, not just maximal components: multiplication has finite fibers, so its product image is a surface, with X an ordered-factor component above it.

## 3. A fixed first factor has compatible dimension at most two

This elementary bound will prevent an unexamined three-dimensional fiber. Fix nonzero a in E and put M_a={b:ab in K}. Its dimension is at most four. If dim M_a<=2, the assertion is immediate. If dim M_a=3, any compatible surface fills P(M_a); if a belonged to M_a, specializing the complete compatible family along a(a+t b) and a(a+t c), for independent b,c modulo Ca, would make v(a^2) belong to Ca. Thus a is not in M_a in this case.

If M_a=E, write pi:E -> E/Ca and T(b)=v(ab) modulo Ca. Away from b proportional to a, compatibility means T(b)=lambda pi(b), with a unique scalar lambda. The pencil T-lambda pi has generic rank three: a 3-by-3 minor has nonzero leading coefficient because pi has rank three. Except at finitely many lambda its projective kernel is a point, so the corresponding compatible family has dimension at most one. At exceptional lambda the rank cannot be zero, since T=lambda pi would make v(a^2) belong to Ca. Every exceptional projective kernel therefore has dimension at most two.

Consequently all compatible components with fixed first factor have dimension at most two. Every surface component is a projective plane P(U_a), with dim U_a=3, aU_a subset K, and a not in U_a. The latter condition follows by the same two-path specialization if a belonged to U_a. Dense compatibility on the plane suffices, since the compatibility wedge identity holds on its closure and is equivalent to compatibility away from the diagonal.

## 4. No compatible component of dimension at least three

Suppose an integral compatible rank-two component has projective closure Z of dimension d>=3. If both factor images have dimension at least two, a general successive ample complete-intersection surface S in Z is integral, meets its dense compatible rank-two open, and has both factor images of dimension two. Here the usual dimension theorem for general sections gives image dimension min(2,dim image): if the original image has dimension two, the section meets its general fibers in dimension zero; if the image has dimension three, the section has zero-dimensional generic fibers onto a surface image. Bertini applies successively to the integral projective Z. Section 2 excludes such S. Thus one factor image has dimension at most one.

A point image contradicts Section 3. Suppose therefore that the first image is an integral curve C. General fibers of Z -> C have dimension d-1; Section 3 makes d=3 and makes every two-dimensional irreducible component of a general fiber a compatible plane P(U), dim U=3, with a not in U. General fibers need not be geometrically integral. To account for possible monodromy of these plane components, choose an irreducible parameter curve Gamma in the relative Grassmannian of planes, dominating C generically finitely, that records one such family of components. Such a curve is obtained by splitting a geometric generic plane component after a finite extension of C(C) and taking its closure.

Choose general points (a,U) and (b,W) of Gamma with distinct first factors. Both three-dimensional vector spaces aU and bW lie in the five-dimensional K, so their intersection is nonzero. But aE intersect bE=C(ab), by unique factorization. Hence ab lies in both spaces and b belongs to U. Keeping the general pair (a,U) fixed and varying (b,W) in Gamma gives a dense set of b in C. Consequently C subset P(U) by closure, in particular a belongs to U. This contradicts square avoidance from Section 3. No descent or uniqueness of the plane component over C is assumed.

All cases are excluded. The compatible rank-two locus, and hence the independent-zero fiber, has dimension at most two. This argument does not assume in advance that all fibers are surfaces or that their factor images have dimension at most two.

## 5. A fixed finite middle set handles moving components

For a point-factor surface, Section 7 of https://github.com/Akilleez-QA/read-em-and-weep/blob/b87127f426256ea0e0ae0d8124ac01b64ae4601f/research/hm/incidence-foundations/nonlinear-curve-factor-exclusion/PROOF.md constructs a corrected (1,3) zero rectangle, putting its middle in the finite middle image of C_(1,3) from https://github.com/Akilleez-QA/read-em-and-weep/blob/7f62d4535d0bfca8b2be93b0b4068cfd06fec717/research/hm/middle-surface/extremal-surface-geometry/GENERALIZATION.md.

For a line-factor surface, the complete classification and integration in https://github.com/Akilleez-QA/read-em-and-weep/blob/77a6edcdf6f8d1e4067c1d8b6074bb0352606653/research/hm/incidence-foundations/quartic-middle-finiteness/PROOF.md, Section 7, put its middle in the union of three fixed finite sets:

- the middle image of C_(2,2), for the degree-zero kernel bundle;
- the middle image of the rank-one (2,3) incidence R from https://github.com/Akilleez-QA/read-em-and-weep/blob/85402222aca57fa071310a21f421755ecf35fe42/research/hm/incidence-foundations/finite-rectangular-incidence/PROOF.md, for cubic type III;
- the middle image of the rank-two flag incidence D from https://github.com/Akilleez-QA/read-em-and-weep/blob/77a6edcdf6f8d1e4067c1d8b6074bb0352606653/research/hm/incidence-foundations/quartic-middle-finiteness/PROOF.md, for quartic types A and B.

Let F be the union of these four finite middle images. Existence of a compatible surface is sufficient to put [u] in F. There is no need to select components, splittings, types, or corrected complements algebraically in a family. In particular varying factor components cannot produce additional middle points outside F.

Let S be the locally closed rank-five, full-support middle stratum. Full support is an open condition on its rank-five kernel bundle. Section 4 bounds all fibers over S by two, and Sections 2 and 5 bound all fibers over S\F by one. Under (H), dim S<=2. The fiber-dimension theorem gives

    dim(projective independent zeros over S\F) <= 2+1=3,
    dim(projective independent zeros over S intersect F) <= 2.

Thus the entire locus over S has dimension at most three. Restoring the three nonzero input scales is a (G_m)^3 torsor, adding exactly three to dimension. This proves the asserted affine bounds. An irreducible component generically over S has the same dimension as its dense open part over S, so special lower-rank boundary fibers cannot invalidate its bound.

## 6. Precise remaining frontier

Combining this result with https://github.com/Akilleez-QA/read-em-and-weep/blob/3888945e9e312d2e0b0ed397f9640ea3cce9513d/research/hm/middle-surface/rank-six-surface-reduction/COROLLARY.md, an independent-zero component of affine dimension at least seven cannot generically have residual rank at least six, or rank five with full support. If its generic residual rank is five, its kernel support must therefore be three-dimensional: support at most two is impossible for a five-dimensional kernel.

Even in the ternary-support case, the compatible rank-two fiber has dimension at most two. Indeed, if it had dimension at least three, intersect its product image in P(K)=P^4 with a general hyperplane P(K'), dim K'=4. This would produce a compatible rank-two surface for K' subset Sym^2 E_0 with the restricted square-avoiding correction. That contradicts the general supported-ternary four-space theorem in https://github.com/Akilleez-QA/read-em-and-weep/blob/c109a2f634916ca7fe9dc4bf3e8f25c2dae6a309/research/hm/normalizer-rank-five/rank-six-cubic-web/REDUCIBLE.md. Under (H), the generic ternary rank-five case consequently has affine dimension at most seven; dimension seven forces a two-dimensional middle image and a two-dimensional generic projective fiber.

This does not exclude ternary rank-five surfaces: the isolated synthetic model in https://github.com/Akilleez-QA/read-em-and-weep/blob/9f4af00ab7ba91719a3f4d91ec4c1f71c12d96c4/research/hm/universal-polar/rank-five-surface-countermodel/PROOF.md is consistent with them. Nor does it exclude their moving families, resolve their required boundary, or treat generic residual rank at most four. Thus no universal independent-zero bound six or global exclusion of dimension seven is claimed.


