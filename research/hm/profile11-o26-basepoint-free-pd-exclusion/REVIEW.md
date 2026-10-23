# Independent review of the basepoint-free P+D exclusion

## Verdict and immutable review boundary

**Accepted within its stated scope.** I independently read all eight sections, checked the geometric arguments and the human completeness argument, inspected the standalone checker, and ran that checker successfully. No mathematical obstruction to the claimed exclusion was found.

This review binds exactly these two files:

- `PROOF.md`, SHA256 `ed72d87f2026d61d58e848628ec5f624921541ccc3e985e2e550d086a0dd23c5`.
- `verify.py`, SHA256 `649a5a9c337f308c133ec2087ee27484a0ee60e8d2d3efe2b25d08a39d68b1c7`.

Review date: 2026-10-23 UTC. The final proof replaces the initial version's W_9 rank-drop-bound argument with its direct tautological multiplication description. I verified this replacement and verified that it is the only change from the initially reviewed proof, whose SHA256 was `c47c6688d39dd178480fec10f9c22840506bf833ae2cedafc6dfbb2b8e6a557b`. The checker is unchanged. The acceptance above binds the final hash, not merely the initial version.

The theorem excludes only the basepoint-free, degree-twenty-eight top systems for the matching P+D sources E6 and E13 of the two specified O(26), zero-original-defect profile-(1,1) labels. Combining it with the stated divisor reduction leaves those source branches in the degree20-divisor stratum. This is not an exclusion of that stratum, of either full label, of source2, or of the global rank possibility.

## 1. Dependency and input checks

I retrieved the cited original files at commit `db51525015bb7c5e825833d550d08dedf6f6ea96` of `Akilleez-QA/read-em-and-weep`, under `research/hm/order-four-quadratic-load/`. The pinned JSON records identify:

- `G3.11.dc58cc54f352` with source index 112, A_q=O(-10)+O(-8)+O(26), B_q=O(-28)+O(6)+O(8), and original determinant defect zero.
- `G3.11.4b6dad66f329` with source index 115, A_q=W O(-9)+O(26), B_q=O(-28)+W O(7), and original determinant defect zero.

Their source overlists contain the displayed E6 and E13 tuples, respectively. The original splitting and strict-top results supply rank E=17, degree E=-54, saturation in the constant ambient bundle, H0(E(1))=0, and H0(E^-(2))=0. The mismatch E6 onto the second negative quotient is indeed impossible: the only possibly contributing negative source block is its one O(-10), whose image has rank at most one.

I also retrieved the exact cited structural proofs:

