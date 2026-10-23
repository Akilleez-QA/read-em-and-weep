# The bb source at index 113 is impossible

## Statement and boundary

The entire original source edge

    G3.11.ad509d55173f, source_index 113,
    (0,2,0,0,0,0,0,1),
    E=P O(-2)+2T O(-3)+O(-10),
    A_q=O(-10)+O(2)+O(16),
    B_q=O(-18)+O(-4)+O(8), determinant defect zero

is impossible. We exclude the divisor-twelve branch and all five exact basepoint-free kernels of its high-P subsystem. The two final kernel branches require new actual constant-span arguments; in one branch a rank-two saturated quotient of degree 38 again forces the original dual strict-top contradiction.

This is one whole source-edge exclusion, not by itself a whole-label or frontier decrement. No selected actual source coefficients, parameters, points, derivative values, matrices, instance ranks, models, scans, or large computation are used. All maps and ranks below are universal bundle deductions, never selected source evaluations.

## 1. Pinned inputs and actual conventions

The original catalog, actual presentation and strict-top data are at immutable commit db51525015bb7c5e825833d550d08dedf6f6ea96:

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The exact files and Git blob hashes are:

- ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md: b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3.
- NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md: d7506dae49b4be43230450c4132bd5db91f137ef.
- one-one-endpoint-necessary-pairs.json: fe0afa410d89340d3082dc814277f89fbb582c19.
- rank-three-quotient-frontier-144.json: 8b5971092f9ef762584912609fd5e9301c4e271d.

The displayed tuple belongs to the complete ten-source overlist of index 113. The original decoder gives exactly the displayed E, of rank 17 and degree -54.

We use and restate the universal high-P kernel classification from PR867 section 2, commit b2a12c98bc162062a938b7a7a6a90ab45786e340:

https://github.com/Akilleez-QA/read-em-and-weep/blob/b2a12c98bc162062a938b7a7a6a90ab45786e340/research/hm/profile11-o16-cdf-kernels/PROOF.md

Its source-specific subsequent exclusions are not assumed. The divisor-twelve method is PR859, commit 6129e92a26572779003f3295227f688b77ed881c:

https://github.com/Akilleez-QA/read-em-and-weep/blob/6129e92a26572779003f3295227f688b77ed881c/research/hm/profile11-o16-high-p-divisor/PROOF.md

The dual degree-38 quotient obstruction is PR868 section 6, commit fb398486839583f8fbd561d6dfaa6ab7b9d3ad67:

https://github.com/Akilleez-QA/read-em-and-weep/blob/fb398486839583f8fbd561d6dfaa6ab7b9d3ad67/research/hm/profile11-source113-cf-exclusion/PROOF.md

Its actual assumptions are reproved here for this different source.

Work over C with the binary icosahedral group G, defining two-space W, other two-space Wp, A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and the even irreducibles V and P of dimensions 3 and 4. All irreducibles are self-dual. The group has no nontrivial one-dimensional characters. Every nonempty invariant effective divisor has degree at least 12; degree 12 gives the reduced exceptional orbit D12.

The actual E is saturated in H O, dim H=30, spans H, has all splitting degrees at most -2, and satisfies H0(E^-(2))=0. The original zero defect identifies

    E^+/E=A_q(2)=O(-8)+O(4)+O(18)                 (1)

with a saturated subbundle of Q=H O/E. All derivatives use the actual constant connection.

We use these standard actual-image facts. If a saturated F in E has saturated external derivative image U and saturated internal image J in (E/F)(-2), then its full raw derivative image I is saturated, with 0->J->I->U->0, and its first span M satisfies 0->F->M->I(2)->0. For a quadratic F=R O(-2), first polars give R W O(-1) onto the raw first span; when that span is saturated its splitting degrees are 0 and -1. For a saturated linear M=R O(-1), with coefficient-span map R W onto C and kernel K1, its actual derivative kernel is K1 O(-2). The latter follows directly from the Euler sequence and fiberwise injectivity of M in C O; no abstract splitting is declared horizontal.

## 2. The divisor-twelve branch is impossible in this exact source

Put F=P O(-2). It has no external component to O(-10) or O(2), by degree and P not occurring in Sym4 W=D. Strict-top injects its four sections into Sym18 W. A nonempty invariant common divisor has degree at most 15; parity and the absence of invariants in Sym14 W leave only degree 12.

