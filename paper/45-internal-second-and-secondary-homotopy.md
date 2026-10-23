# Internal second vanishing and secondary homotopy

**Subsequent update through PR982:** PR982 now constructs the internal third in a canonical two-dimensional space and proves equivalence of its nonvanishing with generic original-fourth nonvanishing. PR985 subsequently selects r=0 and all original generic higher vanishings under the same hypotheses; see [chapter 48](48-collective-radical-images.md). The internal second vanishing and the unselected secondary scalar ν recorded here remain unchanged. See [chapter 46](46-internal-cubic-gate-and-ambient-geometry.md).

**Craig Ward · 23 October 2026 · Update through PR980**

Throughout this chapter, assume an actual source126 Type II occurrence and compatibility of its entire two-dimensional radical J with Q. This hypothesis remains unproved. Let S be its common-annihilator complex, M the original complex and T the quotient. The necessary source-dual relation remains **four pairs across three labels**.

## 1. A new internal vanishing, not a rediscovery of original third vanishing

[PR979](https://github.com/Akilleez-QA/read-em-and-weep/blob/db4c20c05f18d5e2494d99eb4c359828446919c9/research/hm/source126-typeII-internal-second/PROOF.md) proves that the **internal second Bockstein of S vanishes identically** on its surviving D kernel, in every parameter direction. This is distinct from the original second symbol of M, which is a nonzero family on A, and from the **original third Bockstein**, whose already established vanishing is imported as a premise.

PR973 gives internal first symbol b_S,a(k,h)=λak and its rank-two cokernel bundle E, with presentation 0→A O(-1)→D O→E→0. Fixed equivariant corrections define the internal second symbol globally as a bundle map s:D O(-2)→E, independently of correction choices modulo the internal first image.

The equivariant Hom space for s has dimension two. Naturality along the quotient first-kernel line κ:O(-5)→D O(-1) imposes sκ(-1)=0. The restriction map is nonzero with one-dimensional target, so this confines s to a one-dimensional subspace. This is a genuine restriction on surviving first cycles, not an assertion that naturality kills every original D vector without a preceding-cycle condition.

A separate saturation and representation argument proves that every nonzero equivariant quadratic map D O(-2)→E is generically onto. Comparing internal corrections with the original third differential gives

η β₃,M,a = −b̄_T,a δ⁻¹ s_a

on surviving D, with b̄_T the quotient first symbol followed by the quotient by the original second-symbol image. On the dense rank-constant open, b̄_T has rank one on the rank-two E. Imported original-third vanishing forces im(s) into its kernel line. A nonzero s would instead have generic rank two, so s=0 globally.

The **new progress** is the internal comparison, its Hom-space restriction and resulting internal second vanishing. The earlier six-axis classification, local square structure and original-third vanishing are dependencies, not new achievements of this update. No internal third or original fourth value is determined here.

## 2. A canonical homotopy on a radical kernel line

[PR980](https://github.com/Akilleez-QA/read-em-and-weep/blob/3dd68c99b9dfd85fe10cc327c2fa95c24bc185f5/research/hm/source126-typeII-secondary-homotopy/PROOF.md) defines the one-dimensional line

J0=ker[J→Hom_G(H⁰(T),H⁰(S))].

For j∈J0, its descended chain map T→S is zero on Q-cohomology. It has a **unique equivariant degree-minus-one homotopy** h_j:T¹→S⁰ satisfying j⁰=h_jQ_T and j¹=Q_Sh_j. Existence follows from equivariant splitting of finite-dimensional complexes; uniqueness follows because the difference of two homotopies factors through Hom_G(P,A+D)=0. Thus auxiliary choices do not change h_j.

For each negative quadratic a define K⁰=h_jL_T,a and K¹=L_S,a h_j. This is a chain map for the entire same-direction family Q+tL_a. The two displayed components have no minus sign. No simultaneous chain-map identity between unrelated directions a and b is asserted.

On Q-cohomology, first-symbol naturality reads b_S,a k⁰=k¹b_T,a. The potential k¹ channel is a scalar times the invariant bilinear adjoint of b_T. On every nonzero square, b_T is onto P. A nonzero adjoint composite would have rank four, but the other side factors through A and has rank at most three. Hence **k¹=0**. Injectivity of multiplication by a on A then also forces the **A component of k⁰ to vanish**.

## 3. One secondary channel remains, with ν unselected

The sole remaining component is

k⁰_j,a(h)=(0,ν(j){a,h}₁) in A+D,

where ν is a linear functional on J0 and {a,h}₁ is the first transvectant on binary quartics. No theorem here selects ν=0 or ν≠0. Nonzero j implies nonzero h_j, but taking its secondary map and then cohomology may annihilate it; faithful endpoint action does not settle ν.

If ν(j)≠0, this D-channel has rank four for every nonzero a and kernel C·a². Its universal bundle sequence is

0→O(-3)→D O(-1)→D O→O(2)→0.

If ν(j)=0, both secondary induced cohomology maps vanish. These are conditional alternatives, not asserted actual realizations.

**Higher-naturality boundary:** a later differential is defined only on classes surviving all earlier differentials. Any use of this chain map on later pages must restrict to those cycles and respect their quotients. In particular, one cannot apply an unprocessed higher-naturality equation to every D input and thereby claim ν vanishes or that full-radical compatibility is impossible.

## 4. Evidence and remaining gates

Independent reviews report **58 exact checks for PR979** and **111 for PR980**, passing in ordinary and optimized modes. They authenticate pinned inputs and test representation arithmetic, correction signs, Hom-complex identities and universal transvectant ranks. The actual geometric and sheaf comparisons come from the written arguments; these are not actual-instance evaluations or proof-assistant verification of the complete dependency chain.

Under the stated hypothesis, S now has nonzero first multiplication on A, zero first symbol on D and zero internal second symbol on D. The first unresolved internal order is at least three. The secondary scalar ν, actual full-radical occurrence, original fourth and later obstructions, and full repair remain unresolved. No pending two-dimensional third/fourth gate is incorporated, and neither a source pair nor a stable label is removed.
