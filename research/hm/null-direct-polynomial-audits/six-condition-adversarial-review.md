# Adversarial review of the six-condition reduction

20 October 2026. Formal mathematical record; no obstruction coordinates were evaluated.

## Verdict and limits

The strongest claim survives this adversarial review **conditional on the stated first-order existence, pair-character Ext¹, HM-action, and characteristic-zero target-representation premises**. I independently reconstruct the crucial polynomiality bridge below, including a direct fixed-primitive alternative to the height-one proof. I find no need to assume the desired polynomiality, a global root over all coefficient space, singular HKR, or uniqueness of normalized first lifts after normalization.

This is not a verification of any obstruction coordinate or proof that the remaining six coordinates vanish. Six means six allowed coordinates of one weight-eigenspace, not a proof that the actual obstruction map has rank six. The final equivalence with existence of the diagonal second-order module additionally imports the mixed-vanishing result; polynomiality and the six-coordinate restriction themselves do not require mixed vanishing.

## 1. Independently reconstructed source bridge

Let R=C[A,B,C], S=Spec R[1/(AC(B²−4AC))], Y=(P¹)^4, M=ρ*End(H). The finite algebra of the fourfold cover, as a module with deck action, is the direct sum of the fixed line bundles O_Y(−2 on J). Therefore, in every character J,

H^k(X_R,p*M)_J = H^k(Y,M⊗O_Y(−2 on J))⊗R.

This is an equality of modules from finite pushforward and a fixed base Čech complex, not a semicontinuity inference. In particular the invariant target has an actual constant trivialization. The algebra multiplication varies with the branch coefficients; the cohomology module decomposition does not.

Choose a finite affine base cover trivializing ρ*H and L=O_Y(1,1,1,1), with fixed transitions h_ab and l_ab. On any locus carrying the actual root N²=p*L, refine étale locally to square-compatible frames. Write g_ab=τ_ab h_ab, τ_ab²=l_ab. Root-frame refinement introduces only ±1 on additional indices over the same base chart. Relative derivations kill these constants.

For a pair p={i,j}, direct differentiation gives

V_i(g_ab)=τ_ab y_i D_i h_ab,
D_i=∂_i+(∂_i log l_ab)/2.

Here D_i is an operator for this individual transition, not a claim of a globally defined connection on N or H. In the normalized first-order residual the products of τ cancel using the actual transition cocycle. Thus C_1,p is the image of a fixed base Čech cocycle c_p with coefficients M⊗O_i(−2)O_j(−2). The b term has this same property: q_i q_j=y_i y_j/(x_i x_j). No trace-only replacement of the matrix Atiyah class occurs.

Imported first-order cancellation at F0=(1,0,−1), together with the displayed cohomology identification, gives [c_p]=0. Choose a fixed base Čech primitive U_p, δU_p=−c_p. This is an existence deduction on the fixed acyclic cover, not an executed solution for the physical entries. The normalized first boundary x_p=y_i y_j U_p then solves the first-order equation on every root-bearing family. Thus first-order existence does not arise from an unjustified claim that vanishing at one point extends: the actual cocycle and primitive are fixed base data.

### Direct quadratic degree audit

There is also a direct formal check of polynomiality, independent of Hartogs. In the same square-compatible frames,

V_i²(τh)=τ[F_i D_i²h+(F_i′/2)D_i h],
V_iV_j(τh)=τ y_i y_j D_iD_jh  (i≠j),

where F_i=Ax_i³+Bx_i²+Cx_i. For a first boundary u_p=g x_p, its root-normalized coefficient is y_i y_j times fixed base data. Differentiating it uses V_i(y_i)=F_i′/2 and y_i²=F_i. All base differentiation and all l_ab logarithmic derivatives are independent of branch coefficients.

Consequently:

- u_p u_p contains F_iF_j times fixed base data.
- μ_p(u_p,g) and μ_p(g,u_p) contain one branch-linear factor from each pair factor, through F_i or F_i′.
- μ_pp(g,g) consists of products of the displayed branch-linear second-derivative operators or the mixed derivatives whose y squares give F_iF_j.
- T_p(g)g contains a_r, linear in A,C, and q_s V_s(g), which supplies F_s times fixed base data. Hence it is quadratic, not a term omitted from the audit.
- b_p u_p and b_p²g are quadratic by y_i²y_j²=F_iF_j.
- μ_p(b_p,g) has the same derivative accounting as the μ_p(u_p,g) terms, and is quadratic as well.

