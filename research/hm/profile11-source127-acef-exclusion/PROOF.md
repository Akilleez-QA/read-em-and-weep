# The source127 a-c-e-f edge is impossible

## Result and boundary

The entire original source edge

    G3.11.cce6e3ba4eeb, source_index127,
    (1,0,1,0,1,1,0,0),
    E=(P+D) O(-2)+Wp O(-3)+V O(-4)+Wp O(-5)+O(-8),
    A_q=O(-8)+O(2)+O(16),
    B_q=O(-18)+O(-4)+O(6), original defect zero

is impossible. This is not a whole-label exclusion or a global necessary-pair count. No assertion about the separate c-d-f abstract family follows.

The new checks are the complete changed internal target, a horizontal Wp(-3) obstruction after actual constant projection, and the exclusion of a rank-three degree-minus-ten quotient even though the new Wp(-3) channel is allowed. The rank-eight scalar-row branch is reduced to the precise geometric/cohomological interface of the independently established PR888 obstruction, with both zero and nonzero negative rows retained.

No selected actual HM/source coefficients, parameters, points, derivative values, matrices, instance ranks, models, scans or large computation are used.

## 1. Exact inputs and common conventions

The original actual presentation, strict-top theorem and both catalogs are pinned at db51525015bb7c5e825833d550d08dedf6f6ea96 of Akilleez-QA/read-em-and-weep, under

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The manifest records all exact Git blob hashes. The actual E is saturated in H O, spans H, and has

    H=2A+2V+2P+2D, dim H=30,
    rank E=17, degree E=-54, H0(E^-(2))=0,
    Q=H O/E, rank Q=13, degree Q=54, H0(Q*)=0.

The zero defect gives the actual saturated image

    A2=E^+/E=O(-6)+O(4)+O(18) subset Q.          (1)

Write L=O(18) for its high summand. The original dual presentation and strict-top give

    0 -> Q* -> M3* O(-1) -> M2* O ->0,
    M2=A+2V+3P+4D, M3=3Wp+3S+6T,
    H0(Q*(1)) injects into H0(B_q(1))=Wp+T.       (2)

The four other immutable proof inputs are:

- PR859, 6129e92a26572779003f3295227f688b77ed881c, research/hm/profile11-o16-high-p-divisor/PROOF.md. Its theorem explicitly covers the displayed a-c-e-f tuple and makes the high-P map basepoint-free.
- PR867, b2a12c98bc162062a938b7a7a6a90ab45786e340, research/hm/profile11-o16-cdf-kernels/PROOF.md, Section2. The complete kernel classification depends only on rank, degree and two fixed characters.
- PR885, 53939364de5459822be1a32be08f2b12dbbb4280, research/hm/profile11-source127-hbf-kernel-reduction/PROOF.md. We use the stated saturated internal/external derivative principle, quadratic first-polar identities and Section8's degree-38 obstruction.
- PR888, e9908b1d42d59c844abdb79bc734117a041f3d04, research/hm/profile11-source127-hbf-exclusion/PROOF.md. Sections1-4 prove the scalar-row interface obstruction restated in Section5 below. Its exact proof SHA256 is 1740dd7bb504cb49c726952373f74700e3396b7a8a94a1f89e7e3f6121775e38.

No whole theorem for a different source is transferred merely from its name. The changed source maps are checked below, and the interfaces used from the two h-b-f proofs are stated explicitly.

Work over C with binary icosahedral G. Its defining two-space is W, and A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W; Wp,V,P are the other irreducibles of dimensions2,3,4. All irreducibles are self-dual and G has no nontrivial line characters. A nonempty invariant effective divisor has degree at least twelve. All intersections and forward transforms below are the actual ones in the fixed constant H O, not horizontal interpretations of abstract splittings.

## 2. Exhaustive high-P kernels and actual internal images

Let F=P O(-2). It has no derivative to the negative row by degree or to O(2), since P is absent from Sym4 W. PR859 makes its high map onto. Its kernel K0 has rank3, degree-24,

    H0(K0(2))=0,
    H1(K0(2))=A+V+P+D,
    chi_G(K0(3))=-(W+S+T).

The exhaustive classification of PR867 therefore gives exactly

    I. A O(-8);
    II. W O(-7)+O(-10);
    III. W O(-9)+O(-6);
    IV. Wp O(-3)+O(-18);
    V. O(-6)+O(-8)+O(-10).                       (3)

Here the complete internal target is

    (E/F)(-2)=D O(-4)+Wp O(-5)+V O(-6)
               +Wp O(-7)+O(-10).               (4)

Every possible nonzero component, with multiplicity one, is

    I: A(-8) -> D(-4);
    II: W(-7) -> D(-4), O(-10) -> O(-10);
    III: W(-9) -> D(-4);
    IV: O(-18) -> D(-4) or Wp(-5);
    V: O(-8) -> D(-4), O(-10) -> O(-10).         (5)

