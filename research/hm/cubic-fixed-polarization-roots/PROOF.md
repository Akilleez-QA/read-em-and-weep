# Fixed-central-root recovery from high-power polarizations

Work over C. This concerns the abstract cubic-image fourfold V=V51 with L0=O_V(1), not a selected original HM/source instance. Fix an integer m>=1.

## Pinned inputs and scope

All PRs below belong to https://github.com/Akilleez-QA/read-em-and-weep.

- PR611 at 12b28d33627cc0e8b283d142dc16439a51bb5e00: V is integral projective, h0(O_V)=1, h1(O_V)=60, H2(O_V)=0, and L0 is ample.
- PR614 at 73fbf75838c91804ca637b5916d6aac217240958: H0(Theta_V)=0, h1(Theta_V)=576, and the marked abstract Artin deformation functor is unobstructed by local gluing.
- PR615 at 24bc9b741c287f8ac207bd9df4de4c07c50bea2f: polarized tangent spaces fit the Atiyah-symbol sequence; h0(L0)=10 and h1(L0)=65.
- PR628 at f08ff9c2760e4aef074cfe716b923d29d5e7ebe8: compatible polarized formal systems are effective over C[[t]].
- PR630 at 8024882d2129142fece5dbaf83b49e5f8e3817ca: finite original-polarized jets admit curve realizations; nonzero abstract first-order motion forces generic h0(L)<=9.
- PR631 at 4954b42e25592cf4b66a28d6a232fbe6b528f72e: for M0=L0^m very ample with H1(M0)=0 and n=h0(M0), the high-power embedded deformation functor maps formally smoothly to Def_(V,M0), with relative tangent dimension n^2-1. The pair functor maps formally smoothly to Def_V with relative tangent dimension 60. Its tangent dimension is 636; the Hilbert germ dimension is n^2+635.

The new point is that fixing the central root L0 makes passage to its m-th power lose no infinitesimal polarized information. This does not assert existence or uniqueness of roots globally on an algebraic curve.

## 1. Constants and units on every Artin deformation

Let A be a local Artin C-algebra with residue C and X_A a proper flat deformation of V, with specified special-fiber identification. Then the canonical map

    A -> H0(X_A,O_X_A)

is an isomorphism.

Here is a proof that does not assume cohomology-and-base-change surjectivity. Constants inject: a stalk at any point of the nonempty special fiber is a faithfully flat A-algebra, since it is flat and its reduction modulo the maximal ideal is nonzero. Thus A injects into this stalk, and hence into global sections. Induct on the length of A. For a small quotient A -> B with kernel J annihilated by the maximal ideal, flatness gives

    0 -> O_V tensor_C J -> O_X_A -> O_X_B -> 0.

Taking H0 and using h0(O_V)=1 shows that the C-dimension of H0(X_A,O_X_A) is at most dim_C J + dim_C H0(X_B,O_X_B)=length(A). The injection of constants gives the opposite inequality, proving the assertion. Properness supplies finite-dimensionality; alternatively the same exact sequence proves it inductively.

Consequently the global units are exactly A*, and they surject under every Artin quotient A -> B. In particular, in the Picard exact sequence for a small extension the units boundary vanishes, and

    ker(Pic(X_A) -> Pic(X_B)) = H1(O_V) tensor_C J.

