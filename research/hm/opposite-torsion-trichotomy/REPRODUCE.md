# Reproduction and scope

This package proves a structural theorem using the exact actual-geometric presentation and character from PR934. The only new arithmetic is fixed abstract A5/C5 representation arithmetic, checked by verify.py; that script does not prove the sheaf, orbit or local-extension arguments. Those require the mathematical proof and independent review. No actual HM/source instance is computed.

## Obtain the exact original input

Read INPUTS.json. In a clone of Akilleez-QA/read-em-and-weep with the pinned commit available, extract its raw bytes without editing or newline normalization:

    mkdir -p audit-inputs
    git show 8c9847612b5f575b987cec9c62b72b099d745e44:research/hm/reduced-opposite-pencil/PROOF.md > audit-inputs/PR934.md
    git hash-object audit-inputs/PR934.md
    sha256sum audit-inputs/PR934.md
    wc -c audit-inputs/PR934.md

Expected Git blob: 91dc4bc5c629e7ee3ba2694d2c05a4768b89b7ef.
Expected SHA256: 69e72653c1b7fe6925743c877210f0ee5714b284d9e1d370afd8bff279e4c1d8.
Expected size: 15657 bytes.

Alternatively retrieve the immutable blob URL in INPUTS.json, selecting raw contents, and apply the same three checks. The author independently read that pinned remote text and checked exact equality with the local original. PR934 itself records its immutable geometric dependencies; this package does not re-prove them or replace them with matching dimensions.

## Bounded verification

Run with Python 3:

    python verify.py
    python -O verify.py

Both use explicit RuntimeError checks, not removable assertions. They enumerate six unordered pairs of three fixed induction characters and the tiny fixed lists of representations of dimensions three and four. They check the length budget, complementary presentation dimensions, three allowed global-section characters, six quotient-bundle patterns, and the elementary modular cotangent exclusion. They do not enumerate actual parameter values, source cases, matrices or ranks.

The theorem's existence statements do not select the torsion length, the maximal character pattern, an actual local extension class, or a preferred complementary block. No source/frontier count changes.
