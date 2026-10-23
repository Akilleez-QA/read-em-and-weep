# The bf source at index 113 is impossible

## Statement and scope

The entire original source edge

    G3.11.ad509d55173f, source_index 113,
    (0,1,0,0,0,1,0,1),
    E=(P+D) O(-2)+T O(-3)+O(-8)+O(-10),
    A_q=O(-10)+O(2)+O(16),
    B_q=O(-18)+O(-4)+O(8), determinant defect zero

is impossible. The high-P subsystem has no divisor-twelve branch; all five basepoint-free kernels are excluded by exact internal images, actual constant spans, or a saturated rank-two degree-38 quotient and the original dual endpoint.

This is one whole source-edge result. It does not itself certify coverage of the rest of the label. No selected actual coefficients, parameters, points, derivative values, matrices, instance ranks, models, scans or large computation are used. All image-rank statements are universal bundle deductions.

## 1. Immutable inputs and actual conventions

The original source catalog, decoder, actual bundle presentation and strict-top theorem are pinned at db51525015bb7c5e825833d550d08dedf6f6ea96:

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The exact files and Git blob hashes are:

- ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md: b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3.
- NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md: d7506dae49b4be43230450c4132bd5db91f137ef.
- one-one-endpoint-necessary-pairs.json: fe0afa410d89340d3082dc814277f89fbb582c19.
- rank-three-quotient-frontier-144.json: 8b5971092f9ef762584912609fd5e9301c4e271d.

The exact displayed tuple is one of the ten original compatible source types for index 113. Its decoder yields rank E=17, deg E=-54 and the displayed E.

The complete high-P kernel classification is the universal part of PR867 section 2, commit b2a12c98bc162062a938b7a7a6a90ab45786e340:

https://github.com/Akilleez-QA/read-em-and-weep/blob/b2a12c98bc162062a938b7a7a6a90ab45786e340/research/hm/profile11-o16-cdf-kernels/PROOF.md

The divisor-twelve method is PR859, commit 6129e92a26572779003f3295227f688b77ed881c:

https://github.com/Akilleez-QA/read-em-and-weep/blob/6129e92a26572779003f3295227f688b77ed881c/research/hm/profile11-o16-high-p-divisor/PROOF.md

The degree-38 dual obstruction is PR868 section 6, commit fb398486839583f8fbd561d6dfaa6ab7b9d3ad67:

https://github.com/Akilleez-QA/read-em-and-weep/blob/fb398486839583f8fbd561d6dfaa6ab7b9d3ad67/research/hm/profile11-source113-cf-exclusion/PROOF.md

PR877, commit ea4facd73aa88c321adbbf4d7a4f30511c6e7592, verifies the related bb constant-span construction and degree-38 obstruction:

https://github.com/Akilleez-QA/read-em-and-weep/blob/ea4facd73aa88c321adbbf4d7a4f30511c6e7592/research/hm/profile11-source113-bb-exclusion/PROOF.md

All needed parts are restated, and the changed D row and both actual endpoint rows are tested below. No source-specific exclusion is transferred merely from the shared positive endpoint.

Work over C with the binary icosahedral group G and self-dual irreducibles W,Wp,A,V,P,S,D,T, where A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, dim V=3 and dim P=4. The group has no nontrivial one-dimensional characters. Every nonempty invariant effective divisor has degree at least 12; degree 12 is the reduced exceptional orbit D12.

The actual E is saturated in H O, dim H=30, spans H, has all splitting degrees at most -2 and satisfies H0(E^-(2))=0. Original zero defect gives a saturated inclusion

    E^+/E=A_q(2)=O(-8)+O(4)+O(18) in Q=H O/E.   (1)

Write L=O(18) for its highest line. Every derivative uses the original constant connection.

We use the actual-image principle: saturated external derivative image U and saturated internal image J imply a saturated full raw image I, with 0->J->I->U->0. The actual first span M then has 0->F->M->I(2)->0. For a quadratic F=R O(-2), first polars give R W O(-1) onto the raw first span; if saturated, its splitting degrees are 0 and -1. For a saturated linear M=R O(-1), the actual derivative kernel is K1 O(-2), where K1 is the kernel of its constant coefficient map R W->C. The latter follows from the Euler sequence and the fiberwise injectivity of M, not a horizontal interpretation of an abstract splitting.

## 2. The high-P line system is basepoint-free

Let F=P O(-2). Its components to O(-10) and O(2) vanish, by degree and P absent from Sym4 W=D. Strict-top injects P into Sym18 W. A nonempty common invariant divisor has degree at most 15; parity and Sym14 W=A+V+P+D leave only degree 12.

If that divisor occurs, the residual degree-six P system has kernel V O(-4). This is forced by its rank 3, degree -12, H0 at twist 2 equal to zero and H1 at twist 2 equal to V. Its internal derivative target is

    (E/F)(-2)=D O(-4)+T O(-5)+O(-10)+O(-12).    (2)

