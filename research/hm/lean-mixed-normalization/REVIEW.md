# Independent review: mixed normalization adapter

**PASS** for the final source and separate imported-module axiom check.
The reviewer checked the statement types, mathematical derivations, written
source correspondence, final comment delta, dependency copies, and completed
root-run evidence. No compiler was rerun by the reviewer. Comparator and an
independent second kernel were not run.

## Exact files and dependency

All digests are SHA-256; paths and receipt names are portable logical names.

| Artifact | Digest |
| --- | --- |
| `lean/OAI/AlgebraicGeometry/HorrocksMumford/MixedNormalizationAdapter.lean` | `af884b6f80630db9702d92573b57e832c96e9f1224c63d4e5596056a37430963` |
| `Check.lean` | `51d417b774819e22c528df61c5d58edbb4640c4339a24481fed431ec03308592` |
| Compiled `MixedNormalizationAdapter.olean` | `af660db4d29480c2fb3311659bc4fb1b58fadd33bc43da3a80e4fd2a77d4ab9d` |
| Compiled `MixedNormalizationAdapter.olean.private` | `fb835285f23fb61536feaa609611cbe78024eb22980f3d4f40f42b454f616cf1` |
| Original static review | `4211f6466b3e79c434ac456e1216a5c407900a93784e0e7decb819963fc07025` |
| Historical producer `SCOPE.md` | `877da8e4791d65b7b50f7bd4cd29cb3e323453c12ea0ebdd3e37ecb1f4e81be0` |
| PR866 written proof | `a7f6afe41fe569cb9a061a047b1d0a140fd198950cda6fe3bace6978f3cf0b14` |
| G dependency source | `8d0e2257a05d2c88b3414edf588e93ca6f98277b665f912b2772342fafa39ac3` |

The written input is PR866 commit
`25b1d2927294fffbc393e6ac2285f5a58cfd6c60`, path
`research/hm/physical-source-normalization/PROOF.md`. Its saved 12,197 bytes
reproduce Git blob `d6430f3ea8ee841278ed4ce815721b61bf2fdc3d`. The reviewer
read this exact source and the reconnaissance report; primary-source
authentication is inherited from that report's GitHub fetch, not a second
network fetch by this review.

The sole OAI dependency is
`OAI.AlgebraicGeometry.HorrocksMumford.HeterogeneousAffineSourceResponse`,
published at PR873 commit `73359dd41f3729cfb6da2207b6d282a3489294f2`.
Its source is unchanged from the independently reviewed G unit. All five
dependency build artifacts copied into J's build root were compared byte for
byte with that reviewed build:

| Dependency artifact | Digest |
| --- | --- |
| `HeterogeneousAffineSourceResponse.olean` | `834ba20e09b906bc8edb542124a26e68d2c5ae188f0ad1f692c1d95952a73565` |
| `.olean.private` | `2a40d2e83f22c8d3d027d47ca08c05e732c9ed5078fd242647f1abdc29407b14` |
| `.olean.server` | `151c3d0149c1a3d47757744f51082f026548d06efe5d4f20f3ca7656abaf2e6b` |
| `.ir` | `a27f9f36c307997f81871b9fd3f4639f0894c606a31b84fa908bd4995815ee85` |
| `.ir.sig` | `ec165f2fbe8b7f955c7a270fb9f7110dbd474b35bb60cd21a88852d4120cdbd8` |

The compile receipt records G's `.olean` and `.olean.private`; the import
receipt records its `.olean`. The other copied artifacts were independently
compared after the runs. G's response definition is reused directly rather
than copied or replaced. Its overlap theorem is not duplicated.

## Domain and mathematical audit

The six independently universe-polymorphic modules are `C0`, `Dg`, `Dloc`,
`V4`, `Tr`, and `Nm`, over a ring. The `MixedNormalizationAdapter` record
retains `hT : S - qW ∈ LinearMap.range d` and forms exactly that subtype as
the source `t`. Every source-row evaluation is on an image element. No proof
silently replaces `LA(S-qW)` or `LB(S-qW)` by a row evaluated on `S`.

The local map `R4` accepts all `Dloc`, so `delta = coneTau.comp R4` may be
evaluated on `loc S`. The `eta_source` proof expands linearity twice and uses
the explicit cone-vanishing certificate for `qW`. This legal source-only
cone identity has no consequence that `S` lies in the differential image.

The full image comparison certificate is explicit in the record. Separately,
`mixedNormalization_range_comparison` derives it from supplied global rows
`ellA`, `ellB`, their factorizations through `d`, and their comparison on every
global cochain. Pinned `LinearMap.mem_range` supplies a witness with equation
`d x = t.val`; `Subtype.ext` identifies its range-restricted image with `t`.
Both row factorizations then give the result. This does not construct the
global rows or infer global factorization from local primitives.

The lower-jet certificate and full comparison give the two equal changes

```
yB - yA = eta,
LB(t) - LA(t) = eta.
```

