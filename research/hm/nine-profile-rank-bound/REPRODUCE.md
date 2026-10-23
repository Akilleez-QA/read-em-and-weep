# Reproduce the new finite implication certificate

Use Python3's standard library only.

    python3 verify.py > actual.json
    cmp actual.json RESULT.json
    python3 -O verify.py > optimized.json
    cmp optimized.json RESULT.json

The verifier checks52 immutable source originals, their byte/SHA256/Git-blob identities, the frozen imported-scope registry, actual physical/ambient conventions, all nine ordered profiles, lower-rank support, all four source32 alternatives and both P pairing branches, and the exact generic square consequence. It includes exhaustive single-field corruption/deletion controls and input/pin/missing-source controls. No repository verifier is imported or executed, no historical record enumeration is regenerated, and no actual-instance coefficient or rank is evaluated.

The trust boundary is explicit: source authentication is not a proof of source mathematics. This certificate checks a finite implication contract conditional on the imported mathematical theorems with their inherited hypotheses. PROOF.md gives the geometric combination, not an unconditional original repair or proof-assistant certificate. REGISTRY.json fixes precisely which imported theorem scopes the contract may use, and its SHA256 is fixed in verify.py.

The source graph includes complete22 and31 coverage chains rather than their terminal files alone. Additional retained source originals document inherited actual foundations. Their full public URLs appear in INPUTS.json.
