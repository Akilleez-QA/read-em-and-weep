# Independent review: first normal correction

**PASS for the four supporting matrix identities.** The reviewer independently checked the matrix formulas, inverse assumptions, trace-cyclicity API, final comment-only delta, and the complete root-run compilation and importing axiom output. No compilation was rerun by the reviewer. No producer proof file was edited by the reviewer.

## Final source and evidence bindings

All digests are SHA256; artifact names are portable and omit private host paths and process identifiers.

| Artifact | Digest |
| --- | --- |
| Final `OAI/AlgebraicGeometry/HorrocksMumford/FirstNormalCorrection.lean` | `5b4929d3149af4c38d70b2336f947f10fab5cfbca5805fdc06f6856faa5349d9` |
| Final `Check.lean` | `785f024d6fa4b69cc714d1147b5ba2c2dc7092fd6f7644de87ed83ae984cd27b` |
| Imported `FirstNormalCorrection.olean` | `2c6ba516c6d5dfec92cd83fc81aff035a3829dbdda813a43616f0e57134f7698` |
| `FirstNormalCorrection.olean.private` | `c3b0387e9cc8fd1ce56f4010eb71f15667fd241426750b76ecef181638586c77` |
| Published PR815 `PROOF.md` | `78a0f462ffd0710d248658aaf95926f926297b0bae43aade85eb4c7fc934d236` |
| Original CLI proof source | `6a19c677e73d56eb3be33e591d5cbee5414116c4089c5b07b2ef8dd43743554b` |
| Original CLI `Check.lean` | `c1da6d904ac31b592417793cf96411dcb444ee2ac9bcbad3a9978e07d2841fd2` |
| Original CLI `SCOPE.md` | `d1304309b237f7bd84d47554053aecc378ae2a1454cb203a23ac17ff0451850f` |
| Original static review | `05f810fa4053775667941b77bf4b1f0165c5ee00227da42435c8de0082850c82` |

The exact manuscript commit is `0eaeca734b9e17142da2f1bdfd9a1721d0bb1d42` in `Akilleez-QA/read-em-and-weep`, path `research/hm/affine-square-source-response/PROOF.md`. The reviewer confirmed this reference through the primary GitHub API and verified that the retained complete text has Git blob `bef4e26574b3085616c22d5fdaae4e808e3767e4`, matching the API response. The original SCOPE and static review contain the malformed textual citation `8150eaeca734b9e17142da2f1bdfd9a1721d0bb1d42`; this report corrects it while preserving those historical files. Their source-content SHA256 was correct, so this is a citation correction rather than a different mathematical input.

The final proof and Check differ from their preserved original copies only in two module comments replacing stale UNCOMPILED descriptions. Definitions, theorem statements, hypotheses, tactics, imports, and options are unchanged. The final bytes were compiled again after these comment changes.

## Mathematical review

The definitions are actual 2×2 matrices over a field. For the triangular frame `T=[[alpha,0],[c,delta]]`, the explicit inverse has entries `[[1/alpha,0],[-c/(alpha*delta),1/delta]]`. Both inverse-order theorems require exactly the two diagonal entries to be nonzero. No other parameter or geometric source is required nonzero.

For `Z=[[t,0],[ell,-t]]` and `X=[[x,y],[z,-x]]`, independent multiplication gives

```
Z*X-X*Z = [[-ell*y, 2*t*y], [2*ell*x-2*t*z, ell*y]].
```

Conjugation by the frame yields diagonal `-(ell+2*c*t/delta)*y`, upper entry `2*alpha*t*y/delta`, and lower entry

```
2*delta*ell*x/alpha - 2*delta*t*z/alpha
  - 2*c*ell*y/alpha - 2*c^2*t*y/(alpha*delta).
```

The other diagonal is the negative of the first. Every sign, entry, denominator, and multiplication order agrees with manuscript equation (10). In particular, the upper and both lower `y` terms were not dropped. The identities require no division by two and remain valid in characteristic two.

The trace theorem distributes the product and trace over subtraction, then applies the pinned `Matrix.trace_mul_cycle' L Z L`, whose conclusion is exactly `trace (L*(Z*L)) = trace (L*(L*Z))`. This works for arbitrary matrices over a commutative ring. The central scalar `q` in manuscript equation (15) is not explicitly formalized; the source and README accurately identify the proved statement as the underlying cancellation. Its scalar multiple follows by trace linearity.

