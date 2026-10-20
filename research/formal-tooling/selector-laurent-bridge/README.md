> Publication note: Read [PUBLICATION.md](PUBLICATION.md) first. Original checks below are historical; original shell scripts now have `.historical.txt` suffixes. Use the public reproduction instructions, not private-path commands.

# Accepted selector to single-term Laurent coefficient

New proof bridge, 2026-10-18, using existing Lean 4.33.0 and Mathlib dependencies. No dependencies installed and no existing verified sources changed.

## Checked result

`SelectorLaurentBridge.returned_eq_single_coefficient` retains all six generated `Vermilion.inSignedRange 64` premises for five exponent integers and one coefficient integer. It proves that `returned e0 e1 e2 e3 e4 coefficient` equals `Finsupp.single (exponent e0 e1 e2 e3 e4) coefficient` evaluated at `ResidueBridge.residueExponent`, the vector of five minus ones.

`exponent` explicitly maps the five Int inputs to `Fin 5 → Int`. `returned` is the emitted selector return expression after substituting the short-circuit SSA temporary propositions; it retains the machine `sclip 64 (0 - 1)` comparisons. This is an explicit representation of this lowered return expression, not a newly verified Rust interpreter.

`accepted_postcondition` directly applies the actual accepted generated theorem `residue.residue_term.ensures_5`, statement hash `40bc1be52a94f9a9`. It supplies all six input-range premises and proves every arithmetic and branch/temporary assumption. The printed proof term in `bridge.compile.log` records this imported declaration reference. No postcondition is added as an axiom or simply assumed.

`guard_iff_exponent` uses `ResidueBridge.residue_predicate` to identify the five-coordinate condition with equality to the residue exponent. `returned_eq_singleton_residue` also presents the result via the concrete singleton-list Laurent interpretation.

`first_coordinate_face_zero` directly applies accepted `residue.missing_face_zero.ensures_1`, statement hash `882c66ea6eff9c14`, after proving its call-result bounded-range premise from the coefficient-or-zero branches. It proves both the returned value and singleton Laurent residue vanish when e0 is nonnegative. The latter proof independently invokes `ResidueBridge.residue_eq_zero_of_nonnegative_coordinate` at coordinate zero.

## Provenance and checking

The local `residue/*.lean` files are unchanged byte copies of the accepted positive proof twins at `${ARTIFACT_ROOT}/vermilion-tooling/vermilion/examples/residue-selector/proofs/residue/`. Their evidence twin is the accepted repaired version, not the generated placeholder. `ResidueBridge.lean` is an unchanged copy of `${ARTIFACT_ROOT}/lean-koszul/ResidueBridge.lean`. `source-sha256.txt` records all source hashes. Imports resolve to freshly compiled local copies through LEAN_PATH, using existing Vermilion dependency oleans.

Run `./recheck.sh` to verify byte identity and recompile every local module. It exits on any failure and uses only the already installed toolchain/dependencies. `bridge.compile.exit` records exit 0 for the initial successful new bridge compilation. `bridge.compile.log` contains proof printing and axiom reports. All four public result reports list only `propext`, `Classical.choice`, and `Quot.sound`.

## Exact boundary

This closes the mathematical interpretation of the accepted selector VC, for one term. The Rust-to-SST correspondence, VC generation, and embedding conventions remain the existing Vermilion trust boundary; the translator is not foundationally verified. The returned expression is explicitly defined from the accepted VC's SSA form, not imported as a callable Rust function (the generator produces obligations rather than such a function definition).

No sparse-list aggregation executable, arbitrary-precision arithmetic implementation, analytic residue result, full TW/HM bridge, or full certificate checker is claimed. Returning coefficient or zero introduces no accumulation overflow; bounded inputs remain premises. No actual HM values, source/model matrices, ranks, polynomial instances, points, jets, residuals, or Massey computations were used. All new checks are universal formal proof checks.
