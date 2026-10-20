# Independent audit: universal trace detection

Date: 2026-10-18 (UTC). Result: **PASS**, limited to the generic algebraic and conditional class-detection statements below. Independently reviewed both source files and compiled them with the existing Lean 4.33.0 and pinned Lean 4.19.0 environments. No installation or dependency rebuild was performed.

## Source identity

The audit is bound to these SHA-256 values (unchanged before and after checking):

```text
b2f4028caa8053cfb2ab56f7849eb99633fe1a9d1db2c1b9789695984925270b  TraceDetection.lean
73ed88f138941b8ed8cd5098af1bc1357605d41aadb9fe5119ce7a69377057d2  AuditTraceDetection.lean
```

## Environments and reproducibility

- Lean 4.33.0, x86_64-unknown-linux-gnu, release commit `d8b18978322de05a8f3dba51ef03cf5461676c17`; executable directory `${ARTIFACT_ROOT}/vermilion-tooling/toolchain/lean-4.33.0-linux/bin`; existing Vermilion Mathlib revision `db584cd6d46c92f209a44c0f1c829460d327499d`.
- Lean 4.19.0, x86_64-unknown-linux-gnu, release commit `6caaee842e94`; executable directory `${ARTIFACT_ROOT}/lean-koszul/toolchain/lean-4.19.0-linux/bin`; Mathlib revision `c44e0c8ee63ca166450922a373c7409c5d26b00b`.

Exact reproducible command, run successfully from `${ARTIFACT_ROOT}/lean-koszul`:

```bash
bash independent-trace-audit/recheck.sh > independent-trace-audit/RECHECK.log 2>&1
```

The full script is retained at `independent-trace-audit/recheck.sh`. It selects each executable directory, runs `lean --version`, records the Mathlib Git revision, obtains the dependency path using `lake env printenv LEAN_PATH`, normalizes all paths before changing directories, and executes the following commands for each version:

```bash
LEAN_PATH="$ML_PATH" lean --root="$ROOT" -o "$OUT/TraceDetection.olean" TraceDetection.lean > "$OUT/compile.log" 2>&1
LEAN_PATH="$OUT:$ML_PATH" lean --root="$ROOT" AuditTraceDetection.lean > "$OUT/axioms.log" 2>&1
```

Here ROOT is `${ARTIFACT_ROOT}/lean-koszul` and OUT is ROOT/independent-trace-audit/lean433 or ROOT/independent-trace-audit/lean419. The audit imports the independently rebuilt version-specific object, rather than the producer's existing object. Both compile logs are empty; both audit commands exit successfully. Version, dependency revision, axiom reports, elaborated final signature and source hashes are retained in the audit directory.

An initial 4.19 attempt failed because Lake returned relative dependency paths; normalization corrected that environment-only error. Neither source was modified. The final reproducible script contains the correction.

## Mathematical review

1. `injective_comp_ne_zero` proves that an injective linear map γ preserves a nonzero map φ under postcomposition. Assuming γ.comp φ = 0, evaluation at each vector followed by injectivity forces φ = 0. No finite-dimensional hypothesis is used here.
2. `trace_rankOne` uses **Mathlib's actual `LinearMap.trace`**, not a replacement scalar-valued functional. The endomorphism f.smulRight w is identified with `dualTensorHom k W W (f ⊗ₜ[k] w)`, then `LinearMap.trace_eq_contract_apply` and `contractLeft_apply` prove its trace is f(w). Mathlib's trace/contraction theorem is itself a proved theorem, not a new axiom supplied by this file.
3. `exists_trace_comp_ne_zero` obtains w with T(w) ≠ 0 and uses Mathlib's algebraic-dual separation theorem `Module.forall_dual_apply_eq_zero_iff` to obtain f with f(T(w)) ≠ 0. Taking B(x) = f(x)w gives B.comp T = (f.comp T).smulRight w; the rank-one trace identity gives the required nonzero trace. Only W must be finite-dimensional; C can be arbitrary. There is no asserted perfect-trace-pairing hypothesis.
4. `exists_trace_injective_comp_ne_zero` composes the first and third results. It requires both injectivity of γ and nonzeroness of φ as explicit inputs.
5. `class_ne_zero_of_trace_pairing` assumes a pointed type H, a class r, a pairing, pairing(0,B) = 0 for every B, and pairing(r,B) = trace(B.comp (γ.comp φ)) for every B. The previous theorem provides a detecting B. If r = 0, the supplied identities force its nonzero trace to vanish, a contradiction. No linearity or nondegeneracy of the abstract pairing is silently required.

The inspected trace and dual source files have no Git modifications in either Mathlib checkout. Relevant 4.19 source declarations occur in `Mathlib/LinearAlgebra/Trace.lean:156` and `Mathlib/LinearAlgebra/Dual/Lemmas.lean:193`; the corresponding 4.33 declarations occur at lines 177 and 205.

## All five axiom reports

Both independently executed audit files report exactly:

```text
'TraceDetection.injective_comp_ne_zero' depends on axioms: [propext, Quot.sound]
'TraceDetection.trace_rankOne' depends on axioms: [propext, Classical.choice, Quot.sound]
'TraceDetection.exists_trace_comp_ne_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'TraceDetection.exists_trace_injective_comp_ne_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'TraceDetection.class_ne_zero_of_trace_pairing' depends on axioms: [propext, Classical.choice, Quot.sound]
```

These are standard Lean logical axioms. No `sorryAx` or custom axiom occurs in any theorem dependency report. Direct source inspection also found no `sorry`, `admit`, custom `axiom`, `unsafe`, or `native_decide`. The five declarations have completed proof terms accepted by Lean. This is source elaboration/kernel checking in the stated installed environments, not an independent certification of the compiler binary or a rebuild of all imported Mathlib dependencies.

## Exact formalization boundary

The generic trace-detection implication is proved. The final theorem is explicitly **conditional**, and does not construct or prove:

- an actual geometric/cohomological H or class r;
- geometric injectivity of γ;
- the nonzero antecedent φ ≠ 0;
- the geometric pairing or its trace identity and zero-class vanishing;
- the HM presentation, Čech realization, residue normalization, Serre-duality bridge, or supertrace signs.

Thus this audit does not certify the full geometric nonvanishing theorem. It certifies the universal linear-algebra step and the precise implication available once the external inputs are established.

No actual HM source values, model matrices, ranks, polynomial instances, geometric points, jets, residuals, or Massey values were instantiated or evaluated during this audit. The rank-one witness is a generic mathematical construction in a universally quantified proof.
