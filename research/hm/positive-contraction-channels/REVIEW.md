# Independent review: positive contraction channels

## Verdict

PASS for the stated structural theorem and its conditional application, relative to the pinned input statements. No mathematical correction is required. The review does not establish an actual source realization, select a residual mechanism, evaluate actual channel coefficients, or exclude residual-large tau=0.

## Exact reviewed files

SHA-256:

- PROOF.md: 207062874c434f9c0638ead6a5455f51089a5eac0b9c12ea2e7bfc91f2da9a76
- verify.py: 398f1fb9a00bbe04bb508659ffa9298c435c879f95544d2c4b3de4c6dcbe765b
- input1106.md: 64b8b659df676bbca022d3e3bbfbfd0dba2c2fa2a82a3681d70b737d57d8db7d
- input931.md: 2f135afb909aa11483274a1eae49cbb3aa311f36b66b478bbeab59ad38072f8b
- input933.md: 6dcdb17796696fe627489d865ba0a5e2913305dd9c5cbe07d87b7453c9d6b0e1

- INPUTS.json: 1a2349a4f42e78af7f20a02100e507f2efec308679bf00a03182c5df9b9fb005

The proof and checker hashes match the final revisions supplied for review. The checker additionally verifies each input file against both its manifest SHA-256 and Git blob hash. Local copies of the dependencies were inspected for the imported statements and typing. Remote Git provenance and the full recursive dependency closure were not independently reauthenticated in this review.

## Mathematical review

1. Over C, the multiplicity-free decomposition V tensor V = 1 + V + D gives precisely three equivariant triple-to-V tensors. The displayed scalar, alternating, and traceless-symmetric tensors span the corresponding channel spaces. There is no additional finite-group invariant at this tensor order.
2. Commutativity is equivalent to c0 = c1 + 5c2/3. The invariant contraction is c0 - 2c1 + 10c2/3, hence -c1 + 5c2 under commutativity.
3. Every nonzero commuting projected tensor has at least two effective channels. Equivariance, irreducibility, and multiplicity-freeness imply the stated rank possibilities 4, 6, 8, 9 for the restricted first arrow. A zero effective coefficient does not imply the first-arrow channel vanishes, and the proof correctly preserves that distinction.
4. Nonzero tensor plus zero invariant contraction forces the ratio (20/3, 5, 1), so the first arrow is injective. If the first arrow is not injective, zero contraction is equivalent to the projected tensor being zero. Injectivity alone says nothing about whether that contraction vanishes.
5. For the companion, put A=x(y dot z), B=y(x dot z), C=z(x dot y). The symmetric tensor is alpha(A+B)+beta C. Its positive-coordinate D component is alpha[A+B-(2/3)C]. This universal tensor is nonzero, so the D component vanishes exactly when alpha=0. Combined with commutativity, this gives the nonzero pure-invariant ratio (2/3,-1,1). Thus exactly two effective intermediate channels force both positive-quadratic components to be nonzero.
6. The sharpness example has first-arrow image 1+V of dimension 4, symmetric two-step composition, and contraction -Id. It defines a genuine module over Sym(V): use the three listed graded pieces, the displayed degree-one actions, and zero actions outside them. The only nontrivial pairwise degree-one commutator is on the source, where it vanishes by the displayed symmetry. This example demonstrates sharpness for the local representation problem only, not for the actual HM/source setting.
7. The dependency usage is properly conditional. PR1106 supplies the marked actual source and the isomorphism e0 Q2 on it under residual-large tau=0. PR931 and PR933 supply the actual positive arrows and their ordinary quadratic composition. The additional isotypical projection acts identically on the unique V target. No extension of the negative projector to the intermediate positive space is used.

## Checker execution

Executed in the review directory:

- python verify.py: PASS, 76 checks.
- python -O verify.py: PASS, 76 checks.

The checker uses explicit exceptions rather than assert, so optimization does not remove checks. Basis-triple verification proves the tested universal multilinear identities. These are universal representation checks, not evaluated actual-instance matrices. The checker does not independently prove the imported representation decomposition, independently establish remote provenance, or test the companion statement; those matters are covered by the written proof and review, subject to the dependency scope above.

## Final revision check

The final proof incorporates both editorial clarifications raised during review: the invariant volume is explicitly normalized compatibly with the symmetric form, and the companion refers to the already projected T without adding a redundant p. The checker has six additional input-integrity checks. All were inspected and the final checker was rerun in normal and optimized modes.

No publication or external communication was performed.
