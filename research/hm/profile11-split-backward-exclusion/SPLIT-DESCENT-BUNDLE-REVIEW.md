# Independent exact-version review of the split descent and its source applications

## Verdict, reviewed versions, and scope

**PASS.** The source-free split backward-descent theorem is proved under its stated actual equivariant connection hypotheses. The split-bc application establishes every one of those hypotheses and excludes the entire stated bc source after combining its rank-one argument with the pinned prior rank-two exclusion. The split-bf corollary validly composes the separately reviewed bf interface with this theorem and the pinned rank-two exclusions.

The exact reviewed files and SHA256 hashes are:

- `SPLIT-BACKWARD-DESCENT.md`:
  `ee1096f2368fee248792c35feeb3c689a134b8e1a84934c9699575fbe920ee1a`.
- `SPLIT-BC-SOURCE-EXCLUSION.md`:
  `22910f2176448710de765823ee872bcb43ead8e300a9ebdf65e6a16b0307f40e`.
- `SPLIT-BF-SOURCE-COROLLARY.md`:
  `3f7aec33779fe0a1e85069cd734ecbe9bbe44ba956ffcde0c4a42852c51ead48`.

The first two proofs were reviewed in full, not only at their terminal steps. This includes the initial rank-one and defective rank-two alternatives, complete bounded K3 support, all four surviving K3 types, the split-specific IV/d branch, ordinary Ext orientations, exact raw images, both terminal length-twelve defects, both lower-T cases in bc, all top-T derivative patterns, and the actual-connection interface.

The third file was reviewed as an exact-interface corollary. Its bf input theorem is `SPLIT-BF-BACKWARD-INTERFACE.md`, SHA256

    b5924ec48fe1dd7583b37d75d47b8ef1ec3f0b3a589744349ebf924c08de4a61,

with the separate exact-version PASS review `SPLIT-BF-INTERFACE-REVIEW.md`, SHA256

    a3308cc427faa74264a5333964d64ffc9041f1b3a95eded549fed26a1788863d.

The bf interface's asserted output and its composition were checked here. This does not claim to replace the independent full review of that interface or to reprove every earlier public theorem.

The source applications concern only original-zero-defect label G3.11.863639aa192e, source index 69, with

    A_q=O(-10)+O(4)+O(6),
    B_q=O(-8)+O(-6)+O(8).

They exclude respectively the tuples

    bc: (0,1,1,0,0,0,0,1),
    bf: (0,1,0,0,0,1,0,1).

Neither the universal theorem nor these two applications alone is an entire-label exclusion, a new global-frontier count, or a global rank-three exclusion. No mathematical correction is required to the exact versions listed above.

## 1. Immutable dependencies and original input identity

The prior polar and strict-top conventions are pinned in PR814 at commit

    1f94be65b3a470a1b594e61d56df7f6057c9d907,

in [PROOF.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/PROOF.md), SHA256

    f0bd13d85ae8a890dbec84e5f15b7ec8605b04f474d5c7d80faeb3aa08f4defc.

The public bounded-support and elementary-kernel references are PR823, commit

    399abe93debe71232f0b7808fc8f1a5582118708:

- [BF-THIRD-BACKWARD-QUOTIENT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/399abe93debe71232f0b7808fc8f1a5582118708/research/hm/profile11-balanced-bf-backward-exclusion/BF-THIRD-BACKWARD-QUOTIENT.md), SHA256 `16475cd7d6012fff2efd8d3ec04bce884231ffbfe664914e948584c24afa69d0`.
- [BF-FINITE-BACKWARD-DESCENT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/399abe93debe71232f0b7808fc8f1a5582118708/research/hm/profile11-balanced-bf-backward-exclusion/BF-FINITE-BACKWARD-DESCENT.md), SHA256 `9558490385822a4d559d555c4f3372fd594e7ef0f504454da0707d962cf9fd49`.

These supplied bytes have the stated hashes. The present split theorem does not import a balanced image, quotient, or terminal branch classification. Its split quotient claims and the extra IV/d branch were checked directly below.

For the bf corollary, the additional prior exclusion is PR830, commit

    620d5598ccc19e5e1c458a4cddb0d3a0709d83c3,

in [SPLIT-BF-RANK-TWO-NONZERO-CHANNEL.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/620d5598ccc19e5e1c458a4cddb0d3a0709d83c3/research/hm/profile11-split-bf-rank-two-exclusion/SPLIT-BF-RANK-TWO-NONZERO-CHANNEL.md), SHA256

    d762e23c6b402bf8bfd62160e310ecacf601a910d47f6a3e278cd8a3806657f6.

