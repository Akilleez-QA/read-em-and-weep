# Reciprocal symmetry audit for the actual pure obstruction

## Verdict

Accepted, under the already imported HM reversal isomorphism and pair-character Ext¹ vanishing, and using the accepted theorem ev_E(HH²(X)_0)=0. Simultaneous reciprocal transformation on all four elliptic factors, together with h↦−h, preserves the actual deck-invariant pure quadratic obstruction class. The required line twist is an algebraic flat two-torsion twist and admits an exact differential-algebroid module equivalence. It is not disposed of merely by identifying End bundles or by citing the characteristic-map theorem.

This proves an R-even constraint, not vanishing. With the separately supplied 32-dimensional target and traces −2,−2,−4 on its 2-,10-,20-dimensional summands, the permitted invariant subspace has dimension (32−8)/2=12. Those target and character calculations are imported, not independently recalculated here.

No smooth-87-dimensional-family or arbitrary-first-order-boundary independence premise is needed: the torsion-line comparison can be made deck-equivariant, so the given pair-character Ext¹ vanishing suffices.

## 1. Actual automorphism and base action

On C:y²=x³−x put p=(0,0) and

r(x,y)=(1/x, i y/x²).

Substitution verifies the curve equation. The rational map extends to an automorphism of the smooth projective curve, interchanges ∞ and p, and has r²(x,y)=(x,−y). Also r*(dx/y)=i dx/y. The pullback of the invariant vector field V dual to dx/y is −iV, so simultaneous pullback on either pair bivector gives r*π_p=−π_p.

The base action is x↦1/x, hence ordinary reversal on the unscaled quartic coefficients. This is precisely R(e_j)=e_(4−j), not the base action x↦−x of CM_i. Indeed t_p(x,y)=(−1/x,y/x²), CM_i(x,y)=(−x,i y), and r=t_p∘CM_i. A no-go for the uncompensated CM base action therefore does not refute this symmetry: its base automorphism and root-line effect are different. No previously rejected CM identification is reused.

By the imported actual HM reversal isomorphism, r_X*f*H≅f*H. Meanwhile r*O_C(∞)=O_C(p), and hence

r_X*E ≅ E⊗L,  L=⊠_{j=1}^4 O_C(p−∞).

Since div(x)=2p−2∞, L²≅O_X. This line is not assumed trivial, nor descended to a trivial line on the quotient. The identification End(E⊗L)=End(E) is canonical, but by itself would not establish equality of quantization obstructions.

## 2. Algebraic torsion-line comparison, including the noncentral data

Choose an algebraic trivialization L²≅O_X and let Y→X be its finite étale μ₂ torsor of square-root frames. Characteristic zero is essential here. On Y, L has a tautological horizontal frame; on the double overlap the frame ratios are locally constant ±1. Derivations extend uniquely across étale morphisms, so the differential products and overlap derivations of PR16 pull back algebraically to Y. They annihilate these transition constants.

Consequently multiplication by a horizontal transition constant intertwines the entire algebroid module equation, not merely its commutative part:

F_ij(G_jk)⋆G_ij=A_ijk⋆G_ik.

If G_ij is replaced by ε_ij G_ij, every term has the common factor ε_jk ε_ij=ε_ik; derivatives of ε vanish. The triple unit A need not be central. Scalars ±1 commute with it and with every matrix, and F fixes them. Thus the terms T(g)g and −μ₁(b,g), as well as μ₂, b² and all first-lift terms, are retained exactly.

This is an actual invertible bimodule/tensor equivalence for the same algebroid, reducing to tensoring by L. One fully algebraic construction is the sign eigensummand of p_*A_Y, where A_Y is the pulled-back local differential algebra: its underlying O_X[h]/h³-module is L[h]/h³. Multiplication supplies its inverse equivalence, checked on the faithfully flat étale cover where it is the ordinary rank-one bimodule. The overlap maps and triple-unit compatibility descend with it. This proves effective algebraic descent, not only an analytic flat-local-system comparison or an equality after a nonfaithful pullback.

Equivalently L has the unique algebraic flat connection for which L²≅O is horizontal. Changing the chosen square trivialization by a nonzero scalar leaves this connection unchanged. Each deck involution preserves it: the induced action on L² differs from the chosen trivialization by a global constant, whose logarithmic derivative is zero. Hence tensor equivalence is compatible with the natural deck linearisations. A constant scalar ambiguity in these lifts acts trivially on End(E), and introduces no extra character in the obstruction representation.

Under the canonical End identification, normalized residuals and their classes agree after tensor transport. This supplies exactly the line-twist step that the bare HH² comparison does not supply.

## 3. Full first-order ambient identification

The pinned PR16 §§1–4 first-order ambient class is the compensated class ξ=π+B, equivalently product μ₁ and scalar gerbe b=−B. Its displayed representative is

