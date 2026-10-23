# A single scalar-row branch remains for the source127 h-b-f edge

## Result and boundary

Consider the exact original zero-defect source

    G3.11.cce6e3ba4eeb, source_index127,
    (0,1,0,0,0,1,0,1),
    E=(P+D) O(-2)+T O(-3)+O(-8)+O(-10),
    A_q=O(-8)+O(2)+O(16),
    B_q=O(-18)+O(-4)+O(6).

Any actual realization must satisfy all of the following necessary conditions.

1. The D O(-2)->O(2) external row is nonzero.
2. The high-only P O(-2)->O(16) map is onto, with exact kernel W O(-7)+O(-10).
3. Its W O(-7)->D O(-4) internal component and its scalar O(-10)->O(-10) internal component are both nonzero. The latter target is the original O(-8) source summand twisted by -2. The additional O(-10)->T O(-5) component is retained and may be zero or nonzero.
4. The actual first span of P O(-2) is (Wp+T) O(-1), with full constant coefficient span C=V+P+D of dimension twelve. If N=E intersect (P O(-2))^+ and Y=N^+, then

       Y/(P O(-2))^+=W O(-3)+O(-6),
       C O/Y=O(20),

   and the O(-6) component maps nontrivially to the negative O(-6) summand of E^+/E=A_q(2).

All other high-P kernel and internal-row alternatives are excluded. This is an endpoint-sensitive branch reduction, not a whole-source exclusion or a claim that the remaining branch exists. No frontier count changes. No selected actual HM/source coefficients, parameters, points, derivative values, matrices, ranks, models, scans or large computation are used.

## 1. Pinned input and actual connection

The original actual/source data are at db51525015bb7c5e825833d550d08dedf6f6ea96, under

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The manifest pins ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md and both original JSON catalogs. They give the displayed source, rank E=17, degree E=-54, a saturated inclusion E in H O with dim H=30 and H=2A+2V+2P+2D, full constant span, and H0(E^-(2))=0. Original zero defect gives a saturated

    A2=E^+/E=O(-6)+O(4)+O(18) subset Q=H O/E.     (1)

Write L=O(18) for its high summand. All connections and intersections below are the actual ones in H O.

The other immutable dependencies, with all original bytes recorded in the manifest, are:

- PR859 at 6129e92a26572779003f3295227f688b77ed881c, research/hm/profile11-o16-high-p-divisor/PROOF.md: the high-P map for this exact h-b-f source is basepoint-free.
- PR867 at b2a12c98bc162062a938b7a7a6a90ab45786e340, research/hm/profile11-o16-cdf-kernels/PROOF.md, Section2: the profile-free thirteen-candidate rank-three kernel classification.
- PR802 at e484640a6565c278321bf6557860262c1ac1b7df, research/hm/profile11-o16-constant-span-exclusion/PROOF.md: the P+D high-only kernel list, nonzero internal polar obstruction and actual constant projection.
- PR796 at d2b43060c83328dd5118aee6b9288fcfa0c873ac, research/hm/profile12-quadratic-block-exclusion/PROOF.md: the saturated internal/external image principle.
- PR870 at 3a05d057a12d24d62bf3c8e0e96fa778a4022ad5, research/hm/profile11-source127-cf-exclusions/PROOF.md: the exact source127 dual endpoint and degree-38 dual obstruction, also restated in Section8 below.

Work over C with the binary icosahedral group G and notation W,Wp,A,V,P,S,D,T, where A=Sym2 W, S=Sym3 W, D=Sym4 W and T=Sym5 W. All irreducibles are self-dual and G has no nontrivial one-dimensional characters. Every nonempty invariant effective divisor has degree at least twelve.

If a subsystem has saturated external derivative image and saturated internal image J, its full raw image is saturated. Its first span M then has an exact extension by J(2) and the external image twisted by two. For quadratic subsystems, first polars generate M(1), so M has degrees only zero and minus one. For a saturated linear M=R O(-1), its derivative kernel is K1 O(-2), where K1 is the kernel of its constant coefficient map R W->C. These statements follow from the actual Euler maps, not from treating a bundle splitting as horizontal.

## 2. Five possible high-P kernels and all internal images

Let F=P O(-2). Its negative row vanishes by degree and its O(2) row vanishes because P is absent from Sym4 W. PR859 applies to this exact source and gives

    0 -> K -> P O(-2) -> O(16) ->0.

Strict-top and the two fixed characters give

    rank K=3, degree K=-24,
    H0(K(2))=0,
    H1(K(2))=A+V+P+D,
    chi_G(K(3))=-(W+S+T).

