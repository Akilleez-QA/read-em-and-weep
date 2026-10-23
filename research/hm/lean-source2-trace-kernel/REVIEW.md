# Independent review: Source2 trace-coordinate kernel

**PASS.** The final Lean module compiles, and all ten exported theorems
have been checked for axioms. The native reviewer independently reviewed
the source mathematics, authenticated the written source, reviewed the
complete producer-to-final delta, and inspected the root-run compiler
receipts and complete axiom output. The reviewer did not rerun compilation
or edit the producer's executable proof files.

## Exact bindings

All digests below are SHA-256. Names are portable logical artifact names;
machine paths and process identifiers are intentionally omitted.

| Artifact | Digest |
|---|---|
| Final `OAI/AlgebraicGeometry/HorrocksMumford/Source2TraceKernel.lean` | `e580dbcf59da2cb4af5b25793b2f22027935f92d42b27c05a6a298ca1a15f38f` |
| Final `Check.lean` | `8a1760ce719427840546df738892da63b1272384488b6d8a096b827bebf52285` |
| Compiled `Source2TraceKernel.olean` | `4280ca401ae1a482a65d29fbdf0ed19b9f0bf6ecc48626c21a81742c24857ec8` |
| Compiled `Source2TraceKernel.olean.private` | `1593e6d617090cf476322005d2f74551cdef97d920ea8c3c51557cb85930e583` |
| Published PR808 `PROOF.md` | `316ef592bc74f29de4698e740b90ad760ef7ad6cc09777ae3d913fc69043a5d2` |
| Original CLI source, reviewed before compilation | `2c9941705f530927c829ba1e287e9135f340e7ff611a5defbdc415247ceff947` |
| Original CLI `Check.lean` | `81770561d141ed615864e1a70e2a17ea54f9774a1380dd91c8cc70829e4d5029` |
| Original CLI `SCOPE.md`, retained as producer history | `bf85ac8bb356eb95fdddc980dc51f35db1111e00e4b541a0b92c3f25710f1965` |
| Original static-only review | `ea65536d8cb36ed9af3378b4dd474a5fc6259636eb1b1da20ff218f7cd4cb773` |

The written source is PR808, commit
`3c2d80d5bbae109f810b1919fb0adbc2a1d0e392`, path
`research/hm/source2-commutant-gate/PROOF.md`, in
`Akilleez-QA/read-em-and-weep`. The reviewer authenticated its exact bytes
with `git show` at this commit and path. Its section 4 supplies the column
vectors used by this Lean unit.

The build uses Lean **4.34.1** and mathlib revision
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The reviewer checked that local
mathlib HEAD and its `lean-toolchain` match those values. The selected
Darwin arm64 `lean` executable has digest
`1b370cfcbf44e80d1b004ab1b1ab9a4c73951f9f7c242140bcff9bc577576554`.
The reviewed launch wrapper selects this explicit compiler and the pinned
dependency search path, with `-j1 -M1200`. The wrapper digest is
`ce5051e14a6d7b174195c9c949c91ea1c79e9c2ab49f9237c56da4eb48397a69`;
its recorded search-path file digest is
`7a93dfc6d5ce598755ad214d49792c947f3a8fdc4609e424266793e46715bdad`.

## Mathematics and final delta

The uncoupled linear map has ordered columns
`d0=(9,18,16)`, `d8=(15,18,12)`, and `dC=(17,18,9)`.
The coupled map has columns `d0` and `dR=d8+dC=(32,36,21)`.
Nested triples use `K × (K × K)` and vertex order `(2,3,4)`;
inputs use `(a0,a8,aC)` or `(a0,aR)`, respectively.

All five integer-scaled reconstruction identities were independently
checked. Their row multipliers are
`(-54,69,-36)`, `(126,-191,144)`, and `(-72,132,-108)` for the
three uncoupled coordinates, giving `180` times the corresponding
coordinate. The coupled first-two-row multipliers are `(36,-32)` and
`(-18,9)`, giving `-252` times the corresponding coordinate. Every sign
and coefficient matches the final definitions. The third coupled output
is correctly `16*a0+21*aR`; the first two outputs suffice for injectivity.

The definitions and five identities now require only `[Field K]`.
Characteristic zero is introduced for the two injectivity theorems,
where `180` and `-252` must be nonzero. The general theorem
`ker_comp_of_injective` uses an explicit injectivity hypothesis and omits
characteristic zero. The two specialized kernel theorems require it and
conclude exactly `ker (traceMap.comp diag) = ker diag` for a supplied
linear `diag`. They do not require `diag` to be injective or surjective.

The complete delta from the original reviewed source consists of:

- Lean module mode, public narrow imports, and an exposed public section;
- replacing `LinearAlgebra.Prod`, broad `Ring`, and broad `NormNum` imports
  with `Algebra.Module.Prod`, `Algebra.Module.Submodule.Ker`, and `Ring.Basic`;
- replacing nine equality-closing `ring` calls with `ring1` and removing
  two redundant `simp only [smul_eq_mul]` steps after `dsimp`;
- proving the two nonzero constants with `Nat.cast_ne_zero`, `decide`, and
  `neg_ne_zero`, while restricting the characteristic-zero assumption to
  the results that need it;
- adding module mode to `Check.lean`.

No column, reconstruction conclusion, injectivity conclusion, or kernel
conclusion changed. These are proof/import repairs and removal of an
unused assumption, with no semantic substitution of the maps.

