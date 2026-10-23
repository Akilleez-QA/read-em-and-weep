# Intrinsic channel classification of the nonzero-gate opposite core

Work over C on T=P(W*) with standard G=SL2(F5) linearizations and representations W,W',A=Sym2 W,S=Sym3 W,D=Sym4 W,T6=Sym5 W,V=Sym2 W',P. This proof assumes the existing nonzero-mu branch, equivalent to the old nonzero-lambda branch. No selected actual HM/source coefficient, point, parameter, matrix, jet or instance rank is evaluated.

## 1. Immutable inputs and statement

INPUTS.json authenticates three originals in Akilleez-QA/read-em-and-weep.

- SMALL: PR1092 at 7df3f6d6cd19964d5576954790de192d7f8ef8e1, research/hm/small-opposite-core/PROOF.md. It supplies, in this branch, the actual fiberwise-injective core

      0 -> L8+L2 --u--> Y6 -> Q -> 0,
      0 -> F -> Y6 -> B4 -> 0,                  (1)
      L8≅O(-8), L2≅O(-2), F≅W' O(5), B4≅S O(1).

  All source summands and maps are actual inherited objects. One-dimensional trivial multiplicity spaces are implicit in their named types. Q is the actual canonical kernel of C->O(2). The extension defining Y6 splits equivariantly but has no selected splitting.
- UNIVERSAL: PR1095 at 893845c20e964035dd2446897211814f184f93bd, research/hm/one-source-opposite-core/PROOF.md. Sections2 and4 prove universal facts used here: W O(-1) embeds in S O(1) with quotient W O(3); the degree-thirteen W' system is basepoint-free. These universal statements do not require the actual zero-mu branch used elsewhere in that proof. The present proof does not import that branch or identify its actual coefficients with ours.
- TYPES: PR996 at 54dc2b2b301f8a7e453b3101d5813c643beed71a, research/hm/opposite-second-degree-bound/PROOF.md. Sections5–6 give the four necessary nonzero-lambda alternatives:

      row9:  Q=O(12)+V O(4),
      row10: Q=O(18)+A O(2),
      row14: Q=W' O(5)+W' O(7),
      row15: Q=P O(6),                          (2)

  with C=O(2)+Q in this branch.

Let theta:L2->B4 be the projection of the actual source in (1). We prove:

- theta=0 if and only if row9 holds.
- If theta is nonzero, the actual L2 map selects a unique compatible equivariant splitting of Y6. Its graph quotient has a canonical one-source presentation

      0 -> L8 --(alpha,beta)--> F+R -> Q -> 0,
      R≅A O(2).                                (3)

  Its actual channel zero loci classify the other three cases:

      alpha=0 <=> row14,
      beta=0 <=> row10,
      alpha≠0 and beta≠0 <=> row15.             (4)

The pair in (3) cannot be zero. These are exact criteria on inherited maps, not evaluations or assertions that arbitrary channel values occur for actual HM data. The new content includes the compatible target lift, one-source core, and universal evaluation/extension proofs of its quotient types.

## 2. Two universal systems needed for the classification

Every nonempty orbit of the projective A5 action on P1 has size at least twelve. Indeed point stabilizers are cyclic with order in {1,2,3,5}. Consequently a nonzero invariant linear system of degree less than twelve has no common-zero divisor. G is perfect, so line-bundle linearizations have no additional one-dimensional character ambiguities.

### 2.1. The A system in degree ten

There is a unique nonzero map W' O(-5)->A O up to scalar, because

      A tensor Sym5 W=W'+S+2T6.

It has generic rank two. Otherwise its saturated generic image would be a line O(-e) inside A O, with e≥0. The nonzero factor W' O(-5)->O(-e) would require W' in Sym^(5-e) W; nonvanishing requires e≤5, but none of Sym^k W for 0≤k≤5 contains W'. This is impossible.

