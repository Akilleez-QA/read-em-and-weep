# No hyperplane torsion and uniform six-to-ten root cohomology

## Corollary

Let T=P(W*) be the actual negative hyperplane pencil and P=P(Sym^2 W) its negative-quadratic parameter plane. The actual cokernel

    C_lin=coker[44 O_T(-1) -> 46 O_T]

is a globally generated vector bundle of rank five and degree 26. In particular its previously possible exceptional torsion length is

    j=0.

Let Z subset T x P be the universal length-two root scheme, with projections eta:Z->T and nu:Z->P. Then the actual quadratic cokernel is the rank-ten vector bundle

    C_quad=nu_*eta*(C_lin(1)).

Its Chern classes are c1=26h and c2=351h^2. With K=nu_*O_Z(-5), the actual global sequence is an exact sequence of vector bundles

    0 -> A tensor K -> 44 O_P(-1)
      -> 48 O_P -> C_quad -> 0.

It commutes with arbitrary base change. For EVERY nonzero negative quadratic q, including a doubled root supported at any of the twelve order-five parameters,

    h0(B_Dq(4))_-=6,       h1(B_Dq(4))_-=10.

Thus all former good-root restrictions are unnecessary for these cohomology and bundle statements. This does not determine the rank of the positive-direction smoothing map.

## Proof and exact dependencies

[SPECIAL-HYPERPLANE-ADJOINTS-ARE-EXACTLY-SQUARES.md, pin 5ce98e6bef1fd849353f563b1ccfc62f4d28b8d9](https://github.com/Akilleez-QA/read-em-and-weep/blob/5ce98e6bef1fd849353f563b1ccfc62f4d28b8d9/research/hm/order-four-quadratic-load/SPECIAL-HYPERPLANE-ADJOINTS-ARE-EXACTLY-SQUARES.md), together with the earlier nonexceptional result, proves h0(B_Ht(3))=3 at every t, entirely even.

[EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md, pin ff324d0d7f07300adbb9b6e830c3eecfa54eaa61](https://github.com/Akilleez-QA/read-em-and-weep/blob/ff324d0d7f07300adbb9b6e830c3eecfa54eaa61/research/hm/order-four-quadratic-load/EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md) gives the actual kernel A O_T(-6) and the base-change sequence

    0 -> (A O_T(-6)) tensor k(t)
      -> H0(B_Ht(3))_+
      -> Tor_1(C_lin,k(t)) -> 0.

The first two spaces have dimension three, so the Tor term vanishes at every point. Over each local DVR this excludes every torsion elementary divisor. Hence C_lin is locally free, with the already computed rank five and degree 26. Its presentation makes it globally generated. Equivalently, the hyperplane multiplication has constant rank 41, and its two-term complex is locally split into its kernel, image and cokernel. This proves arbitrary base change, not only base change to reduced points.

[QUADRATIC-TARGET-FROM-HYPERPLANE-TORSION.md, pin 998b46a1da4e1c168fb941e103d6a24f08e6ee5a](https://github.com/Akilleez-QA/read-em-and-weep/blob/998b46a1da4e1c168fb941e103d6a24f08e6ee5a/research/hm/order-four-quadratic-load/QUADRATIC-TARGET-FROM-HYPERPLANE-TORSION.md) proves the actual root-transform identity for C_quad, including nonreduced roots. Since eta* C_lin(1) is locally free and nu is finite flat of degree two, its pushforward is locally free of rank ten.

[GLOBAL-NEGATIVE-QUADRATIC-KERNEL-BUNDLE.md, pin 5845de0df879b57dafcbd91bff18e4f1c04e06bf](https://github.com/Akilleez-QA/read-em-and-weep/blob/5845de0df879b57dafcbd91bff18e4f1c04e06bf/research/hm/order-four-quadratic-load/GLOBAL-NEGATIVE-QUADRATIC-KERNEL-BUNDLE.md) proves the actual kernel A tensor K and the conductor comparison on every root scheme. Its cokernel is now known locally free everywhere, so the quadratic multiplication has constant rank 38 and the same local splitting argument gives arbitrary base change. The stated dimensions follow. In particular, a double exceptional root contributes the full length-two fiber of the rank-three square bundle and no extra Tor term.

The previously computed Grothendieck class remains

    ch(C_quad)=10+26h-13h^2.

Now it is the class of an everywhere locally free bundle, giving c2=(26^2+26)/2=351. No new rank hypothesis enters this conclusion.

## Smooth-quadric qualification

The global positive-direction obstruction is consequently a bundle morphism on all of P,

    (A tensor K) tensor Sym^2 V* tensor O_P(1) -> C_quad.

It remains unevaluated. At a double negative root, adding only a positive quadratic never produces a smooth quadric: the negative block has rank one and retains its nonzero kernel, so the block-diagonal form on V directsum W has rank at most 3+1=4. A smooth even quadric requires both a rank-three positive block and a rank-two negative block. The doubled-root cohomology and Hermite-jet formulas are valid without implying a smooth positive-block-only deformation.
