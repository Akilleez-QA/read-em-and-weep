# High School Diploma review of PR #42

Pinned head: `540e3d9266a7683722fa249393e72e88770a5c9c` on `research/hm-current-scalar-evaluator`.

This review checks two gates and keeps the evidence classes apart. It does not replay a supplied quotient file, and it does not run the published evaluator's polynomial arithmetic.

## Source regeneration

The current-L numerator was regenerated and matched `0254c93650e6ca6c1e9cbbb01810704eede98d10d0b75229fcff5d8fa2123e66`. Axis 0 was then regenerated. Pair 01, the input for roles 0123, matched the published byte pins:

- compact `c4aec8ed71a940cf30dfb5d12b04cb1db25e5e4e9cc74f4eafa452b2bb1aef5a`
- clearing `c49aaace6483558e6afcbdb2085d5bfd03d50fff3502fb683509552dbd78dc3a`

That is source regeneration only. It is not a quotient result.

## Independent quotient arithmetic

`independent_quotient.py` (`8306039649cb560ffbba38178173fc992f3abcd789fad1d0c7d583457895323f`) evaluates roles 0123 in `Q[v,w,z]/(v^6,w^37,z^22)` with its own sparse integer arithmetic. It does not import the published evaluator, packed product, or Fraction oracle. The comparison target is the published coefficient digest in `expected.json`, not a replay of a `quotient.json` artifact.

Result, recorded in `edge-0123-receipt.json`: the integer coefficient SHA-256 is `8e91a22e9aa6de274f606dfa3fc27d332edc95fc68b8cf5f702392de37cf904d`. The common representation denominator, recorded separately as `commonDenominator`, is 64, and there are 16 nonzero coefficients. `leastDenominatorRows` stores each of those coefficients in lowest terms. Those least denominators divide 64 and are not all 64; the set is {1, 2, 4, 8, 16, 32, 64}, and the least common multiple of that set is still 64. For example, 600/64 reduces to 75/8 because gcd(600, 64) = 8, and 15432000/64 reduces to 241125/1. The coefficient digest hashes the numerators over the common denominator 64, not the reduced denominators. This gate is reproduced. The other 23 role permutations were not evaluated.

## JSON resume guards

`test_resume_guards.py` (`506e0e6271c84d738e04c0296aafd3c15096043ebb75f38d06c5faac26d76d8c`) feeds crafted inputs to the published loader and to `evaluate()` after replacing its multiply, power, and shift functions with raisers. Receipt: `guard-receipt.json`.

Reproduced rejections, before any quotient product:

- corrupt JSON, including a noncanonical integer and the wrong schema
- truncated JSON and truncated UTF-8
- mismatched compact byte pin, mismatched clearing byte pin, and a checkpoint whose input or arithmetic pin does not match the live contract

Missing hypothesis, not a contradicted claim: a schema-valid checkpoint with the live contract, the recomputed frontier, and a tampered leaf coefficient is not rejected. The resume guard binds the checkpoint to the configuration, program, and input hashes. It does not bind the intermediate numerator table. Frontier and contract pins alone do not certify checkpoint coefficient contents. The separate historical-hash validator is outside that guard.

## Not claimed

No geometric source attribution, pole bound, or full-obstruction statement follows from the coefficient match. No supplied-quotient replay was performed, so the published wrapper timings and memory figures were not remeasured.