In every normalized triple-overlap term, the scalar root factors cancel against τ_ik. All remaining coefficients live on the fixed base cover; parameter denominators cannot come from h,l,U, since these are fixed base data. Each pure term is deck invariant. This constructs a homogeneous quadratic base Čech expression for the complete source on root-bearing loci. Its cocycle identity follows from full algebroid coherence and the first equation, not from separately asserting that its individual summands are cocycles. Since it is a polynomial base expression and is a cocycle on dense S, it is a cocycle over R. This supplies an independent explanation of the polynomial class, without constructing an actual root at the origin of coefficient space.

This argument is symbolic bookkeeping of the complete formula, not a physical source-entry evaluation. It does not compute U_p or an obstruction coordinate. Pair-character Ext¹ vanishing identifies this selected primitive with the stipulated original first boundary up to gauge; induced second-order gauge terms must be retained.

## 2. Independent check of the height-one route

The reported extension route also works without the direct calculation above. At the generic divisor A=0, C is a unit and P0 is a smooth Cartier section because x(C+Bx+Ax²)=y². At C=0 use P∞, and at B²−4AC=0 either marked section works. Their doubled divisors are the pullbacks of 0 or ∞. Thus genuine roots exist at all three needed DVRs; a universal root over all A³ is neither claimed nor needed.

On a common smooth fraction field, N0/N∞ has square O, via div(x)=2P0−2P∞. The associated μ2 torsor is finite étale. Derivations extend uniquely through étale maps and kill the constant ±1 transitions, so tensoring by this line intertwines all differential products and the noncentral T and triple-unit module equations. This is more than cancellation inside End.

The first residual is regular over each DVR and its class lies in a free cohomology module. Generic vanishing therefore implies integral vanishing and a regular first primitive. The complete second residual gives an integral invariant class. Pair-character uniqueness identifies its generic restriction with the same stipulated smooth class. There are no unexamined divisorial poles: S omits exactly the three divisors inspected. Normality removes all remaining codimension-two concerns coordinatewise. In particular no unsupported singular HKR or second-ambient theorem enters this pole-removal step.

## 3. Ambient comparison and D5 covariance: order of dependencies

The invariant smooth HH² calculation gives only four directions V_i⊗H¹(O_Ci). This follows from the independent deck characters, not from a restriction to global bidifferential operators. On every smooth family member each is killed by the characteristic map: vary one ordered branch cross-ratio while retaining the degree-two map, root section, and actual pullback bundle. The nonzero tangent statement uses marked elliptic deformation, not the possibly ramified coarse j-coordinate.

Use this vanishing **after** identifying first-order ambient data and transporting the first module boundary. SL2 binary transformations preserve dx/y and hence the relative vector fields, while the b class transports naturally. An actual scalar coboundary equivalence handles representative changes. Torus preserves N∞; reflection exchanges it with N0, handled by the exact torsion equivalence. Pair-character Ext¹ vanishing then compares boundaries. Only now may the remaining second-jet discrepancy be erased in invariant obstruction cohomology by the characteristic-map theorem.

This proves covariance without assuming the desired second-jet cochain invariance. It also exposes the precise circular shortcut that is not allowed: ambient independence alone would not identify first-order data or a root family. The reviewed construction supplies those earlier steps.

For reflection [[0,i],[i,0]], x′=1/x and y′=−y/x², so A↔C and B is fixed. It sends F0 to −F0. The comparison back by branch scaling changes first order by −1 but pure second order by +1. No reflection-sign twist survives in the pure target. The invariant H¹(O_C) coefficient has the natural SL2 trivial linearization, and scalar HM lift ambiguities cancel in End.

## 4. Canonical target and six-condition count

The full fixed target is H²(Y,M); the diagonal sum, not an arbitrary pair coefficient individually, has the block-even compact target. Internal pair swaps must be accompanied by the appropriate parameter signs in the two-parameter deformation. Block exchange interchanges the two pure coefficients, preserving their sum. The same first-order/ambient comparisons prove actual membership, rather than just availability of a representation.

Import the audited canonical splitting and target representation:

M_compact=H²(End₀H) ⊕ W H²(End₀H(−1)) ⊕ W² H²(End₀H(−2))
          =8ε⊕6ρ1⊕6ρ2.