Its maximal minors are sections of O(10). Their common-zero divisor is G-invariant and has degree at most ten, so the orbit bound makes it empty. Thus this universal map injects on every fiber. Its line quotient is O(10), by degree and G-perfectness:

      0 -> W' O(-5) -> A O -> O(10) -> 0.

Dualizing and twisting by O(2) gives

      0 -> O(-8) -> A O(2) -> W' O(7) -> 0.     (5)

The first map spans its Hom space because A occurs once in Sym10 W=A+V+D. Thus every nonzero map in that channel is saturated with the quotient in (5). This argument proves the universal A evaluation kernel without an assumed multiplication-rank computation.

### 2.2. The S system in degree nine

The unique S system in Sym9 W=S+T6 is basepoint-free by the orbit bound. Let K be the kernel of S O->O(9). It has rank3, degree-9, and H0(K)=0; as a subbundle of a constant bundle all its splitting degrees are at most -1.

H0(K(1)) embeds in S tensor W=A+D and has dimension at most three. D cannot occur by dimension. If A occurred, all three degrees would be -1, contradicting degree-9. Thus H0(K(1))=0 and all degrees are at most -2.

Now H0(K(2)) embeds in S tensor A=W+S+T6 and again has dimension at most three. Its only possible nonzero value is W. Such a value gives the full degree -2 subbundle W O(-2) inside K. The unique nonzero map W O(-2)->S O is the universal inclusion from UNIVERSAL Section2, twisted by O(-1), with quotient W O(2). The evaluation S O->O(9) would then factor through W O(2). But

      Hom_G(W O(2),O(9))=Hom_G(W,Sym7 W)=0,
      Sym7 W=W'+T6.

This contradiction gives H0(K(2))=0. All three degrees are at most -3 and sum to -9, so K is O(-3)^3 ordinarily. Its multiplicity representation follows after twisting by three, when H1(K(3))=0:

      H0(K(3))=S tensor S-Sym12 W
        =(1+A+V+P+D)-(1+A+P+D)=V.

Thus dualizing its evaluation sequence and twisting by O(1) yields

      0 -> O(-8) -> S O(1) -> V O(4) -> 0.      (6)

This first map is the unique Hom channel since S occurs once in Sym9 W. Every nonzero member has the saturated quotient in (6).

## 3. The zero-theta case is structurally the row9 bundle

Suppose theta=0. The actual L2 source then lies in F, and its map is nonzero by the fiberwise injectivity of (1). The unique W' system in Sym7 W=W'+T6 is basepoint-free by the orbit bound. Hence every nonzero L2->F is saturated and has quotient O(12).

Quotient (1) by this actual L2 and its actual image. The result is

      0 -> L8 -> Z5 -> Q -> 0,
      0 -> O(12) -> Z5 -> B4 -> 0.             (7)

The projection L8->B4 cannot vanish. If it did, its fiberwise-injective map into Z5 would lie entirely in O(12), requiring an everywhere injective equal-rank map O(-8)->O(12). Unequal degrees forbid this. Therefore its B4 component is nonzero and, by (6), saturated with quotient V O(4).

The exact quotient diagram in (7) now gives

      0 -> O(12) -> Q -> V O(4) -> 0.          (8)

This extension splits equivariantly since H1(O(8))=0. Its splitting is unique equivariantly because Hom_G(V O(4),O(12))=Hom_G(V,Sym8 W)=0, with Sym8 W=P+D. Therefore Q has precisely the row9 type O(12)+V O(4). This conclusion was obtained from actual graphs and the universal system (6), not assumed from the list (2).

## 4. The nonzero-theta case selects a unique compatible target lift

Suppose theta≠0. Its channel has dimension one, and its nonzero universal model is the dual complete cubic evaluation, twisted by O(1):

      0 -> O(-2) -> S O(1) -> A O(2) -> 0.     (9)

