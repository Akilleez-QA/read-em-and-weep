# The nonzero cubic-kernel alternative has a forced quartic image

## Result

Work over C on the fixed physical binary-icosahedral parameter line, with the actual saturated inclusion E in the constant plane-section bundle, its actual Gauss kernel K=E^-, and A=E/K. Suppose the actual source has the D-type

    E=D O(-2)+(W'+T)O(-3)+V O(-4)+O(-8).

Here D=Sym4 W, S=Sym3 W, and T=Sym5 W, with the fixed marking of the immutable character inputs. The following statements hold without any assumption on the rank of the derivative of K.

1. If H0(K(3)) is nonzero, it is S and the actual restriction of the quotient map to D O(-2) has kernel S O(-3) and locally free image O(2). In particular there is an actual equivariant sheaf injection O(2) -> A.
2. If Hom_G(O(2),A)=0, then H0(K(3))=0 and the following character is genuine:

       H0(A(2)) + chi_G(A(4)) - chi_G(E(4)).       (1)

3. Neither of the following actual quotient shapes is possible:

       A_8=O(-8)+O(4)+O(8),
       A_10=O(-8)+O(4)+O(10).                    (2)

Under the primary four-type theorem, a quotient with an O(-8) summand already forces this exact D-type. Thus (2) excludes those shapes for every actual primary source, not merely a source chosen from a formal ledger. The fixed historical profile-(1,1) list contains the first shape at zero-based indices 98 and 100 and the second at indices 104 and 106. Each shape occurs at original defects 12 and 0, in that order. All four ordered rows are excluded. This is a narrow actual-map theorem, not a claim of full profile-(1,1) exclusion.

## 1. Input and scope

Eight complete immutable public originals are included in inputs/ and authenticated by byte count, SHA256 and Git blob ID in INPUTS.json. The geometric inputs are the actual saturated inclusion and strict-top theorem at db51525015bb7c5e825833d550d08dedf6f6ea96, the near-top visibility lemma at PR1129 (d1238732f42df5c70ba4430e230428d2cf699bbe), and the primary four-type theorem at PR1123 (504b7eb800407dfc7e6340c98c72cdd553939f54). The complete fixed historical 182-row list and its coverage note are also pinned at db51525015bb7c5e825833d550d08dedf6f6ea96, alongside the physical character source. The geometric necessity of that historical overlist is an imported written theorem, not a consequence of the JSON or this note's checker. Section 2 independently re-proves the D-type cubic-kernel alternative; no unpublished local theorem is a prerequisite.

All maps below are restrictions of the actual quotient E -> A, or actual second fundamental forms in the same constant ambient. An equivariant Birkhoff splitting may be chosen to describe ordinary bundle summands, but none of its projections is assumed horizontal. No selected actual coefficient, parameter, point, jet, tensor, matrix, rank evaluation or scan is used.

## 2. Recall the cubic-kernel alternatives directly

Write F=D O(-2) for the top summand. Strict-top makes the map

    H0(E(2))=D -> H0(A(2))

injective, so the restriction p:F -> A is nonzero. Let K_F be its sheaf kernel and I its actual image. Since I is torsion-free on P1, it is locally free and F/K_F=I. Thus K_F is a saturated subbundle of F. It has rank at most four. Its quadratic sections vanish, so all its ordinary degrees are at most -3, giving h0(K_F(3)) at most four.

The top cubic source is

    H0(F(3))=D tensor W=S+T.

Its T channel cannot be killed because dim T=6 exceeds the rank bound four on h0(K_F(3)). The displayed W' O(-3) and T O(-3) blocks have nonzero coefficient maps to A: the near-top lemma applies to each block, whose saturated complementary quotient in E has top degree at most -2.

The T channel from the displayed T O(-3) is independent of the T channel from F. Otherwise its actual map into A would factor through a scalar multiple of the unique nonzero equivariant morphism T O(-3) -> F. This morphism corresponds to the unique T in D tensor W, whose composite into A is nonzero as just proved. Subtracting this factorization replaces the displayed T block by a saturated graph subbundle T O(-3) inside E that the actual quotient kills. Its complementary quotient still has top at most -2. The near-top lemma excludes this: a killed negative saturated graph would have zero internal derivative and hence would be horizontal in the constant ambient.

The sole W' cubic source likewise survives, and all remaining cubic constituents are the single S from F. Semisimplicity therefore proves

    H0(K(3)) is either 0 or S.                    (3)

This recovers only the D-type case of the stronger cubic-kernel theorem, rather than assuming the whole new packet.

## 3. A surviving S forces the actual line image O(2)

Suppose H0(K(3))=S. Since no other cubic source contains S, this S lies in H0(K_F(3)). The bundle K_F(3) is nonpositive of rank at most four with at least four independent sections. Hence K_F has rank exactly four and K_F(3) is trivial. Equivariance identifies its coefficient representation as S:

    K_F=S O(-3).

The image I therefore has rank one and degree

    deg I=deg F-deg K_F=-10-(-12)=2.

The binary icosahedral group has no nontrivial one-dimensional characters. With the fixed linearization, I is O(2). This is the actual coherent image of F -> A, not its saturation in A. It is locally free on the curve, and its actual image inclusion gives

    O(2)=I -> A.

The injection is a sheaf injection; its image need not be a subbundle of A. No saturation in A is needed for the Hom obstruction.

Moreover F -> I is the complete quartic system: twisting by two gives the nonzero equivariant map D -> H0(O(4))=D, hence an isomorphism. This is a forced universal map type, not evaluation or selection of an actual coefficient.

Consequently Hom_G(O(2),A)=0 rules out the nonzero alternative in (3).

## 4. The improved fourth-twist endpoint envelope

If H0(K(3))=0, every ordinary degree of K is at most -4. Apply strict-top to K in the actual constant ambient. The kernel K^- of its own derivative has top at most -5, so H0(K^-(4))=0. Differentiation of K lands in the actual internal quotient A(-2), irrespective of its rank. Thus

    H0(K(4)) -> H0(A(2))

is injective. Euler additivity in 0 -> K -> E -> A -> 0 gives

    chi_G(K(4))=chi_G(E(4))-chi_G(A(4)).

Since H0(K(4))-chi_G(K(4))=H1(K(4)) is genuine, subtracting chi_G(K(4)) from the target H0(A(2)) is genuine. This is exactly (1). Unlike a generic iterated envelope, no extra H0(A) term is allowed: cubic-kernel vanishing has lowered the top of K by one.

## 5. Apply the exact envelope to the two quotient shapes

For A_8 and A_10, an equivariant map from O(2) to the negative scalar summand vanishes by degree. The other possible maps require invariant vectors in Sym2 W and, respectively, Sym6 W or Sym8 W. But

    Sym2 W=A_std,
    Sym6 W=V+P,
    Sym8 W=P+D,

contain no trivial representation. Hence Hom_G(O(2),A_i)=0 in both cases, so (1) applies.

The exact actual Euler character is

    chi_G(E(4))=3V+3P+2D.

The four required target characters are

    H0(A_8(2)) = A_std+2V+P+D,
    chi_G(A_8(4)) = 1+2P+2D,
    H0(A_10(2)) = 1+A_std+V+2P+D,
    chi_G(A_10(4)) = V+2P+2D.

In the first case, (1) has V multiplicity 2+0-3=-1. In the second, it has V multiplicity 1+1-3=-1. Both violate genuineness, proving the exclusions.

The negative O(-8) summand contributes H1 at these twists, and is retained in the Euler characters. In particular chi(A_i(4)) is not being replaced by H0(A_i(4)). This distinction is essential for the complete characters above, although not for the negative V coefficient.

## 6. What this does not settle

This does not exclude A=O(-8)+O(2)+O(16): that shape admits an equivariant map from O(2), so its nonzero cubic-kernel alternative is not removed by the Hom argument. The remaining profile-(1,1) equality case cannot be eliminated by importing the profile-(2,1) bound top(Q*)<=-2, because only top(Q*)<=-1 is available in profile (1,1).

No global rank-three exclusion, complete coverage theorem, obstruction value, maximal rank, smoothing, algebraicity or original-theorem repair is claimed. The four historical labels are not additional live-ledger counts.
