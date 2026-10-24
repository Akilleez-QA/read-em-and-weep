# The first-kernel forward flag closes with a forced reduced degree-twelve defect

## Statement and exact conditional scope

Retain the full-positive triplet branch, original t=0, local delta=12, residual simultaneous rank-seven k=2 geometry, and all complete transitive actual-geometric hypotheses of the three direct originals in Section 1. Assume the remaining original kernel is K1. Let Bhat be the actual lifted common top, let R=Bhat^+, and let S be their actual constant eighteen-dimensional span in the original constant space C.

The actual saturated forward flag is

    Bhat -> R -> R13 -> R15 -> R17 -> S O,
    ranks: 9, 11, 13, 15, 17, 18,
    degrees: -54, -52, -46, -36, -10, 0.

Each arrow is an actual forward transform in the original constant ambient. The first three coherent images are saturated W(-1), W(1), and W(3). At R15, the coherent image is W(5), but its saturation is O(6)+O(16). The saturation quotient has length twelve, supported with length one at each point of the reduced invariant divisor D12. Thus the R15 derivative has rank two, not rank one. Finally R17 is exactly the annihilator in S O of the projected original degree-ten dual scalar curve, and its derivative is everywhere onto O(8).

This excludes the rank-one third-forward possibility and determines the entire finite forward closure of Bhat. It does not exclude or realize K1 or the retained conditional branch. No auxiliary coefficient-span shortcut, new original degree-eighteen higher jet, or algebraicity assertion is made.

Only actual embedded subbundles are differentiated. No quotient connection, differentiated inverse, or horizontal source splitting is used. No selected actual coefficient, parameter, point, jet, tensor, matrix, scalar normalization, or instance rank is evaluated.

## 1. Complete direct originals and retained actual data

The three direct originals are:

- PR1235 at 7152e94cedbab18036b5e032d4e97934c4c061b7, research/hm/rankfour-profile11-triplet-first-kernel-span/PROOF.md, retained as inputs/first-kernel-span.md.
- PR1234 at 3d55622ece9a4bb9e20197dec560b298f1d03fb1, research/hm/rankfour-profile11-triplet-simultaneous-kernel-three-exclusion/PROOF.md, retained as inputs/kernel-three-exclusion.md.
- PR1205 at 97dad5c307a04f61d850e8a4211559e97ed4c2fd, research/hm/rankfour-profile11-triplet-positive-span/PROOF.md, retained as inputs/positive-span.md.

All three entire originals were freshly fetched by read-only connector calls at the stated immutable commits. INPUTS.json records their paths, complete UTF8 lengths, SHA256 hashes, and Git blobs. The full responses are retained in LOCAL-SOURCE-FETCHES.json, excluded from publication and selected-only replay. Complete transitive hypotheses remain assumptions; no excerpt replaces an entire original.

Work over C on the physical binary-icosahedral line P(W*) with G=SL2(F5), det W=1, and the retained determinant convention. Set A=Sym2 W, S4=Sym3 W, D=Sym4 W, and T6=Sym5 W. The alternate triple is V_alt and the alternate doublet is W'. There are no nontrivial scalar characters. Every nonempty invariant effective divisor has degree at least twelve. The fixed projective A5 action has an orbit of length twelve. Its divisor gives an invariant degree-twelve section because G has no nontrivial scalar characters. The universal character Sym12 W=1+A+D+P shows that the invariant line is one-dimensional. Denote a generator only up to nonzero scalar by f12. Every invariant effective divisor of degree twelve is reduced: every nonempty invariant orbit has at least twelve points. Thus div(f12)=D12 is one reduced orbit of length twelve. These are universal facts about the fixed action, not selected actual data or assumptions about the new derivative defect.

The first two originals supply the actual data

    dim C=21, dim S=18, C/S=V_alt,
    Bhat=(D+P)(-6) subset K^-,
    beta_Bhat has saturated coherent image W(-1),
    R=Bhat^+ subset K, R/Bhat=W(1),
    rank R=11, deg R=-52,
    Q=K/R=W'(-3),
    rank K=13, deg K=-58, rank K^-=10, deg K^-=-64,
    span_C(Bhat)=span_C(R)=S.