All maps from V O(-4) vanish, including the same-degree D row by irreducibility. The raw first span therefore has rank 5, degree -2 and quotient O(6) by F. Its invariant saturation defect is at most 2, hence zero. First-polar characters give M=V O+Wp O(-1).

Projection by the actual constant V gives a nonzero P O(-2)->Wp O(-1). Its unique channel is the tensor-Wp Euler surjection. Derivatives of its source lie in that linear target, so local lifting makes Wp O(-1) horizontal, contradicting its negative degree. Thus the divisor branch is impossible and the high map F->O(16) is onto.

## 3. Complete kernel list and every possible internal image

For K=ker(F->O(16)), the exact invariants are

    rank K=3, deg K=-24,
    H0(K(2))=0,
    H1(K(2))=A+V+P+D,
    chi_G(K(3))=-(W+S+T).

The complete list, from these invariants alone, is

    I.   A O(-8);
    II.  W O(-7)+O(-10);
    III. W O(-9)+O(-6);
    IV.  Wp O(-3)+O(-18);
    V.   O(-6)+O(-8)+O(-10).                    (3)

To recall exhaustiveness, a rank-three coefficient bundle has one dimension-three even irreducible, an odd two-space plus a scalar, or three scalars. Rank, degree, parity and the invariant-free H1 budget leave thirteen candidates: A(-8), V(-8); U(-3)+O(-18), U(-5)+O(-14), U(-7)+O(-10), U(-9)+O(-6), U=W or Wp; and scalar degree triples (6,6,12), (6,8,10), (8,8,8). The two displayed characters select exactly (3).

Against the exact target (2), the internal channels are as follows. All Hom spaces to one displayed irreducible target row have multiplicity one.

- I: A(-8) maps only to D(-4) and T(-5).
- II: W(-7) maps only to D(-4); O(-10) maps only to T(-5) and the scalar O(-10).
- III: W(-9) maps only to D(-4) and T(-5); O(-6) has no component.
- IV: Wp(-3) has no component; O(-18) maps only to D(-4) and T(-5).
- V: O(-6) has no component; O(-8) maps only to D(-4); O(-10) maps only to T(-5) and the scalar O(-10).

The following universal formulas establish the exact saturated images, rather than guessing from Hom multiplicities. The T components in I and III are multiplication Sym2 W tensor l^3 into Sym5 W and W tensor l^4 into Sym5 W, hence everywhere injective. The D component in I is the first transvectant with l^4; it factors through the Euler surjection A O(-8)->W O(-7), followed by the everywhere-injective multiplication W tensor l^3 into Sym4 W. The D component in III factors through the Euler surjection W O(-9)->O(-8), followed by the tautological l^4 line in Sym4 W. Thus its image is O(-8).

The II W component and V O(-8) component are those same everywhere-injective D maps. Any nonzero O(-10) component in II or V is a saturated line, by its tautological T component l^5 or nonzero scalar component. It lies in different target summands from the other nonzero image, so their sum is saturated.

In IV a nonzero D component is a degree-fourteen D covariant, and a nonzero T component is a degree-thirteen T covariant. Neither has a common divisor: a degree-twelve divisor would leave D in Sym2 W or T in Sym1 W, respectively, both impossible. No other nonempty invariant divisor of those degrees is available. Therefore every nonzero IV image is a saturated O(-18), including a combination of the two rows.

These facts give the complete saturated image lists

    I:   0, W O(-7), A O(-8);
    II:  0, W O(-7), O(-10), W O(-7)+O(-10);
    III: 0, O(-8), W O(-9);
    IV:  0, O(-18);
    V:   0, O(-8), O(-10), O(-8)+O(-10).         (4)

The alternatives in I correspond to a zero T row or a nonzero T row. No combination in (4) is asserted realizable.

The actual-image principle applies to each. Zero J gives degree M=10, impossible. A sole O(-8) gives degree 4; a sole O(-10) gives degree 2, also impossible. J=W(-9) gives rank M=7, degree -4 and first-polar coefficients A and Wp+T-S, impossible. The same impossible coefficients occur for J=O(-8)+O(-10). Thus III and V are completely excluded.

The remaining actual first-span alternatives are

    I or II, J=W O(-7):       M=(V+P) O;
    I, J=A O(-8):            M=(Wp+T) O(-1);
    II, J=W O(-7)+O(-10):    M=(Wp+T) O(-1);
    IV, J=O(-18):            M=T O(-1).         (5)

## 4. The constant seven-space alternative is impossible

Suppose M=C O=(V+P) O. Its image in Q is exactly the saturated L. Hence N=E intersect C O has

    N/F=W O(-5), rank N=6, deg N=-18.

