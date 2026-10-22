# Ten necessary first quotients in the rank-one dual-image branch

## Result and boundary

Suppose the maximal rank-three Gauss plateau is (k,l)=(3,1) and the restricted dual cubic derivative has rank ONE. Its image is saturated O(e), e=9 or11. Writing A0=E/E^- and K=E^-, the actual quotient splits as

    A0=B + O(1-e).

Exactly the following TEN necessary shapes survive the tests here:

    e=9: B=O(-4)+O(6), O(2)+O(4), O(2)+O(6),
           2O(4), O(4)+O(6), W O(3), W O(5);
    e=11: B=2O(4), O(4)+O(6), W O(5).

These are an overlist, not realized bundles. The full rank-one branch and full (3,1) profile remain open. SF>=3 and positive-square rank>=27 are unchanged. No actual coefficient, source point, instance matrix, rank experiment or scan is used.

## 1. Actual quotient sequence and two-step bound

Use EXTREMAL-31-DUAL-CUBIC-IMAGE-HAS-RANK-AT-MOST-TWO.md, the five Q* splittings in EXCEPTIONAL-CUBIC-GAUSS-CORNER-EXCLUSION.md, and their actual saturated Gauss flags. The rank-one image J is O(9) or O(11). Its saturation has the same individual-block restrictions, hence also degree9 or11. Their difference is an invariant effective divisor of degree at most two, so it is zero.

Negative-transpose duality places J in the saturated annihilator A0*(1) inside E*(1). Dualizing gives a surjection A0 -> O(1-e). Its rank-two kernel B embeds in A0, and B(2) embeds in the actual derivative image inside Q. Thus

    0 -> B -> A0 -> O(1-e) -> 0,                 (1)

and every ordinary summand of B has degree at most six, since the largest degree of Q is eight. All these bundles are center-even.

Put U=chi_G(E(3))=Wprime+2T6. Persistence H0(E^{---}(3))=0 and the two interior derivative maps give

    H0(K(3)) <= H0(A0(1))+H0(A0(-1))
              = H0(B(1))+H0(B(-1)).             (2)

The equality holds because the line quotient in (1), even after twist one, has no sections. The actual second image is used, not its saturation in a larger target. Euler characteristics give

    chi_G(K(3))=U+Sym^(e-6)W-chi_G(B(3)).

Consequently a necessary representation inequality is

    U+Sym^(e-6)W <= chi_G(B(3))+H0(B(1))+H0(B(-1)). (3)

## 2. Exhaustive finite overlist for B

A rank-two center-even equivariant bundle is either O(n)+O(m) with n,m even, or R O(n) with R=W or Wprime and n odd. In all cases its ordinary degrees are at most six.

For a line degree n, the dimension contribution on the right of (3) is

    F(n)=n+4+max(n+2,0)+max(n,0).

The left dimension is e+9. Since F(6)=24, a line-pair candidate must have each degree at least e-19, that is -10 for e9 and -8 for e11. For an irreducible two-dimensional block, n<=-1 gives 2F(n)<=8<e+9; hence only n=1,3,5 need be tested.

The exact representation inequality (3) leaves seventeen candidates for e9 and thirteen for e11. We further require each splitting block to admit an equivariant map into the SAME one of the five Q(-2) types. Repeated equal line blocks require at least their multiplicity in the corresponding Hom space. This is only a necessary injection test; no generic injectivity is inferred from a nonzero Hom.

The survivors are the seven e9 B shapes stated in the result, plus

    e9 extras: O(-10)+O(6), O(-4)+O(4);

and the same seven B shapes for e11, plus

    e11 extra: O(-8)+O(6).

Thus seventeen B/e pairs remain at this stage. The verifier reproduces both finite lists, all five target types, and all Hom exclusions. In particular the tempting Wprime blocks and O(0) or O(-2) line blocks have no allowed target maps.

## 3. Three equality cases are impossible

For each extra pair just listed, (3) is equality. Equations (2) and Riemann--Roch therefore force H1(K(3))=0. Every ordinary summand of K has degree at least -4.

For e9 and B=O(-4)+O(4), sequence (1) splits and A0=O(-4)+O(4)+O(-8). The derivative K -> A0(-2) can reach only O(2), so its rank is at most one, not three.

For e11 and B=O(-8)+O(6), the sequence splits and A0=O(-8)+O(6)+O(-10). Again only the high O(4) target is reachable.

For e9 and B=O(-10)+O(6), retain the possible nonsplit extension. The O(6) block splits off, and the remaining extension of O(-8) by O(-10) is either their sum or W O(-9), by the ordinary Euler extension and equivariance. In either case every low degree of A0(-2) is below -4. Only O(4) is reachable. This excludes the third case without a false splitting assumption.

All fourteen remaining pairs have min degree B>=-4. Therefore

    Ext1(O(1-e),B)=H1(B(e-1))=0,

and (1) splits equivariantly after averaging.

## 4. Four further e11 cases cannot reach the low line

Define the genuine upper bound

    M=chi_G(B(3))+H0(B(1))+H0(B(-1))-U-Sym^(e-6)W.

Equations (2),(3) imply H1(K(3))<=M. Each negative splitting block R O(-j), j>=5, contributes R Sym^(j-5)W to that group. The bound also gives j<=dim(M)+4, so its positive-tail test is finite and exhaustive.

To map to the low line O(-e-1) in A0(-2), a block must additionally have

    Hom_G(R,Sym^(j-e-1)W) != 0.

For e11 the exact tests give:

    B=O(-4)+O(6), O(2)+O(4), O(2)+O(6), W O(3):
        no possible low-mapping block;
    B=2O(4): only O(-12);
    B=O(4)+O(6) or W O(5): only O(-12) or W O(-13).

The first four cases have zero low component in the actual derivative. Its image lies in B(-2), a rank-two bundle, contradicting rank three at the interior K stage. The final three e11 shapes, and all seven e9 shapes, are retained. No assertion that their low components exist or that the rest of their derivative is realizable is made.

## Reproduction

Run python3 verify_extremal_31_rank_one_ten_quotients.py. It checks the exhaustive degree bounds, exact representation inequalities, five-target Hom tests, equality cases, extension degrees, and all possible low-mapping negative blocks. Geometry of the actual saturated flags, characteristic-zero Gauss derivative and section persistence comes from the cited proofs. This is a new rank-one reduction, separate from the five rank-two first-quotient shapes.
