# Standard semiregularity is blind to the current fourfold retained sector

## Conclusion and conditional scope

For X=C^4, with C the elliptic double cover and the genuine factor-permutation action, the full-deck-sign part of the standard bundle semiregularity target is exactly

    [direct sum_{q>=0} H^{q+2}(X,Omega_X^q)]_F
        = H^3(X,Omega_X^1)_F
        = sign tensor permutation_4 = sign direct sum (V tensor sign).

It has dimension 4 and contains no U22. Consequently, assuming the supplied coherent Gdeck semidirect S4 linearization of the classical bundle E and the supplied Ext decomposition, standard semiregularity vanishes identically on its U22 isotypic component. That component has dimension 60 (30 copies of the two-dimensional U22). In particular it vanishes on the retained 30-dimensional space of D8-epsilon lines described in the supplied corrected alternating-boundary reduction.

Thus applying this standard map gives no constraint on those 30 remaining coordinates and cannot prove their vanishing through semiregularity injectivity. This proves a limitation of this map, not vanishing or nonvanishing of the actual obstruction. This is the current FOURFOLD retained-sector test, not the separate PR77 eightfold self-pair rank test.

## 1. Definition, q range, and naturality

For a smooth complex projective X and a bundle (more generally a perfect object) E, the standard components have the form

    sigma_q(x) = (-1)^q tr(At(E)^q composed with x)/q!
    Ext^2(E,E) -> H^{q+2}(X,Omega_X^q),  q>=0.

Changing the Atiyah-class sign convention removes the displayed (-1)^q and does not change kernels, characters, or the conclusion. The wedge of the cotangent factors is understood. The q=0 map is the ordinary trace. On a fourfold q>=3 has q+2>4 and therefore zero coherent cohomology; only q=0,1,2 matter. A degree-two Atiyah expression targeting H^4(Omega^2) must not be mistaken for the only component, and no q=-1 component belongs to this standard map.

Atiyah classes are natural under automorphism pullback; composition, exterior powers, and trace are natural as well. A coherent equivariant structure on E therefore makes every sigma_q equivariant for Gdeck semidirect S4. A merely non-equivariant isomorphism g*E≅E without the action coherences does not suffice to assert the supplied group representations. Here those coherences and the classical bundle identification remain supplied premises, not newly checked geometric certificates.

## 2. Independent character calculation

Write a_i for the one-form pulled back from factor i, and b_i for the H^1(O_C) generator pulled back from factor i. On an elliptic curve, inversion negates both H^0(Omega_C^1) and H^1(O_C). Thus both four-dimensional spans are copies of the same signed permutation representation W of Gdeck semidirect S4. Their cohomology satisfies

    H^r(X,Omega_X^p) = exterior^p W_a tensor exterior^r W_b.

This follows directly from product cohomology and the trivial cotangent bundle of the abelian variety. The wedge in W_b already incorporates the Koszul sign from permuting degree-one cohomology classes. The wedge in W_a incorporates the usual differential-form sign. There is no additional global permutation twist.

For increasing subsets A,B of {1,2,3,4}, a_A tensor b_B has deck character chi_{A symmetric-difference B}. Full deck sign F occurs precisely when A and B are disjoint complements. Necessarily p+r=4. In semiregularity r=p+2, so 2p+2=4, giving p=1 and r=3 uniquely.

As dimensional checks:

- H^2(O_X) has dimension 6, all of deck weight 2, and no F part.
- H^3(Omega_X^1) has dimension 16: its F part has dimension 4; its remaining dimension 12 consists of two dimensions for each of the six weight-2 characters.
- H^4(Omega_X^2) has dimension 6, all of deck weight 2, and no F part.

For the permutation sign, define

    v_i = (-1)^(i-1) a_i tensor (b_1 wedge ... wedge b_(i-1)
                               wedge b_(i+1) wedge ... wedge b_4).

Then a factor permutation s satisfies

    s(v_i) = sign(s) v_{s(i)}.

Indeed the complement wedge has the sign determined by moving its omitted index to the first position; the displayed (-1)^(i-1) exactly converts it to the full four-index permutation sign. Equivalently, exterior^3 W_b = W_b^* tensor det(W_b), and the four complementary monomials correspond to the diagonal tensors in W_a tensor W_b^*, tensored with det(W_b). The diagonal tensors form the ordinary permutation representation, while det(W_b) restricts to sign on S4 and full sign on Gdeck.

Therefore the full-sign S4 character, in classes (1),(12),(12)(34),(123),(1234), is

    (4,-2,0,1,0) = character(sign) + character(V tensor sign).

