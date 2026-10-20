# Preserved mathematical audit

This review concerns the source manuscript and its stated assumptions. It is preserved as mathematical history, not a new independent certification of all publication edits or of unpublished input theorems. Source and publication hashes are recorded in SOURCE-HASHES.json. A split manuscript’s module or polar application remains conditional in its destination unit.

# Independent audit: double-conic conductor intersection

## Verdict

The proof passes independent review. The scheme intersection, nonsplitting safeguard, ribbon and Mayer–Vietoris sequences, relation-space filtration, cochain sign, and Euler and dimension bounds are correct. No actual splitting type, connecting-map rank, ambient obstruction value, or source is evaluated.

Read directly: this directory's PROOF.md; ../simple-pole-cofactor-comparison/PROOF.md; ../discriminant-normalization-conductor/PROOF.md; ../nullcone-normalization/PROOF.md; and ../conductor-cohomology-bounds/PROOF.md.

## 1. Intersection and twists

With the displayed coefficient conventions, substituting a universal quadratic square gives I=D² and J=−2D³. Restricting the ideal (I,J), rather than just its zero set, therefore gives (D²). The intersection is the Cartier double conic in W=P². It has degree 8 for O_Y(1)|W=O_P²(2), and its reduction has degree 4. A Cartier multiple of the smooth conic has no additional embedded points.

The ideal of C in E is I_C/I_C²=O_P²(−2)|C=O_P¹(−4). Since G|C=B_C(−4), its product with that ideal is B_C(−8). Thus the two twists in the canonical filtration are exactly −8 and −4.

## 2. Nonsplitting and the connecting map

The absence of a global retraction follows from the stated conormal sequence. Since the defining equation of E is D², its differential restricts to zero on C, giving Ω_E|C=Ω_P²|C. A retraction would split the conormal sequence. The restricted Euler sequence, twisted by degree 2 on P¹, has the complete conic linear system as its map on global sections. Its kernel has no sections, whereas the proposed split conormal sequence would have an O summand. This contradiction is valid.

It is essential to distinguish this nonsplitting of the ribbon from the rank of the bundle-valued cohomology map ε. The proof does so: no nonzero rank is inferred from the ribbon alone.

For B_C=O⊕O(d)⊕O(−d), set A=max(d−7,0), T=max(d−3,0). Direct line-bundle cohomology gives

    (h0(L),h1(L))=(A,21+A),
    (h0(M),h1(M))=(T,9+T).

The displayed formulas for G_E follow from exactness, retaining ρ=rank ε. The prior bound 0≤d≤20 gives A+T≤30, hence h0(G_E)≤30 and 30≤h1(G_E)≤60.

The further proposed bound is also correct:

    ker[H1(G_E)→H1(M)] = coker ε,
    dim ker =21+A−ρ ≥21+A−T ≥17.

The first equality means the canonical isomorphism supplied by the long exact sequence. Thus passage from E to C kills at least seventeen H1 directions. This is a statement before quotienting by the component H1 image. It does not prove that any such direction survives into D1 or into an ambient restriction image.

## 3. Mayer–Vietoris and relation filtration

For the reduced union, the scheme-theoretic component intersection gives the sheaf sequence with difference map. Tensoring by ambient locally free G is exact. The short exact sequences defining D0, K1, and D1 follow without a splitting, using H2(G_E)=0 because E has dimension one.

The map λbar from K1 is well-defined modulo R0: any two lifts to H1(G_Z) differ by the image of D0. Its image is R/R0. Both the exact relation filtration and the expression for V_Z therefore follow canonically.

The bound dim R0≤h0(G_E)≤30, combined with the imported bound dim R≥90+4h0(B(1))+4h2(B(1)), correctly gives

    dim im λbar≥60+4h0(B(1))+4h2(B(1)).

This is a universal lower bound, not an evaluation of either relation map.

## 4. Restriction and sign

Component restriction can miss the image of D1 in H2(G_Z). The cocycle formula has the stated positive sign: the difference of local primitives t=p_N|E−p_W|E lifts to the pair (p_N,p_W), and its differential is the diagonal restriction of x. The connecting map therefore sends [t] to r(η).

Changes of the component primitives alter [t] by the component H1 image. If the resulting D1 class vanishes, first make the difference a coboundary and then lift its degree-zero primitive through the sheaf-surjective difference map on an affine cover. Subtracting that coboundary makes the component primitives agree and glue. This supplies the cochain detail behind the asserted converse.

## 5. Euler and component checks

Rank B=3 and deg B_C=0 give χ(L)=−21, χ(M)=−9, and χ(G_E)=−30. The Koszul calculation gives χ(G_N)=−75. With χ(G_Z)=−105, Mayer–Vietoris gives χ(G_W)=−60 and component sum −135.

As a separate check, the imported ambient RR polynomial has ch2(B)=−15H². On W, with H=2h, twisting by O_P²(−2) gives ch(G_W)=3−6h−54h². Multiplication by td(P²)=1+(3/2)h+h² yields χ(G_W)=3−9−54=−60.

The component H1 identity and the bound dim K1≥75 plus the component H0 and H2 dimensions are correct. Replacing E by C changes the Euler prediction from −105 to −126, accounting for the missing layer of Euler characteristic −21. The kernel of the reduced difference map is indeed an extension of G_Z by L, so the replacement changes the sheaf, not merely its presentation.

## Scope

This audit is a mathematical review of universal identities and exact sequences. No selected HM matrix, splitting type, rank instance, source, physical jet, or obstruction pairing was computed.
