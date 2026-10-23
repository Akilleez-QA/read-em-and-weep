# The forced unique-doublet subblock and the actual rank22 presentation

Work over C on T=P(W*) with its standard G=2I linearizations. All characters use the current convention. No selected actual HM/source coefficient, point, parameter, jet, derivative, matrix or instance rank is evaluated.

## 1. Immutable interface and new construction

The sole imported proof is RESIDUAL: PR1002, commit b691ab014afa0c546894dba5bcec396ed6694d5d, research/hm/canonical-residual-pencil/PROOF.md, authenticated in INPUTS.json. It supplies the actual canonical rank-four degree24 bundle Q and its fiberwise-injective presentation

    0→E24 O(-1) --Γ_Q--> H28 O→Q→0,
    E24=W⊕W'⊕2S⊕2T6,
    H28=1⊕2A⊕V⊕2P⊕2D.                            (1)

It also proves that the invariant complete-coefficient map is a map λ between two canonical lines. Nonzero λ is precisely the split canonical quotient C→O(2) case (rows9,10,14,15); zero λ is precisely the Euler case (rows17,18,20). Its actual value remains unselected.

We construct a further actual presentation

    0→E22 O(-1)→Z26→Q→0,
    E22=W'⊕2S⊕2T6,                                (2)

with a canonical locally free target Z26 of rank26 and degree2. The target has the following equivariant isomorphism types:

    λ≠0: Z26 ≅ (A⊕V⊕2P⊕2D) O ⊕ W O(1),
    λ=0: Z26 ≅ (1⊕A⊕V⊕2P⊕2D) O ⊕ O(2).         (3)

The constructions in (2) are canonical; the displayed direct-sum splittings in (3) are not claimed canonical. In particular the new source has no W summand. This is an actual further subbundle quotient, not a change of characters in (1).

## 2. The A coefficient image is forced to be nonzero

Let U⊂E24 be its unique W-isotypic subrepresentation. It is canonical because W occurs once. A linear map U O(-1)→H28 O is equivalent to a coefficient map U⊗W→H28, up to the determinant identification W*=W. Since

    W⊗W=1⊕A,

the restriction of Γ_Q to U O(-1) lands in the 1⊕2A isotypic part of H28. Its trivial component is the scalar gate λ, up to nonzero identifications of its source and target lines.

The A component cannot vanish. If it did, a rank-two bundle U O(-1) would map into the rank-one trivial target, contradicting the fiberwise injectivity inherited from (1). This is a rank obstruction for bundles, not evaluation of a selected fiber or matrix.

Since Hom_G(U⊗W,A) has dimension one, the nonzero A component selects an actual irreducible subrepresentation A_b⊂H28's two-copy A-isotypic part. Concretely it is the image of the A-isotypic coefficient map. This image is canonical, without a basis for the A multiplicity space. Let H1=H28^G denote the canonical trivial target line and put

    L4=H1⊕A_b ⊂ H28,
    R24=H28/L4 ≅ A⊕V⊕2P⊕2D.

The actual restriction factors through L4 O and remains injective on every fiber.

## 3. Universal classification of the rank-two block cokernel

Define the canonical vector bundle

    B2=coker[U O(-1)→L4 O].                        (4)

The map is a subbundle inclusion, so B2 is locally free of rank2 and degree2. Its type can be identified entirely by universal SL2 maps.

The multiplication map

    m:W O(-1)→Sym²W O=A O

is injective on each fiber: multiplication by a nonzero element of a one-dimensional tautological subspace is injective in the symmetric algebra. Its cokernel is O(2), giving the complete-evaluation sequence

    0→W O(-1) --m--> A O→O(2)→0.                  (5)

The other irreducible channel is the alternating projection W⊗W→Λ²W=1. After arbitrary nonzero identifications U≅W, H1≅1 and A_b≅A, the two components of (4) are the alternating channel with coefficient λ and the symmetric multiplication channel with a nonzero coefficient. This describes universal intertwining spaces; no actual coefficient is assigned a numerical value.

If λ=0, equation (5) gives

    B2≅O⊕O(2).

If λ≠0, scaling the two irreducible target channels separately identifies (4) with the tensor Euler inclusion

    W⊗O(-1) → W⊗W O=(1⊕A) O.

Indeed the tensor inclusion has nonzero symmetric and alternating projections, and each channel is one-dimensional. Tensoring 0→O(-1)→W O→O(1)→0 by W gives its cokernel W O(1). Hence

    B2≅W O(1)  when λ≠0.                          (6)

The scalar distinction is exactly the old λ gate, not an independently chosen parameter.

## 4. Quotienting the actual subbundle

Define

    Z26=coker[U O(-1)→H28 O].                      (7)

The source in (7) is an actual subbundle of H28 O because it is the restriction of the fiberwise-injective map (1). Thus Z26 is a vector bundle. The nested subbundles U O(-1)⊂E24 O(-1)⊂H28 O give the exact quotient sequence (2), with E22=E24/U. The source is fiberwise injective because its quotient Q is locally free. All maps in (2) are induced from Γ_Q; none is a replacement model.

Quotienting L4 O⊂H28 O by U O(-1) gives a canonical extension

    0→B2→Z26→R24 O→0.                             (8)

Both possible B2 types in Section3 have H1(B2)=0. Consequently Ext1(R24 O,B2)=0 ordinarily, and averaging a splitting gives a G-equivariant splitting. This proves (3), without choosing such a splitting to define (2). In particular any subsequent matrix expression relative to (3) must retain the actual choice of splitting and cannot declare an arbitrary off-diagonal component zero.

The ranks and degrees are

    rank Z26=28−2=26,    deg Z26=0−(−2)=2,
    rank Q=26−22=4,      deg Q=2−(−22)=24.

The target remains globally generated. Taking sections of (7) identifies H0(Z26)=H28 canonically, since H0(O(-1))=H1(O(-1))=0. Thus no global target sections have been discarded by this nonuniform-target reduction.

## 5. Contribution and scope

Fiberwise injectivity forces the actual A coefficient image of the unique W source to be nonzero. Removing that actual subbundle eliminates the last W source and yields the canonical rank22 presentation with the two explicit nonuniform target types (3). Its scalar distinction retains, rather than decides, the split/Euler alternative.

This does not cut the seven possible Q or C types, select λ, determine the top obstruction or vertex scalar, or change a source/frontier ledger. Its new content is the forced nonzero A channel, the identified rank-two block cokernel, and the inherited actual residual maps in (2). All arithmetic checks are fixed abstract representation and bundle identities.
