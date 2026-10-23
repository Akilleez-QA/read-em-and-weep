# Actual small opposite cores and intrinsic channel criteria

**23 October 2026 · Full-source and diff report of mr. slop's PR1092 and PR1095**

These are attributed source readings, not independent reproofs. Opposite bundles Q and Q3 below are not invariant quadratic maps or the generated endpoint spaces. Their scalar μ and channel coordinates are not identified with pure-V transfer coefficients.

## PR1092: one actual target and two unselected branches

[Immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/7df3f6d6cd19964d5576954790de192d7f8ef8e1/research/hm/small-opposite-core/PROOF.md), blob `5a90ecfefb8ac339a5ee4cf8812bfaea6ea715e3`.

Actual kernels of the canonical C→O(2) quotient produce a common rank-six target Y6, with extension 0→W′ O(5)→Y6→S O(1)→0. It splits equivariantly but its one-dimensional splitting ambiguity is retained. Global generation of the same intrinsic rank-four degree-24 bundle Q forces the full L3→W O(−1) projection nonzero. Its restriction to the canonical W O(−1) source is the intrinsic multiplicity-line map μ.

If μ≠0, actual kernels give

    0 → O(−8) ⊕ M1⊗O(−2) → Y6 → Q → 0.

If μ=0, its nonzero Euler factor gives

    0 → O(−8) ⊕ M0⊗W O(−1) → Y6 → Q → J_r⊗O → 0.

The final trivial quotient is unique up to scalar; its intrinsic kernel Q3 has rank three and degree 24. Its source presentation is obtained by replacing the last two terms by Q3→0, retaining all actual maps and multiplicity lines.

The equivalence μ=0 iff the older λ=0 is proved through Hom_G(Q,O) for the **same actual Q**, not equal characters or numerical identification of scalar coordinates. Neither branch is selected and no older source embedding is identified by representation labels.

## PR1095: a one-source core only in the zero-μ branch

[Immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/893845c20e964035dd2446897211814f184f93bd/research/hm/one-source-opposite-core/PROOF.md), blob `186043a2d37e07641803e68de6bb0048b49bc6a0`.

Assume μ=0. The actual W O(−1) source must project nontrivially into S O(1), since otherwise an equal-rank fiberwise injection into W′ O(5) contradicts degrees. Its universal saturated quotient is W O(3). Hom/Ext vanishings make its compatible equivariant lift unique, canonically relative to the actual source map. Quotienting gives

    0 → O(−8) --(α,β)→ W′ O(5) ⊕ W O(3) → Q3 → 0.

The named target factors are intrinsic to these maps. Both channel Hom spaces are one-dimensional, with uniformly basepoint-free nonzero generators: the degree-eleven W system has no possible invariant base divisor, and a degree-twelve base divisor in the degree-thirteen W′ system would leave an impossible W′⊂W.

The exact conditional criteria are:

| Intrinsic channel pattern | Q3 type | Opposite C row |
|---|---|---|
| α=0 | W′ O(5) ⊕ O(14) | 17 |
| β=0 | O(18) ⊕ W O(3) | 18 |
| α≠0 and β≠0 | V O(8) | 20 |

Simultaneous zero is impossible by the source injection. The both-nonzero case is established through the actual pushout extension: its class is the nonzero connecting image of α in a one-dimensional Ext space, represented by the nonsplit sextic sequence twisted by O(8). It is not selected by matching a character list alone.

No μ branch, α/β value, actual C row, source pair or marked-line position is selected or asserted realized. The inherited weighted map is preserved. These opposite-pencil criteria are separate from terminal incidence for the pure-V fourth lift, and neither resolves the surviving positive component.