If that divisor occurs, removing it leaves a basepoint-free P subsystem of Sym6 W=V+P. Its kernel is exactly V O(-4): H1 at twist 2 has budget V, and rank 3, degree -12 and parity force this single atom. The internal target for the present source is

    (E/F)(-2)=2T O(-5)+O(-12),                   (2)

so its internal derivative is zero by degree. The actual raw first span has rank 5 and degree -2, with quotient O(6) by F. Any saturation defect has invariant length at most 2, hence is zero. First-polar characters therefore give

    F^+=V O+Wp O(-1).

Project by the actual constant V. The induced map P O(-2)->Wp O(-1) is nonzero, since rank 4 cannot fit in a constant rank 3. Its unique equivariant channel is the tensor-Wp Euler surjection. Derivatives of its source land in Wp O(-1), so local lifting through the surjection makes the entire projected Wp O(-1) horizontal. Its negative degree contradicts horizontality. This excludes the divisor-twelve branch without replacing its unsaturated external image O(4) by O(16).

## 3. All five basepoint-free kernels and their internal channels

The high-P map is now onto O(16). Its kernel K has rank 3, degree -24, and

    H0(K(2))=0,
    H1(K(2))=A+V+P+D,
    chi_G(K(3))=-(W+S+T).                       (3)

The exhaustive classification in PR867 section 2, using only these invariants, is

    A O(-8);
    W O(-7)+O(-10);
    W O(-9)+O(-6);
    Wp O(-3)+O(-18);
    O(-6)+O(-8)+O(-10).                         (4)

For completeness, the rank-three coefficient possibilities are one dimension-three irreducible, one odd two-space plus a scalar, or three scalars. Rank, degree, parity, and absence of invariant H1 restrict them respectively to A(-8), V(-8); U(-3)+O(-18), U(-5)+O(-14), U(-7)+O(-10), U(-9)+O(-6), U=W or Wp; and scalar degree triples (6,6,12), (6,8,10), (8,8,8). Checking (3) on these thirteen cases gives exactly (4). These are necessary kernel forms, not asserted actual examples.

Against the exact target (2), the possible internal components are respectively

    A O(-8) -> 2T O(-5);
    O(-10) -> 2T O(-5);
    W O(-9) -> 2T O(-5);
    O(-18) -> 2T O(-5);
    O(-10) -> 2T O(-5).                          (5)

Every component to O(-12) is zero, including O(-18)->O(-12), since Sym6 W has no invariants. Each displayed Hom to one T row has multiplicity one. For the first, second and third maps, the universal nonzero maps are multiplication by the tautological third, fifth and fourth powers, respectively:

    Sym2 W tensor l^3 -> Sym5 W,
    l^5 -> Sym5 W,
    W tensor l^4 -> Sym5 W.

They are everywhere injective. With two T rows any nonzero multiplicity vector remains an everywhere-injective diagonal map. For the O(-18) map the six degree-thirteen sections form the unique T covariant. A common divisor could only have degree 12, but division would require T in Sym1 W, impossible. Thus this nonzero map is also everywhere injective. All possible nonzero internal images in (5) are saturated; the zero image is allowed initially.

Zero internal image always gives degree M=-8+18=10, impossible. The second and fifth kernels give only J=O(-10), hence degree M=2, again impossible. In the third case J=W O(-9) gives M rank 7 and degree -4. Its first-polar characters have constant coefficient A and purported linear coefficient Wp+T-S, which is not genuine. Thus this kernel is impossible too.

Only the first and fourth kernels remain. Their saturated nonzero internal images and first-span splittings are

    K=A O(-8), J=A O(-8), M=(Wp+T) O(-1);
    K=Wp O(-3)+O(-18), J=O(-18), M=T O(-1).     (6)

The rest of the proof excludes both.

## 4. Exclude A O(-8): only two coefficient spans are possible

Assume the first case of (6). Since P W=Wp+T, the first-polar map P W O(-1)->M is an isomorphism. The actual coefficient span C of F and M is a quotient of

    P Sym2 W=V+P+D.

It has dimension at least 9 because the negative rank-eight M cannot fill its constant span. The character is multiplicity-free, so only

    C=P+D, dim C=9,
    or C=V+P+D, dim C=12                        (7)

