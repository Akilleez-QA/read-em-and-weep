# Excluding all degree-eleven rank-one first quotients

This continues `EXTREMAL-31-RANK-ONE-TEN-QUOTIENTS.md`, with its actual Gauss flag, equivariant linearizations, and representation notation. It excludes all three remaining e=11 cases and four e=9 cases. Three e=9 first-quotient shapes remain necessary possibilities. No improved SF or square-rank bound is asserted.

Write K=E^-, K2=E^{--}, F0=E^{---}, A0=E/K, and A1=K/K2. The actual derivative realizes A1 as the image in A0(-2), not its saturation. Both interior derivatives have rank three. Persistence gives H0(K(1))=H0(K2(2))=H0(F0(3))=0 and therefore

    H0(K2(3)) embeds in H0(A1(1)) embeds in H0(A0(-1)).

All comparisons below are multiplicity-wise comparisons of genuine representations. Equivariant splitting is used only as a bundle decomposition, never as a horizontal decomposition. We use chi(E(3))=Wp+2T and chi(E(4))=3V+3P+2D; the verifier checks the latter on every pinned E profile.

## 1. e=11, B=2O(4)

Here A0=2O(4)+O(-10), chi(K(3))=-Wp+T, and H1(K(3))<=Wp+2S+T. The preceding low-target classification says only O(-12) can map to the low target O(-12). Its multiplicity is exactly one: rank three forces one, while each costs Wp+T in H1. Its scalar low projection is nonzero. Remove its high graph by a bundle automorphism of the target. Then K=Khi+O(-12), and the derivative on Khi has image in 2O(2).

We have chi(Khi(3))=2T and H1(Khi(3))<=2S. Thus H0(K(3))=2T+R with R<=2S. The derivative kernel has sections at most 2S by persistence. Both T copies consequently map isomorphically onto H0(2O(5))=2T. These sections generate 2O(2), so A1=2O(2)+O(-12).

Now chi(K2(3))=0 and H1(K2(3))=H0(K2(3))<=2S. This eight-dimensional bound forces every ordinary K2 summand to have degree at least -12. The next derivative target is A1(-2)=2O+O(-14). Its low component is unreachable, contradicting derivative rank three.

## 2. The two larger e=11 cases

Let B be O(4)+O(6) or W O(5). Set D=B(-2), so D is O(2)+O(4) or W O(3). In both cases

    chi(K(3))=T-S,
    H1(K(3))<=Wp+2S+2T,
    H0(D(3))=Wp+2T,
    H0(B(-1))=S+T.

The only possible low-mapping blocks in K are O(-12) and W O(-13). They cannot coexist, and neither can occur twice, because each consumes the unique Wp in the H1 bound.

### 2a. Low block W O(-13)

The low projection is the nonzero linear evaluation W O(-13) -> O(-12), with kernel O(-14). It is surjective. There is no high component: Hom(W O(-13),D)=0, as checked by the representation products (equivalently W is absent in Sym15 and Sym17).

After removing W O(-13) from K, the complementary bundle has chi at twist three Wp+3T and H1 at most S. Since H0(K2(3))<=S+T, the map on high sections must surject onto Wp+2T. Consequently its image is all of D, and

    A1=D+O(-12),  K2=K2prime+O(-14).

The contradiction for this full-image case is proved in Section 3.

### 2b. Low block O(-12)

Its low scalar is nonzero. Remove the high graph, and write the remaining rank-two actual image as Ahi subset D. Thus A1=Ahi+O(-12). The source H0(K(3)) contains Wp+2T, whereas its kernel H0(K2(3)) is at most S+T. Therefore H0(Ahi(3)) contains Wp+T.

The bundle K2 has rank eleven and all degrees at most -3, so deg(K2)<=-33. As deg(K)=-54, this yields deg(A1)>=-21 and deg(Ahi)>=-9. The torsion quotient D/Ahi has invariant determinant divisor of degree at most15. Its degree is therefore either0 or12. (The smallest nonzero invariant divisor degree is12 and the next is20.)

If its degree is zero, Ahi=D; Section3 applies. Otherwise Ahi has rank two and degree -6. Equivariant splitting gives either two even-degree invariant line bundles or an irreducible two-dimensional representation tensored with O(-3).

For D=W O(3), every degree in Ahi is at most3. In the unequal-line case the larger even degree is at most2, so H0(Ahi(3)) cannot contain Wp: the first Wp in a symmetric power occurs in degree7. In the equal-degree case Ahi=R O(-3), its sections have dimension2 and cannot contain Wp+T. Both contradict the forced sections.

For D=O(2)+O(4), every degree is at most4. The same argument forces Ahi=O(4)+O(-10); all other splitting types lack Wp+T. Hence

    A1=O(4)+O(-10)+O(-12),
    chi(K2(3))=2T-S.