The equality is the canonical identification supplied by the exact sequence, not an unjustified omission of a units quotient. See the units sequence in [Stacks 0C6Q](https://stacks.math.columbia.edu/tag/0C6Q). Multiplication by m is bijective on this kernel.

## 2. The fixed-root lifting theorem

For a fixed X_A, let Pic_(L0)(X_A) mean isomorphism classes of line bundles equipped with an identification of their restriction to V with L0. Define Pic_(L0^m)(X_A) similarly. Then tensor power induces a natural bijection

    Pic_(L0)(X_A) -> Pic_(L0^m)(X_A).

More precisely, suppose A' -> A is a small extension, X' is a specified abstract lift of X_A, L_A is specified, and M' lifts L_A^m with its specified power identification on X_A. There is a root L' lifting L_A whose m-th power is M'; its marked class is unique.

Proof. The obstruction delta(L_A) to lifting L_A lies in H2(O_V) tensor J. Its m-fold multiple is delta(L_A^m), by naturality of the units sequence under tensor power. The prescribed M' makes this latter obstruction zero. Multiplication by m is invertible on that C-vector space, so delta(L_A)=0. This argument does not require H2(O_V)=0; that vanishing is needed for arbitrary line-bundle lifts without a prescribed power lift, as in PR631.

Choose any lift N of L_A. The discrepancy M' tensor N^(-m) lies in the Picard kernel of Section 1. There is a unique kernel class Q whose m-th power is this discrepancy. Then L'=N tensor Q has the required power. If two such roots restrict to the same class downstairs, their ratio lies in the same kernel and has m-th power trivial, hence is trivial. Induction from A=C proves the stated bijection and relative lifting assertion for all Artin quotients.

Markings cause no missing classes: every scalar change of a special-fiber line-bundle identification lifts through A* -> C*. Thus marked and unmarked line-bundle classes with this fixed restriction are in bijection. The construction is natural because pullback of a root is a root and its marked class is unique.

There is also a precise statement with chosen power isomorphisms. Given M_A with its central identification, consider triples (L_A,alpha,beta), where alpha:L_A|_V -> L0 and beta:L_A^m -> M_A restricts to the prescribed central power identification. Any two such triples over the fixed X_A admit a unique isomorphism respecting alpha and beta. Indeed a marked line-bundle isomorphism exists by the class assertion. Its failure to respect beta is a unit u in 1+maximal_ideal(A); multiply it by the unique m-th root of u (or its inverse, according to the discrepancy convention). This root exists uniquely by the finite logarithm/exponential series. The only automorphism preserving both alpha and beta would be u in 1+maximal_ideal(A) with u^m=1, so it is 1.

By contrast, forgetting beta leaves scalar automorphisms 1+maximal_ideal(A) for a marked line bundle. Without the central marking even a root with beta has the usual constant m-th roots of unity as automorphisms. No assertion of triviality of an unrigidified polarized automorphism group is intended.

## 3. Equivalence on marked pair deformation classes

Let Def_(V,L0)(A) classify marked pair deformations up to marked pair isomorphism; define Def_(V,L0^m) in the same way. The power map is a natural isomorphism of these set-valued functors, commuting with their maps to Def_V. In particular it is formally etale: the map on the usual lifting fiber product for every small extension is bijective.

For surjectivity apply Section 2 on any representative of the underlying marked scheme deformation. For injectivity, pull one root back along a given marked scheme isomorphism between the powered pairs and use root uniqueness on that fixed scheme. This argument needs no arbitrary choice of an identification between distinct scheme representatives. H0(Theta_V)=0 additionally says that a marked scheme has no identity-reducing automorphisms: at each small extension their kernel is H0(Theta_V) tensor J=0. Induction makes the fixed-representative interpretation of fibers over Def_V unambiguous.

On tangent spaces the power map acts by multiplication by m on the 60-dimensional Picard subspace and by the identity on the 576-dimensional abstract quotient. Equivalently its diagram on the Atiyah-symbol tangent exact sequences has left arrow m and right arrow identity. It is therefore an isomorphism on the full 636-dimensional pair tangent spaces, in agreement with the all-orders theorem. No canonical splitting of these sequences is claimed.

## 4. Original-polarized meaning of the high-power Hilbert germ

Choose m and n as in PR631. Compose its high-power forgetful map with the inverse isomorphism of Section 3. This gives

    Def_emb,m -> Def_(V,L0) -> Def_V.

The first map is formally smooth with relative tangent dimension n^2-1; the second has relative tangent dimension 60. Thus a prescribed high-power embedding over A extends over every prescribed original-polarized pair lift over A', after a small extension. Its source remains the smooth Hilbert germ of dimension n^2+635, and it still reaches all 576 abstract tangent directions.

This improves the interpretation of a single high-power Hilbert germ: after fixing its central root it captures all original-polarized formal deformations, not merely the powered pairs. It does not recover the ten original degree-one sections. Their lifting obstruction remains, and PR630's section-loss conclusion still applies. The original P9 embedded rigidity and the high-power lifting theorem are therefore compatible.

## 5. Compatible formal roots and effectivity

Let A_r=C[t]/(t^(r+1)), and let X_r be any compatible flat high-power embedded system with X_0=V in the fixed complete M0 embedding. Put M_r=O(1)|_(X_r), with its compatible transition identifications. Fix the central root L0 and its power identification. Section 2 gives root triples at every order, unique up to unique isomorphism. Their reductions are the corresponding lower-order triples, so their unique comparison maps give compatible transition isomorphisms automatically. Thus the entire given embedded system has a unique compatible marked formal root system in this precise rigidified sense, not merely unrelated roots at individual orders.

Every L_r is ample, since its reduction L0 is ample and the thickening is nilpotent. Applying the polarized effectivity theorem used in PR628, [Stacks 0D4T](https://stacks.math.columbia.edu/tag/0D4T), produces a proper flat finitely presented X over C[[t]] with an ample line bundle L inducing this root system. It is projective over this Noetherian affine base. Its formal powered pair is the prescribed (X_r,M_r), with the compatible chosen power isomorphisms. This conclusion requires no assertion that a root exists on an arbitrary finite-type curve carrying a related high-power family.

Furthermore, for each finite N, PR630 realizes this recovered original-polarized jet on a smooth pointed algebraic curve. That curve and family may depend on N; no descent of the whole initial formal arc is claimed. The root theorem sharpens formal information, while the two-consecutive-power construction in PR630 remains a direct way to retain the original line bundle on a whole approximating curve.

## Contribution and boundaries

The new dependency is closed: a single sufficiently high-power embedded formal deformation, with the central root fixed, canonically determines the original polarized formal deformation class. The proof handles global units, arbitrary small extensions, central markings, scalar automorphisms, and compatible systems explicitly. It also shows that the prescribed-power root-lifting step itself does not need H2(O_V)=0.

This is an authored mathematical proof conditional on the pinned inputs, not proof-assistant verification. It asserts neither global Picard root existence/uniqueness away from the formal neighborhood, nor generic-fiber automorphism rigidity, nor preservation of original sections. The original HM/full-adjoint/source-instance/higher-lifting/Weil-class algebraicity questions remain separate. No selected source evaluation or large computation is used.
