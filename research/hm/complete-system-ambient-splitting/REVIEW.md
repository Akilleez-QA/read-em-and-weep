# Independent review: complete-system constant splitting

Verdict: PASS within the explicitly conditional application scope. This is a
review of the frozen proof and reproducible checker, not a proof-assistant
certificate and not a profile-(1,1) exclusion.

## Frozen artifacts

- `PROOF.md`: SHA256 `4c18ff833e06f88aa4d5985b05b0600c52dd02c8a660931396a64bf4cdf51f68`.
- `verify.py`: SHA256 `1cff50d8cc8998e6c318c461799e12b06ef79b80ca305aba9b3125bd5aa96708`.
- `RESULT.json`: SHA256 `a465e53adea1bdcbe3de743972ff4b6fbb3fb402231531bc7653fbd7414ef286`.

The reviewer read the whole proof, checker, reproduction instructions, and both
full prerequisite-context proofs. Independent immutable GitHub fetches confirmed
that `inputs/pr1138.md` and `inputs/pr1142.md` match the public files byte for byte:

- PR1138, commit `c69f97aaf00e116e3a8abebf19a8e02868c4f7c4`,
  `research/hm/gauss-profile21-closure/PROOF.md`, Git blob
  `49a0b288cb3adc9c7e6df6f29f96ce46896f51e4`, SHA256
  `be3e6ef741268733f9ddc02405a3d8e030742d8ff3f2378570a0f0d1fe4d1328`.
- PR1142, commit `df2fd3d35dac577d7f1e1c4d51fe68b1fcc824ad`,
  `research/hm/gauss-cubic-kernel-exclusions/PROOF.md`, Git blob
  `c5351a3a3e630b0725da49d926171ac966d545c3`, SHA256
  `f2c23c8f4188952d807e920affcbc6eaf09a92af1d436885db444133457c5d30`.

Public PR1 coordination was read through comment 6375020455. That comment
reserves the actual height-seven application and subsequent residual exclusion
to its author. The present packet does not replace that work.

## Mathematical checks

1. The coefficient map of the chosen section has a left inverse after composing
   with the quotient and the inverse complete coefficient map. It therefore
   identifies its coefficient span with the full quotient space. This proves a
   constant complement, not merely a bundle complement. The argument is basis
   independent and applies in every nonnegative degree, not just tested degrees.
2. The direct sum is an equality of actual embedded subbundles. The quotient
   decomposition makes residual saturation immediate from local freeness. The
   constant shear removes all homogeneous degree-e coefficients together, so its
   derivative has no extra connection term. This justifies the block diagonal
   second fundamental form and actual sheaf-kernel decomposition globally.
3. The complete rational-normal line is immersive for e>0 on both affine charts.
   Its sheaf kernel is zero and its derivative contributes precisely one to the
   generic rank. The e=0 exception is stated correctly.
4. Averaging a section preserves its right-inverse property for a finite group
   in characteristic zero. Its coefficient span is then invariant. The section
   and constant complement are not canonical; no arbitrary Birkhoff projection
   is being made horizontal.
5. In the conditional degree-eight application, annihilation gives a projection
   into O(-8). A zero projection would put a nonzero constant space inside Q*,
   contradicting H0(Q*)=0. Ordinary degree vanishing kills the maps from all
   source blocks except the unique O(-8); its nonzero scalar is an isomorphism.
   Thus the required split surjection really follows under the stated actual
   osculating-containment hypotheses.
6. Removing that line gives rank 16, degree -46 in a constant space of dimension
   21. Under actual generic derivative rank three, the residual rank is two.
   If the actual derivative quotient has the separately assumed splitting
   O(-8)+O(2)+O(16), cancellation gives residual quotient O(2)+O(16). This is
   cancellation after an established actual direct-sum identity, not a claim
   about a preferred pre-existing projection.
7. The height-seven completeness paragraph is explicitly conditional on the
   actual equality chain. Eight independent derivative directions and the
   semisimple decomposition Sym8 W=P+D force the full nine-dimensional
   coefficient system. Saturation extends generic osculating containment.
   Neither the stronger profile-(2,1) top bound nor defect zero is inferred
   from the assumed splitting of the primal quotient.

## Reproduction

Both `python verify.py` and `python -O verify.py` were executed independently.
Their complete outputs agree with each other and `RESULT.json`: 78 formal
symbolic cases, 17,709 passing checks. All eight entries in `INPUTS.json` were
verified by byte count, SHA256, and Git blob SHA1. The checker uses explicit
failure conditions, so optimized Python does not suppress the checks.

The symbolic tests cover coefficient shear, inverse, differentiation, residual
block preservation, two-chart immersion, and an incomplete-system negative
control. They do not certify the bundle argument by themselves. No selected
actual source coefficient, parameter, point, jet, or instance-rank experiment
was run. No additional private test is needed to reproduce this review.

## Boundary

The universal lemma and its stated conditional application pass. Establishing
the actual profile-(1,1) equality hypotheses and excluding its residual core
remain separate obligations. This review proves no complete profile exclusion,
global rank-three exclusion, full-adjoint invertibility, or original repair.