This proof uses only universal exterior algebra, not bundle matrices or model evaluations.

## 3. Consequence for the supplied Ext block and retained lines

The supplied decomposition is

    Ext^2(E,E)_F = 20 triv + 60 V + 30 U22 + 30 Vsign + 2 sign,

of total dimension 352. The equivariant map can have nonzero image only from its Vsign and sign isotypes. Schur's lemma gives

    sigma(20 triv + 60 V + 30 U22) = 0.

In particular the full-sign map has rank at most 4 and kernel dimension at least 348; this is an upper bound, not a computed rank. Its restriction to the entire U22 isotype is the zero map, a stronger conclusion than a dimension-count failure of injectivity on the 30 retained lines.

The D8-epsilon space supplied in this problem is 2 sign-lines plus one epsilon-line in each of the 30 U22 copies. After the two sign directions are removed by the supplied corrected alternating boundary, all remaining directions lie in the U22 isotype and remain in ker(sigma). This uses the supplied identification of the retained space, rather than inferring its representation solely from its dimension. The epsilon-space itself is not an S4-subrepresentation; the argument passes through its enclosing S4-isotypic component.

Under the supplied D8-epsilon character convention (epsilon occurs in sign and U22, and not in Vsign), the target epsilon multiplicity is only one. Thus even before boundary reduction the 32-dimensional epsilon source has semiregularity rank at most one. It would be incorrect to claim semiregularity itself eliminates the two sign directions: one target sign copy cannot detect two independent sign-source copies. Their removal is a separate imported boundary fact.

## 4. Dual and volume-form conventions

Using inverse pullbacks instead of pullbacks dualizes these finite-group representations. All S4 irreducibles here and the order-two deck characters are self-dual, so the conclusion and listed character are unchanged.

Equivariant Serre duality gives

    H^{q+2}(Omega^q)^* = H^{2-q}(Omega^{4-q}).

For q=1 this is H^1(Omega^3); its full-sign component has the same sign⊗permutation_4 character, by the same complementary-subset argument with p=3,r=1. There is no missing dual U22 component.

Although K_X is an ordinary trivial line bundle, its natural equivariant volume generator a_1 wedge ... wedge a_4 has character (F,sign). Replacing K_X by a trivially linearized O_X without retaining this twist produces incorrect characters. The direct wedge proof above avoids that mistake. Tensoring E by an equivariant line-character changes neither End(E) nor the natural conjugation action on its Ext groups; arbitrary independent retwisting of the target would not describe the same natural semiregularity map.

## 5. What the obstruction theorem does and does not supply

For a coherent sheaf on a smooth complex projective manifold, the modern standard semiregularity theorem says these maps annihilate all ordinary sheaf-deformation obstructions. Its statement is about deformation of the sheaf in that setting. Applying it to a module over a varying noncommutative or algebroid ambient deformation requires a separate comparison theorem; the ordinary theorem alone does not establish that extension.

Even if such a comparison supplies sigma(o)=0 for the present obstruction, this is automatic on the retained space, so it supplies no new equation there. A different invariant, a richer map not factoring through this sigma, or an independent existence/vanishing theorem is not ruled out. Higher components of an L-infinity enhancement do not make this particular linear map injective on its existing kernel.

## Primary sources

1. R.-O. Buchweitz and H. Flenner, A Semiregularity Map for Modules and Applications to Deformations, original preprint, introduction pp. 2–3 and semiregularity definition on PDF p. 28: https://arxiv.org/pdf/math/9912245 . The introduction explicitly defines the components using (-At)^q/q!, trace, and H^{q+2}(Omega^q); the general definition uses the cotangent complex.
2. R. Bandiera, E. Lepri, M. Manetti, L-infinity liftings of semiregularity maps via Chern–Simons classes, Advances in Mathematics 435 (2023), 109358, p. 3, Corollary 1.1 (=6.4): https://eprints.gla.ac.uk/333483/1/333483.pdf ; https://doi.org/10.1016/j.aim.2023.109358 . This states annihilation of all sheaf-deformation obstructions on complex projective manifolds.

## Inputs and scope log

Read the supplied deck-character-index-2044 and module-parity-0441 result documents for the existing Ext/retained-sector premises and equivariant-volume warning. Independently proved the target character with exterior algebra. Retrieved only the cited primary mathematical literature. No actual physical model, source, or jet evaluation; matrix products; production imports; or experiments were performed. No external posting occurred.
