# The balanced bc source is forced into the excluded backward descent

## Result and scope

For the original-zero-defect balanced label G3.11.73682b4c817f,

    A_q=O(-10)+W O(5), B_q=W O(-7)+O(8),

the bc source, tuple (0,1,1,0,0,0,0,1), is impossible:

    E=(V+P) O(-2)+T O(-3)+V O(-4)+O(-10).

The rank-two top-image branch was already excluded in PR814. This note excludes the remaining rank-one top branch. It does not, by itself, exclude the entire stable label.

The main new point is that the first backward derivative is forced to have the full saturated image W O(3), including when the lower T channel vanishes. A possible degree-twelve defect at that backward step is explicitly retained and then excluded by strict-top. The second quotient and the published finite descent then give the contradiction.

## Immutable inputs

PR814 at commit 1f94be65b3a470a1b594e61d56df7f6057c9d907 gives the top-rank-two exclusion and the strict-top and saturation conventions:

https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/PROOF.md

Its proof SHA256 is f0bd13d85ae8a890dbec84e5f15b7ec8605b04f474d5c7d80faeb3aa08f4defc. Original source and label data are pinned there at db51525015bb7c5e825833d550d08dedf6f6ea96.

The source-free finite descent is supplied by the two proofs of PR823 at immutable commit 399abe93debe71232f0b7808fc8f1a5582118708:

https://github.com/Akilleez-QA/read-em-and-weep/blob/399abe93debe71232f0b7808fc8f1a5582118708/research/hm/profile11-balanced-bf-backward-exclusion/BF-THIRD-BACKWARD-QUOTIENT.md

https://github.com/Akilleez-QA/read-em-and-weep/blob/399abe93debe71232f0b7808fc8f1a5582118708/research/hm/profile11-balanced-bf-backward-exclusion/BF-FINITE-BACKWARD-DESCENT.md

Their respective SHA256 hashes are 16475cd7d6012fff2efd8d3ec04bce884231ffbfe664914e948584c24afa69d0 and 9558490385822a4d559d555c4f3372fd594e7ef0f504454da0707d962cf9fd49. Section6 below specifies and checks the exact interface at which their source-independent arguments are used. Neither a quartic subsystem nor any unpublished continuation is assumed.

Work over C with the actual trivial connection on H O and the binary icosahedral representations of the cited proofs. Nonempty invariant divisors have degree at least12. The profile-(1,1) backward endpoint gives rank beta_(E^-)<=2.

## 1. The top image is the complete O(4) subsystem

Write F=(V+P) O(-2)=Sym^6 W O(-2). Its actual top image cannot be zero by strict-top, and its rank-two alternative is excluded by PR814. Its rank-one saturation in W O(5) is an equivariant O(k), with even k<=4. Strict-top injects the seven-dimensional V+P into H0(O(k+2)), forcing k=4. This is the unique Euler O(4) subline of W O(5), and the top map is its complete degree-six system. It is onto everywhere. Thus

    im(F->A_q)=O(4),
    ker(F->O(4))=T O(-3).                       (1)

Let E'=ker(E->A_q->O(-10)). The negative quotient is an isomorphism on the unique O(-10) source block, so

    E'=(V+P) O(-2)+T O(-3)+V O(-4),
    E'/K_1=W O(5),  K_i=E^{(-i)}.