Their cancellation has exactly the sign in PR866 (N11):
`yB-LB(t) = yA-LA(t)`. The common supplied `Q` and imported definition
`affineSourceNormResponse mu L Q y t = Q + mu(y-L(t))` then prove paired
response equality. Common `Q` is represented by one field; its physical
invariance is not derived from arbitrary per-twist data.

For the mixed response the lower term stays `yA`, so subtraction gives
`rhoAB-rhoAA = -mu(LB(t)-LA(t)) = -mu(eta)`, the negative sign of (N1).
Adding `mu(eta)` gives the compensating term. Trace and norm coefficients
remain distinct; only the supplied linear map `mu` relates them.

Equality of responses is equivalent to `mu(eta)=0`, hence to membership in
`ker mu`, without an injectivity premise. Only the final theorem adds
`Function.Injective mu` and concludes `eta=0`. It neither divides by a
multiplier nor claims fiberwise injectivity on its zero divisor.

The final source and all six theorem types were inspected. Compilation
establishes their elaboration, and the importing check resolves every
exported name. The check prints axiom closures, not theorem types. The only
direct imports are G and `Mathlib.Algebra.Module.Submodule.Range`; G publicly
provides the kernel and abelian-group tactic APIs. Module mode, public imports,
the exposed public section, and disabled auto-implicit variables are retained.
No `sorry`, `admit`, custom axiom, unsafe declaration, or native decision
procedure occurs.

## Final delta and completed evidence

The independently reviewed original source digest was
`85bd243133cb58bf7e793a50900b1b718fa34f2ca060f286bb5fca7ce60ba297`.
The only change replaces the leading prose `UNCOMPILED. PR866, commit` with
`Supporting algebra from PR866, commit`. Reversing that text replacement
reproduces the original bytes. Definitions, structures, theorem statements,
proofs, imports, and the complete `Check.lean` are unchanged. The original
draft, scope, and static review remain preserved. There were no failed J
compile or import attempts in the supplied evidence.

The environment is Lean 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`, and mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The inspected launcher
`run-module.py`, digest
`ce5051e14a6d7b174195c9c949c91ea1c79e9c2ab49f9237c56da4eb48397a69`,
selects the pinned compiler and search path and passes `-j1 -M1200`.

| Run | Exit | CPU seconds | Wall seconds | Sampled group peak RSS, bytes |
| --- | ---: | ---: | ---: | ---: |
| `compile-0001` | 0 | 2.554848 | 6.542043083 | 858963968 |
| `axioms-0001` | 0 | 1.310761 | 4.513744375 | 794263552 |

Their original receipt digests are respectively
`d99a76a9c0e4fd6590c27edb35e7d003571c2f56674a7f351a32dd863902b8c1`
and `3fed3da8e2fbf0ba9ba9a5d11e807b2079aee41699b20b96b13c04396db8e11f`.
Both report success, unchanged recorded input hashes, completed cleanup, and
no termination signals. The reviewer recomputed every recorded input's digest
and byte count. The compile binds the final source and G artifacts; the
separate importing check binds the unchanged check, the exact compiled J
module, and G's `.olean`.

The compile stdout/stderr and import-check stderr are empty, digest
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
The axiom output digest is
`d277c817e6dedb95695f7e509b80059092ff5b75deaf8bac6cc1d3daa6bf509a`.
Each of these six names appears exactly once, with closure exactly
`[propext, Classical.choice, Quot.sound]`:

- `OAI.HorrocksMumford.mixedNormalization_range_comparison`
- `OAI.HorrocksMumford.MixedNormalizationAdapter.eta_source`
- `OAI.HorrocksMumford.MixedNormalizationAdapter.paired_cancellation`
- `OAI.HorrocksMumford.MixedNormalizationAdapter.mixed_defect`
- `OAI.HorrocksMumford.MixedNormalizationAdapter.mixed_eq_iff_mem_ker`
- `OAI.HorrocksMumford.MixedNormalizationAdapter.mixed_eq_iff_of_injective`

The guard limits remain 60 CPU seconds per process, 75 wall seconds, and
1610612736 bytes sampled aggregate RSS at 0.1-second intervals. No cap was
raised. This is not a hard Darwin address-space limit or a guaranteed
between-sample overshoot bound. The receipts attest to their listed inputs,
not an exhaustive bundle of every dependency binary. This review inspected
the root's runs; it is not a separate compiler or second-kernel run.

## Application boundary

This is conditional normalization algebra in one aligned frame. Actual
contractions and both comparison terms, full global row factorizations,
alignment through the needed normal order, determinant and twist transports,
regular trace extraction, unchanged lower data, and the physical ladder and
tensor certificates remain to be authenticated. The record's certificates
are mathematical premises, not validated physical data.

No physical realization of a nonzero defect, actual correct normalization,
global gluing, source-submodule calibration, HM exclusion, or main-theorem
repair is proved. Compatible global nonzero errors may pass overlap tests;
the source and publication scope do not conflate that with zero defect.
