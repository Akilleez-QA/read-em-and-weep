# Selected-only reproduction

Copy exactly these seven files, preserving relative paths, into a newly empty directory:

1. PROOF.md
2. INPUTS.json
3. REPRODUCE.md
4. verify.py
5. characters.py
6. inputs/lifted-jets-and-kernel-two.md
7. inputs/five-kernels.md

Run with the Python standard library:

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python verify.py
    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python -O verify.py

Both outputs must be identical PASS objects. Guards use explicit exceptions and survive optimization. The character module performs 81 fixed exact-rational McKay checks and contains no search.

The frozen proof is 13,289 UTF8 bytes, SHA256 9da994c73b8c5365de31fc8b5552ba364bfc6af624108acdb8567feba9365103. INPUTS.json fixes both complete original paths, immutable commits, UTF8 lengths, SHA256 values and Git blobs: PR1226 at c565bd8b5b65829e99bdd96a7c5f076b01050465 and PR1198 at 7d71f0e2a3963cff64a069198f4415c5cfd0fe9b. Author fresh read-only responses are retained in LOCAL-SOURCE-FETCHES.json but are excluded from publication and replay.

Checks concern only complete input authentication and fixed universal physical representation, degree, rank and exact-sequence arithmetic. The three degree-allowed rank-one image possibilities are the proof's entire fixed local bound, not a kernel-tuple search. No selected actual coefficients, parameters, points, jets, tensors, matrices, graph scalars, invariant normalizations or source-instance ranks are evaluated. There is no large computation, broad scan, package installation, network request or remote write.

A new independent reviewer must read the entire frozen proof, both complete originals and both Python sources; independently fetch both originals through immutable repository path and Git blob; authenticate their exact bytes; and replay only these seven files in a newly empty isolated directory in normal and optimized Python. The entire-proof verdict must bind the exact frozen proof hash. The required geometric audit includes the universal non-composition lemma, saturated rank-two inclusion and quotient line, equivariant Ext vanishing, actual first-jet identification as kernel of the forced cubic row, actual V row, and every zero or f12-divisible deep endpoint row. Arithmetic does not replace geometric proof.

The conclusion excludes only K4 and K5 in the retained residual simultaneous rank-seven k=2 geometry. With PR1226 it leaves K1 and K3, without asserting occurrence or excluding the branch itself. Author result JSONs and reviewer records are publication evidence, not replay inputs. Exclude raw local fetches, scratch audits, caches and the publication manifest itself.