is possible. In either case N=E intersect M satisfies

    N/F=J(2)=A O(-6), rank N=7.                 (8)

### 4a. The nine-dimensional span

Here C=Sym8 W and M is the complete rank-eight linear evaluation kernel, with C O/M=O(8) and M^-=Sym6 W O(-2)=(V+P) O(-2).

If N lies in M^-, their equal ranks and saturation in M make them equal. This would embed a V O(-2) summand in E=P O(-2)+2T O(-3)+O(-10), but every such equivariant Hom is zero.

Otherwise the derivative of N has nonzero image in the line C O/M. Since N lies in E and F^+=M already lies in E^+, saturation forces C O to lie in E^+. Its map to the two lower rows in (1) vanishes on M and factors through O(8), so vanishes entirely by degree. The image is exactly L=O(18), since the image of M already equals L. Thus E intersect C O has rank 8 and degree -18.

This contradicts the degree bound for rank-eight subbundles of E. Its four largest degrees are -2 and its next four are -3, so that bound is -20. This excludes the first span in (7).

### 4b. The full twelve-dimensional quadratic span

Here the coefficient map P Sym2 W->C is an isomorphism. Under this actual coefficient identification, the usual complete quadratic Euler sequences give

    M/F=P O,
    C O/M=P O(2),
    M^-=F,
    beta_M: M/F -> (C O/M)(-2) is an isomorphism. (9)

The saturated A O(-6) in (8) therefore gives a saturated image A O(-4) in C O/M. Since N contains F, its first span contains M. Define Y=N^+; the actual derivative and (9) give

    Y/M=A O(-4), rank Y=11, deg Y=-20,
    C O/Y=O(20).                                (10)

In particular Y is saturated in C O and H O and lies in E^+.

The full C O cannot lie in E^+. If it did, its lower-row map would factor through P O(2). There is no map P O(2)->O(4), because P is absent from Sym2 W, and none to O(-8). Thus its image would be L, and its kernel would be rank 11, degree -18, inside E. The sum of E's eleven largest degrees is -29, a contradiction. Therefore E^+ intersect C O=Y.

The lower-row map of Y also vanishes. It is zero on M, and its quotient is A O(-4). The potential degrees are 8 and -4; A is absent from Sym8 W=P+D, and the negative degree gives zero. Hence Y maps onto exactly L. Put X=E intersect C O; then

    X=ker(Y->L), rank X=10, deg X=-38.

Taking kernels relative to M->L and using (8) and (10) gives an exact sequence

    0 -> A O(-6) -> X/F -> A O(-4) ->0.         (11)

The equivariant extension space is one-dimensional: it is the invariant part of End(A) tensor H1(O(-2)). Thus X/F is either

    A O(-6)+A O(-4),
    or A W O(-5)=(W+S) O(-5).                  (12)

But X/F injects into E/F=2T O(-3)+O(-10). In the split case the A O(-4) summand maps to neither target, since A is absent from T W=V+P+D. In the nonsplit case the W O(-5) summand maps to neither target, since W is absent from T A=Wp+S+2T. Both contradict injectivity. This excludes the second span in (7), hence the entire A(-8) kernel.

## 5. The last kernel forces an actual eight-space and a degree-38 quotient

Assume K=Wp O(-3)+O(-18). By (6), M=T O(-1). Let C be its actual coefficient span and K1 the kernel of T W->C. The linear-bundle derivative-kernel formula gives M^-=K1 O(-2). Since F is killed by beta_M, P is contained in K1. Since T W=V+P+D, C is a quotient of V+D. A negative rank-six bundle has span dimension at least 7, so

    C=V+D=Wp Sym3 W,
    M^-=P O(-2)=F,
    C O/M=Wp O(3),
    M/F=Wp O(1),                               (13)

and beta_M induces an isomorphism between the latter bundle and (C O/M)(-2). These identities are the complete cubic Euler sequences tensored with Wp.

Let N=E intersect M. The actual internal image gives

    N/F=O(-16), rank N=5.

This is the saturated kernel of the onto high-line map M/F=Wp O(1)->L=O(18). By (13) its derivative therefore gives a saturated O(-14) in C O/M. Since F^+=M, the exact first span Y=N^+ satisfies

    Y/M=O(-14), rank Y=7, deg Y=-20,
    C O/Y=O(20).                                (14)

