# Independent review: balanced bb torsion enters the finite backward exclusion

## Verdict and exact scope

**PASS, with no mathematical correction required.** This review applies to the exact bytes of `BALANCED-BB-TORSION-DESCENT-EXCLUSION.md`, SHA256

`db935dd621f64b9336727919f4af4710ceeac03f432d567c9530db9ba5eb10e8`.

Under its stated actual-bundle and profile-(1,1) hypotheses, the proof excludes the generic-rank-two, determinant-defect-twelve top-image branch of

    E=P O(-2)+2T O(-3)+O(-10), F=P O(-2),
    A_q=O(-10)+W O(5), B_q=W O(-7)+O(8),

for stable label G3.11.73682b4c817f, source index72, tuple (0,2,0,0,0,0,0,1).

The new interface is valid: it forces the actual quotients K_1/K_2=W O(3) and K_2/K_3=W O(1), then the precise K_3 character budgets needed by the finite descent. The imported arguments after that interface use no distinguishing property of the bf source or its quartic subsystem. The final quotient is the raw defective image O(-8)+O(-18), not its saturation; retaining it gives the negative horizontal kernel contradiction.

This review does not exclude the entire stable label and does not review, assume, or require an onto-bb exclusion. The contribution is the stated torsion-branch exclusion only.

## 1. Frozen public inputs and verification boundary

