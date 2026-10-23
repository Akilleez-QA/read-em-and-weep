# The two-P quadratic top block is impossible in the O(26) branches

## Result and scope

Neither of the source types

    U6  = (2P+D) O(-2)+Wp O(-5)+O(-8)+O(-10),
    U13 = (2P+D) O(-2)+Wp O(-5)+W O(-9)

can occur in the retained zero-original-defect positive-O(26) profile-(1,1) branches. Concretely, this removes the U6 source entries for G3.11.dc58cc54f352 and G3.11.4b6dad66f329, and the U13 entry for G3.11.4b6dad66f329. U6 and U13 are names for these displayed types, not additional catalog IDs.

The proof classifies a six-element exact top-kernel support, then uses the actual internal derivative map. Its only nonzero possibility forces a first-polar bundle with constant part A+D and linear part Wp+T. The three nonzero channels of the standard binary-form contraction force an entire linear block into the projected first span, a contradiction.

This excludes source entries only, not the two full labels, source2, or the global rank problem. No selected actual HM/source coefficients, parameters, points, derivative values, matrices, source-instance ranks, selected models, scans, or large computations are used. The accompanying verifier checks only the bounded universal character identities displayed in the proof.

## 1. Immutable inputs

The repository is Akilleez-QA/read-em-and-weep. Original source, quotient, strict-top and label data are pinned at

    db51525015bb7c5e825833d550d08dedf6f6ea96,
    research/hm/order-four-quadratic-load/.

The exact files are ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md, ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md, one-one-endpoint-necessary-pairs.json, and rank-three-quotient-frontier-144.json.

The labels and source indices are

    G3.11.dc58cc54f352, index112:
      A_q=O(-10)+O(-8)+O(26), B_q=O(-28)+O(6)+O(8);
    G3.11.4b6dad66f329, index115:
      A_q=W O(-9)+O(26), B_q=O(-28)+W O(7).

The index112 overlist includes the U6 tuple (0,0,0,0,1,1,0,1). Index115 includes that tuple and the U13 tuple (0,0,0,0,1,0,1,0). The relevant exact source overlists and common-divisor alternatives are restated and proved at

    PR813, 3f99ecf539a3a3da61743df0dff409e54270c865,
    research/hm/profile11-o26-divisor-reduction/PROOF.md.

The actual first-polar generation and constant-quotient principle are at

    PR799, 2172e4a7abbbe232f9f448bea6fa01dee7927460,
    research/hm/profile11-quadratic-polar-obstruction/PROOF.md.

The actual internal/external derivative-image sequence is at

    PR796, d2b43060c83328dd5118aee6b9288fcfa0c873ac,
    research/hm/profile12-quadratic-block-exclusion/PROOF.md,

Section3. All uses here are independent of any interior-stage vanishing. Each path is at https://github.com/Akilleez-QA/read-em-and-weep/blob/COMMIT/PATH for the displayed immutable COMMIT and PATH.

Work over C with binary icosahedral group G. Write W for the defining two-space, Wp for the other two-space, A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and V,P for the other even three- and four-dimensional irreducibles. All irreducibles are self-dual. The actual E is saturated in H O, has H0(E(1))=H0(E^-(2))=0, and has the actual quotient A_q. Original defect zero makes A_q saturated in Q(-2), Q=(H O)/E, and gives E^+/E=A_q(2).

## 2. The exact small top kernel

Let F=(2P+D) O(-2), the canonical top block. Its image in A_q lies in O(26). Strict-top vanishing injects its thirteen-dimensional coefficient representation into Sym28 W. A common divisor has degree0,12,or20 by PR813. The last two alternatives would inject 2P+D into Sym16 W=V+P+2D or Sym8 W=P+D, respectively, which is impossible. Therefore the positive map p:F->O(26) is everywhere onto.

Write K0=ker p. Then

    0 -> K0(2) -> (2P+D) O -> O(28) -> 0,
    rank K0=12, deg K0=-52,
    H0(K0(2))=0,
    H1(K0(2))=A+V+2D,
    chi_G(K0(3))=Wp-W-S.                             (1)

Every splitting degree of K0 is at most-3.

For a complete support derivation, denote U O(-j) by U_j. An atom U_j with j>=4 consumes U tensor Sym^(j-4) W in the positive H1 budget A+V+2D. The dimension bound (j-3) dim U<=16 and central parity leave exactly the following atoms that fit componentwise:

    A_4,V_4,D_4,S_5,1_6,W_7,Wp_7,1_8,1_14.           (2)

Their respective H1 budgets are

    A,V,D,A+D,A,A+D,V+D,D,A+V+D,

and their next-twist H1 tails are

    0,0,0,S,W,W+S,T,S,S+T.

The degree-3 coefficient is uniquely forced by (1) and must be an honest representation. The required W tail forces exactly one of 1_6 or W_7, each consuming the sole A. With W_7 chosen, the residual V+D is assembled as V_4+D_4, V_4+1_8, or Wp_7. With 1_6 chosen, the residual V+2D must supply an S tail, so at least one 1_8 is forced. The three possibilities are V_4+D_4+1_8, V_4+2·1_8, or Wp_7+1_8.