It is saturated in C O and H O and lies in E^+.

First C O is not contained in E^+. If it were, the lower-row map would factor through C O/M=Wp O(3); it vanishes because Wp is absent from Sym1 W and the other degree is negative. Thus C O would map onto exactly L, and X=E intersect C O would have rank 7 and degree -18. Its quotient X/F would have rank 3 and degree -10 and inject into

    E/F=2T O(-3)+O(-10).                        (15)

All its splitting degrees would be at most -3. A degree-minus-three coefficient in a rank-three bundle has only possible odd irreducibles W or Wp, and neither maps to the degree-minus-three T target. Therefore no degree-minus-three term can occur at all, so its degree is at most -12, contradicting -10. This rules out C O contained in E^+.

Since Y has codimension one in C O, we now have E^+ intersect C O=Y. The map of Y to either lower row in (1) vanishes on M and factors through O(-14). The two potential invariant degrees are 18 and 6, neither of which has an invariant. Consequently Y maps onto exactly L. Hence

    X=E intersect C O=ker(Y->L),
    rank X=6, deg X=-38.                        (16)

Let U0=C O/X. This is a rank-two vector bundle, injected into Q, with

    0 -> O(18) -> U0 -> O(20) ->0,
    deg U0=38.                                 (17)

It remains essential to prove this injection is saturated. Put Z0=E/X in (H/C) O, and let delta be its saturation defect. The two maps U0->Q and Z0->(H/C) O have the same cokernel H O/(E+C O), hence the same torsion defect. Their residual data are

    rank Z0=11, deg Z0=-16, dim(H/C)=22.

Since E spans H, the saturation Z spans H/C. Its splitting degrees are nonpositive, so

    h0(Z*)=rank Z-deg Z=27-delta >=22.

Thus 0<=delta<=5. A nonzero invariant saturation defect has length at least 12, so delta=0. Therefore U0 is already saturated in Q. Denote it U. This proves (17) as an actual saturated quotient configuration, not an assumed residual saturation.

## 6. The original dual strict-top contradiction

The degree-38 extension (17) is either U=O(18)+O(20) or U=W O(19): Ext1_G(O(20),O(18))=H1(O(-2)) is the one-dimensional trivial representation. Both types have the same equivariant K-class.

Set R=(Q/U)*. Then

    0 -> R -> Q* -> U* ->0,
    rank R=11, deg R=-16.                       (18)

The original actual presentation, unchanged by this source stratum, is

    0 -> Q* -> M3* O(-1) -> M2* O ->0,
    M3=3Wp+3S+6T, M2=A+2V+3P+4D.

Hence H0(Q*)=0, H1(Q*)=M2, and chi_G(Q*(3))=T-2W-S. All splitting degrees of Q* and R are at most -1. Both U types give

    H1(U*)=Sym16 W+Sym18 W=A+2V+3P+3D,
    chi_G(U*(3))=-Sym13 W-Sym15 W.

Therefore

    H1(R)=D,
    chi_G(R(3))=-W+Wp+S+4T.                     (19)

The only negative atoms contributing to H1 budget D are D O(-2) or O(-6), as follows from the bound (j-1)dim U0<=5 and contribution U0 Sym(j-2) W. Thus R is L6 O(-1)+D O(-2) or L10 O(-1)+O(-6). The first requires L6 A=-W+Wp+3T, impossible. The second requires L10 A=Wp+S+4T. Using

    W A=W+S, Wp A=T,
    S A=W+S+T, T A=Wp+S+2T,

forces L10=2Wp+T. Hence

    R=(2Wp+T) O(-1)+O(-6).

The universal strict-top theorem applies to actual Q*, which has all degrees at most -1. For its original exact Gauss quotient B_q=O(-18)+O(-4)+O(8), it gives an injection

    H0(R(1))=2Wp+T -> H0(Q*(1))
      -> H0(B_q(1))=Sym9 W=S+T.

This is impossible because the target has no Wp. No stronger vanishing H0(Q*(1))=0 is used.

The final kernel is excluded. Combined with Sections 2-4, every branch of the high-P subsystem is impossible, proving the whole bb source-edge exclusion. This proof alone makes no claim about the remaining bf edge or the entire label.
