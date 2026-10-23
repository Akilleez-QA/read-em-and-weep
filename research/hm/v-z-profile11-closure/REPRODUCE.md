# Reproduce the V/Z profile-(1,1) closure

Python 3 standard library only. From this directory:

    python3 verify.py > /tmp/vz-result.json
    cmp RESULT.json /tmp/vz-result.json
    python3 -O verify.py > /tmp/vz-optimized.json
    cmp RESULT.json /tmp/vz-optimized.json

Expected: 1135 explicit checks, 81 character controls; each source has 34 compatible frozen records partitioned 16 cubic, 7 quartic, 11 capacity, with zero survivors. All 159 source-compatibility flags are independently recomputed for each source from the 21 specified twists.

INPUTS.json pins eight public originals. Each byte length, SHA256 and Git blob SHA1 is verified. No network, dependencies, historical enumeration regeneration, actual-instance computations, or external state writes are needed. PROOF.md states the exact source-conditioned theorem and its geometric dependencies. RESULT.json is generated deterministic arithmetic evidence, not a standalone geometric completeness assertion.

## Independent verification

The independent review and class-character implementation are in `independent/`. From this packet directory:

    python3 independent/independent_check.py > independent/check-normal.json
    python3 -O independent/independent_check.py > independent/check-optimized.json
    cmp independent/RESULT.json independent/check-normal.json
    cmp independent/check-normal.json independent/check-optimized.json
    python3 independent/compare_packet.py

Expected: 5,248 controls, matching partitions and all eight source authentications. Temporary check outputs are not committed. The independent comparison uses the parent packet directory; the mathematical proof and authored checker are unchanged from the hash-bound review.
