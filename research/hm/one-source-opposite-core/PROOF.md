# The actual one-source Euler core and its two intrinsic channels

Work over C with G=SL2(F5) on T=P(W*) and standard linearizations. Write W' for the other odd doublet, A=Sym2 W, S=Sym3 W, D=Sym4 W, T6=Sym5 W, V=Sym2 W', and P for the even four-dimensional irreducible. Throughout this proof impose the existing branch hypothesis mu=0, equivalent to the old lambda=0. Neither this branch nor any actual coefficient is selected by an evaluation.

## 1. Immutable interfaces and statement

INPUTS.json authenticates three originals in Akilleez-QA/read-em-and-weep.

- SMALL: PR1092 at 7df3f6d6cd19964d5576954790de192d7f8ef8e1, research/hm/small-opposite-core/PROOF.md. Sections1–4 supply, in this branch, the actual fiberwise-injective presentation

      0 -> L8+U --u--> Y6 -> Q3 -> 0,
      0 -> F -> Y6 -> B4 -> 0,                  (1)
      L8≅O(-8), U≅W O(-1), F≅W' O(5), B4≅S O(1).

  These source summands, F, B4 and all maps are inherited actual objects; one-dimensional trivial multiplicity factors are retained implicitly in their names. Q3 is the intrinsic kernel of the unique equivariant quotient Q->O, where Q is the canonical kernel of C->O(2). The weighted map F into Q3 is the inherited map into C. The target extension splits equivariantly but was not assigned a splitting.
- SEXTIC: PR1017 at 7cd8baebbec29ad21def1f8b30e19c707a87aed5, research/hm/rank-three-opposite-core/PROOF.md. Section2 proves

      0 -> W' O(-3) -> V O -> O(6) -> 0.        (2)

- TYPES: PR996 at 54dc2b2b301f8a7e453b3101d5813c643beed71a, research/hm/opposite-second-degree-bound/PROOF.md. Sections5–6 identify the three necessary zero-lambda possibilities as

      row17: C=O(14)+W O(1)+W' O(5),
      row18: C=O(18)+W O(1)+W O(3),
      row20: C=W O(1)+V O(8),                  (3)

  with their positive Q3 types obtained by removing W O(1).

We prove that the actual U projection to B4 is forced nonzero. It selects a UNIQUE compatible equivariant splitting of the target in (1). Quotienting by the actual U image yields

      0 -> L8 --(alpha,beta)--> F+R -> Q3 -> 0,
      R≅W O(3),                               (4)

where the target decomposition is canonical relative to the actual equivariant maps. Both Hom channels in (4) are one-dimensional and individually basepoint-free when nonzero. Their intrinsic zero loci give exact criteria:

      alpha=0   <=> row17,
      beta=0    <=> row18,
      alpha≠0 and beta≠0 <=> row20.             (5)

The pair cannot be simultaneously zero. These criteria follow from actual graphs and a nonzero extension class, not just from the known list. Both values remain unselected; arbitrary channel choices are not asserted to be realized by HM geometry.

## 2. Force the U-to-B4 channel

If the actual U projection to B4 vanished, U would map into F. This factor would remain fiberwise injective by (1). But U and F both have rank2 and degrees -2 and10. An everywhere fiberwise-injective map between equal-rank bundles is an isomorphism, contradicting their unequal degrees. Thus i:U->B4 is nonzero.

Its equivariant Hom space is one-dimensional:

      dim Hom_G(W O(-1),S O(1))
        =dim Hom_G(W,S tensor A)=1,
      S tensor A=W+S+T6.

The universal nonzero map is multiplication by the square of the tautological line, with sequence

      0 -> W O(-1) -> S O(1) -> W O(3) -> 0.    (6)

For a uniform construction, polarize a cubic into W tensor Sym2 W and evaluate the last two factors at the tautological quotient W O->O(1). After twisting by O(1), this maps S O(1) to W O(3). Relative to any generator l of the kernel line and a complement m, it kills l³ and l²m, while lm² and m³ map to nonzero multiples of the two independent W directions. Its kernel is l²W, proving (6). This calculation is universal for an arbitrary line, not an evaluation of an actual HM point or tensor.

Consequently i is saturated, and its canonical quotient R=B4/i(U) has type W O(3).

## 3. The actual source selects a unique compatible target lift

Apply equivariant Hom(-,F) to 0->U->B4->R->0. We have

      Hom_G(R,F)=0,       Ext1_G(R,F)=0.        (7)