Here W,W² are coefficient lines, not duals, and both are D5-trivial. Importing this representation is separate from proving polynomiality. Given U=1(B)⊕ρ1(A,C), Sym²U=2·1⊕ρ1⊕ρ2. There is no trivial target, so the AC and B² coefficients vanish. The AB,BC coefficients vanish on F0. Only the A²,C² coefficients survive, in the six copies of ρ2. If v=Q(1,0,0), then Q(F0)=v+Rv. Its two summands lie in distinct nontrivial rotation eigenspaces; hence this map is injective on the v eigenspace. The allowed original diagonal class therefore has exactly the stated six-dimensional bound, with 2 coordinates in twist −1 and 4 in twist −2.

This does not assert six nonzero/independent functions of the physical source. In fact a particular actual v could occupy a smaller subspace or be zero; no evaluation here distinguishes those possibilities.

## 5. Normalization and full splitting checked independently

At the cusp, x=t²,y=t³ intertwines V with t²∂t/2=−∂u/2. N∞ pulls back to O(1), since normalization is an isomorphism at infinity. Pullback of locally free transitions and their differential equations is legitimate despite nonflatness of normalization; no exact pullback assertion about arbitrary sheaves is needed.

The odd finite algebra summand changes O(−2)→O(−1), but the invariant summand map is O→O by the identity. By finite pushforward and projection formula, the actual invariant H² pullback is exactly the identity on H²(Y,M), not a dimension comparison or an unknown scalar. Thus it faithfully detects v. This does not identify noninvariant Ext¹ groups.

For the splitting, f=(−t,0), q=δf, a=Vf give c=Σβ_rs f_r cup q_s and D=−Σβ_rs π^{sℓ}f_r a_s V_ℓ. The Čech product rule gives δc=b and T−{c,−}=δD. The arrow gauge B_ij=exp_star(−h c_ij) changes the overlap derivation by −{c,−}, and the triple unit is killed through order two. Noncommutative corrections between two h-linear scalar units first occur in degree three; their conjugation effect on ordinary functions is degree two and is precisely the retained Hamiltonian term. Chart maps id+h²D_i then remove δD without changing the local Moyal product through order two.

For module transitions the actual transport is

u′=u−cg,
w′=w−cu+(c²/2)g−μ1(c,g),

followed by the chart correction D_i(g_ij) in w′. These terms are necessary for representative comparison. The resulting global-star problem must use this transported first boundary. Arbitrarily replacing it after normalization is not justified by cusp Ext¹ vanishing, because the noninvariant cohomology has changed. Thus faithful normalization and full splitting pass; automatic normalized quantizability does not follow.

## 6. Dependency DAG and source-provenance boundary

Imported nodes:

P0: actual normalized HM bundle and carrier E=f*H⊗N, not just Chern data.
P1: full compensated first-order obstruction vanishes at F0, separately in the two pair characters.
P2: stipulated pair-character Ext¹ groups vanish in characteristic zero.
P3: genuine binary/HM D5 action; canonical compact coefficient splitting; characteristic-zero target characters/ranks (including 2,10,20 and their D5 refinements).
P4: mixed obstruction vanishing, needed only to turn pure diagonal vanishing into the claimed complete diagonal existence criterion.

New/formal nodes:

P0 + actual PR16 formulas → fixed End target, fixed first-source base cocycle, universal b,T two-jet.
P1 + fixed first-source base cocycle → fixed first primitive and family first existence.
P2 → identification with stipulated boundaries and choice independence in the prescribed characters.
These nodes → polynomial pure class (direct degree argument above, or DVR extension plus normality).
P0 + marked factor deformations → invariant smooth characteristic-map zero.
P0 + P2 + P3 + characteristic-map zero → actual permutation and D5 covariance after first-order/root transport.
Polynomiality + covariance + P3 → six-coordinate diagonal restriction and Q(F0)=v+Rv.
Cusp root extension + normalization differential map + invariant identity → faithful normalized detection.
Explicit c,D gauges → equivalent global Moyal problem with transported boundary.
P4 + all six coordinates zero → original fixed-boundary diagonal second-order existence on an acyclic refinement.

Directly fetched in this review:

1. PR16 at c8aec970fd65a105f39f4e8aeb8a17f0f0053f89, research/hm/second-order-algebroid.md, returned blob a58834ab61e18a5dedd8a7bf20bec7121bfa9165. Sections 2–5 confirm the b,T formulas, λ=15/4, row equation, and all eight residual terms. Section 8 states the ambient-difference characteristic comparison after first-order identification and imports the Ext ranks. Its introduction says the global refinement comparison, first-order lift, and projected residual remain to be instantiated. Section 4 gives first cancellation using the premise ev_E(π)=−15Π id; it does not newly prove that equality from Chern classes alone. Thus P1/P2 are not independently certified by this source read. This is a provenance boundary, not a new gap in a theorem expressly conditional on P1/P2.
https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md

