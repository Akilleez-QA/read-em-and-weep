# Six source-edge exclusions for the three retained O(16) labels

## Result and scope

The following six source edges are impossible. Each statement concerns the complete source stratum, not merely a basepoint-free branch:

- G3.11.ad509d55173f, source index113: tuples (0,0,0,0,1,1,0,1), (0,0,1,0,1,0,0,1), and (0,1,0,0,1,0,0,1).
- G3.11.ea6bced3bddf, source index125: tuple (0,0,0,0,2,0,0,1).
- G3.11.cce6e3ba4eeb, source index127: tuples (0,0,0,0,1,1,0,1) and (0,0,0,0,1,0,1,0).

The main new step is a two-P quadratic-subsystem obstruction. Its only nonzero internal-image alternatives are treated as actual saturated images. One alternative has an impossible first-polar character; the other forces a constant V and two linear channel rows that cannot coexist with the actual connection. A separate V+2P subsystem is excluded by the rank-one quadratic Gauss gap.

No whole stable label is excluded, no necessary-pair count is claimed, and no source outside the six displayed edges is removed. All computations are small fixed abstract representation identities and exact original-catalog reads. No selected actual HM/source coefficients, parameters, points, derivative values, matrices, instance ranks, selected models, scans, or large computation occur.

## 1. Immutable dependencies and complete original scope

All original actual-source, quotient, strict-top and label data below are at commit db51525015bb7c5e825833d550d08dedf6f6ea96 of Akilleez-QA/read-em-and-weep:

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The files and Git blob hashes are:

- ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md: b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3.
- NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md: d7506dae49b4be43230450c4132bd5db91f137ef.
- ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md: dcacf0bcdef8377c1ed7654e5b82659ea409456e.
- one-one-endpoint-necessary-pairs.json: fe0afa410d89340d3082dc814277f89fbb582c19.
- rank-three-quotient-frontier-144.json: 8b5971092f9ef762584912609fd5e9301c4e271d.

The labels are exactly

    index113: A_q=O(-10)+O(2)+O(16), B_q=O(-18)+O(-4)+O(8);
    index125: A_q=O(-10)+O(4)+O(16), B_q=O(-18)+O(-6)+O(8);
    index127: A_q=O(-8)+O(2)+O(16), B_q=O(-18)+O(-4)+O(6).

All three original determinant defects are zero. The complete source lists of indices113 and125 are the same ten tuples: a=d=g=0, h=1, b+c+e+f=2. For index127 the entire thirteen-tuple list is

    (0,0,0,0,0,2,0,1), (0,0,0,0,1,1,0,1),
    (0,0,1,0,0,1,0,1), (0,1,0,0,0,1,0,1),
    (0,0,0,0,0,1,1,0), (0,0,0,0,1,0,1,0),
    (0,0,1,0,0,0,1,0), (0,1,0,0,0,0,1,0),
    (0,0,1,1,0,1,0,0), (1,0,1,0,0,2,0,0),
    (1,0,1,0,1,1,0,0), (1,0,2,0,0,1,0,0),
    (1,1,1,0,0,1,0,0).

These are necessary overlists, not realizability assertions. The complete decoding formula is

    E=((c+g+h-1)V+(d+e+g+h)P+(f+g)D) O(-2)
      +(a Wp+b T) O(-3)+(c V+d P) O(-4)
      +e Wp O(-5)+f O(-8)+g W O(-9)+h O(-10).

We use the actual internal/external derivative-image lemma of PR796, Section3, and its profile-free rank-one quadratic gap in Section8, at commit d2b43060c83328dd5118aee6b9288fcfa0c873ac:

https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

The first-polar generation principle is restated in PR802, Section5, at e484640a6565c278321bf6557860262c1ac1b7df:

https://github.com/Akilleez-QA/read-em-and-weep/blob/e484640a6565c278321bf6557860262c1ac1b7df/research/hm/profile11-o16-constant-span-exclusion/PROOF.md

The two proof blobs are 46a0de762000f21182f6d3168f3ecfd63adaf75f and 98a1bd6123e148476da0b997d879aecbf885ec97. The arguments needed from them are restated below; no unpublished source exclusion or source-completion count is a dependency.

## 2. Actual conventions and two exact line-system kernels

Work over C with the binary icosahedral group G, defining two-space W, other two-space Wp, A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and other even irreducibles V,P of dimensions3,4. All irreducibles are self-dual. Every nonempty invariant effective divisor on P1 has degree at least12. For an actual subbundle F in a constant bundle, F^+ denotes its saturated forward transform, and its derivative has target the ambient quotient twisted by -2.

The actual E is saturated in H O, has rank17, degree-54, H0(E(1))=0, and H0(E^-(2))=0. Original defect zero identifies A_q with the saturated subbundle B_q^*(-2) of Q(-2), Q=H O/E. In particular the positive O(16) direct summand is saturated in Q(-2).

