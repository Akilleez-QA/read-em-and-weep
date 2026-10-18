# Differentiated stage-two HPL transfer

The proof gives an exact conditional decomposition of the differentiated inner stage-two word into a scalar Čech boundary and explicit nonclosed-input, cohomology-connection and differential-variation terms. Both input degrees two and three are covered without assuming closure. Varying row differential, ambient restrictions, selector and input are accounted for explicitly.

## Read and reproduce

- `PROOF.md`: mathematical derivation and precise scope.
- `REVIEW.md`: independent mathematical audit of the accepted proof.
- `dependencies/`: bounded prerequisite proof excerpts and inherited provenance metadata.
- `pins.json`: exact bundled proof/excerpt hashes and source-selection descriptions.
- `check.py`: small standalone formal-word controls; Python standard library only.
- `results/`: saved normal and optimized results.

Run from any working directory:

    python -B /path/to/this/package/check.py
    python -BO /path/to/this/package/check.py

The checker uses explicit runtime failures, not removable assertions. It reads only its bundled pins and authenticated inputs, never imports a production module, never requests network access, and writes its report only to standard output.

## What the executable controls establish

The checker independently expands both sides of the stage-one and stage-two derivative formulas in a small invented noncommutative word algebra. It applies declared contraction/projection/commutation rules with internal-degree support and checks exact cancellation. It separately checks the varying-row-differential compatibility formula, degree-two/three arities, and six term-removal/sign mutations. A mutation's nonzero reduced word residual demonstrates discrimination by these controls, not an evaluated geometric counterexample or a complete decision procedure for the algebra.

The supplied formulas for H′ and j′ are mathematical inputs derived in the written proof. The checker does not mechanically prove their derivation, the actual normalization of the geometric contraction, general HPL, the implementation denotation, or any upstream geometric premise. The mathematical review supplies the audit of those derivations, conditional on the stated premises. It was completed separately before the bounded executable controls were added; no separate executable-checker audit is claimed.

Two small controls use invented scalar/basis symbols: differentiation of t^−1 for an abstract acyclic complex, and the formal e12/e11 row-transport identity for g=diag(t,1). These are not actual physical matrices, model coordinates, owners, sources or jets. The row-transport example has H=0, so it checks nonzero Δ′ with fixed ambient δ, not a nonzero stage-two output.

## Boundaries and provenance

All contraction identities must hold as coefficient-family identities in one admitted localization. The same original-resolution frame, degree-zero cohomology support, transport-compatible selector and valid input domains remain premises. The new boundary has no new global pole/domain certificate. The theorem does not erase outer weights, imply cancellation of the complete remainder, establish a trace/detector value, or decide a global obstruction.

Prerequisite excerpts are selected from already supplied public packets; their full-document hashes and exact selections are recorded. Nested provenance metadata describes upstream material and does not imply those external files are included or freshly checked. No current-branch or fresh remote-source attestation is made. The portable proof differs from the independently audited author version only by rewriting two prerequisite paths to bundled relative paths; both hashes are retained in `pins.json` and the review.