The original source, label, and connection inputs are pinned at commit

    db51525015bb7c5e825833d550d08dedf6f6ea96

under [research/hm/order-four-quadratic-load](https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load). The supplied original files were checked by computing their Git blob hashes:

| Input | Git blob |
|---|---|
| ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md | b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3 |
| NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md | d7506dae49b4be43230450c4132bd5db91f137ef |
| ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md | dcacf0bcdef8377c1ed7654e5b82659ea409456e |
| one-one-endpoint-necessary-pairs.json | fe0afa410d89340d3082dc814277f89fbb582c19 |
| rank-three-quotient-frontier-144.json | 8b5971092f9ef762584912609fd5e9301c4e271d |

The frontier record identifies exactly the label, quotient pair, zero original defect, and source index stated above. Entry 69 of the original necessary-pairs list contains both source tuples. Substituting bc into the original source formula gives

    E=(V+P)[-2]+T[-3]+V[-4]+O(-10),

of rank 17 and degree -54. Substituting bf gives the bundle in its corollary. No assumption that these formal sources are realizable is introduced.

## 2. Geometric and representation preliminaries

Write U[d]=U tensor O(d). The proof is in the actual equivariant constant-connection setting over C. Every actual derivative kernel is saturated in its source and then in the original constant bundle: its source quotient is locally free, and the previous ambient quotient is locally free. The strict-top theorem therefore applies at each iteration. In particular it gives an injection of top-section representations into the sections of the actual derivative target, not a claim of fiberwise injectivity of the top block.

A nonzero negative saturated horizontal bundle is impossible. Its classifying map to the Grassmannian has zero differential, hence is constant in characteristic zero; saturation then identifies it with a degree-zero constant subbundle.

The universal theorem does not need an extra center-even hypothesis. For the center-odd summand of K2, its Euler character is zero at twist four and at twist five: the prescribed characters have respectively even and odd central signs, while twisting reverses the sign. The difference of the two numerical Euler characteristics is the rank of that summand. Its rank is therefore zero. All subsequent kernels inherit center-even parity.

The W-tensor identities and the recurrence for Sym^n W reproduce all the characters used in both proofs. In particular:

    Sym6=V+P, Sym7=Wp+T, Sym8=P+D,
    Sym9=S+T, Sym10=A+V+D, Sym11=W+S+T,
    Sym12=1+A+P+D, Sym14=A+V+P+D.

Thus the invariant degree-twelve section space is one-dimensional, and there are no invariants in degrees 2, 4, 6, 8, 10, or 14. A nonzero irreducible subsystem in degree less than twelve is basepoint-free: its common-zero divisor is invariant and has degree no larger than the section degree.

The complete-evaluation kernel

    ker(Sym^n W[-m] -> O(n-m))=Sym^(n-1) W[-m-1]

is the ordinary equivariant evaluation sequence. The two additional sextic kernels were also checked independently. For P O -> O(6), the kernel has rank three, degree -6, no constant sections, and H1 budget V. The sole supported lower block is V[-2], and rank leaves no degree-minus-one part. For V O -> O(6), the rank-two degree-minus-six negative kernel can only be W[-3], Wp[-3], or O(-2)+O(-4). The last would put a trivial section into V Sym2=P+D. The twist-three character V Sym3-Sym9=Wp selects Wp[-3]. These give precisely the two identities used in the theorem.

All relevant extension splittings use Ext in the correct direction: for subbundle U[a] and quotient Z[b], the ordinary cohomology degree is a-b, not b-a. Averaging preserves a splitting over C. The potentially least-positive degree in the entire pair of proofs is -1 in bc Section 4.2, and H1(O(-1))=0. Separate zero rows already give direct kernel sums and do not need an extension argument.

## 3. The universal theorem's initial quotient is forced exactly

The character chi(K2(4))=V-A and maxdeg K2<=-4 force an actual V[-4] top subblock. Its O(0) component vanishes because Sym4=D has no V. Strict-top makes its O(2) component nonzero, and its sextic V system is onto. The raw image therefore contains the entire direct O(2) summand.

### 3.1 Initial rank one

A rank-one raw image containing that summand is exactly O(2). Exact subtraction gives

    H1(K3(4))=A+P,
    chi(K3(5))=T-W,
    maxdeg K3<=-5.

