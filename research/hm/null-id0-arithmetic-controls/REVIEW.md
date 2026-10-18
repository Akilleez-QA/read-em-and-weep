# Independent review: extracted shared-certificate arithmetic controls

## Verdict

PASS within the stated isolated, invented-input scope. The existing harness was inspected before execution. Its 42 named checks reproduce byte-for-byte against the supplied evidence in Python 3.12.14, both normally and with `-O`. The CLI refusal also reproduces in both modes with exit code 2. This closes a narrow runtime-evidence gap for the retained candidate arithmetic bodies, not the production or physical ID0 execution gap.

No candidate module was imported, no patch was applied, and no source, model, owner, jet, physical route, or actual ID0 computation was executed during this review. Candidate text was read and parsed inertly; only the harness's selected arithmetic AST was executed on its invented controls.

## Integrity and extraction

- Candidate SHA-256 independently verified: `0efb8eff9bacacc9cddad9f29a598479c2c6925cf6472e2733ce4d37e841cc1c`.
- Independently reconstructed extraction AST SHA-256: `cfda96f5c5403152853f2ff0952371072e7cd12347fc0b8b20f7e35580ee21a3`.
- All six entries in the original `SHA256SUMS` verify, including the harness and report.
- The harness verifies the candidate bytes before parsing and the extraction hash before executing. It selects the twelve named definitions and the `ZERO` and `_LAURENT_SEAL` assignments. Only five `Execution` methods are removed: `element`, `scalar`, `x`, `y`, and `curve`. `Element` and `UnsupportedInverse` are excluded.
- Retained method/function bodies, decorators, annotations, descriptors, class slots, and algorithmic checks are unchanged. The module docstring and original imports are not executed. The three original imports are checked textually and their stdlib objects are supplied explicitly.
- The recursive symbol-table check restricts referenced globals to an explicit allowlist, and the selected AST contains no imports. Inspection found no call from the retained arithmetic closure to any omitted method; an independent AST scan likewise found no references to the five removed attribute names.
- Removing those methods therefore does not change the exercised exact-type arithmetic paths. It does change the class API and cannot establish full-module, subclass, introspection, import, or integration equivalence. Class identities and the seal are fresh objects in a separate namespace.

The global-name allowlist is not a security sandbox: attribute access and supplied Python objects are not a transitive capability proof. The original report appropriately limits the harness to inspected code and ordinary invented inputs, rather than hostile Python objects or arbitrary code.

## Runtime evidence

The reproduced output contains 42 distinct named checks: 16 initial arithmetic/identity/immutability controls, 24 poison controls across four cap categories, and two naturally exhausted certification-step-budget controls. These are named checks in one deterministic script, not 42 independent exhaustive test suites.

The evidence supports:

- Full residual division and retained quotient/shift for the selected cancellable rational, with coefficients 7, 5, 3, and 0 at the selected powers.
- A 1:2:1 weighted result of 20, with three additional product-meter events. Static inspection confirms weighted reads use the stored quotient without calling division; the meter observation is corroborating evidence for this toy.
- Exact rational/context/execution identity checks on the tested paths, rejection of an unsealed constructor call, and ordinary frozen-dataclass assignment rejection.
- Nonzero-remainder rejection even when the requested legacy coefficient is out of support; continued long division after an irreducible leading term; and canonical-zero behavior.
- Poison persistence across the specified old/new object operations after product, storage, step, and bit-height triggers. Three counter caps are forced directly through `tick`, bit height through `observe`; only the final step-budget example demonstrates natural budget exhaustion during certification. This does not establish naturally reached exhaustion for every cap in every algorithm.

There are no `assert` statements in either the harness or candidate. `require` explicitly raises `RuntimeError`; missing expected exceptions also raise. Normal and optimized reproduced JSON are byte-identical to each other and to the original evidence, so `-O` did not remove these checks.

## Refusal and guard

The `__main__` branch checks the argument before calling `run_toys()` or `extract()`. Every argument configuration except the single `invented-controls` argument exits with code 2. Both reproduced `actual_id0` runs print the refusal and return 2. This establishes refusal before candidate reading/extraction by this CLI flow; stdlib harness imports occur earlier.

The guard is a CLI scope restriction, not an access-control boundary. Importing or editing the harness could expose its functions; the reviewed file itself contains no actual-ID0 implementation. Nothing here establishes the behavior of an unrelated production admission gate.

## Exact gap closed and limits

The added evidence shows that the hash-pinned, extracted polynomial/rational/certificate closure can execute these invented controls successfully, including shared-certificate reuse and aggregate-lifetime failure checks, rather than being supported solely by static inspection or separately reimplemented arithmetic.

It does not establish production importability, execution of the complete candidate module, integration with field elements, derivations or jets, actual terminal-input correctness, physical source validity, owner matching, model/source evaluation, actual ID0 value, production admission, or resource adequacy. No performance, physical memory, wall-clock bound, adversarial-input robustness, cryptographic authentication, durable certification, or introspection-resistant unforgeability conclusion follows. Other inputs and untested retained methods remain outside this regression evidence.

## Minor report correction

The report says class/function source locations are synthetic. More precisely, the compiled filename is synthetic, while retained AST line/column locations remain those of the original candidate. `ast.fix_missing_locations` does not replace existing locations. This wording issue does not affect the arithmetic result or the attribute-free AST hash.

## Reproduction

From the controls directory:

```sh
sha256sum -c SHA256SUMS
python test_extracted_arithmetic.py invented-controls > review/reproduced-normal.json
python -O test_extracted_arithmetic.py invented-controls > review/reproduced-optimized.json
cmp evidence-normal.json review/reproduced-normal.json
cmp review/reproduced-normal.json review/reproduced-optimized.json
python test_extracted_arithmetic.py actual_id0
python -O test_extracted_arithmetic.py actual_id0
```

The last two commands are expected refusals with exit code 2; they must not be treated as successful physical runs. Reviewed outputs are preserved beside this review, including refusal transcripts and an independent static-audit summary.
