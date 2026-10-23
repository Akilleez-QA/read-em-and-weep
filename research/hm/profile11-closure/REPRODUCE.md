# Reproduce the conditional profile11 integration certificate

Use Python3 standard library only, from this directory:

    python3 verify.py > actual.json
    cmp actual.json RESULT.json
    python3 -O verify.py > optimized.json
    cmp optimized.json RESULT.json

Expected: 3,519 explicit controls and 86 rejected invalid mutations, identical output in both modes. These counts include deliberate rejected runs and are regression controls, not counts of geometric lemmas proved.

PROOF.md contains the assumption ledger, exact pinned theorem scopes and complete combination argument. COVERAGE.json is the typed source/pair contract. INPUTS.json authenticates all sixteen retained direct inputs. verify.py hard-locks the immutable input metadata and accepted proof hashes, checks the original frozen partitions, and tests missing-source, missing-pair, altered-signature, corrupt-input and scope-promotion failures. FRESH-AUTHENTICATION.json records the sixteen public Git blob readbacks; the checker also derives every blob from the retained bytes.

No third-party libraries, actual source data, parameter samples, numerical rank computations, historical-enumeration regeneration or model experiments are needed. Acceptance is conditional on the imported written geometric theorems. This is not proof-assistant verification and does not complete the original repair.

## Independent review

From this directory:

    python3 independent/verify_independent.py . > independent-actual.json
    cmp independent-actual.json independent/RESULT.json
    python3 -O independent/verify_independent.py . > independent-optimized.json
    cmp independent-optimized.json independent/RESULT.json

Expected: 1,612 independent controls and 244 rejected mutations. The independent script's default packet path was adapted to this portable layout; its logic and retained results are unchanged. The frozen proof and author verifier are unchanged.
