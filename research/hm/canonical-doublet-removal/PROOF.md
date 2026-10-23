# Forced doublet channels and a canonical twelve-source opposite presentation

Work over C with G=SL2(F5), W the physical negative doublet, W' the other doublet, A=Sym2 W, S=Sym3 W, D=Sym4 W, T6=Sym5 W, V=Sym2 W', and P the even four-dimensional irreducible. Bundles are on T=P(W*) with standard linearizations. No selected actual HM/source coefficient, point, parameter, matrix or instance rank is evaluated.

## 1. Immutable input and new result

The single immediate input SIXTEEN is PR1076 at commit8d17ad2bae45df6078dbb50ff963228c6105c815, research/hm/sixteen-source-opposite-pencil/PROOF.md in Akilleez-QA/read-em-and-weep. INPUTS.json records its exact Git blob. Its Sections1–5 supply the actual fiberwise-injective presentation

    0 -> E16 O(-1) --u--> Y21 -> C -> 0,
    0 -> F:=J tensor W' O(5) -> Y21 -> H19 O -> 0, (1)
    E16=2W+W'+S+T6, H19=1+2A+V+P+D.

Here J is a one-dimensional trivial multiplicity space. The source, target extension and maps are inherited from the actual opposite cohomological pencil. The extension in (1) admits equivariant splittings but has no selected splitting. The actual C is locally free of rank5 and degree26. SIXTEEN also proves that F->C is nonzero and has saturated image, with its rowwise image/quotient table retained below only to establish a Hom vanishing.

We prove two forced nonzero actual channels, not merely another character identity. First, the unique W' O(-1) source has nonzero constant P projection, and this actual source map selects a UNIQUE compatible P O lift into Y21. After removing this doublet, its Euler quotient Q≅W' O(1) splits off the new target canonically. Second, the remaining T6 O(-1) must map onto this Q. Its kernel is P O(-2). These operations yield

    0 -> P O(-2)+(2W+S) O(-1) -> Y17 -> C -> 0,
    0 -> F -> Y17 -> H15 O -> 0,
    H15=1+2A+V+D.                               (2)

The source splitting in (2) is canonical as an equivariant decomposition. Y17 is an actual quotient, and its displayed weighted extension splits equivariantly but not canonically. All remaining actual maps are retained. The endpoint is rank12 to rank17, with the same actual C. No further cancellation or source-row selection is claimed.

## 2. A degree obstruction forces the constant P channel

Let U' be the unique W' isotypic subspace in E16. Project u|U' O(-1) to H19 O. Its only possible target is the unique P component, since W' tensor W=P. Let

    i:U' O(-1) -> P_act O                         (3)

be this actual constant-target projection, where P_act is the canonical P-isotypic subspace of H19.

If i vanished, the entire U' O(-1) source would map into F. This factor would still be injective on every fiber: u is fiberwise injective, U' is a direct source subspace, and F is a subbundle of Y21. But source and F both have rank2 and degrees -2 and10 respectively. A fiberwise injective map between equal-rank vector bundles is an isomorphism, contradicting these unequal degrees. Thus i is nonzero. This uses no evaluation of a determinant at a parameter.

The Hom channel in (3) is one-dimensional, since P=W' tensor W and the coefficient map is the tensor Euler map. Consequently (3) is the universal inclusion, up to the named representation identifications, and has exact sequence

    0 -> U' O(-1) --i--> P_act O -> Q -> 0,
    Q≅W' O(1).                                  (4)

In particular (3) is saturated on every fiber. Its quotient Q, with the actual map, is canonical even though an identification with the named model W' O(1) is only up to scalar.

## 3. The actual source determines a unique constant P lift

Let Y_P be the preimage of P_act O in Y21. It is the actual extension

    0 -> F -> Y_P -> P_act O -> 0.               (5)

An equivariant splitting exists because H1(O(5))=0. The ambiguity between two splittings is Hom_G(P_act O,F). The actual source map u|U' O(-1) is a lift of i through (5).

Apply equivariant Hom(-,F) to (4). The two groups

    Hom_G(Q,F)=0,       Ext1_G(Q,F)=0            (6)

vanish. For Hom, the character test is

    Hom_G(W',W' tensor Sym4 W)
      =Hom_G(1+V,D)=0;