Its extension by F splits because H1(O(3))=0. The map of N/F into E/F has only the D O(-2) component: the T component would require W in T A=Wp+S+2T, and both scalar components vanish by degree. The unique D map is multiplication W tensor l^3 into Sym4 W. The complete quartic jet sequence therefore gives

    D O(-2)/(W O(-5))=A O.

Constant projection by C is legitimate and saturated because C/N=L is saturated in Q. It produces the actual embedded bundle

    E/N=A O+T O(-3)+O(-8)+O(-10)

whose derivative image is the saturated O(-10)+O(2). Project again by its actual constant A. The remaining bundle is

    Z=T O(-3)+O(-8)+O(-10),
    derivative image O(-10)+O(2).               (6)

The canonical O(-8) in Z has zero external derivative: its O(-10) component vanishes by degree and its O(2) component would require an invariant in Sym10 W=A+V+D. Its internal derivative into (Z/O(-8))(-2)=T O(-5)+O(-12) also vanishes: T is absent from Sym3 W=S, and the last degree is too small. It would therefore be a negative horizontal line in a constant bundle, impossible. This rules out the first case in (5).

The exact negative endpoint O(-10) is essential to this last argument; it is not asserted for a source with O(-8) instead.

## 5. Both rank-eight linear cases have only two possible spans

Consider either middle case of (5). Since P W=Wp+T, first polars identify M with P W O(-1). Its actual coefficient span C is a quotient of the multiplicity-free P Sym2 W=V+P+D and has dimension at least 9. Thus either

    C=P+D, dim C=9,
    or C=V+P+D, dim C=12.                       (7)

The exact intersection N=E intersect M satisfies

    N/F=A O(-6),
    or N/F=W O(-5)+O(-8),                       (8)

respectively. Both have rank N=7 and degree N=-26.

### 5a. Exclude the nine-space

Here C=Sym8 W, M is the complete linear evaluation kernel, C O/M=O(8), and M^-=(V+P) O(-2). If N lies in M^-, their equal ranks and saturation in M make them equal. This would embed V O(-2) in E, but the top coefficient of E is P+D and every such Hom is zero.

Otherwise the derivative of N supplies the line C O/M. Since N is in E, saturation forces C O inside E^+. Its lower-row map factors through O(8) and vanishes by degree. Hence it maps onto exactly L, giving a rank-eight, degree-minus-eighteen kernel X inside E.

Such an equivariant X cannot occur. Its ordinary degrees are at most -2, and its degree excess relative to eight copies of -2 is 2. Thus the only degree patterns are six copies of -2 with two of -3, or seven copies of -2 with one of -4. Its coefficient at degree -2 therefore has dimension 6 or 7 and must inject into the top P+D of E. The possible subrepresentation dimensions of the multiplicity-free P+D are 0,4,5,9, not 6 or 7. This contradiction excludes C of dimension 9.

### 5b. The twelve-space forces a degree-38 quotient

Here the full quadratic coefficient map P Sym2 W->C is an isomorphism, so the actual Euler sequences give

    M/F=P O,
    C O/M=P O(2),
    M^-=F,
    beta_M: M/F -> (C O/M)(-2) is an isomorphism.

The saturated subbundle N/F in (8) therefore yields Y=N^+ with

    Y/M=A O(-4),
    or Y/M=W O(-3)+O(-6),
    rank Y=11, deg Y=-20,
    C O/Y=O(20).                                (9)

Saturation holds because (8) is the kernel of the onto high-line map M/F->L, and beta_M is an isomorphism. Also Y lies in E^+.

C O is not contained in E^+. If it were, its lower-row map would factor through P O(2), whose Hom to O(4) vanishes because P is absent from Sym2 W, and whose Hom to O(-8) vanishes by degree. The kernel of C O->L would have rank 11 and degree -18 inside E, whereas E's eleven largest ordinary degrees sum to -24. This is impossible. Therefore E^+ intersect C O=Y.

The lower-row map of Y vanishes as well. It factors through the two alternatives in (9). For A O(-4)->O(4), A is absent from Sym8 W=P+D. For W O(-3)->O(4), W is absent from Sym7 W=Wp+T. For O(-6)->O(4), Sym10 W=A+V+D has no invariant. All their components to O(-8) vanish by degree. Thus Y maps onto exactly L and

    X=E intersect C O=ker(Y->L),
    rank X=10, deg X=-38,
    0 -> O(18) -> C O/X -> O(20) ->0.          (10)

Section 7 proves this rank-two quotient is saturated in Q and impossible.

## 6. The rank-six linear case has the same degree-38 obstruction

