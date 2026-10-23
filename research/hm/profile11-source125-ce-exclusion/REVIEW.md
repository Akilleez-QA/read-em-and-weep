# Independent whole-proof review of the source125 ce exclusion

## Verdict and exact reviewed bytes

PASS. No mathematical gap was found in the complete single-source exclusion, conditional on the pinned actual-bundle and universal representation lemmas stated in the proof. This is an independent written-mathematics audit, not formal certification or a selected-source evaluation.

Reviewed on 2026-10-23. This approval is bound to these exact SHA256 hashes:

- PROOF.md: `0cfb8e53201202683d4f5dfb20b24c684d9c8b271f0eca55df51ef019dfbb120`
- verify.py: `3dbb1498896a7e317119df59b38bb5da148394625714325c9336085e1abf15f6`
- REPRODUCE.md: `6251f55eb6d1e6d432873f59d26e773e535f1ddcde046cff0750f970d2234c4e`

The scope is exactly source index125, tuple `(0,0,1,0,1,0,0,1)`, stable label `G3.11.ea6bced3bddf`. The source has rank17 and degree-54, and its full quadratic top has rank11 and degree-22. The source and stable-label catalog Git blob hashes are checked before accepting that identity. No whole-label exclusion or current frontier count follows from this review.

I read the complete candidate, its verifier and reproduction instructions, the cf actual-bundle arguments, the be high-P classification and constant-projection argument, and the two-P classification in the cited PR846 local proof. No exclusion of a different source is used as an exclusion of ce.

## Initial lower-row and divisor reductions

1. If the lower row on two P copies is zero, strict-top supplies eight independent high sections. A nonempty invariant divisor would leave at most seven, so the high map is onto. The seven displayed nonzero-H1 assemblies exhaust the two-P budget at rank at most seven. Their twist-three characters leave precisely the two stated kernels. Each has only the scalar V(-4) internal channel. The zero channel gives a positive-degree first span; the nonzero channel gives constant coefficient A+D but a putative linear coefficient Wp-S+T, which is not a representation. Thus the lower P functional is nonzero.

2. In the high-only P basepoint-free branch, the three high-P kernels and both possible low kernels have zero Hom to the complementary internal target. Vanishing on both ends of the kernel extension suffices; splitting is not needed. The whole positive pair is covered everywhere, and the full-top first-span degree is two. This excludes the branch.

3. The remaining high-only P divisor has degree12. Its raw high image is O(4), with kernel V(-4). If the only scalar internal channel vanishes, the rank-four quadratic rank-one gap would require a saturation correction of degree two, contrary to invariance. If it is nonzero, the raw first-span degree is minus eight. A nonzero invariant saturation correction has length at least twelve and would make that degree positive. Hence the raw span is already saturated.

   The resulting first span is `(Wp+T)(-1)`. Its intersection with E is exactly `(V+P_h)(-2)`, and its quotient is O(6), mapping to the original high O(18) through the degree12 divisor. The internal scalar channel identifies the source top V itself. The possible extension by V(-2) splits by ordinary H1 vanishing, and there is no V-to-P_h scalar component. Thus this intersection is not an arbitrary abstract splitting.

## Nonzero lower V row and exact constant-V capture

The assertion that the external image of N is abstractly O(4)+O(4) is justified. In addition to the onto degree-six low V and high P_h systems, the possible high V component also contains the same invariant degree12 factor: V occurs once in Sym18, and multiplication of its degree-six covariant realizes that occurrence. This multiplicity fact is explicitly stated in Section 5 and does not depend on the lower V row being zero. The off-diagonal V high component can therefore be removed by an abstract row operation on the two O(4) lines.

The kernel is Wp(-5)+V(-4), and its only internal channel is the canonical Euler Wp(-5) into P_l(-4). The two raw first-span degrees, minus two and minus eight, rule out every nonzero invariant saturation correction. The corresponding first-polar characters are the stated M0 and M1.

For M0, projection by the genuine constant V+P either covers the entire linear Wp summand or vanishes. The first case violates the actual-connection linear-channel obstruction. The second would place saturated N of rank seven and negative degree in a constant rank-seven space, which is impossible.

For M1, the projection of N to `L=(Wp+T)(-1)` has the three asserted nonzero channels. The V channel cannot land in the constant V or in Wp(-1). If either P_h channel vanishes, the projected image covers a complete nonzero linear block, again contradicting the actual derivative condition. Rescaling the irreducible source and target factors therefore identifies this inclusion with the standard saturated `Sym6 W O(-2) -> Sym7 W O(-1)`, whose quotient is O(6).

The extra Euler block is handled correctly, rather than silently omitted:

- The exact intersection of M1 with E is an extension of N by the canonical Wp(-3) in P_l(-2). The extension splits because its relevant ordinary H1 is zero.
- Its projection to L/N=O(6) is zero, since Wp does not occur in Sym9. Since N maps isomorphically onto its image in L, subtracting the corresponding N lift places the extra block in the actual constant V.
- Consequently the rank-two intersection with V is Wp(-3). A rank-three intersection would put the whole constant V inside saturated E, contradicting H0(E)=0. There is no larger equal-rank intersection hidden by torsion because these are saturated intersections.
- This block retains its nonzero canonical P_l projection. It has no lift into the source top V, because Wp is absent from V tensor W; any P_h lift has zero low row. Its lower derivative is therefore nonzero. Otherwise the P_l lower system would factor through Wp(-1), whose Hom to O(4) is zero. The degree-seven restricted system is onto.

It follows that `V/(E intersect V)=O(6)` maps isomorphically to the lower O(6) factor. Its image is a saturated graph in the saturated positive pair, so projecting this genuine constant V gives exactly the claimed saturated E' and derivative image O(-10)+O(16). Possible diagonal P_h lifts merely change the P multiplicity basis and do not change the splitting.

The highest Wp(-1) in E' has a basepoint-free high system: a degree12 divisor would require Wp in Sym5. Its kernel O(-18) has only the V(-4) and P(-4) internal channels, and each nonzero degree14 component is basepoint-free. Thus the nonzero internal image is a saturated line. Its first span is the actual constant P with exact intersection Wp(-1)+O(-16), capturing the saturated high line. After projection, the O(-16) line has no tail components and lies entirely in `(V+P)(-2)`. Its quotient is a locally free rank-six degree-two direct summand of the projected source, which cannot embed in a constant bundle. This closes the nonzero-V-low branch.

## Last complementary-P alternatives

### Nonzero restricted high row

Strict-top forces the high system on `(V+P_h)(-2)` to be the complete degree-six system times the degree12 invariant. The restriction q of the remaining P_l high row to its low kernel V(-4) is a degree20 V covariant. If nonzero, it is basepoint-free: the only possible invariant divisor degrees at most20 are12 and20, and V occurs in neither Sym8 nor Sym0.

Surjectivity of q on the low kernel, together with surjectivity of the low P_l row, gives surjectivity of the full map to O(4)+O(16) at every point, including the high-only divisor. This is stronger than generic independence of the two rows and justifies the full positive-kernel exact sequence and cohomology budget.

The five-kernel list is complete. Strict-top bounds every ordinary kernel degree above by minus three. The excess-degree bound `r*(j-3)<=15`, central parity and the H1 budget give exactly the displayed twenty-two nonzero-H1 atoms. Only O(-6), W(-7), A(-8) and O(-18) can supply the required negative W at twist three. Each uses the unique A in the budget, so exactly one can occur, even allowing degree-minus-three atoms with positive twist-three character. O(-6) cannot inject into the full top. A(-8) and O(-18) consume the complete budget and force the stated degree-minus-three corrections. After W(-7), the remaining V+P budget has exactly the three displayed assemblies. Their corrections give the remaining three kernels.

Every resulting kernel has zero Hom to the remaining internal target. The full positive image is saturated, so no hidden internal image or divisor survives, and the first-span degree is two. This excludes q nonzero.

### Zero restricted high row

If q is zero, the complementary high row factors through the low O(4) quotient, with factor a scalar multiple of the unique degree12 invariant. The full raw external image is therefore abstractly O(4)+O(4). Its kernel is the extension of V(-4) by T(-3), which splits by ordinary H1 vanishing. Both summands have zero internal channel.

The raw first-span rank is thirteen and degree is minus ten. Every nonzero invariant saturation correction has length at least twelve and would give positive degree. Thus it is saturated, with the stated splitting `V O+(2Wp+T)(-1)`.

After projecting the actual constant V, choose a nonzero P multiplicity direction killed by the unique T channel. It cannot also be killed by both Wp channels, since a rank-four source would then inject into the rank-three constant V. Its remaining channel is the Euler surjection onto a whole Wp(-1) multiplicity summand. Every local section of that summand lifts to the quadratic top; the actual derivative and constant projection place its first span inside the pure linear bundle. A nonzero linear block has a nonzero constant first span, contradicting the vanishing of global sections of that pure linear bundle. This closes q zero.

## Independent reproduction and boundaries

I inspected and independently ran the frozen verifier. It exited successfully with:

    PASS: 121 fixed Hom spaces, kernel/polar identities, and pinned source125 ce identity.
    No selected actual source evaluation, source scan, parameter, point, matrix, or instance rank was used.

I also independently checked the finite support assertion by applying the parity, rank/degree and exact H1-budget filters to all irreducible atoms with degrees four through eighteen. The resulting twenty-two atoms agree exactly with the displayed support. This was a bounded universal representation check, not a selected-source calculation. The negative-W argument above supplies the written completeness proof; neither this check nor the companion verifier substitutes for the actual-connection, saturation or intersection arguments.

No proof changes were necessary. No selected actual HM/source coefficients, parameters, points, derivative evaluations, matrices, instance rank tests, experiments, source scans or large computation were used. No publication action was taken. Substantive changes to the exact bound files require renewed review.
