# 136. Actual maximal profile (2,1) is excluded

**Checkpoint: 23 October 2026 · PR1138 · Scope frozen at the profile-(2,1) closure**

## Result and source

[Mr. Slop's immutable PR1138 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/c69f97aaf00e116e3a8abebf19a8e02868c4f7c4/research/hm/gauss-profile21-closure/PROOF.md) excludes all four original profile-(2,1) rows that remained at the [PR1135 checkpoint](135-actual-gauss-profile-cuts.md): indices **2, 5, 9, 10**. Together with the pinned direct reductions of PR1134 and PR1135, this excludes the actual maximal profile (2,1), using the original written thirteen-pair necessity theorem. It does not rely on treating a later finite ledger as exhaustive geometry.

Maximal profile (1,2) was separately excluded. Profile (1,1) is not excluded here. A reduction of every hypothetical generic-rank-three object to that one profile still requires the separate theorem excluding the other six profiles and its applicability. No global rank-three exclusion or complete original repair follows from this checkpoint.

## Six endpoint height partitions, not an infinite scan

Work in the original constant ambient with S=Q*, rank S=13, degree S=−54 and top S≤−2. For profile (2,1), its dual endpoint L=S⁻ has rank 10 and derivative rank at most two. Set F₀=S, F₁=L and Fⱼ₊₁=Fⱼ⁻, using saturated actual derivative kernels; put Gⱼ=Fⱼ/Fⱼ₊₁ and G₀=B=S/L.

The genuine quotient maps inject Gⱼ into B(−2j), including across ramification. Their ranks qⱼ are weakly decreasing and at most two. No nonzero negative saturated subbundle of the constant ambient can be horizontal, so the chain terminates and the ranks sum to 10.

Writing hᵢ=#{j:qⱼ≥i} gives h₁≥h₂≥0 and h₁+h₂=10. Thus the only height pairs are **(5,5), (6,4), (7,3), (8,2), (9,1), (10,0)**. For the two highest ordinary degrees λ₁,λ₂ of B, exterior powers of the actual injections give

    deg L ≤ Σᵢ₌₁² [hᵢ λᵢ − hᵢ(hᵢ+1)].

This is a finite universal endpoint bound, not an evaluation of selected coefficients, actual jets or historical enumeration.

| Original row | B | Actual degree of L | Maximum endpoint capacity | Result |
|---|---|---:|---:|---|
| 2 | O(6)+O(−4)+O(−18) | −38 | −38 | Equality analysis required |
| 5 | O(6)+O(−6)+O(−18) | −36 | −42 | Excluded strictly |
| 9 | O(6)+O(−8)+O(−18) | −34 | −46 | Excluded strictly |
| 10 | O(6)+W′O(−11) | −38 | −49 | Excluded strictly |

## Equality makes the derivative images rigid

For row 2, equality occurs only at (h₁,h₂)=(7,3) or (8,2). Every determinant bound must then be equality. Since B has distinct ordinary degrees 6, −4, −18, each relevant top exterior-power summand is unique. Its determinant is a nonzero constant, while all lower components vanish. Consequently the actual composite derivative image is the corresponding top flag everywhere, not merely a bundle with the same Euler character.

The intermediate derivative arrows agree with the top-flag inclusions. The final saturated line is C=O(6−2h), where h=h₁. If h=7 this is O(−8), contradicting the iterative strict-top bound top F₇≤−9. Hence h=8 and C=O(−10).

Its successive derivatives have nonzero leading components in new graded steps. Lower derivatives cannot cancel those components, so the first eight derivative steps produce at least nine independent directions inside S.

## The full polynomial system and its apolar annihilator

The actual inclusion C→H*O has an equivariant coefficient map Sym¹⁰W→H*. Since Sym¹⁰W=A_std+V+D has constituent dimensions 3, 3, 5, every proper equivariant quotient has dimension at most eight. The required nine-dimensional coefficient image therefore forces the entire **11-dimensional** polynomial system to embed as a genuine constant subspace V₀.

The eighth osculating bundle of the full degree-ten system is

    U=Sym⁸W O(−2)=(P+D)O(−2),

of rank nine. Its fiber is ℓ² Sym⁸W. Generic containment in S extends everywhere because S is saturated in the original constant ambient. Under the invariant apolar pairing, the annihilator of ℓ² Sym⁸W is ℓ⁹W, giving the bundle U⊥=W O(−9) inside V₀*O.

The earlier direct reduction forces the same actual source

    E=D O(−2)+(W′+T)O(−3)+V O(−4)+O(−8).

Every ordinary degree of E is at least −8. Hence Hom(E,W O(−9))=0 even without equivariance. Since E annihilates S, its projection into V₀*O factors through U⊥ and must vanish. Thus the entire constant V₀O annihilates E and lies in S, contradicting H⁰(S)=0. This excludes row 2 and finishes the four-row closure.

## What is closed and what remains

The thirteen original necessary profile-(2,1) rows are excluded in disjoint groups: **five by PR1134, four by PR1135, four by PR1138**. The necessity theorem, not the count, supplies geometric coverage within that profile.

The four rows recorded in chapter 135 are now a historical PR1135 frontier, not four current possibilities. They were distinct from the four general necessary E types and the four historical source pairs; none of those different counts can be substituted for another. This proof forces D-type under its now-contradictory profile-(2,1) premise, not as a realized choice of the actual source.

Open boundaries remain profile (1,1), other-profile exhaustion and the broader actual-source/global rank-three bridge. No full-adjoint invertibility, smoothing, algebraicity, selected obstruction value or complete repair is claimed. Independent review found no gap relative to ten matched immutable inputs and replayed the bounded verifier; that is supporting verification, not proof-assistant certification of the entire project.

The delivered Craig Ward v0.3 PDF remains the unchanged historical **23 October 2026, 19:16 UTC** snapshot. This chapter updates the living Markdown account only.
