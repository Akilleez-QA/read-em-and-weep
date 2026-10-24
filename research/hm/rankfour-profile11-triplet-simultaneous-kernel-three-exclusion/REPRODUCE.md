# Exact seven-file selected-only replay

Copy exactly these seven files into a newly empty directory, preserving relative paths:

1. PROOF.md
2. INPUTS.json
3. REPRODUCE.md
4. verify.py
5. characters.py
6. inputs/top-normal-extension.md
7. inputs/eighteen-jets.md

From that directory run with only the Python standard library:

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python verify.py
    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python -O verify.py

Both outputs must be identical PASS objects with 51 packet checks and 81 fixed exact-rational physical-W consistency checks. Every guard uses an explicit exception, so no guard disappears under optimization. The checks are complete-source/proof authentication, the finite universal representation identities, rank and degree formulas, invariant-degree bounds, and ordinary Hom inequalities explicitly used in the proof. There is no actual-instance, extension-class, source-parameter, or splitting-tuple search.

The entire frozen proof is 16,183 UTF8 bytes, SHA256 9a164b510ccb9c529d2380c7e9e4880067bde0e86656b82e2c4649e09e5443c2.

The first direct source is the entire PR1231 original at immutable commit 192f771436114029ccbaf0413a5e8f96edb6fce5, repository path research/hm/rankfour-profile11-triplet-top-normal-extension/PROOF.md. It has 16,808 UTF8 bytes, SHA256 074dba0e590290f7b811a848b5fb4910ab6eebe5597f855111b66d5cd5fe71d0, and Git blob 59d734b137e2bfc014a6932ad1844d26a27ac147.

The second direct source is the entire PR1209 original at immutable commit 913892c66403ea57ed1681957ae1b9f8db9e5e15, repository path research/hm/rankfour-profile11-triplet-eighteen-jets/PROOF.md. It has 17,528 UTF8 bytes, SHA256 33a3c8866f072f4aec607c2d6647222ee0031a3f1bbbaef550e58df5075b3dbf, and Git blob 730021d4e97c4c1307a1d3c6c5303e4e9792202d.

The verifier hard-codes these entire-source identities and the entire-proof identity independently of INPUTS.json. Both direct sources retain their complete transitive actual geometry. The argument uses no later cyclic backward-flag theorem, auxiliary full-span theorem, actual lifted auxiliary-jet statement, capacity theorem, or coefficient-span refinement.

The fresh complete author read-only connector responses are retained separately in LOCAL-SOURCE-FETCHES.json. Exclude that file, caches, scratch notes, author result JSONs, manifests, and reviewer records from selected replay. Replay uses no network, package installation, selected actual coefficient, parameter, point, jet, tensor, matrix, normalization, or instance rank. Arithmetic success authenticates the packet and checks its bounded formulas; it is not an entire-proof geometric review.

A new entire-proof reviewer must read the complete frozen proof, both complete immutable direct originals, and both Python files. Independently fetch each original at the exact repository path and commit and by its Git blob, verify the complete bytes, and copy exactly the seven selected files to a newly empty isolated directory before normal and optimized replay. Bind the verdict to the frozen entire-proof SHA256, not a section or a checker result. In particular review:

- The exact shared actual maps, the full coherent beta_K, and the conditional K1/K3 common-top scope from the complete inputs.
- Algebraic inverse lifting only: the H(-2) normal leakage is O-linear and zero by degree; no inverse map is differentiated.
- The actual equality Bhat^-=Chat, the isomorphic coherent projection I->E, and the exact locally free quotient that proves I is saturated in the full normal bundle.
- The actual forward R inside K, and the everywhere isomorphism p:R->B^+ from the exact derivative-image diagram.
- Nonvanishing and saturation of beta_K on R/Bhat via its unique universal Euler Hom space; the exact intersection R intersect K^-=Bhat.
- The two distinct actual quotients Q->O(4): one from p, one from beta_K. They must not be identified merely by type.
- The quotient-based rank-two classification, central parity in the unequal case, and balanced H0(Q(3)) injection into Sym7 W. No selected extension class is used.
- For split Q, nonvanishing of q_beta on the canonical O(4), the actual N/Bhat isomorphism onto A(2), and the regular factorization of beta_N through N/Bhat into (E0/N)(-2).
- The exact normal extension split by beta_N, the cotangent twist, and the resulting forbidden actual quotient E0->O(-10). No quotient connection or horizontal splitting may be assumed.
- For K3, the canonical D(-4) map to Q vanishes; its unique row into W(1) is represented by universal complete quartic evaluation followed by Euler inclusion, with kernel S4(-5). Both zero and nonzero rows contradict top(Bhat)=-6.
- The exact stopping boundary: only original K3 within the retained simultaneous rank-seven k=2, delta=12 case is excluded. K1 remains, with necessary Q=W'(-3), not an occurrence assertion or further exclusion.

No merge, upstream submission, or other repository write is performed by this packet.