Hence rank K_1=14, degree K_1=-54, and maxdeg K_1<=-3. At twist3,

    H0(E'(3))=Wp+3T,
    H0(W O(8))=Wp+S+2T.

The image of F at that twist is H0(O(7))=Wp+T. The lower T O(-3) has a component into the Euler quotient W O(5)/O(4)=O(6). There are precisely two cases, according as that component is zero or nonzero. The V O(-4) block has no sections at twist3 and does not affect this distinction.

The common Euler characters needed below are

    chi_G(K_1(3))=T-S,
    chi_G(K_1(4))=2V+2P+D-A,
    chi_G(K_1(5))=-W+2Wp+S+4T.                  (2)

They follow directly from E'/K_1=W O(5), using

    V W=T, V A=P+D, P A=V+P+D,
    V S=Wp+S+T, P S=S+2T, T A=Wp+S+2T.

## 2. A vanishing lower-T quotient channel already forces W O(3)

Suppose T O(-3)->O(6) is zero. Then its section image at twist3 is contained in the top O(4) image, so

    H0(K_1(3))=2T.                              (3)

The derivative of this actual top block lands in W O(3), since its map to the other summand O(-12) of (E/K_1)(-2) vanishes by degrees. Strict-top injects all twelve top sections into its image.

A generic rank-one image has saturation O(k) with even k<=2, hence at most six sections at twist3. It cannot contain twelve independent sections. The image therefore has rank two. If its determinant defect is delta, its twist3 image is generated of rank two and degree12-delta, so

    12<=14-delta, hence delta<=2.

Invariance forces delta=0. Thus the top block supplies the whole W O(3). The endpoint rank bound at most two eliminates any additional O(-12) component, and the actual quotient is

    K_1/K_2=W O(3).                             (4)

This argument does not assume the lower T quotient channel is nonzero.

## 3. A nonzero lower-T quotient channel forces an exact small kernel

Now suppose T O(-3)->O(6) is nonzero. On sections at twist3 it adds a T line to the image Wp+T from F. Therefore

    H0(K_1(3))=T,
    H1(K_1(3))=S.                               (5)

These identities and (2) determine K_1. A block Z O(-j), j>=5, contributes Z Sym^(j-5) W to H1(K_1(3)). Within the irreducible four-dimensional S budget, the only possibilities are S O(-5) or O(-8). Indeed at j5 the coefficient must be S; at j6 the only dimension-allowed even coefficient is trivial and gives W, not S; odd j7 already exceeds the budget; at j8 the trivial coefficient gives S; all later admissible degrees exceed the dimension budget.

The degree-minus-three block is T by (5). If the lower contribution were S O(-5), the twist4 character would require degree-minus-four coefficient V+P-A, which is not genuine. If it is O(-8), its twist4 H1 is A, and (2) forces coefficient V+P. Thus uniquely

    K_1=T O(-3)+(V+P) O(-4)+O(-8).              (6)

In particular every component of K_1->O(-12) is zero by degrees. Its entire derivative lies in W O(3).

## 4. All exceptional images of the first backward derivative are impossible

Apply the derivative to the T O(-3) top in (6). It is nonzero by strict-top. If its generic rank is two, the same generation bound gives defect delta<=8<12, so the top already maps onto W O(3), proving (4).

Suppose its rank is one. Its saturated line is O(k), with even k<=2. Six independent top sections force k=2, and the T map is the complete quintic system onto the Euler O(2) subline. Project the remaining derivative to the Euler quotient

    0 -> O(2) -> W O(3) -> O(4) -> 0.

The V O(-4) block has zero quotient channel because V is absent from Sym^8 W=P+D. The P O(-4) block has the unique P channel of degree8. If nonzero, it is basepoint-free, since its invariant common-zero divisor would have degree less than12. Together with the full Euler line, it makes the image all of W O(3), again proving (4).

It remains to consider a zero P quotient channel. Only O(-8) can then contribute to the Euler quotient O(4).

If that last channel is zero, the raw derivative image is exactly O(2). Its kernel K_2 is an extension of (V+P) O(-4)+O(-8) by the quintic evaluation kernel D O(-4). The extension splits by ordinary H1 vanishing. Hence

    K_2=(V+P+D) O(-4)+O(-8).

Its derivative lands in O(2)(-2)=O. Strict-top at twist4 would inject V+P+D into H0(O(4))=D, impossible.

If the O(-8)->O(4) channel is nonzero, its image is O(-8), with divisor degree12. Retain this defect. The full raw image I fits into

    0 -> O(2) -> I -> O(-8) -> 0,

which splits since H1(O(10))=0. The kernel K_2 is now an extension of (V+P) O(-4) by D O(-4), also split, so

    I=O(2)+O(-8), K_2=(V+P+D) O(-4).

The actual derivative of K_2 lands in I(-2)=O+O(-10), not in the saturation W O(1). Strict-top at twist4 again would inject V+P+D into D, impossible. This excludes the nonsaturated rank-two image rather than silently replacing it by its saturation.

All cases therefore give the exact quotient (4).

## 5. The second quotient is the full W O(1)

Subtracting (4) from (2) at twist4 gives

    chi_G(K_2(4))=V-A.

Also rank K_2=12, degree K_2=-60, and maxdeg K_2<=-4. Thus H0(K_2(4)) contains V and supplies an actual V O(-4) top subblock. Its derivative into (K_1/K_2)(-2)=W O(1) is nonzero by strict-top.

Its image cannot have rank one. A saturated equivariant line in W O(1) has even degree<=0, so at twist4 its sections are D, A, the trivial representation, or zero, none containing V. Its rank-two defect satisfies delta<=9 by the generated-image estimate 3<=12-delta. Invariance again forces zero defect. Thus

    K_2/K_3=W O(1),
    rank K_3=10, deg K_3=-62, maxdeg K_3<=-5.    (7)

## 6. The published finite descent applies at an exact source-free interface

The derivative of K_3 lands in W O(-1). Equations (2), (4), (7) give

    H1(K_3(4))=A+P+D,
    chi_G(K_3(5))=-W.                           (8)

For the first identity, the twist4 character is -(A+P+D) and H0 is zero by maxdeg<=-5. For the second, subtract W Sym^8 W=Wp+S+2T and W Sym^6 W=Wp+2T from the twist5 character in (2).

These are exactly the rank, degree, degree-bound, target and two character inputs used from Section1 onward of BF-THIRD-BACKWARD-QUOTIENT in PR823. That argument first produces its four necessary K_3 types and then forces K_3/K_4=W O(-1). Its preceding source-specific quartic construction is not imported; (4) and (7) have been proved here independently.

BF-FINITE-BACKWARD-DESCENT starts solely from those four types and that quotient. Its universal kernel, Hom, Ext and strict-top calculations force W O(-3), W O(-5) as the next two quotients, and then

    K_6=O(-8)+W O(-9)+O(-18),
    K_6/K_7=O(-8)+O(-18) subset W O(-7),
    K_7=W O(-9).

The last raw image has determinant defect12, retained in that proof. The derivative of K_7 factors through its twist O(-10)+O(-20), to which W O(-9) has no nonzero map. This makes a negative saturated subbundle horizontal, impossible in characteristic zero.

Thus the rank-one top branch of balanced bc is excluded. Together with the public rank-two top exclusion, the entire stated bc source is impossible.

## Boundary

No other source or entire label is counted as excluded by this note alone. It uses universal exact-sequence and actual-connection arguments and bounded abstract representation identities only. No selected source coefficients, parameters, points, evaluated derivatives, matrices, instance ranks, experiments, scans, or unapproved large computation are used.
