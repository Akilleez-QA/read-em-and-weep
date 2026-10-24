# Exact six-file selected-only replay

Copy exactly these six files into a newly empty directory, preserving relative paths:

1. PROOF.md
2. INPUTS.json
3. REPRODUCE.md
4. verify.py
5. characters.py
6. inputs/top-normal-extension.md

From that new directory run with only the Python standard library:

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python verify.py
    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python -O verify.py

Both outputs must be identical PASS objects with 47 packet checks and 81 fixed exact-rational physical-W consistency checks. Every guard uses an explicit exception, so none disappears under optimization. Only the finite universal identities, ranks, degrees, divisor-degree bounds and ordinary Ext arithmetic explicitly used in the proof are checked. No actual-instance or splitting-tuple search occurs.

The entire frozen proof is 16,724 UTF8 bytes, SHA256 5a9a86e376cce495818f2ffefd0442b0a45e9b249143cf333d48c7ed9d302959.

The only direct source is the entire PR1231 original at immutable commit 192f771436114029ccbaf0413a5e8f96edb6fce5, repository path research/hm/rankfour-profile11-triplet-top-normal-extension/PROOF.md. It has 16,808 UTF8 bytes, SHA256 074dba0e590290f7b811a848b5fb4910ab6eebe5597f855111b66d5cd5fe71d0, and Git blob 59d734b137e2bfc014a6932ad1844d26a27ac147. The verifier hard-codes this entire-source identity and the entire-proof identity independently of INPUTS.json. The direct source retains the complete transitive actual geometry; this proof explicitly re-proves the rank-one coherent capacity bound and does not use the optional auxiliary full-span theorem.

The fresh complete author read-only connector response is retained separately in LOCAL-SOURCE-FETCHES.json. Exclude it, drafts, caches, scratch notes, author result JSONs and reviewer records from selected replay. Replay uses no network, package installation, selected actual coefficient, parameter, point, jet, tensor, matrix, normalization, or instance rank. Arithmetic success authenticates and checks the stated bounded formulas; it is not a geometric review.

A new entire-proof reviewer must read the complete frozen proof, the complete immutable direct original, and both Python files. It must independently fetch the original at the exact repository path and commit and by its Git blob; verify the exact complete bytes; and copy exactly the six selected files to a newly empty isolated directory before normal and optimized replay. Its verdict must bind the frozen entire-proof SHA256, not just a section or a checker result. Specifically review:

- Actual Z4 intersection C=Z3, and each of the three saturated Euler quotient identifications.
- The explicit rank-one coherent backward-capacity proof, including termination by negative horizontality.
- The complementary degree-six and degree-seven rows: nonvanishing, lack of invariant base divisors, exact kernel types, and full coherent normal images.
- Every section step determining the V_alt-row kernel, including twist-nine nonvanishing and the rank-two section budget.
- Actual U2 subset C, U1 subset R5, U0 subset R3, and identification of U0 with the scalar tail by the exact equivariant graph Hom vanishing.
- Both terminal Hom vanishings and O-linearity of the actual U0 normal derivative; no inverse bundle connection or horizontal splitting may be assumed.
- The coherent inverse-image equality, sheaf-injectivity of the f12 row, actual terminal kernel, and precise cyclic torsion sheaf O_D12(-6).
- Distinction between saturated forward spans and the unsaturated coherent mixed sums, including their ranks, degrees, support, and no unsupported later elementary-divisor claim.
- The conditional boundary: this is a full actual backward-flag and terminal-defect theorem, not an exclusion, realization, new original higher-jet theorem, or algebraicity claim.

No merge, upstream submission, or other repository write is performed by this packet.
