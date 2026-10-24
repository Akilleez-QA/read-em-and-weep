# The original degree-eighteen curve has a forced ramified seven-space projection

## Statement and exact conditional scope

Retain the full-positive triplet branch, original t=0, original local delta=12, residual simultaneous rank-seven k=2 geometry, and all complete transitive actual-geometric hypotheses of the three direct originals in Section 1. Assume the remaining original kernel is K1. Work in the original constant 21-space C and the actual constant eighteen-space S.

PR1237 gives the genuine constant splitting S=Z direct-sum C7, where dim Z=11, dim C7=7, and C7=A+P. Let X0=O(-10) and Y0=O(-18) be the ORIGINAL DUAL scalar curves. Let y7:O(-18)->C7* O be the actual constant projection of Y0. Let Zhat0 be the DISTINCT AUXILIARY PRIMAL degree-ten curve. None of these names denotes the auxiliary degree-eighteen curve.

Then:

1. The actual projected curve y7 is an everywhere saturated line with coefficient span all of C7*. Its associated scalar section system has dimension seven and degree eighteen.
2. If L5=ann_S(R13) and x2 is the second complete jet bundle of the projected ORIGINAL X0, then Q2=L5/x2 maps as an everywhere saturated rank-two subbundle of C7* O. It is exactly the saturation of the actual first-jet image of y7.
3. The actual intrinsic first-jet source W(-17) injects as a coherent image into Q2. Its cokernel is reduced of length one at each point of D12. The equivariant bundle type of Q2 is W'(-11).
4. The full Wronskian divisor of the seven-dimensional system is 7D12. Its vanishing sequence is (0,2,3,4,5,6,8) at every point of D12 and (0,1,2,3,4,5,6) elsewhere.

The missing projection-saturation step is proved by an explicit additional defect e and the Wronskian bound 6(12+e)<=84. The coherent first-jet image is never silently replaced by its saturation. No first-jet saturation is presumed to survive constant projection.

This is a necessary theorem in the retained conditional K1 case, not occurrence, a K1 exclusion, or a whole-profile conclusion. It does not classify further jet-image defects, assert a stationary subspace, or imply algebraicity. The newly determined projected first-jet divisor is not identified with the separately retained original local delta.

Only actual embedded subbundles in constant spaces are differentiated. There is no quotient connection, differentiated nonconstant inverse, or horizontal Birkhoff splitting. No selected actual coefficient, parameter, point, jet, tensor, matrix, scalar normalization, or instance rank is evaluated. All calculations below are fixed universal character, degree, orbit, and vanishing-order arguments.

## 1. Three complete direct originals and assertion provenance

The complete direct originals are:

- PR1237 at 2dfb37187cf61c59b1277a4492881c0fd42de44f, research/hm/rankfour-profile11-triplet-ten-pairing-splitting/PROOF.md, retained as inputs/ten-pairing-splitting.md.
- PR1236 at 092fc5f31dfaa5553ee5ea687f175ecba1878a2a, research/hm/rankfour-profile11-triplet-first-kernel-forward-closure/PROOF.md, retained as inputs/first-kernel-forward-closure.md.
- PR1206 at 252b967ebbfbea6fc0c6451a835ab2daff92d73b, research/hm/rankfour-profile11-triplet-shared-d/PROOF.md, retained as inputs/shared-d.md.

All three entire originals were freshly fetched through read-only connector calls at these immutable commits, without line-range limits. Their complete bytes equal the complete local originals independently read during the structural audit. INPUTS.json records exact UTF8 byte lengths, SHA256 hashes, Git blobs, and immutable source URLs. Full connector responses are retained only in LOCAL-SOURCE-FETCHES.json, outside publication and selected-only replay. All complete transitive hypotheses remain assumptions; an excerpt does not replace an entire original.