Thus the complete list is

    Wp_3+V_4+D_4+W_7;
    (Wp+S)_3+V_4+W_7+1_8;
    (Wp+T)_3+W_7+Wp_7;
    Wp_3+V_4+D_4+1_6+1_8;
    (Wp+S)_3+V_4+1_6+2·1_8;
    (Wp+T)_3+Wp_7+1_6+1_8.                           (3)

This is a two-budget character classification, not an all-twist envelope. The bounded verifier checks the finite eligible atom identities and all six displayed rank, degree and cohomology identities.

## 3. The actual first polar has only one possible splitting

The internal derivative map of K0 has target

    (E/F)(-2)=Wp O(-7)+O(-10)+O(-12),

or

    (E/F)(-2)=Wp O(-7)+W O(-11),

according to the source type. Every degree in (3) is at least-8, so all maps to the last negative factors vanish by degree. For the Wp O(-7) target, the only nonzero channel is the scalar map Wp O(-7)->Wp O(-7). In particular 1_8 has no such map because Wp is absent from W, and W_7 has no such scalar map. Thus the actual image J is either zero or the full saturated Wp O(-7).

Let B be the raw first span of F, and I its derivative image. The original connection gives

    0 -> J -> I -> O(26) -> 0,
    0 -> F -> B -> I(2) -> 0.                         (4)

If J=0, then B has rank14 and degree2, impossible for a bundle injecting into a constant bundle.

Hence J=Wp O(-7). Both this internal image and the external O(26) are saturated, so the derivative-image lemma gives B=F^+, a saturated subbundle of H O. Equivalently, (4) has rank16, degree-8, and any invariant saturation defect would have degree at least12, again impossible.

The image B is generated by the universal first-polar map

    (2P+D) tensor W tensor O(-1) -> H O.

Its splitting degrees are therefore0 or-1. Its Euler characters, computed from (4), are

    chi_G(B)=A+D,
    chi_G(B(1))=W+Wp+2S+2T.

Since W tensor (A+D)=W+2S+T, this forces

    B=(A+D) O+(Wp+T) O(-1).                           (5)

The degree-zero part C=A+D is an actual constant eight-space. Projection gives a genuine saturated inclusion

    B/C O=(Wp+T) O(-1) subset (H/C) O.

The image bar F of F lies there, and so do its derivatives, because B is the first span of F and C is constant.

No whole nonzero direct linear block of (Wp+T) O(-1) can lie in bar F. Its first span in the constant quotient would be a nonzero constant coefficient space lying in (Wp+T) O(-1), contradicting the absence of global sections. This is a statement about the actual projected connection, not an abstract splitting declared horizontal.

## 4. The three-channel contraction is everywhere onto

There are exactly three nonzero equivariant linear channels from (P+D) O(-2) to (Wp+T) O(-1):

    P -> Wp, P -> T, D -> T.                           (6)

Each is one-dimensional; D->Wp is zero. These assertions follow from

    P tensor W=Wp+T, D tensor W=S+T.

The standard binary-form contraction provides an everywhere-onto map

    Sym8 W O(-2) -> Sym7 W O(-1),
    ker=O(-10).                                      (7)

Here Sym8 W=P+D and Sym7 W=Wp+T. All three channels in (6) occur nontrivially in (7). The P->Wp channel must be nonzero to reach the Wp target. The D->T channel cannot vanish, since the kernel of (7) has rank one, not at least five. If P->T vanished, the kernel of the P->Wp channel would have rank two and would lie in the kernel of (7), again impossible.

Any map having all three channels nonzero is obtained from (7) by rescaling the two source and two target irreducible coefficients: the three-channel incidence graph has no cycle. Thus every such map is onto. Its projection (P+D) O(-2)->T O(-1), when both channels to T are nonzero, is likewise onto after the same source rescalings. Finally P O(-2)->Wp O(-1) alone is the tensor-Wp Euler map and is everywhere onto.

These are universal identities in arbitrary fibers. No point or coefficient value is selected.

## 5. Exhaust the multiplicity rows

Write the projection F->(Wp+T) O(-1) using the two-dimensional P multiplicity space. Let lambda be its row to Wp, mu its row to T, and nu the scalar for D->T. All other channels vanish.

Suppose first lambda=0.

- If mu=0, the direct summand 2P O(-2) of F lies in C O. It is saturated in H O, hence saturated in C O, and has the same rank eight as C. This would identify it with C O, contrary to its degree-16.
- If nu=0, the kernel contains one P O(-2) and D O(-2), of total rank nine, inside C of rank eight. This is impossible.
- If both mu and nu are nonzero, choose the constant P multiplicity line on which mu is nonzero. The restriction from that P plus D to T O(-1) has its two channels nonzero, so Section4 makes it onto. Thus bar F contains all T O(-1), contrary to Section3.

Therefore lambda is nonzero. If lambda and mu are independent, a P multiplicity line killed by mu but not by lambda maps onto the full Wp O(-1), again impossible. The same contradiction holds if mu=0. We may therefore assume mu is a nonzero scalar multiple of lambda.

If nu=0, the common P-row kernel plus D has rank nine and lies in the constant rank-eight part, a contradiction. If nu is nonzero, choose a P multiplicity line not killed by lambda. Its P plus D restriction has all three channels (6) nonzero, so it maps onto the full (Wp+T) O(-1). This is the final forbidden linear block.

Every case is impossible. Hence neither U6 nor U13 can occur in the stated O(26) branches. No further source entry or entire label is excluded by this theorem.
