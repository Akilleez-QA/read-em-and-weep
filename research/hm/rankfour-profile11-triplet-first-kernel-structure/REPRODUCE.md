# Selected-only reproduction

Copy exactly these seven files, preserving relative paths, into a newly empty directory:

1. PROOF.md
2. INPUTS.json
3. REPRODUCE.md
4. verify.py
5. characters.py
6. inputs/lifted-jets-and-kernel-two.md
7. inputs/five-kernels.md

Run inside that new directory using only the Python standard library:

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python verify.py
    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python -O verify.py

Both outputs must be identical PASS objects. Every guard uses an explicit exception and survives optimization. The copied character module performs 81 fixed exact-rational McKay consistency checks and contains no search. The verifier requests only the finitely many universal representations and elementary arithmetic explicitly used by the proof; the two scalar-image degrees are the entire degree-allowed bound in Section 2, not a tuple search.

The frozen entire proof is 12,921 UTF8 bytes, SHA256 4869bca9584bfa6876533516b61a6a14d6ca0fde97e80649828588b28e8f617e. INPUTS.json and hard-coded verifier pins identify both complete immutable originals by exact repository path, commit, UTF8 length, SHA256 and Git blob: PR1226 at c565bd8b5b65829e99bdd96a7c5f076b01050465 and PR1198 at 7d71f0e2a3963cff64a069198f4415c5cfd0fe9b. Full author fresh read-only responses are retained in LOCAL-SOURCE-FETCHES.json, excluded from publication and replay.

Checks concern input authentication and fixed universal character, rank, degree and Ext arithmetic only. They do not evaluate any selected actual coefficient, parameter, point, jet, tensor, matrix, graph scalar, invariant normalization or source-instance rank. They involve no broad scan, large computation, package installation, network request or remote write. Arithmetic does not replace geometric proof.

A new independent reviewer must read the entire frozen proof, both complete immutable originals and both Python sources; independently fetch both originals by immutable repository path and Git blob; authenticate the exact bytes; and replay only these seven files in a newly empty isolated directory in both normal and optimized Python. Its entire-proof verdict must bind the exact frozen proof hash. The geometric audit must check the actual fifth-jet complement, the saturated canonical quadratic line and quotient W(3), both component kernels, all extension components, the actual negative-horizontal contradiction in the small ambient, the genuine coherent-image projection used to identify F^-, and every step of the rank-four quotient section argument. It must not replace these with hash or arithmetic success.

The conclusion is conditional on original K1 in the retained residual simultaneous rank-seven k=2 case. It forces F=(D+P)(-6)+O(-10) and F^-=S4(-7)+V_alt(-8)+O(-12), without excluding or realizing K1, K3, the simultaneous case, or any whole branch/profile. The unresolved potentially nonsplit normal extension remains explicit. Author normal/optimized result JSONs and later reviewer records are publication evidence, not replay inputs. Exclude raw fetches, drafts, scratch files, caches and publication manifests from replay.