The complete PR1237 proof supplies the actual constant splitting S=Z direct-sum C7, C7=A+P, the perfect Delta^10 pairing, completeness of projected original X0, the actual containment Zhat7 subset R15, and the exact terminal annihilator R17=ann_S(x0). The complete PR1236 proof supplies the actual forward relation R13^+=R15, R15^+=R17, their ranks and degrees, and R15 subset ann_C(X0+Y0). The complete PR1206 proof supplies dim span(X0)=11, dim span(Y0)=15, and their joint coefficient span equal to C*. Its U,T,C10,C18 are respectively our X0,Y0 and their original coefficient spaces. Original degree-ten completeness is prior work, not a novelty claim.

No additional actual-geometric source is needed: all these assertions are explicit in the three complete originals. The universal orbit argument is derived in Section 2. The fixed character identities are recorded in Section 10 and checked from the physical representation ring; they require no actual coefficient-system input.

## 2. Actual notation and the universal orbit facts

All bundles are on the physical line P(W*) over C, with G=SL2(F5), det W=1. Let A=Sym2 W, D=Sym4 W, P the even four-dimensional irreducible, and W' the alternate doublet. G has no nontrivial one-dimensional characters. The projective action is A5. A finite subgroup of PGL2 fixing a point is cyclic: after moving that point to infinity it consists of affine maps, averaging an orbit gives a common finite fixed point, and conjugation to the two fixed points identifies the group with a finite subgroup of C*. The element orders in A5 are 1,2,3,5, as follows from the even cycle types on five letters. Thus projective stabilizer orders are among 1,2,3,5 and orbit sizes are among 60,30,20,12. In particular every nonempty invariant effective divisor has degree at least 12.

The fixed character Sym12 W=1+A+D+P gives a one-dimensional invariant space in degree 12. A nonzero invariant section f12 has an invariant zero divisor of degree 12, so that divisor is one reduced orbit. Conversely the section of any invariant divisor of degree 12 is semi-invariant; G has no nontrivial characters, so it belongs to that same line. Thus there is a unique invariant effective divisor of degree 12, denoted D12. Neither a scalar normalization of f12 nor any orbit point is selected.

The original dual curves are X0=O(-10) and Y0=O(-18) in C* O. Their coefficient spaces have dimensions 11 and 15 and jointly span the original C* of dimension 21. The auxiliary primal degree-ten curve is denoted Zhat0, never X0 or Y0.

The complete PR1237 original supplies an actual constant splitting S=Z direct-sum C7, with dim Z=11, C7=A+P, and C7 annihilating the entire original X0 coefficient space. Thus S*=Z* direct-sum C7*. The original projected degree-ten curve x0 is complete in Z*, and its actual saturated complete jets are

    x_j=Sym^j W(j-10), 0<=j<=10.

Here completeness gives actual constant coefficient-space isomorphisms, so these are the intrinsic jets of the complete degree-ten system. In more detail, the full system H0(O(10)) separates j-jets for j<=10: the evaluation exact sequence at a variable length-(j+1) point has obstruction H1(O(9-j))=0. Thus its jet-evaluation map is everywhere onto, and dualizing gives an everywhere saturated inclusion. The universal principal-parts identity is P^j(O(10))*=Sym^j W(j-10), with successive quotient O(2j-10). Consequently x1=W(-9), x2=A(-8), and x2/x1=O(-6). This uses proved completeness of the projected original X0, not an assumption about projected Y0.

The determinant pairing identifies ann_Z*(Zhat7)=x2 as an actual subbundle. Indeed the mixed biform is a nonzero multiple of Delta^10, so its mixed derivatives of total order at most nine vanish on the diagonal. This says that the actual first two jets of x0 annihilate Zhat7. The resulting inclusion has equal ranks three on both sides; both subbundles are saturated in Z* O, so it is equality. No particular point, jet, or scalar is selected.

The retained forward flag gives R13^+=R15, R15^+=R17, ranks 13,15,17 and degrees -46,-36,-10. Also R15 lies in ann_C(X0+Y0), R17=ann_S(x0), and Zhat7 lies in R15.

Write y for the actual constant projection of Y0 into S*, y_Z for its Z* component, and y7 for its C7* component. Until basepoint-freeness is proved, these denote morphisms from O(-18), not presumed saturated line subbundles. Put L3=ann_S(R15) and L5=ann_S(R13), of ranks 3,5 and degrees -36,-46.