The complete thirteen-candidate check in PR867 Section2 therefore leaves exactly

    I. A O(-8);
    II. W O(-7)+O(-10);
    III. W O(-9)+O(-6);
    IV. Wp O(-3)+O(-18);
    V. O(-6)+O(-8)+O(-10).                       (2)

This classification uses only rank, degree, parity and those characters, so is independent of the different internal targets. The actual target here is

    (E/F)(-2)=D O(-4)+T O(-5)+O(-10)+O(-12).     (3)

Every possible component has multiplicity one:

- I: A(-8) to D(-4) or T(-5).
- II: W(-7) to D(-4); O(-10) to T(-5) or O(-10).
- III: W(-9) to D(-4) or T(-5); the scalar has no component.
- IV: O(-18) to D(-4) or T(-5); Wp(-3) has no component.
- V: O(-8) to D(-4); O(-10) to T(-5) or O(-10); O(-6) has no component.

The nonzero T maps in I and III are multiplication by the formal l^3 or l^4 and are everywhere injective. The D map in I is the Euler surjection A(-8)->W(-7) followed by multiplication by l^3. The D map in III is W(-9)->O(-8) followed by l^4. In II the W map is that same injective l^3 map. In II and V a nonzero scalar O(-10) image is saturated by its complete l^5 T component or its nonzero scalar isomorphism. In IV a nonzero degree-fourteen D covariant or degree-thirteen T covariant has no common divisor: dividing by a possible degree-twelve invariant divisor would require D in Sym2 W or T in Sym1 W. A combination is also saturated. All sums landing in different rows are saturated.

Thus the full list of saturated J is

    I: 0, W(-7), A(-8);
    II: 0, W(-7), O(-10), W(-7)+O(-10);
    III: 0, O(-8), W(-9);
    IV: 0, O(-18);
    V: 0, O(-8), O(-10), O(-8)+O(-10).           (4)

Zero J, a sole O(-8), or a sole O(-10) makes degree M equal to10,4,2 respectively, impossible in a constant bundle. For J=W(-9) or O(-8)+O(-10), M has rank7 and degree-4; its constant coefficient is A and its putative linear coefficient is Wp+T-S, not a genuine representation. Consequently III and V are excluded. The surviving alternatives are

    J=W(-7): M=(V+P) O;
    J=A(-8) or W(-7)+O(-10): M=(Wp+T) O(-1);
    J=O(-18): M=T O(-1).                         (5)

## 3. A projected scalar-plane obstruction

We first prove that no saturated full-span bundle

    Z=T O(-3)+O(-8)+O(-10)

in a constant space Hbar=A+V+P+2D can have saturated derivative image O(2)+O(-8).

The T(-3)->O(2) row is nonzero. Otherwise all external derivative rows of T(-3) vanish by degree. Its remaining internal targets are O(-10)+O(-12), also too low, making T(-3) horizontal. This is impossible for a negative bundle. The nonzero row is the complete degree-five T system, onto everywhere, with kernel D O(-4). The latter has zero internal derivative toward the two scalar summands. Hence the actual derivative of T(-3) has exactly this kernel, and D O(-4) differentiates inside T(-3).

Its derivative toward T(-3)/D(-4)=O(2), twisted by -2, is nonzero: otherwise D(-4) would be horizontal. The unique complete quartic map gives kernel S(-5). Repeating the same argument gives the complete chain

    O(-8), W(-7), A(-6), S(-5), D(-4), T(-3),

each term the actual saturated first span of the preceding one. The line O(-8) has coefficient space a quotient of Sym8 W=P+D. Its constant span contains the rank-six last term, whereas every proper subrepresentation of P+D has dimension at most five. Thus its span is the full C=Sym8 W, and T(-3) is the standard U5^8 there. In particular

    C O/T(-3)=A O(6).                            (6)

Project the ambient constant bundle by C. Let pi denote this constant projection and let N0=O(-8)+O(-10), with its original direct-sum lattice. The map pi on the second line L0=O(-10) is nonzero. If it were zero, L0 would lie in C; its map to (6) would vanish because

    Hom_G(O(-10),A O(6))=Hom_G(A,Sym16 W)=0.

It would then lie in T(-3), impossible since these are distinct direct summands of Z. The nonzero projected line has no zero divisor, since such an invariant divisor would have degree at most ten, less than twelve. Its nonzero constant coefficient span is a subrepresentation of Hbar/C=A+V+D, so has dimension at least three.

The derivative of pi(L0) lies in pi(N0). Indeed L0 has zero external component to O(-8), because Sym2 W has no invariant; its possible O(2) component is killed by projection, since that entire row is supplied inside the constant C by the T subsystem. All remaining derivatives lie in Z and project into pi(N0).

