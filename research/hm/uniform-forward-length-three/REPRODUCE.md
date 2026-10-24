# Reproduction and evidence boundary

Use standard-library Python 3 from this directory.

```sh
python3 verify.py > /tmp/length-three-normal.json
python3 -O verify.py > /tmp/length-three-optimized.json
cmp RESULT.json /tmp/length-three-normal.json
cmp RESULT.json /tmp/length-three-optimized.json
python3 verify_sources.py
python3 -O verify_sources.py
```

Both author runs must reproduce RESULT.json byte-for-byte, with 391
explicit requirements. Checks use runtime exceptions, not optimization-
disabled assert statements. Every full signed expression for chi(K(4))
is compared, including the negative multiplicities in the middle cases.
The verifier evaluates only abstract representation characters through
Sym^25 W and the displayed fixed degree lists. It does not read or
execute a historical enumerator or any actual-instance data.

The independent current checker and review are in review/. Follow the
commands in the independent review; its implementation must not import
the author's character implementation. Arithmetic agreement is not a
proof of the geometric premises, saturation, or differentiation steps.
Those are covered by PROOF.md and its whole-proof review.

## Retained earlier review

review/retained/ preserves the exact earlier proof, author verifier,
result and independent geometric review. Their original hashes remain
checkable, and the 388-check earlier author result reproduces with:

```sh
python3 review/retained/verify_l3.py > /tmp/length-three-retained.json
python3 -O review/retained/verify_l3.py > /tmp/length-three-retained-optimized.json
cmp review/retained/RESULT-L3.json /tmp/length-three-retained.json
cmp review/retained/RESULT-L3.json /tmp/length-three-retained-optimized.json
```

That earlier review is evidence about its named earlier proof, not a
claim to have reviewed later edits. The current proof adds explicit
foundational premises, expands the dual quotient injections and orbit
argument, and states the shorter dependency bridge relative to current
public coverage. The current author verifier strengthens three V-only
checks to full signed-character comparisons. A fresh independent review
binds the current proof. The current entry points are PROOF.md and
DEPENDENCIES.md, not the retained snapshot's broader provenance list.

All four foundational originals were fetched again at their immutable
public commit/path and compared byte-for-byte with the retained files,
including their Git blob and SHA256 identities. verify_sources.py checks
those identities locally; it does not prove the contents' mathematics or
claim to reconstruct their entire transitive dependency tree.