## 3. The projected coefficient span and the actual rank-three identity

Restriction C* -> C7* is surjective and kills the full coefficient space of X0. Since the coefficient spaces of X0 and Y0 jointly span C*, the coefficient space of y7 is all of C7*. In particular y7 is nonzero, and its scalar component sections define a seven-dimensional linear system in H0(O(18)). No completeness of the original degree-eighteen system is asserted.

The actual x1 lies in L3. Indeed R15 is annihilated by x0 and its derivatives lie in R17, also annihilated by x0. Differentiation of the constant pairing shows that first derivatives of x0 annihilate R15. The saturated first-jet bundle x1 is therefore contained in L3. The original containment R15 subset ann_C(Y0) also puts y in L3.

Since x1 is entirely in Z* and y7 is nonzero, the morphism

    x1 direct-sum O(-18) -> L3

has generic rank three. Its source and target both have degree -36. Its determinant is consequently a nonzero section of O, so the map is an everywhere isomorphism. Therefore

    L3=x1 direct-sum y

as actual embedded bundles. This proves the saturation and directness of y in S*. It does not assume that a projected curve remains unramified or saturated.

## 4. The projected seven-space line is basepoint-free

Because Zhat7 lies in R15 and Y0 annihilates R15, the actual morphism y_Z factors through x2=ann_Z*(Zhat7).

It is not identically zero: otherwise the 15-dimensional coefficient space of original Y0 would annihilate the 11-dimensional Z in the 21-dimensional C, forcing it into an annihilator of dimension 10.

The composite y_Z -> x2/x1=O(-6) is nonzero. If it vanished, y_Z would factor through x1, but

    Hom_G(O(-18),W(-9))
      = (W tensor Sym9 W)^G = 0,
    Sym9 W=S4+T6.

The composite is therefore a nonzero invariant section of O(12), hence a nonzero multiple of f12. In particular the fiber y_Z belongs to x1 at every point of D12.

At any point of D12, vanishing of y7 would put the full fiber y in x1. This contradicts the everywhere direct sum L3=x1 direct-sum y. Thus y7 does not vanish at any point of D12.

Its common-zero divisor, if nonempty, is G-invariant and has degree at most 18. The orbit sizes 12,20,30,60 imply that the only possible such divisor is a single reduced orbit of length 12. The invariant line H0(O(12))^G is one-dimensional, so that orbit is precisely D12. This possibility was excluded above. Consequently

    y7:O(-18) -> C7* O

is an everywhere saturated line inclusion. In this part the orbit-size statement, or an equivalent invariant-section calculation up to degree 18, is necessary; the minimum-orbit-size statement alone would not identify the possible divisor.

## 5. The rank-five inclusion and the exact generic projection kernel

Differentiation of the constant pairing gives x2 subset L5: x1 annihilates R15, and derivatives of R13 lie in R15. Likewise the actual first-jet morphism of y factors through L5, since y annihilates R15. Its intrinsic source is

    J1=P^1(O(18))*=W(-17).

The projection of this first-jet morphism to C7* is exactly the first-jet morphism of y7, because the projection is an actual constant linear map. Its generic rank is two: a characteristic-zero curve whose coefficient span has dimension seven is nonconstant, so its value and first derivative are generically independent.

It follows that

    x2 direct-sum J1 -> L5

has generic rank five, and hence is a sheaf injection. Its determinant is nonzero and has degree

    -46 - (3*(-8)+2*(-17)) = 12.

All the maps are equivariant and scalar determinant twists give no character, so its divisor is D12.

Since x2 is saturated in the full constant ambient S*, it is also saturated in L5. Thus

    Q2=L5/x2

is a vector bundle of rank two and degree -22. The induced map

    q:Q2 -> C7* O

has generic rank two by the preceding first-jet argument. Its sheaf kernel is zero because Q2 is locally free and a generically zero kernel would be torsion. Equivalently, L5 intersect (Z* O)=x2 as sheaves. This intersection is saturated in L5.

