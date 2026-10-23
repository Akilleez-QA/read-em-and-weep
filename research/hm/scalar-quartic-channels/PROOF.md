# Forced scalar and quartic channels in the actual opposite presentation

Work over C on T=P(W*) with the standard G=SL2(F5) linearizations. The fixed representations are W, W', A=Sym2 W, S=Sym3 W, D=Sym4 W, T6=Sym5 W, V=Sym2 W', and the even four-dimensional P. No actual HM/source coefficient, point, parameter, matrix, derivative or instance rank is evaluated.

## 1. Immutable interfaces and theorem

The two immediate originals in Akilleez-QA/read-em-and-weep are authenticated in INPUTS.json.

- NINE: PR1087 at ad34e86521236df3617c5e6c26976266bf4d9b61, research/hm/forced-quadratic-channel/PROOF.md. It proves the actual presentation

      0 -> O(-8)+(M tensor W+S) O(-1) --u--> Y14 -> C -> 0,
      0 -> F:=J tensor W' O(5) -> Y14 -> (1+2A+D) O -> 0. (1)

  M is the two-dimensional trivial multiplicity space of 2W, and J is one-dimensional. The indicated source summands and target quotient are inherited actual objects. Their named representation models need not have selected scalar identifications. C is locally free, rank5, degree26, and has no maps to constant bundles. The weighted map F->C is nonzero with saturated image.
- SIXTEEN: PR1076 at 8d17ad2bae45df6078dbb50ff963228c6105c815, research/hm/sixteen-source-opposite-pencil/PROOF.md. Section6 supplies the actual saturated-image filtration 0->I->C->C/I->0, with the seven necessary alternatives recalled in Section4 below. They are necessary alternatives, not asserted realized choices.

We prove two forced nonzero actual channels. First the constant scalar target of (1) receives a nonzero Euler map from M tensor W O(-1). Its multiplicity kernel is a canonical line M0 in M. Taking the actual kernel gives

      0 -> O(-8)+S O(-1)+L3 -> Y13 -> C -> 0,
      0 -> F -> Y13 -> (2A+D) O -> 0,            (2)
      0 -> M0 tensor W O(-1) -> L3
           -> (M/M0) tensor O(-2) -> 0.        (3)

Sequence (3) splits equivariantly, but not canonically: its equivariant splitting ambiguity is one-dimensional. No complement of M0 is selected.

Second, the inherited S O(-1) source in (2) has NONZERO constant D projection. It is the universal multiplication inclusion with quotient O(4), hence saturated on every fiber. This conclusion uses a forbidden P O(2) quotient of C and a universal degree-eight evaluation lemma. It is stronger than the rank reduction alone. The actual remaining channels and the extension (3) are retained; work stops at (2) and this forced quartic channel.

## 2. The scalar channel and its actual kernel

Compose the target quotient of (1) with its canonical trivial-isotypic projection to obtain p0:Y14->O. This is intrinsic and surjective without choosing any target splitting. If p0u=0, it would factor through a surjection C->O, contrary to NINE's positivity argument.

The O(-8) source cannot contribute because Sym8 W=P+D has no invariants. Nor can S O(-1), since Hom_G(S,W)=0. On M tensor W O(-1), the equivariant channel is a functional on M times Euler evaluation W O(-1)->O. Thus there is a nonzero functional a on M, defined up to the named target scalar, and a canonical line M0=ker(a). The actual source projection is everywhere onto. Set L3=ker[M tensor W O(-1)->O]. Passing to the canonical quotient M/M0 gives (3), by the ordinary Euler sequence

      0 -> O(-2) -> W O(-1) -> O -> 0.          (4)

The exact sequence (3), not a selected decomposition, is the intrinsic object. Its Ext1 group vanishes by H1(O(1))=0. But its equivariant Hom from the quotient to its subbundle is

      Hom(M/M0,M0) tensor (W tensor H0(O(1)))^G,

which is one-dimensional because W tensor W=1+A. Consequently any presentation of L3 as W O(-1)+O(-2) requires a noncanonical splitting. A chosen complement of M0 in M supplies one, but no such choice is made here.

Define Y13=ker(p0). It has the weighted target extension in (2). The map to C is the restriction of the actual Y14->C, and is onto because p0u is onto: locally correct a lift by an actual source section with the same p0-value. Its kernel is O(-8)+S O(-1)+L3. This proves (2) without choosing a target section or asserting a descent through a target quotient. Since C is locally free, the new source injects fiberwise everywhere. F lies in Y13, so its actual map to C remains unchanged.

## 3. A universal degree-eight D evaluation lemma

The multiplicity-one system D in H0(O(8))=Sym8 W=P+D is basepoint-free. A nonempty common-zero divisor would be invariant under the projective A5 action and have degree at most eight. Every nonempty orbit has size at least twelve: a point stabilizer in a finite subgroup of PGL2(C) is cyclic, and A5 has no element of order greater than five. Thus the divisor cannot exist.

