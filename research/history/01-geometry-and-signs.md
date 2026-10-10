# Reconstruction 01: withdrawal, local geometry and corrected signs
Period: 2026-10-10, approximately 02:10–02:36 UTC.

This is a reconstruction of recorded mathematical work. Approximate times identify checkpoints, not exact start times. Historical calculations below were not freshly rerun while preparing this document. “Checked” describes the recorded scope of the check; it is not formal verification or external review.

## 1. Establish the common dependency

The investigation selected the split-Weil-eightfold construction as the first shared bottleneck for three withdrawn claims:
- [Split Weil eightfolds](https://github.com/openai/math/blob/main/preprints/Algebraicity-of-Weil-classes-on-split-abelian-eightfolds-September-18-2026/README.md)
- [Kuga–Satake correspondences](https://github.com/openai/math/blob/main/preprints/Algebraicity-of-Kuga-Satake-Correspondences-for-K3-Surfaces-October-3-2026/README.md)
- [Products of K3 surfaces](https://github.com/openai/math/blob/main/preprints/The-rational-Hodge-conjecture-for-products-of-K3-surfaces-October-4-2026/README.md)

The archived eightfold source is pinned to adc7f1241b42e322a6451854ab7e4b4c146bf78a, in its build/sections/03-topology.tex. Relevant labels are top:negative-doubles, top:negative-index and top:trace-signs.

The withdrawal notice, reread during reconstruction, states that reverse traces contribute −1 rather than +1: I(f₁)=−m becomes −2m rather than zero. It withdraws the proof, not the theorem.

A replacement must preserve the represented class να, orientation/spin, injective H₂ and H₆ maps, the required cohomology surjection/kernel, and the relevant grading. Merely producing an immersion is insufficient.

## 2. First candidate inventory, around 02:11

The record contains twenty proposed routes. Proposal is not execution:

1. Audit oriented cusp determinants.
2. Replace the immersion directly using EEMS minimal-double results.
3. Tune Euler characteristic by connected sums.
4. Use a negative-Euler-characteristic stabilization region.
5. Match actions and cancel by Whitney moves.
6. Cross-surgeries between several oriented branes.
7. Replace odd-index requirements by exclusion of ordered degree 2.
8. Solve the immersed Maurer–Cartan equation.
9. Use local-system or bulk parameters.
10. Use twisted complexes of graph branes.
11. Build a tropical Lagrangian and smooth it.
12. Use a singular/conical brane category.
13. Use a fourfold secant-object route.
14. Construct the Kuga–Satake correspondence directly through moduli.
15. Salvage restricted/high-Picard K3 cases.
16. Spread cycles from dense CM loci.
17. Degenerate to lower-dimensional Weil factors.
18. Construct an algebraic perfect object directly.
19. State a conditional dependency theorem.
20. Produce a rigorous obstruction report.

Routes 4, 7 and 13 were selected for concrete tests. Routes without a later test remain ideas.

## 3. Direct EEMS replacement rejected

A proposed immediate replacement confused conventions. EEMS gives Euclidean I=(−1)^(n/2)χ/2; the target manuscript uses I=(α²−χ)/2 in dimension eight. The apparent sign repair did not survive translation between conventions.

Primary foundation reread during reconstruction: [EEMS, Corollary 1.3 and its proof; Lemma 2.1](https://arxiv.org/pdf/1303.0588). The EEMS theorem controls double points under its hypotheses; it does not automatically retain all target homology and grading conditions.

## 4. Negative-Euler stabilization and weaker grading gate, around 02:17

Research calculation: every nonempty compact stabilization superlevel region contains an interior maximum. Negative Euler characteristic can repair a net count but leaves an ordinary forward-trace point with the bad local grading.

The fixed-phase calculation used q=(u=eᵗ,x), p=(z,uy), cusp coordinate s=y₁ and determinant s+s³+iu. The lower cusp sheet differs by +1 from the canonical graph grading. Forward ordered indices are {2,n−2}; reverse indices are {1,n−1}. In dimension eight, {2,6} retains a degree-2 curvature generator.

[Akaho–Joyce, Propositions 12.2 and 13.10](https://people.maths.ox.ac.uk/joyce/AkahoJoyce.pdf) provides the abstract exact-Calabi–Yau gate excluding ordered degree 2. It does not make this particular cusp satisfy it. Arbitrary index shifts are not legitimate.

Connected sum with S³×S⁵ changes χ by −2 while retaining useful H₂/H₆ data, but does not remove the bad refill point. The nonorientable-surgery/orientation-cover escape also fails: invariance under an orientation-reversing deck involution forces rational top-class pushforward zero.

## 5. Essential-circle surgery and the action-order correction, by 02:36

A proposed Hicks k=1 surgery on an added essential null-image S¹ was pursued because it could kill H₁ without adding H₂.

An initial rejection asserted that its positive-action degree differed from the forward cusp. That assertion was withdrawn after recomputing with common conventions:
- ω=dq∧dp and λ=−p dq;
- q₊→q₋ has degree 6;
- the reverse positive-action branch has degree 2;
- Hicks k=1 matches the forward cusp.

Do not resurrect the mismatch or claim that dense periods must reverse the bad lobe’s action.

The unresolved gate is actual full finite-area surgery support. A framed isotropic core and adjustable periods do not supply an embedded neighborhood with all required compatibility. A separate global obstruction test was recorded using #³(S¹×S⁷)#(S⁴×S⁴), χ=−2, an EEMS one-point immersion and a FOOO closed-Lagrangian obstruction. Its exact FOOO citation is not recovered here, so this reconstruction does not promote it to a standalone sourced theorem.

Sources: [Hicks v3](https://arxiv.org/abs/2102.10197), [Eliashberg–Murphy](https://arxiv.org/pdf/1303.0586), [EEMS](https://arxiv.org/pdf/1303.0588).

## Outcome

The unchanged local repair was not obtained. No original algebraicity statement was disproved. The algebraic carrier branch became the main alternative; new global geometric constructions remained open.