In the final case of (5), M=T O(-1). Let K1 be the kernel of its coefficient map T W->C. Since beta_M kills F, the linear-bundle kernel formula puts P inside K1. Since T W=V+P+D and a negative rank-six bundle spans at least seven constants, necessarily

    C=V+D=Wp Sym3 W,
    M^-=P O(-2)=F,
    C O/M=Wp O(3),
    M/F=Wp O(1).                               (11)

These are actual complete cubic Euler sequences tensored with Wp, with beta_M inducing an isomorphism between the last bundle and (C O/M)(-2).

The exact N=E intersect M has N/F=O(-16), the saturated kernel of M/F->L. Hence Y=N^+ is saturated and satisfies

    Y/M=O(-14), rank Y=7, deg Y=-20,
    C O/Y=O(20).                               (12)

First C O is not contained in E^+. Otherwise its lower-row map would factor through Wp O(3) and vanish, since Wp is absent from Sym1 W. The kernel X of C O->L would have rank 7 and degree -18. Its quotient X/F, of rank 3 and degree -10, would inject into

    E/F=D O(-2)+T O(-3)+O(-8)+O(-10).          (13)

Its splitting degrees are at most -2. A top degree-minus-two coefficient of rank at most 3 cannot map to the irreducible D coefficient of dimension 5, so there is no degree-minus-two term. At degree minus three only W or Wp can occur in rank 3; neither maps to T at equal degree or to D O(-2), since D W=S+T contains neither. Therefore every degree is at most -4, giving degree at most -12, contradicting -10.

Thus E^+ intersect C O=Y. The map of Y to either lower row factors through O(-14); the possible invariant degrees are 18 and 6, both invariant-free. Its image is exactly L, so

    X=E intersect C O=ker(Y->L),
    rank X=6, deg X=-38,
    0 -> O(18) -> C O/X -> O(20) ->0.          (14)

Again Section 7 applies.

## 7. A uniform full-span lemma makes both rank-two quotients saturated

In either (10) or (14), put c=dim C, so c=12 or 8. The actual quotient U0=C O/X injects into Q and is a rank-two extension of O(20) by O(18). The projected Z0=E/X injects into (H/C) O. The two maps have the same cokernel H O/(E+C O), so the torsion lengths of their respective saturation quotients agree; call the length delta.

The residual data are

    rank Z0=19-c,
    deg Z0=-16,
    dim(H/C)=30-c.

Because E spans H, the saturation Z spans H/C. Its splitting degrees are nonpositive, so

    h0(Z*)=rank Z-deg Z=35-c-delta >=30-c.

Thus 0<=delta<=5. A nonzero invariant effective defect divisor has degree at least 12. Therefore delta=0: U0 is already saturated in Q. Denote it U.

This is the actual saturation proof. A residual projection has not been assumed saturated, and its possible torsion is eliminated before applying the dual obstruction.

## 8. The exact original dual endpoint contradicts the degree-38 quotient

The extension U is either O(18)+O(20) or W O(19), because the equivariant extension space H1(O(-2)) is one-dimensional and trivial. Put R=(Q/U)*. Then

    0 -> R -> Q* -> U* ->0,
    rank R=11, deg R=-16.

The original presentation gives

    0 -> Q* -> M3* O(-1) -> M2* O ->0,
    M3=3Wp+3S+6T,
    M2=A+2V+3P+4D.

Hence H0(Q*)=0, H1(Q*)=M2 and chi_G(Q*(3))=T-2W-S. All splitting degrees of Q* and R are at most -1. Both U types have

    H1(U*)=Sym16 W+Sym18 W=A+2V+3P+3D,
    chi_G(U*(3))=-Sym13 W-Sym15 W.

Consequently

    H1(R)=D,
    chi_G(R(3))=-W+Wp+S+4T.

The only degree-at-most-minus-two atoms with H1 contained in the budget D are D O(-2) and O(-6); this follows from (j-1)dim U0<=5 and the contribution U0 Sym(j-2) W. Thus R is L6 O(-1)+D O(-2) or L10 O(-1)+O(-6). The first would force L6 A=-W+Wp+3T, impossible. The second requires L10 A=Wp+S+4T. The four odd irreducible products

    W A=W+S, Wp A=T,
    S A=W+S+T, T A=Wp+S+2T

force L10=2Wp+T. Hence R=(2Wp+T) O(-1)+O(-6).

Strict-top for actual Q*, whose splitting degrees are at most -1, injects H0(Q*(1)) into the original B_q endpoint. Thus

    2Wp+T=H0(R(1)) -> H0(Q*(1))
      -> H0(B_q(1))=Sym9 W=S+T

is injective, impossible since the target has no Wp. No stronger vanishing H0(Q*(1))=0 is assumed.

This excludes both remaining span cases. Every branch of (3)-(5), as well as the divisor-twelve branch, has now been excluded. The entire source113 bf tuple is impossible. No separate source or label count is asserted by this proof alone.