This proves only that q is a sheaf injection at this stage. It does not yet prove that q has rank two on every fiber or that its image is saturated in C7* O. Those stronger claims are established in Section 7 below.

## 6. The first-jet defect inside Q2 is exactly the reduced D12

The image of y in Q2 maps under q to the already proved basepoint-free y7. Therefore O(-18) -> Q2 is itself an everywhere saturated line inclusion. Indeed divisibility by a local parameter in Q2 would imply the same divisibility after mapping into C7* O. Its quotient is a line bundle of degree -4, with the unique equivariant linearization:

    0 -> O(-18) -> Q2 -> O(-4) -> 0.

The map J1 -> Q2 has generic rank two and determinant degree

    -22 - (-34)=12.

It is equivariant, so the determinant divisor is D12. The intrinsic value line O(-18) is saturated in J1 and maps onto the saturated value line in Q2. In local frames adapted to this line, one invariant factor is therefore a unit. The other invariant factor has the simple zeros of f12. Hence the cokernel of J1 -> Q2 has length one at every point of D12 and zero elsewhere.

This is a statement about the actual coherent first-jet image inside Q2. It is not yet a claim that Q2 is its saturation in C7* O.

## 7. The Wronskian budget proves the missing projected saturation

Let E2 be the saturation of q(Q2) in C7* O and let

    e=length(E2/q(Q2)) >= 0.

The associated effective divisor is G-invariant. Since J1 injects into Q2 and its defect there is D12, additivity of lengths gives

    length(E2/im(J1))=12+e.

For completeness, the precise local ramification interpretation is as follows. At an arbitrary point p, let

    0=a0<a1<...<a6

be the vanishing sequence of the seven-dimensional scalar linear system defined by y7. Basepoint-freeness gives a0=0. In a local trivialization with a unit value component, subtracting its multiples reduces the first-jet minors to derivatives of the normalized remaining components. In characteristic zero, their minimum vanishing order is a1-1. Thus the local length of E2/im(J1) is exactly a1-1. This is a universal local lemma applied at every point, not a selected evaluation of an actual point or jet.

The seven independent sections have a nonzero full Wronskian in characteristic zero. One way to see nonvanishing without any actual coefficient calculation is to use the vanishing filtration of an arbitrary linearly independent system: a local adapted basis has distinct leading orders, and the universal determinant of their falling-factorial derivative coefficients is a nonzero Vandermonde determinant. This establishes the usual generic-rank theorem structurally.

The Wronskian is the determinant of the evaluation map to P^6(O(18)). The principal-parts filtration has graded lines O(18),O(16),...,O(6), so

    det P^6(O(18))=O(84),
    84=7*(18-6).

The constant source determinant is the determinant representation of C7, which is trivial because G has no nontrivial scalar characters. Equivalently, the determinant section has invariant zero divisor directly from the equivariant evaluation map. Thus its divisor is G-invariant. Its local weight is

    w(p)=sum_(i=0)^6 (a_i-i).

For i>=1, strict increase gives a_i>=a1+i-1. Hence

    w(p)>=6*(a1-1).

Summing over all points gives

    84 >= 6*(12+e),
    e <= 2.

If e were positive, its invariant effective divisor would have degree at least 12. Therefore e=0. The map q is consequently an everywhere saturated rank-two inclusion. In particular Q2 is the actual saturated first-jet bundle of the projected y7 in the constant seven-space, and its actual first-jet ramification divisor is exactly reduced D12.

This proves the projected-saturation bridge. The coherent image was not replaced by its saturation anywhere before the defect e was proved to vanish.

## 8. The equivariant bundle type is W'(-11)

The extension in Section 6 has equivariant extension space

    Ext^1_G(O(-4),O(-18))
      = H1(O(-14))^G
      = (Sym12 W)^G = C,
    Sym12 W=1+A+D+P.

Here taking invariants is exact in characteristic zero, and Serre duality gives the displayed invariant dimension; self-duality is used only to write the representation compactly.

