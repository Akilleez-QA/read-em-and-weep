# Independent review: all-non-V quadratic-annihilator reduction

Reviewed 2026-10-23 UTC, independently of the author's self-check.

- PROOF.md SHA-256: `8b86340503bca7e74a1a903d9648cb2521470b817f13c4e6e59c7a23e97b20e2`
- verify.py SHA-256: `2fc2ed4209650a7991553d51b944ba3010e60cd487ce1d0b46728a3258e8117b`
- INPUTS.json SHA-256: `b16fe423dbe0522ca3e04f4e733f2cf1b2ff9bd14fb6d48e5851329282b09874`

Verdict: PASS for the stated conditional generalization.

Read the whole proof and checker and compared the extension with the
previously checked exact794,795,950 and957 mathematical interfaces.
The decisive new observation is valid: NC/I embeds as a genuine subpencil
of N/I, with initial space V+D and final space zero for every non-V j.
Therefore every ordered composite B_m A_l annihilates its initial space.
This argument is independent of the middle quotient, which is zero in
regular directions and T in the exceptional mixed direction.

The theorem correctly uses only this embedded eight-dimensional space.
It does not claim its first arrows vanish, identify it with a common
first-arrow kernel in the exceptional case, or assert it is the maximal
common kernel of the quadratic family. It does not use or require the
exceptional contraction normal-form theorem or its extension splitting.

All subsequent steps need only quadratic annihilation: the restriction
of barQ to Z has rank3 or8 by its kernel A+D and Schur's lemma; the
perturbation restriction remains constant; polynomial triangular
cancellation preserves the filtration; and the rank3 case retains D[0].
Thus the active dimensions, invariant kernels/cokernels, and ranks remain
24->20 with A+D/P and rank16, or D[0] plus24->25 with A/P and rank21.
No three-vertex or full-module splitting is inferred from these operations.

The multivariable rank argument is also unchanged and valid. Over the
fraction field of C[[z1,z2,z3]], the permanent five-dimensional quotient
kernel and the invertible nine-block give original rank at most36.
The polynomial-ring injection implies every37-minor vanishes identically
on Q+Sym²W, even where that nine-block may specialize singular. This is
not a claim that the nine-block is invertible everywhere.

Executed `python verify.py` and `python -O verify.py` independently:
168 checks pass with identical JSON output. All four exact input SHA-256
and Git blob digests pass. The synthetic negative controls genuinely have
nonzero first arrows into a six-dimensional middle space, while every
composite vanishes. Their purpose and the coefficientwise shear tests are
accurately bounded; no actual-source data is evaluated.

The pure V line remains outside this argument because NC4/I4=D is not
zero. Neither compatible-line existence nor which restriction rank occurs
is proved. There is no catalogue cut or completed original proof repair.
This review is supporting verification, not a separate new deduction or
proof-assistant certificate.
