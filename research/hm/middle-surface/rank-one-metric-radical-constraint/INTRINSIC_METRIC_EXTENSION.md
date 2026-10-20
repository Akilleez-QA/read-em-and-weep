# Intrinsic ternary metric extension through every residual-rank drop

## Theorem and assumptions

Let X be an integral variety over C. Let V have dimension five, let f:V³→J be one fixed outer-symmetric cyclic-zero trilinear operation, and assume every repeated map A_u:V/Cu→J is injective. Suppose regular subbundles

    U⊂H⊂V⊗O_X,        rank U=1, rank H=4

are given, with U the middle line and E=H/U. On a dense open assume that the residual kernel is a five-dimensional hyperplane K⊂Sym²E and that its correction is supported in E. These are precisely the good-family and support-extension hypotheses imported from the earlier proofs; this theorem does not prove extension of H.

Then there is a canonical rank-one quotient h:Sym²E→M on all of X whose kernel extends K. The projective ternary metric therefore extends uniquely over X, including arbitrary actual residual-rank drops. No normality or smoothness is required for this intrinsic construction once H is regular. Every fiber of the projective metric graph over X is a single point; indeed the graph is isomorphic to X.

## 1. The smaller repeated-image quotient

Restrict the repeated-input bundle map to E:

    A_H:U²⊗E→J⊗O_X.

This is well-defined without a splitting of H→E: adding a multiple of u to an argument changes nothing because f(u,u,u)=0. It has constant rank three by repeated injectivity. Its image I_H is a rank-three subbundle, and J_H=(J⊗O_X)/I_H is locally free.

Choose locally a splitting s:E→H and define the symmetric middle-linear map

    Φ_s:U⊗Sym²E→J_H,
    u⊗ab ↦ f(s(a),u,s(b)) modulo I_H.

Under s→s+d, where d:E→U, the change consists of the two terms A_u(d(a)b) and A_u(d(b)a); both belong to I_H. The term with two added middle vectors vanishes. Thus the local Φ_s glue to a canonical map Φ, independent of all splittings.

This quotient is by the three supported repeated directions, not by the full four-dimensional repeated image. That distinction retains the supported-correction condition within the intrinsic map itself.

## 2. Generic rank one bounds the rank everywhere

On the dense good open, the supported correction identity places U⊗K inside ker Φ. Hence rank Φ≤1 there. Rank Φ cannot be zero there, as will follow at every point from Section 3. Alternatively its quotient to the ordinary residual target is the nonzero rank-one restriction of Q to Sym²E, so rank Φ=1 there directly.

Every coefficient of Λ²Φ is a regular function locally. It vanishes on a dense open, and X is integral, so Λ²Φ=0 identically. Consequently rank Φ≤1 everywhere, with no hypothesis that the actual residual kernel has constant dimension.

## 3. Rank zero contradicts the universal quadratic eigenline obstruction

Suppose Φ vanishes at a geometric point x. Trivialize U_x and choose a splitting of H_x. By definition, every middle numerator f(s(a),u,s(b)) lies in I_H,x=A_u(E_x). Since A_u is injective, there is a unique linear correction

    W:Sym²E_x→E_x

with f(s(a),u,s(b))=A_u(W(ab)) for all a,b∈E_x. Every square now lies in the actual residual kernel. Repeated injectivity, outer symmetry and cyclic zero imply

    W(r²)∉Cr for every r≠0.                              (1)

For completeness, if W(r²) were proportional to r, the identity f(r,u,r)=−2A_r(u) would make A_r(u) proportional to A_u(r). The repeated-input pencil argument excludes this: for independent u,r those two repeated values are independent, or a repeated map at an appropriate nonzero pencil vector would have a nontrivial kernel.

But no quadratic map W on a three-dimensional space can satisfy (1). On P(E_x)=P², with tautological line O(−1) and quotient bundle Q of rank two, W induces a section of Q(2). Its zeros are exactly the lines Cr with W(r²)∈Cr. If it had no zeros, its top Chern class would be zero. Yet, writing H for the hyperplane class,

    c1(Q)=H,   c2(Q)=H²,
    c2(Q(2))=H²+2H·H+4H²=7H²≠0.

This contradiction excludes rank zero at every geometric point. Together with Section 2, Φ has constant rank one.

## 4. Canonical metric and correction

A constant-rank-one map of vector bundles has a line-bundle image L⊂J_H and a locally free rank-five kernel. Define

    M=L⊗U*,
    h:Sym²E→M

by untwisting the surjection Φ:U⊗Sym²E→L. It is a surjection everywhere. Its kernel agrees with K on the dense good open, so its projective class is exactly the original ternary metric and extends it canonically.

On K_h=ker h the original numerator lies in I_H. Inverting A_H there gives a regular supported correction K_h→E⊗U in local splittings, with the usual shear transformation law. Thus its regularity and supportedness at rank drops follow directly here, without first resolving a projective metric graph.

The graph of this everywhere-defined section of the separated relative projective metric bundle is closed. Its dense good-locus graph therefore has this entire graph as its reduced closure. In particular the projective metric graph is isomorphic to X, not merely finite over X.

## Consequences and remaining boundary

Apply the theorem to the normalized middle surface once the independently established support-finiteness argument has extended H. The projective metric line bundle M is then defined directly on that normal surface. On the generically nondegenerate metric branch, its determinant defines the effective Cartier divisor Δ. The extension theorem itself also applies to generically rank-two or rank-one metrics; it does not exclude those branches or assign them a determinant divisor when the determinant vanishes identically. A metric-graph resolution is unnecessary for extending h. The canonical complement can still fail to extend at rank-one metric points: its determinant-cleared covector may have a coefficient base ideal there, and resolving that ideal can introduce exceptional curves. The theorem eliminates metric indeterminacy, not complement indeterminacy.

The rank-one radical Picard identity in PROOF.md applies to every complete rank-one curve after normalization and is an independent further restriction. Together these conclusions still do not exclude the remaining middle surface. Rank-two boundary divisors, and rank-one boundary divisors satisfying that identity, remain possible under the presently proved restrictions.

 The proof uses only actual-family identities, repeated injectivity, constant-rank bundle algebra, and the universal Chern class of Q(2).
