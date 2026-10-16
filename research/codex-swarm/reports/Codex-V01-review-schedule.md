> Reviewed staging handoff. Portable deliverables and limits are in STATUS.md.

# A06 independent adversarial schedule review

Reviewed schedule_validator.py SHA256264d67358d74c2e3427376171340b37eac58331f9ef68f37903f363dd8311e2f and test_schedule_validator.py SHA256810b374342bc5696ae79d33caea06bcffedb286ccf9717ac2c1e44b9bad22157. Ran producer's12 tiny fictional controls with python-B unittest: all pass. Ran own Codex-V01-review-schedule.py fictional controls; receipt in .json. No producer files changed, no physical inputs/cost certificate/evaluation.

## Accepted exact contract

Accept a pure consistency replay of ONE caller-supplied SYNTHETIC global snapshot, with distinct allocation IDs defined to be independent storage and repeated use of the same ID treated as shared storage. This is not authentication of actual process aliases/global state.

Counters: initial spent plus EVERY remaining reservation must fit the global cap. Planned operation counts must fit each chosen reservation. At begin, debit its remaining counters and increment spent equally, keeping spent+remaining constant. Unused other-worker commitments remain reserved; there is no per-worker cap grant in one replay. Integer validators reject Boolean/unknown/negative costs. No spent-counter refund on free.

Memory: total is live allocation bytes + all concurrently active workspace + max(0,reserved_bytes-backing) for every currently active reservation. Equivalently each reservation contributes the greater of its actual backed live/workspace bytes and its committed bytes, plus unreserved memory. Shared ID counted once; new outputs allocated at begin; charge BEFORE all event end/free actions. This conservatively includes outputs plus input/workspace at the peak. Input-producer completion must precede consumer begin. Exact last-use/end rules and no-free-while-active prevent premature reuse. Unique producers and initial/output checks prevent overwrite under this abstract immutable-input model.

Records reject missing/extra fields and source/evidence modes other than synthetic. All returned actual_source_admitted, arithmetic_admission and execution_release remain false. No blocking replay-arithmetic bug found within this scoped contract.

## Demonstrated limits requiring explicit publication scope

1. No history authentication: validate(fixture) twice returns spent_after5 twice and does not advance caller state. A caller-chosen revision0/spent0/global_complete=true also passes, returning spent_after2. ledger_id/revision are shape-checked only. Thus global_complete is an assumption; no historical no-reset guarantee follows across calls. An external authenticated monotone global ledger is still required for real use.
2. No owner-authorization enforcement: move opA and its output backing to workerB's reservation, preserving the global total; accepted. Owner strings are labels. This cannot be described as verified cross-worker authorization or transfer approval.
3. Byte reservations are commitments, NOT individual capacity ceilings: reservationA bytes1 with actual output5/workspace2 still passes at globally charged peak20. This is sound for the implemented global-byte metric; document it rather than claiming per-reservation byte-overrun rejection. Counts DO have reservation overrun checks.
4. Storage alias semantics are declared by IDs; no external pointer/allocation binding exists. Distinct IDs conservatively count separately; shared IDs count once. Unknown real aliasing or source/cost completeness is not checked.

These controls fail no physical authorization because the validator explicitly refuses physical evidence and always returns admission/release=false. Publishing the generic validator is acceptable with the limited synthetic contract above. candidate_preflight.py remains staging metadata, not an operation-cost, actual-source, peak-RSS or execution certificate. Read back final producer hashes after any changes before citing this review.
