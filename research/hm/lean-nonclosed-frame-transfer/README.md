# Typed nonclosed frame transfer — Lean checked

This supporting Lean unit formalizes the degree-zero component identity in
[null's PR816](https://github.com/Akilleez-QA/read-em-and-weep/blob/eed6010347fcebc21aef30413b0e1da3be68a9b4/research/hm/nonclosed-frame-transfer/NONCLOSED-FRAME-TRANSFER-EXACT-DEFECT.md):

```
M_b g_ba^C - g_ba^D M_a = p_b^D (T h_b^C + h_a^D T) i_a^C,
T = d_D E - E d_C.
```

The source and target degrees `-1,0,+1` and the four frame modules are
independent types over an arbitrary ring. Both endpoint components of `E`
remain arbitrary. The first defect term uses the source homotopy from
frame `b`; the second uses the target homotopy from frame `a`. Both signs
are positive, and Lean checks the composition types.

The core theorem needs only two degree-zero homotopy identities, a closed
source inclusion, and a closed target projection. It does not require
`E` to be closed, a retraction identity, differential-square-zero, or
normalized homotopies. These are minimal hypotheses for this component
calculation; authenticating a complete complex remains an application
obligation.

The three exported theorems are:

- `nonclosedFrameTransfer`: the full typed defect identity.
- `nonclosedFrameTransfer_closed`: the zero-defect limit when the two
  relevant components of `d_D E - E d_C` vanish.
- `nonclosedFrameTransfer_exactProjection`: closed inclusion and
  projection kill `d_D K + K d_C` for arbitrary typed degree-minus-one
  components `K`.

The closed limit is a local algebraic equality. This unit constructs no
global section, actual HM contraction, physical response, marking,
eigenframe, weight, or twist identification. It supplies no Lambda,
`qZ`, `beta4`, row-support or rank certificate, ladder calculation, or
repair of the original theorem. Global compatibility and the appropriate
cohomology vanishing require separate proofs; adjoint vanishing does not
eliminate scalar transfer.

## Verification

The source and final importing check both completed with exit code 0 under
Lean 4.34.1 and mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`.
The import check displays all three theorem types and their transitive
axiom reports. The core and closed-limit theorems use only `propext`,
`Classical.choice`, and `Quot.sound`; the exact-projection theorem uses
only `propext` and `Quot.sound`. There are no custom axioms or unfinished
proofs. See `REVIEW.md`, `AXIOMS.txt`, and `VERIFICATION.json`.

The source compile reports one nonblocking unused-simplifier warning for
`map_add` in the exact-projection proof. The first module attempt failed
solely because `Mathlib.Tactic.Abel.olean` was missing; that failure is
preserved. After the targeted cache fetch, the same source compiled.
The earlier importing check also passed; the final check was rerun after
changing only its leading status comment, with byte-identical output.

The targeted runs used one compiler thread, Lean's `-M1200` internal
ceiling, and the existing 60-second per-process CPU, 75-second wall, and
sampled 1.5 GiB process-group RSS guard. Final source and import-check
sampled peaks were 746,258,432 and 721,420,288 bytes. Their input hashes
were unchanged and cleanup completed. Sampled RSS is not a hard
address-space limit or a bound on between-sample overshoot.

An independent native reviewer checked the mathematics, exact source
deltas, and the root-run compiler/axiom evidence. Comparator and an
independent second kernel were not run. This verification covered the
targeted unit and its importing check, not the entire upstream library.

For replay in the repository after preparing its pinned dependencies,
from `lean/`:

```sh
lake build +OAI.AlgebraicGeometry.HorrocksMumford.NonclosedFrameTransfer
lake env lean --root=../research/hm/lean-nonclosed-frame-transfer ../research/hm/lean-nonclosed-frame-transfer/Check.lean
```

The targeted local build uses module mode and narrow imports. This
supporting result is not registered as a formalized main theorem in
`formalization.yaml`.