The extension cannot split equivariantly. A split O(-4) summand would map to C7* O under the injection q, but

    Hom_G(O(-4),(A+P)O)
      = ((A+P) tensor Sym4 W)^G = 0,
    Sym4 W=D.

Thus that whole summand would be killed, a contradiction. An ordinarily split equivariant extension would admit an equivariant splitting by averaging, so this also excludes that alternative.

A model of the nonzero invariant extension is supplied without choosing any actual map. The universal identity

    Sym7 W=W'+T6

gives a one-dimensional nonzero Hom_G(O(-18),W'(-11)). Any nonzero member has common-zero divisor of degree at most 7. That divisor is invariant, so it is empty. Its quotient is O(-4), giving

    0 -> O(-18) -> W'(-11) -> O(-4) -> 0.

This extension is nontrivial: its middle bundle has ordinary splitting O(-11) direct-sum O(-11), not O(-18) direct-sum O(-4). Since the invariant extension space is one-dimensional, all its nonzero classes have isomorphic equivariant middle bundle after rescaling an endpoint. Therefore the actual Q2 has type

    Q2 isomorphic to W'(-11).

This is an equivariant bundle-type conclusion. It does not specify an actual embedding, coefficient, scalar, or normalization, and does not make any Birkhoff splitting horizontal.

## 9. The full Wronskian and exact vanishing sequences

At D12 the first-jet defect is one, so a1=2. The weight bound gives at least six units of full Wronskian weight there. Therefore the full Wronskian divisor contains 6D12, of degree 72. Its residual divisor is effective, G-invariant, and has degree 12. The unique such divisor is D12. Hence

    div(Wr)=7D12.

Every point of D12 has weight exactly 7. With a0=0, a1=2 and strict increase, the minimal sequence is (0,2,3,4,5,6,7), of weight 6. A total excess of one can be placed only in the final entry, since increasing any earlier entry would force a later increase as well. Thus the unique sequence is

    (0,2,3,4,5,6,8) at every point of D12.

Outside D12 the weight is zero, so the sequence is

    (0,1,2,3,4,5,6).

These are global orbit-uniform conclusions. No point was selected or evaluated.

## 10. Fixed universal identities, contribution, and verification boundary

The required character identities are

    Sym4 W=D,
    Sym7 W=W'+T6,
    Sym9 W=S4+T6,
    Sym12 W=1+A+D+P.

They follow from the fixed physical W-tensor ring by the recurrence Sym^(n+1) W = W tensor Sym^n W - Sym^(n-1) W. Its adjacency data are

    W tensor 1=W,
    W tensor W=1+A,
    W tensor A=W+S4,
    W tensor S4=A+D,
    W tensor D=S4+T6,
    W tensor T6=D+V_alt+P,
    W tensor V_alt=T6,
    W tensor P=T6+W',
    W tensor W'=P.

These are fixed universal characters, not a tensor chosen from the actual geometry. The checker runs this recurrence only through degree twelve. The only other checks are complete-file authentication, fixed orbit-size arithmetic, and the displayed rank, degree, Wronskian, and vanishing-sequence arithmetic. Checks are explicit runtime requirements, so normal Python and optimized Python perform the same tests.

The new result concerns the original Y0 after projection to the canonical constant seven-space: basepoint-freeness, its exact saturated first-jet bundle, its reduced first-jet ramification divisor, and its full Wronskian and vanishing sequences. The saturation bridge in Section 7 is essential. Its invariant additional defect is proved zero; it is not omitted or assumed away.

The theorem retains the full conditional scope stated above. It does not show occurrence, exclude K1, classify further coherent jet-image defects, assert a stationary P-subspace, settle other original local defects, or prove algebraicity. Only actual embedded constant-ambient maps were differentiated.

The bounded checker cannot certify actual-map containment, basepoint exclusion, the generic projection-kernel argument, the local ramification interpretation, the Wronskian saturation bound, or source sufficiency. An independent review of the entire frozen proof and all three complete immutable direct originals remains required before publication. The earlier separate structural audit is not substituted for that fresh entire-proof review.
