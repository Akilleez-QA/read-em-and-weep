# The split bc source is forced into the universal split descent

## Result and scope

For the original-zero-defect profile-(1,1) label G3.11.863639aa192e, source index 69, the source tuple

    (0,1,1,0,0,0,0,1)

is impossible. The source and quotient are

    E=(V+P) O(-2)+T O(-3)+V O(-4)+O(-10),
    A_q=O(-10)+O(4)+O(6).

This is a source-stratum exclusion, not an entire-label exclusion. The rank-two top-image branch was excluded publicly in PR814. This note excludes the remaining rank-one top branch, without evaluating any selected actual source.

## Immutable inputs and local theorem dependency

PR814, immutable commit 1f94be65b3a470a1b594e61d56df7f6057c9d907, supplies the source and label data, the rank-two top exclusion, strict-top conventions, and original-data pins:
https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/PROOF.md

Its proof SHA256 is f0bd13d85ae8a890dbec84e5f15b7ec8605b04f474d5c7d80faeb3aa08f4defc. Original source and label data are pinned there at db51525015bb7c5e825833d550d08dedf6f6ea96.

The proof below verifies the exact input interface of the companion source-free theorem SPLIT-BACKWARD-DESCENT.md. That theorem must be published together with this note, or pinned immutably when this note is published. It independently rederives every split quotient and does not import a balanced-target conclusion. The balanced-bc argument is not a dependency.

Work over C with the binary icosahedral representations defined in those proofs. Write U[d]=U tensor O(d). The original ambient bundle carries its actual trivial connection. Set Ki=E^{(-i)}. The profile-(1,1) endpoint gives generic derivative rank at most two from K1 onward; outward Gauss ranks are nonincreasing. Actual backward kernels are saturated in the same constant ambient bundle, strict-top lowers the maximal degree at each step, and the derivative of Ki+1 factors through (Ki/Ki+1)(-2). Nonempty invariant divisors have degree at least twelve.

## 1. The rank-one top image is exactly the complete O(4)

Put F=(V+P)[-2]=Sym6 W[-2]. Its actual top image in O(4)+O(6) is nonzero by strict-top. Its rank-two case is publicly excluded, so let its rank-one saturation be an equivariant line O(k). Since G has no nontrivial one-dimensional characters and the bundles are center-even, k is even. Also k<=6.

At k=6 the line is the direct O(6) summand by ordinary degrees, but strict-top would inject V+P into Sym8=P+D, impossible. At k<=2 its twist-two section dimension is at most five, smaller than seven. Thus k=4. The equivariant O(4) line is precisely the direct summand, since Hom_G(O(4),O(6))=(Sym2 W)^G=0. Its map from F is the complete sextic section system, so it is onto everywhere, with kernel T[-3].

The negative O(-10) quotient of E is an isomorphism on the unique O(-10) source block; all higher-degree blocks have zero maps to that line. Remove this quotient and write

    E'=ker(E->A_q->O(-10))=(V+P)[-2]+T[-3]+V[-4].

The graph is harmless: E' is isomorphic to the displayed higher-degree sum, and maps onto O(4)+O(6), with kernel K1. Consequently

    rank K1=14, deg K1=-54, maxdeg K1<=-3.

