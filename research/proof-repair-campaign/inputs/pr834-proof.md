# The V+P+D quadratic top block is impossible in the O(26) branches

## Result and scope

The source types

    E3  = (V+P+D) O(-2)+V O(-4)+O(-8)+O(-10),
    E12 = (V+P+D) O(-2)+V O(-4)+W O(-9)

cannot occur in the retained zero-original-defect positive-O(26) profile-(1,1) branches. This removes the E3 entries for G3.11.dc58cc54f352 and G3.11.4b6dad66f329, and the E12 entry for G3.11.4b6dad66f329.

The proof uses a complete small exact-kernel support and its actual internal derivative map. Each nonzero internal-image alternative forces the same constant eight-space A+D. The D top summand cannot remain in that constant part. Every possible additional linear channel then forces a full linear block into a projected first span that contains no constants.

This is a source-branch exclusion only. Neither full label, source2, nor the global rank problem is claimed excluded. No selected actual HM/source coefficients, parameters, points, derivative values, matrices, source-instance ranks, selected models, scans, or large computations are used. The accompanying verifier checks bounded universal character identities, not an all-twist envelope.

## 1. Immutable public inputs

All paths below are in Akilleez-QA/read-em-and-weep.

The original data are pinned at

    db51525015bb7c5e825833d550d08dedf6f6ea96,
    research/hm/order-four-quadratic-load/.

The exact files used are ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md, ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md, one-one-endpoint-necessary-pairs.json, and rank-three-quotient-frontier-144.json.

The two labels have source indices112 and115, with respectively

    A_q=O(-10)+O(-8)+O(26), B_q=O(-28)+O(6)+O(8),
    A_q=W O(-9)+O(26), B_q=O(-28)+W O(7).

Index112 contains the E3 source tuple (0,0,1,0,0,1,0,1). Index115 contains that tuple and the E12 tuple (0,0,1,0,0,0,1,0).

The complete exact source overlists and common-divisor reduction are

    PR813, 3f99ecf539a3a3da61743df0dff409e54270c865,
    research/hm/profile11-o26-divisor-reduction/PROOF.md.

The actual derivative-image sequence is

    PR796, d2b43060c83328dd5118aee6b9288fcfa0c873ac,
    research/hm/profile12-quadratic-block-exclusion/PROOF.md,

Section3. The first-polar generation and actual constant-quotient principle are

    PR799, 2172e4a7abbbe232f9f448bea6fa01dee7927460,
    research/hm/profile11-quadratic-polar-obstruction/PROOF.md.

No interior-stage vanishing is used. Each path is at https://github.com/Akilleez-QA/read-em-and-weep/blob/COMMIT/PATH for the displayed immutable COMMIT and PATH.

Work over C with the binary icosahedral group G and notation W,Wp,A,V,P,S,D,T. Thus A=Sym2 W, S=Sym3 W, D=Sym4 W and T=Sym5 W. All irreducibles are self-dual. The actual E is saturated in H O, satisfies H0(E(1))=H0(E^-(2))=0, and has the actual quotient A_q. Original defect zero gives a saturated derivative image A_q in Q(-2), Q=(H O)/E, and E^+/E=A_q(2).

## 2. Complete exact top-kernel support

The canonical top block F=(V+P+D) O(-2) maps only to the positive O(26) part of A_q. The strict-top vanishing injects its coefficient representation into Sym28 W. By PR813 its common divisor has degree0,12,or20, every degree12 alternative is excluded, and degree20 requires the different coefficient P+D. Thus the map p:F->O(26) is everywhere onto.

Let K0=ker p. Then

    0 -> K0(2) -> (V+P+D) O -> O(28) -> 0,
    rank K0=11, deg K0=-50,
    H0(K0(2))=0,
    H1(K0(2))=A+P+2D,
    chi_G(K0(3))=-W-S.                               (1)

Every splitting degree of K0 is at most-3. Write U_j for U O(-j). An atom U_j with j>=4 consumes U tensor Sym^(j-4) W from the H1 budget in (1). The bound (j-3) dim U<=17, central parity and componentwise positivity leave exactly

    A_4,P_4,D_4,Wp_5,S_5,1_6,V_6,W_7,1_8,Wp_9,1_12. (2)

Their respective budgets are

    A,P,D,P,A+D,A,P+D,A+D,D,A+P+D,P+D,

and their next-twist H1 tails are

    0,0,0,Wp,S,W,T,W+S,S,S+T,Wp+T.

The required W in the tail forces exactly one of 1_6 or W_7. Both exhaust the sole A budget, excluding every other A-consuming atom. If W_7 is chosen, the residual P+D can be filled in exactly six ways:

    P_4+D_4, Wp_5+D_4, P_4+1_8,
    Wp_5+1_8, V_6, 1_12.

If 1_6 is chosen, the residual P+2D must supply S; the only remaining source of S is 1_8, so it occurs at least once. The remaining P+D gives exactly the same six choices. This proves the complete twelve-element list:

    P_4+D_4+W_7;
    Wp_3+Wp_5+D_4+W_7;
    S_3+P_4+1_8+W_7;
    (Wp+S)_3+Wp_5+1_8+W_7;
    T_3+V_6+W_7;
    (Wp+T)_3+1_12+W_7;
    P_4+D_4+1_6+1_8;
    Wp_3+Wp_5+D_4+1_6+1_8;
    S_3+P_4+1_6+2·1_8;
    (Wp+S)_3+Wp_5+1_6+2·1_8;
    T_3+V_6+1_6+1_8;
    (Wp+T)_3+1_12+1_6+1_8.                           (3)

