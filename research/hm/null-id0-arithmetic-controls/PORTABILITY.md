# Portable evidence bundle

## Scope

This bundle is prepared locally for review. It has not been published. It contains no physical inputs, production modules, source/owner/model data, machine-specific paths, or private operational accounting. Its algorithmic meter counts are toy-test evidence.

Supply the inert candidate text separately. The only accepted candidate SHA-256 is:

`0efb8eff9bacacc9cddad9f29a598479c2c6925cf6472e2733ce4d37e841cc1c`

The exact arithmetic extraction AST remains pinned to:

`cfda96f5c5403152853f2ff0952371072e7cd12347fc0b8b20f7e35580ee21a3`

## Portability delta

The independently reviewed original harness is preserved unchanged outside this bundle. Its SHA-256 is `d57cf8fe2e6e84e7af4f411162abea77e79721c3cb67a4e09bf122b094c40682`.

The portable harness makes only these changes:

1. Remove the machine-specific candidate path constant.
2. Pass an explicit candidate path through run_toys(candidate_path) and extract(candidate_path).
3. Require `invented-controls --candidate-path FILE`; missing or malformed arguments exit 2 before reading candidate text.
4. Retain the mode refusal before path handling. `actual_id0` and all other non-invented modes always exit 2, regardless of path arguments.

No candidate-byte pin, extracted-AST pin, extraction selection, allowed dependency, arithmetic check, input, budget, or output JSON is changed. The current bundle hashes are in SHA256SUMS. The candidate file is read only as inert bytes; it is never imported as a module.

REPORT.md corrects the source-location wording: the compiled filename is synthetic; retained AST line/column positions are original. Its reproduction commands use the portable CLI. REVIEW.md is the unchanged independent review of the original harness, not a claim of separate independent review of this portability delta. Its reproduction commands apply to the original CLI.

## Reproduction

Use Python 3.12 (the independent original review used 3.12.14). From this bundle, with FIELD_CANDIDATE.txt supplied separately:

    sha256sum -c SHA256SUMS
    python test_extracted_arithmetic.py invented-controls --candidate-path FIELD_CANDIDATE.txt
    python -O test_extracted_arithmetic.py invented-controls --candidate-path FIELD_CANDIDATE.txt

Both portable runs reproduced all 42 checks and the original output byte-for-byte. The evidence SHA-256 in each case is `55bb2d6f04090a050d79be623a38c21d68aa324a2e440def6585001a0fa26031`.

Expected refusals (exit 2):

    python test_extracted_arithmetic.py actual_id0
    python -O test_extracted_arithmetic.py actual_id0 --candidate-path DOES_NOT_EXIST
    python test_extracted_arithmetic.py invented-controls
    python -O test_extracted_arithmetic.py invented-controls

The second refusal demonstrates that the actual-ID0 mode gate precedes any candidate-path read. Missing-path controls demonstrate the required explicit path. Refusal transcripts are included. Original artifact and independent-review hash manifests were reverified after preparing this bundle; all originals remain unchanged.

## Limits

A path argument supplies bytes for the pinned arithmetic extraction, not permission to run production. Hash mismatch fails before AST parsing. The harness is inspected-code regression evidence, not a hostile-code sandbox. Actual ID0, physical values, production integration, jets and admission remain outside scope.