At twist three,

    H0(E'(3))=Wp+3T,
    H0(O(7)+O(9))=Wp+S+2T,

and the top F image is H0(O(7))=Wp+T. The lower T[-3] component into O(6) is therefore the sole distinction at this twist. The common Euler characters, computed from the exact E' quotient, are

    chi(K1(3))=T-S,
    chi(K1(4))=2V+2P+D-A,
    chi(K1(5))=-W+2Wp+S+4T.                       (1)

Directly, the two latter identities are

    chi(K1(4))=(V+P) Sym2+T Sym1+V
               -Sym8-Sym10=2V+2P+D-A,
    chi(K1(5))=(V+P) Sym3+T Sym2+V Sym1
               -Sym9-Sym11=-W+2Wp+S+4T.

They use V A=P+D, P A=V+P+D, V S=Wp+S+T, P S=S+2T, T A=Wp+S+2T. The formulas, not the existence of an abstract splitting of the connection, are the input.

## 2. A zero lower-T O(6) channel forces the full first split quotient

Suppose T[-3]->O(6) is zero. Its sections map into the top O(4) image, so

    H0(K1(3))=2T.

The actual top block 2T[-3] differentiates into O(2)+O(4): its component into the remaining O(-12) target is zero by degrees. Strict-top makes all twelve top sections independent in its image.

A rank-one image has an equivariant saturated line O(k), k even and k<=4. If k=4, that line is the direct O(4) summand and its twist-three sections Sym7=Wp+T contain only one copy of T, not two. If k<=2, there are at most six sections. Thus the top derivative has rank two.

Let delta be its determinant defect in O(2)+O(4). Its twist-three image is globally generated of rank two and degree 12-delta, so

    12 <= h0(image(3))=14-delta.

Hence delta<=2. Invariance forces delta=0. The top already supplies the full O(2)+O(4). The endpoint rank bound at most two rules out any further O(-12) component in the full image. Therefore

    K1/K2=O(2)+O(4).                               (2)

Indeed an additional nonzero projection to O(-12) would raise generic rank to three once both positive direct summands were contained.

## 3. A nonzero lower-T O(6) channel determines K1

If T[-3]->O(6) is nonzero, its twist-three section image gives an independent T in the quotient by H0(O(7)). Thus

    H0(K1(3))=T,    H1(K1(3))=S.                  (3)

The S budget determines the possible lower blocks. A block U[-j], j>=5, contributes U Sym(j-5) to H1(K1(3)), with parity U=(-1)^j. At j5 only S[-5] fits; at j6 only the trivial coefficient is dimension-eligible and gives W, not S; odd j7 already has minimum dimension six; at j8 the trivial coefficient gives S; all later admissible degrees exceed the budget. Hence the only lower possibilities are S[-5] or O(-8), in addition to the T[-3] top and degree-minus-four blocks.

If S[-5] occurred, the twist-four character (1) would require degree-minus-four coefficient V+P-A, not genuine. If O(-8) occurs, its twist-four H1 is A, and (1) forces coefficient V+P. Thus

    K1=T[-3]+(V+P)[-4]+O(-8).                      (4)

All components of (4) to O(-12) vanish by degrees. Its entire derivative therefore lies in O(2)+O(4).

## 4. Exhaust the T-top derivative channels without discarding torsion

Strict-top makes the T[-3] derivative nonzero. If it has nonzero components to both O(2) and O(4), it has generic rank two. To see this carefully, a rank-one saturation O(k) would need six independent twist-three sections, hence even k>=2. For k=4 it cannot project to O(2); for k=2 its projection to O(4) vanishes equivariantly because (Sym2 W)^G=0. Neither is compatible with both rows nonzero.

The rank-two top image is globally generated after twist three. Its defect delta therefore satisfies 6<=14-delta, so delta<=8<12 and delta=0. This proves (2) in that case.

### 4.1 The T top maps only onto O(2)

This is its complete quintic system, with kernel D[-4]. Of the (V+P)[-4] blocks only P can map to O(4), because Sym8=P+D excludes V. If the P row is nonzero, its degree-eight system is basepoint-free and gives the full second line, proving (2).

If the P row vanishes, only O(-8) can contribute to O(4). If that last channel vanishes too, the raw image is O(2) and the kernel is

    K2=(V+P+D)[-4]+O(-8).

The extensions by D[-4] split, since the quotient degrees are -4 and -8. Its next derivative targets O(0), so strict-top at twist four would inject V+P+D into Sym4=D. Impossible.

If O(-8)->O(4) is nonzero, it is a scalar multiple of f12 and has its invariant degree-twelve divisor. Retain this defect. Since the full O(2) direct summand is already contained, the actual raw image and kernel are

    I=O(2)+O(-8),    K2=(V+P+D)[-4].

The actual next derivative targets I(-2)=O(0)+O(-10), not the saturation O(0)+O(2). Its twist-four section character is still only D, giving the same strict-top contradiction. Thus this nonsaturated possibility is excluded explicitly.

### 4.2 The T top maps only onto O(4)

Its T subsystem of Sym7=Wp+T is basepoint-free, since degree seven is below twelve. The kernel is

    V[-4]+Wp[-5].                                  (5)

Indeed H1 at twist three is Wp. The same dimension-and-parity argument as above supports only Wp[-5] below degree -4; at twist four the Euler character is

    T W-Sym8=(V+P+D)-(P+D)=V,

forcing V[-4].

Both V[-4] and P[-4] from the lower source part of (4) have possible degree-six rows to O(2). Any nonzero one is basepoint-free, so it supplies O(2) and proves (2).

If both vanish, O(-8) has no O(2) row because Sym10 has no invariant. The raw image is exactly O(4). Its kernel is

    K2=(2V+P)[-4]+Wp[-5]+O(-8).

This follows from (5) and the remaining source blocks; the only least-positive Ext degree is (-5)-(-4)=-1, so every extension splits. Its derivative targets O(2), and strict-top at twist four would inject 2V+P into Sym6=V+P, impossible by V multiplicity.

All possibilities therefore force the full exact quotient (2).

## 5. Verify the source-free split-descent interface

From (1),(2), rank and degree subtraction give

    rank K2=12, deg K2=-60, maxdeg K2<=-4,
    chi(K2(4))=V-A,
    chi(K2(5))=-W+Wp+2T.

For the last two equalities, subtract respectively

    Sym6+Sym8=V+2P+D,
    Sym7+Sym9=Wp+S+2T

from the twist-four and twist-five characters in (1). The actual derivative of K2 takes values in

    (K1/K2)(-2)=O(0)+O(2),

which is an actual subbundle of (H O/K2)(-2), since K1 is saturated in H O. Thus the kernel and raw image agree with those of the actual derivative, not merely with an abstract factorization.

The generic rank bound and actual-kernel factorization persist. These are exactly the hypotheses of the companion universal split-descent lemma, which gives a contradiction. No source-specific constant subsystem or additional source equation is needed after this interface.

Consequently the rank-one top branch is impossible. Together with PR814's rank-two top exclusion, the entire stated split bc source is excluded.

## Boundary and verification requirements

This note concerns only the stated tuple on the stated original-zero-defect split label. It does not exclude any other source or the entire label. The companion universal lemma remains independently reusable for any actual configuration meeting its precise interface.

All cases of the lower T channel, all T-top image types, and the possible f12 torsion image have been included. The proof uses actual connection kernels, complete evaluation kernels, bounded representation identities, invariant-divisor bounds, and explicit Ext vanishing only. It uses no selected coefficients, parameters, points, evaluated derivatives, matrices, source-instance ranks, experiments, scans, or unapproved large computation. Both this proof and its companion theorem require fresh independent review before publication.
