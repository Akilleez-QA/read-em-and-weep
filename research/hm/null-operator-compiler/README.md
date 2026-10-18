# General HM scalar differential operator compiler

This standalone package publishes the reusable **v5 source-binding and formal
normal-order layer for all 78 selector seeds and 624 E12/E34 edge branches**.
It also retains the selected scalar-demand graph (199 nodes) as a separately
scoped dependency example. It does not evaluate or expand physical source
polynomials, admit the full actual detector, or compute the actual second-order
obstruction O2. There is no global vanishing or nonvanishing conclusion.

## Replay

With Python 3.12 and the versions in `requirements.txt`, run:

    python run_checks.py

The wrapper verifies `SHA256SUMS`, verifies and decompresses the deterministic
archive using `prepare_artifacts.py`, reproduces both generated artifacts
byte-for-byte, and executes every `test_*.py` script. Assertions-disabled Python
is rejected. Tests use symbolic arbitrary functions, abstract split-complex
matrices, finite toy identities, and metadata. They do not evaluate pinned
physical polynomials. No network or sibling package is needed for replay.
The recorded replay passes 58 tests across 8 test scripts.
The decompressed large JSON is a generated working file, excluded from the
published inventory; use `prepare_artifacts.py` to restore it.

## What this adds to the two companion stages

`../null-proof-foundations/` supplies scalar reduction, conditional jet duality,
formal selector pruning and abstract proof controls. Its shared pruning and seed
metadata code is copied here only to make this runtime closure standalone.
`../null-support-certificates/` supplies focused support/cancellation certificates
and selected seed-4 E12 results. Neither stage substitutes for the general v5
source-binding compiler and its tests shipped here.

Later selected-seed proofs may discharge some historical selected obligations.
They do not automatically discharge the all-seed compiler's 78 unresolved
regularization/Laurent groups. The serialized flags remain closed deliberately.
See `claim-map.md` for precisely what can be reused and what remains open.

## Public-source adaptation

The mathematical code and all 78 emitted seed records are preserved. Private
operational budget fields were removed from public copies, one proof-note
budget phrase was generalized, and its bound SHA-256 was regenerated.
A local-only documentation pointer was replaced by the shipped authenticated
public source notes. The pinned model and source excerpt remain byte-identical.
No mathematical formula, owner, sign, branch, source AST or domain was changed.
The original working files were not modified.

The entire serialized v5 artifact was compared to its source version. Its only
changes were deletion of operational gate fields, replacement of the local
formula-source pointer, and the updated public proof hash. The selected demand
DAG is byte-identical to its source artifact. A hash authenticates bytes, not a
mathematical proof or arithmetic admission.
