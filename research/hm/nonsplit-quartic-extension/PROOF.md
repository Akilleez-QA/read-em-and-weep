# A forced nonsplit quartic extension in the actual opposite target

Work over C on T=P(W*) with standard G=SL2(F5) linearizations. We use W, W', A=Sym2 W, S=Sym3 W, D=Sym4 W, T6=Sym5 W, V=Sym2 W', and the even four-dimensional P. All arguments concern actual inherited sheaf maps and fixed universal representations. No selected HM/source coefficient, point, parameter, matrix, jet or instance rank is evaluated.

## 1. Immutable interfaces and new statement

INPUTS.json authenticates two immediate originals in Akilleez-QA/read-em-and-weep.

- EIGHT is PR1088 at d84d980079242e516e25b4fbdd854a3378650369, research/hm/scalar-quartic-channels/PROOF.md. It gives the actual presentation

      0 -> O(-8)+S O(-1)+L3 --u--> Y13 -> C -> 0,
      0 -> F:=J tensor W' O(5) -> Y13
           -> (M_A tensor A+D) O -> 0,          (1)

  where dim M_A=2 and dim J=1, with trivial multiplicity actions. The source summands are actual inherited subbundles. L3 has its exact sequence

      0 -> M0 tensor W O(-1) -> L3
           -> M1 tensor O(-2) -> 0,             (2)

  for one-dimensional trivial multiplicity spaces M0,M1. This extension splits equivariantly but not canonically. EIGHT proves that the actual S O(-1) projection to D O is nonzero and saturated, with quotient O(4). The weighted map F->C is retained and has saturated image. C is locally free of rank5 and degree26.
- QUOTIENT is PR996 at 54dc2b2b301f8a7e453b3101d5813c643beed71a, research/hm/opposite-second-degree-bound/PROOF.md. Section6 proves

      dim Hom_G(C,O(2))=1,                      (3)

  and every nonzero member is onto. In particular its kernel is the canonical rank-four, degree24 bundle Q. No actual necessary row is selected by that result.

We prove that the actual S O(-1) projection to M_A tensor A O is NONZERO. Its coefficient vector determines a canonical line L_A in M_A. After quotienting (1) by the actual S source and its actual image, we obtain

      0 -> O(-8)+L3 -> Z9 -> C -> 0,
      0 -> F -> Z9 -> B7 -> 0,                  (4)
      0 -> M_A tensor A O -> B7 -> O(4) -> 0.   (5)

The extension vector in (5) is nonzero and has image line L_A. Consequently B7 is equivariantly isomorphic to A O+S O(1), but no complement is selected. More intrinsically B7 has a canonical subbundle B4 of type S O(1) and canonical quotient (M_A/L_A) tensor A O. The actual weighted extension Z9 is retained; its splitting as a bundle is noncanonical. The unique quotient C->O(2) is realized explicitly by evaluating this residual A quotient.

## 2. The actual A coefficient cannot vanish

Let b be the actual S O(-1) projection to M_A tensor A O through the quotient in (1). Its universal channel is one-dimensional because

      Hom_G(S,A tensor W)=Hom_G(S,W+S)=C.

Thus b corresponds to a vector a in M_A up to the nonzero scalar used to identify the universal channel. Its zero/nonzero status and, when nonzero, its image line L_A are intrinsic. No splitting of Y13 is needed to define b.

Compose Y13's constant quotient with the projection to M_A tensor A and the universal quadratic evaluation A O->O(2). This yields a canonical surjection

      e:Y13 -> M_A tensor O(2).                 (6)

The other source terms cannot contribute equivariantly:

      Hom_G(O(-8),O(2))=(Sym10 W)^G=0,
      Hom_G(W O(-1),O(2))=Hom_G(W,Sym3 W)=0,
      Hom_G(O(-2),O(2))=(Sym4 W)^G=0,           (7)

using Sym10 W=A+V+D, Sym3 W=S and Sym4 W=D. Applying Hom(-,O(2)) to (2) gives Hom_G(L3,O(2))=0, without choosing a splitting of L3.

If b were zero, (6) would kill the entire source of (1), and would descend to a surjection C->M_A tensor O(2). Its two component maps to O(2) would be linearly independent: a nonzero functional on M_A cannot vanish after a surjective sheaf map. Hence dim Hom_G(C,O(2)) would be at least two, contradicting (3). Therefore a is nonzero and L_A is a canonical line.

This argument forces the actual A channel; it does not infer it from generic coefficients or from an abstract rank balance.

## 3. Quotient the actual graph, not just the D component

Write i:S O(-1)->D O for the actual saturated D projection established in EIGHT. Its quotient sequence is

      0 -> S O(-1) --i--> D O -> O(4) -> 0.     (8)

The full constant-target map of the actual S source is the graph (b,i) into M_A tensor A O+D O. Since i is saturated, this graph is saturated as well. Its quotient B7 fits into (5).