Suppose F=(mV+2P) O(-2), m=0 or1, is an actual saturated subbundle of E whose quotient image lies in O(16). Strict-top gives an injection mV+2P -> H0(O(18)). A common divisor of this line system would leave at most h0(O(6))=7 sections, fewer than rank F>=8. Thus the map p:F->O(16) is onto everywhere, with no divisor alternative. Set K0=ker p. Then

    H0(K0(2))=0,
    H1(K0(2))=A+(1-m)V+D,
    chi_G(K0(3))=Wp+mT-W-S.                         (1)

Here Sym18 W=A+V+2P+D and Sym19 W=W+Wp+S+2T.

The exact complete kernel list is

    K0=(Wp+mT) O(-3)+(1-m)V O(-4)+W O(-7),
    or K0=(Wp+mT) O(-3)+(1-m)V O(-4)+O(-6)+O(-8). (2)

For completeness, an atom Z O(-j), j>=4, contributes Z Sym(j-4) W to the H1 budget in (1). The bound (j-3)dim Z<=11 and central parity yield precisely the following atoms fitting A+V+D:

    atom              H1 at twist2       H1 at twist3
    A O(-4)                 A                   0
    V O(-4)                 V                   0
    D O(-4)                 D                   0
    S O(-5)                A+D                  S
    O(-6)                   A                   W
    W O(-7)                A+D                 W+S
    Wp O(-7)               V+D                  T
    O(-8)                   D                   S
    O(-14)                A+V+D                S+T.

At j4 the support is immediate. At j5 only S fits: W W contains1, Wp W=P is forbidden, and T exceeds the dimension bound. At j6 the trivial coefficient fits, while A^2 contains1 and V A=P+D contains forbidden P. At j7 the W and Wp coefficients give the two listed rows. At j8 only the trivial coefficient fits. Every odd j>=9 exceeds the bound; the only possible even degrees thereafter are10,12,14, contributing V+P, P+D, A+V+D respectively. Only14 survives. Larger degrees exceed the bound. For m=1 remove every atom with V in its budget.

The negative W in (1) forces exactly one of O(-6), W O(-7), each consuming the unique A. With W O(-7) chosen the remainder is (1-m)V O(-4). With O(-6) chosen an S tail is still necessary, forcing O(-8), followed again by (1-m)V O(-4). All other rows consume the already used A, have no S tail, or contain forbidden constituents. The degree-minus-three coefficient is then exactly Wp+mT. This proves (2), rather than merely checking two possible kernels.

## 3. The two-P subsystem with a complementary D is impossible

Consider either bundle

    E=(2P+D) O(-2)+Wp O(-5)+O(-8)+O(-10),
    E=(2P+D) O(-2)+Wp O(-5)+W O(-9),               (3)

when A_q has positive part O(2)+O(16). Take F=2P O(-2), a saturated constant-multiplicity subblock of the top splitting block. It has no map to O(2), because Sym4 W=D contains no P, and no map to the negative quotient by degree. Thus Section2 applies with m=0.

The actual internal derivative is

    kappa:K0 -> (E/F)(-2)
       =D O(-4)+Wp O(-7)+O(-10)+O(-12),

or D O(-4)+Wp O(-7)+W O(-11). All components from (2) vanish except

    W O(-7) -> D O(-4),
    or O(-8) -> D O(-4),                           (4)

respectively. In particular V->D and W->Wp are zero by irreducibility; O(-6)->D O(-4) and O(-8)->Wp O(-7) vanish because D is absent from Sym2 W and Wp is absent from W.

Both nonzero maps in (4) are unique up to scalar and saturated. At an arbitrary tautological line l in W they are, respectively, multiplication W tensor l^3 -> Sym4 W and the tautological l^4 line in Sym4 W. They are injective at every l; their ranks never drop. This is a universal formula, not evaluation at a selected point.

Thus the actual internal image J is exactly one of

    0, W O(-7), O(-8).                            (5)

Every alternative is saturated in (E/F)(-2). Since the external O(16) is saturated, the internal/external image lemma gives the actual saturated raw derivative image I and first span M=F^+ with

    0 -> J -> I -> O(16) ->0,
    0 -> F -> M -> I(2) ->0.                      (6)

No saturation correction or discarded divisor is hidden in (6).

If J=0, then deg M=-16+18=2. A subbundle of a constant bundle cannot have positive degree. This excludes that alternative.

If J=O(-8), equation (6) gives rank M=10, degree-4. First polars supply an onto map (2P) W O(-1)->M. Hence all splitting degrees of M are0 or-1: M(1) is generated, and M is a subbundle of a constant bundle. Its constant coefficient C=H0(M) and linear coefficient L must satisfy

    C=chi_G(M)=A+V,
    C W+L=chi_G(M(1))=W+Wp+2T.

Because (A+V)W=W+S+T, this would give L=Wp+T-S, not a genuine representation. Thus J=O(-8) is impossible.

If J=W O(-7), equation (6) instead forces

    M=V O+(Wp+T) O(-1).                           (7)

Indeed chi_G(M)=V and chi_G(M(1))=Wp+2T. The constant V in (7) is an actual subspace of H, because sections of an ambient constant bundle are constant. Projecting by this V gives a saturated actual inclusion

    L0=(Wp+T) O(-1) subset (H/V) O.

