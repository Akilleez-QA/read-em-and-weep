# Exact five-file selected-only replay

Copy exactly these five files into a newly empty directory, preserving relative paths:

1. PROOF.md
2. INPUTS.json
3. REPRODUCE.md
4. verify.py
5. inputs/top-backward-flag.md

From that directory run with only the Python standard library:

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python verify.py
    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python -O verify.py

Both outputs must be identical PASS objects with 41 checks. Every guard raises an explicit exception, so optimization does not remove it. The only algebra checked is four fixed universal formal Q[t]-module presentations for j=1,2,3,4, exact rational elimination identities, and the displayed rank and degree totals. There is no character helper, source-instance evaluation, actual matrix or evaluated rank, broad enumeration, package installation, network access, or external write during replay.

The entire frozen proof is 8,768 UTF8 bytes, SHA256 55a65f12dc249217cd542f70b9acf9429c8715b810c06044de9b1e3240d358ca.

The sole direct source is the complete PR1232 original at immutable commit 16998561d07a6c69a2529a8a052a7f9c3a510bee, repository path research/hm/rankfour-profile11-triplet-top-backward-flag/PROOF.md. It has 16,724 UTF8 bytes, SHA256 5a9a86e376cce495818f2ffefd0442b0a45e9b249143cf333d48c7ed9d302959, and Git blob 2407aeca994376c073fb4ded46e988bab0c7ca70. The verifier hard-pins this identity and the entire proof independently of INPUTS.json. Complete transitive actual-geometric assumptions remain retained through that source.

The complete author read-only connector response is retained separately in LOCAL-SOURCE-FETCHES.json. It is excluded from publication and replay, as are drafts, caches, scratch notes, author result JSONs and reviewer records. Arithmetic authentication and formal module identities do not replace a geometric review.

A new independent entire-proof reviewer must read the complete frozen proof, the complete immutable original and verify.py. It must independently fetch the original by exact path/ref and by exact Git blob, compare all bytes, and replay exactly the five selected files in a newly empty isolated directory under normal and optimized Python. Its verdict must bind the entire frozen proof hash. In particular audit:

- The exact initial A0=Z1 direct-sum U0 and simple cyclic A1/M1 defect supplied by the actual flag.
- The primitive z-double-prime column and derivation of the initial u-prime relation, rather than an assumed normal form.
- Absorption of an arbitrary unit into the complementary generator, with every derivative of that unit retained afterward.
- The adapted regular basis derived inductively from the actual full intermediate quotient maps and exact backward kernels, with no assumed derivative of A4.
- The triangular differentiated identity including every derivative of a and b_i, and the fact that no step divides by the uniformizer t.
- The reversible universal elimination using only nonzero characteristic-zero integers, which establishes R/(t^j) directly rather than inferring cyclicity from a length.
- Descent from completed arbitrary DVRs, the exact elementary orders, and the distinction between coherent and fiber intersections.
- No inferred global identification of the torsion sheaf's line twist on jD12, no claim about differently indexed mixed sums, no branch exclusion, and no new original higher jets or algebraicity.

No merge or upstream submission is part of this packet.
