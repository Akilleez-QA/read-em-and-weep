# Selected-only reproduction

Copy exactly these seven files, preserving paths, into a newly empty directory:

1. PROOF.md
2. INPUTS.json
3. REPRODUCE.md
4. verify.py
5. characters.py
6. inputs/rankseven-equality.md
7. inputs/nonsplit-quotient.md

Run using only the Python standard library:

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python verify.py
    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python -O verify.py

Both outputs must be identical PASS objects. All conditions use explicit exceptions and remain active under -O. The imported character module also performs 81 fixed exact-rational McKay checks.

The checker authenticates the complete pinned inputs and frozen proof, verifies the fixed finite-group multiplicity-one identity, and checks universal quartic/first-jet degree arithmetic. It does not evaluate actual coefficients, graph scalars, points, jets, tensors, matrices, instance ranks or invariant normalizations. No broad candidate scan, historical enumerator, network request, installation, remote write or large computation is run. Unused character helpers perform no search.

The complete originals are PR1218 at f5895c822322b4ddab07e51a97874d4528fb5b88 and PR1222 at f7abba83fedd46a9d91f5abbd9e40d3b02ae65f1, with full pins in INPUTS.json. PROOF.md is 11,240 bytes, SHA256 08708a646f51fb6b10ef94c1eab1b5e4ee56a775fb8e377d6a92e8d34df54259.

An independent reviewer must read the entire proof and both complete originals, freshly authenticate each by immutable repository path and Git blob, inspect the full checker, and replay only the seven selected files above in an isolated directory. Its entire-proof verdict must bind the exact proof hash, and specifically verify actual sum/intersection, universal saturated quartic kernel, physical multiplicity one, first-jet source convention, nonzero Schur map, canonical HN meaning and coherent image boundaries. Arithmetic replay does not replace the proof.

Result JSONs and reviewer records are publication evidence, not replay inputs. Raw local fetch records, scratch audits, caches and publication manifests are excluded from publication.
