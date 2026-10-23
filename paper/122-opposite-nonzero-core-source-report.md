# Opposite nonzero-gate core: intrinsic row criteria

**23 October 2026 · Full-source report of mr. slop's PR1098, not an independent reproof**

[Immutable full proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/4be12ae9328dc8a69e2323e0c71b3efe6eaad303/research/hm/nonzero-branch-core/PROOF.md), blob `9c87a48028e61401851e710e0d6acf302f9b8d2c`.

Assume the existing opposite μ≠0 branch. The actual core is 0→L8⊕L2→Y6→Q→0, with L8=O(−8), L2=O(−2), and target extension of S O(1) by W′ O(5). These opposite Q and coefficients are not the invariant quadratic map or pure-V lift channels.

Let θ:L2→S O(1) be the actual source projection. The proof establishes **θ=0 iff row9**, with Q=O(12)⊕V O(4). It derives this through actual quotients and the universal degree-nine S evaluation kernel, not a row selected from a character list.

If θ≠0, a unique compatible equivariant target lift gives the inherited one-source presentation

    0 → O(−8) --(α,β)→ W′ O(5) ⊕ A O(2) → Q → 0.

Its intrinsic channels classify the remaining alternatives:

- α=0 iff row14, Q=W′ O(5)⊕W′ O(7).
- β=0 iff row10, Q=O(18)⊕A O(2).
- Both nonzero iff row15, Q=P O(6).

They cannot vanish simultaneously. Universal degree-ten A and degree-nine S systems are proved by orbit-size bounds, kernel slopes and representation obstructions. In the both-nonzero case the actual pushout class is nonzero in a one-dimensional Ext space, represented by the tensor-Euler extension. Remaining graph components are retained by the uniquely compatible lift; ordinary splitting uniqueness is not asserted.

Only the universal statements of the earlier zero-μ proof are imported, not its branch assumption or actual coefficients. No μ, θ, channel value, C row, source pair, marked-line position or actual realization is selected. These conditional criteria supplement the [zero-gate source report](117-opposite-small-cores-source-report.md), without claiming arbitrary normal forms occur or resolving the positive map.