- [PR796 proof at d2b43060c83328dd5118aee6b9288fcfa0c873ac](https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md).
- [PR799 proof at 2172e4a7abbbe232f9f448bea6fa01dee7927460](https://github.com/Akilleez-QA/read-em-and-weep/blob/2172e4a7abbbe232f9f448bea6fa01dee7927460/research/hm/profile11-quadratic-polar-obstruction/PROOF.md).
- [PR813 divisor reduction at 3f99ecf539a3a3da61743df0dff409e54270c865](https://github.com/Akilleez-QA/read-em-and-weep/blob/3f99ecf539a3a3da61743df0dff409e54270c865/research/hm/profile11-o26-divisor-reduction/PROOF.md).
- [PR825 endpoint result at ea94799a3b1e1c18a4d83061b92d7e7e2f1c631e](https://github.com/Akilleez-QA/read-em-and-weep/blob/ea94799a3b1e1c18a4d83061b92d7e7e2f1c631e/research/hm/profile11-o26-degree10-endpoint/PROOF.md).

The imported derivative-image, first-polar, and quadratic constant-span principles apply to the actual embedded bundles and do not require the forward endpoint to be section-free. The use of PR813 for divisor alternatives and of PR825 only for the surviving degree20 scope is correctly delimited. The present horizontal residual lemma is proved independently rather than imported as an unsupported separation assertion.

## 2. Kernel budgets and human completeness

For the assumed onto map F=(P+D) O(-2) to O(26), the rank-eight kernel has degree -44. Twisting the exact sequence by two gives the budget

    H1(K0(2)) = Sym28 W - (P+D) = A+V+P+2D.

The strict-top vanishing makes every kernel degree at most -3. Twisting by three gives Euler character -W-S-T. For an irreducible block U O(-j), j>=4, its H1 contribution has dimension (j-3)dim U and character U Sym^(j-4) W. This justifies the dimension/parity bound and prevents cancellation of forbidden constituents. Degree -3 blocks are uniquely recovered from the honest character sum(t)-W-S-T.

I checked the support completeness argument separately from the checker. The five possible W-producing atoms each consume the unique A and contribute exactly one W. At least one is necessary and at most one is possible. After that choice, no other A-consuming atom is available.

For the residual budget V+P+D, a T contribution is necessary. The available T-producing atoms give exactly the nine displayed residual configurations. Two such atoms cannot fit: they overlap V or P, or require two D. Any leftover V is V_4, any leftover D is D_4 or 1_8, and any leftover P is P_4 or Wp_5.

The resulting five cases are exhaustive:

- Distinguished 1_6: if 1_8 occurs, the nine residual configurations apply. If 1_8 does not occur, S can only be supplied by W_9 or 1_20. These give exactly the two extra supports, hence 11.
- Distinguished W_7: the remaining budget is V+P+D and the remaining requirement is T, giving 9.
- Distinguished 1_18: only one D remains, supplied by D_4 or 1_8, giving 2.
- Distinguished A_8: again only one D remains, giving 2.
- Distinguished Wp_13: the entire first budget is spent and the degree -3 coefficient is forced to be T, giving 1.

Thus 11+9+2+2+1=25, with disjoint distinguished cases and no omitted support. The checker verifies the numerical and character identities of the declared supports; it is not being used to establish this completeness by a hidden enumeration.

## 3. Internal images, first polars, and saturation

The declared atomic Hom table covers every atom occurring in those 25 supports and all four possible target factors. Every support has exactly one active source block. The two-dimensional Hom spaces from 1_20 and Wp_13 to T_5 are retained as whole spaces. No choice of a coefficient in either space is required.

I checked the image arguments as follows:

- T_5, V_6, Wp_7, and A_8 have the indicated scalar or tautological multiplication descriptions and are saturated.
- For P_6, contraction on Sym6 W has tautological kernel O(-12). Its projection to V O(-6) is nonzero. Its degree-six coefficient system cannot have a nonempty invariant base divisor, so this projection is nowhere zero. The restriction to P_6 is therefore a saturated injection.
- For W_9, I independently identified the unique channel W O(-9) to Sym5 W O(-5) as multiplication by the fourth power of the tautological line. It is everywhere injective, proving saturation directly. The final proof now uses exactly this argument, without an unnecessary rank-drop-degree assertion.
- Each nonzero line-source T component has no base divisor: degrees 5 and 7 are below twelve, while a degree-twelve divisor at degrees 13 or 15 would leave a nonexistent T system in degree 1 or 3. The nonzero scalar or tautological tail components are also nowhere zero. Diagonal line images are consequently saturated.
- For Wp_13, any rank-one image would be an equivariant quotient line O(-j) with even 6<=j<=12. The only possible source quotient has j=6, and that line cannot map to T O(-5). Hence every nonzero map in this full two-dimensional Hom space has rank two. No saturation is assumed at this step.

For the raw first span B, the exact image sequences hold before saturation. First-polar generation makes B(1) globally generated; its injection into a constant bundle bounds its degrees above by zero. Thus its degrees are exactly among -1 and 0. The rank and degree formulas are

    rank B = 10 + rank J,
    deg B = 10 + deg J + 2 rank J.

The two Euler-character identities then determine all twelve displayed polar rows. The positive-degree rows and the row with a negative S multiplicity are genuine contradictions. For every surviving row except Wp_13, the saturation defect is below twelve and hence zero. The exceptional row has degree -12 and permits precisely defect zero or twelve. In particular, an unsaturated exceptional image is not silently identified with a saturated forward span.

## 4. Constant quotients and the horizontal residual lemma

The degree-zero part of a saturated first span is an actual constant subspace, so projecting by it gives a saturated bundle in a genuine constant quotient. This is the right setting for the forbidden-full-linear-block argument. A full nonzero linear block in the projected F would have its constant first span inside a pure O(-1) bundle, which is impossible.

The generation observation is also valid without declaring an abstract splitting horizontal: after a missing linear component is quotiented out, the remaining derivative component is an O-linear map from O(-2)^9 to O(-3)^u and vanishes by degrees. That would contradict raw first-span generation.

The three universal linear channels are exactly P to Wp, P to T, and D to T. The first is onto and the last injective. The full Sym8-to-Sym7 contraction has all three nonzero, and rescaling source and target irreducibles normalizes any three nonzero channel coefficients to this contraction. This justifies the onto statements used to remove the indicated polar rows. The tautological O(-6) in D O(-2) proves that D cannot inject into a constant subrepresentation of A+D, since its coefficient system lies in Sym6 W=V+P.

For Section 5, an actual constant C0 containing F and mapping onto the positive O(28) has N=E intersect C0 O with degree -28 and N/F of degree -10. Its derivative has no negative quotient component. The negative quotient map E/F=T O(-3)+L to L is zero on T O(-3) and an isomorphism on L. Thus N/F is saturated in T O(-3), and its quotient Z0 has degree -8 with every degree at least -3.

The positive image is saturated in Q, so E+C0 O is saturated in the original constant bundle. This establishes, rather than assumes, saturation of R=E/N=Z0+L in the constant quotient. The external derivative of Z0 factors through L and vanishes by degrees; the remaining internal derivative into L(-2) also vanishes. Hence this actual embedded Z0 is horizontal and must have degree zero, contradicting degree -8. This removes both constant polar rows and the exceptional saturation-defect-twelve case.

## 5. The degree-six subsystem

In either remaining T-linear row, the D-to-T channel is nonzero and the P-to-T channel must be zero. The projected F is exactly the saturated multiplication image D O(-2) in T O(-1). Its first span is the whole projected T O(-1), with quotient O(4).

The quadratic-column principle makes the second span constant. The derivative factors through a line, so the constant span has rank at most seven; the rank-six first span of degree -6 cannot itself be constant. The constant span therefore has rank seven and quotient O(6). The induced derivative O(4) to O(4) is nonzero, hence an isomorphism. Vanishing of both H0 and H1 of T O(-1) identifies the seven-space with all H0(O(6)). This proves the actual complete-evaluation and backward-kernel identities, not just their abstract splitting types.

After adding back the actual constant part C, the full span C0 has B of corank one and B^- of degree -10. The saturated intersection E^+ intersect C0 O is either B or C0 O. The horizontal lemma excludes the latter. In the former case N=E intersect C0 O has degree -34 and the same rank as B^-. Its connection gives N contained in B^-. Both are saturated in C0 O, so they are equal, contradicting the degrees. This excludes both T-linear rows.

## 6. Complete-evaluation classification in the exceptional row

For the surviving pure-linear B, its constant span C0 has quotient Q0 of rank at most three: the derivative of B kills F and B/F has rank three. Every splitting degree of Q0 is positive, since it is globally generated and any trivial quotient would give a constant functional annihilating the full span of B. Also H0(B)=H1(B)=0, so C0=H0(Q0) and B is its complete evaluation kernel.

Rank at most three, degree twelve, and central parity leave precisely the 15 quotient shapes declared in the checker: a single even line; two even lines; three even lines; an irreducible three-space at degree four; or W/Wp at odd degree 1, 3, or 5 together with the remaining even line. These are all possibilities, not a search over unconstrained twists. Comparing complete-kernel coefficients leaves exactly O(4)+O(8), Wp O(1)+O(10), and V O(4).

The first has backward coefficient A+V+P and cannot contain D O(-2). In the second, equality of saturated rank-nine degree -18 bundles forces F to be the degree-ten block's backward kernel; its first span would have rank ten, not twelve. The last therefore occurs, giving the actual identities

    C0 = V tensor Sym4 W,
    B = V tensor U_3^4,
    F = V tensor U_2^4,
    B/F = V O(2),
    C0 O/B = V O(4).

The induced derivative between the last two bundles after twisting by -2 is an isomorphism. The equality for F follows from its saturated inclusion in B^- and equality of rank and degree.

## 7. Exact endpoint intersection and the final contradiction

I checked the final intersection at the sheaf level. I0=E intersect B is saturated in B, with I0/F=Wp O(-11) and B/I0=O(28). The second fundamental form of E^+ kills I0. Since the derivative B/F to (C0 O/B)(-2) is an isomorphism, C0 O/(E^+ intersect C0 O) has rank at most one.

Rank zero would put all of C0 O in E^+ and is excluded by the horizontal lemma. In rank one, the restricted derivative kernel on B and I0 are saturated of the same rank eleven, hence equal. Quotienting the derivative isomorphism then gives exact bundle identities

    (E^+ intersect C0 O)/B = Wp O(-9),
    C0 O/(E^+ intersect C0 O) = O(30).

The map to the negative L(2) part vanishes first on B by degrees and then on the quotient Wp O(-9) by the three stated representation vanishings. Its positive image is exactly O(28), already attained on B. Consequently N=E intersect C0 O has rank thirteen and degree -58.

The actual constant projection of E has sheaf kernel N. Its locally free image E/N has rank four and degree -54-(-58)=+4 and injects into the constant quotient (H/C0) O. Such an injection forces every splitting degree to be nonpositive, a contradiction. This final argument does not need saturation of the projected image E/N, or a claim of full fiberwise intersection in a quotient by E^+.

## 8. Executed verification and limits

The only mathematics verifier executed was:

    python verify.py

It exited successfully and checked the declared 34 atoms, the five W-producing atoms, nine residual configurations, 25 supports, 84 atomic Hom dimensions, twelve first-polar rows, fifteen positive quotient shapes, and the stated universal polar and endpoint vanishings. I inspected its exact Q(sqrt(5)) character arithmetic, explicit support declarations, and bounded loops. It contains no all-twist envelope or support generator. Its arithmetic checks are consistent with, but do not replace, the independent geometric checks above.

No selected actual HM/source coefficient, parameter, point, derivative value, matrix, source-instance rank, selected model experiment, scan, or large computation was used. The conclusions remain restricted to the frozen theorem's basepoint-free matching E6/E13 branches; the degree20-divisor stratum remains open.
