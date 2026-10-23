# Reproduce the bounded controls

Run from this directory:

    python3 verify.py
    python3 -O verify.py

Both runs must reproduce RESULT.json exactly. To regenerate the retained result
after an intentional verifier revision, use python3 verify.py --write.

Only the standard library is required. All checks use explicit exceptions, not
assertions, and therefore remain active with optimization. The verifier covers
seven retained input identities, two fixed historical records, twelve universal
height-partition capacities, the equality heights, fixed small representation
identities, residual rank/degree arithmetic, and all five positive sextic-net
syzygy degree pairs. It performs no historical enumeration, parameter sampling,
actual source-instance computation, selected matrix evaluation or rank scan.

PROOF.md supplies the actual geometric arguments and imported scope. Passing
this verifier is not a substitute for checking saturation, actual-map
compatibility, geometric necessity of the original list, or the proof itself.