The complete supported lower-block list is A[-6], P[-6], Wp[-7], O(-8). The required W in H1 at twist five forces O(-8), which consumes the A budget. The two necessary types are exactly

    T[-5]+P[-6]+O(-8),
    (T+Wp)[-5]+Wp[-7]+O(-8).

The second violates strict-top into O(0) at twist five. In the first, the complete T quintic row is onto O(0), with kernel D[-6]. The extension by P[-6]+O(-8) splits with degrees 0 and 2. Hence K4=(P+D)[-6]+O(-8), whose top cannot inject into H0(O(-2)(6))=D. This exhausts initial rank one.

### 3.2 Initial rank two with possible torsion defect

Since O(2) is contained in the image, projection to O(0) identifies the raw image exactly as

    I=O(2)+O(-d), d>=0.

This is an ideal-sheaf decomposition, not replacement by saturation. If d>0, invariance gives d>=12. Exact Euler-character subtraction and H0(K3(4))=0 give

    H1(K3(4))=A+P-Sym^(d-6) W.

Dimension bounds d by 12. At d=12 the expression is A-V and is not genuine. Thus d=0, the actual quotient is O(0)+O(2), and

    rank K3=10, deg K3=-62,
    H1(K3(4))=A+P+D, chi(K3(5))=-W.

No initial rank or defect alternative remains unexamined.

## 4. Exhaustive K3 support and all four split images

For a lower block U[-j], j>=6, the twist-four budget contribution is U Sym^(j-6) W. The dimension bound (j-5)dim U<=12 and central parity give exactly:

| Block | H1 at twist four | H1 at twist five |
|---|---|---|
| A[-6] | A | 0 |
| P[-6] | P | 0 |
| D[-6] | D | 0 |
| Wp[-7] | P | Wp |
| S[-7] | A+D | S |
| O(-8) | A | W |
| V[-8] | P+D | T |
| W[-9] | A+D | W+S |
| O(-10) | D | S |
| Wp[-11] | A+P+D | S+T |
| O(-14) | P+D | Wp+T |

The dimension/parity exclusions at j=6 through 16 were independently checked. At j=8 the only dimension candidates are 1,A,V,P; A contributes a forbidden trivial constituent and P contributes a forbidden V. At j=9, Wp Sym3=V+D is forbidden. At j=11, W Sym5 contains V while Wp Sym5=A+P+D. At j=12 and 16, the only possible coefficient is trivial and its character contains V. Odd j>=13 and even j>=18 exceed the budget.

Only O(-8) and W[-9] supply the required W at twist five. Each consumes the single A budget, so exactly one occurs. With W[-9], the residual P budget has two possibilities. With O(-8), the residual P+D budget has six. This gives exactly the eight types printed in the proof. Matching the top against S+T removes precisely the four with Wp[-5]. The four survivors are:

    I:   S[-5]+P[-6]+W[-9];
    II:  (P+D)[-6]+O(-8);
    III: S[-5]+P[-6]+O(-8)+O(-10);
    IV:  T[-5]+(V+1)[-8].

Each has rank 10 and degree -62. This is a complete necessary overlist; it is not a realizability assertion.

For I and III, S[-5] maps only to O(-2), by its complete cubic system. P[-6] is the only source of an O(0) row. If this row vanished, the kernel would have top (A+P)[-6], impossible against the next target O(-4). Thus the P sextic row is nonzero and onto. For II, D[-6] maps only to O(-2) and P[-6] only to O(0); strict-top forces both onto.

For IV, T[-5] maps only and onto O(0), O(-8) has neither component, and V[-8] can reach only O(-2). If its sextic row vanished, the next two complete rows give successively

    D[-6]+(V+1)[-8],
    S[-7]+(V+1)[-8],
    (A+V+1)[-8].

The middle extension splits with degree difference 1 even if the intervening V row is nonzero. The last top cannot inject into the next target's twist-eight sections A. Hence the V row must be nonzero and onto. This proves the full raw quotient O(-2)+O(0) in IV as well.

The exact kernels are consequently

    II -> a: S[-7]+(V+1)[-8];
    I  -> b: A[-6]+V[-8]+W[-9];
    III-> c: A[-6]+(V+1)[-8]+O(-10);
    IV -> d: D[-6]+O(-8)+Wp[-11].

