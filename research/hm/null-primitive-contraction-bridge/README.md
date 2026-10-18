# Conditional primitive contraction bridge

This self-contained bundle proves a decoder theorem and a three-premise contraction reduction. The pinned evaluation map and all six H1-eta zero identities are verified by literal record inspection. Six cleared resolution identities A_pol and the common complex identity C_pol remain unevaluated.

Read PROOF.md and review/REVIEW.md for the exact theorem and independent review. The proof is conditional on exact scalar semantics and stated localization. It is not an ID0 certificate and does not authorize physical polynomial products or removal of any execution guard.

## Run the safe controls

From this directory:

    python check.py
    python -O check.py --source-root inputs
    python test_controls.py
    sha256sum -c SHA256SUMS

Only Python's standard library is used. The checker parses source text and JSON records, checks literal metadata, reduces invented formal words and checks tiny invented matrix countermodels. It never imports or executes any input file. In particular, do not execute the historical SymPy checker preserved as inert text.

The normal and optimized reports in logs/ are identical. The negative pin control runs the portable checker under -O against an altered copy of the model and requires rejection at the immutable-hash boundary, before model parsing. The formal reducer uses QU block consequences supplied by the prose determinant/adjugate argument; it does not mechanize that argument or evaluate A_pol/C_pol.

## Input paths and immutable source identity

All five public source inputs are included under inputs/. pins.json contains repository paths, commit IDs, source URLs and immutable SHA-256 hashes; the historical checker also has its Git blob SHA-1.

The default source root is inputs/ beside check.py, independent of the shell's working directory. To use another directory containing the five filenames from pins.json:

    python check.py --source-root /path/to/input-directory

Individual overrides may be combined with a source root:

    python check.py --raw-engine /path/to/raw_engine.py --model /path/to/model.json

Other flags are --source-formulas, --first-order and --historical-checker. Input overrides do not bypass digest verification. A different version or different serialization requires a separate reviewed artifact; modifying pins to make an input pass invalidates this pinned result.

The historical checker omits explicit checks of ev delta and delta gamma. This observation is confined to that pinned file and the displayed first-order list; it does not assert that no proof exists elsewhere in the project.

All checksums use paths relative to this bundle. Nothing in this bundle publishes files or changes production code.
