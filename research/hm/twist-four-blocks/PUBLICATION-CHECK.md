# Final public-text publication check

Review date: 2026-10-20 UTC. Result: passes within the scope below.

## Exact reviewed bytes

- PROOF.md SHA-256: `279de6595a2baf83e218b8ea6f9a6e0c00a7999051cc6c02c53583d315117750`
- characters.py SHA-256: `43067ef9761001bf36ab4b682331631e9059d17e4828289779077c6b09e3f937`
- Imported twist-three-reduction/PROOF.md SHA-256: `114adf003fbf14dc8ea4cd597731fb7e0df4899dbf397e8fbc7732823179831c`
- Imported twist-three-reduction/INPUTS.md SHA-256: `834f2bfba295bd7405a91f2d106b6aabe4cbbae469cc48e238b2ea016fd62c15`
- Compared original PROOF.md SHA-256: `3b88b7758e1a0f4e8eebf0aa30ca890b3a3148eba42ca84b5b60cfb011ed9a3d`

These hashes bind the final public proof and imported refined inputs, not merely the historical mathematical audit. Any later change to a reviewed proof or input requires this check to be renewed.

## Checks performed

1. Read the complete public PROOF.md and compared it with the stated original. The sole proof-text publication change replaces private prerequisite paths with public companion links and the explicit primary-source input note. The theorem, arguments, numerical conclusions, and unresolved block-value boundary are unchanged.
2. Verified the refined cohomology inputs and A,C recovery in the separately checked INPUTS.md. They are not attributed to the numerical twist-two prerequisite. Checked the twist-zero line-cohomology complex and its representation-valued Euler identity identifying G, then the acyclic twist-minus-one complex identifying P. The twist-two complex identifies H¹F(2). Exactness and finite-group semisimplicity justify actual representation identifications rather than arbitrary interpretation of virtual characters.
3. Inspected HM Lemmas 2.4 and 3.3 and the printed-p.81 Appendix character table. Checked the tensor identities obtained by duality and Galois conjugation, and compared all nine character-table rows in characters.py with the primary table. Ran that small universal character check successfully: G has coefficient χ₅+W, P has coefficient χ₃, and its source, target, and trace-free-source decompositions match the proof. The check involves no bundle-map entries or selected HM instance.
4. Checked the two-entry twist-four E₁ page, dimensions 175 and 190, absence of other rows and higher differentials, and the canonical trace quotient. Its five inequivalent irreducibles have dimensions 20,25,10,20,30; multiplicity-freeness makes each kernel summand all-or-nothing. The target multiplicities agree with the proof and do not justify treating the block maps as scalars.
5. Checked the scalar dimension 70, Euler characteristic χB(4)=−85, and companion cohomology. Checked the cubic multiplication representation, absence of χ₆ from its image, and the resulting minimal-generator statement. Multiplication by one nonzero linear form is injective on cubic sections of the locally free bundle; the allowed image subset sums then give h⁰B(4)≥20 in the nonzero cubic branch.

## Limits

No mathematical correction to PROOF.md or characters.py was needed. This is an independent final-text and dependency review, not a formal proof certificate. It neither determines the five obstruction-map values nor proves quartic vanishing. It is independent of the kernel-semistability slice: the required companion is the twist-three reduction and its refined inputs. Numerical twist-two vanishing remains the pinned prerequisite in PROVENANCE.md and is not re-audited here. No selected source, cofactor, pairing, collision, or physical-obstruction instance was evaluated, and no external service was changed.