The third original supplies

    E0=D(-2)+(W'+T6)(-3)+V_alt(-4),
    rank E0=16, deg E0=-46, span_C(E0)=C,
    K=E0^-, K^+=E0, E0/K=A(4),
    beta_K:K -> A(2) everywhere onto,
    beta_E0 has everywhere coherent image A(4).

In the original dual constant ambient C* O it supplies

    S0=ann(E0), L0=S0^-=X0+Y0,
    X0=O(-10), Y0=O(-18),
    S0/L0=A(-6),
    beta_L0:L0 -> A(-8) is everywhere injective and saturated.

Here X0 is the original dual degree-ten curve and Y0 is the original dual degree-eighteen curve; neither denotes an auxiliary curve. The coefficient span of X0 contains its A coefficient component. Its intrinsic first-jet source is W(-9), by the universal principal-parts identity retained in PR1205. We shall prove the required properties after projection to S*, rather than transfer unramifiedness to that projection.

All annihilators below use the actual constant pairing. A superscript plus denotes saturated forward span; a minus denotes the actual derivative kernel. Omega=O(-2).

## 2. The original rank-nineteen forward span and its full derivative

Set E19=E0^+. The retained actual transpose S0/L0=A(-6) maps isomorphically to (E0/K)* tensor Omega=A(-6). Dualizing that actual isomorphism shows that the coherent image A(4) of beta_E0 is saturated in its full normal bundle. It gives

    E19/E0=A(6), rank E19=19, deg E19=-28.          (1)

The annihilator-transpose identity gives

    E19=ann(S0^-)=ann(L0).

For completeness, a local section of S0 annihilates E0 and its first derivatives precisely when its own derivatives still annihilate E0. This identifies the annihilator of the generic forward span with S0^-. Both sides are saturated, giving the stated equality.

Since beta_L0 is an everywhere injective saturated map to A(-8), its negative transpose is everywhere onto L0* tensor Omega. Thus the actual derivative of E19 satisfies

    beta_E19:E19 -> (C O/E19)(-2)=O(8)+O(16)
    is everywhere onto.                            (2)

In particular E19^- has rank seventeen. Also E0 lies in E19^-, because derivatives of E0 lie in E19. No general theorem with central rank seventeen is applied here.

## 3. Two saturated Euler graphs give R13 and R15

Because Bhat^+=R, beta_R kills Bhat. Because R lies in K=E0^-, its derivatives lie in E0. It therefore factors through an actual morphism

    a1:R/Bhat=W(1) -> (E0/R)(-2).

Projection to (E0/K)(-2)=A(2) is beta_K|R. It is nonzero: otherwise R would lie in K^-, whose rank is ten, whereas R has rank eleven. The universal Hom space is one-dimensional, and its nonzero member is the saturated Euler inclusion

    0 -> W(1) -> A(2) -> O(4) -> 0.                (3)

Consequently a1 is an injective saturated graph. More explicitly, the normal target surjects to A(2) with kernel Q(-2), and the quotient by this graph is an extension of O(4) by Q(-2), hence locally free. Thus

    R13:=R^+,
    R13/R=W(3), rank R13=13, deg R13=-46,
    R13 subset E0, R13 intersect K=R.               (4)

The intersection is fiberwise: the projection of the added quotient to E0/K is the saturated inclusion W(3) in A(4).

Likewise beta_R13 kills R and factors through

    a2:R13/R=W(3) -> (E19/R13)(-2).

Its projection to (E19/E0)(-2)=A(4) cannot vanish. Otherwise R13 would lie in ker beta_E0=K, contradicting its intersection R with K in (4). The corresponding universal Hom space is again one-dimensional, generated by

    0 -> W(3) -> A(4) -> O(6) -> 0.                (5)

The same graph argument, now with kernel (E0/R13)(-2), proves full saturation. Hence

    R15:=R13^+,
    R15/R13=W(5), rank R15=15, deg R15=-36,
    R15 subset E19, R15 intersect E0=R13.           (6)

All these bundles lie in S O: a constant space containing an actual subbundle contains all its derivatives and its saturated forward span.

## 4. The missing constant triple determines the internal normal bundle

Let pi:C->C/S=V_alt be the actual constant projection. Since pi kills R, its restriction to K factors through

    q:Q=W'(-3) -> V_alt O.                         (7)

This map has full constant coefficient span V_alt, because K has constant span C. It has generic rank two. Indeed, a generic rank-one image would saturate to an equivariant scalar line O(a) with a<=0. The center forces a even. The resulting nonzero map W'(-3)->O(a) would require W' in Sym^(a+3) W, where 0<=a+3<=3. None of these characters contains W'.

The rank-two minors of (7) have degree six. Their common divisor is invariant and has degree at most six, so is empty. Thus q is an everywhere saturated rank-two inclusion, and

    0 -> Q=W'(-3) -> V_alt O -> O(6) -> 0.         (8)

Here Q has become an actual subbundle of a constant ambient. Its own derivative is nonzero, since a horizontal saturated bundle in a constant ambient is constant in characteristic zero and has degree zero, whereas deg Q=-6. It maps to O(4). Its entries have degree seven, so the same invariant-divisor argument makes that nonzero map everywhere onto.

The constant projection pi commutes with derivatives of sections of K. Local sections of Q lift locally to K, whose derivatives lie in E0. Thus pi(E0) contains Q and surjects onto the normal line V_alt O/Q=O(6), because the derivative of Q is onto O(4). Therefore

    pi:E0 -> V_alt O is everywhere onto.

Its kernel has rank thirteen and degree -46 and contains R13. Both are saturated, so equality of rank and degree gives

    E0 intersect S O=R13.                          (9)

Since E0 lies in E19, pi:E19->V_alt O is also onto. Its kernel has rank sixteen and degree -28. After quotienting by R15, which lies in that kernel, we obtain

    0 -> O(8) -> E19/R15 -> V_alt O -> 0.          (10)

The extension splits ordinarily, since H1(O(8))=0, and hence equivariantly. Therefore

    E19/R15=O(8)+V_alt O.                          (11)

The O(8) in (10) is actual and canonical; the abstract splitting in (11) is used only for Hom calculations. It is not made horizontal.

## 5. The projected third row is the universal gradient and is everywhere onto

Because R13^+=R15, beta_R15 kills R13 and factors through

    b:W(5)=R15/R13 -> (C O/R15)(-2).               (12)

Project (12) to the actual normal quotient of E19 from (2). Its O(8) row is zero, because

    Hom_G(W(5),O(8))=Hom_G(W,Sym3 W)=0.

Its O(16) row is nonzero. Otherwise R15 would lie in E19^-. The latter has rank seventeen and contains E0, which projects onto V_alt O by (9). Hence E19^- intersect S O has rank fourteen, and cannot contain rank-fifteen R15.

The universal character identity

    Sym11 W=W+S4+T6

gives dim Hom_G(W(5),O(16))=1. The gradient, or first polarization, of the universal degree-twelve invariant f12 supplies a nonzero generator of that space. It is used only to identify a universal Hom generator, not to assign an actual scalar normalization to the row.

The two gradient entries have no common zero. If both vanished at a point, Euler's degree-twelve identity would give f12=0 there, while vanishing of the tangent derivative would make that root multiple. This contradicts the reduced divisor D12. Thus every nonzero map in this one-dimensional Hom space is everywhere onto. Denote the actual row by v. Then

    0 -> O(-6) -> W(5) --v--> O(16) -> 0.         (13)

The kernel degree is 10-16=-6. This argument does not infer negativity from any quotient of a negative bundle.

## 6. The only possible internal row is a multiple of f12

Restrict b in (12) to the actual kernel O(-6) of (13). It lands in the internal normal bundle (E19/R15)(-2), which by (11) is O(6)+V_alt(-2). Its V_alt(-2) component vanishes, since

    Hom_G(O(-6),V_alt(-2))
      =(V_alt tensor Sym4 W)^G=0.

Consequently the internal row is exactly a scalar multiple, possibly zero, of

    f12:O(-6) -> O(6).                            (14)

The next section excludes the zero possibility using actual annihilators. It does not simply identify the projected rank-one image with the full derivative image.

## 7. The rank-one possibility contradicts an actual degree-ten annihilator

Suppose (14) is zero. Then b factors through O(16), and the resulting map to the full normal bundle is an injective saturated graph over the O(16) summand of (2). The actual forward span would be a bundle N with

    N=R15^+, N/R15=O(18), rank N=16, deg N=-18.
                                                               (15)

Let x0:X0=O(-10)->S* O be the actual constant projection of the original dual scalar curve X0. It is nonzero and retains the original A coefficient component: the kernel C*->S* is the alternate triple V_alt, not A. Its common-zero divisor would be invariant of degree at most ten, hence empty. Thus x0 is an everywhere saturated line inclusion. Put

    A17=ann_S(x0(X0)), rank A17=17, deg A17=-10.

The vanished O(8) row in Section 5 means that derivatives of R15 still annihilate X0. Consequently N lies in A17. The actual beta_A17 kills R15, because their derivatives lie in N subset A17. Its restriction to N therefore factors through

    N/R15=O(18) -> (S O/A17)(-2)=O(8),

and is zero by ordinary degree. Hence derivatives of N lie in A17.

Differentiate the actual constant pairing. Since X0 annihilates N and the derivatives of N, its first jets annihilate N. Let

    eta1:W(-9)=P^1(O(10))* -> S* O

be the intrinsic first-jet map of the projected curve x0. Its generic rank is two: the retained A coefficient span has dimension at least three, so this curve is nonconstant, and a nonconstant characteristic-zero curve has generic first-jet rank two. It factors through ann_S(N), which has rank two and degree -18. Source and target have equal rank and degree, so the determinant is a nonzero constant. Thus

    eta1 identifies X1=W(-9) with ann_S(N),
    0 -> X0 -> X1 -> O(-8) -> 0.                    (16)

This proves saturation after projection; it does not assume it.

Because X1 consists of actual first jets, beta_X1 kills X0. Transposing this actual factorization shows that beta_N lands in

    (X1/X0)* tensor Omega=O(6)

inside its full normal target. On the other hand, N=R15^+ means beta_N kills R15, so it factors through O(18) in (15). The morphism O(18)->O(6) is zero. Therefore beta_N=0. A saturated horizontal subbundle of a constant bundle is constant in characteristic zero and has degree zero, contradicting deg N=-18.

This excludes the rank-one possibility. Notice that no saturation of beta_X1 was needed, and no inference about the top degree of a quotient was used.

## 8. Exact coherent image, saturation, and reduced cyclic defect

The internal row (14) is therefore nonzero. Since v is onto, b has generic rank two and has zero sheaf kernel. Its actual coherent image is consequently isomorphic to W(5).

Let Ibar be its saturation in the full actual normal bundle. The kernel of its projection to O(16) is the saturated O(6) from (10). Indeed, the row on ker v is nonzero f12 times that line. Modulo O(6), the image of b factors through O(16) and projects isomorphically to the indicated O(16), so is a saturated graph. Thus

    0 -> O(6) -> Ibar -> O(16) -> 0.               (17)

The equivariant extension group vanishes:

    Ext^1_G(O(16),O(6))=H1(O(-10))^G
      =(Sym8 W)^G=0,
    Sym8 W=P+D.

Hence

    im beta_R15=W(5), Ibar=O(6)+O(16).             (18)

The determinant of W(5)->Ibar is a nonzero invariant section of degree

    deg Ibar-deg W(5)=22-10=12.

It is therefore a nonzero multiple of f12. Because v is onto, one local invariant factor is a unit everywhere. The other has the simple zeros of f12. Consequently Ibar/im beta_R15 is supported precisely on D12, with length one at each of its twelve points. This is the reduced cyclic local defect, not merely a total-degree count. The argument uses no evaluation at a selected point or of an actual matrix.

## 9. The rank-seventeen span is exact and its next span is S

From (18), the actual saturated forward span R17=R15^+ satisfies

    R17/R15=Ibar(2)=O(8)+O(18),
    rank R17=17, deg R17=-36+26=-10.               (19)

The same vanished O(8) projected row used in Section 7 puts R17 inside A17=ann_S(x0(X0)). Both have rank seventeen and degree -10, and both are saturated in S O. Therefore

    R17=ann_S(x0(X0)).                               (20)

Its actual derivative targets (S O/R17)(-2)=O(8). It kills R15, since R15^+=R17. Hence it factors through the quotient in (19). The O(18) row is zero by degree. The O(8) row is a scalar, and must be nonzero: otherwise R17 would be horizontal, contradicting deg R17=-10. It is therefore everywhere onto, proving

    beta_R17 has full coherent image O(8),
    R17^+=S O.                                    (21)

The forward chain now reaches the actual constant span, rather than merely a bundle of the same abstract rank.

## 10. Contribution and limits

The new obstruction is the rank-one exclusion in Section 7. Keeping the internal normal row then forces the rank-two coherent image W(5), its split saturation O(6)+O(16), and its reduced degree-twelve defect. Together with the two preceding saturated Euler graphs, this determines the exact finite forward flag through ranks 9,11,13,15,17,18 and degrees -54,-52,-46,-36,-10,0.

No K1 contradiction or realization is claimed. Original t=0 and the retained local delta=12 are unchanged; the newly described defect is the separately identified derivative saturation defect at R15. No new original degree-eighteen jet, auxiliary span transfer, whole-profile exclusion, or algebraicity assertion is made. Other coherent-image branches, other local defects, and the remaining original geometric compatibility remain separate.

The three direct originals are freshly authenticated and the complete proof is frozen for independent review. A complete independent actual-map review is required before publication. The permitted bounded checks are the displayed universal characters, Hom and Ext vanishings, ranks, degrees, and invariant-divisor orders; they cannot replace that review.
