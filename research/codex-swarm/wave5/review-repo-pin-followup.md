# Independent repository-pin follow-up to PR87

Accept the narrow repository-provenance repair and FD pin refresh relative to
reviewed snapshot `f65b2d680`. No blocking finding in this delta. This acceptance
concerns repository selection and authenticated snapshot continuity only; it
does not repeat or enlarge the accepted mathematical review.

The original PB/QB/FD `review-independent.md` files remain byte-for-byte
immutable, including their historical hashes and acceptance boundaries. PB and
QB independent tests are unchanged. FD's original independent test changes
only `MARKER_SHA` and `PINS_SHA`, after independent verification below. Its
historical review still describes the original snapshot; this report supplies
acceptance of the follow-up bytes, rather than rewriting that history.

## Verified delta

Inspected `git diff f65b2d680` for PB/QB/FD and the separate wave5 runner delta.
PB has no changes. QB's sole implementation change replaces optional
`QH.authenticate_sources(repo)` with a check that `repo` is None or resolves to
the workspace containing the module, followed by the existing canonical
`authenticate()`. A noncanonical path therefore raises before either QB or QH
authentication. Canonical aliases resolve to the same repository. The unchanged
description path continues to use the canonical constructors and sources.

QB's other changes are the explicit repository constraint in README/PROOF,
one added producer regression test and its mock import, and the corresponding
producer marker hashes, seven-control count, and post-review note. Outside the
constructor guard, `q_binding.py` is byte-identical to the reviewed version;
the new independent test verifies this by exact byte replacement. There is no
symbolic denotation, owner, source formula, coordinate/frame, degree,
coefficient/stream refusal, or physical admission gate change.

FD's `source-pins.json` differs by exactly one SHA256 value: the canonical
`source-faithful-Q/q_binding.py` entry. Its path, scope, other four workspace
inputs, all thirteen immutable dependency records, and all other JSON bytes
are unchanged. FD's marker differs only in the `source-pins.json` digest.
All eleven other FD producer files, including code, proof, descriptors,
contract, tests, receipts and logs, are byte-identical to `f65b2d680`. This is
checked against Git snapshot bytes, not just the producer's current claims.

All three producer markers were independently hashed and all 23 listed file
hashes verified (PB 6, QB 5, FD 12). The new suite captures marker and producer
bytes before its tests and verifies exact equality afterward. Independently
computed SHA256 values:

| Artifact | SHA256 |
| --- | --- |
| PB marker, unchanged | `8150a3a02b529be8398ba857b7e9f3fcd993900be2f14cc6f3a5fe2722169c62` |
| QB marker | `5b9eec260415123bf2f42cc05ec8d569df0fb21d952c06bff23e2a9ba2546b6d` |
| QB implementation | `487a415c2b8fdfae0cfdcbab0e8144c137d0ab5e2c31d2b96bce2fe976210107` |
| FD marker | `31135b2e17f41b67580b1639afafd654ef8e1b5dc4ab87a968a4363d0d3f2c47` |
| FD pins | `09b2f3af2112c8880950d465c89229b9c043c37f81c0f7a1d1ed8ef5529440cc` |

The computed FD marker and pin digests match the supplied candidate strings;
those strings were not used as evidence for authorizing the anchor updates.

## Direct-file verification

Each file below passed with both `python -B FILE` and `python -B -O FILE`,
under `timeout 60s`, from the repository root. No receipt-generating runner was
invoked.

| File beneath `research/codex-swarm/` | Tests per mode |
| --- | ---: |
| `source-faithful-Q/test_binding.py` | 7 |
| `source-faithful-Q/test_independent.py` | 7 |
| `source-domain-application/test_domain.py` | 10 |
| `source-domain-application/test_independent.py` | 13 |
| `source-domain-application/test_pin_followup.py` | 6 |
| Total | 43 |

**86 successful test executions.** The six new controls authenticate all
markers; spy on canonical/None construction (including a resolving alias);
reject noncanonical paths before either authentication entry point; enforce
the exact QB implementation replacement; enforce FD's single-hash pin/marker
delta; and preserve all other tracked lane files, with only the two authorized
FD independent-test anchor substitutions. The existing FD independent suite
also reauthenticates its immutable Git inputs and canonical workspace pins.
The new suite uses 512 MiB address-space and 59 CPU-second limits.

No actual HM coefficients, physical polynomial evaluation, actual fiber
enumeration, broad scan, mathematical re-review, resource admission, commit,
push, or Git post was performed. Existing bounded tests retain their
coefficient-free metadata and explicitly artificial controls. The original
source, frame, symbolic-domain, fresh-primitive and execution boundaries remain
those of the original independent reports.

Only the authorized FD independent-test anchors, new
`source-domain-application/test_pin_followup.py`, and this report were written.
The pre-existing `wave5/run_controls.py` changes and untracked wave5
receipts/logs were left untouched and are outside this acceptance.
