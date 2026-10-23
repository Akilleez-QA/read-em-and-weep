# The remaining split bf branch has a saturated split backward quotient

## Result and scope

For G3.11.863639aa192e, with original defect zero and

    A_q=O(-10)+O(4)+O(6),

consider the bf source, tuple (0,1,0,0,0,1,0,1),

    E=(P+D) O(-2)+T O(-3)+O(-8)+O(-10).

The remaining top-rank-one branch necessarily has the exact backward quotient

    E^-/E^{--}=O(2)+O(4),                        (1)

with saturated actual derivative image. The next kernel has an explicit source-free character interface recorded below. This note proves a forced subsystem, not by itself a full source or label exclusion.

The top-rank-two branch is excluded by PR814 combined with PR830:

https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/PROOF.md

https://github.com/Akilleez-QA/read-em-and-weep/blob/620d5598ccc19e5e1c458a4cddb0d3a0709d83c3/research/hm/profile11-split-bf-rank-two-exclusion/SPLIT-BF-RANK-TWO-NONZERO-CHANNEL.md

The first proof has SHA256 f0bd13d85ae8a890dbec84e5f15b7ec8605b04f474d5c7d80faeb3aa08f4defc and the second d762e23c6b402bf8bfd62160e310ecacf601a910d47f6a3e278cd8a3806657f6.

The original source and label inputs, strict-top lemma, and Gauss persistence conventions are those at db51525015bb7c5e825833d550d08dedf6f6ea96, pinned in these proofs. Work over C with the actual constant connection and binary icosahedral notation W,Wp,A,V,P,S,D,T. Nonempty invariant effective divisors have degree at least12.

## 1. The complete O(6) top and the nonzero lower T channel

Put F=(P+D) O(-2)=Sym^8 W O(-2). A rank-one top image has saturation O(k) in O(4)+O(6). Strict-top injects its nine coefficient sections into H0(O(k+2)), forcing k>=6. Since k<=6, the saturation is the O(6) direct summand and the map is the complete degree-eight system. Thus

    im(F->A_q)=O(6),
    ker(F->O(6))=(Wp+T) O(-3).                 (2)

Let E'=ker(E->A_q->O(-10)) and K_i=E^{(-i)}. The unique O(-10) source block maps isomorphically to that negative quotient, so

    E'=F+T O(-3)+O(-8),
    E'/K_1=O(4)+O(6).

Modulo the top image O(6), the map T O(-3)+O(-8)->O(4) is onto. Its T component is nonzero: if it vanished, the O(-8) component alone would be a degree-twelve section and could not be everywhere surjective. The nonzero irreducible degree-seven T system is basepoint-free because a common-zero divisor would be invariant of degree less than12.

At twist3, the image of F is Sym^9 W=S+T. The lower T adds a T line into the quotient O(4), so

    H0(K_1(3))=Wp+T,
    H1(K_1(3))=Wp+S.                            (3)

For the second equality, the section cokernel in H0(O(7)+O(9)) is Wp and H1(E'(3))=S; the cohomology sequence and complete reducibility give their sum. Also rank K_1=14, degree K_1=-54, maxdeg K_1<=-3.

## 2. The exact first kernel

A lower block Z O(-j), j>=5, contributes Z Sym^(j-5) W to H1(K_1(3)). Within the budget Wp+S, the only supported blocks are Wp O(-5), S O(-5), and O(-8). At j6, even coefficients of dimension at most3 give W, W+S, or T after tensoring W, none supported. At j7 the two possible doublets give W+S or T after tensoring A, also unsupported. At j8 the trivial coefficient gives S; j10 gives T, not supported, and the other later parity-allowed cases exceed the dimension budget.

Thus the lower contribution is either Wp O(-5)+S O(-5), or Wp O(-5)+O(-8). The twist4 character is

    chi_G(K_1(4))=2V+2P+D-A.                   (4)

The first possibility would require degree-minus-four coefficient V-A, which is not genuine. The second gives precisely V. Together with the top in (3), this forces

    K_1=(Wp+T) O(-3)+V O(-4)+Wp O(-5)+O(-8).  (5)

All its maps to O(-12) vanish by ordinary degrees, so its derivative lands in the split positive target O(2)+O(4).

## 3. Every possible failure of the full split image contradicts strict-top

The Wp O(-3) top block maps only to O(4), since Wp is absent from Sym^5 W=T. Strict-top makes this map nonzero; its degree-seven system is basepoint-free. Hence the derivative image contains the whole O(4) summand.

The only possible complementary channels to O(2) are

    T O(-3) -> O(2),
    V O(-4) -> O(2),
    Wp O(-5) -> O(2).

They are respectively irreducible systems of degrees5,6,7. Any nonzero one is basepoint-free and, together with O(4), gives the entire O(2)+O(4). The O(-8) block has no such channel because there is no degree-ten invariant.

Suppose all three complementary channels vanish. The raw derivative image is then exactly O(4). Strict-top identifies the section map of the top (Wp+T) O(-3) with the full Sym^7 W system, since both have eight sections. Its kernel is (V+P) O(-4).

Consequently K_2 fits into an extension of V O(-4)+Wp O(-5)+O(-8) by (V+P) O(-4). All ordinary Ext1 groups vanish, so

    K_2=(2V+P) O(-4)+Wp O(-5)+O(-8).

Its actual derivative lands in O(4)(-2)=O(2). Strict-top at twist4 would inject 2V+P into H0(O(6))=V+P, which is impossible. Thus some complementary channel is nonzero and (1) follows, with no divisor correction.

## 4. The source-free next-kernel interface

Rank and degree subtraction and strict-top give

    rank K_2=12, degree K_2=-60, maxdeg K_2<=-4,
    beta_(K_2) factors through O+O(2).

The source characters are

    chi_G(K_1(3))=T-S,
    chi_G(K_1(4))=2V+2P+D-A,
    chi_G(K_1(5))=-W+2Wp+S+4T.

Subtracting the characters of O(2)+O(4) gives the exact bounded interface

    H1(K_2(3))=Wp+S+T,
    chi_G(K_2(4))=V-A,
    chi_G(K_2(5))=-W+Wp+2T.                    (6)

This is a necessary actual-kernel subsystem. A separate split-target descent must be proved before inferring a source exclusion; the balanced W O(1) descent is not substituted for the different target O+O(2).

No selected source coefficients, parameters, points, evaluated derivatives, matrices, instance ranks, model experiments, scans, or unapproved large computation are used.