The generic rank of pi(N0) is two. If it had rank one, the projected line and its derivatives would remain in a one-dimensional generic fiber. Its projective map would be constant in characteristic zero, contrary to its coefficient span of dimension at least three. Thus N0->(Hbar/C) O is injective as a sheaf. Its coherent image N is isomorphic to the original lattice O(-8)+O(-10), regardless of whether that image is saturated in the ambient constant bundle.

Inside N the projected L0 is a direct summand, with quotient O(-8). Its derivative toward N/L0, twisted by -2, is a nonzero scalar map O(-10)->O(-10). It is therefore an isomorphism. The raw sheaf generated by L0 and its derivatives is exactly N: it contains L0 and surjects onto N/L0 everywhere. This is an equality of coherent images, not an inference from equal generic ranks or a presumed saturation.

But the first polar of any degree-ten line map is the image of W O(-9). Euler's identity includes the value in this polar image, so W O(-9) would surject onto N. Composing with the direct projection N->O(-10) is impossible, since Hom(W O(-9),O(-10))=0 by ordinary degree. This contradiction proves the obstruction.

## 4. The low D row and constant seven-space are excluded alternatives

Suppose D O(-2)->O(2) is zero. Then the entire top F0=(P+D) O(-2) maps only to O(16). It is onto because its P component is onto. Its exact high-only kernels are the three P+D forms of PR802 Section3. Against T(-5)+O(-10)+O(-12), their only possible nonzero internal image is O(-10). The nonzero-image first-polar contradiction in PR802 Section5 applies verbatim: it uses the P+D source, the saturated J=O(-10), and the three Euler channels after projection by its constant A, not any omitted negative endpoint.

Therefore J=0. Its actual first span is the constant C0=A+V+P, with C0/F0=L=O(18) saturated in Q. Constant projection produces a saturated full-span Z=E/F0 of exactly the form in Section3, with derivative image O(2)+O(-8). That section gives a contradiction. Thus the low D row must be nonzero.

Now consider the constant case M=(V+P) O in (5). Its image in Q is exactly L. Hence N=E intersect M has N/F=W O(-5). This quotient maps into E/F only through D O(-2): the T component would require W in T A=Wp+S+2T and the scalar targets vanish by degree. Its unique D map is multiplication by l^3, with quotient A O. Constant projection by M is saturated because M/N=L is saturated in Q. It gives

    E/N=A O+T O(-3)+O(-8)+O(-10).

Projecting again by this actual constant A produces the prohibited Z of Section3. Thus the constant alternative in (5) is impossible, without identifying an abstract splitting with a horizontal one.

## 5. Rank-eight first span: nine-space impossible, twelve-space conditional

For either rank-eight linear case in (5), first polars identify M=P W O(-1). Its constant span is a quotient of P Sym2 W=V+P+D and has dimension at least nine. It is therefore C=P+D of dimension nine, or C=V+P+D of dimension twelve. The exact N=E intersect M has

    N/F=A O(-6),              in case I;
    N/F=W O(-5)+O(-8),        in case II.           (7)

Both have rank N=7 and degree N=-26.

For C of dimension nine, the complete linear sequence gives C/M=O(8) and M^-=(V+P) O(-2). If N lies in M^-, their equal ranks and saturation in M make them equal, forcing the absent V O(-2) coefficient into E. Otherwise the derivative of N supplies C/M, and saturation puts C inside E^+. Its lower rows vanish: on M they factor through M/F=P O, which has no map to O(4) or O(-6), and the remaining quotient O(8) has no map to either lower row. Its image is exactly L, so its kernel in E has rank8 and degree-18. All its degrees are at most-2, forcing a degree-minus-two coefficient of dimension6 or7. Neither dimension occurs as a subrepresentation of the multiplicity-free top P+D. This excludes the nine-space.

For the full twelve-space, the complete quadratic Euler sequences give

    M/F=P O, C/M=P O(2), M^-=F,
    beta_M: M/F -> (C/M)(-2) is an isomorphism.

The saturated kernel (7) therefore produces Y=N^+ with

    Y/M=A O(-4),                 in case I;
    Y/M=W O(-3)+O(-6),           in case II;
    rank Y=11, degree Y=-20, C/Y=O(20).             (8)

C is not contained in E^+. If it were, its lower rows would factor through P O(2) and vanish: P is absent from Sym2 W and the negative degree is too small. Its high-only kernel would have rank11 and degree-18 inside E, impossible since every degree of E is at most-2. Thus E^+ intersect C=Y.

For case I the lower rows of Y vanish. The O(4) row of A O(-4) would require A in Sym8 W=P+D, and its O(-6) row vanishes by degree. Hence X=E intersect C has rank10, degree-38 and C/X is the extension O(18)->C/X->O(20). Section8 excludes it, so case I is impossible.