## Compilation and axioms

The final compile, `compile-0005`, succeeded with exit code 0 and empty
stdout/stderr. It recorded 1.420559 CPU seconds, 1.540995708 wall seconds,
863,928,320 bytes sampled group peak RSS, and 874,741,760 bytes child
`wait4` peak RSS. Input hashes were unchanged and cleanup was complete.
Its raw receipt digest is
`c01bc6426b7d126e04f24e803b3bc68e3c8aa22747ad04d21d29ee7c8b886ecf`.

The separate `axioms-0001` check succeeded with exit code 0 and empty
stderr. Its receipt binds the final `Check.lean` and compiled `.olean`
listed above. It recorded 1.277671 CPU seconds, 4.87179025 wall seconds,
825,360,384 bytes sampled group peak RSS, and 828,358,656 bytes child
`wait4` peak RSS. Input hashes were unchanged and cleanup was complete.
Its raw receipt digest is
`e40dc4bd5aadc7056e9713fd483ab48408c7b611044d58e531de458494fc2695`;
the complete stdout digest is
`3cf4d1853504a509576da83fd66d33a2e4193e06931361b8a39c182ed73e68d7`.

Each of the five reconstruction theorems and `ker_comp_of_injective`
reports exactly `[propext, Quot.sound]`. Each of the two injectivity
theorems and two specialized kernel theorems reports exactly
`[propext, Classical.choice, Quot.sound]`. All ten requested declarations
appear in the output. None depends on `sorryAx` or a custom axiom.
The final source contains no `sorry`, `admit`, custom axiom declaration,
`native_decide`, `unsafe`, or `run_tac`.

Both successful runs used 60 CPU seconds per process, a 75-second wall
watchdog, and a sampled 1.5 GiB aggregate process-group RSS limit at
0.1-second intervals. The guard claims neither a Darwin hard address-space
limit nor a finite between-sample RSS overshoot bound. Its source digest
is `6915a220408dc3bb5045b6cfaaaef8267a6516319cdb98deca5ba5717614c6fc`.

Earlier failures remain preserved: `compile-0001` and `compile-0002`
reached Lean's internal memory ceiling before source diagnostics;
`compile-0003` exposed the redundant `simp` steps;
`compile-0004` exposed a doc-comment/`omit` placement syntax error.
Their raw receipt digests, in order, are
`4af31b9970f78061521e7f951472a9bc463bf825cd78e5da60960c8c73960c41`,
`48227609da4a04c13b17768ea05a812eb12e918e5d3c174e6a20f766a44b51f6`,
`13708313a5f322153313de652a24039c91dc71149de1a0829eda91a0e6c291f2`,
and `103ceeb01b0634f76475f8166c49b9854163e35c4b7b3afc5d89bab136924d83`.
The original `SCOPE.md` and static-only review describe their earlier
uncompiled state; this report supplies the final verified status.

## Application boundary

This is a proved universal coordinate-algebra unit. Applying it to an
actual HM commutant still requires an authenticated normal-form diagonal
projection and the ordinary vertex-trace formulas for that actual action.
The unit does not construct that identification or identify an arbitrary
trace kernel with a Jacobson radical. It establishes no actual tensor
coefficients, tensor ranks, dimension bounds, or source2 exclusion.
There is no remaining blocker within the stated coordinate-algebra scope.


## Publication status and evidence binding

The final publication layout was independently inspected after the report
above was frozen. This combined review preserves that original report
(digest `b28ef4177822e0b5f73a63c967781bc0db716291a0d43dc33339694641d34706`)
and adds the following exact publication bindings, relative to
`research/hm/lean-source2-trace-kernel/`:

| Publication artifact | SHA-256 |
|---|---|
| `README.md` | `78e2999a84f6b47395c6e5754bdbee3d7faddc81013d7ee0516f56060e65a699` |
| `VERIFICATION.json` | `ab8dbe589eec508151fbb41f695c6d3a32a7e2a12e6cc2c6406ef4199473e214` |
| `AXIOMS.txt` | `3cf4d1853504a509576da83fd66d33a2e4193e06931361b8a39c182ed73e68d7` |

The staged Lean source and `Check.lean` have the exact final hashes listed
above. `README.md` correctly states the completed Lean status, the weaker
field assumptions of the identities, the characteristic-zero requirement
for injectivity, and the supporting-result application boundary. It
explicitly records that Comparator and an independent second kernel were
not run. Its repository replay commands are distinct from the archived
isolated-workspace invocation. The original uncompiled `SCOPE.md` remains
historical producer evidence and is not used as the publication status.

The reviewer compared the normalized success status, return code, timing,
CPU use, sampled RSS, limits, unchanged-input flag, cleanup flag, stdout,
and stderr in `VERIFICATION.json` against both original receipts/logs.
All compared values match. `AXIOMS.txt` is byte-identical to the successful
axiom-check stdout. No private host workspace path or process identifier
appears in these publication files.

The pinned mathlib manifest has SHA-256
`8f67b2cf24143ac091cdb425e886c2164b2fc2d6fbccd6db9454b697f9541a67`.
The reviewer independently compared all eight dependency revisions and
URLs in it against `lean/lake-manifest.json` from repository commit
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`; all match. This check was a
read-only manifest comparison, not another compilation or whole-library
verification. Publication review result: **PASS**.
