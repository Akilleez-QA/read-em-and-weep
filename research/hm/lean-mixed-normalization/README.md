# Mixed normalization adapter — Lean checked

This unit formalizes the conditional normalization identities in
[PR866](https://github.com/Akilleez-QA/read-em-and-weep/blob/25b1d2927294fffbc393e6ac2285f5a58cfd6c60/research/hm/physical-source-normalization/PROOF.md)
in one aligned ambient frame. It uses independent global cochain, global
target, local map, projected coefficient, trace, and norm modules over a
ring. The physical maps and comparison certificates remain supplied inputs.

The source rows `LA` and `LB` accept only `range d`. Their argument is the
certified corrected source `t = ⟨S − qW, hT⟩`, never an uncertified `S`.
The local comparison `delta = coneTau.comp R4` has a full local domain,
so its cone evaluation on `loc S` is legal without source-image membership.

The adapter assumes a comparison on every image element,
`LB(t) − LA(t) = delta(loc(t.val))`, cone vanishing for `qW`, the lower-jet
change `yB − yA = eta`, and a common lower norm datum `Q`. It imports
[PR873's heterogeneous response definition](https://github.com/Akilleez-QA/read-em-and-weep/blob/73359dd41f3729cfb6da2207b6d282a3489294f2/lean/OAI/AlgebraicGeometry/HorrocksMumford/HeterogeneousAffineSourceResponse.lean)
to set

```text
rhoAA = Q + mu(yA − LA(t))
rhoAB = Q + mu(yA − LB(t))
rhoBB = Q + mu(yB − LB(t)).
```

Six theorems establish:

- Full-range comparison from supplied global rows, their factorizations,
  and their comparison on every global cochain.
- The source-only cone identity `eta = delta(loc S)`.
- Paired cancellation `yB − LB(t) = yA − LA(t)` and `rhoBB = rhoAA`.
- The mixed defect `rhoAB − rhoAA = −mu(eta)` and compensation
  `rhoAB + mu(eta) = rhoAA`.
- Equality `rhoAB = rhoAA` exactly when `eta ∈ ker mu`, without injectivity.
- Equality exactly when `eta = 0`, only under explicit `Function.Injective mu`.

This keeps trace and norm coefficients distinct and performs no division by
a multiplier. Injectivity concerns regular coefficient sections when the
unit is applied physically; it is not fiberwise cancellation at source zeros.
Removing `qW` from the cone defect does not remove it from the response-row
input or erase its next-boundary contribution.

The unit does not construct actual contractions, global source rows, ambient
frame alignment, physical trace extraction, or tensor compatibility. The
unchanged `Q` and lower-jet identities are assumptions to authenticate.
It does not prove correct physical normalization or global gluing. A compatible
global nonzero error may pass overlap tests. Full source-submodule calibration
is not formalized, and no main-theorem repair or actual HM exclusion is claimed.

## Verification and replay

The final source and separate importing `Check.lean` passed under Lean 4.34.1
and mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. All six theorem axiom
closures contain only `propext`, `Classical.choice`, and `Quot.sound`.
The source compile emitted no warnings. The only change from the independently
reviewed draft was its stale status comment; all executable source and the
check file remained unchanged. See `REVIEW.md`, `AXIOMS.txt`, and
`VERIFICATION.json` for exact bindings.

The runs used one compiler thread, Lean's `-M1200`, a 60-second per-process
CPU limit, a 75-second wall watchdog, and a sampled 1.5 GiB process-group RSS
threshold. Source and import-check sampled peaks were 858,963,968 and
794,263,552 bytes. Recorded inputs were unchanged and cleanup completed.
Sampled RSS is not a hard address-space bound or a guarantee against
between-sample overshoot. The independent reviewer inspected these root-run
receipts without rerunning the compiler. Comparator and an independent second
kernel were not run.

This unit depends on PR873's source being present. After preparing the pinned
repository dependencies, replay from `lean/`:

```sh
lake build +OAI.AlgebraicGeometry.HorrocksMumford.MixedNormalizationAdapter
lake env lean --root=../research/hm/lean-mixed-normalization ../research/hm/lean-mixed-normalization/Check.lean
```

The archived runs used an isolated source/build layout and exact reviewed
dependency artifacts. These repository replay commands were not separately
executed. This supporting result is not registered as a formalized main theorem
in `formalization.yaml`.
