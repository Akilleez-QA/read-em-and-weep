# Independent review: the third backward quotient

## Verdict and exact scope

**PASS.** The proof in `BF-THIRD-BACKWARD-QUOTIENT.md`, reviewed at SHA256

`16475cd7d6012fff2efd8d3ec04bce884231ffbfe664914e948584c24afa69d0`,

correctly proves, conditional on the nonzero internal channel of the specified source,

    K2/K3 = W O(1),
    K3/K4 = W O(-1),

as actual derivative quotients with no torsion correction. Consequently K3 has rank 10 and degree -62, and K4 has rank 8 and degree -60. No mathematical blocker was found. This is not a full source or stable-label exclusion, and none is inferred here.

The scope is precisely stable label G3.11.73682b4c817f, source_index72, source

    E = (P+D) O(-2) + T O(-3) + O(-8) + O(-10),

with source tuple (0,1,0,0,0,1,0,1), and with its internal channel nonzero. The argument concerns actual saturated subbundles and their constant-connection derivatives. Equivariant splitting is used for cohomology and maps, not as a splitting of that connection.

## Public dependencies and source identification

The quartic subsystem input is [BF-SUBSYSTEM.md at the immutable PR819 commit](https://github.com/Akilleez-QA/read-em-and-weep/blob/03fee9278072f9ac00a5fcee5deb04b7fce61ae5/research/hm/profile11-balanced-low-positive-subsystems/BF-SUBSYSTEM.md), commit `03fee9278072f9ac00a5fcee5deb04b7fce61ae5`, SHA256 `087d0b78196b7c0d5e773375e603359450e0e9fb0ebb3003734c44eea4e133b9`. Its actual quartic flag, exact sequence, and quotient K1/K2=W O(3) are the inherited conclusions used below.

The original immutable input commit is `db51525015bb7c5e825833d550d08dedf6f6ea96`:

- [The original stable-label frontier](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json) identifies G3.11.73682b4c817f with source_index72, profile (1,1), original defect zero, and A_q=O(-10)+W O(5).
- [The original necessary-pair list](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json), entry 72, includes the stated source tuple.
- [Actual equivariant splitting and Gauss persistence](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md) provides the actual saturated inclusion, rank 17, degree -54, equivariant splitting conventions, and outward Gauss-rank monotonicity.
- [Strict lowering of the top slope](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md) gives both the successive top-degree bounds and the top-section injectivity used here.

The subsystem proof records its earlier public dependencies at PR796 commit `d2b43060c83328dd5118aee6b9288fcfa0c873ac` and PR799 commit `2172e4a7abbbe232f9f448bea6fa01dee7927460`. No unpublished continuation is needed for the present review.

## 1. The preceding quotient is genuinely derived

Write K_i=E^(-i). In the actual quartic subsystem, F^- = T O(-3) and F^{--}=V O(-4). The map

    F^- -> (F/F^-)(-2)=V O(-2) -> W O(3)

is the actual derivative of F^- followed by the quotient to (E/K1)(-2). Its kernel contains F^{--}, and its residual kernel after quotienting by F^{--} is O(-12). In particular F^{--} lies in K2.

The actual derivative of F^{--} is onto

    (F^-/F^{--})(-2)=V O(-4).

The induced map from this bundle to (K1/K2)(-2)=W O(1) is exactly, up to a nonzero scalar in the canonical osculation identifications, the twist by -4 of

    0 -> O(-10) -> V O -> W O(5) -> 0.

Thus the derivative image of K2 contains all of W O(1). Its derivative lands in that same bundle: this follows from K2 being the actual derivative kernel of K1. Equivalently, the inherited rank bound of two excludes any larger generic image. Hence the raw image, not merely its saturation, is W O(1), proving K2/K3=W O(1).

Rank and degree subtraction gives (rank K1,deg K1)=(14,-54), (rank K2,deg K2)=(12,-60), and (rank K3,deg K3)=(10,-62). Strict-top iteration from maxdeg E=-2 gives maxdeg K3<=-5. Its derivative lands in W O(-1).

## 2. Independent representation and two-twist audit

The tensor-with-W identities are

    W^2=1+A, WA=W+S, WS=A+D, WD=S+T,
    WT=V+P+D, WV=T, WP=Wp+T, WWp=P.

Using Sym^n W=W Sym^(n-1) W-Sym^(n-2) W gives

    Sym6 W=V+P,       Sym7 W=Wp+T,
    Sym8 W=P+D,      Sym9 W=S+T,
    Sym10 W=A+V+D.

The additional products needed for completeness are

    A^2=1+A+D,       VA=P+D,         PA=V+P+D,
    Wp A=T,          Wp S=V+D,
    Wp D=S+T,        Wp T=A+P+D.

Subtracting the three established quotients O(-10)+W O(5), W O(3), W O(1) from the stated E independently yields

    chi_G(K3(4))=-(A+P+D),
    chi_G(K3(5))=-W.

For a direct check, put B=P+D. Then BA=A+2V+2P+2D, BS=W+Wp+2S+4T, and TA=Wp+S+2T; substitution in the Euler characters gives the two displayed identities. Since H0(K3(4))=0, the first gives H1(K3(4))=A+P+D.

For U O(-j), j>=6, the first H1 contribution is U Sym^(j-6)W. Parity and (j-5)dim U<=12 give exactly the following supported rows. The two columns were checked independently:

| Block | H1 at twist 4 | H1 at twist 5 |
|---|---|---|
| A O(-6) | A | 0 |
| P O(-6) | P | 0 |
| D O(-6) | D | 0 |
| Wp O(-7) | P | Wp |
| S O(-7) | A+D | S |
| O(-8) | A | W |
| V O(-8) | P+D | T |
| W O(-9) | A+D | W+S |
| O(-10) | D | S |
| Wp O(-11) | A+P+D | S+T |
| O(-14) | P+D | Wp+T |

Completeness is important. At j=6 only A,P,D fit the character budget. At j=7, tensoring the four odd irreducibles by W leaves only Wp,S. At j=8 the dimension bound leaves 1,A,V,P; A^2 contains 1 and PA contains V, so only 1,V survive. At j=9 only W,Wp fit, and Wp S contains V. At j=10 only 1 fits. At j=11 only W,Wp fit, and WT contains V. At j=12 only 1 fits but Sym6 W contains V. Odd j>=13 exceed the bound. The only further even candidates are j=14 and 16 with coefficient 1; Sym8 W is supported and Sym10 W is not. Even j>=18 exceed the bound. This verifies all eleven rows without an unbounded envelope calculation.

The identity H0(K3(5))=H1(K3(5))-W forces a W-bearing row. Only O(-8) and W O(-9) supply W, and each exhausts the A budget, so exactly one occurs. W O(-9) leaves P, supplied by P O(-6) or Wp O(-7). O(-8) leaves P+D, supplied separately in four ways or jointly by V O(-8) or O(-14). Matching the degree-minus-five coefficient therefore gives exactly:

    S O(-5)+P O(-6)+W O(-9);
    (S+Wp) O(-5)+Wp O(-7)+W O(-9);
    (P+D) O(-6)+O(-8);
    S O(-5)+P O(-6)+O(-8)+O(-10);
    Wp O(-5)+D O(-6)+Wp O(-7)+O(-8);
    (Wp+S) O(-5)+Wp O(-7)+O(-8)+O(-10);
    T O(-5)+(V+1) O(-8);
    (Wp+T) O(-5)+O(-8)+O(-14).

Every row has rank 10 and degree -62. Strict-top injectivity at twist five maps its degree-minus-five coefficient into W Sym4 W=S+T. It excludes exactly rows 2,5,6,8. The remaining four types are precisely I,II,III,IV in the proof. In particular the W O(-9) row and type I are present and necessary.

## 3. Rank-one exclusion uses the actual next derivative

A rank-zero derivative would make the saturated negative K3 constant, which is impossible. If the generic derivative rank were one, its equivariant saturation inside W O(-1) would be a line O(k). Degree gives k<=-1. The center-even linearization and the absence of nontrivial one-dimensional characters give even k, hence k<=-2.

For type II, strict-top at twist six would inject P+D, of dimension nine, into at most k+7<=5 sections. For type IV, strict-top at twist five would inject T, of dimension six, into at most k+6<=4 sections. Both are impossible.

For I and III, the corresponding dimension-four S injection forces k=-2. Its nonzero map into H0(O(3))=S is the full cubic section system, so the top block already surjects onto O(-2). Thus the actual image is exactly O(-2), and K3/K4=O(-2), without a divisor correction.

The P O(-6) summand is killed because Hom_G(P,Sym4 W)=Hom_G(P,D)=0. It is therefore contained in K4, and H0(K4(6)) contains P. Strict-top iteration gives maxdeg K4<=-6. Since K4 is the actual kernel, its next derivative lands in

    (K3/K4)(-2)=O(-4).

Strict-top injectivity would then embed H0(K4(6)), and hence P, into H0(O(2))=A. Distinct irreducibility forbids this. This argument correctly excludes rank one in I and III; it does not infer a connection on an abstract complement.

## 4. Saturation is proved in every surviving branch

For II, restrict the derivative to the top (P+D) O(-6). Its section map is injective. A rank-one restricted image would saturate in O(k), k<=-2, giving at most five sections at twist six, versus nine required. Hence the restriction has rank two. Its image after twisting by six is globally generated, so it has H1=0. If its determinant defect is delta, its degree is 10-delta and

    9 <= h0(image)=12-delta.

Thus delta<=3. The determinant-defect divisor is invariant. Every nonempty invariant divisor on this P1 has degree at least 12, so delta=0. The top block itself surjects onto W O(-1).

For IV, the same argument applied to T O(-5) first excludes restricted rank one by 6>4, then gives 6<=10-delta, hence delta<=4. The same invariant-divisor argument gives delta=0.

For I and III, the S O(-5) component has a unique channel to W O(-1), since W Sym4 W=S+T. The nonzero composition of the complete cubic section system with the Euler inclusion

    O(-2) -> W O(-1)

spans that channel. Strict-top makes the channel nonzero, so its image is exactly this Euler O(-2) subline. Compose the full derivative with the Euler quotient W O(-1)->O. The S component vanishes because S is absent from Sym5 W=T. In I the W O(-9) component vanishes because W is absent from Sym9 W=S+T. In III the O(-8),O(-10) components vanish because 1 is absent from Sym8 W=P+D and Sym10 W=A+V+D. Only P O(-6) remains.

The already-proved rank two forces that channel to be nonzero. Its coefficient map P->Sym6 W is injective, providing four independent sextic sections. Their common-zero divisor is invariant and has degree at most six, so it must be empty. Hence this component surjects onto the Euler quotient O. The full image contains the entire Euler kernel O(-2) and surjects onto its quotient O, so it is all of W O(-1), sheaf-theoretically and everywhere.

All four branches therefore have actual saturated derivative quotient K3/K4=W O(-1). The two-twist list is only a necessary splitting classification, not a realization assertion. The review used exact sequences, universal representation identities, dimension bounds, and constant-connection arguments; it required no selected source coefficients, points, evaluated derivatives, instance matrices or ranks, or model scans.
