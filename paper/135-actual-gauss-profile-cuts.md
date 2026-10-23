# 135. Direct actual Gauss visibility and profile-specific exclusions

**23 October 2026 · Frozen checkpoint through PR1135.** This chapter records a direct actual-embedding argument and its bounded profile consequences. It does not infer original Gauss compatibility from the different terminal-pencil coefficient presentation.

## Immutable proof sources

- [PR1129: full immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/d1238732f42df5c70ba4430e230428d2cf699bbe/research/hm/primary-gauss-visibility/PROOF.md), commit `d1238732f42df5c70ba4430e230428d2cf699bbe`.
- [PR1134: full immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/7cb2e260b2bcbac15df89612b6a2096263a9c89c/research/hm/primary-gauss-profile-reduction/PROOF.md), commit `7cb2e260b2bcbac15df89612b6a2096263a9c89c`.
- [PR1135: full immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/24e713fe352f4ff8f70cd2e86940afa70df99c5c/research/hm/gauss-two-shape-exclusion/PROOF.md), commit `24e713fe352f4ff8f70cd2e86940afa70df99c5c`.

## What the primary cubic block now proves

Let E be the actual saturated HM subbundle of the constant rank-30 plane-section bundle, β_E its second fundamental form, and A_q=E/ker β_E the actual locally free derivative quotient. Its sheaf image in the ambient quotient twisted by −2 need not be saturated. These are the original Gauss objects, not a replacement inclusion into the rank-54 coefficient presentation.

The canonical primary block C=(W′+T6)O(-3) is saturated in this same E, and every splitting degree of E/C is at most −2. For any nonzero coefficient line L⊂C, the quotient E/L has the same upper degree bound. If β_E killed L, its internal derivative would land in (E/L)(-2), but the relevant Hom space is zero. The resulting negative saturated horizontal line cannot lie in a constant bundle over C. Therefore

    W′+T6 ↪ H0(A_q(3)).

This is an **injection of coefficient/global-section spaces**, not fiberwise injectivity of a rank-eight bundle into A_q. It supplies no generic fiber-rank lower bound of eight. It also does not make the canonical negative-tail projector horizontal or compatible with positive or quadratic multiplication.

## A direct profile-(1,2) exclusion

PR1134 combines this visibility with the four necessary E types and an iterated section envelope. Successive actual Gauss kernels F_i give quotients J_i with injections J_i→A_q(-2i), even when later derivative ranks drop. Strict-top bounds and the kernel sequences yield, for r≥2,

    H0(E(r)) ≤ Σ_(i=0)^(r−2) H0(A_q(r−2i))

as a representation-multiplicity inequality.

Using the imported original ten-shape necessary theorem for maximal profile (1,2), degree obstructions remove the impossible negative quotient blocks, cubic visibility removes a missing-W′ shape, and the r=4 section envelope removes the remaining three shapes. Thus **profile (1,2) is excluded**, under those pinned profile-specific necessity hypotheses. The argument does not invoke the later composite four-pair ledger or identify independent primal and dual witnesses.

This does not by itself establish that the listed maximal profiles exhaust every relevant rank-three possibility. Profile (1,1) is still open.

## Profile (2,1): exact D-type and four remaining original rows

PR1134 forces E to have the exact D-type

    E=D O(-2)+(W′+T6)O(-3)+V O(-4)+O(-8)

under maximal profile (2,1). Quotient degrees and cubic visibility remove several shapes; the exceptional non-D possibility is excluded by the r=10 section envelope, where four trivial source constituents would have to fit into three target constituents. Eight original rows remain at that intermediate checkpoint.

PR1135 then excludes both actual quotient shapes

    O(-8)+O(4)+O(6),       O(-8)+W O(5),

without assuming a later Gauss rank or choosing a determinant defect. The actual D row is proved onto its indicated target, and its cubic channels are nonzero. A saturated graph argument forces an independent T6 channel. Hence the full map on cubic sections is an isomorphism, forcing the derivative kernel to be (2V+2P)O(-4). Strict-top would then inject two V constituents into a target containing only one, a contradiction. The V O(-4) source rows are retained, not discarded because they have no cubic sections.

Removing original rows 3/4 and 6/7 leaves exactly these **four necessary profile-(2,1) rows at this checkpoint**:

| Original index | Actual quotient shape A_q | Original determinant defect |
|---|---|---:|
| 2 | O(-8)+O(2)+O(16) | 0 |
| 5 | O(-8)+O(4)+O(16) | 0 |
| 9 | O(-8)+O(6)+O(16) | 0 |
| 10 | O(-8)+W′O(9) | 0 |

Each requires the same D-type E. They are necessary leftovers, not actual realizations. In these defect-zero rows the original dual quotient is B_q=A_q* (-2). Profile (2,1) remains open; later endpoint arguments are outside this frozen checkpoint.

## Three different counts of four

1. **Four general necessary E types:** the source-independent formal bundle classification of Chapter 132. None has been selected globally.
2. **Four residual profile-(2,1) rows:** original indices 2, 5, 9, 10 above. All require D-type under that additional profile hypothesis; they are not four different E types.
3. **Four historical source pairs:** the old ledger using E10, E13 and E14. Those specified types are incompatible with the newer primary-terminal theorem and are not an active compatible frontier.

The visibility test rejects 30 labels in the fixed historical 182-row list, while PR1135's two-shape theorem rejects 14 historical rows across profiles (1,1) and (2,1). These are overlapping-context historical-list cuts, not new live campaign totals, completion percentages or counts to add to the four-row statement.

## Evidence and remaining boundary

The three complete immutable proofs were read. Independent scoped review of PR1134 and PR1135 found no gap relative to their pinned inputs, authenticated sixteen retained originals, replayed both exact checkers and independently checked the required representation arithmetic. This is supporting verification, not a new reduction or proof-assistant certificate. Their geometric statements depend on pinned actual-bundle, strict-top and profile-specific necessity theorems; row arithmetic and exact character checks do not independently prove geometric coverage. The checkpoint distinguishes a direct actual Gauss-quotient bridge from the still-unproved stronger positive/Q/Gauss compatibility of canonical projectors.

No full maximal-profile coverage, global rank-three exclusion, maximal-rank theorem, original obstruction value, full-adjoint invertibility, smoothing, algebraicity or complete repair follows. Earlier chapters, archive 52 and the fixed 19:16 UTC v0.3 PDF remain unchanged. No new PDF is supplied.