b=(15/4)(q₁∪q₂+q₃∪q₄), q=y/x.

There is no first-order overlap derivation: F=id+h²T. On H¹(O_C), r* acts by −i, since Serre duality pairs it with H⁰(ω_C), on which r* acts by i. Thus each pair component of [b] transforms by (−i)²=−1. This also follows from the actual Čech representative, but the cover permutation must be included: the raw function identity r*q=iq does not by itself describe the action on its Čech class because r exchanges the two charts.

Both the bivector and gerbe parts therefore change sign. The compensating h↦−h identifies the full first-order ambient class with itself, separately for P and Q. No unsupported inference from Poisson equivariance alone is made.

On a common algebraic refinement, equality of these first-order classes supplies a first-order algebroid equivalence. At this order the product is already matched; any discrepancy in the scalar gerbe representative is a scalar Čech coboundary. Its primitive can be chosen in the appropriate pair character by averaging over the finite deck group. This gives an actual equivariant first-order identification, with its induced second-order terms retained. It does not claim that the original raw T or chosen scalar primitive is literally r-invariant.

## 4. First-order module boundary and second-order ambient comparison

Pull back the actual first-order module by r, replace h by −h, use the HM symmetry isomorphism, and undo the flat line L by the equivalence above. Transport through the first-order ambient identification. The result has the same reduction E and is another pair-character first-order lift over the original first-order ambient.

The difference from the prescribed u_P+u_Q is an End-valued Čech one-cocycle in the two pair characters. The imported Ext¹(E,E)_P=Ext¹(E,E)_Q=0 removes it by a reduction-preserving first-order gauge. Averaging supplies homogeneous primitives. Its induced second-order correction must be retained; doing so changes obstruction representatives only by coboundaries. Therefore the original module boundary is identified, not silently replaced by an arbitrary Ext¹ choice.

At this point the transported and original second-order ambients are valid extensions of the same identified first-order ambient and module boundary. Their remaining difference is a total Hochschild two-cocycle η, including product, overlap and triple-unit changes. The obstruction difference is ev_E([η]). By the accepted source-specific result,

pr₀ ev_E([η])=ev_E(pr₀[η])=0.

The conclusion uses this theorem only after the line twist and first-order data have been handled. It never substitutes it for those steps. It also does not require η to be represented only by a bidifferential product correction.

Functoriality now gives R·o_even=o_even because h² is unchanged. The same argument applies to each separate pure coefficient if s↦−s,t↦−t is used in the two-parameter presentation. The actual quadratic source includes all noncentral terms throughout.

## 5. Representation and group-law qualifications

The action on the obstruction coefficient is induced by r_X*End(E)≅End(E), obtained from the HM isomorphism and the canonical cancellation of L. The line twist cannot supply an additional scalar reflection character on End. Projective scalar ambiguities in an HM lift also disappear under conjugation.

Although r has order four upstairs, its square is the simultaneous deck involution. On the deck-invariant target this acts trivially. Thus the induced operation there is an involution and its fixed-space dimension is (dimension+trace)/2. This requires the actual equivariant target decomposition and its trace conventions, not an arbitrary identification of the underlying vector space with a 32-dimensional model.

The claim is therefore: the canonical pure obstruction lies in the +1 eigenspace of the specified reciprocal-induced involution. It is not a D5-invariance claim for the full branch-dependent pure ambient, is not a negative-sign cancellation of the P and Q terms, and does not establish zero obstruction or a full second-order module lift.

## Sources and limitations

Directly inspected pinned PR16 source:
https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md

The actual carrier and root line are recorded in the prior independently audited source:
https://github.com/Akilleez-QA/read-em-and-weep/blob/3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f/research/hm-carrier-and-atlas.md

The accepted characteristic-map and first-boundary audit was read in [pure-square-next.md](pure-square-next.md) and [pure-ambient-audit.md](pure-ambient-audit.md). The scope distinction between mixed and pure lifts was read in [second-order-implication-audit.md](second-order-implication-audit.md). HM reversal preservation and the target dimensions/traces were supplied as premises for this task. The torsion-line equivalence and the reciprocal symmetry argument above are formal deductions, not claims already stated in those sources.



## Cross-check of the companion target report

The reciprocal comparison in [pure-target-next.md](pure-target-next.md) §4 is accepted with the detailed algebraic and equivariance justifications above. Its intrinsic check of the gerbe sign is especially useful: θ=c₁(N) is fixed by r because r*N=N⊗L and L is torsion. Therefore B=15 ι_π(θ²)/2 transforms by −1 together with π. This avoids all raw Čech q/cover conventions. Its statement that the constant two-dimensional projection vanishes follows from its separately established M₀=2ε and the accepted R-even comparison; no additional obstruction evaluation is needed.
