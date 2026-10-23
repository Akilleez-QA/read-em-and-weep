# The balanced bb torsion branch enters the excluded finite descent

## Result and exact scope

For the balanced original-zero-defect label G3.11.73682b4c817f,

    A_q=O(-10)+W O(5), B_q=W O(-7)+O(8),

consider the bb source, tuple (0,2,0,0,0,0,0,1),

    E=P O(-2)+2T O(-3)+O(-10), F=P O(-2).

The generic-rank-two top-image branch with determinant defect12 is impossible. The new step is a universal interface calculation: it forces the first two backward quotients W O(3), W O(1), and then exactly the character budgets used by the published finite backward exclusion. That argument then gives a contradiction.

This proof alone excludes only the stated torsion branch. A separate onto-branch exclusion is not a dependency. No entire stable label is excluded here.

## Immutable public inputs

The defect-twelve top-image and actual cubic subsystem are established in PR819, immutable commit 03fee9278072f9ac00a5fcee5deb04b7fce61ae5:

https://github.com/Akilleez-QA/read-em-and-weep/blob/03fee9278072f9ac00a5fcee5deb04b7fce61ae5/research/hm/profile11-balanced-low-positive-subsystems/BALANCED-TORSION-CUBIC-SUBSYSTEM.md

Its SHA256 is b1a6b94b0e1a7cce942af8e52d4bcc59317ce9d8c6823610e5d288da0c62429f. In particular the raw top image is I=Wp O(-1), and F->I is onto.

The finite backward exclusion is PR823, immutable commit 399abe93debe71232f0b7808fc8f1a5582118708, under research/hm/profile11-balanced-bf-backward-exclusion/:

https://github.com/Akilleez-QA/read-em-and-weep/blob/399abe93debe71232f0b7808fc8f1a5582118708/research/hm/profile11-balanced-bf-backward-exclusion/BF-THIRD-BACKWARD-QUOTIENT.md

https://github.com/Akilleez-QA/read-em-and-weep/blob/399abe93debe71232f0b7808fc8f1a5582118708/research/hm/profile11-balanced-bf-backward-exclusion/BF-FINITE-BACKWARD-DESCENT.md

Their SHA256 hashes are respectively

    16475cd7d6012fff2efd8d3ec04bce884231ffbfe664914e948584c24afa69d0,
    9558490385822a4d559d555c4f3372fd594e7ef0f504454da0707d962cf9fd49.

Those proofs were stated for another source. Section4 below explicitly identifies the source-free interface at which their arguments apply; no quartic subsystem or source-specific earlier quotient is imported.

The original source, stable label, strict-top lemma, and Gauss-rank persistence conventions are at db51525015bb7c5e825833d550d08dedf6f6ea96, under research/hm/order-four-quadratic-load/, as pinned in the cited proofs. In particular the original profile-(1,1) backward endpoint has rank at most two. Work over C, with the actual constant connection and binary icosahedral notation of those inputs. A nonempty invariant effective divisor has degree at least12.

## 1. The first backward kernel has exactly Wp+T top sections

Put K_i=E^{(-i)}, K_0=E, and put E'=ker(E->A_q->O(-10)). Only the O(-10) source block maps to that negative quotient; its restriction is an isomorphism. Thus

    E'=P O(-2)+2T O(-3),
    E'/K_1=W O(5), rank K_1=14, deg K_1=-54.     (1)