for Ext, H1(O(4))=0. Thus restriction is an isomorphism

    Hom_G(P_act O,F) -> Hom_G(U' O(-1),F).       (7)

Starting with any splitting of (5), its error on U' O(-1) can therefore be corrected by a unique element of the left side of (7). There is exactly one equivariant splitting s:P_act O->Y_P satisfying s i=u|U' O(-1). This characterization is intrinsic: the resulting P lift does not depend on the initially chosen splitting. It is a normalization forced by the actual source map, not an arbitrary declaration that a weighted coefficient is zero.

Relative to this unique lift, Y_P=F+s(P_act O) canonically, and the actual source lies in the second summand. Quotient the source and target of (1) by U' O(-1) and its actual image. The source quotient is canonically E14 O(-1), E14=2W+S+T6, by isotypic decomposition. The target Z19 is locally free and fits into

    0 -> E14 O(-1) -> Z19 -> C -> 0,
    0 -> F+Q -> Z19 -> H15 O -> 0.              (8)

Here the indicated Q subbundle is the quotient s(P_act O)/u(U' O(-1)). The split F+Q inside Z19 is canonical relative to these actual maps.

## 4. The Euler quotient is an intrinsic direct summand

Define Y17=Z19/Q. Then

    0 -> F -> Y17 -> H15 O -> 0.                (9)

We claim that 0->Q->Z19->Y17->0 has a UNIQUE equivariant splitting. Apply equivariant Hom(-,Q) to (9). For its two outer bundles,

    Hom_G(H15 O,Q)=Hom_G(H15,P)=0,
    Ext1_G(H15 O,Q)=0,
    Hom_G(F,Q)=0,
    Ext1_G(F,Q)=0.                              (10)

The first uses the absence of P in H15, and the second H1(O(1))=0. The third follows from H0(O(-4))=0. The fourth is the character vanishing

    ((W')* tensor W' tensor H1(O(-4)))^G
       =((1+V) tensor A)^G=0.

The factor J does not affect any vanishing. The long exact sequence gives both Hom_G(Y17,Q)=0 and Ext1_G(Y17,Q)=0. The latter gives existence of an equivariant splitting, and the former makes it unique. Thus

    Z19=Q+Y17                                  (11)

is a canonical actual decomposition, not a chosen target complement. In contrast, the weighted extension (9) has only an unspecified equivariant splitting; we do not normalize its remaining off-diagonal maps.

## 5. The forbidden doublet quotient forces the T6 surjection

The actual C satisfies Hom_G(C,W' O(1))=0. This follows directly from SIXTEEN's saturated-image table. For each necessary row, C is an extension of its image I by its listed quotient C/I. All image atoms have degree at least5. Every quotient atom has degree at least2, except possible W O(1). Maps from the higher-degree atoms to W' O(1) vanish by negative twist, and Hom_G(W O(1),W' O(1))=0 because W and W' are distinct. Applying Hom(-,W' O(1)) to 0->I->C->C/I->0 proves the claim without assuming that extension splits or choosing a realized row.

Project the actual source in (8) to the canonical Q summand of (11). This projection cannot vanish: if it did, the quotient C would have a nonzero equivariant quotient Q, contrary to that Hom vanishing. The only source which can reach Q is the unique T6 component, since

    Hom_G(E14,W' tensor Sym2 W)
      =Hom_G(E14,T6)

is one-dimensional. Thus the actual map T6 O(-1)->Q is nonzero. It is the tensor by W' of complete quadratic evaluation, with exact sequence

    0 -> P O(-2) -> T6 O(-1) -> W' O(1) -> 0.   (12)

Indeed the scalar quadratic sequence is 0->W O(-2)->A O(-1)->O(1)->0, and W' tensor W=P, W' tensor A=T6. Therefore this projection is onto on every fiber.

The isotypic decomposition E14=T6+(2W+S) is canonical; the second summand maps zero to Q. Its full kernel is consequently the actual canonical direct sum P O(-2)+(2W+S) O(-1). As a check, the cross Hom groups vanish in both directions: one has negative line degree, and the other is Hom_G(P,(2W+S) tensor W)=0, since (2W+S) tensor W=2+3A+D. Both cross Ext groups also vanish, using H1(O(-1))=H1(O(1))=0.

The map Y17->C in (2) is defined by the UNIQUE splitting section Y17->Z19 in (11), followed by Z19->C. It is not asserted that Y21->C descends through quotienting by the lifted P target. Since the source projection onto Q is surjective, the section-induced map Y17->C is onto, with kernel the full source kernel just computed. Taking this kernel diagram in (8), with (11), gives exactly (2). Its cokernel is the same actual C and its source map is injective on every fiber. The weighted F->C map also persists unchanged: F lies in the actual Y17 kernel of the Q projection because Hom_G(F,Q)=0 and its original map to C is used throughout.

## 6. Invariants, scope and verification

The final source has rank4+8=12 and degree-8-8=-16. Its target has rank15+2=17 and degree10. Hence rank(C)=17-12=5 and degree(C)=10-(-16)=26, as required.

The substantive constraints are the forced nonzero W'-to-P channel, the unique compatible P lift selected by the actual map, the canonical Q direct summand, and the forced T6-to-Q surjection. The twelve-source sequence records their joint effect on the original opposite bundle; it does not replace the actual remaining maps with freely chosen ones.

The seven necessary types are used only to forbid a W' O(1) quotient. No C type, source pair, vertex scalar or position of the initial marked line relative to K0 is selected. This construction does not compare separately marked conditional mixed-Q or im-h subspaces. Work stops at (2), with no additional cancellation asserted.

verify.py authenticates the immutable input and checks only fixed representation channels, Hom/Ext character tests, the seven conditional quotient tests and universal rank/degree balances. REPRODUCE.md reconstructs the omitted audit copy. REVIEW.md binds fresh independent whole-proof review to the final bytes; this is not a proof-assistant certification or an actual-instance computation.