For example the potential degree-thirteen Wp covariant in IV is retained; it is not a T covariant. All omitted maps vanish by degree or the character identities checked by the verifier. The D maps in I and III factor through the Euler quotients W(-7) and O(-8), followed by multiplication by l^3 and l^4, respectively. The W map in II is injective multiplication by l^3. The scalar maps in II and V are either zero or isomorphisms. In IV the degree-fourteen D and degree-thirteen Wp covariants are saturated: a possible degree-twelve divisor would require D in Sym2 W or Wp in Sym1 W, both absent. Thus every nonzero combination is saturated as well.

The complete actual internal-image list is

    I: 0, W(-7);
    II: 0, W(-7), O(-10), W(-7)+O(-10);
    III: 0, O(-8);
    IV: 0, O(-18);
    V: 0, O(-8), O(-10), O(-8)+O(-10).           (6)

Since the external O(16) is saturated, the internal/external image principle gives exact sequences

    0 -> J -> I_F -> O(16) ->0,
    0 -> F -> M=F^+ -> I_F(2) ->0.               (7)

First polars generate M(1), so its degrees are zero or minus one. Zero J, a sole O(-8) or a sole O(-10) gives positive degree M, impossible. The last image in V gives rank7, degree-4, constant coefficient A and putative linear coefficient Wp+T-S, impossible. Hence the only possibilities are

    J=W(-7): M=(V+P) O;
    J=W(-7)+O(-10): M=(Wp+T) O(-1);
    J=O(-18): M=T O(-1).                         (8)

## 3. The constant first span forces a horizontal negative block

Suppose M=(V+P) O is a constant seven-space. Its image in Q is exactly L. For N=E intersect M, (7) gives N/F=W O(-5). This quotient maps to E/F only through D O(-2). Its other possible same-or-higher-degree targets vanish: W is absent from Wp Sym2 W=T and V W=T, and W is inequivalent to Wp at degree minus five. The O(-8) target is too low. The unique D map is multiplication by l^3, with quotient A O.

Because M/N=L is saturated in Q, constant projection by M gives a saturated inclusion

    E/N=A O+Wp O(-3)+V O(-4)+Wp O(-5)+O(-8)
         subset (H/M) O.

The A O summand defines an actual constant subspace of H/M. Projecting by it produces a saturated residual

    Z=Wp O(-3)+V O(-4)+Wp O(-5)+O(-8)

whose raw derivative image is O(2)+O(-8): the two projections remove precisely the saturated high quotient L. Its top Wp O(-3) block has no external derivative, because Wp is absent from Sym5 W=T and the negative target is too low. Its internal derivative toward

    V O(-6)+Wp O(-7)+O(-10)

vanishes by degree. Thus this negative block is preserved by the trivial connection. A preserved coherent subbundle of a constant bundle is a constant degree-zero subbundle in characteristic zero, contradicting its degree -6. This excludes the constant alternative in (8).

## 4. The rank-eight span: exact scalar-row interface

Suppose M=(Wp+T) O(-1)=P W O(-1). Its constant span is a quotient of P Sym2 W=V+P+D. It has dimension at least nine, hence is C=P+D of dimension nine or C=V+P+D of dimension twelve. The actual N=E intersect M satisfies

    N/F=W O(-5)+O(-8), rank N=7, degree N=-26.    (9)

For dim C=9, the complete linear sequence gives C/M=O(8), M^-=(V+P) O(-2). If N lay in M^-, equal rank and saturation in M would give equality and force an absent V O(-2) coefficient in E. Otherwise its derivative supplies C/M, putting C inside E^+. All lower rows vanish: on M they factor through M/F=P O, and on C/M they vanish by degree. Thus E intersect C has rank8 and degree-18. Its degrees are at most-2, forcing a degree-minus-two coefficient of dimension6 or7, neither a subrepresentation of P+D. Hence dim C=9 is impossible.

For dim C=12, the complete quadratic Euler sequences give

    M/F=P O, C/M=P O(2), M^-=F,
    beta_M: M/F -> (C/M)(-2) is an isomorphism.

The first span Y=N^+ is saturated in C and satisfies

    Y/M=W O(-3)+O(-6),
    rank Y=11, degree Y=-20, C/Y=O(20).           (10)

C cannot lie in E^+. Its lower rows would factor through P O(2) and vanish, leaving a rank11 degree-18 kernel inside E, impossible when all its degrees are at most-2. Since Y is saturated and has codimension one in C, this proves E^+ intersect C=Y.

The O(4) row of Y vanishes: it kills M, and the two components in (10) would require W in Sym7 W or an invariant in Sym10 W. Its negative O(-6) row kills M and W O(-3), but its scalar O(-6) component may be zero or nonzero. The high row is onto L already on M. These are exactly the actual geometric hypotheses needed below. In particular, we do not discard the allowed negative row supplied by the original O(-8) source summand.

If the scalar row is zero, X=E intersect C has rank10 and degree-38, and C/X is an extension of O(20) by L. The PR885 Section8 obstruction applies. To recall the exact source-independent interface: for any constant c-space with X of rank c-2 and degree-38, the projected E/X has rank19-c, degree-16 and full span H/C. Shared-cokernel saturation defect is at most5, so invariance forces zero. The original presentation (2) then forces the dual residual top coefficient 2Wp+T, contradicting its injection into Wp+T. Only the rank/degree, original presentation and exact endpoint are used, all identical here.