For case II the O(4) row vanishes because W is absent from Sym7 W and Sym10 W has no invariant. The W O(-3) component cannot map to O(-6), but the O(-6) component can map to the negative O(-6) row. If this last map is zero, the same degree-38 contradiction applies. Therefore it must be nonzero. This is exactly the endpoint-specific row that survives here and would be absent for a negative O(-8) row in A2.

Moreover this surviving row forces the internal scalar O(-10)->O(-10) component in (3) to be nonzero. The O(-8) factor of N/F=J(2) has a possible T(-3) component and its scalar O(-8) component. Only the latter can map to the original negative O(-8) quotient; the T component is too high by degree. The negative quotient itself is supplied only by the original O(-8) source summand, because the O(-10) source would require an invariant quadratic. Thus the negative map of Y is nonzero precisely when that scalar internal component is nonzero. The T component remains unrestricted.

## 6. The rank-six first span is impossible

In case IV, M=T O(-1). Its coefficient-map kernel contains P because beta_M kills F. Since T W=V+P+D and a negative rank-six bundle spans at least seven constants, its span is C=V+D, of dimension eight. The complete cubic Euler sequences tensored with Wp give

    M^-=F, C/M=Wp O(3), M/F=Wp O(1),
    beta_M: M/F -> (C/M)(-2) is an isomorphism.

Here N=E intersect M has N/F=O(-16). Its first span Y is saturated, with

    Y/M=O(-14), rank Y=7, degree Y=-20,
    C/Y=O(20).

If C lay in E^+, its lower rows would factor through Wp O(3) and vanish, since Wp is absent from Sym1 W and the negative target is too small. Its high-only kernel X would have rank7 and degree-18. Then X/F of rank3 and degree-10 would inject into D(-2)+T(-3)+O(-8)+O(-10). It has no degree-minus-two term, since a coefficient of dimension at most3 cannot map to irreducible D. At degree minus three only W or Wp can occur, and neither maps to T at equal degree or to D(-2), since D W=S+T. All its degrees would be at most-4, contradicting degree-10. Thus E^+ intersect C=Y.

The lower maps of Y factor through O(-14). The required invariant degrees are18 for O(4), and8 for O(-6); both invariant spaces are zero. Therefore X=E intersect C has rank6 and degree-38, with the same extension O(18)->C/X->O(20). Section8 excludes this case as well.

## 7. What remains, without a whole-source claim

Sections2-6 leave exactly case II with both indicated internal components nonzero, full twelve-space C, and its nonzero negative row in (8). They also force the low D row nonzero. These are the conditions in the result. No argument here discards that negative row or imports the source113 scalar-endpoint conclusion.

## 8. Uniform degree-38 saturation and the source127 dual contradiction

This section justifies every invocation above. Suppose C is an actual constant c-space, X=E intersect C has rank c-2 and degree-38, and U0=C/X is an extension of O(20) by the saturated L=O(18). The image U0 in Q and the projected E/X in (H/C) O have the same cokernel H/(E+C), hence the same saturation defect length delta. The latter has rank19-c and degree-16, and its saturation spans the constant (30-c)-space. Since its degrees are nonpositive,

    h0((E/X)^*_sat)=35-c-delta >=30-c.

Thus delta<=5, and invariance forces delta=0. U0 is saturated in Q. Its two possible equivariant splitting types are O(18)+O(20) and W O(19), because H1(O(-2)) is one-dimensional and trivial.

For R=(Q/U0)* the original actual presentation gives rank11, degree-16 and

    H1(R)=D,
    chi_G(R(3))=-W+Wp+S+4T.

Indeed H1(Q*)=A+2V+3P+4D, chi_G(Q*(3))=T-2W-S, while both U0 types have H1(U0*)=Sym16 W+Sym18 W=A+2V+3P+3D and chi_G(U0*(3))=-Sym13 W-Sym15 W. All degrees of R are at most-1. The only more-negative atoms whose H1 contribution fits the single-D budget are D O(-2) or O(-6). The first would force its linear coefficient L6 to satisfy L6 A=-W+Wp+3T, impossible. The second forces L10 A=Wp+S+4T, whose unique nonnegative solution is L10=2Wp+T, using

    W A=W+S, Wp A=T,
    S A=W+S+T, T A=Wp+S+2T.

Hence H0(R(1))=2Wp+T. Original strict-top for Q* injects H0(Q*(1)) into H0(B_q(1))=Sym7 W=Wp+T. The inclusion R subset Q* would inject two copies of Wp into one, a contradiction. This proves the asserted degree-38 obstruction with the exact source127 endpoint.
