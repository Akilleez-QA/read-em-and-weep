# Complete-source constant-scalar operator compiler

This package compiles the complete corrected source into typed formal matrix/cochain circuits for the PR83 twenty scalar maps and thirty-two weighted outputs. It expands the Cech faces and graded End homotopies, rebuilds the baseline with its gerbe terms, and emits coefficient operators. It does **not** realize the physical rational matrix leaves, partition coefficients, or scalar-source numerators. No physical value or arithmetic release follows.

## Reproduce

From the repository root:

```sh
python -B research/codex-swarm/scalar-compiler/run_formal.py
python -B research/codex-swarm/scalar-compiler/run_controls.py
```

The first command writes `compiled-template.json` and `formal-run-receipt.json`. The second runs thirteen exact producer controls normally and under `-O`, each in a separate bounded subprocess, and writes `controls-receipt.json`. Bounds are 512 MiB address space, 59 seconds CPU, and 60 seconds wall per subprocess. The node cap is 25,000 and serialized circuit cap 4,000,000 bytes.

The current formal output has 4,270 interned nodes and 20 complete-source triple stencils. Its bounded generation took 0.075930 seconds and 24,928,256 bytes kernel-reported child maximum RSS. The normal and optimized controls pass, including strict integer/Boolean input rejection. These measurements concern formal circuit generation and tiny abstract controls, not physical coefficient evaluation.

## What is executable

`compiler.py` provides:

- A dimension-checked matrix DAG with exact rational coefficients, noncommutative multiplication, transpose, trace-free projection, and formal physical differentiation. Product derivatives expand by the ordered Leibniz rule; inverse derivatives use `-g^-1 (Vg) g^-1`. Moving-frame derivatives are never discarded.
- The complete five-branch `Rsharp`: trace-free normalized `M0`, both `Fk` corrections, and both complementary derivative corrections. `M0` is rebuilt at `u0=gk` from the seven mixed kinetic terms and all three gerbe terms. It never calls the legacy scalar-inclusive first lift.
- The full `J0,J1,J2,J3` matrix-block stencils, with every alternating Cech face expanded and homotopy owners attached before later face deletions. Shared degrees/signs come from the hash-bound `transport-binding/lift_schema.py`.
- All twenty constant scalar entry rows, applied to the two blocks of `J2`. The 1,500 polynomial coefficients of `L d_End=0` are checked for all thirty constant rows.
- Thirty-two weighted Laurent-coefficient circuits, retaining the PR83 127 listed contributions and 121 distinct map/exponent pairs. The outer transport contains all 24 CCCC staircases per coefficient, the five full-owner fibers, and owned outer weights. It uses no old 78-selector table or special scalar carrier merger.
- `bind_outer_assignment`, which instantiates one symbolic outer assignment, verifies full occurrence identity and source sorting, and preserves every partition owner. Repeated carrier alone is not a zero rule.

The inner solver has three explicit operator branches: the two signed prisms grouped as `Hrho`, the standard `R K_cov Pi` branch, and the standard `R A h S Pi` branch. Its derivative is a distinct **whole combined solver** node. It cannot be replaced by derivatives of separately cleared raw pieces. The actual source-clearing equality and finite coefficient realization remain unresolved.

The circuit is a universal stencil on symbolic full owners. It does not enumerate `96^5` outer assignments or materialize a Laurent rectangle. That raw fiber count and the 3,048 staircase occurrences are combinatorial metadata, not execution-cost or occupied-support claims.

## Source and theorem bindings

`source-pins.json` identifies the exact Git blobs consumed. The baseline/source/model, combined-inner pole implication, and order-comparison note are pinned at PR79 `10810ee877fdaf291399198ad60d7dd0c316a42d`. The uniform scalar-family transport theorem is additionally consumed at `43193bc8badf3f29a1363132135d956cc12d46ad`, proof blob `fc8befcc863efd073d4a66dc6eec12c722504447`.

The latter theorem supplies the conditional all-row operator and common carrier54/legal29/standard5251 domain. This compiler does not duplicate its geometric proof or assert its actual-source hypotheses have been discharged. Standard order5251 is recorded as a unit/domain allowance, not an extra partition factor. The pair-specific inner14/legal1 partition is distinct from the outer54/legal29 partition.

`validate_template` reconstructs the exact formal circuit and rejects changed selectors, owners, signs, source components, proof bindings or gates. A successful validation authenticates a formal artifact. It cannot open any physical-source gate.

## What remains unresolved

The emitted gates explicitly keep false: physical matrix-leaf lowering; actual F clearing witness; actual all-row domain witness; outer fiber coefficient realization; historical-order identification; physical evaluation; execution release. Proof bytes and a displayed pole bound are not those witnesses.

In particular the combined-pole theorem assumes the actual identity `P=C_u C_v C_w F` and the standard-branch realization. The uniform transport theorem requires regular extension to the target standard intersection, not merely regularity on the common localization. Fresh-order source formulas cannot be substituted for a historical nonlinear cup prescription by sorting alone. These are null/source-adapter obligations, not newly claimed results here.

The formal scalar output is `L S Pi_outer J2`, with `J2=-H_-1 delta H_0 delta j(Rsharp)`. `J3` remains in the closure certificate even though it contributes no terminal scalar row. Actual evaluation still requires the complete closed representative and the authenticated original frames, deck-product removal, `tau^-4`, and all retained owner data. The current obstruction remains undecided.