The cubic torsion input is [BALANCED-TORSION-CUBIC-SUBSYSTEM.md at the PR819 commit](https://github.com/Akilleez-QA/read-em-and-weep/blob/03fee9278072f9ac00a5fcee5deb04b7fce61ae5/research/hm/profile11-balanced-low-positive-subsystems/BALANCED-TORSION-CUBIC-SUBSYSTEM.md), immutable commit

`03fee9278072f9ac00a5fcee5deb04b7fce61ae5`, SHA256

`b1a6b94b0e1a7cce942af8e52d4bcc59317ce9d8c6823610e5d288da0c62429f`.

The two continuation inputs are at the PR823 immutable commit

`399abe93debe71232f0b7808fc8f1a5582118708`:

- [BF-THIRD-BACKWARD-QUOTIENT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/399abe93debe71232f0b7808fc8f1a5582118708/research/hm/profile11-balanced-bf-backward-exclusion/BF-THIRD-BACKWARD-QUOTIENT.md), SHA256 `16475cd7d6012fff2efd8d3ec04bce884231ffbfe664914e948584c24afa69d0`.
- [BF-FINITE-BACKWARD-DESCENT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/399abe93debe71232f0b7808fc8f1a5582118708/research/hm/profile11-balanced-bf-backward-exclusion/BF-FINITE-BACKWARD-DESCENT.md), SHA256 `9558490385822a4d559d555c4f3372fd594e7ef0f504454da0707d962cf9fd49`.

All four SHA256 values, including the reviewed proof, were recomputed from the supplied files and match. The local copies of the original geometric lemmas also match their pinned Git blob IDs at commit `db51525015bb7c5e825833d550d08dedf6f6ea96`:

- [Actual equivariant splitting and Gauss persistence](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md), blob `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
- [Negative Gauss kernels strictly lower the top slope](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md), blob `d7506dae49b4be43230450c4132bd5db91f137ef`.
- [Profile-(1,1) endpoint conventions](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md), blob `dcacf0bcdef8377c1ed7654e5b82659ea409456e`.

The source and label remain those of the [frozen frontier](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json), blob `8b5971092f9ef762584912609fd5e9301c4e271d`, and [necessary-pair list](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json), blob `fe0afa410d89340d3082dc814277f89fbb582c19`.

The present review independently checks the new interface and the source independence of every imported continuation stage. It treats the pinned cubic theorem and original actual-bundle setup as inputs, not as conclusions obtained from an abstract splitting alone. No selected source coefficients, points, evaluated derivatives, instance matrices or ranks were used. The only arithmetic verification was a fixed finite list of abstract representation identities and byte hashes.

## 2. Geometric rules and the first section map

Write K_i=E^(-i). Each K_i is the actual derivative kernel in the same constant ambient bundle. It is saturated there: the derivative image is torsion-free on the smooth curve, hence locally free, and the two successive ambient quotients are locally free. Consequently strict-top applies at every stage. Starting with maxdeg E<=-2 gives maxdeg K_i<=-2-i.

If K_(i+1) is the derivative kernel of K_i, the next derivative lands in the **actual** quotient (K_i/K_(i+1))(-2). This remains true when that quotient has a defective embedding into an earlier target. Equivariant splitting is used only for cohomology and bundle maps, not as a splitting of the connection.

The map E->O(-10) is zero on P O(-2)+2T O(-3) by ordinary degrees. Surjectivity of E->A_q forces its remaining scalar O(-10)->O(-10) to be nonzero. Therefore

    E'=ker(E->O(-10))=P O(-2)+2T O(-3),
    0 -> K_1 -> E' -> W O(5) -> 0.

In particular rank K_1=14 and degree K_1=-54. Any positive component of the O(-10) block in E->A_q does not affect this exact sequence.

The pinned cubic input gives the actual raw top image I=Wp O(-1) and the onto map

    0 -> Wp O(-3) -> F -> I -> 0.

After twist3, H1(Wp O)=0, so the map on sections from F(3) onto I(3) is onto. Its image is precisely one T multiplicity line in

    H0(W O(8))=Wp+S+2T,

because H0(I(3))=Wp Sym2 W=T. Meanwhile

    H0(E'(3))=P W+2T=Wp+3T.

The lower two T blocks can contribute only to the target's T-isotypical component. If the total image had multiplicity one in T, it would coincide with the image of H0(I(3)). Since E'(3) is globally generated, its sheaf image would then be contained in the subsheaf generated by these sections, which is I(3). Here I(3)=Wp O(2) is itself globally generated, so this generated subsheaf is exactly I(3), not a larger saturation. That contradicts E'(3)->W O(8) being onto, since I is a proper defective subsheaf of W O(5).

Thus the image has exactly two T multiplicities, and semisimplicity gives

    H0(K_1(3))=Wp+T,
    H1(K_1(3))=Wp+S.

The word “exactly” is justified: F supplies only T, and the remaining blocks can supply only T. No Wp or S section channel is available in the image. With maxdeg K_1<=-3, its twist3 section evaluation identifies the actual saturated top block (Wp+T) O(-3).

## 3. First actual quotient: W O(3)

The derivative of K_1 lands in

    (E/K_1)(-2)=O(-12)+W O(3).

Its top degree-minus-three block has zero map to O(-12). Strict-top injects all eight top sections into the image of its W O(3) component.

A generic-rank-one top image would have equivariant saturation O(k) in W O(3). The group has no nontrivial one-dimensional character, and central parity makes k even. Ordinary degree gives k<=3, hence k<=2. Its twist3 section space has dimension at most six, contradicting the eight independent sections. Rank zero is also excluded by strict-top.

For the generic-rank-two top image J, let delta be the length of W O(3)/J. Its twist3 is globally generated, so H1(J(3))=0 and

    h0(J(3))=2+deg J(3)=14-delta.

Section injectivity yields delta<=6. A nonzero equivariant torsion divisor has degree at least12; therefore delta=0. The top block alone maps onto the whole W O(3), with zero O(-12) component.

The profile-(1,1) backward endpoint has generic derivative rank at most two. If any lower block contributed a nonzero O(-12) component, the full image, already containing W O(3), would have generic rank three. Thus that component is identically zero. This proves the actual quotient

    K_1/K_2=W O(3),
    rank K_2=12, degree K_2=-60, maxdeg K_2<=-4.

This is where the endpoint rank bound is genuinely needed. No rank-three assertion about the endpoint, and no assumption of saturation from generic rank alone, has been made.

## 4. Second actual quotient: the forced V channel

The fixed character identities are

    P Sym2 W=V+P+D,    T W=V+P+D,
    W Sym9 W=A+V+P+2D,
    W Sym7 W=V+2P+D.

They give

    chi_G(K_1(4))=2V+2P+D-A,
    chi_G(K_2(4))=V-A.

Since H0 and H1 are genuine representations, the latter equality forces at least one V in H0(K_2(4)); it does not require H1 to vanish. As maxdeg K_2<=-4, this produces a saturated V O(-4) summand of the actual top block.

Strict-top makes its derivative a nonzero section-injective map to

    (K_1/K_2)(-2)=W O(1).

If its generic rank were one, its equivariant saturated line O(k) would have even k<=0. After twist4 its possible section representations are D, A, 1 or zero, according as k=0,-2,-4 or k<=-6. None contains V. Thus rank one is impossible.

If its rank-two image has defect delta, its twist4 is a globally generated quotient of V O. Riemann--Roch and section injectivity give

    3 <= 12-delta,

hence delta<=9<12. The invariant divisor bound forces delta=0. The V block itself is onto W O(1), and no additional rank assumption is needed because this is the entire derivative target. Consequently

    K_2/K_3=W O(1),
    rank K_3=10, degree K_3=-62, maxdeg K_3<=-5.

The proof correctly uses section injectivity rather than falsely claiming the rank-three V block is fiberwise injective into a rank-two target.

## 5. The exact source-free interface

At twist4 the last quotient has character W Sym5 W=V+P+D, giving

    chi_G(K_3(4))=-(A+P+D).

The bound maxdeg K_3<=-5 gives H0(K_3(4))=0. Hence

    H1(K_3(4))=A+P+D.

At twist5 the identities

    P Sym3 W=S+2T,
    T Sym2 W=Wp+S+2T,
    W Sym10 W=W+2S+2T

give chi_G(K_1(5))=-W+2Wp+S+4T. Subtracting

    W Sym8 W=Wp+S+2T,
    W Sym6 W=Wp+2T

for the two already proved exact quotients gives

    chi_G(K_3(5))=-W.

The entire transfer interface is therefore:

1. K_3 is a saturated center-even subbundle of the original constant bundle, with its actual constant connection.
2. Its rank is10, degree is-62, and maxdeg is at most-5.
3. H1(K_3(4))=A+P+D and chi_G(K_3(5))=-W.
4. The actual preceding quotient is K_2/K_3=W O(1), so the derivative target is W O(-1).
5. Strict-top, actual-kernel saturation, the rank-at-most-two target and the minimum invariant divisor degree12 continue to apply.

These are sufficient. The quartic subsystem, the bf source, and its internal J channel do not occur in the argument from Section1 onward of the pinned third-quotient proof.

For a direct independent check of its finite support step, a block U O(-j), j>=6, contributes U Sym^(j-6) W to the twist4 H1 budget. The dimension bound is (j-5)dim U<=12, with central parity U=(-1)^j. The supported blocks are exactly

    A[-6], P[-6], D[-6], Wp[-7], S[-7], 1[-8],
    V[-8], W[-9], 1[-10], Wp[-11], 1[-14].

Their two H1 contributions agree with the published table. Only 1[-8] and W[-9] supply W at twist5, and each consumes the entire A budget at twist4. Resolving the remaining P,D budget yields the published eight types. Strict-top at twist5 excludes precisely the four with a Wp top coefficient because H0(W O(4))=S+T. This leaves exactly

    I:   S[-5]+P[-6]+W[-9];
    II:  (P+D)[-6]+1[-8];
    III: S[-5]+P[-6]+1[-8]+1[-10];
    IV:  T[-5]+(V+1)[-8].

In particular the W[-9] possibility is retained. None of these necessary splitting types is presumed realizable.

## 6. The third quotient and its saturation do not use the old source

For a rank-one derivative image in W[-1], the saturated line has even degree at most-2. Types II and IV violate the immediate strict-top section dimension bound. In I and III, strict-top forces the line to be 1[-2] and forces S[-5] onto it through its complete cubic system. The P[-6] block maps to zero there because P is absent from Sym4 W=D. The next kernel therefore has a P top coefficient at degree-6, while its derivative target is 1[-4]; strict-top would inject P into H0(O(2))=A. This is impossible.

For rank two, the top blocks in II and IV have respective section dimensions nine and six. Their globally generated image bounds give defects at most three and four, respectively, hence zero by invariance.

In I and III, the unique S[-5] channel is the Euler subline 1[-2] in W[-1]. The only channel to the Euler quotient 1 is P[-6]. The other lower blocks have zero Hom into that quotient, using

    Sym8 W=P+D, Sym9 W=S+T, Sym10 W=A+V+D.

Rank two forces the P channel nonzero. Its degree-six common-zero divisor would be invariant and have degree at most six, so it has none. This channel surjects to the Euler quotient, and the top S channel already surjects to the Euler line. Thus the raw image itself is W[-1].

This independently verifies the transferred conclusion

    K_3/K_4=W[-1], rank K_4=8, degree K_4=-60.

Only the four types and the interface in Section5 have been used.

## 7. Audit of the remaining finite descent

The following checks verify the source independence of the pinned finite-descent argument, rather than merely accepting its source-specific conclusion.

### 7.1 The K_4 overlist and quotient W[-3]

The required kernels are the universal evaluation kernels

    ker(S[-5]->1[-2])=A[-6],
    ker(P[-6]->1)=V[-8].

For the second, the map is basepoint-free by the degree-six invariant-divisor bound; at twist6 its kernel has H1 budget V and no H0, which forces V[-8]. For type II the onto top kernel is S[-7]+V[-8]. For IV the two necessary top-kernel possibilities are S[-7] and A[-6]+1[-10]. The degree-zero and H1 budgets prove this overlist without needing to realize its second possibility.

The remaining extensions split by degree, except the potential equivariant term Ext1_G(V[-8],1[-10])=V^G=0, which also vanishes. The 1[-8] lower block maps identically to zero and splits independently; no invalid claim that Ext1_G(1[-8],1[-10]) vanishes is needed. The necessary K_4 types are

    a: S[-7]+(V+1)[-8];
    b: A[-6]+V[-8]+W[-9];
    c: A[-6]+(V+1)[-8]+1[-10].

In W[-3], each nonzero top channel is the complete Euler subline 1[-4]. Only V[-8] can reach the Euler quotient 1[-2]. A nonzero V channel is onto by the degree-six divisor bound. If it is zero, type a immediately violates strict-top at the next stage; types b,c force a further quotient 1[-6], preserve V[-8], and then require V to inject into the trivial section space of 1[-8]. Thus all rank-one alternatives are impossible, and

    K_4/K_5=W[-3]

is the full saturated image.

### 7.2 The K_5 types and quotient W[-5]

The V[-8] channel to 1[-2] has kernel Wp[-11]. After twisting by8, this is a rank-two degree-minus-six kernel of V O->O(6), with no constant sections. Its center-even possibilities are W[-3], Wp[-3], or 1[-2]+1[-4]. The last is excluded because V Sym2 W=P+D has no trivial section; the twist3 Euler character V Sym3 W-Sym9 W=Wp identifies Wp[-3]. This is a complete small splitting argument.

The resulting K_5 overlist is

    (A+1)[-8]+Wp[-11];
    W[-7]+W[-9]+Wp[-11];
    W[-7]+1[-8]+1[-10]+Wp[-11].

The first contradicts strict-top into W[-5] because W Sym3 W=A+D has no trivial constituent. In the other two, the W[-7] channel maps onto the Euler line 1[-6]. Only Wp[-11] can reach the Euler quotient 1[-4]. Its nonzero degree-seven system is basepoint-free and therefore onto.

If that component is zero, the next kernel has either two trivial degree-minus-eight coefficients, impossible in a derivative target 1[-8], or it has one such coefficient mapping isomorphically onto 1[-8]. The latter leaves a kernel with top W[-9] and next derivative target 1[-10], again impossible by strict-top. Consequently

    K_5/K_6=W[-5]

is the full saturated image.

### 7.3 The final image must remain raw and defective

The Euler-line kernel is 1[-8], and the onto Wp[-11]->1[-4] channel has line kernel 1[-18]. The extension splits by ordinary Ext1 vanishing. The two necessary K_6 types are

    1[-8]+W[-9]+1[-18],
    2 1[-8]+1[-10]+1[-18].

The second violates strict-top into W[-7], whose twist8 section representation W W=1+A has only one trivial coefficient. Therefore

    K_6=1[-8]+W[-9]+1[-18].

The top 1[-8] maps isomorphically to the Euler subline 1[-8] of W[-7]. The W[-9] block has zero component to its quotient 1[-6], because W is absent from Sym3 W=S. If the bottom 1[-18] also had zero quotient component, the next kernel would have top W[-9] and derivative target 1[-10], contradicting strict-top. Hence the bottom quotient map is a nonzero invariant section of O(12).

Its divisor has degree12, and the invariant section space is one-dimensional. The top 1[-8] and bottom 1[-18] define an injective rank-two sheaf map into W[-7]: its determinant is nonzero, so its kernel is zero on the smooth curve. The W[-9] image lies in the already-present Euler line. It follows that the actual raw image is exactly

    I=1[-8]+1[-18] inside W[-7],
    length(W[-7]/I)=(-14)-(-26)=12.

This is not W[-7]. The raw image is abstractly isomorphic to the displayed direct sum because that direct sum maps injectively onto it; no splitting of its embedding or of the connection is asserted.

The actual kernel is W[-9]: projecting a kernel section to the Euler quotient first kills its 1[-18] coefficient, and the isomorphic top 1[-8] cancels any W[-9] component in the Euler line. This is a graph kernel, hence isomorphic to W[-9] even if that component is nonzero.

Thus K_7=W[-9] and its derivative target is the actual quotient twisted by-2,

    I(-2)=1[-10]+1[-20].

Every bundle map from W[-9] to either summand vanishes by ordinary degree. Hence K_7 is horizontal. It is saturated in the same constant ambient bundle by the actual-kernel argument, so in characteristic zero it must be constant of degree zero. Its degree is instead-18. This is the claimed contradiction.

## 8. Final assessment

The global-generation step, the two full saturated quotients, both K_3 character budgets, the finite support calculation, and every subsequent descent stage are valid for the bb torsion source. The prior bf source is used only as the location of a universal argument whose hypotheses are now separately proved. Its quartic subsystem and source-specific preliminary quotient calculation have not been imported.

The final determinant defect12 is essential and has been retained all the way to the derivative target of K_7. There is no circular use of the onto-bb branch and no jump from a branch exclusion to a full-label exclusion. No selected-instance evaluation, source scan, or large computation was needed. The exact reviewed proof is suitable for use as a torsion-branch exclusion with the public dependency pins and scope above.