Let K4 be the kernel of D O->O(8). It has rank4 and degree-8. Since it lies in a constant bundle and its map on global sections is the inclusion D into Sym8 W, all its splitting degrees are at most -1. Therefore H0(K4(1)) consists exactly of the multiplicity space of its degree -1 summands and has dimension at most four. It embeds in

      D tensor W=S+T6.

The T6 summand is impossible by dimension. If the S summand occurred, it would have dimension four and force all four splitting degrees to be -1, contradicting degree-8. Hence H0(K4(1))=0. All four degrees are at most -2 and sum to -8, so K4 is O(-2)^4 ordinarily.

Twisting by two and taking cohomology gives its equivariant multiplicity representation:

      H0(K4(2)) = D tensor A - Sym10 W
                  = (A+V+P+D)-(A+V+D)=P.

The H1 of K4(2) vanishes by the already established ordinary splitting; there is no assumed surjectivity of an unverified multiplication map. Thus the universal evaluation sequence and its dual are

      0 -> P O(-2) -> D O -> O(8) -> 0,
      0 -> O(-8) -> D O -> P O(2) -> 0.         (5)

The Hom space from O(-8) to D O is one-dimensional because D occurs once in Sym8 W. Every nonzero map in that channel is therefore the saturated inclusion in (5), up to scalar. This is a universal fixed-system argument, not an evaluation of actual HM data.

## 4. The forbidden P(2) quotient

SIXTEEN's saturated-image filtration has the following seven alternatives. Here R(d) means R tensor O(d).

      row    I                C/I
       9     O(12)            O(2)+V(4)
      10     O(18)            O(2)+A(2)
      14     W'(5)            O(2)+W'(7)
      15     W'(5)            O(2)+W'(7)
      17     W'(5)            O(14)+W(1)
      18     O(18)            W(1)+W(3)
      20     W'(5)            W(1)+O(14).

Each atom of degree greater than two has no map to P O(2) by negative twist. The only lower-degree tests are

      Hom_G(O(2),P O(2))=0,
      Hom_G(A O(2),P O(2))=0,
      Hom_G(W O(1),P O(2))=Hom_G(W,P tensor W)=0,
      P tensor W=W'+T6.

Thus Hom_G(I,P O(2)) and Hom_G(C/I,P O(2)) vanish in every necessary alternative. Applying Hom(-,P O(2)) to the actual filtration gives

      Hom_G(C,P O(2))=0.                        (6)

No splitting of the filtration and no choice of an actual row is used.

## 5. The actual S-to-D channel cannot vanish

Project Y13 to the unique D component of its constant quotient (2A+D) O. This is a canonical surjection pD:Y13->D O. The L3 source maps zero under this projection. Indeed both Hom_G(W O(-1),D O) and Hom_G(O(-2),D O) vanish, by

      D tensor W=S+T6,      Hom_G(1,D tensor A)=0.

Applying Hom(-,D O) to (3) proves Hom_G(L3,D O)=0, regardless of its noncanonical splitting.

Suppose now that the inherited S O(-1) also had zero D projection. Then only the O(-8) source could contribute to pD. Its component must be nonzero, or pD would give a forbidden constant quotient of C. By (5), this nonzero component has quotient P O(2). Consequently the composite

      Y13 -> D O -> P O(2)

is surjective and kills the whole actual source in (2). It descends to a surjection C->P O(2), contradicting (6). This proves that the actual S-to-D projection is nonzero.

Finally Hom_G(S O(-1),D O) is one-dimensional, since D tensor W=S+T6. Its nonzero generator is universal multiplication l tensor Sym3 W into Sym4 W, with exact sequence

      0 -> S O(-1) -> D O -> O(4) -> 0.        (7)

Thus the actual S projection is saturated everywhere. Its coefficient is not evaluated or declared to be an independently chosen parameter. Equation (7) is a constraint on the inherited map; we do not perform a further target quotient or remove another source in this packet.

## 6. Scope and checks

L3 has rank3 and degree-4. The source in (2) has rank1+4+3=8 and degree-8-4-4=-16. Its target has rank2+6+5=13 and degree10. Their actual quotient has rank5 and degree26. The two substantive constraints are the nonzero scalar functional with canonical kernel M0 and the forced nonzero S-to-D projection via the forbidden P(2) quotient.

The weighted target extension in (2) splits equivariantly by H1(O(5))=0, but is not assigned a splitting. We retain all actual remaining maps, all source splitting ambiguities in (3), and the actual weighted map. No C row, source pair, vertex scalar, or position of the initial marked line relative to K0 is selected. The separate conditional mixed-Q lane is not used.

verify.py authenticates the two immutable originals and performs bounded fixed-character, Hom/Ext and rank/degree checks only. REPRODUCE.md reconstructs omitted audit originals. REVIEW.md binds independent whole-proof review to the final author bytes. Neither verification nor this proof evaluates an actual selected instance or claims machine formalization.