They all have rank eight and degree -60. All lower zero-row claims hold: W is absent from Sym7 and Sym9, and the needed even degrees have no invariant. The last type d is indispensable and is not obtained by importing a balanced-target overlist.

## 5. Complete a,b,c descent and the first terminal defect

In a,b,c, the top complete cubic or quadratic row is onto O(-4). Only V[-8] can reach O(-2). If its row vanished in a, the next top A+V+1 would have to inject into A. If it vanished in b or c, the quadratic kernel W[-7] would next map onto O(-6), leaving V[-8] in a kernel whose next target is O(-8). The resulting top injection would contain V on the source side and only 1 on the target side. Thus all three cases force the full quotient O(-4)+O(-2).

Its exact kernels are

    a: (A+1)[-8]+Wp[-11];
    b: W[-7]+W[-9]+Wp[-11];
    c: W[-7]+O(-8)+O(-10)+Wp[-11].

The first fails strict-top against O(-6)+O(-4), whose twist-eight sections are A+D and have no invariant.

In b,c, W[-7] supplies O(-6), and only Wp[-11] can reach O(-4). The latter's nonzero septic system is onto. If it vanished, the two possible next kernels would be

    O(-8)+W[-9]+Wp[-11],
    2O(-8)+O(-10)+Wp[-11].

The second violates strict-top into O(-8). In the first, the actual O(-8) top maps isomorphically to that next target. Eliminating any lower graph leaves W[-9]+Wp[-11], whose top cannot map to the following O(-10) target. Thus the quotient is fully O(-6)+O(-4).

The resulting kernels are exactly

    O(-8)+W[-9]+O(-18),
    2O(-8)+O(-10)+O(-18).

Here the kernel of Wp[-11]->O(-4) is the line O(-18), by rank and degree and the absence of nontrivial one-dimensional characters. The second displayed kernel fails because the next target O(-8)+O(-6) has only one trivial twist-eight section. The possible extension of O(-18) by O(-8) has cohomology degree 10, in the correct orientation.

For the remaining kernel K6=O(-8)+W[-9]+O(-18), strict-top makes the first line an isomorphism to the O(-8) target. Its O(-6) row is zero; W[-9] also has zero O(-6) row. Only O(-18) can supply that row, through the unique invariant f12. If this coefficient were zero, the kernel would be W[-9]+O(-18), again failing strict-top into O(-10).

For nonzero f12 the raw image is exactly

    I=O(-8)+O(-18) subset O(-8)+O(-6),

with defect length 12. The two source lines inject as a rank-two sheaf and the W[-9] image lies in the already supplied first line. Removing its graph gives the actual K7=W[-9]. The next target is I(-2)=O(-10)+O(-20), not the twist of the saturation. Every map from W[-9] into it vanishes by ordinary degree, contradicting negative saturated horizontality. This confirms both the raw image and the final contradiction, including the divisor correction.

## 6. The split-specific d descent and its terminal defect

For d, D[-6] supplies O(-2) by its complete quartic row, O(-8) has neither component, and Wp[-11] can reach only O(-4). If the Wp row vanished, the next kernel would be S[-7]+O(-8)+Wp[-11]. Its cubic top supplies O(-4). Even if its lower Wp row to that same line is nonzero, the next kernel is

    (A+1)[-8]+Wp[-11],

because Ext1(Wp[-11],A[-8]) has cohomology degree 3. Strict-top into the following O(-6) fails on the trivial top coefficient. Thus the Wp row is nonzero and onto, giving

    K5=S[-7]+O(-8)+O(-18).

Its cubic S top maps only and onto O(-4) in the next target O(-6)+O(-4). O(-8) has no row. The O(-18)->O(-6) row is a multiple of f12, and O(-18)->O(-4) is zero because degree fourteen has no invariant.

If f12 is zero, the raw image is O(-4), the next kernel is (A+1)[-8]+O(-18), and strict-top into O(-6) fails. If f12 is nonzero, the exact raw image is

    O(-4)+O(-18) subset O(-6)+O(-4),

again of defect length 12, and the kernel is (A+1)[-8]. Its actual next target is O(-6)+O(-20), with twist-eight sections A only. The same trivial coefficient is impossible. Both alternatives are exhausted without replacing the raw image by its saturation.

Sections 3 through 6 verify the complete universal theorem, including the new split-specific branch.

## 7. Full independent check of the bc source application

### 7.1 Its initial top line and Euler characters