Strict-top gives maxdeg K_1<=-3. At twist3, source and target sections are

    H0(E'(3))=Wp+3T,
    H0(W O(8))=Wp+S+2T.                         (2)

The image of H0(F(3)) is exactly one T multiplicity line: F->I=Wp O(-1) is onto, its kernel is Wp O(-3), and

    H0(I(3))=Wp Sym^2 W=T.

The two lower T O(-3) blocks can map only to the two T occurrences in the target of (2). Their combined image together with F must span both T multiplicity lines. Otherwise the entire image of H0(E'(3)) would equal the already present T from I(3). The bundle E'(3) is globally generated, as is I(3); equality of those section images would force the bundle image of E'->W O(5) to lie in the proper defective sheaf I, contradicting its surjectivity in (1).

Consequently the section map in (2) has image exactly2T, and

    H0(K_1(3))=Wp+T,
    H1(K_1(3))=Wp+S.                            (3)

The first identity gives an actual saturated top block (Wp+T) O(-3) inside K_1. No selected source-map rank has been evaluated; the section multiplicity rank is forced by the surjectivity and the known defective top image.

## 2. The first backward quotient is the full W O(3)

Derivatives of K_1 land in

    (E/K_1)(-2)=O(-12)+W O(3).

On its top block in (3), the negative component vanishes by ordinary degrees. Strict-top injects all eight top sections into the actual image in W O(3).

That top image cannot have generic rank one. Its saturated equivariant line would be O(k) with k<=2, by parity and the bound k<=3 for a line in W O(3). At twist3 it has at most six sections, too few for the eight independent sections in (3).

Let delta be the torsion length of the generic-rank-two top image in W O(3). Twisting by3 gives a globally generated rank-two image of degree12-delta, with h0=14-delta. Thus

    8<=14-delta, so delta<=6.

Equivariance and the minimum invariant divisor degree imply delta=0. Hence the top derivative already contains the entire saturated W O(3) summand.

The endpoint rank bound is at most two. Any nonzero remaining component into O(-12) would increase the generic rank beyond two. Since that negative line is torsion-free, the component is identically zero. Therefore the actual quotient is

    K_1/K_2=W O(3),                              (4)

with no divisor correction. It follows that rank K_2=12, degree K_2=-60, and maxdeg K_2<=-4.

## 3. A forced V top block gives the second full quotient

Euler characteristics from (1) give

    chi_G(K_1(4))=2V+2P+D-A.

Indeed P Sym^2 W=V+P+D, T W=V+P+D, and W Sym^9 W=A+V+P+2D. Subtracting the twist4 character of (4), namely W Sym^7 W=V+2P+D, yields

    chi_G(K_2(4))=V-A.                           (5)

Since H0 and H1 are genuine representations, (5) forces H0(K_2(4)) to contain V. The degree bound maxdeg K_2<=-4 therefore supplies an actual saturated V O(-4) subblock of K_2.

Its derivative lands in (K_1/K_2)(-2)=W O(1) and is nonzero by strict-top. It cannot have generic rank one: a saturated equivariant line in W O(1) is O(k) with even k<=0. At twist4 its section representation is respectively Sym^4 W=D, Sym^2 W=A, the trivial representation, or zero. None contains V.

The derivative of this V block thus has generic rank two. If its defect is delta, its twist4 image is globally generated of rank two and degree10-delta, so

    3<=12-delta, hence delta<=9.

Again invariance forces delta=0. This V block alone maps onto W O(1), proving the exact saturated quotient

    K_2/K_3=W O(1).                              (6)

Consequently rank K_3=10, degree K_3=-62 and maxdeg K_3<=-5.

## 4. Verify the exact published descent interface

The derivative of K_3 lands in W O(-1). Subtracting (6) from (5) at twist4 gives

    chi_G(K_3(4))=-(A+P+D).

The degree bound makes H0(K_3(4))=0, hence

    H1(K_3(4))=A+P+D.                            (7)

At twist5, the identities

    P Sym^3 W=S+2T,
    T Sym^2 W=Wp+S+2T,
    W Sym^10 W=W+2S+2T

give chi_G(K_1(5))=-W+2Wp+S+4T. Subtracting W Sym^8 W=Wp+S+2T and W Sym^6 W=Wp+2T from the two exact quotients (4),(6) yields

    chi_G(K_3(5))=-W.                            (8)

Equations (7)-(8), rank10, degree-62, maxdeg<=-5, and derivative target W O(-1) are exactly the hypotheses used from Section1 onward in the published BF-THIRD-BACKWARD-QUOTIENT proof. Its preliminary quartic argument is not used here: (4) and (6) have been proved directly for the present cubic torsion source.

For explicitness, the source-free support argument in that section uses only (7)-(8) and central parity. It leaves the four types

    I:   S O(-5)+P O(-6)+W O(-9);
    II:  (P+D) O(-6)+O(-8);
    III: S O(-5)+P O(-6)+O(-8)+O(-10);
    IV:  T O(-5)+(V+1) O(-8).

Its next two sections exclude generic derivative rank one by strict-top, then prove saturation of the rank-two image using the top Euler-line and complementary P or T channels. Those steps depend solely on these four types and target W O(-1). They therefore give here, exactly as there,

    K_3/K_4=W O(-1).                             (9)

The published BF-FINITE-BACKWARD-DESCENT then starts with exactly the four types and (9). Every subsequent kernel, Hom and Ext calculation, strict-top contradiction, and saturation argument is source-independent. In the same indices it forces

    K_4/K_5=W O(-3),
    K_5/K_6=W O(-5),
    K_6=O(-8)+W O(-9)+O(-18).

At the final step its actual raw image is

    K_6/K_7=O(-8)+O(-18) subset W O(-7),

with determinant defect12, and K_7=W O(-9). The defect is retained, not replaced by saturation. The derivative of K_7 factors through the raw quotient twisted by -2, namely O(-10)+O(-20), to which there is no nonzero map from W O(-9). Thus K_7 is a negative-degree horizontal saturated subbundle of the original constant bundle, impossible in characteristic zero.

This verifies all inputs needed to transfer the published finite descent and completes the torsion-branch exclusion.

## Boundary

The proof uses no onto-bb result and does not claim a full-label exclusion. Its new contribution is the exact cubic-torsion-to-finite-descent interface (3)-(8). All calculations are bounded abstract representation identities or universal bundle/connection arguments. No actual source coefficients, parameters, points, evaluated derivatives, matrices, instance ranks, selected-model experiments, scans, or unapproved large computation are used.
