# Rank-two flag finiteness and quartic middle rigidity

## Theorem

Work over C. Let dim V=5 and let f:V³→J be trilinear, outer symmetric, and cyclic zero. Assume that for every nonzero a, the map

    A_a: V/Ca → J,   b ↦ f(a,a,b)

is injective. No bound or prescribed dimension on J is needed. Define the closed projective incidence

    D = {([u],X,H): dim X=2, dim H=4, X⊂H,
                    dim span f(X,u,H)≤2}.

Then u is outside H at every point of D, and the projection of D to P(V)×P(V*) has finite set-theoretic image. In particular, only finitely many middle lines occur in D. This does not assert that D itself is finite: its X-fibers are not analyzed here. No scheme-theoretic reducedness is asserted.

Consequently, middle points carrying a densely compatible quartic surface of either squarefree residual type A or B classified in /research/hm/normalizer-rank-five/quartic-line-factor-cases/PROOF.md form a finite set in any fixed operation satisfying these hypotheses. A kernel of one of these types without a densely compatible surface is not covered by this consequence. Their independently projectivized zero locus has dimension at most two, and restoring the three nonzero input scalings gives dimension at most five. Thus neither quartic type can supply a moving-middle component of affine dimension seven or eight.

## 1. Two repeated-input values are independent

For independent u,x, the vectors A_u(x) and A_x(u) are nonzero. If A_u(x)=t A_x(u), then cyclic zero and outer symmetry give

    f(x,u,x) = -2 A_x(u),
    A_(u+t x)(x) = A_u(x)-t A_x(u)=0.

The vector u+t x is independent of x, contradicting repeated-input injectivity. Therefore A_u(x),A_x(u) are independent for every independent pair, with no genericity qualification.

## 2. The entire flag boundary is excluded

Take a point of D and let M=span f(X,u,H), so dim M≤2. Suppose u∈H.

If u∈X, then M contains f(u,u,H)=A_u(H), which has dimension three because H contains Cu. This is impossible.

If u∉X, outer symmetry gives f(x,u,u)=A_u(x) for all x∈X. Since u∈H, this is contained in M. The restriction A_u|X is injective, so M=A_u(X) and dim M=2. The homogeneous quadratic map

    g:X→X,   g(x)=(A_u|X)^(-1) f(x,u,x)

is therefore defined everywhere. The scalar det(x,g(x)) is a homogeneous binary cubic. Over C it has a projective zero, including the case that it vanishes identically. For some nonzero x∈X, this gives g(x)=λx. Consequently

    -2 A_x(u)=f(x,u,x)=λ A_u(x),

contradicting the independence established in Section 1. Thus u∉H at every flag point. In particular no extra condition on rank f(Sym²X,u) is needed to control the boundary.

## 3. Projectivity forces finite middle and hyperplane images

The incidence D is closed in P(V)×Flag(2,4;V): its equations are the 3×3 minors of the bundle map from the rank-eight bundle X⊗U⊗H to the trivial bundle J. Hence its reduction is projective and has finitely many irreducible components.

On the open set u∉H the rank-one projector onto Cu along H is regular. If H=ker α, it is

    p_(u,H)(v)= α(v)u/α(u).

The expression is independent of the scalar representatives u and α and is regular because its denominator never vanishes. Its image line and kernel recover (Cu,H). By Section 2 it restricts to a regular map D_red→End(V), an affine space. On each projective irreducible component every regular scalar function is constant, so this map is constant. Therefore only finitely many projectors, and hence finitely many pairs (Cu,H), occur.

Equivalently, the complement of the incidence divisor {u∈H} in P(V)×P(V*) is affine, since that divisor is a hyperplane section under the Segre embedding. The proper image of D in this affine complement is a finite set. The projector proof above makes the conclusion elementary and avoids any compactification assumptions on the originally given quartic family.

## 4. Transfer from quartic residual kernels

Fix a middle u whose residual kernel is quartic type A or B and whose quartic surface is densely compatible with the actual correction. Choose an initial splitting V=Cu⊕E. Let B_u:Sym²E→J be q↦f(-,u,-)(q), and let K be the five-dimensional residual kernel, namely the kernel after quotienting J by A_u(V/Cu). Thus B_u(q)=A_u(v(q)) for q∈K and a uniquely defined linear correction v:K→E.

