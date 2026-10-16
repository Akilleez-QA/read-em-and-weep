# SPIKE BURN mathematical result intake

Small, offline Python 3 standard-library intake for a batch of 30–40 worker results. No daemon, network, model calls, dependencies, external writes, or execution of submitted commands. JSON output goes to stdout. `null` is mathematical intake; `mr.slop` is a proposed independent reviewer. Naming that role does not assign, authenticate, or accept a review.

## Run

    cd research/hm/null-support-certificates/spike-triage
    python triage.py example.json --context context.example.json
    python triage.py - < example.json
    python -m unittest -v

Exit codes: 0 structurally valid input envelopes, 1 one or more quarantined envelopes, 2 invalid JSON/file/context. Exit 0 is never a mathematical verdict. The context snapshot is optional; without it freshness is explicitly unverified. Context is a trusted operator-supplied snapshot, not fetched or updated by this script.

## Envelope contract (validator is authoritative)

See `example.json` for a complete candidate and `schema.json` for the structural schema.

- `result_id`, `worker_identity`, `claim_id`: nonempty stable identifiers.
- `parent_claim`: nonempty identifier or explicit null.
- `source_commit_hash`: full lowercase 40- or 64-character Git commit hash.
- `input_artifact_hashes`: nonempty mapping of artifact names to SHA-256 hashes.
- `scope`: exact `domain`, `quantifiers`, `restrictions`, `family`, each explicit text. Specify “none” if unrestricted. Free text must still be checked by a mathematical reviewer.
- `scope_relation`: same, narrower, broader, new. Declared broadening always requires review; any scope hash mismatch also requires review even when the producer declares “same”. Semantic equivalence/inclusion cannot be decided here.
- `conclusion_kind`: proved_zero, proven_nonzero, candidate_overlap, counterexample, blocker. These are producer claims.
- `hypotheses`: explicit list of premises; empty means no premises declared.
- `proof_artifacts`, `receipts`: explicit lists of `{path, sha256}` references. Mathematical conclusions require at least one proof/witness artifact. Paths are not opened; hashes are not recomputed.
- `test_commands`: explicit list of reproducible command strings. These are never executed. Nonempty means a submitted next step, not a verified safe or working executable.
- `evidence_kind`: proof, support_overlap_only, computation, none. Support overlap alone cannot justify nonzero.
- `execution_status`: completed, not_run, resource_failure. Resource failure must be reported as blocker and remains undecided.
- `eliminates_family`: boolean; true requires a claimed proved_zero conclusion. Whether the proof covers the whole family is a review obligation.
- `review`: status pending/needs_review/accepted/rejected, reviewer_identity (null until assigned), reviewer_independence boolean, and review_receipt reference (required for accepted). Accepted requires an identity different from the producer and an assertion of independence. This checks declarations only, not actual independence or review quality.
- `changed_claim`, `unresolved_obligation`, `next_discriminating_test`: nonempty text, or explicit “none”.

`context.example.json` gives the snapshot structure: `seen_result_ids` and `current_claims`, keyed by claim ID with `source_commit_hash`, `input_artifact_hashes`, `scope_hash`. Scope hash is SHA-256 of UTF-8 canonical JSON using sorted keys, compact separators, ensure_ascii=False; use `triage.scope_hash(scope)`.

## Queue rules

Deterministic order, with result ID as tie-breaker; no probabilities, invented confidence or risk-priority scores:

1. Correctness conflicts: simultaneous zero and nonzero/counterexample claims with exactly matching claim ID, scope, commit, input hashes and hypotheses. All matching items are escalated, not resolved.
2. Reported independently reviewed family elimination.
3. Candidate overlap with submitted test commands.
4. Review required (includes quarantined envelopes).
5. Unresolved blockers.
6. Archive: stale inputs, duplicate result IDs, identical resubmissions except result ID, rejected review.

Scope changes/broadening downgrade effective review to needs_review. The original review assertion remains visible. Different hypotheses or scope do not automatically conflict: the reviewer must examine broader correctness conflicts. Duplicate detection is within the batch or against seen result IDs; no persistent state is maintained. Proof/review changes are not treated as identical resubmissions. Stale-input items remain in the report as archived work, never silently disappear. Freshness unverified is visible when context is absent.

## Human handoff

Intake checks provenance and scope, then routes the highest-priority unresolved obligation to one worker with one discriminating test. A reviewer independently replays/verifies the exact artifact, premise set and scope, recording a receipt before acceptance. Review broader/narrower domain relationships explicitly. Read every blocker as missing evidence; neither a timeout nor support overlap settles nonvanishing. The tool does not certify truth, authenticate identities or hashes, check proof semantics, execute code, or grant review acceptance.