Thus theta is saturated and R=B4/theta(L2) has type A O(2). The relevant relative lift groups vanish:

      Hom_G(R,F)=Hom_G(A,W' tensor Sym3 W)=0,
      W' tensor S=V+D,
      Ext1_G(R,F)=0                            (10)

where the last equality uses H1(O(3))=0. Applying Hom_G(-,F) to 0->L2->B4->R->0 shows that restriction Hom_G(B4,F)->Hom_G(L2,F) is an isomorphism.

Begin with any equivariant splitting of 0->F->Y6->B4->0, which exists by H1(O(4))=0. The actual source lift on L2 differs from this splitting by a map L2->F. The restriction isomorphism gives exactly one correction making the splitting agree with the actual source. Hence there is a UNIQUE compatible equivariant section s:B4->Y6 with s theta=u|L2. Uniqueness is equivariant, not a claim about ordinary splittings.

Quotient the actual source L2 and its actual image s theta(L2). The remaining source is the inherited L8. The target becomes canonically F+R relative to these actual maps. This proves (3). The two maps alpha and beta are therefore intrinsic projections after the actual compatible normalization; their zero loci do not depend on named representation identifications. No graph component was discarded by a free choice.

## 5. The two channels and their nonzero extension

Both channel spaces in (3) are one-dimensional:

      Hom_G(L8,F)=Hom_G(W',Sym13 W)=C,
      Hom_G(L8,R)=Hom_G(A,Sym10 W)=C.

Every nonzero alpha is basepoint-free by UNIVERSAL Section4 and has line quotient O(18). Every nonzero beta has quotient W' O(7) by (5). Since the full map in (3) is fiberwise injective, they cannot both vanish.

If alpha=0, quotienting (3) gives Q=F+W' O(7), the row14 type. If beta=0, it gives Q=O(18)+R, the row10 type.

If both are nonzero, the actual graph quotient and the saturated beta sequence give

      0 -> F -> Q -> W' O(7) -> 0.             (11)

Its class is the connecting image of alpha, up to the harmless pushout sign convention. That connecting map

      Hom_G(L8,F) -> Ext1_G(W' O(7),F)

is an isomorphism by (10). Thus (11) has NONZERO class. Its Ext space is one-dimensional, because H1(O(-2)) is trivial and (W' tensor W')^G has dimension one. Tensoring the Euler sequence by W' and twisting by O(6) gives a nonzero model

      0 -> W' O(5) -> P O(6) -> W' O(7) -> 0,
      W' tensor W=P.                           (12)

This is nonsplit since even ordinary Hom(W' O(7),P O(6))=0. Thus Q has type P O(6), the row15 type.

These three types differ from the row9 type obtained in Section3. Together with the exhaustive necessary alternatives in TYPES, this proves both directions of theta=0 iff row9 and of (4), within the retained nonzero-mu branch. The criteria identify actual channel incidences in the new normal form; they do not identify theta, alpha or beta with named coefficients of older cores simply by matching characters.

## 6. Scope and numerical checks

The target in (3) has rank2+3=5 and degree10+6=16. Its rank-one source has degree-8, giving Q rank4 and degree24. In (7), the target has rank5 and degree12+4=16, yielding the same Q invariants. The source/target maps are induced throughout from (1), so their cokernels are the actual canonical Q and not abstract substitute bundles.

The new information is the intrinsic theta test, its uniquely compatible target lift when nonzero, the actual one-source presentation, and exact channel criteria for all four nonzero-gate alternatives. Universal degree-nine and degree-ten kernel proofs supply the geometric quotient identifications. No gate, row, source pair, marked-line position or vertex scalar is selected. No arbitrary normal form is asserted to occur for actual HM data, and no further cancellation is claimed.

verify.py authenticates the three immutable originals and checks bounded fixed characters, Hom/Ext tests, orbit-degree obstructions and universal rank/degree balances. REPRODUCE.md reconstructs omitted audit inputs. REVIEW.md binds independent whole-proof review to final author bytes. No selected actual-instance evaluation or proof-assistant certification is asserted.