2. Actual carrier/atlas at 3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f, research/hm-carrier-and-atlas.md, returned blob fc0b0c7cf512d93c7a4ea976f986b7332b926f51. It explicitly gives E=f*H⊗N and the actual infinity-root frames, while warning that the atlas is not its quantization. This supplies P0, not P1 or any second-order vanishing.
https://github.com/Akilleez-QA/read-em-and-weep/blob/3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f/research/hm-carrier-and-atlas.md

Reviewed inputs: [branch-boundary-extension.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9412e435d6349ea5c9395711aa794e3dd003641/research/hm/null-branch-polynomial-extension/branch-boundary-extension.md), [branch-boundary-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9412e435d6349ea5c9395711aa794e3dd003641/research/hm/null-branch-polynomial-extension/branch-boundary-audit.md), [branch-covariance-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9412e435d6349ea5c9395711aa794e3dd003641/research/hm/null-branch-polynomial-extension/branch-covariance-next.md), [pure-target-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-target-next.md), [pure-square-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-square-next.md), [pure-ambient-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-ambient-audit.md), [cusp-normalization-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/2420001144ab274e51e32d60fb88f492e178115f/research/hm/null-cusp-normalization/cusp-normalization-next.md), [cusp-normalization-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/2420001144ab274e51e32d60fb88f492e178115f/research/hm/null-cusp-normalization/cusp-normalization-audit.md). I did not rerun physical ranks or independently reprove the HM stabilizer/normalizer and characteristic-zero representation premises P3. The finite-characteristic small certificate mentioned in the target report must not silently be relabeled as a fresh characteristic-zero rank proof by this review.

Bottom line: the previous smooth-locus denominator objection is genuinely closed under the imported premises. The normalized six-coordinate obstruction remains unevaluated.

## 7. Further check: global cochain gluing and novelty

After writing the independent degree argument, I inspected [cusp-base-source-formula.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/871422b59c159d9e607735f2e0f33b953c4ea2b9/research/hm/null-cusp-base-source/cusp-base-source-formula.md). Its §2 already contains the complete general-F eight-term expansion, including the correct Alexander–Whitney endpoints, and its §3 contains the derivative identities used above. Those eight formulas are not new here. The additional conclusion of this review is their **universal polynomial-cochain interpretation** with a fixed primitive, so they can prove polynomiality rather than depend on prior polynomiality for the cusp interpretation.

More explicitly, refine the fixed base cover by the standard coordinate charts and by trivializations of the odd O_i(−2) lines. U_p is chosen in the ordinary Čech complex of the actual pair-twisted bundle on this cover. Thus its component changes and its differential are already the genuine twisted ones; it is not an arbitrary list of matrices on a root-trivializing refinement. The extra odd-generator transition from y_i to z_i=y_i/x_i² is independent of A,B,C. Coordinate and tangent changes, the h/l transitions, their regular inverses on intersections, and the logarithmic derivative rules are likewise branch-independent. In each chart one uses the corresponding local odd generator and the global derivation formula, so finite-chart powers of 1/x are used only where they are regular.

On root-bearing loci, extra square-frame refinements add only ±1 transitions. The complete differentiated expression is unchanged under these constants and cancels its τ factors by the actual root cocycle. It therefore descends to the fixed base intersections. This is stronger than saying that any deck-invariant function on an arbitrary refinement automatically descends, which would not be justified.

The resulting chart expressions consist only of regular fixed base coefficients, branch-linear F,F′ and a, and the fixed U. Their half-root differential transformation rules give the same base Čech cochain on overlaps; alternatively their overlap equalities hold on dense S and hence as polynomial identities. No discriminant, A, C, F, y, or F′ is inverted to pass between these expressions. Consequently the universal coefficient cochains are regular over all Spec R, despite absence of an actual global root there. The same dense polynomial identity gives closure, since the fixed End Čech differential does not depend on F.

On A≠0 the actual infinity root exists, including at the cusp, so the universal cochain agrees with the actual full residual there, not merely with a polynomial extrapolation. P2 still supplies the comparison with the stipulated lift. This universal interpretation does not evaluate the earlier eight-term expression or remove its six unknown cohomology coordinates.
