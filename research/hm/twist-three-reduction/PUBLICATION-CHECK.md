# Final public-text publication check

Review date: 2026-10-20 UTC. Result: passes within the scope below.

## Exact reviewed bytes

- PROOF.md SHA-256: `114adf003fbf14dc8ea4cd597731fb7e0df4899dbf397e8fbc7732823179831c`
- INPUTS.md SHA-256: `834f2bfba295bd7405a91f2d106b6aabe4cbbae469cc48e238b2ea016fd62c15`
- Compared original PROOF.md SHA-256: `7f016e9e092e94d0f6f27bc39de2d5e367a4bfeb866bd72e74994f55fd6a18e7`

These hashes identify the final public proof and its new input note, not the earlier mathematical audit's target. Any later change to either reviewed file requires this check to be renewed.

## Checks performed

1. Read the full public PROOF.md and INPUTS.md and compared the proof against the stated original. The theorem, spectral-sequence argument, scalar cancellation, geometric evaluation argument, defect divisibility, and explicit unresolved boundary are preserved. Publication changes replace private dependency references and give an explicit primary-source derivation.
2. Inspected HM printed pp.72–74, including (4.2), (4.4), (4.6), (4.11), (4.12) and the cohomology table, with the normalization F=F_HM(−3). The separate H⁰F(3)=χ₄ and H¹F(3)=W′ assertions are present in (4.12), not inferred merely from their virtual difference. Inspected Decker's printed p.16 resolution and its section-module comparison. The input note correctly recovers C and A by twisting the section resolution by three: the isolated entries are C in total degree zero and A⊗H⁴O(−5) in total degree one; no spectral-sequence differential connects them. Triviality of H⁴O(−5) follows from N⊂SL₅.
3. Checked equivariant refinement by finite-group semisimplicity, determinant linearization, the twist-one complex identifying D, the three nonzero twist-three E₁ entries, the irreducible obstruction restriction, and the companion Euler characteristic. Refined A,C and cohomology labels are supplied by INPUTS.md, not claimed to follow from the numerical twist-two prerequisite.
4. Checked the rank-one and rank-two evaluation exclusions, the elementary two-plane Plücker argument, divisorial-defect exclusion using HM Theorem 3.5, and the degree-two Hilbert-polynomial argument giving 5|t. The semistability implication in this slice remains explicitly conditional.

## Corrections and limits

Corrected an ambiguous “last two” sentence in INPUTS.md to name exactly the two assertions supplied by (4.12), and named (4.2) for H²F(−2). Also removed a grammatical comma. No theorem or proof conclusion was changed.

This is a check of the final exposition, dependencies, and mathematical reasoning, not a formal proof certificate. The numerical twist-two vanishing remains the stated external prerequisite, pinned in PROVENANCE.md; its proof is not independently re-audited here. No cubic differential, selected HM instance, source membership, cofactor, pairing, or physical obstruction was evaluated. In particular the check does not select between h⁰B(3)=0 and 15. No external service was changed.
