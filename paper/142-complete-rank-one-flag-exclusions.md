# 142. Two further actual shapes excluded by complete rank-one Gauss flags

**Craig Ward · 23 October 2026 · Representation-valued flag obstruction; profile (1,1) remains open**

## New exclusions and their limits

The [complete rank-one flag theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/b6c3581c1a6df25ea72a776f9d6cf2082bd73461/research/hm/rank-one-flag-obstruction/PROOF.md) excludes both actual quotient shapes

    A = W′ O(-3) + O(16),
    A = W′ O(-5) + O(16)

for every one of the four necessary actual primary source types when the maximal rank-three plateau has backward length k=1. In particular it applies in profile (1,1), independently of the upper quotient and historical row labels. It does not close that profile or the original repair.

Together with [chapter 141's two exclusions](141-terminal-doublet-two-shape-exclusion.md), this excludes all four A shapes singled out by the forced-factorization part of the P-source certificate, PR1155. That certificate's nineteen records were the residual of specified tests on a fixed historical list, not a live total. No current remaining-case count or percentage follows. Other-profile exhaustion and the global rank-three bridge also remain separate obligations.

## What the predecessor did and did not prove

The [scalar-endpoint theorem, PR1158](https://github.com/Akilleez-QA/read-em-and-weep/blob/bfbb3fe3dd0659e69b6b818ec86038a62ebd2675/research/hm/forced-scalar-endpoints/PROOF.md) assumed the P source and A=W′ O(-r)+O(16), r=3 or 5, with k=1. It proved that the actual derivative of K=E⁻ has rank one and coherent image exactly the displayed O(14) in A(-2). It did **not** exclude either target.

Its actual-map argument fills that scalar line: the cubic top W′ O(-3) has a nonzero scalar map, and any common invariant divisor would have degree at most 10, below the minimum nonempty orbit size 12. A rank-two derivative is then ruled out by coherent-image degree constraints for r=5 and a signed quartic obstruction for r=3. This gives the exact quotient K/K⁻=O(14), not merely its saturation or a guessed line image.

The new proof uses that statement as an explicit predecessor and follows the entire backward flag. Its exclusions must not be backdated into PR1158.

## Why the conclusion covers all four actual sources

The ambient is the actual constant thirty-dimensional plane-section bundle, not the coefficient presentation of dimension 54. The actual saturated E has rank 17 and degree -54, and A=E/K is its locally free Gauss quotient.

All four necessary source types D, P, V and Z have χ_G(E(4))=3V+3P+2D. Cubic-kernel vanishing would make

    H0(A(2)) + χ_G(A(4)) − (3V+3P+2D)

an actual cokernel character plus H1(K(4)), hence genuine. Its values for r=3 and r=5 are respectively

    1 + 2A_std + D + P − V,
    1 + 2A_std + D − V.

The negative V multiplicity forbids vanishing and removes V and Z. For D, a nonzero cubic kernel forces a nonzero actual O(2) image in A. The negative doublet is inaccessible by degree; the scalar component would require an invariant in Sym¹⁴W=A_std+V+P+D, which has none. D is impossible. Only P remains, with H0(K(3))=W′, so the scalar-endpoint predecessor applies. Here A_std=Sym²W is the standard three-dimensional representation and is distinct from V and from the quotient bundle A.

## Fourteen line quotients, including the terminal one

Set F₀=K and F_(j+1)=ker β_(F_j), always using the actual saturated Gauss kernel in the same constant ambient. The first quotient Q₀=F₀/F₁ is O(14). Each subsequent derivative lands in Q_(j−1)(-2), so its rank is at most one. It cannot vanish while F_j is nonzero: a horizontal saturated bundle in a constant bundle would be constant, contrary to negativity. Thus the rank is exactly one at every stage until rank 14 is exhausted:

    F₀ ⊃ F₁ ⊃ ... ⊃ F₁₄=0,
    rank F_j=14−j,       Q_j=F_j/F_(j+1)=O(b_j),  0≤j≤13.

Strict-top gives maxdeg F_j≤-3-j. Every kernel is saturated; no finite-length terminal piece is silently dropped. These are coherent-image quotients, not replacements by their saturations in derivative targets. No horizontal splitting is assumed.

Perfectness of the group removes any extra one-dimensional character on the line quotients. The actual nonzero injections Q_(j+1)→Q_j(-2), including the terminal injection, give invariant effective vanishing divisors of degrees δ_j and the recurrence

    b₀=14,       b_(j+1)=b_j−2−δ_j,       0≤j≤12.

## Weighted invariant defects leave exactly five and two patterns

Projective A5 orbit sizes are 12, 20, 30 and 60. Each δ_j is therefore a nonnegative sum of 12, 20 and 30; 60 is redundant. This is a necessary divisor-degree condition, not an assertion that any pattern is realized.

The undeflected sequence 14,12,...,-12 has sum 14. Since deg K=-70+2r, degree additivity forces

    Σ_(j=0)^12 (13−j)δ_j = 84−2r.

The totals are 78 for r=3 and 74 for r=5. Reduction modulo four forces a single weighted 30-atom, at weight one. The remaining equations leave exactly these necessary patterns, with omitted δ_j zero:

| r | Nonzero deficits |
| --- | --- |
| 3 | δ₉=12, δ₁₂=30 |
| 3 | δ₁₀=12, δ₁₂=42 |
| 3 | δ₁₁=24, δ₁₂=30 |
| 3 | δ₁₁=12, δ₁₂=54 |
| 3 | δ₁₂=78 |
| 5 | δ₁₁=12, δ₁₂=50 |
| 5 | δ₁₂=74 |

This is exhaustive for the bounded necessary weighted-defect equation, not an enumeration of actual instances or campaign rows.

## Equality of representations fails although every dimension matches

Exact sequences in the complete flag require the representation-ring equality

    R_flag = χ_G(E) − χ_G(A) − Σ_(j=0)^13 χ_G(O(b_j)) = 0.

All Euler terms are signed, retaining H1. For the five r=3 patterns, in the order above, the residuals are

    1+2A_std−V−P,
    1+2A_std−V−P,
    1+2A_std−V−P,
    1+A_std−P,
    A_std−V.

For the two r=5 patterns they are

    2+2A_std−2P,
    1+A_std−P.

Every residual is nonzero because the irreducible characters form a basis. Every residual nevertheless has ordinary dimension zero. Thus ordinary ranks, degrees and Euler dimensions all match, but exact equivariant Euler additivity fails.

This is an **equality obstruction**, not an unsupported claim that a nongenuine virtual character cannot appear where arbitrary virtual characters are allowed. In particular, the distinct three-dimensional representations A_std and V cannot cancel as representations merely because their dimensions agree. The failure eliminates all seven necessary flags and therefore both targets.

## Separate short check for r=5 only

The minimum orbit degree already forces δ₀,...,δ₆=0. A strict-top injection at F₇, twisted by 10, gives another genuine-character necessity. Its value is

    r=5:  −1+2A_std+3V+4P+4D,
    r=3:     2A_std+4V+4P+4D.

The negative trivial multiplicity independently excludes r=5. The r=3 character is genuine and gives no exclusion; the complete-flag equality argument supplies that case. These two logical tests are kept separate.

## Verification and current boundary

The proof is bound to SHA256 `a75ab590e7f7e2ecdf4e89661f54c5edb38e9e0fe9a60c061321b048ec5d180e`. Independent written review checked the all-source reduction, predecessor scope, saturated fourteen-line termination, orbit-degree recurrence, all seven representation equalities and the early-envelope indexing. Eleven complete public originals were freshly authenticated, including the full immutable PR1158 proof.

The author verifier passes 1,003 explicit checks plus 81 character-module checks; the independent evaluator passes 509. Normal and optimized Python outputs agree. The independent evaluator uses exact class characters and a closed-binomial symmetric-power formula, separately enumerates the bounded deficit patterns, and reproduces all signed residuals. These controls support the written proof, not proof-assistant verification of the full geometric dependency chain.

No actual source coefficient, selected parameter, point, jet, matrix or instance rank was evaluated; no historical list was regenerated and no stopped experiment restarted. Profile (1,1), wider coverage and the original repair remain open. Chapter 141 and the delivered v0.3 PDF are unchanged historical snapshots.