The four named theorems are `referenceFrame_mul_inv`, `referenceFrame_inv_mul`, `conjugated_commutator`, and `trace_mul_commutator`. The Check file requests every one. There is no `sorry`, custom axiom, `admit`, `unsafe`, `native_decide`, or `run_tac` in the proof source. The code proves the matrix identities and does not encode them as assumptions.

## Compilation and axiom audit

The final source compile `compile-0002` completed with exit code 0, unchanged inputs, completed cleanup, and empty stderr. It recorded 2.338994 CPU seconds, 2.447160125 wall seconds, 982433792 bytes sampled process-group peak RSS, and 996065280 bytes child `wait4` peak RSS. Raw receipt SHA256 is `38880b258312ab3c87ee951eb8a423ba0ee21ddd3f218873636fc8b625cea654`.

Compilation stdout has two `linter.unnecessarySeqFocus` warnings at lines 44 and 52 concerning `tac1 <;> tac2` where sequential tactics suffice. These are style warnings, not errors; they were neither suppressed nor described as absent. Compilation stdout SHA256 is `0c5489ba2076145090b8bf5b62e5103d8f9e4a8a8c00cc46e2e5602d63eab227`.

The separate `axioms-0001` import check completed with exit code 0, unchanged inputs, completed cleanup, and empty stderr. It recorded 1.162492 CPU seconds, 1.224321792 wall seconds, 926810112 bytes sampled group peak RSS, and 929955840 bytes child peak RSS. Its raw receipt SHA256 is `0d5ead077be6b809296c81b543e818432389a0d6239d32ef7616029f29528212`; complete stdout SHA256 is `9b5e691767eb10e003e120cece7ab7e48a75de748abac52cdfba727926c7261c`.

Each of all four imported theorem names reports exactly `[propext, Classical.choice, Quot.sound]`. None depends on `sorryAx` or another axiom. The reviewer verified current source, Check, wrapper, path manifest, and imported olean hashes against the successful receipts. The module-system conversion is not a trust bypass: local theorem bodies are kernel checked, and Lean4.34.1 exports the transitive axiom dependencies computed from full private bodies for downstream queries.

The earlier `compile-0001` also succeeded on the original source with the same two warnings; its raw receipt SHA256 is `245bb3c83267693732fc7d9099962747bc6e2c9534f0abfe20d3fc21ef58b835`. No C proof compilation failure is recorded. Original draft, original SCOPE, and static/import reviews remain historical artifacts, not current verification-status statements.

## Environment and limits

The compiler is Lean4.34.1, executable SHA256 `1b370cfcbf44e80d1b004ab1b1ab9a4c73951f9f7c242140bcff9bc577576554`. The reviewer independently checked local mathlib HEAD `d13f23b723b8a846827a245b89c10fc7d3f11612`. The wrapper SHA256 is `ce5051e14a6d7b174195c9c949c91ea1c79e9c2ab49f9237c56da4eb48397a69`, with path manifest SHA256 `7a93dfc6d5ce598755ad214d49792c947f3a8fdc4609e424266793e46715bdad`. It selects the explicit compiler, one thread, and `-M1200`, with no trust override.

Both final runs used the existing 60-second per-process CPU limit, 75-second wall watchdog, and sampled 1.5 GiB process-group RSS guard at 0.1-second intervals. Guard SHA256 is `6915a220408dc3bb5045b6cfaaaef8267a6516319cdb98deca5ba5717614c6fc`. Darwin address-space enforcement is explicitly unavailable, and sampling gives no finite between-sample overshoot guarantee. No limit was increased. Cached dependencies were prepared before the successful compile; the earlier import review identified a cache prerequisite, not a failed C proof.

This review trusts the pinned compiler and imported dependency artifacts. Comparator and an independent second kernel were not run. Axiom auditing is not advertised as either.

## Application boundary and publication

No blocker remains within the four-theorem matrix-algebra scope. Applying the formulas to an actual HM transition requires independent identification of the frame, first-normal generator, and full input coefficients. This unit does not prove geometric gluing, regular extension, harmonic coefficient extraction, source-row factorization, physical normalization, or the split-eightfold algebraicity theorem. It does not evaluate coefficients, ranks, rho16, beta4, or source models. Trace cyclicity alone does not license omitting the normal term from matrix transport.

The publication README replaces the original uncompiled status and malformed citation with the verified status and exact manuscript reference. Its repository replay commands are distinct from the recorded isolated run. The remaining publication assembly must preserve the final source/Check hashes, copy exact axiom stdout, and accurately normalize receipt/output evidence. This report does not claim to have inspected publication files that had not yet been staged when it was written.
