# Distinct conic discriminants and actual smooth jumping conics

## Theorem

Let R=P(V) be the positive fixed plane of HM inversion, let F_R be the normalized HM restriction, and let

       0 -> A tensor O_R(-3) --M--> D tensor O_R(-2) -> F_R -> 0

be its actual stable Steiner resolution, with dim V=dim A=3 and dim D=5. Write

       mu:Sym^2 V* -> Sym^2 A

for the actual symmetric conic-multiplication isomorphism. Let Sigma be the ordinary discriminant of singular conics in P(Sym^2 V*), and let J be the jumping cubic defined by det(mu(q)). Then:

1. J and Sigma are distinct irreducible reduced cubic hypersurfaces.
2. The locus

       J minus (Sigma union Sing(J))

   is a nonempty dense open subset of J. It is a smooth irreducible four-dimensional family of smooth conics C with

       F_R|C = O_P1 directsum O_P1(-2).

3. Scheme-theoretically J intersect Sigma is a complete intersection of two cubics, of pure dimension three and degree nine. No reducedness or smoothness of this intersection is asserted.

In particular, the ordinary jumping type really occurs on smooth conics. This does not settle whether the more exceptional O_P1(1) directsum O_P1(-3) type occurs on a smooth conic: the Veronese surface Sing(J) could still lie entirely in Sigma.

## 1. The actual cohomology relation

The input ACTUAL-CONIC-DISCRIMINANT-AND-JUMP-STRATA.md proves that mu is an isomorphism and establishes the actual injection and differential

       j:A* -> A tensor Sym^2 V,
       d_M:A tensor Sym^2 V -> D tensor V,
       d_M composed with j = 0.

Here j is the cohomology injection H1(F_R(-2)) -> A tensor H2(O_R(-5)), and d_M is induced by the same linear map M in the Steiner sequence. The full contraction of j with a conic q is exactly mu(q):A*->A, not merely its symmetric part. The actual Serre-duality argument proves this whole map symmetric for every q. Perfect contraction in the Sym^2 V factor therefore determines j uniquely from mu; in particular there is no undetected alternating A tensor A summand. Thus the relation is not imposed on a freely chosen symmetric pencil.

The same input identifies J with the actual jumping-conic determinant scheme and identifies its singular scheme with the inverse image of the rank-one Veronese surface. These statements apply to nonzero conic equations without assuming the domain conic smooth.

## 2. A determinant-preserving isomorphism is a symmetric square

Suppose, for contradiction, that J=Sigma. The projective linear isomorphism P(mu) would then map the source symmetric determinant hypersurface onto the target symmetric determinant hypersurface. An isomorphism preserves the singular scheme. Hence it maps

       nu_2(P(V*)) onto nu_2(P(A)).

Restriction and inversion of the two Veronese embeddings give an isomorphism f:P(V*)->P(A). Every such isomorphism is projective linear: its pullback on Picard groups sends O(1) to O(d), and the inverse sends O(1) to O(e), where d,e are positive integers with de=1. Thus d=e=1, and the induced isomorphism of complete spaces of linear sections yields f=P(T) for an isomorphism T:V*->A.

It follows that P(mu) and P(Sym^2 T) agree at every point of the source Veronese surface. To see that they agree everywhere, apply their quotient to Sym^2 V*. Every square vector is then an eigenvector of a linear representative. There are finitely many eigenspaces, while the Veronese surface is irreducible; it is therefore contained in one eigenspace. Its linear span is all P(Sym^2 V*), so that eigenspace is the whole vector space. Consequently

       mu = c Sym^2 T,  c nonzero.

This step needs no identification of the two three-dimensional A5 representations. It is a statement about the actual projective map under the hypothetical equality of its determinant hypersurfaces.

## 3. The intrinsic contraction contradiction

Use T to identify A with V*. The dual identification identifies A* with V. After dividing j by the nonzero scalar c, contraction of j with q is the usual symmetric map q:V->V*. Therefore j is the canonical map

       j_can(v) = sum_i e^i tensor (e_i symmetric-product v),

where e_i is any basis of V and e^i its dual. This expression is basis independent: it uses the identity tensor in V* tensor V. The division by c does not change d_M j=0.

For clarity fix the convention

       u symmetric-product v = (u tensor v + v tensor u)/2.

Under Serre duality, multiplication by a linear form ell on H2 is contraction on symmetric tensors:

       ell contraction (u symmetric-product v)
           = (ell(u) v + ell(v) u)/2.

This follows directly by dualizing multiplication of linear sections. A different common symmetric-tensor normalization multiplies the following identity by a nonzero scalar and has no effect on its vanishing.

The coefficient map of M is now V*->D tensor V*. Reorder its tensor factors to obtain the D-valued endomorphism K:V->D tensor V defined by

       K(v) = sum_i M(e^i)(v) tensor e_i.

Let s=tr_V(K) in D. Applying the displayed contraction formula gives the intrinsic identity

       d_M(j_can(v)) = (K(v) + s tensor v)/2.

Indeed, contraction against the first symmetric factor contributes sum_i M(e^i)(e_i) tensor v = s tensor v; contraction against the second contributes K(v). Thus the actual kernel relation forces

       K + s tensor Id_V = 0.

Taking the V-trace gives s+3s=4s=0. Over C this implies s=0 and then K=0. Reordering tensor factors is an isomorphism, so the entire coefficient map M is zero. That contradicts the rank-three subbundle inclusion in the Steiner resolution.

Therefore J cannot equal Sigma. The argument is intrinsic linear algebra applied to the actual cohomology relation. It neither chooses nor evaluates a coefficient of the HM presentation.

## 4. The nonempty smooth jumping locus

Both cubics are irreducible and reduced. Their distinctness implies J is not contained in Sigma. Hence J minus Sigma is a nonempty dense open subset of the irreducible fourfold J. Its intersection with J minus Sing(J) is also nonempty and dense, because Sing(J) is a two-dimensional Veronese surface.

At a point of this intersection the domain conic is smooth and mu(q) has rank exactly two. The actual restriction sequence gives

       h0(F_R|C_q)=dim ker mu(q)=1.

Since deg(F_R|C_q)=-2, Birkhoff--Grothendieck forces O_P1 directsum O_P1(-2). The family is smooth because it is open in the smooth locus of J.

The two distinct irreducible cubic equations form a regular sequence in the polynomial ring of the parameter P5. Their intersection is therefore a complete intersection of pure projective dimension three, with degree 3 times 3 = 9. This statement does not assert that this boundary intersection is reduced.

Every smooth conic obtained here can occur as the positive fixed conic of a smooth inversion-even quadric in P4: take its nondegenerate positive block and any nondegenerate quadratic form on the two-dimensional negative eigenspace. The resulting block-diagonal quadratic form is nondegenerate. This realizes the splitting on actual smooth even quadrics, but does not infer a rank or extension property for their global full-adjoint sections.

## Input and scope

The sole specialized input is ACTUAL-CONIC-DISCRIMINANT-AND-JUMP-STRATA.md, read at immutable commit 313c54bec3f2556518dd531a8ce71f7a8ce22461, path research/hm/order-four-quadratic-load/ACTUAL-CONIC-DISCRIMINANT-AND-JUMP-STRATA.md (blob 7e065fa886a62883cbf394bbf07aba542ff7302e). Its proof supplies the actual Steiner, Serre-duality, symmetry, and multiplication interfaces used above.

No selected HM coefficient, matrix-rank evaluation, scan, or experiment is used. The rank-one smooth-domain intersection, the actual odd and positive full-adjoint boundary maps, and exact twist-four corank remain undecided here.
