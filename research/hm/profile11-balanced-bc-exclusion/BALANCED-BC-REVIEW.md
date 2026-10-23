# Independent exact-version review of the balanced bc exclusion

## Verdict

**Accepted for the stated source-stratum exclusion.** The argument in `BALANCED-BC-BACKWARD-EXCLUSION.md`, SHA256

`64e55ab01aa6811d9a87ea73282512633c807aeb8a29f9be2f3636f652303288`,

excludes the whole source

    E=(V+P) O(-2)+T O(-3)+V O(-4)+O(-10)

for the original-zero-defect balanced label G3.11.73682b4c817f, source index 72 and tuple (0,1,1,0,0,0,0,1). It does not exclude the entire label or any other source. No substantive correction is required to the reviewed version.

The new first-backward argument is exhaustive, including the vanishing lower-T quotient channel and the nonsaturated degree-twelve image. The second quotient is proved independently of any quartic subsystem. The transfer to the published finite descent is valid at a genuinely source-free interface. The raw image, not its saturation, is used at both ramified steps where this distinction matters.

This review was completed on 2026-10-23. It checks the actual-connection arguments, exact sheaf images, all case splits, the equivariant extension splittings, the character calculations, and the dependence of the imported descent on its stated inputs. It does not infer mathematical correctness from a verifier alone.

## 1. Exact inputs and scope of verification

The following local bytes have the stated SHA256 hashes:

- Reviewed proof: `BALANCED-BC-BACKWARD-EXCLUSION.md`, `64e55ab01aa6811d9a87ea73282512633c807aeb8a29f9be2f3636f652303288`.
- PR814 `PROOF.md`: `f0bd13d85ae8a890dbec84e5f15b7ec8605b04f474d5c7d80faeb3aa08f4defc`.
- PR823 `BF-THIRD-BACKWARD-QUOTIENT.md`: `16475cd7d6012fff2efd8d3ec04bce884231ffbfe664914e948584c24afa69d0`.
- PR823 `BF-FINITE-BACKWARD-DESCENT.md`: `9558490385822a4d559d555c4f3372fd594e7ef0f504454da0707d962cf9fd49`.

The immutable public dependency locations are:

- [PR814 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/PROOF.md), commit `1f94be65b3a470a1b594e61d56df7f6057c9d907`.
- [PR823 third backward quotient](https://github.com/Akilleez-QA/read-em-and-weep/blob/399abe93debe71232f0b7808fc8f1a5582118708/research/hm/profile11-balanced-bf-backward-exclusion/BF-THIRD-BACKWARD-QUOTIENT.md), commit `399abe93debe71232f0b7808fc8f1a5582118708`.
- [PR823 finite backward descent](https://github.com/Akilleez-QA/read-em-and-weep/blob/399abe93debe71232f0b7808fc8f1a5582118708/research/hm/profile11-balanced-bf-backward-exclusion/BF-FINITE-BACKWARD-DESCENT.md), the same commit.

The five original input files were checked by Git blob hash against the manifest in PR814. At the original-data pin `db51525015bb7c5e825833d550d08dedf6f6ea96`, they are:

- `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`: `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
- `NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md`: `d7506dae49b4be43230450c4132bd5db91f137ef`.
- `ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md`: `dcacf0bcdef8377c1ed7654e5b82659ea409456e`.
- `one-one-endpoint-necessary-pairs.json`: `fe0afa410d89340d3082dc814277f89fbb582c19`.
- `rank-three-quotient-frontier-144.json`: `8b5971092f9ef762584912609fd5e9301c4e271d`.

The original frontier entry confirms the label, source index, original defect zero, and

    A_q=O(-10)+W O(5), B_q=W O(-7)+O(8).

The tuple decodes to the displayed E using the original splitting formula, including the extra P O(-2) contribution. Its rank and degree are 17 and -54. The original profile-(1,1) endpoint supplies rank beta_(K_1)<=2. These hypotheses are not replaced by an assumption that later endpoints have rank three.

All later K_i are actual successive derivative kernels, saturated in the same ambient constant bundle. Thus strict-top applies repeatedly, and the derivative of K_(i+1) factors through the actual quotient (K_i/K_(i+1))(-2). Equivariant splitting is used for bundles and cohomology only, never to split the connection.

## 2. Rank-two top input and complete rank-one top image

The rank-two top exclusion in PR814 applies to this exact bc source. Its relevant mechanism is valid: the small top kernel has zero internal derivative; the first top span is the actual constant (P+D) O; constant projection leaves the saturated bundle T O(-3)+V O(-4)+O(-10), with only the O(-10) external quotient. The top T O(-3) then has both zero external derivative and zero internal derivative into V O(-6)+O(-12), contradicting negative horizontality. This is not merely a splitting-degree contradiction asserted without constant projection.

For the remaining rank-one top branch, put F=(V+P) O(-2). The top map cannot vanish by strict-top. A saturated equivariant line in W O(5) has trivial coefficient and even degree k<=4. The injection of the seven-dimensional V+P into H0(O(k+2)) forces k=4. At k=4 the entire space of sections is Sym^6 W=V+P, so the top map is the complete evaluation system, not an arbitrary subsystem with possible base divisor. It is onto O(4), and its kernel is T O(-3).

The equivariant inclusion O(4)->W O(5) is unique up to scalar because the invariant part of W tensor W is one-dimensional. It is the saturated Euler inclusion, with quotient O(6).

The map to O(-10) vanishes on every higher-degree source block. Surjectivity of E->A_q forces its restriction to the sole O(-10) block to be an isomorphism. Consequently

    E'=(V+P) O(-2)+T O(-3)+V O(-4),
    E'/K_1=W O(5).

This proves, without a connection-splitting assumption,

    rank K_1=14, degree K_1=-54, maxdeg K_1<=-3.

At twist three the source sections are Wp+3T and the target sections are Wp+S+2T. The top image contributes precisely Wp+T. The lower T's projection to the Euler quotient is either zero or a nonzero irreducible T map into H0(O(9))=S+T. Thus the two cases in the proof are exhaustive and their section images are as claimed. The V O(-4) block has no twist-three sections and creates no missing third case.

The Euler characters independently recompute to

    chi K_1(3)=T-S,
    chi K_1(4)=2V+2P+D-A,
    chi K_1(5)=-W+2Wp+S+4T.

## 3. Vanishing lower-T quotient channel

When T O(-3)->O(6) vanishes, all its sections land in the already-full top line image. Therefore H0(K_1(3))=2T, not T. Because maxdeg K_1<=-3, these twelve sections constitute an actual top block 2T O(-3).

Its derivative has zero O(-12) component by ordinary degrees and lands in W O(3). A rank-one saturation there has even degree at most 2, hence at most six twist-three sections. Strict-top excludes rank one and rank zero.

For its rank-two raw image J, J(3) is globally generated as a quotient of 2T O. If delta is the torsion cokernel length in W O(3), then

    h0(J(3))=14-delta,  12<=14-delta.

Global generation justifies H1=0 in this equality. The determinant divisor is invariant, so its positive length is at least 12; delta<=2 forces delta=0. The top block therefore supplies the actual whole W O(3), not just a generic rank-two image.

A nonzero remaining O(-12) component would increase the full derivative's generic rank to three, contradicting the profile endpoint bound. Consequently the exact quotient is K_1/K_2=W O(3). No classification of the lower splitting of K_1 is needed in this case.

## 4. Nonzero lower-T quotient channel and the small kernel

Here the added T quotient channel is injective on its irreducible section coefficient, giving

    H0(K_1(3))=T, H1(K_1(3))=S.

For a block Z O(-j), j>=5, its H1 contribution is Z Sym^(j-5) W. The four-dimensional S budget is exhaustive: the only supported blocks are S O(-5) and O(-8). At j=6 only the trivial even coefficient fits the dimension bound, and it contributes W rather than S; j=7 exceeds the bound for every odd coefficient; j=8 permits the trivial coefficient, giving S; every later admissible block exceeds the budget.

The degree-minus-three coefficient is T. If S O(-5) occurs, the twist-four Euler character forces the degree-minus-four coefficient V+P-A, which is not genuine. For O(-8), the twist-four H1 is A, and the coefficient is V+P. Thus the asserted unique splitting follows:

    K_1=T O(-3)+(V+P) O(-4)+O(-8).

All degrees are greater than -12, so the entire derivative has zero O(-12) component. It genuinely lands in W O(3).

## 5. Exhaustive first-backward image audit

The T O(-3) top derivative is nonzero. If it has rank two, its twist-three generated image has h0=14-delta and must contain six independent sections. Hence delta<=8<12 and it is onto W O(3).

If it has rank one, its saturation O(k), with even k<=2, must have at least six twist-three sections. This forces k=2 and the complete quintic system. The image therefore contains the entire Euler O(2), with quotient O(4).

Projection of the remaining blocks to that quotient gives exactly:

- V O(-4): zero, since V is absent from Sym^8 W=P+D.
- P O(-4): its unique P channel, potentially nonzero.
- O(-8): its degree-twelve invariant channel, potentially nonzero.

If the P channel is nonzero, its common-zero divisor has degree at most eight and is invariant. Hence it is empty, so P O(-4)->O(4) is onto. Together with the full Euler line, this gives the whole W O(3) as a sheaf image.

If the P channel vanishes, there are exactly two remaining cases.

### 5.1 The final quotient channel also vanishes

The raw image is precisely O(2). The top quintic evaluation kernel is D O(-4). Since the top map is onto O(2), projection of the full kernel to the lower source blocks is onto, giving

    0 -> D O(-4) -> K_2
      -> (V+P) O(-4)+O(-8) -> 0.

The extension groups reduce to H1(O) and H1(O(4)), both zero. Averaging yields an equivariant splitting. Thus

    K_2=(V+P+D) O(-4)+O(-8).

Its actual derivative target is O, whose twist-four sections are D. Strict-top would inject V+P+D into D, impossible.

### 5.2 The degree-twelve quotient channel is nonzero

The nonzero sheaf map O(-8)->O(4) is injective, with image isomorphic to O(-8) and cokernel length 12. The full raw image I fits into

    0 -> O(2) -> I -> O(-8) -> 0.

Its extension class lies in H1(O(10))=0, so I=O(2)+O(-8) equivariantly. This is not the saturated target W O(3): their degrees differ by 12.

In the kernel, projection to O(4) forces the O(-8) source component to vanish, since its quotient-channel map is injective as a sheaf map. Thus

    0 -> D O(-4) -> K_2 -> (V+P) O(-4) -> 0,

which splits by H1(O)=0. It follows that K_2=(V+P+D) O(-4). Its derivative target is the actual I(-2)=O+O(-10), whose twist-four sections are again only D. The same strict-top contradiction follows.

This correctly excludes the ramified raw image rather than replacing it by its saturation. All cases have now been exhausted, proving K_1/K_2=W O(3).

## 6. The second quotient and exact descent interface

Subtracting the full W O(3) quotient at twist four gives chi K_2(4)=V-A. Strict-top gives maxdeg K_2<=-4. Since H1 is genuine, H0(K_2(4)) contains V; this supplies an actual V O(-4) top subblock even without knowing the complete splitting of K_2.

Its derivative into W O(1) cannot vanish. A rank-one saturation has even degree at most zero. Its twist-four sections are D, A, 1, or zero, never containing V. Thus the image has rank two. Its generated twist-four image has h0=12-delta; strict-top gives 3<=12-delta, hence delta<=9<12. This again forces zero defect and proves

    K_2/K_3=W O(1),
    rank K_3=10, degree K_3=-62, maxdeg K_3<=-5.

The derivative of K_3 lands in W O(-1). The exact cohomology inputs are

    H1(K_3(4))=A+P+D,
    chi K_3(5)=-W.

For the first, chi K_3(4)=-(A+P+D) and H0 vanishes. For the second, subtract W Sym^8 W=Wp+S+2T and W Sym^6 W=Wp+2T from the computed chi K_1(5). These identities do not require the nonzero-lower-T case or its special K_1 splitting.

From Section 1 onward, `BF-THIRD-BACKWARD-QUOTIENT.md` uses only these rank, degree, strict-top, target, and two cohomology inputs, together with the actual constant connection and equivariance. Its source-specific opening quartic flag is used only to establish those inputs for bf. It is neither used nor assumed in this bc application. The transfer is therefore valid.

## 7. Audit of the transferred third quotient

The H1(K_3(4)) budget supports exactly the eleven blocks listed in the dependency: A, P, D at degree -6; Wp and S at -7; 1 and V at -8; W at -9; 1 at -10; Wp at -11; and 1 at -14. This exhausts parity-compatible blocks under (j-5)dim Z<=12. A bounded tensor-with-W recurrence independently reproduces this support and the S-budget support in Section 4 above.

At twist five, the required W in H1 can arise only from O(-8) or W O(-9). Each consumes the sole A budget, so precisely one occurs. Completing the P,D budget gives the eight stated candidates. Strict-top into H0(W O(4))=S+T removes exactly the four with Wp at degree -5. The four remaining types are

    I:   S O(-5)+P O(-6)+W O(-9);
    II:  (P+D) O(-6)+O(-8);
    III: S O(-5)+P O(-6)+O(-8)+O(-10);
    IV:  T O(-5)+(V+1) O(-8).

The often-sensitive W O(-9) type is retained.

A rank-one derivative is excluded by section dimensions in II and IV. In I and III it forces the full Euler O(-2) image; P O(-6) then lies in the next kernel, whose derivative targets O(-4). At twist six strict-top would inject P into A, impossible.

For rank-two images, the top generation bounds force defect at most three in II and at most four in IV, hence zero. In I and III the unique S top channel fills Euler O(-2); all lower quotient-to-O channels vanish except P O(-6). Generic rank two makes this P channel nonzero; its degree-six system is basepoint-free by the invariant-divisor bound. Therefore the actual quotient is W O(-1), with rank K_4=8 and degree K_4=-60.

No source-specific input reappears in this argument.

## 8. Audit of the finite descent and extension issues

The finite-descent proof starts from the four types above and the exact quotient just proved. Its following steps remain source-independent.

1. The three necessary K_4 types are

       a: S O(-7)+(V+1) O(-8),
       b: A O(-6)+V O(-8)+W O(-9),
       c: A O(-6)+(V+1) O(-8)+O(-10).

   The cubic Euler kernel is A O(-6), the P sextic kernel is V O(-8), and the type-II top kernel is S O(-7)+V O(-8). In type IV, the allowed top kernels are S O(-7) or A O(-6)+O(-10). The only extension here not killed by ordinary H1 vanishing is the potential extension of V O(-8) by O(-10). Its equivariant Ext group is H1(V O(-2))^G=V^G=0. Thus all claimed equivariant splittings are justified. The lower blocks asserted to vanish in W O(-1) have zero equivariant Hom, not merely zero projection to its Euler quotient.

2. For K_4->W O(-3), the top S or A fills Euler O(-4), and only V O(-8) can reach the Euler quotient O(-2). A nonzero V channel is basepoint-free. If it vanishes, type a fails strict-top immediately; in b and c the resulting W O(-7) top forces one more rank-one quotient, after which the retained V O(-8) would have to inject into a trivial section. Therefore K_4/K_5=W O(-3) exactly.

3. The V sextic evaluation kernel is Wp O(-11). Its normalized rank-two degree-minus-six kernel has only the possibilities W O(-3), Wp O(-3), or O(-2)+O(-4). The trivial twist-two section excludes the last, and the twist-three character identifies Wp. The subsequent extensions by A O(-8) or W O(-7) have positive-degree H1=0. This yields the three K_5 types in the dependency. The type with top A+1 at degree -8 fails strict-top because H0(W O(3))=A+D has no trivial coefficient.

4. In the remaining K_5 types, W O(-7) fills Euler O(-6) in W O(-5), and only Wp O(-11) reaches the quotient O(-4). If that channel vanishes, the next kernels are exactly the two displayed rank-one cases. One has two trivial top coefficients mapping to a single trivial section; the other forces a further isomorphic top line quotient and then W O(-9) would map to O(-10), impossible. Hence K_5/K_6=W O(-5) exactly.

5. The line kernel of Wp O(-11)->O(-4) is O(-18). Its extension by O(-8) splits by H1(O(10))=0. The alternative K_6 with two O(-8) top lines fails the single-trivial-coefficient bound in H0(W O(1))=1+A. Therefore

       K_6=O(-8)+W O(-9)+O(-18).

6. In K_6->W O(-7), the top O(-8) maps isomorphically to Euler O(-8). The W O(-9) quotient channel vanishes. The O(-18)->O(-6) quotient channel must be nonzero, or the next W O(-9) top again violates strict-top. Its divisor has degree 12; the invariant space in Sym^12 W has dimension one. The two line source blocks inject as a rank-two sheaf, so the actual image is

       I=O(-8)+O(-18),

   with determinant defect 12 in W O(-7). The W O(-9) component adds only a graph into the already-full Euler line. Thus K_7=W O(-9), not a different saturated or modified kernel.

7. The derivative of K_7 targets the actual I(-2)=O(-10)+O(-20). Both Hom groups from W O(-9) vanish by ordinary degrees. Thus this saturated negative bundle is horizontal in the original constant ambient bundle, impossible in characteristic zero.

These checks include the lower-block Hom vanishings, graph-kernel identifications, and all uses of ordinary versus equivariant Ext. In particular, replacing I by W O(-7) at the last step would be invalid and is not done.

## 9. Contribution and boundary

The new proof establishes an exact source-independent route from balanced bc to the already-proved finite negative descent. Combined with PR814's rank-two top exclusion, this is a complete exclusion of the specified bc source, not merely its nonzero lower-T subcase or its saturated first-image subcase.

The verification used universal sheaf and connection arguments, exact public inputs, and small abstract binary-icosahedral representation identities. The bounded recurrence used only the nine irreducible tensor-with-W rules and the two stated cohomology budgets. No selected HM/source coefficients, parameters, points, derivatives, matrices, evaluated instance ranks, experiments, or large scans were used. No additional label exclusion, frontier-count change, realizability assertion, or conclusion about the global open goal follows from this note alone.