The first is Hom_G(W,W' tensor Sym2 W)=Hom_G(W,T6)=0; the second follows from H1(O(2))=0. Therefore restriction is an isomorphism

      Hom_G(B4,F) -> Hom_G(U,F).                (8)

An equivariant splitting of the target extension in (1) exists by H1(O(4))=0. Begin with any such splitting. Its error on U, compared with u|U, is a map U->F. By (8) there is exactly one correction removing this error. Hence there is a UNIQUE equivariant section s:B4->Y6 satisfying s i=u|U, independent of the initially chosen splitting. Uniqueness is equivariant; ordinary splittings need not be unique.

It follows that Y6=F+s(B4) canonically relative to the actual maps. Quotient source and target by U and its actual image s i(U). The source quotient is the inherited L8, and the target quotient is canonically F+R. This proves (4) with the same actual Q3. The remaining map includes every component induced by u after this uniquely compatible lift; it does not discard a graph by fiat. Since Q3 is locally free, (4) injects on all fibers.

The maps alpha:L8->F and beta:L8->R are actual projections to this intrinsic direct decomposition. Their zero/nonzero status is independent of named representation identifications, which only rescale channel generators.

## 4. The two universal covariants are basepoint-free

The fixed character identities are

      Sym11 W=W+S+T6,
      Sym13 W=W+W'+S+T6.                       (9)

Thus Hom_G(L8,R) and Hom_G(L8,F) both have dimension one. A nonzero beta corresponds to the W system in H0(O(11)), and a nonzero alpha to the W' system in H0(O(13)), through the usual section description of a map from a line bundle.

Every projective icosahedral orbit has size at least twelve. A point stabilizer in a finite subgroup of PGL2(C) is cyclic, and its order in A5 belongs to {1,2,3,5}. Orbit sizes are therefore 60,30,20 or12. The degree-eleven W system has no nonempty common-zero divisor.

For the degree-thirteen W' system, a common-zero divisor, if present, must have degree twelve by these orbit sizes. A section defining it spans a one-dimensional G representation. Since G=SL2(F5) is perfect, that character is trivial. Dividing the W' system by this invariant degree-twelve section would embed W' into H0(O(1))=W, impossible. Hence this system is also basepoint-free.

Every nonzero alpha or beta is therefore an everywhere saturated line inclusion into its rank-two target. Degree and the absence of nontrivial one-dimensional G characters determine their line quotients:

      coker(alpha)=O(18) when alpha≠0,
      coker(beta)=O(14) when beta≠0.            (10)

This proves uniform saturation, not merely generic injectivity, without evaluating an actual polynomial or a selected parameter.

## 5. The actual extension class distinguishes the three cases

The pair cannot vanish simultaneously because (4) is injective. If alpha=0, (10) gives Q3=F+O(14), of type W' O(5)+O(14). If beta=0, it gives Q3=O(18)+R, of type O(18)+W O(3).

If both are nonzero, quotienting the actual graph using the saturated beta inclusion gives

      0 -> F -> Q3 -> O(14) -> 0.              (11)

Its class is the connecting image of alpha, up to the harmless pushout sign convention, under

      Hom_G(L8,F) -> Ext1_G(O(14),F).

This is an isomorphism by (7), applied to 0->L8 --beta--> R->O(14)->0. Thus (11) has NONZERO class. Its Ext space is one-dimensional:

      Ext1_G(O(14),W' O(5))
        =(W' tensor H1(O(-9)))^G
        =(W' tensor Sym7 W)^G=C,
      Sym7 W=W'+T6.

Twisting (2) by O(8) provides the universal model

      0 -> W' O(5) -> V O(8) -> O(14) -> 0.     (12)

It is nonsplit because Hom(O(14),V O(8))=0. Hence (12) represents the nonzero class in this one-dimensional Ext space, and Q3 in (11) has type V O(8). This identifies the both-nonzero case without first choosing a row from a list.

The three resulting Q3 types are pairwise distinct. TYPES matches them to exactly the three necessary zero-lambda C alternatives (3), proving both directions of (5). These are actual coefficient incidences in the new canonical target; no coefficient is identified with one in an older rank-three presentation merely by its representation label.

## 6. Scope and checks

The source of (4) has rank1 and degree-8, while its target has rank4 and degree10+6=16. Thus Q3 has rank3 and degree24. The weighted map F->Q3 is unchanged under the quotient and remains the map inherited from C.

The new content is the forced U-to-S projection, the uniquely compatible equivariant lift selected by the actual U map, the resulting one-source core, and the exact channel criteria proved by its pushout extension. Neither alpha nor beta is evaluated. No zero-mu branch is selected, no source pair or marked-line position is determined, and no arbitrary abstract core is asserted to occur in the actual HM family.

verify.py authenticates all three immutable originals and performs bounded fixed-character, Hom/Ext, divisor-degree and universal rank/degree checks. REPRODUCE.md reconstructs omitted audit originals. REVIEW.md binds independent whole-proof review to final author bytes. No selected actual-instance evaluation or proof-assistant certification is claimed.
