> Reviewed staging handoff. Portable deliverables and limits are in STATUS.md.

Staged [A06-second-wave.md](staging/Codex-A06/A06-second-wave.md), [schedule_validator.py](staging/Codex-A06/schedule_validator.py), and [candidate-preflight.json](staging/Codex-A06/candidate-preflight.json).

Scope: exact A01 seed12 and A02 seed30 `E34(T12F12)` requests, V01 UNKNOWN endpoint records, available A05 metadata, and synthetic global-ledger controls.

Evidence: 14 tests pass normally and under `-O`. Serialized metadata footprints are reported separately from unknown physical bounds. No physical arithmetic or incumbent scan ran.

Pins: release `6e28c6b59f8245779f6c03a20798e4de6842ae19`; source `08b73637d4136f91606aad332c46cafd064417f8`.

Admission remains **FALSE**: actual global state, operation costs, and source/pole proofs are unavailable. Next: V06/I01 review, then authenticated state and cost certificates. **Artifact review pending.**