The actual full source S O(-1)->Y13 may also have a weighted F component relative to a target splitting. Define Z9 by quotienting Y13 by this FULL actual image, not by the D projection alone. The projection to the constant quotient is already fiberwise injective, so the image meets F trivially on every fiber. Thus F remains a subbundle of Z9 and (4)'s weighted extension is exact. Quotienting the first sequence of (1) by this source and actual image yields (4), with the same actual C. Both source and target quotients are locally free and the remaining source injects on every fiber.

For clarity, the weighted graph admits a unique correction only after other lifts have been fixed. Choose any equivariant splitting of the target extension in (1), and keep its A lift fixed. Changes of its D lift are maps D O->F. Restriction along (8) gives an isomorphism

      Hom_G(D O,F) -> Hom_G(S O(-1),F),          (9)

because Hom_G(O(4),F)=Hom_G(1,W' tensor W)=0 and Ext1_G(O(4),F)=0 by H1(O(1))=0. Thus exactly one D-lift correction absorbs the weighted S component relative to those fixed lifts. This does not produce a globally selected splitting of Y13 or Z9. In particular it cannot remove b: Hom_G(D O,A O)=0. The actual A graph must be retained.

## 4. Its extension class is forced nonzero

Apply equivariant Hom(-,A O) to (8). Since

      Hom_G(D O,A O)=0,     Ext1_G(D O,A O)=0,

its connecting map is an isomorphism

      Hom_G(S O(-1),A O) -> Ext1_G(O(4),A O).
                                                        (10)

Both spaces are one-dimensional. The first is the channel in Section2; the second is (A tensor H1(O(-4)))^G=(A tensor A)^G. The graph quotient (5) is the pushout of (8) by b, up to an irrelevant sign convention. Hence its extension vector is a nonzero scalar multiple of a. It is nonzero and has the same intrinsic multiplicity image L_A.

The standard complete cubic evaluation sequence is

      0 -> A O -> S O(1) -> O(4) -> 0.          (11)

It is nonsplit because Hom(O(4),S O(1))=0. Therefore (11) represents the nonzero equivariant extension class in (10). Restricting the vector in (5) to its image line gives this model; a choice of complementary line to L_A gives B7≅A O+S O(1). Such a complement is not part of the theorem's actual data.

There is also a complement-free description. Push (5) out along M_A->M_A/L_A. Its extension class is zero, and the resulting extension of O(4) by (M_A/L_A) tensor A O has a UNIQUE equivariant splitting, since Hom_G(O(4),A O)=0. Projection through this split pushout defines a canonical surjection

      B7 -> (M_A/L_A) tensor A O.               (12)

Its kernel B4 is the nonsplit extension of O(4) by L_A tensor A O and has type S O(1). Thus

      0 -> B4 -> B7 -> (M_A/L_A) tensor A O -> 0 (13)

is intrinsic. This last sequence admits equivariant splittings, but not a unique one: Hom_G(A O,S O(1)) has dimension one because S tensor W=A+D, while Ext1_G(A O,S O(1))=0. Equivalently B4 is the positive-degree Harder–Narasimhan subbundle of B7.

Finally Ext1_G(B7,F)=0, as follows using B7≅A O+S O(1) and H1(O(5))=H1(O(4))=0. Thus Z9 has bundle type

      W' O(5)+S O(1)+A O.                      (14)

This is only an equivariant bundle isomorphism type, with the multiplicity lines understood. No splitting of (4), no residual source-map entries and no actual coefficients are selected. The source L3 likewise retains its noncanonical splitting (2).

## 5. Identify the canonical degree-two quotient

Compose (6) with M_A->M_A/L_A. It kills the S source because b takes values in L_A tensor A, and kills the other source terms by (7). It therefore descends to a surjection

      C -> (M_A/L_A) tensor O(2).               (15)

Surjectivity follows from that of (6) and the multiplicity quotient. This is the nonzero member of the unique line (3), with its target multiplicity retained. Hence its kernel is exactly QUOTIENT's canonical Q, not a newly chosen quotient of the same character.

The map in (15) is equally obtained from Z9->B7, (12), and quadratic evaluation A O->O(2). Indeed the map from M_A tensor A O+D O to (M_A/L_A) tensor A O is projection to A modulo L_A; it kills the graph (b,i), and agrees with the unique pushout construction of (12). This identifies the canonical degree-two quotient through the actual graph quotient, without requiring any chosen target complement.

## 6. Scope and reproduction

The source in (4) has rank1+3=4 and degree-8-4=-12. The target has rank9 and degree10+4=14. Its actual quotient therefore has rank5 and degree26. These balances check the construction but do not replace the forced-nonzero extension argument.

The new information is the unavoidable A graph, its nonzero extension vector, the intrinsic active A line and S(1) subbundle, and the exact realization of the canonical C quotient through the residual A evaluation. No C type, source pair, vertex scalar, or original marked-line position is selected. No further source cancellation is claimed.

verify.py authenticates both immutable inputs and checks only fixed representation identities, Hom/Ext tests and rank/degree balances. REPRODUCE.md reconstructs omitted audit originals. REVIEW.md records independent whole-proof review against the final author bytes; no proof-assistant certification or actual-instance computation is asserted.