The projected image bar F and its derivatives lie in L0. No entire nonzero direct linear block can lie in bar F: its first span is its nonzero constant coefficient span, and the actual derivative condition would place that constant space inside L0, contrary to H0(L0)=0.

The map 2P O(-2)->L0 has exactly two linear channel rows on the two-dimensional P multiplicity space, lambda to Wp and mu to T. Both channels are one-dimensional because P W=Wp+T. If the two rows are linearly dependent, including either row being zero, their common kernel contains a P O(-2) of rank4. That block would map into constant V of rank3, contradicting injectivity of F->H O. If they are independent, a P multiplicity line killed by mu but not lambda maps onto the full Wp O(-1). This map is the tensor-Wp Euler map

    P O(-2)=(Wp W) O(-2) -> Wp O(-1),

which is everywhere onto. It gives the forbidden full linear block in bar F. Both cases are impossible, proving the obstruction for (3).

This excludes source113's first tuple in the result, and both stated source127 tuples. The different negative quotient degrees do not affect the argument.

## 4. The be source of index113 is impossible

Here

    E=2P O(-2)+T O(-3)+Wp O(-5)+O(-10).

Again F=2P O(-2) maps only to saturated O(16), and Section2 with m=0 gives exactly (2). The internal target is

    T O(-5)+Wp O(-7)+O(-12).

Every component is zero. Beyond the degree and inequivalent-scalar vanishings, the only possible checks are W O(-7)->T O(-5), O(-6)->T O(-5), and O(-8)->T O(-5). They vanish because W is absent from T Sym2 W=Wp+S+2T, and T is absent from Sym1 W and Sym3 W. The O(-8)->Wp O(-7) channel is zero as above. Thus J=0, and the actual first span has degree2 by (6), impossible.

## 5. The ce source of index113 is impossible

Here

    E=(V+2P) O(-2)+V O(-4)+Wp O(-5)+O(-10).

Take the full top F=(V+2P) O(-2). Neither V nor P occurs in Sym4 W=D, so F again maps only to O(16). Section2 with m=1 gives

    K0=(Wp+T) O(-3)+W O(-7),
    or K0=(Wp+T) O(-3)+O(-6)+O(-8).

Its internal target is V O(-6)+Wp O(-7)+O(-12). Every component vanishes: W O(-7)->V O(-6) would require W in V W=T; O(-6)->V O(-6) is zero; O(-8)->V O(-6) would require V in Sym2 W=A; the Wp channels are zero as before. Thus J=0 and F^+/F=O(18) exactly.

The profile-free rank-one quadratic gap states that for saturated quadratic F of rank r with saturated raw first derivative and F^+/F=O(b), either b=2r or b<=r-1. To recall its proof: values and the first two derivatives of quadratics span the full coefficient space, so F^{++} is constant. Its rank is r+1 or r+2 because the derivative of F^+ kills F. In the first case deg F^+=0 gives b=2r. In the second, the nonzero derivative O(b)->O(2r-b-2) gives b<=r-1. No maximal-profile or no-section endpoint hypothesis is used.

For r=11, b=18 is neither22 nor at most10. This excludes ce.

## 6. The ee source of index125 is impossible

Here

    E=3P O(-2)+2Wp O(-5)+O(-10),
    A_q=O(-10)+O(4)+O(16).

Strict-top injects the full top3P into

    H0(O(6)+O(18))=A+2V+3P+D.

The resulting map on the three-dimensional P multiplicity spaces is an isomorphism. Its projection to the single P occurrence in Sym6 W is therefore nonzero, and its kernel is a two-dimensional constant multiplicity subspace. Let F=2P O(-2) be precisely that kernel subblock. It is saturated in E, has no component to O(4), and maps injectively on global sections to H0(O(18)). Section2 applies with m=0, including basepoint-freeness and both exact kernels.

The internal target is now

    (E/F)(-2)=P O(-4)+2Wp O(-7)+O(-12).

All components vanish. For the P target, V O(-4)->P O(-4) is zero; W O(-7)->P O(-4) is zero because P Sym3 W=S+2T has no W; and the O(-6), O(-8) components are zero because P is absent from Sym2 W and Sym4 W. The Wp and negative components vanish as in Section3. Thus J=0 and the actual first span again has positive degree2, impossible.

The choice of F here is an abstract kernel construction forced by strict-top, not a choice or evaluation of actual coefficients. This completes all six edge exclusions.

## Verification and unresolved boundary

The two kernel branches, all their internal images, the zero/nonzero scalar alternatives, both P-row dependency cases, and every possible common divisor at the high-line interface have been exhausted. The attached bounded verifier checks the declared character atoms, kernels, Hom vanishings, polar characters, and exact source-list membership. It does not supply the connection and saturation arguments, which are proved above.

Other members of the complete 10/10/13 source overlists remain outside this proof, including every source without one of the six displayed exact edge identities. No current source-completion count or full-label claim follows merely from the original catalogs. In particular source2 and the O26 and low-positive lanes are untouched. An earlier exploratory approach would have analyzed the full positive-endpoint transform in the index125 ee source; it is unnecessary, because its forced two-P subblock already has a positive-degree first span. No assertion from that longer route is used.