For F=(V+P)[-2], a rank-one top saturation O(k) in O(4)+O(6) has even k<=6. The k=6 possibility is the O(6) summand and cannot receive an injective V+P section map into Sym8=P+D. For k<=2 there are at most five twist-two sections, fewer than seven. Thus k=4. The absence of degree-two invariants makes this the direct O(4) line. Strict-top identifies the coefficient map V+P -> Sym6=V+P as an isomorphism, so the actual image is the complete, everywhere-surjective sextic system, with kernel T[-3].

The unique O(-10) source block maps isomorphically to the negative quotient; all higher blocks have zero map there by degree. Removing it gives the actual exact sequence

    E'=(V+P)[-2]+T[-3]+V[-4] -> O(4)+O(6),
    kernel K1,
    rank K1=14, deg K1=-54, maxdeg K1<=-3.

The top F already supplies H0(O(7)) at twist three. The lower T[-3]->O(6) channel is therefore the only additional section channel at that twist. Direct representation subtraction gives precisely

    chi(K1(3))=T-S,
    chi(K1(4))=2V+2P+D-A,
    chi(K1(5))=-W+2Wp+S+4T.

These calculations were independently recomputed, including V A=P+D, P A=V+P+D, V S=Wp+S+T, P S=S+2T, and T A=Wp+S+2T.

### 7.2 Zero lower-T channel

If the lower T has zero O(6) row, H0(K1(3))=2T. Its derivative top 2T[-3] has no O(-12) component. A rank-one image in O(2)+O(4) has even saturated degree k<=4. For k=4 it has only one T in its twist-three sections; for k<=2 it has at most six sections. Neither can contain 2T. Thus the top image has rank two.

After twist three this image is globally generated. If its determinant defect is delta, its degree is 12-delta and its section dimension is 14-delta. Strict-top gives 12<=14-delta, hence delta<=2. Invariance forces delta=0. The top therefore contains both positive direct summands. Any nonzero O(-12) projection of the full image would then raise generic rank to three, contrary to the endpoint bound. This proves the exact quotient K1/K2=O(2)+O(4) in this entire branch.

### 7.3 Nonzero lower-T channel and the exact K1 splitting

For a nonzero lower-T O(6) channel, the extra T section map is injective modulo the top O(4) image. Hence H0(K1(3))=T and H1(K1(3))=S.

The complete S-budget calculation supports only S[-5] or O(-8) below degree -4. Indeed j=5 allows only S; j=6 allows only a trivial coefficient by dimension, giving W rather than S; j=7 already exceeds dimension four; j=8 gives S from the trivial coefficient; later degrees exceed the budget. The S[-5] alternative would require the nongenuine degree-minus-four coefficient V+P-A. The O(-8) alternative requires exactly V+P. Therefore

    K1=T[-3]+(V+P)[-4]+O(-8).

Every map from this bundle to O(-12) vanishes by ordinary degree. Its derivative is entirely in O(2)+O(4).

### 7.4 Exhaustion of all top-T derivative patterns

Strict-top makes the T top nonzero. If both rows to O(2) and O(4) are nonzero, a rank-one saturation would have even degree 2 or 4. Degree 4 cannot project to O(2), while degree 2 cannot project equivariantly to O(4), because Sym2 has no invariant. Thus the top image has rank two. Its global-generation estimate is 6<=14-delta, so delta<=8<12 and delta=0. The full split quotient follows.

If the top maps only to O(2), it is the complete quintic system with kernel D[-4]. Only P[-4] among the next two irreducibles can reach O(4). A nonzero P row is a basepoint-free degree-eight system and gives the full split quotient. If that row is zero, the only remaining O(4) channel is O(-8)->O(4), a multiple of f12.

- If f12 is zero, the raw quotient is O(2), and K2=(V+P+D)[-4]+O(-8). Its top cannot inject into the next target O(0) at twist four.
- If f12 is nonzero, the raw quotient is O(2)+O(-8), and K2=(V+P+D)[-4]. The next target is O(0)+O(-10), not O(0)+O(2); its twist-four sections are still only D, giving the same contradiction.

In these kernel identifications the extension of the lower source by D[-4] has ordinary degrees 0 and 4 and splits. The nonzero f12 component is injective as a sheaf, so its source line disappears from the kernel. Its length-twelve defect is retained throughout.

