# Independent review: typed nonclosed frame transfer

**PASS.** The native reviewer independently checked the statement,
proof, source correspondence, exact final deltas, and root-run compiler
and importing axiom-check evidence. The reviewer did not run another
compiler. Comparator and an independent second kernel were not run.

## Exact bindings

All digests are SHA-256. Paths are portable logical names.

| Artifact | Digest |
|---|---|
| `lean/OAI/AlgebraicGeometry/HorrocksMumford/NonclosedFrameTransfer.lean` | `9fd1bfdae44e2edc2e7f83838d97d150b75d3f5a7fb870b9038866f193ee5c0f` |
| Final `Check.lean` | `80d120533e0859a41f34406d74f4e3029f56efb3e89576bf68efaad074b11520` |
| Compiled `NonclosedFrameTransfer.olean` | `65429418bd2cef7325120b92eb5f8e3f082e861e6b6aa2c8f7e9da35a8a67da5` |
| Compiled `NonclosedFrameTransfer.olean.private` | `ccb2bc6f2ffb4528590f019f8621a2c13e190bcd900b7ac859daf6c2aadba4a3` |
| Authenticated PR816 source proof | `5f2069fe845df87caa3a4bdb1c2bd7434ff6513bddda5bc21f54f042a04a4e84` |
| Earlier independent static review | `0fe3b031de61f0d4898c38f9a88f783476b4e00bc5227dabf8a8231bd5c4aba3` |
| Historical producer `SCOPE.md` | `5e2885a64946d4dc94dd81e858a685218ffdf4ebb9f5142dfccdf8e9dc065b85` |

The written source is null's PR816, commit
`eed6010347fcebc21aef30413b0e1da3be68a9b4`, path
`research/hm/nonclosed-frame-transfer/NONCLOSED-FRAME-TRANSFER-EXACT-DEFECT.md`,
in `Akilleez-QA/read-em-and-weep`. The reviewer fetched the exact bytes
through the GitHub connector and reproduced Git blob
`575004321d185de506573a1baad97bdf046b215f`. The Lean result formalizes that
written identity; it does not claim to discover it anew.

## Mathematical and typing audit

The core theorem has ten independent module types over an arbitrary ring,
including distinct source/target degrees `-1,0,+1` and four frame modules.
The emitted theorem type confirms these are independently universe
polymorphic. Its only four identity hypotheses are

```
dCm hCb0 + hCb1 dC0 = id - iCb pCb,
dDm hDa0 + hDa1 dD0 = id - iDa pDa,
dC0 iCa = 0,
pDb dDm = 0.
```

The endpoint maps `Em` and `Ep` are arbitrary. Set
`Tm=dDm Em-E0 dCm` and `T0=dD0 E0-Ep dC0`. The conclusion is exactly
PR816 equation (1), an equality in `HCa →ₗ[R] HDb`:

```
M_b g_ba^C - g_ba^D M_a = pDb (Tm hCb0 + hDa1 T0) iCa.
```

Both signs are positive. The source homotopy belongs to frame `b`, the
target homotopy to frame `a`. Composition order and the two distinct
transition maps are correct. No field, characteristic, finite-rank,
retraction, differential-square-zero, or normalized-homotopy premise is
hidden in the type.

The pointwise proof derives the two required homotopy rearrangements,
then cancels the `Em` term using the closed projection and the `Ep` term
using the closed inclusion. It rearranges addition without commuting
composition. The closed-limit theorem adds precisely `Tm=0` and `T0=0`.
The exact-projection theorem proves
`pDb (dDm K0 + K1 dC0) iCa=0` for arbitrary typed `K0,K1`, using only
the two closedness hypotheses. Its plus sign is the degree-minus-one
coboundary sign. All three emitted theorem types match these statements.

No executable proof changed after the original static review. The source
leading comment changed from `UNCOMPILED draft` to `Supporting algebra
draft`. The check's leading comment was revised twice, ending with
`Imported-module axiom audit for every theorem.` Reversing exactly these
comment edits reproduces original source digest
`6566f244992881ae5b0d0850da204f6cae348e0bddce7f81b216931de42bffe8`
and check digest
`109c2f434e9015f5bde4c1efd89bcdabec3a474b856fdb16647338e7837f5059`.
The original source and `SCOPE.md` remain historical producer evidence.

## Compiler and axiom evidence

The pinned environment is Lean 4.34.1 and mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The launch wrapper digest is
`ce5051e14a6d7b174195c9c949c91ea1c79e9c2ab49f9237c56da4eb48397a69`;
it explicitly selects the pinned compiler, dependency search path, and
`-j1 -M1200`. The same reviewed guard is used for both final runs.

| Final run | Exit | CPU seconds | Wall seconds | Sampled group peak RSS, bytes |
|---|---:|---:|---:|---:|
| `compile-0002` | 0 | 1.79678 | 5.825397541999999 | 746258432 |
| `axioms-0002` | 0 | 1.292444 | 4.340847333 | 721420288 |

Both receipts record unchanged input hashes and completed cleanup. The
compile receipt binds the final source; the import receipt binds the
final check and exact compiled `.olean`. Receipt digests are respectively
`919131793e2a4ed4ae3ee91a11e36f4c216853d19870b96971b0d3afa0eba752`
and `fd8de4a96b5f757f5b1087154ffb6050eeeb7ecbb7c5eda15df6ad0752eb6b70`.

The compile reports one nonblocking unused `map_add` simp-argument warning
in the exact-projection proof, followed by the three axiom reports. Its
original stdout digest is
`762f00a541a044d0240de473ee48b131716a3224b52cfa3a0797c453b486f460`.
The final import check emits all three theorem types and axiom reports;
its stdout digest is
`5b4f6b4385e19dae3cf528081ce7e2b030b592629307c46ff0cb6f12c461a7b7`.
Both stderr files are empty.

The core and closed-limit axiom closures are exactly
`[propext, Classical.choice, Quot.sound]`. The exact-projection closure is
exactly `[propext, Quot.sound]`. Neither source nor the emitted closure
contains an unfinished proof or custom axiom; no `native_decide` or unsafe
proof escape is used.

The only unsuccessful module attempt, `compile-0001`, stopped because
`Mathlib.Tactic.Abel.olean` was missing. Its sole diagnostic is a missing
object file, and its receipt digest is
`f4b0cc886ef4c46af081fcb4bfda33cdf9fa6737e256d9a85a07bfade0453a07`.
After the targeted cache fetch, the unchanged source passed. The earlier
`axioms-0001` also succeeded; its receipt
`6528827c0b95f18855457ba102501f33e8dd3a783d13dd7d3cba7fc53a432138`
binds the intermediate check comment. Its stdout is byte-identical to
the final import-check stdout. All prior receipts remain preserved.

The limits remained 60 CPU seconds per process, a 75-second wall watchdog,
and 1.5 GiB sampled aggregate process-group RSS at 0.1-second intervals.
This is not a hard Darwin address-space limit or a guaranteed bound on
between-sample RSS overshoot. The review relies on the root-run Lean
compiler and evidence; it is not a second independent kernel run.

## Application boundary

This proves universal component algebra. It does not authenticate actual
HM complexes, contractions, markings, physical frames, weights, twists,
primitive components, or response rows. Global compatibility, descent,
cohomology vanishing, and tracefree/scalar distinctions remain separate
application obligations. The result supplies no Lambda, `qZ`, `beta4`,
rank, row-support certificate, ladder, or repaired main theorem. The
closed-limit equality is not presented as a constructed global section.
There is no remaining blocker in the stated supporting-algebra scope.