The degree-3 coefficients are forced by the second Euler identity of (1). The accompanying bounded verifier checks the finite atom table, these twelve rank/degree/cohomology identities, and the complete internal Hom list used next.

## 3. The only internal image alternatives

The actual internal derivative map has target

    (E/F)(-2)=V O(-6)+O(-10)+O(-12)

for E3, and

    (E/F)(-2)=V O(-6)+W O(-11)

for E12. Among the atoms occurring in (3), the only nonzero channels are

    V_6 -> V_6;
    1_12 -> V_6;
    1_12 -> 1_12       for E3;
    1_12 -> W_11       for E12.                       (4)

Each channel is one-dimensional. There are no maps to O(-10). No support in (3) contains both V_6 and 1_12.

Consequently the internal image J is zero, the full saturated V O(-6), or a line isomorphic to O(-12). Every nonzero line image is saturated: a nonzero V channel has coefficient degree6, a scalar O(-12) channel has degree0, and the W channel has degree1. Any common zero divisor is invariant and would have degree at least12, impossible for any of these nonzero components. This also handles diagonal images with multiple components.

Let B be the raw first span of F and I its derivative image. The original connection gives

    0 -> J -> I -> O(26) -> 0,
    0 -> F -> B -> I(2) -> 0.                         (5)

For J=0, B has rank13 and degree4, impossible for a bundle injecting into a constant bundle.

Both remaining J alternatives are saturated; the external O(26) is saturated by original defect zero. Therefore the derivative-image lemma makes B=F^+ a saturated subbundle of H O. Its first-polar generation by (V+P+D) tensor W tensor O(-1) forces splitting degrees0 or-1. The exact characters from (5) give

    J=V O(-6):  B=(A+D) O+(Wp+T) O(-1),
    J=O(-12):   B=(A+D) O+T O(-1).                    (6)

Thus in either case C=A+D is a genuine constant eight-space. Let L be the coefficient Wp+T or T of the negative part of B. Then

    B/C O=L O(-1)

is actually saturated in (H/C) O. The projected image bar F and its derivatives lie there. If bar F contains an entire nonzero direct linear block, that block's first span is its nonzero constant coefficient span, contradicting H0(L O(-1))=0. All uses of this observation below concern the actual projected connection.

## 4. Universal channel facts

First, no equivariant quadratic inclusion D O(-2)->(A+D) O exists. The tautological O(-6) inside D O(-2) maps on coefficients through the highest Sym6 W in D tensor Sym2 W. But Sym6 W=V+P has no map to A+D, so every such quadratic map kills that nowhere-zero line.

Second, neither V O(-2) nor P O(-2) has a quadratic component in A O, since

    V tensor A=P+D,
    P tensor A=V+P+D.                                (7)

Therefore an inclusion (V+P) O(-2)->(A+D) O would have image inside the constant D of rank5, impossible for a rank-seven domain.

The nonzero linear channels from V+P+D to T are each one-dimensional. The D channel is ordinary multiplication D O(-2)->T O(-1), everywhere injective, with quotient O(4). If a nonzero V or P channel had its generic image contained in this D subbundle, it would factor globally through D O(-2), contradicting Hom_G(V,D)=Hom_G(P,D)=0. Hence either D plus V, or D plus P, with both channels nonzero, is generically onto T O(-1).

It is in fact onto everywhere. Any rank-drop divisor is invariant. A nonzero maximal minor has degree6, so such a common divisor has degree at most6, less than the minimum invariant orbit degree12. This proves

    (D+V) O(-2) -> T O(-1),
    (D+P) O(-2) -> T O(-1)

are onto whenever both displayed channels are nonzero.

For the possible Wp component, V->Wp and D->Wp vanish; P->Wp is the unique everywhere-onto tensor-Wp Euler map. The three channels P->Wp, P->T, D->T form the standard contraction

    Sym8 W O(-2) -> Sym7 W O(-1),
    ker=O(-10),
    Sym8 W=P+D, Sym7 W=Wp+T.                          (8)

Each channel in (8) is nonzero. Otherwise the Wp target is missed, or D of rank5 or the P-to-Wp kernel of rank2 lies in its rank-one kernel. Any map with all three channels nonzero is carried to (8) by rescaling its irreducible source and target coefficients. Hence every such map is onto.

These facts are universal channel and bundle identities. No actual coefficient value or point is selected.

## 5. Both first-polar alternatives are impossible

Consider first the second row of (6), with projected target T O(-1). The D component of the projection cannot be zero, by the first obstruction in Section4. If either V or P has a nonzero projected component, its image together with D is all T O(-1), forbidden by Section3. If neither projects, (V+P) O(-2) lies in C O, contradicting (7). This excludes J=O(-12).

Now consider the first row of (6), with projected target (Wp+T) O(-1). Again the D-to-T channel must be nonzero. Denote the P-to-Wp scalar by lambda and the P-to-T scalar by mu.

If lambda is nonzero and mu is zero, the P image is the entire Wp O(-1), forbidden. If both are nonzero, the P+D restriction has all three channels of (8), so the projected image contains all (Wp+T) O(-1), also forbidden.

Thus lambda=0. If the V-to-T or P-to-T channel is nonzero, it combines with D to give all T O(-1), forbidden once more. Otherwise V+P lies in the constant part C and contradicts (7). This excludes J=V O(-6).

All possible internal images have been excluded, proving the stated E3/E12 source exclusions and no stronger conclusion.