If the top maps only to O(4), its septic T subsystem is basepoint-free. Its kernel is V[-4]+Wp[-5]: H1 at twist three is Wp, whose only supported lower block is Wp[-5], and the twist-four Euler character is T W-Sym8=V. Either nonzero sextic row from V[-4] or P[-4] to O(2) supplies that line and proves the full split quotient.

If both sextic rows vanish, O(-8) has no O(2) component because Sym10 has no invariant. The raw quotient is exactly O(4). The kernel is

    (2V+P)[-4]+Wp[-5]+O(-8).

Here the kernel of the top map is the subbundle in the extension and the remaining source is the quotient. The ordinary cohomology degrees are 0, -1, 4, and 3, all with vanishing H1. This verifies the potentially delicate Ext orientation. The next target is O(2), whose twist-four sections V+P cannot contain 2V+P. This is the last top-T alternative.

Every lower-T branch and every top-T image pattern therefore forces the exact raw quotient K1/K2=O(2)+O(4).

## 8. Exact actual-connection transfer for bc

Subtracting that quotient from K1 gives

    rank K2=12, deg K2=-60, maxdeg K2<=-4,
    chi(K2(4))=V-A,
    chi(K2(5))=-W+Wp+2T.

The subtracted characters are Sym6+Sym8=V+2P+D and Sym7+Sym9=Wp+S+2T. These are precisely the universal theorem's two character inputs, with no extra cohomology vanishing presumed.

The transfer is geometric, not merely numerical. The inclusion

    K1/K2 -> H O/K2

has locally free quotient H O/K1 because K1 is saturated in the original constant bundle. Thus its twist O(0)+O(2) is an actual subbundle of (H O/K2)(-2). Gauss factorization identifies the induced map from K2 with its actual second fundamental form followed through this inclusion. A monomorphic target inclusion preserves both its kernel and its raw image sheaf.

The profile-(1,1) endpoint supplies the rank bound at most two, and successive actual kernels and Gauss factorizations remain in the same constant ambient connection. Every hypothesis of the universal theorem is therefore met. Its contradiction excludes the rank-one top branch. PR814, Section 6, excludes the rank-two top branch of this same bc source. Rank zero was already excluded by strict-top. The stated whole-source conclusion follows, with no appeal to a balanced-bc argument.

## 9. Exact-interface corollary for bf

The bf corollary's source and source index match the original inputs. Its top cannot have rank zero. If its top has rank two, the nine independent twist-two sections give 9<=16-delta; hence delta<=7<12 and the image is onto. PR814 excludes the zero internal derivative channel, while PR830 excludes the nonzero internal channel for the same split target. This is a complete rank-two partition, not an assumption that a particular internal component is nonzero.

For top rank one, the exact bf interface theorem identified in the opening section supplies the raw quotient K1/K2=O(2)+O(4), the same rank/degree/maximal-degree conditions on K2, and exactly the two Euler characters required above. Its use here is consistent with its stated conditional scope.

As in bc, K1/K2 is an actual subbundle of H O/K2 because K1 is saturated. Its twist is therefore the required actual O(0)+O(2) target; the induced map has the actual derivative kernel and raw image. The same endpoint rank bound and Gauss factorization persist. This verifies the full composition, not just a matching tuple of characters. The universal theorem eliminates rank one, completing the whole bf-source exclusion. No horizontal splitting, balanced-target assertion, or saturation substitution is introduced by the corollary.

## 10. Verification method and conclusion

The mathematical review was supplemented by a separately written bounded abstract representation check using only the nine irreducibles, W-tensor recurrence, central parity, and the proved small cohomology budgets. It independently recovered the eleven supported K3 blocks, eight necessary types, four strict-top survivors, two initial rank-one types, and both small bc support lists. It also checked rank, degree, and Euler-character additivity for the complete and irreducible evaluation kernels, all four K3-to-K4 sequences, the subsequent full split quotients, both terminal raw images, and the bc interface.

Those arithmetic checks do not substitute for the basepoint-free arguments, actual-kernel factorization, saturation, Ext orientation, or strict-top reasoning. Each of these geometric steps was checked separately above. No selected actual HM/source coefficients, parameters, points, derivative evaluations, matrices, instance ranks, selected-model experiments, scans, or unapproved large computation were used.

The final conclusions are version-bound: the universal split-descent obstruction, the stated split-bc source exclusion, and the exact-interface split-bf corollary all pass at the hashes listed in this review. Their companion theorem/interface files must accompany the applications in publication or be pinned immutably. No broader label or frontier conclusion is certified here.