Persistence gives H0(K2(3))<=T. This is incompatible with chi(K2(3))=2T-S, whose T multiplicity already exceeds the allowed H0 multiplicity. Thus the defect12 case is impossible.

## 3. Contradiction whenever A1=D+O(-12)

In both larger e=11 cases, chi(K2(3))=-S. Persistence gives H0(K2(3))<=S+T and therefore H1(K2(3))<=2S+T. The only equivariant splitting block within this H1 budget that can map to the next low target O(-14) is O(-14) itself. The verifier checks the complete finite list, with the range bounded by dim(H1). Its multiplicity is at most one since it consumes S+T. Rank three forces its scalar low projection to be nonzero.

Thus K2 contains one direct bundle summand O(-14). Let K2prime be its splitting complement. This also covers the direct O(-14) kernel already obtained in Section2a. Then

    rank(K2prime)=10, deg(K2prime)=-34,
    chi(K2prime(3))=T, H1(K2prime(3))<=S.

All its degrees are at most -3 by persistence. If H1 were S, then H0 would be T+S of dimension10. All ten rank positions would have degree -3, leaving no negative summand to supply H1, a contradiction. Hence H1=0, and splitting forces

    K2prime = T O(-3) + R O(-4)

for a genuine four-dimensional even representation R. But the exact sequences at twist four give

    chi(K2prime(4)) = -A+2V+2P+D,
    T tensor W = V+P+D,
    R = -A+V+P.

The negative A multiplicity is impossible. This proves the full-image contradiction and excludes both larger e=11 cases.

## 4. Additional e=9 exclusion

Take B=O(-4)+O(6), so A0=O(-4)+O(6)+O(-8). The prior bound is H1(K(3))<=T, and the only block able to reach the low O(-10) target is O(-10). Rank three forces that block once; its H1 contribution is the entire T budget. Every other summand of K therefore has degree at least -4. No such summand maps to the other low target O(-6). Nor does O(-10) map equivariantly to O(-6), because Sym4 has no invariant. The derivative into O(-6)+O(4)+O(-10) has rank at most two, a contradiction.

## 5. Three more e=9 cases

For B=O(2)+O(4), O(2)+O(6), or W O(3), the prior low-target list contains only O(-10). The low map on its multiplicity space is forced nonzero. Choose one O(-10) summand on which it is an isomorphism, split off that low projection, remove its high graph, and write K=Y+O(-10). Additional O(-10) summands, if allowed by the budget, remain in Y; none is silently discarded. The bounds are respectively

    chi(Y(3))=S+T, Wp+T, S+T;
    H1(Y(3))<=W+S, W+S+T, W+S.

For B=O(2)+O(4), persistence bounds H0(K2(3)) by W+S. The T sections of Y therefore generate the O(2) high factor: the other high factor O has no T sections at twist three. Thus Ahi=O(2)+O(-d) inside O(2)+O, where d>=0 is an invariant divisor degree. Consequently A1=Ahi+O(-10) and the ordinary Euler characteristic of K2(3) is d. If d>0, then d>=12 whereas H0(K2(3))<=H0(A1(1)) has dimension at most4, a contradiction. Hence d=0. Now chi(K2(3))=0 and H1(K2(3))<=W+S, so every degree of K2 is at least -10. It cannot reach the next low O(-12) target.

For B=W O(3), the same T sections map isomorphically onto the unique T subrepresentation of H0(W O(4))=S+T. This subsystem generates W O(1): it is the polarization map Sym5 W -> W tensor Sym4 W. At any point its first derivatives span the two-dimensional fiber, as follows by differentiating the fifth power of a linear form nonvanishing there and its product with a fourth power and an independent form. Equivalently this is the homogeneous first-jet evaluation of all quintics. Thus A1=W O(1)+O(-10). Again chi(K2(3))=0, H1<=W+S, and the next low target O(-12) is unreachable.

For B=O(2)+O(6), persistence bounds H0(K2(3)) by W+T. The Wp sections cannot lie in the kernel and occur only in the O(4) high factor. The Wp septic pencil has no common zero: its common-zero divisor would be invariant of positive degree at most7, but the minimum is12. Hence it generates O(4), and Ahi=O(4)+O(-d) inside O(4)+O, with d an invariant divisor degree. The ordinary Euler characteristic of K2(3) is d-4. For d>=12 this is at least8, but persistence bounds its H0 dimension by6. Hence d=0. The exact character is now chi(K2(3))=-S, and H1(K2(3))<=W+S+T. The complete low-block calculation in the verifier shows no summand within this budget can map to O(-12). This contradicts rank three.

## Remaining scope

Only e=9 remains, with B equal to 2O(4), O(4)+O(6), or W O(5), and A0=B+O(-8). These are necessary possibilities, not realizations. This note does not exclude the entire maximal plateau and does not improve the SF or positive-square rank bound.
