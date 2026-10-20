# Universal-plane deformation bundle and the exact H¹(U,V(-3)) recipient

## Result

Let U⊂P²_h be the nonempty open of stable planes established in RESULT.md. Let m:P²_z×P²_h→P⁴ multiply binary quadratics, let E=m*HM, and let s:P²_z×U→U be projection. Define

    W=R¹s_*End(E),
    V=R¹s_*(End(E)⊗O_z(-3)).

Both W and V are locally free of rank 12. Relative Serre duality identifies V with W*, after the fixed standard identification ω_P²≅O(-3). More intrinsically, replace O_z(-3) by ω_s and the duality is canonical without a choice of determinant trivialization.

The rank-12 sheaf V₁₂ on the elliptic good base B° from DECK_ADDENDUM.md is the pullback p_base*V. Filtering its H¹ by full base deck sign and base-swap odd parity gives precisely

    H¹(U,V⊗O_h(-3)).

This is an exact cohomological recipient for the restrictions of the stipulated global full-deck-sign classes odd under both inner swaps. It is not a computed value, a dimension bound of twelve, or a vanishing theorem. Block exchange remains a comparison between two fibrations and their respective good loci.

## 1. The actual universal family

Set Z=P(Sym²V₀) and H=P(Sym²V₀), two copies of P² for a fixed two-dimensional binary-form space V₀. Multiplication of two nonzero binary quadratics never vanishes identically, so it defines the everywhere-defined morphism

    m:Z×H→P(Sym⁴V₀),   ([g],[h])↦[gh].

The fiber map over h is the linear embedding i_h already proved. In particular m*O_P⁴(1)=O_Z(1)⊠O_H(1), but this bidegree introduces no additional base twist into the relative canonical bundle ω_s: s is a product projection, so ω_s=pr_Z*ω_Z.

Define the locally free family E=m*HM on Z×U and A=End(E). Its fiber A_h=End(E_h) has h⁰=1,h¹=12,h²=0, for every h∈U. The twisted fiber A_h(-3) has h⁰=0,h¹=12,h²=1. These are the stable-plane calculations in DECK_ADDENDUM.md. Consequently both R¹ direct images are locally free of rank 12 and commute with base change. This conclusion does not require a fine moduli space or a universal bundle on a global moduli space: E itself is the explicit family needed here.

## 2. Relative Serre duality and trace

The trace pairing canonically identifies A*≅A. Relative Serre duality for the smooth proper relative surface s gives perfect pairings

    R¹s_*A ⊗ R¹s_*(A⊗ω_s) → R²s_*ω_s → O_U.

Thus

    R¹s_*(A⊗ω_s) ≅ (R¹s_*A)* = W*.

Choosing once the usual identification ω_Z≅O_Z(-3) yields V≅W*. If projective space is kept without a basis/determinant trivialization, the identification of ω_Z with O_Z(-3) includes a constant one-dimensional determinant factor. This is a constant line, not an O_H(k) twist; retaining ω_s everywhere makes the assertion completely canonical. The fixed coordinate conventions allow the displayed O(-3) notation.

Replacing A by A₀=End₀(E) makes no difference to either R¹ bundle, because

    H¹(P²,O)=H¹(P²,O(-3))=0.

It also removes the scalar R⁰ and R² terms from the corresponding relative complexes. In particular the rank-12 description is genuinely tracefree in deformation degree one.

Fiberwise W_h=Ext¹(E_h,E_h) is the ordinary infinitesimal deformation space of the plane bundle, and V_h is its dual. Since Ext²(E_h,E_h)=0, these plane-bundle deformation spaces have no ordinary obstruction at this point. One may therefore call V the family of cotangent deformation spaces. It is **not** Ω_U: its rank is 12 whereas dim(U)=2. The family has a Kodaira–Spencer map T_U→W, hence a dual map V→Ω_U after the stated duality convention. Neither map is asserted injective or surjective, and no global fine-moduli identification is needed or claimed.

## 3. Pullback to the elliptic parameter surface

Let t=p_base:C₃×C₄→H be the fixed degree-eight elliptic symmetric-square cover and B°=t^(-1)(U). The bundle on the original fourfold is, up to the irrelevant line twist N, obtained from E by applying the corresponding degree-eight map p_fiber:C₁×C₂→Z and t on the two factors.

In End(F) the line twist cancels canonically. The fiber-full-deck-sign/inner-swap-odd finite pushforward summand is exactly A⊗O_Z(-3), with no base twist, by the equivariant decomposition proved in DECK_ADDENDUM.md. Its higher direct image after base change is therefore

    V₁₂ ≅ t*V.

The relevant base-change map is an isomorphism: s is projective and smooth, A(-3) is flat over U, its cohomology dimensions are constant, and the computed R¹ is locally free and universally base-change compatible. Also t is finite flat; either criterion supplies the needed flat base change.

## 4. Base deck and base swap filtering

Because t:B°→U is finite, t_* is exact on quasi-coherent sheaves and has no higher direct images. Projection formula gives

    H¹(B°,t*V) ≅ H¹(U,V⊗t_*O_B°).

The decomposition of t_*O is the same geometric one as for the fiber cover, restricted to U. In the base-full-deck-sign character, it is

    O_H(-2)_(base swap +) ⊕ O_H(-3)_(base swap −).

The sheaf t*V has its pullback linearization: the base deck involutions and base swap act trivially on the quotient H and hence on V. Their action in the displayed projection formula is consequently carried by t_*O alone. Selecting odd parity under the base swap therefore gives exactly

    H¹(B°,t*V)_(base deck 11, base swap −)
        ≅ H¹(U,V⊗O_H(-3)).

No extra Koszul sign occurs in this finite pushforward calculation. The actual action on derived cohomology is induced from the indicated equivariant sheaves. In particular both inner-swap signs are already accounted for, once in defining V from O_Z(-3) and once in selecting O_H(-3).

Combining this with the natural equivariant Leray isomorphism yields an exact identification of the subgroup of H²(r^(-1)B°,End₀F) with full deck sign and negative parity under both inner swaps with H¹(U,V(-3)), within the subgroup preserving this fibration.

## 5. What remains outside this reformulation

The block exchange (13)(24) exchanges the fiber and base projections. It sends r^(-1)B° to the analogous good locus for the other projection, which need not be the same open subset of X. Hence it does not automatically define a sheaf endomorphism of V or an involution of this one H¹(U,V(-3)) presentation. A global D8-equivariant class satisfies a compatibility relation between the two restricted presentations, including their overlap. That relation has not been computed here.

Moreover restriction from global H²(X,End₀F) to this good-locus group need not be injective. Classes lost on restriction and extensions across the exceptional parameters remain possible. The identification does not evaluate H¹(U,V(-3)); U need not be affine, and the cohomology dimension has no bound coming solely from rank(V)=12. All thirty global obstruction values remain unknown.

This derivation is a static-geometry argument. No physical source or jet values are evaluated in this argument. It retains the supplied physical-bundle and equivariance identifications as premises.
