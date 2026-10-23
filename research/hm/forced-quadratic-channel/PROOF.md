# A forced quadratic channel and the actual nine-source opposite presentation

Work over C with G=SL2(F5) and the standard linearizations on T=P(W*). W is the physical negative doublet, W' the other doublet, A=Sym2 W, S=Sym3 W, D=Sym4 W, T6=Sym5 W, V=Sym2 W', and P the even four-dimensional irreducible. No selected actual HM/source coefficients, parameters, points, matrices or instance ranks are evaluated.

## 1. Immutable inputs and statement

INPUTS.json authenticates two originals in Akilleez-QA/read-em-and-weep:

- TWELVE: PR1083, commit b99fc50247fe8f992420d452ef359827011631aa, research/hm/canonical-doublet-removal/PROOF.md. Its Sections1–5 establish the actual fiberwise-injective presentation

      0 -> P O(-2)+(2W+S) O(-1) --u--> Y17 -> C -> 0,
      0 -> F:=J tensor W' O(5) -> Y17 -> H15 O -> 0,
      H15=1+2A+V+D.                              (1)

  J is a one-dimensional trivial multiplicity space. The source decomposition is canonical equivariantly. The target extension splits equivariantly but has no selected splitting. All maps, including F->C, are actual inherited maps. C is locally free, rank5, degree26. Section5 uses the authenticated saturated-image filtration of C, all of whose atoms have strictly positive line degree.
- SEXTIC: PR1017, commit 7cd8baebbec29ad21def1f8b30e19c707a87aed5, research/hm/rank-three-opposite-core/PROOF.md. Section2 proves the universal equivariant sequence

      0 -> V O(-2) -> P O -> O(6) -> 0.          (2)

  This is the kernel sequence of the basepoint-free P summand in Sym6 W; its proof uses projective icosahedral orbit sizes and bundle degrees, not selected HM evaluations.

We prove that the actual quadratic P O(-2) projection onto the unique constant V target in (1) is nonzero and everywhere onto. Its kernel is O(-8). Consequently the actual C admits the canonical kernel presentation

      0 -> O(-8)+(2W+S) O(-1) -> Y14 -> C -> 0,
      0 -> F -> Y14 -> H12 O -> 0,
      H12=1+2A+D.                               (3)

The source has rank9, the target rank14. The source decomposition is canonical equivariantly; the weighted target extension is not given a splitting. The actual weighted map F->C, hence its saturated image, is unchanged. This is a forced actual channel and kernel construction, not an arbitrary smaller model for C.

## 2. An intrinsic projection and a forbidden quotient

Inside H15, let V_act be the unique V-isotypic subspace. The isotypic projection H15->V_act is canonical. Compose it with Y17->H15 O to obtain the canonical surjection

      p:Y17 -> V_act O.                         (4)

No section or complement in Y17 is chosen. In particular p kills F. The elementary vanishing Hom(F,V_act O)=0 is consistent with this construction, but the already specified quotient in (1) is what defines p.

We have Hom(C,V_act O)=0, even without equivariance. Indeed the filtration in TWELVE Section5 expresses C as an extension of sums of positive-degree line bundles tensored with constant representations. Each such atom has no map to a trivial bundle, since H0(O(-d))=0 for d>0. Applying Hom(-,V_act O) to that filtration proves the vanishing without splitting C or selecting one of its necessary types.

Thus p u cannot vanish. If it did, (4) would descend through the cokernel C of u to a surjection C->V_act O, contradicting that vanishing.

## 3. Identify the unique nonzero quadratic channel

The linear source summand E8 O(-1), where E8=2W+S, cannot reach V_act O because

      Hom_G(E8,V tensor W)=Hom_G(2W+S,T6)=0.     (5)

The quadratic source has exactly one channel:

      dim Hom_G(P O(-2),V_act O)
         =dim Hom_G(P,V tensor A)=1,            (6)
      V tensor A=P+D.

Therefore the actual restriction p u|P O(-2) is nonzero. Dualizing (2) and twisting by O(-2), using self-duality of P and V, gives the exact universal sequence

      0 -> O(-8) -> P O(-2) -> V O -> 0.        (7)

The nonzero map in (7) spans (6). Hence the actual restriction is onto on every fiber, not just generically, and its actual kernel L is a line bundle equivariantly isomorphic to O(-8). A named identification L≅O(-8) is only up to scalar; L itself and its inclusion in the actual source are canonical.

The full source kernel K9=ker(pu) is canonically

      K9=L+E8 O(-1).                            (8)

This follows directly from the canonical source decomposition in (1) and (5). For an independent uniqueness check on the associated extension, Hom_G(E8 O(-1),L)=0 by H0(O(-7))=0, while

      Ext1_G(E8 O(-1),L)
        =(E8* tensor H1(O(-7)))^G
        =(E8* tensor Sym5 W)^G=0.              (9)

Thus 0->L->K9->E8 O(-1)->0 has a unique equivariant splitting. Also Hom_G(L,E8 O(-1))=Hom_G(E8,Sym7 W)=0, since Sym7 W=W'+T6. No hidden shear is being fixed by a scalar choice.

## 4. The actual kernel diagram, not target descent

Define Y14=ker p, a canonical subbundle of Y17. Taking the kernel in (1)'s target extension gives

      0 -> F -> Y14 -> (1+2A+D) O -> 0.         (10)

Its equivariant splitting exists because H1(O(5))=0, but no splitting is selected. The map Y14->C is simply the restriction of the actual Y17->C map, not an asserted descent through a target quotient and not a section-induced replacement.

It is surjective: locally lift a section of C to Y17; its p-value can be lifted to the source since pu is onto by (7); subtract that actual source image to obtain a lift in Y14. Its kernel is exactly ker(pu)=K9. This proves (3). As C is locally free, K9->Y14 is fiberwise injective everywhere. F is already contained in ker p, so its actual map to C and its saturated image are unchanged.

The ranks and degrees agree: K9 has rank1+8=9 and degree-8-8=-16; Y14 has rank2+12=14 and degree10; their cokernel has rank5 and degree26. The reduction depends on the genuine forced nonzero quadratic channel, not merely on these numerical balances.

## 5. Scope and reproducibility

This result does not choose an opposite C type, a source pair, the vertex extension scalar, or the position of the initial marked line relative to K0. It does not identify conditional mixed-Q or im-h subspaces with the bundles constructed here. Current PR1's exclusion of a separate conditional endpoint is not used in this proof. Work stops at the single forced quadratic channel and the nine-source presentation (3).

verify.py authenticates both original Git blobs and checks bounded fixed representation identities, Hom/Ext tests and universal degree balances. It evaluates no actual HM/source instance. REPRODUCE.md reconstructs omitted audit originals. REVIEW.md records independent whole-proof review bound to final bytes; this is not a proof-assistant certification.
