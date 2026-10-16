# Twenty constant scalar maps already form a complete minimal family

**Conclusion:** over the rationals, the explicit family below has exactly the same cohomological kernel as all thirty constant scalar maps. It therefore separates the actual 32-dimensional epsilon sector under the published geometric membership hypotheses. Twenty is the minimum number of constant scalar maps that can do so. This is a theorem about the family of maps; its values on the complete corrected obstruction remain missing.

## Precise meaning of the derived relation

Let K be the pinned perfect line complex on P4 and B=End(K). The supertrace pairing is a perfect pairing of complexes, giving B-dual isomorphic to B. Each constant scalar row is a global chain map

    lambda : B -> O(-2)[2].

The shift [2] places the sole target term in internal degree -2. Consequently

    Hom_D(P4)(B,O(-2)[2])
      = H^2(P4,B-dual(-2))
      = H^2(P4,B(-2)).

This identifies the class of the scalar map with its supertrace-dual hypercohomology class. It does not identify arbitrary constant coefficient rows with classes: the row must first satisfy its chain-map equation.

Write

    L_(i,b)(X) = X13[i,b]
                 - sum_(a,k) gamma[i,a,k] X02[a,5b+k].

These thirty rows are precisely the constant chain-map basis at source pin P. Let K_j be the positive kernel cycles in the independent twist-minus-two certificate at pin H, with j=15b+i. The explicit orientation is

    str(X K_j) = -L_(i,b)(X).

The Hom directions must be reversed when making this identification. A uniform shift of the resolution changes a common sign, not the relations.

The authenticated d5 image at H gives the ten hypercohomology relations

    [K_r]+[K_(25+r)] = 0,
    [K_(10+r)]+[K_(20+r)] = 0,       r=0,...,4.

Therefore the corresponding scalar morphisms satisfy, in the derived category,

    [L_(r,0)] + [L_(10+r,1)] = 0,
    [L_(10+r,0)] + [L_(5+r,1)] = 0.

A zero hypercohomology class here means **zero derived morphism**. It does not assert that the original polynomial chain map vanishes pointwise, or that there is a global homotopy inside the original unaugmented complex of global sections. The higher-Cech zigzag is allowed and is essential.

## Pullback and all scalar output coordinates

The symmetric-product map rho:(P1)^4 -> P4 is finite flat. Pullback, followed by tensoring with the full-sign deck line O(-2,-2,-2,-2), preserves these zero derived morphisms. The source becomes the full-sign End complex; the target is O(-4,-4,-4,-4)[2]. Hence each relation induces the zero map

    H^2(full-sign End complex) -> H^4(O(-4,-4,-4,-4)).

The target has 81 harmonic Laurent coordinates. The relation thus holds simultaneously in **all 81 coordinates**, in the same authenticated target frame. It is not restricted to a chosen test polynomial or to the epsilon sector.

This is the same scalar cohomology map used by the finite S rows: the negative harmonic input is in Cech degree four and internal degree minus two, and the global scalar row selects that component. Higher perturbation corrections increase internal degree and cannot contribute to this scalar row. Positive inputs are killed. Source `structural-relations.md` likewise defines S on the negative block alone.

## Explicit complete family and omitted-map reconstruction

Take the twenty indices

    I20 = {(i,0): 5 <= i <= 10}
          union {(i,1): 0 <= i <= 14 and i != 5}.

This contains both old maps up to sign:

    L = -L_(10,0),       Lminus = -L_(10,1).

Every omitted map is recovered cohomologically by one of these identities:

    L_(i,0) = -L_(10+i,1),     i=0,...,4;
    L_(i,0) = -L_(i-5,1),     i=11,...,14;
    L_(5,1) = -L_(10,0).

There are five plus four plus one omitted maps. Therefore the 20-map family and the 30-map family have identical common kernels on the entire full-sign H^2.

The published all-30 kernel is the 20-dimensional pure-positive subspace. Its classes have global constant Cech-degree-zero representatives fixed by factor permutations. It is the trivial D8 representation. Its intersection with the nontrivial epsilon sector is zero in characteristic zero. Thus I20 is complete on that sector.

The independent P4 block bound is

    rank of m constant scalar maps on epsilon
      <= min(20,m)+min(10,5m)+min(2,15m).

For m<20 this is less than 32. Since I20 is complete, the lower bound is attained: it is a **minimal family in number of constant scalar maps**.

## What this changes operationally

No selection of the remaining ten and two rows is needed to establish completeness of the family I20 with all its scalar output coordinates. A source-authenticated zero for all 20 images would prove the actual epsilon class is zero. Two old scalar images, even if fully authenticated, remain insufficient.

This does not supply 32 independent individual output rows. The earlier small-P4 selection remains useful to reduce evaluation: 20 Q^2 tests, ten selected v_k Q tests, and two selected v_k v_l tests. The missing ten-plus-two labels and their rank certificates are still required for that narrower 32-only evaluation plan. Nor does the present theorem regenerate any source polynomial or repair an incomplete source comparison.

All applications to the actual class retain the complete corrected Rsharp, source-order, owner, frame, gerbe-baseline and regular-comparison requirements. No obstruction value has been computed.

## Pinned sources and validity

- P=`08b73637d4136f91606aad332c46cafd064417f8`: `research/hm/current-scalar-proof/structural-relations.md`, sections 3-4; `map-and-comparison.md`, section 1. The former identifies the entire all-30 kernel, including explicit vanishing on all pure-positive classes.
- H=`e6e8d272e760a432dbbc1053b88c8eae03a47304`: `research/hsd/twist-minus2-d5/NOTE.md`, Result; `certificate.py`, `decode80/index80` and printed kernel/d5 data. The note supplies the ten disjoint unit relations.
- S=`f968b53943ba2312f09fbc3e8f9d462e86bcaa34`: `research/hm/d8-small-certificates/p4/Perfect-Complex-D8-F3.md`, sections 1-4, for perfect self-duality, finite-flat projection and small cohomology dimensions. Its characteristic-three perfect-complex statements are not being used to assert characteristic-three obstruction geometry.
- PR1 comments `6130352358` and `6130391535`: characteristic-zero geometric epsilon membership and dimension 32. Comments `6205127744`, `6205249609`, `6205660472`: corrected representative and regular source binding.

This deduction was independently challenged at the morphism/shift, supertrace, pullback and cohomological-output levels by V07. The previously accepted D01 basis/orientation review supplies an independent check of its explicit coordinate premise. No finite matrix or physical-source run was used.