By the quartic classification, K has full support, is squarefree, lies in XE for a two-plane X⊂E, and every compatible correction has the form

    v(lm)=d(l)m+d(m)l

for a linear functional d∈E*. Define the hyperplane H as the graph of -d:

    H={e-d(e)u:e∈E}.

The new inclusion E→H removes the correction because outer symmetry gives

    f(l-d(l)u,u,m-d(m)u)
       = B_u(lm)-A_u(d(l)m+d(m)l).

The u,u,u term vanishes by cyclic zero. Thus the lifted K is killed by the bilinear map f(-,u,-) on H. Let X_H be the lift of X to H. The product space X_H H⊂Sym²H has dimension seven, while the lifted K has dimension five, so

    dim f(X_H,u,H)≤7-5=2.

Hence every such compatible quartic middle determines a point of D. Section 3 applies regardless of how the type or splitting behaves in a family. There is no appeal to the older rank-one (2,3) incidence.

The hyperplane H is unique among complements that kill K. Indeed, the difference between two corrections is a contraction c_e vanishing on K. In characteristic zero, c_e(q)=0 says the symmetric tensor q annihilates e under contraction. If this holds for all q∈K then e annihilates the linear span of their supports. Full support makes that span E, so e=0. Uniqueness is useful intrinsically but is not needed for the finite-middle conclusion: existence of at least one flag at every middle already suffices.

## 5. Exact dimension consequence and limits

For each of types A and B, every rank-two member of K has one factor in X, and the ordered factor locus is the union of two ruled surfaces. This is proved in /research/hm/normalizer-rank-five/line-projected-rank-five-reduction/QUARTIC_REALIZATION.md, Section 1. Since K is squarefree, all nonzero decomposable members have independent factors. Once the correction has been removed, repeated-input injectivity uniquely lifts a residual independent zero to its factors in H: for l,m independent,

    f(l+αu,u,m+βu)=A_u(βl+αm),

so vanishing forces α=β=0. Therefore each such compatible quartic middle has a two-dimensional separately projectivized ordered zero fiber. Finitely many middles give dimension two, and the free three-factor scaling adds three, giving affine dimension five.

This is a bound for the quartic locus only. It neither classifies arbitrary rank-five surface fibers with non-line factor image nor settles all other residual ranks or the total independent-zero dimension. Isolated realizable quartic examples remain fully consistent with this theorem.

## 6. Provenance and scope

The proof uses only the three stated tensor hypotheses and algebraic geometry of a closed flag incidence. It was derived concurrently with the argument and independently checked at the boundary.

## 7. Integration with the complete line-projected classification

Under the same global hypotheses, consider middle points whose full residual kernel K has dimension five and full support, and which admit a compatible irreducible rank-two surface with an ordered first-factor image equal to a projective line. The classification in /research/hm/normalizer-rank-five/line-projected-rank-five-reduction/PROOF.md gives exactly the following possibilities for the saturated kernel bundle on that line:

- Degree zero: the surface is a Segre product of complementary two-planes. Compatibility supplies a corrected (2,2) zero rectangle. Its middle belongs to the finite annihilation incidence C_(2,2) of /research/hm/middle-surface/extremal-surface-geometry/GENERALIZATION.md.
- Degree one: the only square-avoiding surviving full-support model is cubic type III. Its corrected projection spans supply a point of the finite rank-one (2,3) rectangular incidence R of /research/hm/incidence-foundations/finite-rectangular-incidence/PROOF.md, Section 5. This includes the contraction and noncontraction corrections.
- Degree two: the models are quartic A and B. Sections 2–4 above place their middles in the finite middle image of D.

The union of these three fixed finite middle sets is finite. Thus the middle points admitting ANY compatible surface with these full-support, dimension-five and line-projection hypotheses form a finite set. Pointwise corrected choices suffice; no global choice of complement, basis or normal form in a family is required.

In particular, let C be an independent-zero component generically of full-support residual rank five, whose generic projective fibers are surfaces admitting such a line projection. Its middle image is a point, its separately projectivized dimension is two, and its affine dimension is five. More generally, any component over these middle points with generic projective fiber dimension at most two has affine dimension at most five. This does not assert finiteness of the entire rank-five middle stratum, classify non-line-projected surface fibers, or bound moving-middle components whose generic fiber has dimension one.
