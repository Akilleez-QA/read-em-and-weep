# Reproduce the bounded canonical-line checks

Run with Python 3.8 or newer and its standard library only:

    python verify.py > VERIFY.json
    python -O verify.py > VERIFY-OPT.json

Both commands must exit zero and return identical PASS results. All enforcement uses explicit checks raising RuntimeError, never Python assert, so optimized execution retains every check.

The verifier authenticates the entire frozen PROOF.md and three complete immutable originals against hardcoded byte lengths, SHA256 hashes, Git blob IDs, exact commit refs, and paths. INPUTS.json carries the same pins. It then checks a single fixed five-class even character table over Q(sqrt(5)), the few symmetric powers of degrees at most twelve used in the proof, universal rank/degree bookkeeping, and the formal second-transvectant differential identity. Its eleven jet bookkeeping stages are the fixed complete degree-ten system, not a scan of actual source instances.

The proof's geometric assertions, invariant-divisor saturation, diagonal-ideal argument, rational-function solution-space bound, coefficient completeness, and normal-incidence interpretation require reading PROOF.md. The verifier is not a substitute for those arguments and never evaluates an actual HM coefficient, source point, jet, tensor, matrix, relative normalization, or instance rank. It uses no explicit polynomial representative of the universal invariant f12.

For an isolated replay copy exactly these eight files, preserving their relative paths, into a fresh directory:

* PROOF.md
* INPUTS.json
* REPRODUCE.md
* verify.py
* characters.py
* inputs/nine-jets.md
* inputs/defect-capacity.md
* inputs/deep-images.md

Run both commands there, independently of neighboring packets and their cached outputs. Independent source authentication must fetch each full original anew using its exact commit and path, then compare all bytes, SHA256, and Git blob identity; line excerpts and preexisting local copies do not suffice.

PUBLICATION-MANIFEST.json selects the final publication files. LOCAL-*, REVIEWER-LOCAL-*, temporary files, and __pycache__ are never publication material. No command here performs a GitHub write, merge, or upstream submission.
