# Universal trace detection

`TraceDetection.lean` proves the finite-dimensional linear-algebra implication used in §5 of `../cubic-structural-nonvanishing/PROOF.md`, and a deliberately conditional class-detection theorem.

## Statements proved

Let k be any field, A and C arbitrary k-vector spaces, and W a finite-dimensional k-vector space.

1. `injective_comp_ne_zero`: if γ : A → C is injective and φ : W → A is nonzero, then γ ∘ φ is nonzero. This lemma itself does not require finite dimension.
2. `trace_rankOne`: for f : W → k and w ∈ W, the trace of x ↦ f(x)w is f(w). This is proved from Mathlib's `LinearMap.trace_eq_contract_apply` and `contractLeft_apply`, not introduced as an axiom.
3. `exists_trace_comp_ne_zero`: if T : W → C is nonzero, then some B : C → W satisfies tr_W(B ∘ T) ≠ 0.
4. `exists_trace_injective_comp_ne_zero`: consequently, injective γ and nonzero φ give some B with tr_W(B ∘ γ ∘ φ) ≠ 0.
5. `class_ne_zero_of_trace_pairing`: let H be any type with a distinguished zero, r ∈ H, and pairing : H → Hom(C,W) → k. If pairing(0,B)=0 for every B and pairing(r,B)=tr_W(B ∘ γ ∘ φ) for every B, then r ≠ 0, provided γ is injective and φ ≠ 0.

No finite-dimensionality assumption on A or C is required. No characteristic-zero or explicit nontriviality hypotheses on W, A, or C are required: the nonzero-map hypothesis supplies the needed nontrivial situation. The field instance already excludes the zero ring.

## Proof mechanism

A nonzero T supplies an abstract w with T(w) ≠ 0. Mathlib's algebraic dual separation (`Module.forall_dual_apply_eq_zero_iff`) supplies an abstract f ∈ C* with f(T(w)) ≠ 0. The proof uses the rank-one map B(x)=f(x)w. The trace/contraction theorem then gives tr(BT)=f(T(w)) ≠ 0.

The witnesses remain universally quantified/existentially selected mathematical objects. No coordinates, source/model matrices, ranks, polynomial instances, points, jets, residuals, or Massey values are instantiated or evaluated.

## Exact boundary

This file does not formalize the HM presentation, sheaf or fiber injectivity, the nonzero transgression antecedent, Čech complexes, supertrace signs, Serre duality, residue normalization, or the geometric pairing identity. The final theorem exposes the three essential inputs explicitly:

- γ is injective;
- φ is nonzero;
- the class pairing is exactly the specified trace and vanishes at the zero class.

Thus it closes the abstract trace-detection step, rather than claiming a formal proof of the entire geometric nonvanishing theorem. H needs only a zero because that minimal hypothesis is sufficient for this implication; an actual cohomology group can instantiate H when its external bridge is proved.

## Verification

Initial independent toolchain check: Lean 4.33.0 with the already-installed Mathlib in `../vermilion-tooling/vermilion`. The repository's 4.19.0 pins are unchanged. `TraceDetection433.compile.log` is empty, indicating a clean compilation. `TraceDetection433.axioms.log` records the five theorem axiom reports and the final theorem's fully elaborated signature.

All five theorems depend only on Lean's standard logical axioms `propext`, `Quot.sound`, and (where needed) `Classical.choice`. There is no `sorryAx`, user axiom, `unsafe`, `native_decide`, or unproved perfect-pairing assumption.

`AuditTraceDetection.lean` is the reproducible axiom/signature audit. Pinned Lean 4.19.0 verification is also complete: `TraceDetection.compile.log` is empty and `TraceDetection.axioms.log` has the same standard-axiom-only results. The 4.19 compiled object is `TraceDetection.olean`. Run `./check-trace-detection.sh` to reproduce both compilation and audit using the pinned toolchain; only the already-pinned official Mathlib cache was supplemented, with no changes to version pins.
