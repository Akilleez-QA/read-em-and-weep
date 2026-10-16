# Source-independent prefix pruning versus the old four-tail reduction

## Result

The refinement still permits the exact prefix collapse of J1 and J2 and the associated78 terminal-selector words. It also permits repeated-CARRIER prefix pruning after the authenticated common-frame conversion. It does not justify replacing refined residual tails by the four distinct coarse-carrier tails123,124,134,234. Tail vertices may share carriers or even physical source labels while differing in standard tags.

All checks below use algebraic contraction identities and zero/nonzero seed support only. No physical source polynomial products or values were generated.

## 1. Prefix collapse is independent of the residual formula

For any End-valued2-cochain R, write j_a(R)=I_a R^t P_a in the common original frame. The pinned side conditions H^2=HI=PH=0 imply

    h_a^2=0,   h_a j_a=0.

On an ordered quadruple, all but the first face of delta(jR) have j anchored at the original first vertex and hence are annihilated by its leading h. Therefore

    J1_abcd=h_a j_b(R_bcd).

On an ordered quintuple, all but the first face of delta(J1) have leading h_a and are killed by h_a^2. Consequently

    J2_abcde=-h_a h_b j_c(R_cde).

These are cochain identities before closedness is used. Closedness is needed for the total-lift/cohomology interpretation, not for this prefix simplification. The same reasoning gives J3=-h_a h_b h_c j_d(R_def), retained in the comparison even though S has no degree-five target.

## 2. Equal-carrier prefix pruning is authenticated

Directly fetched pinned `source-identity.md`, commit08b73637d4136f91606aad332c46cafd064417f8, blob7e12e8c7479427db87cd496763f5f003005af9c5. Its section2 explicitly states that repeated prefix carriers vanish, including different line masks for the same carrier, because their common-frame homotopies coincide.

The companion `hm-full-sign-legal-line-bound.md` section6 identifies common-frame H and E=IP as carrier-only. Its endpoint-frame conversion puts an included arbitrary R in the form

    I_carrier Mbar^t P_carrier,

with physical endpoint frame factors absorbed into Mbar. Hence h_a j_b=0 whenever a,b have the same carrier, even if their masks or standard tags differ. No specific formula or locality of Mbar is required.

Since the common ordering is source first, carrier labels are nondecreasing along an increasing common tuple. Surviving J1 therefore requires the first two carrier labels strictly increasing. Surviving J2 requires the first three strictly increasing. This condition concerns the prefix anchors and the included tail's FIRST vertex only. It says nothing about equality among the final two tail labels.

## 3. Exact terminal selector words and signs

Let M denote the row residual on the three actual tail vertices. For J0 anchored at a, lambda2 has the three words

    row9(I_a) M^t col3(P_a),
    row10(I_a) M^t col4(P_a),
    -2 row12(I_a) M^t col6(P_a).

For J1 with prefix b and tail anchor a, lambda3 has

    row0(H0_b I_a) M^t col3(P_a),
    2 row2(H0_b I_a) M^t col6(P_a),
    row10(E_b I_a) M^t col1(P_a H1_b),
    2 row12(E_b I_a) M^t col5(P_a H1_b).

For J2 with prefix A,B and tail anchor C, the two selected blocks are

    (J2)_M20=-H0_A E_B I_C M^t P_C H1_B,
    (J2)_M31=+E_A E_B I_C M^t P_C H1_B eta_A.

The lambda4 entry signs are(-,+), so BOTH final words have positive coefficient:

    row0(H0_A E_B I_C) M^t col0(P_C H1_B),
    row10(E_A E_B I_C) M^t col0(P_C H1_B eta_A).

These are precisely3,4,2 words, multiplied by2!,3!,4! staircase paths, giving78 raw terminal-selector paths. All tuple owners, weights and restrictions remain attached. This removes the artificial4038 raw face/homotopy expansion without evaluating a single physical polynomial.

## 4. Safe bounded carrier predicates from seed support

The following are NECESSARY conditions for each word to survive; passing a condition is not a nonvanishing assertion. They are obtained by reading whether pinned polynomial entries are empty, not by multiplying them.

For lambda2:

- Leading carrier*,0,2 gives zero after the listed seed zeros.
- At carrier1, only the third word can survive, with coefficient-2.
- At carriers3,4, none of the three individual words is eliminated by these endpoint zero tests.

Thus the allowed candidate leaders are1,3,4. The old exclusion of3,4 used two larger DISTINCT coarse carriers and cannot be made on the refinement.

For lambda3, additionally require b<a by section2:

- Word1 requires a in{2,3,4}, since P_a[:,3] is zero for*,0,1.
- Word2 requires a in{1,3,4}, since P_a[:,6] is zero for*,0,2.
- Word3 requires b in{2,3}: E_b row10 is zero for*,0, while H1_1[:,1]=0; b<a rules out b=4.
- Word4 requires b in{1,3}: E_2 row12=0, and H1_*[:,5]=H1_0[:,5]=0; b<a rules out b=4.

For lambda4, require A<B<C:

- Word1 requires B>=1 because H1_*[:,0]=H1_0[:,0]=0.
- Word2 requires A>=1 because E_* and E_0 row10 are zero.
- The final eta factor uses its actual anchor: eta_A[:,0] has its sole nonzero entry at the pivot of A. Therefore col0(H1_B eta_A) is the corresponding H1_B column times the pivot denominator. One must not substitute column0 independently of A.

A Boolean-support matrix-word interpreter may refine these necessary tests by rejecting empty reachability between the selected endpoints. Boolean survival is still only an upper-support certificate: polynomial cancellations can create additional zeros. Exact identities such as h_a^2=0 should be applied separately, not inferred from Boolean multiplication.

## 5. Concrete obstruction to importing distinct-tail support

The old four-tail proof first projected onto an alternating coarse-carrier cochain using fixed legal-mask weights. That step made repeated coarse carriers cancel and allowed strictly increasing distinct carrier tuples. The new Rsharp is a cochain on common vertices (physical source,standard tag) with scalar-homotopy dependence on those tags. No descent to a carrier-only cochain has been proved. Neither a common vertex nor a raw residual value is determined by its carrier label.

A source-independent local selector counterexample is available without polynomial evaluation. Read the carrier1 primitive support:

    a=I_1[12,0] is nonzero,
    P_1[:,6]=(0,c)^t with c nonzero.

The other lambda2 words vanish at carrier1. For the tracefree matrix M=E21, its selector is therefore exactly-2ac, a nonzero rational expression over the characteristic-zero function field. Nonzeroness follows from the recorded nonzero factors and the integral-domain property; no product was expanded.

Choose three distinct common vertices having this carrier and fixed mask but different standard tags. A local End1-cochain supported on their last edge realizes this M as the value of its closed coboundary on the triple (multiply by any nonzero local full-sign scalar section when recording characters). Thus closedness alone does not force the repeated-carrier local selector to vanish.

This is NOT a claim that actual Rsharp has this prescribed value, NOT an obstruction computation, and NOT a counterexample to gauge invariance. The complete detector of that exact global cochain is zero; cancellations can involve other tuples. It disproves a universal pointwise zero-support argument for repeated carriers. A new class-level carrier descent could in principle recover a coarse four-tail presentation, but that would need its own regular maps, denominator ownership and comparison proof.

For actual Rsharp, even repeated physical source labels cannot generally be discarded merely because their standard tags differ. For example if the first two physical labels coincide then A=g_ij=I and k_A=L_A=C=0, but E_p(s_q) can still retain U_B times derivatives of the scalar edge s_q,ij. The transition-only scalar solver need not vanish on an edge with equal physical labels and unequal standard tags. The degeneracy of the pulled-back FIRST-ORDER F must not be transferred automatically to this new second-order source.

## 6. Additional old reductions that do not follow

The old determinant grouping over carrier permutations requires the residual entry to be the SAME alternating coarse cochain after each permutation. The refined standard-tag dependence prevents that inference. Likewise the781 owner-feature count, joint-moment formulas for a three-carrier-local residual, and equal-source-value merger of outer weights cannot be imported unchanged.

The existing primitive identities and their pointwise selector consequences remain available on each actual common tuple. In particular equality of two prefix selector matrices alone does not imply equality of the differently tagged residual values being multiplied by those matrices.

The valid next step is owner-aware structural pruning of the78 terminal-selector words, retaining all source/common labels and the inner scalar sums. No coefficient value or execution-resource conclusion follows from that combinatorial pruning alone.

## 7. Prefix legal-mask sums can be eliminated independently

One further exact reduction does survive. After section2, prefix carriers are strictly increasing and strictly less than the tail's first carrier. In the common original frame every prefix H,E and eta factor depends only on its carrier. The residual Rsharp is evaluated on the three tail common vertices and hence has no free dependence on a removed prefix mask. Its internal scalar-solver summation labels remain independent dummy indices and are not identified with an outer prefix mask.

For a fixed assignment of prefix carriers and standard rows, varying a prefix mask cannot change its position in source-first sorting: strict carrier inequalities already fix all its comparisons with other prefixes and the tail. Its alternating permutation sign and the standard row carrying its weight remain unchanged. Thus the mask sum factors independently:

    sum_(m in {0,1}^4) rho_outer(e,b,m)
      = R_outer(e,b) product_i(sum_(m_i=0,1)L_outer(e,i,m_i))
      = R_outer(e,b).

This removes up to16 raw mask choices for each prefix: at most16 for J1 and256 for J2, before the existing structural zeros in finite coordinates. The prefix carrier weight, standard-tag ownership and homotopy factor are retained. The same algebra applies to the third prefix in J3 if used in a comparison certificate, although there is no degree-five terminal detector row.

This does not sum any tail mask, does not identify residuals with different standard tags, and does not reproduce the old joint-moment/781-feature reduction. In particular, no differentiated prefix mask weight is being discarded: the resolution prefix maps take no derivatives and the scalar derivative occurs inside the tail residual.
