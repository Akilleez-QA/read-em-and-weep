> Worker handoff; portable code is under arithmetic/. Physical gates remain false.

Staged in the dedicated directory:

- [Recurrence proof](seed30_partition_proof.md)
- [Source-authenticated contract generator](seed30_partition_demand.py)
- [Generated request contract](seed30_partition_demand.json)
- [Synthetic controls](test_synthetic_demand.py)

Scope: exact seed30 E34 request with all five specified owners. Derives generating-function demand propagation, shared diagonal states, prefix denominator occurrences, and the all-infinity \(B_4=1\) rule.

Pins: release `6e28c6b59f8245779f6c03a20798e4de6842ae19`; source `08b73637d4136f91606aad332c46cafd064417f8`.

Evidence: authenticated public binders and pinned source; two synthetic/metadata controls passed. No physical arithmetic or certificate scans ran.

Gap: exact A02 branch ledger, carrier0 dh clearance, frame shifts, and certified physical supports. All admission gates remain false.

Reviewers **A03/V06**; artifact review pending. Next step: review the recurrence, then attach A02’s complete ledger.