If the scalar row is nonzero, Section5 below gives a contradiction. Thus both possible scalar values are covered.

## 5. The nonzero scalar-row obstruction applies with all hypotheses verified

For clarity we state the full interface extracted from PR888 Sections1-4. Assume (1)-(2), the fixed ranks and degrees in Section1, and an actual constant C=V+P+D of dimension twelve with F=P(-2) of full constant span C, M=F^+=(Wp+T)(-1), Y as in (10), E^+ intersect C=Y, zero middle row, and a nonzero scalar negative row on Y/M. No particular lower splitting of E is needed for the following argument.

The negative-row kernel Y0 is saturated in C, with

    Y0/M=W(-3), rank Y0=10, degree Y0=-14.

Then X=E intersect C is the kernel of the onto high row Y0->O(18), so rank X=9 and degree X=-32. The quotient V0=C/Y0 is positive of rank2, degree14: it is globally generated and H0(V0*)=0 because F spans C. Its Euler character is 1+A+V+P+D. The five possible positive center-even rank-two splittings are W O(7), Wp O(7), O(2)+O(12), O(4)+O(10), O(6)+O(8); only Wp O(7) has that character. Hence

    U0=C/X=O(18)+Wp O(7).

The extension splits since H1(Wp O(11))=0. Saturation is not presumed: the projected E/X has rank8, degree-22 and full span H/C of dimension18, so the shared defect delta is at most12. The only invariant possibilities are0 and12. At delta12 the dual quotient has rank10, degree-10, hence is pure O(-1), contradicting the dimension-eight bound in (2). Thus U0 is saturated.

For R=(Q/U0)*, exact cohomology of (2) now gives

    rank R=10, degree R=-22,
    H1(R)=V+P+D,
    chi_G(R(1))=-W.                              (11)

Every degree of R is at most-1. The complete atoms of degree at most-2 whose H1 contribution fits V+P+D, using (j-1)dim B<=12 and center parity, are

    V(-2), P(-2), D(-2), Wp(-3), T(-3),
    V(-4), P(-4), Wp(-5), O(-6), W(-7), O(-8), O(-10).

Their twist-one H1 characters are, in order,

    0, 0, 0, Wp, T, T, Wp+T, T, S, S+T, T, Wp+T.

Every one is W-free; any degree-minus-one coefficient contributes only nonnegative W multiplicity to H0(R(1)). This contradicts (11). PR888 proves the exhaustion and saturation argument in full, and the present verifier repeats the bounded character test. Section4 has supplied every actual geometric hypothesis, so this excludes the nonzero scalar row for a-c-e-f without transferring an unproved source-specific conclusion.

## 6. The rank-six span and the new rank-three injection check

In the last alternative M=T O(-1), its constant coefficient-map kernel contains P, since beta_M kills F. With T W=V+P+D and rank M=6, its full constant span is C=V+D of dimension eight. The complete cubic Euler sequences tensored with Wp give

    M^-=F, M/F=Wp O(1), C/M=Wp O(3),
    beta_M: M/F -> (C/M)(-2) is an isomorphism.

Here N=E intersect M has N/F=O(-16). Its saturated first span Y satisfies

    Y/M=O(-14), rank Y=7, degree Y=-20, C/Y=O(20).

Suppose C lay in E^+. Its lower rows would factor through Wp O(3) and vanish: Wp is absent from Sym1 W, and the negative degree is too small. Therefore X=E intersect C would have rank7 and degree-18, and X/F of rank3 and degree-10 would inject into

    D O(-2)+Wp O(-3)+V O(-4)+Wp O(-5)+O(-8).     (12)

There is no degree-minus-two coefficient in X/F: its coefficient has dimension at most three and cannot map to the irreducible D at equal degree. There is no higher degree either. Hence every ordinary splitting degree is at most-3. Rank3 and degree-10 force degrees (-3,-3,-4). By central parity the last line is the trivial-coefficient O(-4); its coefficient cannot mix with the odd degree-minus-three rank-two coefficient. But O(-4) has no map to any target in (12): D is absent from Sym2 W, Wp is absent from Sym1 W, the degree-zero V component has no invariant, and the other targets are too low. Thus the required injection is impossible, even though a Wp(-3) component itself can map nontrivially. This treats the new channel rather than incorrectly declaring all degree-minus-three maps zero.

It follows that E^+ intersect C=Y. The lower rows of Y factor through O(-14) and require invariant degrees18 and8, both absent. Thus X=E intersect C has rank6 and degree-38, and C/X is again an extension of O(20) by L. The exact obstruction recalled in Section4 excludes this final case.

All five high-P kernels, all their saturated internal images, both constant-span sizes and both negative scalar rows have now been exhausted. Together with the exact high-P divisor exclusion in PR859, this proves the whole displayed source edge.
